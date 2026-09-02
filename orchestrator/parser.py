"""
Parser for akstack Markdown files: ToDos.md, plan.md, PROGRESS.md.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from .models import Gate, ProjectPlan, Task, TaskStatus, TaskType


class MarkdownParser:
    """Parses and manipulates akstack task ledgers, plans, and progress journals."""

    TASK_HEADER_PATTERN = re.compile(
        r"^[ \t]*- \[(?P<status>[ ~x!])\] \*\*(?P<id>P\d+-[TGF]\d+)\*\*(?P<rest>.*)$",
        re.MULTILINE
    )

    FIELD_PATTERNS = {
        "owner": re.compile(r"^[ \t]*-[ \t]+\*\*Owner:\*\*[ \t]+(?P<val>.+)$", re.MULTILINE | re.IGNORECASE),
        "deps": re.compile(r"^[ \t]*-[ \t]+\*\*Deps:\*\*[ \t]+(?P<val>.+)$", re.MULTILINE | re.IGNORECASE),
        "files": re.compile(r"^[ \t]*-[ \t]+\*\*Files:\*\*[ \t]+(?P<val>.+)$", re.MULTILINE | re.IGNORECASE),
        "do": re.compile(r"^[ \t]*-[ \t]+\*\*Do:\*\*[ \t]+(?P<val>.+)$", re.MULTILINE | re.IGNORECASE),
        "accept": re.compile(r"^[ \t]*-[ \t]+\*\*Accept:\*\*[ \t]+(?P<val>.+)$", re.MULTILINE | re.IGNORECASE),
        "verify": re.compile(r"^[ \t]*-[ \t]+\*\*Verify:\*\*[ \t]+(?P<val>.+)$", re.MULTILINE | re.IGNORECASE),
    }

    PHASE_HEADER_PATTERN = re.compile(r"^## Phase (\d+)", re.MULTILINE)

    @staticmethod
    def parse_status_char(char: str) -> TaskStatus:
        if char == "x":
            return TaskStatus.COMPLETED
        elif char == "~":
            return TaskStatus.IN_PROGRESS
        elif char == "!":
            return TaskStatus.BLOCKED
        return TaskStatus.PENDING

    @staticmethod
    def status_to_char(status: TaskStatus) -> str:
        if status == TaskStatus.COMPLETED:
            return "x"
        elif status == TaskStatus.IN_PROGRESS:
            return "~"
        elif status == TaskStatus.BLOCKED:
            return "!"
        return " "

    @classmethod
    def parse_todos(cls, content: str) -> List[Task]:
        """Parse tasks from ToDos.md content."""
        tasks: List[Task] = []
        lines = content.splitlines(keepends=True)

        # Map line numbers to phases
        current_phase = 1
        line_phase_map: Dict[int, int] = {}
        for idx, line in enumerate(lines, 1):
            m = cls.PHASE_HEADER_PATTERN.match(line)
            if m:
                current_phase = int(m.group(1))
            line_phase_map[idx] = current_phase

        matches = list(cls.TASK_HEADER_PATTERN.finditer(content))
        for i, match in enumerate(matches):
            start_pos = match.start()
            end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            raw_block = content[start_pos:end_pos].strip()

            status_char = match.group("status")
            task_id = match.group("id")
            rest_of_header = match.group("rest")

            # Determine task type
            if "-G" in task_id:
                task_type = TaskType.GATE
            elif "-F" in task_id:
                task_type = TaskType.FINDING
            elif "-C" in task_id:
                task_type = TaskType.CHANGE
            else:
                task_type = TaskType.STANDARD

            # Check for phase from ID: e.g. P2-T001 -> 2
            phase_m = re.match(r"P(\d+)-", task_id)
            phase = int(phase_m.group(1)) if phase_m else 1

            is_senior = "★" in rest_of_header or "senior" in rest_of_header.lower()
            is_human = "🧑" in rest_of_header or "HUMAN" in rest_of_header

            # Clean title
            title = rest_of_header.replace("★", "").replace("🧑 HUMAN", "").strip()

            # Parse fields
            owner = cls._extract_field(raw_block, "owner")
            deps_raw = cls._extract_field(raw_block, "deps")
            files_raw = cls._extract_field(raw_block, "files")
            do = cls._extract_field(raw_block, "do")
            accept = cls._extract_field(raw_block, "accept")
            verify = cls._extract_field(raw_block, "verify")

            deps = cls._clean_list(deps_raw)
            files = cls._clean_files(files_raw)

            tasks.append(Task(
                id=task_id,
                title=title,
                phase=phase,
                task_type=task_type,
                status=cls.parse_status_char(status_char),
                owner=owner,
                deps=deps,
                files=files,
                do=do,
                accept=accept,
                verify=verify,
                is_senior=is_senior,
                is_human=is_human,
                raw_text=raw_block,
            ))

        return tasks

    @classmethod
    def _extract_field(cls, block: str, field_name: str) -> str:
        pattern = cls.FIELD_PATTERNS.get(field_name)
        if not pattern:
            return ""
        m = pattern.search(block)
        return m.group("val").strip() if m else ""

    @staticmethod
    def _clean_list(raw: str) -> List[str]:
        if not raw or raw in ("—", "-", "none", "None", ""):
            return []
        items = re.split(r"[,;]\s*", raw)
        cleaned = []
        for item in items:
            it = item.strip().strip("`")
            if it and it not in ("—", "-"):
                cleaned.append(it)
        return cleaned

    @staticmethod
    def _clean_files(raw: str) -> List[str]:
        if not raw or raw in ("—", "-", "none"):
            return []
        extracted = re.findall(r"`([^`]+)`", raw)
        if extracted:
            return [f.strip() for f in extracted if f.strip()]
        return [f.strip() for f in raw.split(",") if f.strip() and f.strip() != "—"]

    @classmethod
    def update_task_status(cls, content: str, task_id: str, new_status: TaskStatus) -> Tuple[str, bool]:
        """Update a task's checkbox status in ToDos.md content."""
        char = cls.status_to_char(new_status)
        pattern = re.compile(
            rf"^([ \t]*- \[)[ ~x!](] \*\*{re.escape(task_id)}\*\*)",
            re.MULTILINE
        )
        new_content, count = pattern.subn(rf"\g<1>{char}\g<2>", content)
        return new_content, count > 0

    @classmethod
    def parse_plan(cls, content: str) -> ProjectPlan:
        """Extract high level metadata from plan.md."""
        title_m = re.search(r"^#\s+(.+?)(?:—|-|\n)", content, re.MULTILINE)
        name = title_m.group(1).strip() if title_m else "Project"

        track_m = re.search(r"## 0\.\s*Track\s*\n+\*?\*?([A-Za-z/]+)", content)
        track = track_m.group(1).strip() if track_m else "Product/Web"

        # Hard rules
        hard_rules = []
        rules_section = re.search(r"## 3\.\s*Domain & Hard Rules\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
        if rules_section:
            for line in rules_section.group(1).splitlines():
                line = line.strip()
                if line and (line.startswith("-") or re.match(r"^\d+\.", line)):
                    cleaned = re.sub(r"^(?:-|\d+\.)\s*", "", line).strip()
                    if cleaned and not cleaned.startswith("{{"):
                        hard_rules.append(cleaned)

        # Open questions
        open_questions = []
        questions_section = re.search(r"## 8\.\s*Open Questions.*?\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
        if questions_section:
            for line in questions_section.group(1).splitlines():
                line = line.strip()
                if line and (line.startswith("-") or re.match(r"^\d+\.", line)):
                    cleaned = re.sub(r"^(?:-|\d+\.)\s*", "", line).strip()
                    if cleaned and not cleaned.startswith("{{"):
                        open_questions.append(cleaned)

        return ProjectPlan(
            project_name=name,
            track=track,
            hard_rules=hard_rules,
            open_questions=open_questions
        )
