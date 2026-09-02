"""
Command Line Interface (CLI) for akstack orchestration.
"""

import argparse
import os
import sys
from pathlib import Path

# Ensure UTF-8 output handling on Windows terminals
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from .engine import OrchestratorEngine
from .graph import DependencyGraph
from .models import TaskStatus

# ANSI Color Utilities
COLOR_CYAN = "\033[96m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_BOLD = "\033[1m"
COLOR_DIM = "\033[2m"
COLOR_RESET = "\033[0m"


def colorize(text: str, color: str) -> str:
    if not sys.stdout.isatty() or os.environ.get("NO_COLOR"):
        return text
    return f"{color}{text}{COLOR_RESET}"


def cmd_status(engine: OrchestratorEngine, args: argparse.Namespace) -> int:
    status = engine.get_status()
    print()
    print(colorize(f"=== Akram-Stack: {status['project_name']} ===", COLOR_BOLD + COLOR_CYAN))
    print(f"Track: {colorize(status['track'], COLOR_BOLD)} | Active Phase: {colorize(f'Phase {status['active_phase']}', COLOR_YELLOW)}")
    print()

    # Status summary bar
    total = status["total_tasks"]
    comp = status["completed_tasks"]
    pct = (comp / total * 100) if total > 0 else 0
    print(f"Progress: [{comp}/{total}] {pct:.1f}% complete")

    print(f"  • Completed   : {colorize(str(comp), COLOR_GREEN)}")
    print(f"  • In Progress : {colorize(str(len(status['in_progress_tasks'])), COLOR_YELLOW)}")
    print(f"  • Pending     : {colorize(str(status['pending_tasks']), COLOR_DIM)}")
    print(f"  • Blocked     : {colorize(str(len(status['blocked_tasks'])), COLOR_RED)}")
    print()

    # Active tasks
    if status["in_progress_tasks"]:
        print(colorize("▶ Active In-Progress Tasks:", COLOR_YELLOW))
        for t in status["in_progress_tasks"]:
            senior = colorize("★ ", COLOR_YELLOW) if t.is_senior else ""
            print(f"  - {senior}{colorize(t.id, COLOR_BOLD)}: {t.title} (Owner: {t.owner})")
        print()

    # Blocked tasks
    if status["blocked_tasks"]:
        print(colorize("✖ Blocked Tasks (- [!]):", COLOR_RED))
        for t in status["blocked_tasks"]:
            print(f"  - {colorize(t.id, COLOR_BOLD)}: {t.title} (Owner: {t.owner})")
        print()

    # Next runnable
    next_t = status["next_task"]
    if next_t:
        senior = colorize("★ ", COLOR_YELLOW) if next_t.is_senior else ""
        print(colorize("➜ Next Runnable Task:", COLOR_GREEN))
        print(f"  ID    : {senior}{colorize(next_t.id, COLOR_BOLD)}")
        print(f"  Title : {next_t.title}")
        print(f"  Owner : {colorize(next_t.owner or 'Unassigned', COLOR_CYAN)}")
        if next_t.files:
            print(f"  Files : {', '.join(next_t.files)}")
        if next_t.verify:
            print(f"  Verify: {colorize(next_t.verify, COLOR_DIM)}")
    else:
        if total > 0 and comp == total:
            print(colorize("[OK] All tasks in the ledger are COMPLETED!", COLOR_GREEN))
        else:
            print(colorize("Waiting on dependencies or human intervention.", COLOR_YELLOW))

    print()
    return 0


def cmd_next(engine: OrchestratorEngine, args: argparse.Namespace) -> int:
    waves = engine.get_next(phase=args.phase, parallel=args.parallel)
    if not waves:
        print(colorize("No runnable tasks found for the selected criteria.", COLOR_YELLOW))
        return 0

    if not args.parallel:
        task = waves[0][0]
        senior = "★ " if task.is_senior else ""
        human = "🧑 HUMAN " if task.is_human else ""
        print(colorize(f"NEXT TASK: {senior}{human}{task.id} - {task.title}", COLOR_BOLD + COLOR_GREEN))
        print(f"Owner: {task.owner}")
        print(f"Files: {', '.join(task.files) if task.files else 'None specified'}")
        print(f"Do: {task.do}")
        print(f"Accept: {task.accept}")
        print(f"Verify: {task.verify}")
        return 0

    print(colorize(f"Scheduled {len(waves)} conflict-free wave(s):", COLOR_BOLD + COLOR_CYAN))
    for idx, wave in enumerate(waves, 1):
        print(f"\n{colorize(f'=== Wave {idx} ({len(wave)} parallel task[s]) ===', COLOR_BOLD)}")
        for t in wave:
            senior = "★ " if t.is_senior else ""
            files_str = f" [Files: {', '.join(t.files)}]" if t.files else ""
            print(f"  • {senior}{colorize(t.id, COLOR_BOLD)}: {t.title} ({colorize(t.owner, COLOR_CYAN)}){colorize(files_str, COLOR_DIM)}")

    return 0


def cmd_start(engine: OrchestratorEngine, args: argparse.Namespace) -> int:
    success, msg = engine.start_task(args.task_id)
    color = COLOR_GREEN if success else COLOR_RED
    print(colorize(msg, color))
    return 0 if success else 1


def cmd_complete(engine: OrchestratorEngine, args: argparse.Namespace) -> int:
    success, msg = engine.complete_task(
        task_id=args.task_id,
        run_verify=not args.no_verify,
        git_commit=not args.no_commit,
        verification_notes=args.notes or ""
    )
    color = COLOR_GREEN if success else COLOR_RED
    print(colorize(msg, color))
    return 0 if success else 1


def cmd_fail(engine: OrchestratorEngine, args: argparse.Namespace) -> int:
    success, msg = engine.fail_task(task_id=args.task_id, error_msg=args.error)
    color = COLOR_YELLOW if success else COLOR_RED
    print(colorize(msg, color))
    return 0 if success else 1


def cmd_gate(engine: OrchestratorEngine, args: argparse.Namespace) -> int:
    success, msg = engine.run_gate(gate_id=args.gate_id)
    color = COLOR_GREEN if success else COLOR_RED
    print(colorize(msg, color))
    return 0 if success else 1


def cmd_lint(engine: OrchestratorEngine, args: argparse.Namespace) -> int:
    print(colorize("Running akstack system lint...", COLOR_BOLD + COLOR_CYAN))
    errors = engine.lint()
    if not errors:
        print(colorize("[OK] Lint clean! All tasks, owners, dependencies, and agent briefs are valid.", COLOR_GREEN))
        return 0

    print(colorize(f"Found {len(errors)} issue(s):", COLOR_RED))
    for err in errors:
        print(f"  [X] {err}")
    return 1


def cmd_graph(engine: OrchestratorEngine, args: argparse.Namespace) -> int:
    tasks = engine.load_tasks()
    graph = DependencyGraph(tasks)
    if args.mermaid:
        print(graph.to_mermaid())
        return 0

    # Text tree
    print(colorize("Task Dependency Topology:", COLOR_BOLD + COLOR_CYAN))
    for t in tasks:
        senior = "★ " if t.is_senior else ""
        deps_str = f" <- [{', '.join(t.deps)}]" if t.deps else ""
        status_symbol = {"PENDING": "[ ]", "IN_PROGRESS": "[~]", "COMPLETED": "[x]", "BLOCKED": "[!]"}.get(t.status, "[ ]")
        print(f"  {status_symbol} {senior}{t.id}: {t.title}{colorize(deps_str, COLOR_DIM)}")
    return 0


def cmd_init(engine: OrchestratorEngine, args: argparse.Namespace) -> int:
    success, msg = engine.init_project(project_name=args.name, track=args.track)
    color = COLOR_GREEN if success else COLOR_RED
    print(colorize(msg, color))
    return 0 if success else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="akstack",
        description="Akram-Stack (akstack) Programmatic AI Orchestrator"
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # status
    p_status = subparsers.add_parser("status", help="Show project progress, active phase, and blockers")
    p_status.set_defaults(func=cmd_status)

    # next
    p_next = subparsers.add_parser("next", help="Find the next runnable task(s) in topological order")
    p_next.add_argument("--phase", type=int, help="Filter to a specific phase")
    p_next.add_argument("--parallel", action="store_true", help="Group runnable tasks into conflict-free parallel waves")
    p_next.set_defaults(func=cmd_next)

    # start
    p_start = subparsers.add_parser("start", help="Mark a task as in-progress (- [~])")
    p_start.add_argument("task_id", help="Task ID (e.g. P1-T001)")
    p_start.set_defaults(func=cmd_start)

    # complete
    p_complete = subparsers.add_parser("complete", help="Verify and mark task as completed (- [x])")
    p_complete.add_argument("task_id", help="Task ID (e.g. P1-T001)")
    p_complete.add_argument("--no-verify", action="store_true", help="Skip running the task Verify command")
    p_complete.add_argument("--no-commit", action="store_true", help="Skip automatic git commit")
    p_complete.add_argument("--notes", type=str, help="Additional verification notes for PROGRESS.md")
    p_complete.set_defaults(func=cmd_complete)

    # fail
    p_fail = subparsers.add_parser("fail", help="Mark task as blocked (- [!]) and record error diagnosis")
    p_fail.add_argument("task_id", help="Task ID")
    p_fail.add_argument("--error", required=True, help="Failure explanation or error log")
    p_fail.set_defaults(func=cmd_fail)

    # gate
    p_gate = subparsers.add_parser("gate", help="Run a quality/security gate (e.g. P5-G1)")
    p_gate.add_argument("gate_id", help="Gate ID (e.g. P5-G1)")
    p_gate.set_defaults(func=cmd_gate)

    # lint
    p_lint = subparsers.add_parser("lint", help="Verify task graph integrity, agent briefs, and file paths")
    p_lint.set_defaults(func=cmd_lint)

    # graph
    p_graph = subparsers.add_parser("graph", help="Visualize dependency graph")
    p_graph.add_argument("--mermaid", action="store_true", help="Output Mermaid diagram syntax")
    p_graph.set_defaults(func=cmd_graph)

    # init
    p_init = subparsers.add_parser("init", help="Bootstrap a new project from templates")
    p_init.add_argument("name", help="Project name")
    p_init.add_argument("--track", choices=["Product/Web", "AI/ML", "Hybrid"], default="Product/Web", help="Project track")
    p_init.set_defaults(func=cmd_init)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 0

    engine = OrchestratorEngine()
    return args.func(engine, args)


if __name__ == "__main__":
    sys.exit(main())
