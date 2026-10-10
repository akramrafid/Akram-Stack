# Akram-Stack (`akstack`) — Master Documentation & Operations Manual

> **Production-Grade Multi-Agent Orchestration Operating System for Full-Stack, AI/ML, and Hybrid Systems**

---

## Table of Contents

1. [Executive Overview & Core Philosophy](#1-executive-overview--core-philosophy)
2. [Disk-Driven State Architecture](#2-disk-driven-state-architecture)
3. [The 7-Phase Engineering Lifecycle](#3-the-7-phase-engineering-lifecycle)
4. [The 3-Track System](#4-the-3-track-system)
5. [CLI Orchestrator Engine (`akstack`)](#5-cli-orchestrator-engine-akstack)
6. [Complete Agent Roster & Roles (`.agents/agents/`)](#6-complete-agent-roster--roles-agentsagents)
7. [The Skills Ecosystem (`.agents/skills/`)](#7-the-skills-ecosystem-agentsskills)
8. [Workflows & Slash Commands (`.agents/workflows/`)](#8-workflows--slash-commands-agentsworkflows)
9. [Quality Gates & Verification Protocol (Phase 5)](#9-quality-gates--verification-protocol-phase-5)
10. [Frontend Quality Contract & Design Lock](#10-frontend-quality-contract--design-lock)
11. [Step-by-Step Operator Playbook (Unlocking Full Potential)](#11-step-by-step-operator-playbook-unlocking-full-potential)
12. [Repository Directory Structure](#12-repository-directory-structure)

---

## 1. Executive Overview & Core Philosophy

Most AI-assisted software projects fail as they scale because **context scrolls away in conversation windows**. LLMs hallucinate previous decisions, silently violate architecture invariants, overwrite other agents' files, and accumulate technical debt that cannot be audited.

**Akram-Stack (`akstack`)** eliminates these failure modes by transforming AI development into a **deterministic, disk-driven, multi-agent assembly line**:

- **Disk is the Source of Truth**: Chat memory is treated as ephemeral and untrusted. Every work session orients from markdown ledgers on disk (`plan.md`, `ToDos.md`, `PROGRESS.md`).
- **Zero Third-Party Engine Dependencies**: The orchestrator engine runs on pure Python ≥ 3.10 standard library, guaranteeing portability across Windows, Linux, and macOS.
- **Strict File Ownership & Isolation**: Agents operate within non-overlapping file lists. Parallel tasks execute without git merge conflicts.
- **Enforced Domain Invariants (Hard Rules)**: Architecture invariants (integer currency, tenant isolation, idempotency, strict schema validation) are locked in `plan.md` §3 and cannot be bypassed.
- **Separation of Implementers vs. Reviewers**: Verification gates (G2 Code Review, G3 Security, G3-P Privacy, G4 Visual, G4-CRO, G4-A11Y, G5 Performance) are **review-only**. Reviewers cannot fix code they inspect; they file actionable `-F` remediation tasks.
- **Model Tiering Policy**: High-stakes architecture, schema, security, and coordinator tasks (**★ Senior**) are pinned to flagship reasoning models.

---

## 2. Disk-Driven State Architecture

Every project bootstrapped with `akstack` maintains four core continuity artifacts in its root:

```
my-project/
├── plan.md            — System Architecture, Domain Hard Rules, SLO Budgets, Non-Goals
├── ToDos.md           — Machine-Parsable Directed Acyclic Graph (DAG) Task Ledger
├── PROGRESS.md        — Append-Only Historical Execution Journal
└── .akstack.lock      — Multi-process lock file serializing disk and git mutations
```

### 2.1 `plan.md` (The Constitution)
- **§0 Track**: Declares project track (`Product/Web`, `AI/ML`, or `Hybrid`).
- **§1–2 Requirements & Personas**: Exact problem statements, user journeys, target scale.
- **§3 Domain & Hard Rules**: **The most critical section**. Invariants that, if violated, corrupt data or cause production failure (e.g., zero float math for financials, tenant ID on every query).
- **§4 Architecture & Tech Stack**: Topological diagrams, database selection, protocol definitions.
- **§5 Schema & Storage Invariants**: Table schemas, migrations, caching boundaries.
- **§6 SLO Budgets**: Latency percentiles (P95 < 300ms), Core Web Vitals, accessibility standards.
- **§8 Non-Goals**: Explicit boundaries preventing feature creep.
- **§9 Open Questions**: Ambiguities surfaced during discovery.

### 2.2 `ToDos.md` (The Machine-Parsable Task Ledger)
Tasks follow strict syntax parsed by `orchestrator/parser.py`:

```markdown
- [ ] **P4-T012** Implement Stripe webhook idempotent handler
  - **Owner:** senior-backend-engineer
  - **Deps:** P4-T010, P4-T011
  - **Files:** src/services/billing/webhook.ts, src/services/billing/events.ts
  - **Do:** Handle charge.succeeded and invoice.payment_failed with idempotency keys.
  - **Accept:** Duplicate webhooks return 200 with no duplicate ledger entries.
  - **Verify:** `npm test tests/billing/webhook.test.ts`
```

#### Task Status Identifiers:
- `- [ ]` **Pending**: Waiting for dependencies or dispatch.
- `- [~]` **In-Progress**: Currently locked and executing.
- `- [x]` **Completed**: Verification passed, journal appended, git commit generated.
- `- [!]` **Failed / Blocked**: Failed verification or halted for diagnosis.
- `- [-]` **Skipped**: Explicitly bypassed with documented justification.

#### Task ID Taxonomy:
- `P<n>-T<nnn>`: Standard implementation task (e.g., `P4-T005`).
- `P<n>-G<n>`: Quality, security, or release gate (e.g., `P5-G1`, `P5-G3-P`, `P5-G4-CRO`).
- `P<n>-F<nn>`: Remediation fix task filed under a failing gate.
- `P<n>-C<nn>`: Cross-cutting requirement change request.

### 2.3 `PROGRESS.md` (The Immutable Journal)
Records every state transition in reverse chronological order:
- Timestamps, task ID, owner, exit status.
- Verification command and output.
- Files modified and git commit SHA.
- Open questions, handoffs, and blocked states.

### 2.4 Human Intervention & Handoff Protocols
- **`STOP` file**: When a human approval or credential blocker occurs, `akstack handoff` writes a `STOP` file. All agents halt immediately until human sign-off via `akstack approve` or `akstack resume`.
- **`akstack question`**: If requirements are ambiguous and costly to reverse, agents must ask instead of silently guessing.

---

## 3. The 7-Phase Engineering Lifecycle

Every product progresses through 7 sequential phases:

```
Phase 0: Setup
   └── Dependencies installed, templates initialized, browser evidence kit ready
Phase 1: Discovery
   └── Requirements analyzed, personas defined, capabilities mapped, open questions answered
Phase 2: Architecture
   └── Hard Rules (§3) locked, database schemas drafted, API specs created, C4 diagrams rendered
Phase 3: Design
   └── Design system created, screen specs written, SEO/funnel matrices defined, P3-G1 human sign-off
Phase 4: Build
   └── Deterministic build loop, strict file isolation, parallel wave execution
Phase 5: Quality & Security
   └── Sequential gates G0-ML → G6, review-only audits, remediation tasks (-F)
Phase 6: DevOps & Launch
   └── CI/CD pipelines, container hardening, observability dashboards, staging/prod deploy
```

| Phase | Specifications | Key Artifacts | Lead Roles |
|---|---|---|---|
| **0 — Setup** | `phases/PHASE-0-SETUP.md` | Initialized repository, evidence kits, CI scripts | `coordinator`, CLI |
| **1 — Discovery** | `phases/PHASE-1-DISCOVERY.md` | `plan.md` §1-2, capabilities, personas, user journeys | `requirement-analyzer`, `senior-product-manager`, `ux-researcher` |
| **2 — Architecture** | `phases/PHASE-2-ARCHITECTURE.md` | `plan.md` §3-6, schema migrations, OpenAPI, ADRs | `senior-system-architect` (★), `senior-database-architect` (★), `senior-security-engineer` (★) |
| **3 — Design** | `phases/PHASE-3-DESIGN.md` | `design-system/MASTER.md`, screen specs, CRO/SEO matrix | `senior-product-designer`, `ui-designer`, `design-system-engineer`, `growth-cro-engineer` |
| **4 — Build** | `phases/PHASE-4-BUILD.md` | Verified application code, unit tests, integration tests | Track implementation roles (`senior-backend-engineer`, `senior-frontend-engineer`, etc.) |
| **5 — Quality & Security** | `phases/PHASE-5-QUALITY-SECURITY.md` | Test reports, security scans, visual QA, a11y, privacy audit | `senior-qa-architect`, `code-reviewer`, `senior-security-engineer`, `senior-privacy-engineer` |
| **6 — DevOps & Launch** | `phases/PHASE-6-DEVOPS-LAUNCH.md` | Dockerfiles, Terraform, CI/CD, Grafana, SLO alerts, runbooks | `senior-devops-engineer`, `senior-sre-observability-engineer`, `senior-mlops-engineer` |

---

## 4. The 3-Track System

The active agents in Phase 4 (Build) depend on the project track declared in `plan.md` §0:

### Track 1: Product/Web
- **Focus**: Web portals, SaaS platforms, responsive apps, API services, mobile apps.
- **Active Build Roles**:
  - `senior-backend-engineer`
  - `senior-frontend-engineer`
  - `senior-integration-engineer`
  - `senior-mobile-engineer`
- **Mandatory Gates**: G1, G2, G3, G3-P, G4 (Visual), G4-CRO, G4-A11Y, G5, G6.

### Track 2: AI/ML
- **Focus**: Research pipelines, fine-tuning, RAG architectures, CV/NLP models, data pipelines.
- **Active Build Roles**:
  - `senior-ai-research-engineer` (★)
  - `senior-machine-learning-engineer`
  - `senior-deep-learning-engineer`
  - `senior-llm-engineer`
  - `senior-generative-ai-engineer`
  - `senior-nlp-engineer`
  - `senior-computer-vision-engineer`
  - `senior-data-engineer`
- **Mandatory Gates**: G0-ML (Lineage & Eval threshold), G1, G2, G3, G3-P, G5, G6.

### Track 3: Hybrid
- **Focus**: Full-stack applications with integrated generative AI, embeddings, or ML inference.
- **Active Build Roles**: Both Product/Web and AI/ML groups, working in strictly isolated files defined in `.agents/TEAM.md` §3.
- **Mandatory Gates**: All gates G0-ML through G6.

---

## 5. CLI Orchestrator Engine (`akstack`)

Akram-Stack includes a zero-dependency CLI written in Python 3. Launch it via:
```bash
python -m orchestrator.cli <command> [options]
# Or using the launcher scripts:
./bin/akstack <command>        # Unix / macOS
.\bin\akstack.bat <command>    # Windows
```

### Complete CLI Command Reference

#### 1. System Health & Inspection
- `akstack doctor` — Verifies Python version, Git, templates, agent briefs, phase docs, Node/NPM/NPX, and ledger state.
- `akstack doctor --frontend` — Performs comprehensive frontend contract checks.
- `akstack status` — Displays human-readable ASCII table of phase progress, active tasks, gates, and blockers.
- `akstack status --json` — Emits structured JSON state for autonomous agent consumption.
- `akstack lint` — Validates the entire task DAG: cycles, unmet dependencies, task ID formatting, and owner brief presence.
- `akstack graph --mermaid` — Generates a Mermaid diagram representing the full task dependency graph.

#### 2. Project Bootstrapping
- `akstack init "<Project Name>" --track <Product/Web|AI/ML|Hybrid>` — Seeds `.agents/`, `templates/`, `phases/`, and creates `plan.md`, `ToDos.md`, and `PROGRESS.md`.
- `akstack init "<Project Name>" --force` — Overwrites existing ledgers (use with caution).

#### 3. Task Selection & Dispatch
- `akstack next` — Analyzes the DAG and outputs the single next runnable task respecting topological order.
- `akstack next --parallel` — Analyzes all runnable tasks and groups them into **conflict-free parallel execution waves** whose `Files:` lists do not overlap.
- `akstack packet` — Generates a complete, context-isolated execution packet for the current/next task, containing task instructions, owner role brief, domain Hard Rules, and team rules.
- `akstack packet --task <id>` — Generates execution packet for a specific task ID.

#### 4. Task Execution Lifecycle
- `akstack start <task-id>` — Transitions task to in-progress (`- [~]`). Fails if dependencies are unmet or a `STOP` file is active.
- `akstack complete <task-id>` — Executes the task's `Verify:` command. If exit code is 0:
  1. Marks task complete (`- [x]`).
  2. Appends entry to `PROGRESS.md`.
  3. Stages declared files only (`git add <files>`).
  4. Commits to git with structured message (`feat(P4): complete P4-T005 ...`).
- `akstack fail <task-id> --error "<diagnosis>"` — Increments failure count, logs diagnosis to `PROGRESS.md`, and marks task `- [!]` if max retries (3) exceeded.
- `akstack reset <task-id>` — Resets failed task back to pending (`- [ ]`).

#### 5. Quality & Security Gates (Phase 5)
- `akstack gate <gate-id> --evidence <workspace-relative-path>` — Validates and clears a quality gate. Verifies prerequisites, checks report contents, and records sign-off.
- `akstack finding <gate-id> --title "<title>" --owner <agent> --severity <Critical|High|Medium|Low> --file <path:line> --issue "<issue>" --fix "<fix>"` — Files a formal remediation `-F` task directly under the specified gate in `ToDos.md`.

#### 6. Human Approvals & Blocker Management
- `akstack handoff <task-id> --blocked-on "<reason>" --why "<explanation>"` — Creates `STOP` file, halts autonomous execution, and logs handoff requirement.
- `akstack approve <human-task-id> --notes "<decision>" --evidence <report-path>` — Records human approval for human tasks (`🧑 HUMAN`).
- `akstack resume --notes "<resolution>"` — Removes `STOP` file and allows the build loop to continue.
- `akstack question <task-id> --ambiguity "<query>" --risk "<impact>" --recommended "<suggestion>"` — Formats and logs architectural questions that require stakeholder clarity.

#### 7. Frontend Quality Contract
- `akstack frontend-check --area <all|design-system|screens|tokens|funnel|evidence>` — Runs automated validation checks against frontend specifications in `design-system/MASTER.md`, `docs/screens/`, and component traceability matrices.

---

## 6. Complete Agent Roster & Roles (`.agents/agents/`)

All agent role briefs reside in [`.agents/agents/`](file:///d:/akstack/.agents/agents/). Each role has narrow responsibilities, explicit inputs/outputs, and defined tool allowances.

### 6.1 The 42 Akram-Stack Core Roles

#### Orchestration & Coordination
- [`coordinator`](file:///d:/akstack/.agents/agents/coordinator.md) (**★ Senior**) — The operating system of akstack. Reads disk, dispatches tasks, checks gates, manages human halts, enforces boundaries. **Never writes application code.**

#### Discovery & Product Architecture (Phase 1)
- [`requirement-analyzer`](file:///d:/akstack/.agents/agents/requirement-analyzer.md) — Analyzes natural-language requests, extracts capabilities, personas, and edge cases.
- [`senior-product-manager`](file:///d:/akstack/.agents/agents/senior-product-manager.md) — Crafts product strategy, defines feature scope, user stories, and acceptance criteria.
- [`ux-researcher`](file:///d:/akstack/.agents/agents/ux-researcher.md) — Defines user journeys, information architecture, cognitive walk-throughs, and user needs.
- [`design-researcher`](file:///d:/akstack/.agents/agents/design-researcher.md) — Evaluates competitive aesthetics, industry benchmarks, and interaction patterns.
- [`pinterest-researcher`](file:///d:/akstack/.agents/agents/pinterest-researcher.md) — Curates visual references, moodboards, color harmonies, and typography directions.
- [`content-designer`](file:///d:/akstack/.agents/agents/content-designer.md) — Writes product copy, empty states, transactional messaging, error copy, and tone guidelines.

#### Architecture, System Design & Infrastructure (Phase 2)
- [`senior-system-architect`](file:///d:/akstack/.agents/agents/senior-system-architect.md) (**★ Senior**) — Defines overall system topology, C4 diagrams, service boundaries, and communication protocols.
- [`senior-system-designer`](file:///d:/akstack/.agents/agents/senior-system-designer.md) — Designs low-level component interactions, caching strategies, and event choreography.
- [`senior-cloud-architect`](file:///d:/akstack/.agents/agents/senior-cloud-architect.md) — Selects cloud infrastructure (AWS/GCP/Azure), serverless/container topologies, and VPC networking.
- [`senior-database-architect`](file:///d:/akstack/.agents/agents/senior-database-architect.md) (**★ Senior**) — Designs relational/NoSQL schemas, normalization, indexing, partitioning, and zero-downtime migration plans.
- [`senior-security-engineer`](file:///d:/akstack/.agents/agents/senior-security-engineer.md) (**★ Senior**) — Threat models (STRIDE), defines authentication/authorization (OAuth2/RBAC), secrets management, and cryptographic standards.
- [`senior-privacy-engineer`](file:///d:/akstack/.agents/agents/senior-privacy-engineer.md) (**★ Senior**) — Enforces GDPR/CCPA compliance, data minimization, consent architectures, DPIA, and audit logs.
- [`senior-sre-observability-engineer`](file:///d:/akstack/.agents/agents/senior-sre-observability-engineer.md) (**★ Senior**) — Defines SLIs/SLOs, OpenTelemetry tracing, Prometheus metrics, structured logging, and alerting rules.
- [`senior-technical-writer`](file:///d:/akstack/.agents/agents/senior-technical-writer.md) — Authors ADRs (Architecture Decision Records), developer onboarding docs, and OpenAPI 3.1 specifications.

#### Design, UI/UX & Design Systems (Phase 3)
- [`senior-product-designer`](file:///d:/akstack/.agents/agents/senior-product-designer.md) — Creates comprehensive screen specifications, responsive wireframes, and user flows.
- [`ui-designer`](file:///d:/akstack/.agents/agents/ui-designer.md) — Establishes visual hierarchy, micro-interactions, layout grids, and aesthetic polish.
- [`design-system-engineer`](file:///d:/akstack/.agents/agents/design-system-engineer.md) — Converts design tokens into reusable UI components (`design-system/MASTER.md`).
- [`senior-accessibility-engineer`](file:///d:/akstack/.agents/agents/senior-accessibility-engineer.md) — Enforces WCAG 2.2 AA / AAA standards, focus traps, screen-reader semantics, and APCA contrast.
- [`brand-guardian`](file:///d:/akstack/.agents/agents/brand-guardian.md) — Protects brand voice, visual thesis, asset usage, and aesthetic integrity.

#### Frontend Growth, CRO, SEO & Analytics (Phases 1, 3, 4, 5)
- [`growth-cro-engineer`](file:///d:/akstack/.agents/agents/growth-cro-engineer.md) — Optimizes acquisition funnels, value propositions, checkout flows, and ethical conversion mechanisms.
- [`product-analytics-engineer`](file:///d:/akstack/.agents/agents/product-analytics-engineer.md) — Implements event schemas, privacy-compliant tracking plans, and retention funnel measurement.
- [`technical-seo-engineer`](file:///d:/akstack/.agents/agents/technical-seo-engineer.md) — Builds structured schema (JSON-LD), sitemaps, OpenGraph metadata, and Core Web Vitals optimization.

#### Implementation — Product/Web Track (Phase 4)
- [`senior-backend-engineer`](file:///d:/akstack/.agents/agents/senior-backend-engineer.md) — Implements API controllers, business logic, ORM models, transactional boundaries, and background workers.
- [`senior-frontend-engineer`](file:///d:/akstack/.agents/agents/senior-frontend-engineer.md) — Implements responsive React/Vue/Svelte components, client state, routing, and browser rendering.
- [`senior-integration-engineer`](file:///d:/akstack/.agents/agents/senior-integration-engineer.md) — Integrates external third-party APIs (Stripe, Twilio, SendGrid, OAuth providers, Webhooks).
- [`senior-mobile-engineer`](file:///d:/akstack/.agents/agents/senior-mobile-engineer.md) — Implements React Native / Flutter / native iOS/Android features, offline sync, and device sensors.

#### Implementation — AI/ML Track (Phase 4)
- [`senior-ai-engineer`](file:///d:/akstack/.agents/agents/senior-ai-engineer.md) — Bridges software engineering and AI; designs LLM pipelines and embedding workflows.
- [`senior-ai-research-engineer`](file:///d:/akstack/.agents/agents/senior-ai-research-engineer.md) (**★ Senior**) — Mathematical modeling, novel algorithm implementation, loss function design, experiment validation.
- [`senior-machine-learning-engineer`](file:///d:/akstack/.agents/agents/senior-machine-learning-engineer.md) — Model training pipelines, hyperparameter tuning, scikit-learn/XGBoost, and tabular workflows.
- [`senior-deep-learning-engineer`](file:///d:/akstack/.agents/agents/senior-deep-learning-engineer.md) — PyTorch/TensorFlow deep networks, neural backbones, GPU memory optimization.
- [`senior-llm-engineer`](file:///d:/akstack/.agents/agents/senior-llm-engineer.md) — RAG systems, vector search, chunking strategies, prompt engineering, structured JSON outputs.
- [`senior-generative-ai-engineer`](file:///d:/akstack/.agents/agents/senior-generative-ai-engineer.md) — Diffusion models, multimodal image/audio generation, ComfyUI/fal.ai pipelines.
- [`senior-nlp-engineer`](file:///d:/akstack/.agents/agents/senior-nlp-engineer.md) — Tokenization, semantic embeddings, entity recognition, language classification, multilingual NLP.
- [`senior-computer-vision-engineer`](file:///d:/akstack/.agents/agents/senior-computer-vision-engineer.md) — Object detection (YOLO), image segmentation, OpenCV, video analysis pipelines.
- [`senior-data-engineer`](file:///d:/akstack/.agents/agents/senior-data-engineer.md) — Ingestion pipelines (Kafka, Spark, dbt), ETL/ELT transformations, feature stores, data lake architecture.

#### Quality Assurance & Verification (Phase 5)
- [`senior-qa-architect`](file:///d:/akstack/.agents/agents/senior-qa-architect.md) — Writes automated unit, integration, and E2E test suites (Gate G1). Never fixes production bugs directly.
- [`code-reviewer`](file:///d:/akstack/.agents/agents/code-reviewer.md) (**Review-Only**) — Audits architecture compliance, edge cases, error handling, and Hard Rules (Gate G2). Files `-F` tasks.
- [`visual-qa`](file:///d:/akstack/.agents/agents/visual-qa.md) (**Review-Only**) — Audits responsive rendering across all approved breakpoints (320px–1440px) (Gate G4).
- [`senior-performance-engineer`](file:///d:/akstack/.agents/agents/senior-performance-engineer.md) (**Review-Only**) — Audits P95 latency, database query execution plans, and Core Web Vitals (Gate G5).

#### DevOps, MLOps & Launch (Phase 6)
- [`senior-devops-engineer`](file:///d:/akstack/.agents/agents/senior-devops-engineer.md) — Hardened Dockerfiles, GitHub Actions CI/CD pipelines, Kubernetes manifests, zero-downtime rollouts.
- [`senior-mlops-engineer`](file:///d:/akstack/.agents/agents/senior-mlops-engineer.md) — Model registries (MLflow), automated evaluation harnesses, model lineage, GPU inference serving.

---

### 6.2 Model Tiering Policy

To balance intelligence, cost, and latency:

| Tier | When Required | Minimum Model Class |
|---|---|---|
| **★ Senior Tier** | `coordinator`, System & Database Architecture, Security & Privacy Threat Modeling, Novel ML Research, Schema Migrations | Flagship Reasoning Models (e.g., Claude 3.7 Sonnet Thinking / GPT-4o / Gemini 1.5 Pro) |
| **Standard Tier** | Feature Implementation, Frontend Components, Test Implementation, DevOps scripts | Standard Fast Coding Models (e.g., Claude 3.5 Sonnet / GPT-4o-mini) |

---

## 7. The Skills Ecosystem (`.agents/skills/`)

The [`.agents/skills/`](file:///d:/akstack/.agents/skills/) directory contains over **290 specialized domain skills**. Skills provide concrete code recipes, constraints, checklists, and anti-patterns that agents automatically activate based on task intent.

### Skills Categorized by Domain

```
.agents/skills/
├── [Architecture & Backend]     → api-design, database-migrations, postgresql, redis-patterns, hexagonal-architecture...
├── [Frontend & Design Systems] → tastemaker, ui-ux-pro-max, better-ui, motion-*, threejs, cobejs...
├── [AI, LLM & MLOps]           → ai-engineer, rag-implementation, mlops-engineer, agent-eval, eval-harness...
├── [Testing & Quality]         → tdd-workflow, e2e-testing-patterns, unit-testing-test-generate, react-testing...
├── [Security & Compliance]     → security-review, threat-modeling-expert, gdpr-data-handling, hipaa-compliance...
├── [Growth, CRO & SEO]         → landing-page-design, ai-seo, schema, cro, copywriting, marketingskills...
└── [DevOps, Cloud & SRE]       → docker-patterns, kubernetes-architect, terraform-specialist, distributed-tracing...
```

### Key Skills and Their Strategic Use

| Domain | Skill Name | When and How to Leverage |
|---|---|---|
| **Design** | `tastemaker` | **Use First in Phase 3**. Extracts aesthetic direction and visual tokens from reference URLs or design images. Prevents generic "AI template" aesthetics. |
| **Design** | `ui-ux-pro-max` | Generates complete, harmonious design systems, spacing scales, and typography hierarchies from scratch. |
| **Design** | `better-ui` / `better-typography` | Applies surgical polish passes to spacing, border radii, hit areas, optical alignments, and type scales. |
| **Motion** | `animate` / `motion-patterns` | Implements physics-based springs, micro-interactions, exit transitions, and reduced-motion fallbacks using Framer Motion / GSAP. |
| **Backend** | `architecture-patterns` | Guides Clean Architecture and Hexagonal / Ports & Adapters separation for backend services. |
| **Backend** | `database-migrations` | Provides zero-downtime database migration strategies (expand/contract pattern, concurrent indexing). |
| **AI / RAG** | `rag-implementation` | Implements semantic chunking, reciprocal rank fusion (RRF), hybrid search (keyword + vector), and re-ranking. |
| **Testing** | `tdd-workflow` | Enforces strict Red &rarr; Green &rarr; Refactor discipline. Writes failing tests before implementation. |
| **Security** | `security-review` | Systematic audit of OWASP Top 10, auth tokens, SQL injection, IDOR, SSRF, and sensitive data exposure. |
| **SEO** | `ai-seo` / `schema` | Formats data for AI citation (Perplexity, ChatGPT, Claude) and generates JSON-LD rich snippets. |
| **DevOps** | `docker-patterns` | Generates multi-stage, non-root, minimal-footprint production container builds. |

---

## 8. Workflows & Slash Commands (`.agents/workflows/`)

Workflows in [`.agents/workflows/`](file:///d:/akstack/.agents/workflows/) are structured procedural guides that can be invoked via slash commands in your AI coding environment (Antigravity IDE or Claude Code):

### Most Impactful Workflows

- **/orch-add-feature** — End-to-end autonomous feature build: research &rarr; plan &rarr; TDD implementation &rarr; code review &rarr; gated commit.
- **/orch-fix-defect** — Bug fix workflow: reproduces issue as a failing regression test, fixes to green, verifies, and commits.
- **/orch-refine-code** — Behavior-preserving refactoring: verifies test suite is green, restructures code cleanly, verifies tests stay green.
- **/gan-build** — Generator/Evaluator loop that runs iterative development passes against automated scoring criteria.
- **/gan-design** — Design generator/evaluator loop for visual and frontend components.
- **/checkpoint** — Runs verification checks and stamps workflow checkpoints into the progress journal.
- **/build-fix** — Detects build/type errors and applies minimal surgical fixes.
- **/test-coverage** — Analyzes test gaps and generates targeted test cases to hit coverage thresholds (80%+).
- **/quality-gate** — Runs quality and formatting checks for individual files.
- **/pr** — Inspects branch diffs, drafts conventional release notes, and submits a pull request.

---

## 9. Quality Gates & Verification Protocol (Phase 5)

Phase 5 enforces **strict quality gates** that must be executed sequentially before any code is marked production-ready.

```
[Build Complete]
       │
       ▼
[G0-ML: Model Eval & Lineage]  (AI/ML & Hybrid tracks)
       │
       ▼
[G1: Automated Test Suite]      (100% Green, Hard Rules Tested)
       │
       ▼
[G2: Code Review]              (Architecture, Error Handling, Ownership)
       │
       ▼
[G3: Security Audit]           (OWASP Top 10, Auth Boundaries)
       │
       ▼
[G3-P: Privacy Audit]          (Data Minimization, GDPR/CCPA)
       │
       ▼
[G4: Visual & UX QA]           (Responsive Breakpoints, Drift Check)
       │
       ▼
[G4-CRO: Funnel & SEO]         (Clear Value/Price, Events, Metadata)
       │
       ▼
[G4-A11Y: Accessibility]       (WCAG 2.2 AA, Keyboard Navigation)
       │
       ▼
[G5: Performance Audit]        (Core Web Vitals, API Latency Budgets)
       │
       ▼
[G6: Phase Sign-Off]           (All Tasks & Gates Cleared)
```

### The Iron Rules of Phase 5 Gates
1. **Review-Only Roles Never Edit Production Code**:
   `code-reviewer`, `senior-security-engineer`, `senior-privacy-engineer`, `visual-qa`, and `senior-accessibility-engineer` inspect code and file findings. They never fix the code they review.
2. **Actionable Remediation Tasks (`-F`)**:
   Every High or Critical finding is filed using:
   ```bash
   akstack finding P5-G2 --title "Missing CSRF token on checkout" --owner senior-backend-engineer --severity High --file src/routes/checkout.ts:42 --issue "POST endpoint unprotected" --fix "Add verifyCsrfToken middleware"
   ```
3. **Mandatory Evidence Reports**:
   No gate can be checked off without a workspace-relative evidence file:
   ```bash
   akstack gate P5-G1 --evidence docs/qa/test-report.md
   akstack gate P5-G2 --evidence docs/qa/code-review.md
   akstack gate P5-G3 --evidence docs/qa/security-report.md
   akstack gate P5-G4-CRO --evidence docs/analytics/cro-report.md
   ```

---

## 10. Frontend Quality Contract & Design Lock

Frontend work in `akstack` is held to the highest standard. A frontend is considered broken if it looks like an unstyled AI template, fails at mobile breakpoints, lacks accessible contrast, or leaks user privacy.

### The Five Invariants
1. **Visual Thesis Lock (`design-system/MASTER.md`)**:
   Every project defines its signature visual identity before writing frontend code. No default Tailwind gray cards or generic AI slop.
2. **Screen Specifications**:
   Every route has a spec in `docs/screens/<screen-name>.md` detailing layout, typography, interactive states, real copy, and instrumentation events.
3. **Responsive Breakpoint Matrix**:
   All screens must be verified at: `320px`, `375px`, `768px`, `1024px`, `1280px`, and `1440px`.
4. **Token Traceability**:
   Components consume tokens from `MASTER.md`, never ad-hoc hex codes or arbitrary padding values.
5. **Pre-Build Verification**:
   ```bash
   python -m orchestrator.cli frontend-check --area all
   ```
   Must pass cleanly before Phase 4 frontend tasks are considered ready.

---

## 11. Step-by-Step Operator Playbook (Unlocking Full Potential)

Here is how to run a project from inception to launch using the full power of Akram-Stack:

### Step 1: Bootstrap the Workspace
Clone `akstack` into a new project directory and initialize it:
```bash
# Initialize a new project on the Product/Web track
python -m orchestrator.cli init "FinTrack Pro" --track Product/Web

# Check system readiness
python -m orchestrator.cli doctor
```

### Step 2: Phase 1 — Discovery & Hard Rules Definition
Feed your raw product concept to the agent using the Bootstrap Prompt in `PROMPT_LIBRARY.md` §1.
The agents will populate `plan.md`.

> [!IMPORTANT]
> **Human Review Gate**: Inspect `plan.md` §3 (Domain & Hard Rules). Ensure all critical business invariants are identified. Explicitly approve before proceeding:
> ```bash
> python -m orchestrator.cli approve P1-HUMAN-PLAN --notes "Hard rules approved" --evidence plan.md
> ```

### Step 3: Phase 2 & 3 — Architecture & Design System
Run the orchestrator build loop to generate architecture diagrams, schemas, and design specs:
```bash
python -m orchestrator.cli next
python -m orchestrator.cli packet
python -m orchestrator.cli start P2-T001
# Implement task...
python -m orchestrator.cli complete P2-T001
```
Validate frontend contracts before building UI:
```bash
python -m orchestrator.cli frontend-check --area all
```

### Step 4: Phase 4 — High-Velocity Build Loop
Execute tasks using single dispatch or parallel waves:
```bash
# To run one task:
python -m orchestrator.cli next
python -m orchestrator.cli start <task-id>
# Code within declared Files: list...
python -m orchestrator.cli complete <task-id>

# To inspect parallel wave opportunities:
python -m orchestrator.cli next --parallel
```

### Step 5: Handling Obstacles & Questions
- **Encountered an architectural ambiguity?**
  ```bash
  python -m orchestrator.cli question <task-id> --ambiguity "Should invoices use Net-30 or immediate charge?" --risk "Affects payment gateway choice" --recommended "Immediate charge"
  ```
- **Blocked on an API key or external dependency?**
  ```bash
  python -m orchestrator.cli handoff <task-id> --blocked-on "Stripe Secret Key" --why "Need live test credentials"
  ```
  *(Execution halts safely. Once resolved by human, resume with:)*
  ```bash
  python -m orchestrator.cli resume --notes "Stripe test keys placed in .env"
  ```

### Step 6: Phase 5 & 6 — Gating & Launch
Clear the quality gates sequentially:
```bash
python -m orchestrator.cli gate P5-G1 --evidence docs/qa/test-report.md
python -m orchestrator.cli gate P5-G2 --evidence docs/qa/code-review.md
python -m orchestrator.cli gate P5-G3 --evidence docs/qa/security-report.md
python -m orchestrator.cli gate P5-G3-P --evidence docs/qa/privacy-report.md
python -m orchestrator.cli gate P5-G4 --evidence docs/qa/visual-report.md
python -m orchestrator.cli gate P5-G4-CRO --evidence docs/analytics/cro-report.md
python -m orchestrator.cli gate P5-G4-A11Y --evidence docs/qa/a11y-report.md
python -m orchestrator.cli gate P5-G5 --evidence docs/performance/report.md
python -m orchestrator.cli gate P5-G6 --evidence docs/release/signoff.md
```
Deploy infrastructure in Phase 6 and verify live health metrics.

---

## 12. Repository Directory Structure

```
akstack/
├── README.md                    — Master documentation & operations manual (this file)
├── GETTING-STARTED.md           — Quick-start operator guide
├── GLOBAL-RULES.md              — Global coding discipline & invariant rules
├── PROMPT_LIBRARY.md            — Verbatim prompts & CLI recipes for every phase
├── AGENTS.md                    — Rules for developers modifying akstack engine
├── bin/
│   ├── akstack                  — POSIX shell CLI launcher
│   └── akstack.bat              — Windows batch CLI launcher
├── orchestrator/                — Zero-dependency programmatic engine
│   ├── cli.py                   — Command-line interface & output formatting
│   ├── engine.py                — Task execution, state transitions, git staging
│   ├── graph.py                 — DAG dependency resolution & parallel waves
│   ├── models.py                — Data models (Task, Gate, Plan, Status)
│   ├── parser.py                — Markdown parser & state updater
│   └── frontend.py              — Frontend design contract checker
├── .agents/                     — Integral framework root
│   ├── TEAM.md                  — Master team roster, tiers & ownership contract
│   ├── agents/                  — 112 agent briefs (42 core roles + ECC specialists)
│   │   ├── coordinator.md       — Operating system orchestrator (★ Senior)
│   │   ├── senior-backend-engineer.md
│   │   ├── senior-frontend-engineer.md
│   │   └── ... (all 112 briefs)
│   ├── skills/                  — 290+ specialized domain skills
│   │   ├── akstack/             — Native Antigravity orchestration skill
│   │   ├── tastemaker/          — Premium design extraction & anti-slop
│   │   ├── tdd-workflow/        — Red-Green-Refactor testing discipline
│   │   └── ... (all domain skills)
│   ├── workflows/               — 80+ procedural workflows & slash commands
│   └── rules/                   — Operational constraints & behavior rules
├── templates/                   — Production-grade document templates
│   ├── plan.template.md
│   ├── ToDos.template.md
│   ├── PROGRESS.template.md
│   ├── adr.template.md
│   ├── design-system.MASTER.template.md
│   ├── screen-spec.template.md
│   └── ...
├── phases/                      — Formal specifications for Phases 0 through 6
│   ├── PHASE-0-SETUP.md
│   ├── PHASE-1-DISCOVERY.md
│   ├── PHASE-2-ARCHITECTURE.md
│   ├── PHASE-3-DESIGN.md
│   ├── PHASE-4-BUILD.md
│   ├── PHASE-5-QUALITY-SECURITY.md
│   └── PHASE-6-DEVOPS-LAUNCH.md
├── tests/                       — Orchestrator engine test suite (34 unit tests)
└── integrations/
    ├── SKILLS-GUIDE.md          — When to trigger which skill
    └── EXTERNAL-TOOLS.md        — Third-party tools setup guide
```

---

## License & Attribution

Akram-Stack is designed and maintained by **Akram Rafid**. Built for professional engineers, founders, and autonomous agents demanding rigor, auditability, and speed in modern software construction.
