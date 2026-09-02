# Phase 5 — Quality & Security Gating

**Objective:** Execute the strict quality, security, accessibility, and performance gate sequence. Every review-only gate logs actionable findings as new `-F` tasks; reviewers NEVER grade or fix their own findings.

## Gate Sequence

| Gate | Agent | Focus / Review Bar | Mode |
|---|---|---|---|
| **G0-ML** *(AI/ML only)* | `senior-mlops-engineer` | Model lineage, reproducible training, metric threshold cleared | Implement |
| **G1 Test** | `senior-qa-architect` | Automated test suite 100% green, Hard Rules tested first | Implement (tests only) |
| **G2 Code Review** | `code-reviewer` | Clean architecture, error handling, maintainability, ownership | Review-only |
| **G3 Security** | `senior-security-engineer` | OWASP Top 10 + ASVS, auth boundaries, Hard Rules verification | Review-only |
| **G4 UX/Visual** | `visual-qa` + `brand-guardian` | Breakpoint fidelity, design system compliance, Impeccable slop check | Review-only |
| **G4-A11Y Accessibility** | `senior-accessibility-engineer` | WCAG 2.2 AA compliance, axe-core audit, keyboard navigation | Review-only |
| **G5 Performance** | `senior-performance-engineer` | Core Web Vitals, API latency, Lighthouse CI thresholds | Review-only |
| **G6 Sign-Off** | coordinator / CLI | All prior gates `- [x]`, regression suite green, tag release | Sign-off |

Exact prompts and checklists: `PROMPT_LIBRARY.md` §4.

## How Findings Flow
- Every Critical and High finding from G2 through G5 becomes a new `-F` task (e.g. `P5-F01`) filed directly below the evaluating gate in `ToDos.md`.
- Tasks are assigned to the responsible implementation engineer.
- The gate remains unchecked until all filed finding tasks are implemented, verified, and re-reviewed.

## CLI Gate Execution

```bash
# Validate and clear a gate once preconditions are met
python -m orchestrator.cli gate P5-G1
```

## Exit Criteria
- All gates G0-ML through G6 are checked `- [x]`.
- Zero unresolved Critical or High security, test, or accessibility defects.
- Full regression suite exits with code 0.
- `git tag phase-5-complete`.

## Next Phase
`phases/PHASE-6-DEVOPS-LAUNCH.md`
