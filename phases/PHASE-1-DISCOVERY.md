# Phase 1 — Discovery

**Objective:** Transform raw product requirements into a structured, ambiguity-free plan approved by a human stakeholder before any architecture or code is authored.

## Active Agents

| Agent | Role in this Phase | Tier | Mode |
|---|---|---|---|
| `requirement-analyzer` | Capability breakdown, constraints, SEO scope, track selection | Standard | Implement |
| `senior-product-manager` | PRD, prioritized user stories, acceptance criteria, non-goals | Standard | Implement |
| `ux-researcher` | Personas, user journeys, task flow mapping | Standard | Implement |
| `design-researcher` | Competitor interaction patterns and mental models | Standard | Implement |
| `pinterest-researcher` | Visual moodboard direction & aesthetic benchmarking | Standard | Implement |

Run sequentially: `requirement-analyzer` runs first to establish the capability map. The remaining discovery agents can run in parallel since their investigative outputs do not collide.

## Inputs
- Raw product requirement in plain language from the user.
- Relevant domain context, target audience, and business objectives.

## Outputs
- `plan.md` §0 (Track confirmed: Product/Web, AI/ML, or Hybrid).
- `plan.md` §1-2 (What & Why, Users & Roles) filled in detail.
- `plan.md` §8 (Non-Goals) populated to prevent scope creep.
- `plan.md` §9 (Open Questions & Assumptions) logged explicitly.
- Discovery documentation in `docs/discovery/` (personas, journey maps, competitor benchmark).

## Exit Criteria
- Human stakeholder has read and approved `plan.md` §1-2 and §8-9.
- Zero unresolved, hidden ambiguities in the requirement.
- Phase 2 tasks generated in `ToDos.md`.

## Next Phase
`phases/PHASE-2-ARCHITECTURE.md`
