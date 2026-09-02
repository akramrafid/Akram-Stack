# {{PROJECT_NAME}} — Task Ledger

## §0. Operating Contract

Read in full before every work session — no assumed memory of any prior session. `PROGRESS.md` is the only continuity. Use the `akstack` CLI (`python -m orchestrator.cli`) for deterministic task management.

1. **Orient**: Run `akstack status` or read `plan.md`, this file, `agents/TEAM.md`, `PROGRESS.md` (newest entries first).
2. **Select**: Run `akstack next` to find the first `- [ ]` task whose every `Deps:` is already `- [x]`.
3. **🧑 HUMAN Task**: Write a `HANDOFF` entry in `PROGRESS.md`, create a `STOP` file, commit, and halt.
4. **Gate Task (`-G`)**: Follow the gate execution sequence in §0.4 and `phases/PHASE-5-QUALITY-SECURITY.md`.
5. **Implement**:
   - Run `akstack start <task-id>` (marks `- [~]`).
   - Read the role brief in `agents/<owner>.md` for the task's Owner first.
   - Touch ONLY the paths specified in `Files:`.
   - Adhere strictly to domain Hard Rules in `plan.md` §3 and standing rules in `agents/TEAM.md` §4.
6. **Verify**:
   - Run `Verify:` command. Must exit 0 cleanly.
7. **Complete**:
   - Run `akstack complete <task-id>`.
   - Automatically verifies exit code, marks `- [x]`, appends `PROGRESS.md` journal entry, and creates git commit `<TASK-ID>: <title>`.
8. **Failure & Blockers**:
   - Up to 3 retries. If still failing, run `akstack fail <task-id> --error "<diagnosis>"`.
   - Marks `- [!]`, records root-cause analysis in `PROGRESS.md`, and stops.

**Reality beats the ledger.** Where `PROGRESS.md` shows the actual repository state differs from what a task assumed, follow `PROGRESS.md`, do the task's intent, and correct the ledger.

**Genuinely ambiguous + costly to reverse → QUESTION entry in `PROGRESS.md`, never a silent guess.**

### §0.1 Task ID Scheme

- `P<phase>-T<nnn>`: Standard implementation task.
- `P<phase>-G<n>`: Quality, security, or release gate.
- `P<phase>-F<nn>`: Gate finding fix (filed directly below failing gate).
- `P<phase>-C<nn>`: Cross-cutting requirement change request.

### §0.2 Task Format

```markdown
- [ ] **P<N>-T<NNN>** {{★ if architect-tier}} <title>
  - **Owner:** <agent from agents/TEAM.md>
  - **Deps:** <comma-separated task IDs, or —>
  - **Files:** <comma-separated exact paths>
  - **Do:** <specific instruction>
  - **Accept:** <observable done-condition>
  - **Verify:** `<exact shell command exiting 0>`
```

Small tasks beat large ones — if `Do:` requires more than a short paragraph, split it.

### §0.3 ★ Senior Tasks

Schema, core domain logic implementing a Hard Rule, security/auth internals, architectural topology, and novel algorithm validation are ★ Senior. They MUST execute on the flagship model tier, never delegated. See `agents/TEAM.md` §2.

### §0.4 Gate Sequence (Phase 5 Quality & Security)

| Gate | Owner | Reviews for | Mode |
|---|---|---|---|
| **G0-ML** *(AI/ML track)* | `senior-mlops-engineer` | Model lineage, reproducible training, eval threshold cleared | Implement |
| **G1 Test** | `senior-qa-architect` | Automated test suite 100% green, Hard Rules tested first | Implement (tests only) |
| **G2 Code Review** | `code-reviewer` | Clean architecture, error handling, maintainability, ownership compliance | Review-only |
| **G3 Security** | `senior-security-engineer` | OWASP Top 10 + ASVS, auth boundaries, Hard Rules verification | Review-only |
| **G4 UX/Visual** | `visual-qa` + `brand-guardian` | Pixel/breakpoint fidelity, brand sign-off, Impeccable critique | Review-only |
| **G4-A11Y Accessibility** | `senior-accessibility-engineer` | WCAG 2.2 AA compliance, screen reader support, keyboard traps | Review-only |
| **G5 Performance** | `senior-performance-engineer` | Core Web Vitals, Lighthouse CI, API latency budgets | Review-only |
| **G6 Sign-off** | coordinator | All gates `- [x]`, exit criteria proven, tag `phase-<N>-complete` | Sign-off |

Each review-only gate files Critical/High findings as new `-F` tasks directly below itself and stays unchecked until none remain open — reviewers NEVER edit production code.

---

## Phase 1 — Discovery

**Exit Criteria:** Structured capability map + user personas + domain Hard Rules draft + open questions logged.

- [ ] **P1-T001** Produce structured capability map
  - **Owner:** requirement-analyzer
  - **Deps:** —
  - **Files:** `plan.md`
  - **Do:** Analyze raw requirement, identify core capabilities, SEO scope, and technical constraints.
  - **Accept:** `plan.md` §1-2 populated with capabilities, users, and roles.
  - **Verify:** manual review against `plan.md` §1-2

{{... remaining Phase 1 tasks generated at bootstrap. Generate subsequent phases one at a time.}}
