---
name: akstack
description: Production-grade multi-agent orchestration framework for full-stack applications across architecture, system design, databases, frontend, backend, integrations, mobile, SQA, SRE, and DevOps.
---

# Akram-Stack (akstack) Orchestrator Skill

## Overview
Akram-Stack is an enterprise-grade AI agent orchestration framework. It persists all state in deterministic markdown files on disk (`plan.md`, `ToDos.md`, `PROGRESS.md`), executes a disciplined 7-phase lifecycle (Phases 0 through 6), isolates agent responsibilities through strict file ownership, enforces domain Hard Rules, and gates all production shipments through quality checkpoints (G0-ML through G6).

## CLI Orchestration Commands

The programmatic CLI tool `akstack` is available in `bin/` or executable via `python -m orchestrator.cli`:

```bash
# Check overall project progress, active phase, and blocked tasks
python -m orchestrator.cli status

# Resolve next runnable task(s) in topological dependency order
python -m orchestrator.cli next
python -m orchestrator.cli next --parallel   # group into conflict-free parallel waves

# Start executing a task (marks - [~])
python -m orchestrator.cli start <task-id>

# Complete a task (runs Verify command, marks - [x], logs to PROGRESS.md, git commits)
python -m orchestrator.cli complete <task-id>

# Flag a blocked task (marks - [!], logs diagnostic error)
python -m orchestrator.cli fail <task-id> --error "<error details>"

# Run quality/security gate checks (validates phase completion preconditions)
python -m orchestrator.cli gate <gate-id>

# Validate system integrity (no circular dependencies, valid agent owners, unique IDs)
python -m orchestrator.cli lint

# Export dependency diagram in Mermaid format
python -m orchestrator.cli graph --mermaid
```

## Core Agent Roster & Ownership
- **Architecture & System Design**: `senior-system-architect` (★), `senior-system-designer`, `senior-cloud-architect`, `senior-database-architect` (★), `senior-security-engineer` (★), `senior-sre-observability-engineer` (★), `senior-technical-writer`.
- **UI/UX & Accessibility**: `senior-product-designer`, `ui-designer`, `senior-accessibility-engineer`, `brand-guardian`.
- **Implementation**: `senior-backend-engineer`, `senior-frontend-engineer`, `senior-integration-engineer`, `senior-mobile-engineer`, and specialized AI/ML engineers (`senior-llm-engineer`, `senior-ai-engineer`, etc.).
- **Quality & Verification**: `senior-qa-architect` (tests only), `code-reviewer` (review-only), `visual-qa` (review-only), `senior-performance-engineer` (review-only).
- **Operations & Launch**: `senior-devops-engineer`, `senior-mlops-engineer`.

## Mandatory Engineering Principles
1. **Never Violate Hard Rules**: Rules defined in `plan.md` §3 must be respected across every single commit.
2. **Never Edit in Review-Only Gates**: G2 (Code Review), G3 (Security), G4 (Visual/UX), and G5 (Performance) never edit source code directly; they file actionable `-F` tasks.
3. **★ Senior Tier Integrity**: Senior tasks must execute on the highest-capability model tier available; never delegate to lightweight tiers.
4. **Boundary Validation & Security**: Validate all inputs at transport boundaries with schemas (Zod/Pydantic). Protect against OWASP vulnerabilities (BOLA/IDOR, SQLi, XSS, SSRF).
