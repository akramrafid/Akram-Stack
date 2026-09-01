# Phase 4 — Build

**Objective:** Implement the tasks Phase 2 generated, one at a time,
through the build loop — the actual product/model gets built here.

## Active agents — by track (from `plan.md` §0)

**Product/Web track:**

| Agent | Owns |
|---|---|
| `senior-backend-engineer` | API routes, services, business logic (non-★) |
| `senior-frontend-engineer` | Components, pages, client state |

**AI/ML track:**

| Agent | Owns |
|---|---|
| `senior-ai-research-engineer` | Novel technique validation (★) |
| `senior-machine-learning-engineer` | Classical ML, structured data |
| `senior-deep-learning-engineer` | Neural architectures, training infra |
| `senior-llm-engineer` | LLM systems, prompt engineering, RAG |
| `senior-generative-ai-engineer` | Multimodal/diffusion generation |
| `senior-nlp-engineer` | Text classification, embeddings, extraction |
| `senior-computer-vision-engineer` | Image/video processing, detection |
| `senior-data-engineer` | Pipelines feeding every AI/ML role above |

**Hybrid track:** both tables apply, on their own files — see
`agents/TEAM.md` §3 for the file-ownership boundary between them.

## How to run this phase

Use `PROMPT_LIBRARY.md` §2 (single task) or §3 (whole phase). Every task
was generated in Phase 2 with an `Owner:` field — the agent reads its own
role brief in `agents/` before touching anything.

## Inputs

`ToDos.md` Phase 4 task list, the schema/API contracts from Phase 2,
`design-system/MASTER.md` from Phase 3.

## Outputs

The actual implemented product/model. Every task ends in a commit, per
`ToDos.md` §0.

## Exit

Every `- [ ]` task in this phase's section of `ToDos.md` is `- [x]`. No
task is `- [!]` blocked without a recorded diagnosis in `PROGRESS.md`.

## Next

`phases/PHASE-5-QUALITY-SECURITY.md`
