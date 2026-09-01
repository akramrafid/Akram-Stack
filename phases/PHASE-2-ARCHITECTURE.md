# Phase 2 — Architecture

**Objective:** Turn the approved plan into a concrete technical shape —
architecture, schema, contracts, and (this phase's most important output)
the project's Hard Rules — before any feature code is written.

## Active agents

| Agent | Role in this phase | Tier |
|---|---|---|
| `senior-system-architect` | Top-level architecture, rendering strategy | ★ |
| `senior-system-designer` | API contracts, interfaces, data flow | Standard |
| `senior-cloud-architect` | Infra topology, cost | Standard |
| `senior-database-architect` | Schema, migrations, indexing | ★ |
| `senior-security-engineer` | Auth design, threat model | ★ |
| `senior-ai-engineer` | AI/ML system architecture (AI/ML or Hybrid track only) | ★ |

`senior-system-architect` goes first — everything else in this phase builds
within the shape it sets. `senior-database-architect` and
`senior-security-engineer` are ★ — never delegate their tasks to a
faster model tier, even ones that look small.

## Inputs

`plan.md` §1-2 from Phase 1, the chosen track (`plan.md` §0).

## Outputs

`plan.md` §3 (Hard Rules — the most important artifact of this whole
phase), §4-6 finalized. Schema/migration files. API contract specs.
`agents/TEAM.md` §3 File Ownership updated for the actual stack. Phase 4
task list generated in `ToDos.md`.

## Exit

A human has reviewed `plan.md` §3 specifically — this is where a rushed
review costs the most later. Schema exists and migrates cleanly. Every
Phase 4 task has a clear Owner, Files:, and Verify:.

## Next

`phases/PHASE-3-DESIGN.md`
