"""
Core orchestration engine executing akstack commands and workflows.
"""

import datetime
import os
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from .graph import DependencyGraph
from .models import Gate, ProjectPlan, Task, TaskStatus, TaskType
from .parser import MarkdownParser


class OrchestratorEngine:
    """Core execution engine for managing tasks, verification, and git synchronization."""

    def __init__(self, workspace_root: Optional[Path] = None):
        self.workspace_root = workspace_root or Path.cwd()
        self.todos_file = self.workspace_root / "ToDos.md"
        self.plan_file = self.workspace_root / "plan.md"
        self.progress_file = self.workspace_root / "PROGRESS.md"
        self.agents_dir = self.workspace_root / "agents"
        self.phases_dir = self.workspace_root / "phases"
        self.templates_dir = self.workspace_root / "templates"

    def load_tasks(self) -> List[Task]:
        """Load and parse all tasks from ToDos.md."""
        target_file = self.todos_file
        if not target_file.exists():
            # Fallback to template if ToDos.md hasn't been instantiated yet
            template_file = self.templates_dir / "ToDos.template.md"
            if template_file.exists():
                target_file = template_file
            else:
                return []
        content = target_file.read_text(encoding="utf-8")
        return MarkdownParser.parse_todos(content)

    def load_plan(self) -> Optional[ProjectPlan]:
        """Load and parse plan.md."""
        target_file = self.plan_file
        if not target_file.exists():
            template_file = self.templates_dir / "plan.template.md"
            if template_file.exists():
                target_file = template_file
            else:
                return None
        content = target_file.read_text(encoding="utf-8")
        return MarkdownParser.parse_plan(content)

    def get_status(self) -> Dict[str, Any]:
        """Compute full health and progress metrics for the current project."""
        tasks = self.load_tasks()
        plan = self.load_plan()

        by_status = {
            TaskStatus.PENDING: 0,
            TaskStatus.IN_PROGRESS: 0,
            TaskStatus.COMPLETED: 0,
            TaskStatus.BLOCKED: 0,
        }
        by_phase: Dict[int, Dict[str, int]] = {}
        blocked_tasks: List[Task] = []
        in_progress_tasks: List[Task] = []

        for task in tasks:
            by_status[task.status] += 1
            if task.phase not in by_phase:
                by_phase[task.phase] = {"total": 0, "completed": 0, "blocked": 0, "in_progress": 0}
            by_phase[task.phase]["total"] += 1
            if task.status == TaskStatus.COMPLETED:
                by_phase[task.phase]["completed"] += 1
            elif task.status == TaskStatus.BLOCKED:
                by_phase[task.phase]["blocked"] += 1
                blocked_tasks.append(task)
            elif task.status == TaskStatus.IN_PROGRESS:
                by_phase[task.phase]["in_progress"] += 1
                in_progress_tasks.append(task)

        # Detect active phase (first phase with incomplete tasks)
        active_phase = 1
        for p in sorted(by_phase.keys()):
            stats = by_phase[p]
            if stats["completed"] < stats["total"]:
                active_phase = p
                break

        graph = DependencyGraph(tasks)
        cycles = graph.detect_cycles()
        runnable = graph.get_runnable_tasks(phase=active_phase)

        return {
            "project_name": plan.project_name if plan else "Unknown Project",
            "track": plan.track if plan else "Product/Web",
            "total_tasks": len(tasks),
            "completed_tasks": by_status[TaskStatus.COMPLETED],
            "pending_tasks": by_status[TaskStatus.PENDING],
            "in_progress_tasks": in_progress_tasks,
            "blocked_tasks": blocked_tasks,
            "by_status": by_status,
            "by_phase": by_phase,
            "active_phase": active_phase,
            "runnable_count": len(runnable),
            "next_task": runnable[0] if runnable else None,
            "has_cycles": bool(cycles),
            "cycles": cycles,
        }

    def get_next(self, phase: Optional[int] = None, parallel: bool = False) -> List[List[Task]]:
        """Find next runnable tasks scheduled into conflict-free parallel waves."""
        tasks = self.load_tasks()
        graph = DependencyGraph(tasks)
        runnable = graph.get_runnable_tasks(phase=phase)
        if not runnable:
            return []
        if not parallel:
            # Sequential mode: return one task at a time
            return [[runnable[0]]]
        return graph.schedule_parallel_waves(runnable)

    def start_task(self, task_id: str) -> Tuple[bool, str]:
        """Mark task as IN_PROGRESS (- [~]) in ToDos.md."""
        if not self.todos_file.exists():
            return False, "ToDos.md does not exist. Run init first."
        content = self.todos_file.read_text(encoding="utf-8")
        new_content, updated = MarkdownParser.update_task_status(content, task_id, TaskStatus.IN_PROGRESS)
        if not updated:
            return False, f"Task {task_id} not found in ToDos.md."
        self.todos_file.write_text(new_content, encoding="utf-8")
        return True, f"Task {task_id} status updated to IN_PROGRESS (- [~])."

    def complete_task(
        self,
        task_id: str,
        run_verify: bool = True,
        git_commit: bool = True,
        verification_notes: str = ""
    ) -> Tuple[bool, str]:
        """
        Run verification command (if enabled), mark task COMPLETED (- [x]),
        append entry to PROGRESS.md, and optionally create a git commit.
        """
        if not self.todos_file.exists():
            return False, "ToDos.md does not exist."

        tasks = self.load_tasks()
        task = next((t for t in tasks if t.id == task_id), None)
        if not task:
            return False, f"Task {task_id} not found."

        # Run verification command if requested
        verify_output = "Manual verification or skip flag specified."
        if run_verify and task.verify and task.verify not in ("—", "-", "manual review", ""):
            try:
                res = subprocess.run(
                    task.verify,
                    cwd=str(self.workspace_root),
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=300
                )
                if res.returncode != 0:
                    error_detail = (res.stderr or res.stdout).strip()
                    return False, f"Verification command failed (exit code {res.returncode}):\n{error_detail}"
                verify_output = f"Command `{task.verify}` passed (exit code 0)."
            except Exception as e:
                return False, f"Verification execution error: {str(e)}"

        # Update ToDos.md
        content = self.todos_file.read_text(encoding="utf-8")
        new_content, updated = MarkdownParser.update_task_status(content, task_id, TaskStatus.COMPLETED)
        if not updated:
            return False, f"Failed to update task {task_id} in ToDos.md."
        self.todos_file.write_text(new_content, encoding="utf-8")

        # Append to PROGRESS.md
        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        progress_entry = (
            f"\n### {date_str} — {task.id}: {task.title}\n"
            f"**Owner:** {task.owner}\n"
            f"**Changed:** {', '.join(task.files) if task.files else 'Task files'}\n"
            f"**Verified:** {verification_notes or verify_output}\n"
            f"**Status:** COMPLETED\n"
        )
        if self.progress_file.exists():
            with open(self.progress_file, "a", encoding="utf-8") as f:
                f.write(progress_entry)

        # Commit to Git
        if git_commit:
            try:
                subprocess.run(["git", "add", "."], cwd=str(self.workspace_root), check=True)
                commit_msg = f"{task.id}: {task.title}"
                subprocess.run(["git", "commit", "-m", commit_msg], cwd=str(self.workspace_root), check=True)
            except Exception as e:
                return True, f"Task {task_id} marked complete, but git commit failed: {str(e)}"

        return True, f"Task {task_id} completed successfully and committed."

    def fail_task(self, task_id: str, error_msg: str) -> Tuple[bool, str]:
        """Mark a task as BLOCKED (- [!]) and log diagnosis to PROGRESS.md."""
        if not self.todos_file.exists():
            return False, "ToDos.md does not exist."

        content = self.todos_file.read_text(encoding="utf-8")
        new_content, updated = MarkdownParser.update_task_status(content, task_id, TaskStatus.BLOCKED)
        if not updated:
            return False, f"Task {task_id} not found."
        self.todos_file.write_text(new_content, encoding="utf-8")

        # Append failure to PROGRESS.md
        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        entry = (
            f"\n### {date_str} — BLOCKED: {task_id}\n"
            f"**Error:** {error_msg}\n"
            f"**Diagnosis:** Task failed verification; execution halted on dependent tasks.\n"
        )
        if self.progress_file.exists():
            with open(self.progress_file, "a", encoding="utf-8") as f:
                f.write(entry)

        return True, f"Task {task_id} marked as BLOCKED (- [!]). Error logged to PROGRESS.md."

    def run_gate(self, gate_id: str) -> Tuple[bool, str]:
        """
        Check gate status and preconditions.
        Ensures all tasks in that phase are COMPLETED before the gate can pass.
        """
        tasks = self.load_tasks()
        phase_m = re.match(r"P(\d+)-", gate_id)
        phase = int(phase_m.group(1)) if phase_m else 5

        # Check all non-gate tasks in that phase
        pending = [t for t in tasks if t.phase == phase and t.task_type != TaskType.GATE and t.status != TaskStatus.COMPLETED]
        if pending:
            return False, f"Gate {gate_id} cannot pass: {len(pending)} tasks in Phase {phase} are still incomplete (e.g. {pending[0].id})."

        # Mark gate as completed in ToDos.md
        content = self.todos_file.read_text(encoding="utf-8")
        new_content, updated = MarkdownParser.update_task_status(content, gate_id, TaskStatus.COMPLETED)
        if not updated:
            return False, f"Gate {gate_id} not found in ToDos.md."
        self.todos_file.write_text(new_content, encoding="utf-8")

        # Record in PROGRESS.md
        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        entry = (
            f"\n### {date_str} — GATE PASSED: {gate_id}\n"
            f"**Phase:** {phase}\n"
            f"**Status:** Cleared all gate preconditions.\n"
        )
        if self.progress_file.exists():
            with open(self.progress_file, "a", encoding="utf-8") as f:
                f.write(entry)

        return True, f"Gate {gate_id} passed successfully."

    def lint(self) -> List[str]:
        """Validate structural integrity of all akstack documents, agents, and tasks."""
        errors: List[str] = []
        tasks = self.load_tasks()

        # Check unique task IDs
        seen_ids: Set[str] = set()
        for t in tasks:
            if t.id in seen_ids:
                errors.append(f"Duplicate task ID found: {t.id}")
            seen_ids.add(t.id)

        # Check dependencies exist
        for t in tasks:
            for dep in t.deps:
                if dep not in seen_ids and not dep.startswith("{{"):
                    errors.append(f"Task {t.id} references non-existent dependency: {dep}")

        # Check cycle detection
        graph = DependencyGraph(tasks)
        cycle = graph.detect_cycles()
        if cycle:
            errors.append(f"Circular dependency detected in tasks: {' -> '.join(cycle)}")

        # Check all agent role briefs exist in agents/
        if self.agents_dir.exists():
            agent_files = {f.stem for f in self.agents_dir.glob("*.md")}
            for t in tasks:
                if t.owner and t.owner not in agent_files and not t.owner.startswith("<") and not t.owner.startswith("{{"):
                    errors.append(f"Task {t.id} references undefined agent owner: '{t.owner}' (no agents/{t.owner}.md)")

            # Validate agent frontmatters
            for agent_file in self.agents_dir.glob("*.md"):
                if agent_file.name == "TEAM.md":
                    continue
                content = agent_file.read_text(encoding="utf-8")
                if not (content.startswith("---") and "name:" in content and "description:" in content):
                    errors.append(f"Agent brief {agent_file.name} missing valid YAML frontmatter (name, description).")

        return errors

    def init_project(self, project_name: str, track: str = "Product/Web") -> Tuple[bool, str]:
        """Bootstrap a new project from akstack templates."""
        if not self.templates_dir.exists():
            return False, "templates/ directory missing."

        plan_tpl = self.templates_dir / "plan.template.md"
        todos_tpl = self.templates_dir / "ToDos.template.md"
        progress_tpl = self.templates_dir / "PROGRESS.template.md"

        if not (plan_tpl.exists() and todos_tpl.exists() and progress_tpl.exists()):
            return False, "Required template files missing in templates/."

        # Substitute placeholders
        plan_content = plan_tpl.read_text(encoding="utf-8").replace("{{PROJECT_NAME}}", project_name)
        plan_content = plan_content.replace("{{Product/Web | AI/ML | Hybrid}}", track)
        self.plan_file.write_text(plan_content, encoding="utf-8")

        todos_content = todos_tpl.read_text(encoding="utf-8").replace("{{PROJECT_NAME}}", project_name)
        self.todos_file.write_text(todos_content, encoding="utf-8")

        progress_content = progress_tpl.read_text(encoding="utf-8").replace("{{PROJECT_NAME}}", project_name)
        self.progress_file.write_text(progress_content, encoding="utf-8")

        return True, f"Project '{project_name}' successfully initialized with track '{track}'."
