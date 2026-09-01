# {{PROJECT_NAME}} — Task Ledger

## §0. Operating Contract

Read in full before every work session — no assumed memory of any prior
session. `PROGRESS.md` is the only continuity.

1. Read `plan.md`, this file, `agents/TEAM.md`, `PROGRESS.md` (newest
   entries first).
2. Find the first `- [ ]` task whose every `Deps:` is already `- [x]`.
3. `🧑 HUMAN` task → HANDOFF entry in `PROGRESS.md`, create `STOP`, commit,
   stop.
4. ID contains `-G` → run the matching gate in §0.4.
5. Otherwise: mark `- [~]`, commit that alone, then implement. Read the
   role brief in `agents/` for the task's Owner first. Touch only the
   `Files:` list.
6. Run `Verify:`. Must exit 0.
7. Pass: `- [~]` → `- [x]`, append PROGRESS.md entry, commit
   `<TASK-ID>: <title>`.
8. Fail: retry up to 3 total. Still failing → `- [!]`, full error +
   diagnosis in PROGRESS.md, commit, stop.
9. One task per run unless a whole-phase run was explicitly requested.

**Reality beats the ledger.** Where `PROGRESS.md` shows the actual repo
state differs from what a task assumed, follow `PROGRESS.md`, do the task's
intent, correct the ledger for the next session.

**Genuinely ambiguous + costly to reverse → QUESTION entry, not a guess.**

### §0.1 Task ID scheme

`P<phase>-T<nnn>` normal · `P<phase>-G<n>` gate · `P<phase>-F<nn>` gate
finding fix · `P<phase>-C<nn>` change request.

### §0.2 Task format

```
- [ ] **P<N>-T<NNN>** {{★ if architect-tier}} <title>
  - **Owner:** <agent from agents/TEAM.md>
  - **Deps:** <task IDs, or —>
  - **Files:** <exact paths>
  - **Do:** <specific instruction>
  - **Accept:** <observable done-condition>
  - **Verify:** `<command>`
```

Small tasks beat large ones — if `Do:` needs more than a short paragraph,
split it.

### §0.3 ★ tasks

Schema, core domain logic implementing a Hard Rule, auth internals, novel
algorithm correctness, and security-sensitive code are ★. Always the
strongest available model tier, never delegated. See `agents/TEAM.md` §2.

### §0.4 Gate sequence (Phase 5, every phase that ships user-facing or
production code)

| Gate | Owner | Reviews for |
|---|---|---|
| **G1 Test** | senior-qa-architect | Suite genuinely green, Hard Rules tested first |
| **G2 Code Review** | code-reviewer | Industry-standard quality, maintainability, review-only |
| **G3 Security** | senior-security-engineer | OWASP baseline + Hard Rules, review-only |
| **G4 UX/Visual** | visual-qa + brand-guardian | Pixel/breakpoint fidelity, brand + Impeccable critique, review-only |
| **G5 Performance** | senior-performance-engineer | Core Web Vitals / latency budget, review-only |
| **G6 Sign-off** | coordinator | All above `- [x]`, exit criteria demonstrated, tag `phase-<N>-complete` |

Each review-only gate (G2, G3, G4) files Critical/High findings as new tasks
directly below itself and stays unchecked until none remain open — never
fixes them itself. AI/ML tracks add a **G0-ML Model Eval** gate before G1
(senior-mlops-engineer: metrics threshold, reproducibility, no unversioned
dataset) — see `phases/PHASE-5-QUALITY-SECURITY.md`.

---

## Phase 1 — Discovery

**Exit:** capability map + personas + open questions resolved.

- [ ] **P1-T001** Produce structured capability map
  - **Owner:** requirement-analyzer
  - **Deps:** —
  - **Files:** `plan.md`
  - **Do:** {{}}
  - **Accept:** {{}}
  - **Verify:** manual review against `plan.md` §1-2

{{... generate remaining Phase 1 tasks from the requirement at bootstrap.
Do not hand-write every phase before plan.md is real — generate one phase
at a time.}}

---

{{Repeat Phase N sections per README.md's phase map. Each phase's Owner
values come from agents/TEAM.md's roster for that phase/track.}}
