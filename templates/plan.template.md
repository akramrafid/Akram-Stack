# {{PROJECT_NAME}} — Plan

> Filled in once, at bootstrap (`PROMPT_LIBRARY.md` §1). Revised only via
> the cross-cutting change prompt (§6.3) — never edited silently mid-build.

## 0. Track

**{{Product/Web | AI/ML | Hybrid}}** — decides which agents activate in
Phase 4. See `README.md`'s track table and `phases/PHASE-4-BUILD.md`.

## 1. What & Why

{{One paragraph: what this product/system does, who it's for, the problem
it solves. Written for someone who's never seen the requirement.}}

## 2. Users & Roles

| Role | Can do | Cannot do |
|---|---|---|
| {{}} | | |

## 3. Domain & Hard Rules

**The most important section in the file.** See `GLOBAL-RULES.md` §2 for
the reasoning. Name this project's non-negotiable invariants explicitly:

1. {{rule}}
2. {{rule}}
3. {{rule}}

## 4. Architecture & Stack

- **Frontend:** {{}}
- **Backend:** {{}}
- **Database:** {{}}
- **Auth:** {{}}
- **Hosting/Infra:** {{}}
- **AI/ML stack (if Track includes AI/ML):** {{frameworks, model providers,
  serving infra}}
- **Key integrations:** {{}}

## 5. Data / Model (high level)

{{Core entities and relationships (Product/Web), or the modeling approach,
data sources, and evaluation strategy (AI/ML). A paragraph, not a full
schema — the schema/architecture itself is a Phase 2 task.}}

## 6. Phases

Standard six-phase shape (`README.md`'s phase map). Note any project-
specific deviation here — most projects don't need one.

## 7. Non-Goals

{{What this explicitly will NOT do in this version.}}

## 8. Open Questions / Assumptions

{{Every genuine ambiguity from the requirement, with the assumption made
and why — resolved here by a human, not guessed silently downstream.}}
