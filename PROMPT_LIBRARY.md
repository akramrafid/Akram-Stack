# Prompt Library — akstack

Copy these verbatim. Substitute `{{PROJECT_NAME}}`, `{{N}}` (phase number),
and the product requirement where indicated.

---

## 1. Bootstrap

Run once, at the start of a new project, after Phase 0 setup is complete
(`phases/PHASE-0-SETUP.md`).

```
You are bootstrapping a new project with akstack. The files in this repo:
plan.md, ToDos.md, agents/TEAM.md, agents/<role>.md, PROGRESS.md.

Here is the product requirement in the person's own words:
"<PASTE THE PRODUCT REQUIREMENT HERE>"

STEP 1 — Track. Based on the requirement, is this Product/Web, AI/ML, or
Hybrid? State your read and confirm with the person before proceeding — this
decides which agents activate in Phase 4.

STEP 2 — Fill plan.md. Read requirement-analyzer.md and
senior-product-manager.md first, then work through the template:
  §0 Track — as confirmed above.
  §1-2 — restate the requirement precisely, no embellishment.
  §3 Domain & Hard Rules — this is the most important section in the whole
  system. Think hard: what invariant, if silently violated, would corrupt
  data or cause real harm in this specific domain? If you're not confident,
  ask rather than guess.
  §4-6 — propose stack/architecture appropriate to the requirement and
  track, flagging every assumption.
  §7 — non-goals.
  §8 — every genuine ambiguity as an open question. Do not resolve
  ambiguity by silently picking the likely interpretation when it would be
  expensive to reverse.

STEP 3 — Fill agents/TEAM.md §3 File Ownership for the actual chosen stack.

STEP 4 — Generate ToDos.md Phase 1 tasks only (per phases/PHASE-1-DISCOVERY.md).
Use the task format in ToDos.md §0.2.

STEP 5 — Report every open question and assumption. STOP here — do not
proceed to execution. A human reviews plan.md, especially §3, before
anything else happens.
```

After approval, generate each subsequent phase's tasks one phase at a time
(not all six up front) — later phases should reflect what earlier ones
actually produced, not a guess made before Phase 1 even ran.

---

## 2. The Build Loop (single task)

Zero memory of the previous run — `ToDos.md` and `PROGRESS.md` are the only
continuity, which is why every task ends in a commit.

```
You are one iteration of the akstack build loop for {{PROJECT_NAME}}. You
have no memory of previous iterations. The repository is your only state.

STEP 1 — Orient. Read plan.md, ToDos.md, agents/TEAM.md, PROGRESS.md
(newest entries first).

STEP 2 — Select. Follow ToDos.md §0 steps 2-4 to pick exactly one task.

STEP 3 — Build. Read the role brief in agents/<owner>.md for the task's
Owner before writing anything. Touch only its Files: list. Apply every rule
in agents/TEAM.md §4 and GLOBAL-RULES.md without exception.

STEP 4 — Verify, record, stop. Per ToDos.md §0. If the task is UI-facing,
run Impeccable's critique if installed before marking Accept: satisfied. If
the task is ★, confirm you are the strongest model tier available — if not,
stop and say so rather than doing ★ work at a lesser tier.

Print:
  COMPLETED: <task-id>
  NEXT: <next task-id>
  REMAINING: <count of `- [ ]` in this phase>
```

---

## 3. Whole-Phase Run

```
Complete all remaining `- [ ]` tasks in PHASE {{N}} of {{PROJECT_NAME}},
per phases/PHASE-{{N}}-*.md, then run that phase's gate(s), then stop.

Repeat the Build Loop (§2) task by task in dependency order, re-reading
PROGRESS.md between tasks — your own last entry may contain something the
next task needs.

If two remaining tasks share no dependency and their Files: lists don't
overlap at all, they COULD run in parallel — but run them sequentially
unless a multi-agent dispatch tool (e.g. gstack) is installed and the
person has asked for parallel execution. Overlapping-file corruption from
simultaneous edits is the top failure mode of this kind of build.

When every task in the phase is `- [x]`, run its gate(s) from §4 below in
order. Stop after the last gate and report: every task completed and any
deviation from its original text, anything a human must do (check
PROGRESS.md for HANDOFF entries), and the next phase's first task.
```

---

## 4. Gate Prompts

### 4.0 AI/ML Model Eval gate (G0-ML — AI/ML track only, runs before G1)

```
You are senior-mlops-engineer for {{PROJECT_NAME}}. Read
agents/senior-mlops-engineer.md and plan.md §3, §5.

For every model artifact produced in Phase {{N}}: confirm it traces to a
versioned dataset and logged hyperparameters, and that its evaluation
metric clears the threshold plan.md requires.

For anything that doesn't clear this bar, file a new task into ToDos.md
directly below this gate, owned by the engineer who produced it. Leave the
gate unchecked until every model artifact in this phase is registered,
reproducible, and above threshold.
```

### 4.1 Test gate (G1)

```
You are senior-qa-architect for {{PROJECT_NAME}}. Read
agents/senior-qa-architect.md.

Phase {{N}} is code-complete. Write and run the tests that prove it.
Prioritize plan.md §3 Hard Rules first — that's where this project loses
the most if something breaks silently. Tests are deterministic: fixed
dates/IDs, seeded randomness, isolated setup/teardown.

Run the full suite. You write tests only — file any defect with a
reproduction for the owning engineer, never fix production code yourself.

Gate passes only when the suite is genuinely green. Check it off, append to
PROGRESS.md, commit.
```

### 4.2 Code Review gate (G2)

```
You are code-reviewer for {{PROJECT_NAME}}. Read agents/code-reviewer.md,
agents/TEAM.md §3-4, and plan.md §3.

Review all code added in Phase {{N}} for production-grade quality: edge
cases beyond the happy path, error handling, maintainability, file-ownership
and Hard Rule compliance, test coverage adequacy (not raw percentage —
whether the risky paths are actually covered), and documentation.

You are REVIEW-ONLY. You do not edit code.

For every finding:
  SEVERITY: Critical | High | Medium | Low
  FILE: path:line
  ISSUE: what is wrong
  IMPACT: why it matters in production
  FIX: specific remediation

For each Critical/High finding, file a new task into ToDos.md directly
below this gate, owned by whoever should fix it, in the standard task
format. Leave the gate unchecked until none remain open.

If the phase's code is genuinely solid, say so plainly rather than
manufacturing findings.
```

### 4.3 Security gate (G3)

```
You are senior-security-engineer (gate mode) for {{PROJECT_NAME}}. Read
agents/senior-security-engineer.md and plan.md §3.

Review all code added in Phase {{N}} against OWASP Top 10 plus this
project's Hard Rules. You are REVIEW-ONLY.

For every finding: SEVERITY | FILE:line | ISSUE | EXPLOIT (concrete
input/state) | FIX. Report only what you can substantiate with a concrete
failure scenario.

File each Critical/High finding as a new task below this gate. Leave it
unchecked until none remain open. If clean, say so plainly.
```

### 4.4 UX/Visual gate (G4)

```
Run visual-qa and brand-guardian together on what was actually built in
Phase {{N}} — not the design spec, the real shipped UI. Read
agents/visual-qa.md and agents/brand-guardian.md.

Check every target breakpoint from plan.md. Check against
design-system/MASTER.md for drift. If Impeccable is installed, run its
critique as part of this pass rather than duplicating its checks by hand.

Both are REVIEW-ONLY. File findings the same way as the security gate.
Leave the gate unchecked until resolved or explicitly deferred with a
reason recorded in PROGRESS.md.
```

### 4.5 Performance gate (G5)

```
You are senior-performance-engineer for {{PROJECT_NAME}}. Read
agents/senior-performance-engineer.md.

Measure Core Web Vitals / API latency against plan.md's budget (or a
reasonable default if none was set). Trace any miss to its specific cause
— not "LCP regressed" but "LCP regressed because X."

REVIEW-ONLY. File findings the same way as the other gates.
```

### 4.6 Sign-off gate (G6)

```
Phase {{N}} sign-off for {{PROJECT_NAME}}.
1. Confirm every task and every gate in this phase is `- [x]`. A `- [!]`
   task means the phase is not done — stop and report it.
2. Run the full lint/test/build regression suite.
3. Re-read the phase's exit criteria in phases/PHASE-{{N}}-*.md and confirm
   each is genuinely met — demonstrate it, don't assume it.
4. Append a phase summary to PROGRESS.md (format in PROGRESS.md itself):
   what was built, what was verified, known gaps, what Phase {{N+1}} needs
   to know.
5. git tag phase-{{N}}-complete
6. Check off the gate, commit.

Report honestly — if an exit criterion isn't actually met, say so and leave
the gate unchecked rather than pass a phase that isn't done.
```

---

## 5. Recovery Prompts

### 5.1 A task is blocked (`- [!]`)

```
ToDos.md has a task marked `- [!]`. Read PROGRESS.md for the recorded
error. Diagnose the root cause rather than retrying blindly — three
attempts already failed. Consider: under-specified? too large? a missing
dependency? a wrong Verify: command?

Then either: (a) fix the real problem and reset to `- [ ]`, (b) split it
into smaller tasks, (c) correct its Files:/Accept:/Verify: fields and
reset, or (d) mark it 🧑 HUMAN if it's genuinely a human decision.

Record your reasoning in PROGRESS.md and commit.
```

### 5.2 The loop is stuck

```
No task has completed in the last several iterations. Diagnose: unmet
dependencies or a dependency cycle? An orphaned `- [~]` from a crashed
iteration? A repo-wide build break failing every Verify:? A missed STOP
file?

Fix the root cause, record it in PROGRESS.md, commit, report what changed.
```

### 5.3 Reverting a bad task

```
git log --oneline -10
git reset --hard <commit-before-the-bad-task>
```
Reset that task's checkbox to `- [ ]` in `ToDos.md` and re-run the loop.

---

## 6. Ad-Hoc Prompts

### 6.1 Status

```
Report build status: tasks complete vs remaining per phase, current phase,
next task, any `- [!]` blocked tasks, the last 5 PROGRESS.md entries. Do
not change anything.
```

### 6.2 Re-plan a phase

```
Phase {{N}} has proven wrong in practice: <what went wrong>.
Re-plan only this phase, keeping the task format and ID scheme. Preserve
completed `- [x]` tasks. Explain what changed and why in PROGRESS.md. Do
not touch other phases.
```

### 6.3 Cross-cutting change (including on a live system, post-Phase-6)

```
A requirement has changed: <the new requirement>.
1. Update plan.md — the relevant section, plus §8 if an assumption changed.
2. Identify every affected ToDos.md task. Completed ones get a new
   `- [ ] P<N>-C<nn>` change task; pending ones are edited in place.
3. If this touches a live, already-launched system, treat it as a new pass
   through the relevant phase's gates (Phase 5) before it ships again — a
   live system doesn't get to skip the review it already passed once.
4. Do not silently widen the scope of an unrelated task.
5. Summarize the impact in PROGRESS.md and commit.
```

---

## 7. Running Unattended — read before enabling

If your harness supports a fully-autonomous / bypass-permissions mode:

- **Always on a branch, never `main`.** Merge only after review.
- **A commit after every task** — any bad iteration reverts with one
  `git reset --hard`.
- **An iteration cap.** Never let it run indefinitely unsupervised.
- **Stuck detection** — N consecutive iterations with no completed task
  stops the loop rather than spinning forever.
- **The `STOP` file convention** — any 🧑 HUMAN task halts immediately.
- **All six Phase 5 gates stay mandatory**, even in unattended mode — never
  let a speed optimization quietly skip code review, security, or UX.

Skim `git log` and `PROGRESS.md` between phases even when running
unattended. Safe to leave alone is not the same as safe to never check.
