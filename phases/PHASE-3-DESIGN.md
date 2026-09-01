# Phase 3 — Design

**Objective:** A persisted design system and approved high-fidelity screens
— before Phase 4 build starts, so frontend work never has to invent visual
decisions on the fly.

## Active agents

| Agent | Role in this phase | Mode |
|---|---|---|
| `senior-product-designer` | Information architecture, design system curation | Implement |
| `ui-designer` | High-fidelity screens, micro-interactions | Implement |
| `brand-guardian` | Ongoing brand/conversion review as screens land | Review-only |

## External tools this phase calls

- **New brand, no existing assets:** `ui-ux-pro-max` generates the design
  system from the product category + `pinterest-researcher`'s direction.
- **Existing brand assets (PDFs, Figma, screenshots):** `design-system-skill`
  ingests them instead — don't let the reasoning engine invent a palette
  when a real one already exists.
- Either way, **persist the result** to `design-system/MASTER.md` before
  Phase 4 starts. See `PROMPT_LIBRARY.md` §1 for the exact persist command.

## Inputs

`plan.md`, personas/journeys and moodboard direction from Phase 1, the
information architecture this phase produces.

## Outputs

`design-system/MASTER.md` (+ `design-system/pages/*.md` overrides as
needed), high-fidelity screen specs for Phase 4's core flows.

## Exit

`design-system/MASTER.md` exists and brand-guardian has signed off on it.
Core screens are specified precisely enough for `senior-frontend-engineer`
to build against without re-deciding visual details mid-implementation.

## Next

`phases/PHASE-4-BUILD.md`
