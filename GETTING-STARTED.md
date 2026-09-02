# Getting Started with Akram-Stack (akstack)

## 1. Clone it for a New Project

```bash
git clone <akstack-repo-url> my-new-project
cd my-new-project
rm -rf .git && git init -b main
```

`akstack` ships clean — `plan.md`, `ToDos.md`, and `PROGRESS.md` do not exist yet in your clone; only their templates in `templates/` do. Every project's plan is authored fresh at bootstrap.

---

## 2. Initialize the Project

You can bootstrap using either the **Programmatic CLI** or the **Agent Bootstrap Prompt**:

### Option A: Using the Orchestrator CLI

```bash
python -m orchestrator.cli init "My Cool Project" --track Product/Web
```

Options for `--track`: `Product/Web`, `AI/ML`, or `Hybrid`.

### Option B: Using the Agent Prompt

Open the repo in Antigravity or Claude Code and send the **Bootstrap Prompt** from `PROMPT_LIBRARY.md` §1 with your product requirement pasted in.

---

## 3. Review the Plan (The Non-Negotiable Gate)

Read `plan.md` in full before writing any application code, especially:
- **§3 Domain & Hard Rules**: Did it identify the real domain risks (e.g. integer money, transactional consistency, tenant isolation, idempotency)?
- **§6 SLOs & Budgets**: Are latency, availability, and accessibility targets clear?
- **§9 Open Questions**: Resolve genuine ambiguities before architecture and implementation.

Approve `plan.md` or instruct the agent to revise specific sections.

---

## 4. Execute the Phases

The pipeline runs sequentially through 7 phases:

```bash
# Phase 1 — Discovery: capability map, personas, open questions
# Phase 2 — Architecture: C4 diagrams, database schema, API contracts, threat model
# Phase 3 — Design: design system in design-system/MASTER.md, accessibility audit
# Phase 4 — Build: deterministic build loop
# Phase 5 — Quality & Security: G0-ML through G6 gates
# Phase 6 — DevOps & Launch: CI/CD, container hardening, observability, live deploy
```

---

## 5. Day-to-Day: The Build Loop

In Phase 4, tasks are executed one at a time or in conflict-free parallel waves:

```bash
# 1. View project status and blockers
python -m orchestrator.cli status

# 2. Select the next runnable task in dependency order
python -m orchestrator.cli next

# 3. Mark task as in-progress
python -m orchestrator.cli start <task-id>

# 4. Implement strictly within declared Files: boundary.

# 5. Complete task (runs Verify command, verifies exit 0, commits)
python -m orchestrator.cli complete <task-id>
```

For parallel multi-agent dispatch:
```bash
python -m orchestrator.cli next --parallel
```
The CLI automatically groups runnable tasks into waves whose declared file boundaries do not overlap.

---

## 6. Running Quality & Security Gates (Phase 5)

Phase 5 enforces 7 mandatory gates in order:

```bash
# Run and clear gates once verification criteria are satisfied:
python -m orchestrator.cli gate P5-G1         # Test Gate (automated test suite 100% green)
python -m orchestrator.cli gate P5-G2         # Code Review Gate (clean architecture & standards)
python -m orchestrator.cli gate P5-G3         # Security Gate (OWASP Top 10 + Hard Rules)
python -m orchestrator.cli gate P5-G4         # Visual/UX Gate (breakpoint fidelity)
python -m orchestrator.cli gate P5-G4-A11Y    # Accessibility Gate (WCAG 2.2 AA compliance)
python -m orchestrator.cli gate P5-G5         # Performance Gate (Core Web Vitals budget)
python -m orchestrator.cli gate P5-G6         # Final Sign-Off & Git Tag
```

Reviewers in G2 through G5 are **review-only** — they never edit production code; they file `-F` tasks directly below the gate until resolved.

---

## 7. Diagnostics & Recovery

- **Check system consistency:**
  ```bash
  python -m orchestrator.cli lint
  ```
- **Inspect dependency graph:**
  ```bash
  python -m orchestrator.cli graph
  python -m orchestrator.cli graph --mermaid
  ```
- **When a task is blocked (`- [!]`):**
  Use `PROMPT_LIBRARY.md` §5.1 to diagnose the root cause, fix the issue, and reset the task to `- [ ]`.
- **Reverting a bad commit:**
  ```bash
  git log --oneline -10
  git reset --hard <commit-before-bad-task>
  ```
  Reset the task in `ToDos.md` to `- [ ]` and re-run.

---

## 8. Antigravity Skill Integration

`akstack` includes native Antigravity skill configuration in `.agents/skills/akstack/SKILL.md`. Antigravity automatically detects this skill and can trigger `akstack` commands autonomously during pairing sessions.
