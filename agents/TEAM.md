# {{PROJECT_NAME}} — Team & Orchestration Roster

## §1. Full Roster (35 Roles)

| Agent | Phase | Track | Tier | Mode |
|---|---|---|---|---|
| `requirement-analyzer` | 1 Discovery | Shared | Standard | Implement |
| `senior-product-manager` | 1 Discovery | Shared | Standard | Implement |
| `ux-researcher` | 1 Discovery | Shared | Standard | Implement |
| `design-researcher` | 1 Discovery | Shared | Standard | Implement |
| `pinterest-researcher` | 1 Discovery | Shared | Standard | Implement |
| `senior-system-architect` | 2 Architecture | Shared | ★ Senior | Implement |
| `senior-system-designer` | 2 Architecture | Shared | Standard | Implement |
| `senior-cloud-architect` | 2 Architecture | Shared | Standard | Implement |
| `senior-database-architect` | 2 Architecture | Shared | ★ Senior | Implement |
| `senior-security-engineer` | 2 Architecture + 5 Gate | Shared | ★ Senior | Implement (P2) / Review-only (P5) |
| `senior-sre-observability-engineer` | 2 Architecture + 6 Launch | Shared | ★ Senior | Implement |
| `senior-technical-writer` | 2 Architecture + 6 Launch | Shared | Standard | Implement |
| `senior-ai-engineer` | 2–4 AI strategy | AI/ML | ★ Senior | Implement |
| `senior-product-designer` | 3 Design | Shared | Standard | Implement |
| `ui-designer` | 3 Design | Shared | Standard | Implement |
| `senior-accessibility-engineer` | 3 Design + 5 Gate | Shared | Standard | Implement (P3) / Review-only (P5) |
| `brand-guardian` | 3 Design + 5 Gate | Shared | Standard | Review-only |
| `senior-backend-engineer` | 4 Build | Product/Web | Standard | Implement |
| `senior-frontend-engineer` | 4 Build | Product/Web | Standard | Implement |
| `senior-integration-engineer` | 4 Build | Product/Web | Standard | Implement |
| `senior-mobile-engineer` | 4 Build | Product/Web | Standard | Implement |
| `senior-ai-research-engineer` | 4 Build | AI/ML | ★ Senior | Implement |
| `senior-machine-learning-engineer` | 4 Build | AI/ML | Standard | Implement |
| `senior-deep-learning-engineer` | 4 Build | AI/ML | Standard | Implement |
| `senior-llm-engineer` | 4 Build | AI/ML | Standard | Implement |
| `senior-generative-ai-engineer` | 4 Build | AI/ML | Standard | Implement |
| `senior-nlp-engineer` | 4 Build | AI/ML | Standard | Implement |
| `senior-computer-vision-engineer` | 4 Build | AI/ML | Standard | Implement |
| `senior-data-engineer` | 4 Build | AI/ML | Standard | Implement |
| `senior-qa-architect` | 5 Gate (G1) | Shared | Standard | Implement (tests only) |
| `code-reviewer` | 5 Gate (G2) | Shared | Standard | Review-only |
| `visual-qa` | 5 Gate (G4) | Shared | Standard | Review-only |
| `senior-performance-engineer` | 5 Gate (G5) | Shared | Standard | Review-only |
| `senior-mlops-engineer` | 5 Gate (G0-ML) + 6 | AI/ML | Standard | Implement |
| `senior-devops-engineer` | 6 Launch | Shared | Standard | Implement |

Full role briefs are available in `agents/<agent-name>.md`.

---

## §2. Model Tier Policy

**★ Senior tasks must NEVER be delegated to a lower or faster model tier**, regardless of task size. The failure mode of architect-tier tasks is not poor code syntax — it is an undetected domain invariant violation, flawed schema constraint, uncontained security breach, or unrecoverable data corruption in production.

**★ Senior Roles (Mandatory Flagship Tier):**
- `senior-system-architect`: Defines boundaries, modularity, and top-level architecture.
- `senior-database-architect`: Dictates storage schema, migration atomicity, and indexing.
- `senior-security-engineer`: Threat modeling, auth invariants, and OWASP review.
- `senior-sre-observability-engineer`: Telemetry standards, error budgets, and graceful degradation.
- `senior-ai-engineer`: Model selection, AI safety bounds, and architectural orchestration.
- `senior-ai-research-engineer`: Algorithmic and mathematical validation.

All other roles may execute on standard model tiers when bounded by strict acceptance and verification criteria.

---

## §3. File Ownership & Boundary Isolation

File ownership prevents simultaneous write collisions and architectural drift. Two tasks with overlapping file boundaries must never run in parallel. Customize paths at bootstrap for the selected stack:

```
{{schema/migrations path}}         → senior-database-architect only (★)
{{backend services path}}          → senior-backend-engineer, senior-system-architect (★)
{{integrations/webhooks path}}     → senior-integration-engineer
{{frontend components/pages path}} → senior-frontend-engineer, ui-designer
{{mobile app path}}                → senior-mobile-engineer
{{observability/telemetry path}}   → senior-sre-observability-engineer (★)
{{ml/ training+eval path}}         → relevant senior-*-engineer AI/ML role
{{data/ pipelines path}}           → senior-data-engineer
{{design-system/}}                 → senior-product-designer, ui-designer
{{ci/deploy/infra config path}}    → senior-devops-engineer, senior-cloud-architect
{{tests path}}                     → senior-qa-architect (writes tests only, never edits source)
docs/, ADRs, OpenAPI specs         → senior-technical-writer, or owning architect
plan.md, ToDos.md, PROGRESS.md     → coordinator / orchestrator CLI only
```

---

## §4. Standing Production Rules (Every Task, Every Agent)

1. **Domain Hard Rules (`plan.md` §3)**: Non-negotiable domain invariants apply to every line of code written by any agent.
2. **Boundary Validation**: Validate all external inputs at application boundaries using schema validators (Zod, Pydantic, TypeBox). Never trust client payloads.
3. **Atomic Mutations**: Any multi-step write that must succeed or fail together must execute inside an ACID database transaction.
4. **Server-Side Authorization**: Re-verify authorization and tenant isolation on the server on every request. Never rely on client-side route guards.
5. **Exact Financial Quantities**: Financial and precise numerical calculations must never use floating-point numbers. Use integer minor units or high-precision decimal libraries.
6. **Idempotent Mutations & Webhooks**: Every mutating webhook or external payment handler must support idempotency keys and verify cryptographic signatures.
7. **Production Telemetry**: Log using structured JSON with timestamps, log levels, correlation IDs (`trace_id`), and service context. Never emit unstructured `console.log()` or `print()` in production code.
8. **Design System Adherence**: Frontend and mobile UI must strictly consume typography, colors, and layout tokens from `design-system/MASTER.md`.
9. **Accessibility (WCAG 2.2 AA)**: Semantic HTML elements, accessible form labels, keyboard navigability, focus management, and minimum 4.5:1 text contrast are mandatory.
10. **Surgical Scope**: Touch only files declared in the task's `Files:` list. Do not refactor unrelated code. Report pre-existing anomalies to `PROGRESS.md`.
11. **Explicit Escalation**: Unresolved domain ambiguities, credentials requirements, or irreversible operations require a `QUESTION` or `HANDOFF` entry in `PROGRESS.md`. Never guess silently.

---

## §5. Escalation & Autonomous Protocol

When an agent encounters a blocker:
1. If a **Domain Hard Rule** is threatened, an **external credential** is required, or a decision is **costly to reverse**:
   - Write a `HANDOFF` or `QUESTION` entry in `PROGRESS.md`.
   - If human input is required, emit a `STOP` signal.
   - Do not guess or fabricate credentials/mock data to bypass real barriers.
2. If a task fails verification up to 3 times:
   - Mark `- [!]` in `ToDos.md`.
   - Record root-cause diagnosis in `PROGRESS.md`.
   - Halt execution of dependent tasks until resolved.
