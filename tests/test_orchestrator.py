"""
Comprehensive automated unit tests for the akstack orchestration engine.
"""

import shutil
import tempfile
import unittest
from pathlib import Path

from orchestrator.engine import OrchestratorEngine
from orchestrator.graph import DependencyGraph
from orchestrator.models import Task, TaskStatus, TaskType
from orchestrator.parser import MarkdownParser


class TestMarkdownParser(unittest.TestCase):

    def test_parse_sample_todos(self):
        sample_md = """
# Test Project — Task Ledger

## Phase 1 — Discovery

- [ ] **P1-T001** ★ Produce structured capability map
  - **Owner:** requirement-analyzer
  - **Deps:** —
  - **Files:** `plan.md`, `docs/capabilities.md`
  - **Do:** Analyze requirements
  - **Accept:** Capability matrix populated
  - **Verify:** `python -m unittest test_plan`

- [~] **P1-T002** 🧑 HUMAN Review domain rules
  - **Owner:** senior-product-manager
  - **Deps:** P1-T001
  - **Files:** `plan.md`
  - **Do:** Sign off on section 3
  - **Accept:** Human approval
  - **Verify:** manual review

## Phase 5 — Quality & Security

- [x] **P5-G1** Test Gate
  - **Owner:** senior-qa-architect
  - **Deps:** P1-T002
  - **Files:** —
  - **Do:** Run test suite
  - **Accept:** Green tests
  - **Verify:** pytest
"""
        tasks = MarkdownParser.parse_todos(sample_md)
        self.assertEqual(len(tasks), 3)

        # Task 1
        t1 = tasks[0]
        self.assertEqual(t1.id, "P1-T001")
        self.assertEqual(t1.title, "Produce structured capability map")
        self.assertEqual(t1.status, TaskStatus.PENDING)
        self.assertTrue(t1.is_senior)
        self.assertEqual(t1.owner, "requirement-analyzer")
        self.assertEqual(t1.files, ["plan.md", "docs/capabilities.md"])
        self.assertEqual(t1.deps, [])

        # Task 2
        t2 = tasks[1]
        self.assertEqual(t2.id, "P1-T002")
        self.assertEqual(t2.status, TaskStatus.IN_PROGRESS)
        self.assertTrue(t2.is_human)
        self.assertEqual(t2.deps, ["P1-T001"])

        # Task 3 (Gate)
        t3 = tasks[2]
        self.assertEqual(t3.id, "P5-G1")
        self.assertEqual(t3.task_type, TaskType.GATE)
        self.assertEqual(t3.status, TaskStatus.COMPLETED)

    def test_update_status(self):
        sample_md = "- [ ] **P1-T001** Task 1\n- [ ] **P1-T002** Task 2\n"
        updated_md, ok = MarkdownParser.update_task_status(sample_md, "P1-T001", TaskStatus.IN_PROGRESS)
        self.assertTrue(ok)
        self.assertIn("- [~] **P1-T001**", updated_md)
        self.assertIn("- [ ] **P1-T002**", updated_md)

        completed_md, ok2 = MarkdownParser.update_task_status(updated_md, "P1-T001", TaskStatus.COMPLETED)
        self.assertTrue(ok2)
        self.assertIn("- [x] **P1-T001**", completed_md)


class TestDependencyGraph(unittest.TestCase):

    def test_cycle_detection(self):
        # A -> B -> C -> A
        tA = Task(id="A", title="A", phase=1, task_type=TaskType.STANDARD, status=TaskStatus.PENDING, deps=["C"])
        tB = Task(id="B", title="B", phase=1, task_type=TaskType.STANDARD, status=TaskStatus.PENDING, deps=["A"])
        tC = Task(id="C", title="C", phase=1, task_type=TaskType.STANDARD, status=TaskStatus.PENDING, deps=["B"])

        graph = DependencyGraph([tA, tB, tC])
        cycle = graph.detect_cycles()
        self.assertIsNotNone(cycle)
        self.assertIn("A", cycle)
        self.assertIn("B", cycle)
        self.assertIn("C", cycle)

    def test_runnable_tasks(self):
        t1 = Task(id="T1", title="T1", phase=1, task_type=TaskType.STANDARD, status=TaskStatus.COMPLETED)
        t2 = Task(id="T2", title="T2", phase=1, task_type=TaskType.STANDARD, status=TaskStatus.PENDING, deps=["T1"])
        t3 = Task(id="T3", title="T3", phase=1, task_type=TaskType.STANDARD, status=TaskStatus.PENDING, deps=["T2"])

        graph = DependencyGraph([t1, t2, t3])
        runnable = graph.get_runnable_tasks()
        self.assertEqual(len(runnable), 1)
        self.assertEqual(runnable[0].id, "T2")

    def test_parallel_waves_disjoint_files(self):
        # T1 touches file_a, T2 touches file_b (parallel safe)
        # T3 touches file_a (must not run in same wave as T1)
        t1 = Task(id="T1", title="T1", phase=1, task_type=TaskType.STANDARD, status=TaskStatus.PENDING, files=["src/a.ts"])
        t2 = Task(id="T2", title="T2", phase=1, task_type=TaskType.STANDARD, status=TaskStatus.PENDING, files=["src/b.ts"])
        t3 = Task(id="T3", title="T3", phase=1, task_type=TaskType.STANDARD, status=TaskStatus.PENDING, files=["src/a.ts"])

        graph = DependencyGraph([t1, t2, t3])
        waves = graph.schedule_parallel_waves([t1, t2, t3])
        self.assertEqual(len(waves), 2)
        # Wave 1 contains T1 and T2
        wave1_ids = [t.id for t in waves[0]]
        self.assertIn("T1", wave1_ids)
        self.assertIn("T2", wave1_ids)
        # Wave 2 contains T3
        self.assertEqual(waves[1][0].id, "T3")

    def test_to_mermaid(self):
        t1 = Task(id="P1-T001", title="Setup", phase=1, task_type=TaskType.STANDARD, status=TaskStatus.COMPLETED)
        t2 = Task(id="P1-T002", title="Build", phase=1, task_type=TaskType.STANDARD, status=TaskStatus.PENDING, deps=["P1-T001"])
        graph = DependencyGraph([t1, t2])
        mm = graph.to_mermaid()
        self.assertIn("flowchart TD", mm)
        self.assertIn("P1-T001 --> P1-T002", mm)


class TestOrchestratorEngineIntegration(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        self.repo_root = Path(__file__).resolve().parent.parent
        # Copy templates and agents into test directory
        shutil.copytree(self.repo_root / "templates", self.test_dir / "templates")
        shutil.copytree(self.repo_root / "agents", self.test_dir / "agents")

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_init_and_workflow(self):
        engine = OrchestratorEngine(workspace_root=self.test_dir)
        ok, msg = engine.init_project("TestApp", track="Hybrid")
        self.assertTrue(ok)

        # Status check
        status = engine.get_status()
        self.assertEqual(status["project_name"], "TestApp")
        self.assertEqual(status["track"], "Hybrid")

        # Start first task
        t_first = status["next_task"]
        self.assertIsNotNone(t_first)
        ok, _ = engine.start_task(t_first.id)
        self.assertTrue(ok)

        # Check status shows in progress
        status2 = engine.get_status()
        self.assertEqual(len(status2["in_progress_tasks"]), 1)

        # Complete task without verify command
        ok, _ = engine.complete_task(t_first.id, run_verify=False, git_commit=False)
        self.assertTrue(ok)

        # Check completed
        status3 = engine.get_status()
        self.assertEqual(status3["completed_tasks"], 1)

        # Fail task test
        t_dummy = "- [ ] **P1-T999** Dummy\n  - **Owner:** senior-backend-engineer\n"
        with open(engine.todos_file, "a", encoding="utf-8") as f:
            f.write("\n" + t_dummy)

        ok, _ = engine.fail_task("P1-T999", "Failed test expectation")
        self.assertTrue(ok)
        status4 = engine.get_status()
        self.assertEqual(len(status4["blocked_tasks"]), 1)

    def test_lint_system(self):
        engine = OrchestratorEngine(workspace_root=self.test_dir)
        engine.init_project("LintTest", track="Product/Web")
        errors = engine.lint()
        self.assertEqual(len(errors), 0)


if __name__ == "__main__":
    unittest.main()
