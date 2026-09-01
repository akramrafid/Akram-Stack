# Phase 5 — Quality & Security

**Objective:** Six gates, run in order, before anything from this phase is
considered shippable. Every review-only gate files findings as tasks — it
never fixes what it finds.

## Gate sequence

| Gate | Agent | Reviews for | Mode |
|---|---|---|---|
| G0-ML *(AI/ML track only, runs before G1)* | `senior-mlops-engineer` | Model lineage, versioned data, eval threshold cleared | Implement |
| G1 Test | `senior-qa-architect` | Suite genuinely green, Hard Rules tested first | Implement (tests only) |
| G2 Code Review | `code-reviewer` | Industry-standard quality, maintainability, edge cases, error handling, Hard Rule/ownership compliance | Review-only |
| G3 Security | `senior-security-engineer` | OWASP baseline + Hard Rules | Review-only |
| G4 UX/Visual | `visual-qa` + `brand-guardian` | Pixel/breakpoint fidelity, brand + Impeccable critique | Review-only |
| G5 Performance | `senior-performance-engineer` | Core Web Vitals / API latency budget | Review-only |
| G6 Sign-off | coordinator | All above `- [x]`, exit criteria demonstrated | — |

Exact prompts for each gate: `PROMPT_LIBRARY.md` §4.

## How findings flow

Every Critical/High finding from G2-G5 becomes a new `-F` task filed
directly below that gate in `ToDos.md`, owned by whichever role should fix
it. The gate stays unchecked until none remain open. This is what keeps a
review honest — the reviewer never grades its own fix.

## Inputs

Everything built in Phase 4.

## Outputs

A written report per gate, fix tasks for anything Critical/High, and (once
clean) `git tag phase-<N>-complete`.

## Exit

All six gates `- [x]`. `PROGRESS.md` has a phase summary entry.

## Next

`phases/PHASE-6-DEVOPS-LAUNCH.md`
