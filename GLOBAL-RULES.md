# Global Rules

Every agent in `agents/` inherits these without being told twice. They're
listed here once so a fresh clone on a machine that hasn't set up the global
tooling yet still carries the reasoning, not just the mechanism.

## 1. Coding discipline (Karpathy-style, enforced globally via GEMINI.md)

- **Think before coding.** State assumptions. If multiple interpretations
  exist, name them instead of silently picking one. Stop and ask when
  something is genuinely unclear.
- **Simplicity first.** The minimum code that solves the problem. No
  speculative flexibility, no configurability nobody asked for.
- **Surgical changes.** Touch only what the task requires. Don't "improve"
  adjacent code while you're in there. Match existing style even if you'd
  do it differently.
- **Goal-driven execution.** Turn every task into a verifiable success
  condition before starting, not after.

If `~/.gemini/GEMINI.md` is set up on this machine, these are already
enforced on every action automatically. If not, treat this section as
standing instruction until it is.

## 2. Domain Hard Rules (project-specific, written once per project)

Every domain has a small number of invariants that, if silently violated,
corrupt data or cause real harm. `plan.md` §3 names them explicitly for
*this* project. Examples, for calibration — not a checklist to copy:

- Financial system: money is never a floating-point number; every mutation
  writes an audit row; every multi-table write is transactional.
- Carbon-market platform: a credit is never counted twice across two
  registries; retirement is irreversible and append-only.
- ML system in production: no unversioned dataset or untracked
  hyperparameter change ships; every prediction is traceable to the model
  version that produced it.

Every agent, regardless of role, enforces `plan.md` §3 in anything it
touches. This is not the security engineer's job alone.

## 3. File ownership

Each agent touches only the files its current task names. Two tasks with
overlapping files never run in the same wave — sequence them instead.
Overlapping, unreviewed changes to the same file are the single most common
way an autonomous build corrupts itself.

## 4. Review-only roles never edit code

`brand-guardian`, `senior-security-engineer` (in gate mode), `visual-qa`,
and `code-reviewer` file findings as new tasks. They do not fix what they
find — that keeps the review honest and keeps a fix from being rushed
through by the same pass that's supposed to be catching it.

## 5. Escalation, not guessing

Anything that would violate a Hard Rule, needs a credential or physical
action, or is genuinely ambiguous in a costly-to-reverse way gets a HANDOFF
or QUESTION entry in `PROGRESS.md` — never a silent guess. See
`ToDos.md` §0 and `PROMPT_LIBRARY.md` §5.
