# Phase 4 — Build Loop

**Objective:** Implement all tasks generated in Phase 2 in dependency order through the deterministic build loop. This is where the product, APIs, UI, mobile experiences, and AI/ML pipelines are engineered.

## Active Agents by Track

### Product/Web Track
| Agent | Core Ownership | Tier |
|---|---|---|
| `senior-backend-engineer` | API routes, domain services, business logic (non-★) | Standard |
| `senior-frontend-engineer` | Components, pages, client state, Core Web Vitals | Standard |
| `senior-integration-engineer` | Payment gateways, webhooks, third-party APIs, idempotency | Standard |
| `senior-mobile-engineer` | Cross-platform mobile apps (React Native/Expo/Flutter/PWA) | Standard |

### AI/ML Track
| Agent | Core Ownership | Tier |
|---|---|---|
| `senior-ai-research-engineer` | Novel algorithmic and mathematical validation | ★ Senior |
| `senior-machine-learning-engineer` | Tabular/classical ML models, feature engineering | Standard |
| `senior-deep-learning-engineer` | Deep neural network architectures and training runs | Standard |
| `senior-llm-engineer` | LLM systems, structured outputs, prompt templates, RAG | Standard |
| `senior-generative-ai-engineer` | Multimodal and diffusion generation pipelines | Standard |
| `senior-nlp-engineer` | Text processing, embeddings, semantic tokenization | Standard |
| `senior-computer-vision-engineer` | Image/video analysis, detection, segmentation | Standard |
| `senior-data-engineer` | Data ingestion pipelines, feature stores, data cleaning | Standard |

### Hybrid Track
Both tables apply. Agents operate on strictly isolated files defined in `agents/TEAM.md` §3 File Ownership.

## Execution via Orchestrator CLI

Each task is executed through the `akstack` CLI loop:

```bash
# 1. Determine next runnable task (verifies dependencies and topological order)
python -m orchestrator.cli next

# 2. Mark task as in-progress
python -m orchestrator.cli start <task-id>

# 3. Implement strictly within declared Files: boundary.
# Read agents/<owner>.md before editing code.

# 4. Complete task (runs Verify command, appends to PROGRESS.md, commits to git)
python -m orchestrator.cli complete <task-id>
```

For parallel wave execution (when multiple independent tasks share no overlapping files):
```bash
python -m orchestrator.cli next --parallel
```

## Exit Criteria
- Every `- [ ]` task in `ToDos.md` Phase 4 is marked `- [x]`.
- Zero `- [!]` blocked tasks remaining.
- All code committed with standard `<TASK-ID>: <title>` messages.

## Next Phase
`phases/PHASE-5-QUALITY-SECURITY.md`
