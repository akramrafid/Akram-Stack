"""
Data models for the Akram-Stack (akstack) orchestration engine.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Set


class TaskStatus(str, Enum):
    PENDING = "PENDING"        # - [ ]
    IN_PROGRESS = "IN_PROGRESS"  # - [~]
    COMPLETED = "COMPLETED"    # - [x]
    BLOCKED = "BLOCKED"        # - [!]


class TaskType(str, Enum):
    STANDARD = "STANDARD"      # P<n>-T<nnn>
    GATE = "GATE"              # P<n>-G<n>
    FINDING = "FINDING"        # P<n>-F<nn>
    CHANGE = "CHANGE"          # P<n>-C<nn>


@dataclass
class Task:
    id: str
    title: str
    phase: int
    task_type: TaskType
    status: TaskStatus
    owner: str = ""
    deps: List[str] = field(default_factory=list)
    files: List[str] = field(default_factory=list)
    do: str = ""
    accept: str = ""
    verify: str = ""
    is_senior: bool = False
    is_human: bool = False
    raw_text: str = ""
    line_start: int = 0
    line_end: int = 0

    @property
    def file_set(self) -> Set[str]:
        """Normalized set of affected files for collision checking."""
        return {f.strip().replace("\\", "/").lower() for f in self.files if f.strip()}


@dataclass
class Gate:
    id: str
    phase: int
    title: str
    owner: str
    status: TaskStatus
    review_focus: str = ""
    open_findings: List[str] = field(default_factory=list)


@dataclass
class ProjectPlan:
    project_name: str
    track: str = "Product/Web"
    mission: str = ""
    hard_rules: List[str] = field(default_factory=list)
    frontend: str = ""
    backend: str = ""
    database: str = ""
    auth: str = ""
    infra: str = ""
    ai_stack: str = ""
    open_questions: List[str] = field(default_factory=list)
