# Phase 3 — Design & Accessibility System

**Objective:** Produce a persisted design system, comprehensive component design tokens, and approved screen specifications before frontend/mobile coding begins, guaranteeing UI developers never make arbitrary visual decisions.

## Active Agents

| Agent | Role in this Phase | Tier | Mode |
|---|---|---|---|
| `senior-product-designer` | Information architecture, layout systems, design token curation | Standard | Implement |
| `ui-designer` | High-fidelity screen specifications, micro-interactions, responsive states | Standard | Implement |
| `senior-accessibility-engineer` | WCAG 2.2 AA audit, keyboard focus flows, ARIA semantics | Standard | Implement |
| `brand-guardian` | Brand alignment, visual consistency, conversion review | Standard | Review-only |

## External Tooling Integration
- **New Brand (No Existing Assets):** Execute `ui-ux-pro-max` against the domain category and `pinterest-researcher`'s moodboard direction.
- **Existing Brand Assets (Figma, PDFs, Screenshots):** Ingest brand guidelines via `design-system-skill`.
- **Persistence Mandate:** Persist the generated tokens and rules to `design-system/MASTER.md` before Phase 4 begins.

## Inputs
- Approved `plan.md` (target personas, brand tone, viewport requirements).
- Moodboard and competitor benchmarks from Phase 1.
- Technical API contracts and data models from Phase 2.

## Outputs
- `design-system/MASTER.md` (color tokens, typography scales, spacing units, elevations, radii).
- Page-level override files in `design-system/pages/*.md` if specific flows require unique layouts.
- Component specifications with explicit loading, empty, success, and error states.
- Accessibility focus map and contrast audit report in `docs/design/accessibility-spec.md`.

## Exit Criteria
- `design-system/MASTER.md` is committed and signed off by `brand-guardian`.
- Accessibility specs achieve WCAG 2.2 AA compliance across all proposed color pairs.
- Core user flows are specified in high fidelity so `senior-frontend-engineer` and `senior-mobile-engineer` have zero ambiguity during Phase 4.

## Next Phase
`phases/PHASE-4-BUILD.md`
