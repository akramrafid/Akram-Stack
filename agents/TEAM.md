# {{PROJECT_NAME}} — Team

## §1. Full Roster

| Agent | Phase | Track | Tier | Mode |
|---|---|---|---|---|
| requirement-analyzer | 1 Discovery | Shared | Standard | Implement |
| senior-product-manager | 1 Discovery | Shared | Standard | Implement |
| ux-researcher | 1 Discovery | Shared | Standard | Implement |
| design-researcher | 1 Discovery | Shared | Standard | Implement |
| pinterest-researcher | 1 Discovery | Shared | Standard | Implement |
| senior-system-architect | 2 Architecture | Shared | ★ Senior | Implement |
| senior-system-designer | 2 Architecture | Shared | Standard | Implement |
| senior-cloud-architect | 2 Architecture | Shared | Standard | Implement |
| senior-database-architect | 2 Architecture | Shared | ★ Senior | Implement |
| senior-security-engineer | 2 Architecture + 5 Gate | Shared | ★ Senior | Implement (P2) / Review-only (P5) |
| senior-ai-engineer | 2–4 AI strategy | AI/ML | ★ Senior | Implement |
| senior-product-designer | 3 Design | Shared | Standard | Implement |
| ui-designer | 3 Design | Shared | Standard | Implement |
| brand-guardian | 3 Design + 5 Gate | Shared | Standard | Review-only |
| senior-backend-engineer | 4 Build | Product/Web | Standard | Implement |
| senior-frontend-engineer | 4 Build | Product/Web | Standard | Implement |
| senior-ai-research-engineer | 4 Build | AI/ML | ★ Senior | Implement |
| senior-machine-learning-engineer | 4 Build | AI/ML | Standard | Implement |
| senior-deep-learning-engineer | 4 Build | AI/ML | Standard | Implement |
| senior-llm-engineer | 4 Build | AI/ML | Standard | Implement |
| senior-generative-ai-engineer | 4 Build | AI/ML | Standard | Implement |
| senior-nlp-engineer | 4 Build | AI/ML | Standard | Implement |
| senior-computer-vision-engineer | 4 Build | AI/ML | Standard | Implement |
| senior-data-engineer | 4 Build | AI/ML | Standard | Implement |
| senior-qa-architect | 5 Gate (G1) | Shared | Standard | Implement (tests only) |
| code-reviewer | 5 Gate (G2) | Shared | Standard | Review-only |
| visual-qa | 5 Gate (G4) | Shared | Standard | Review-only |
| senior-performance-engineer | 5 Gate (G5) | Shared | Standard | Review-only |
| senior-mlops-engineer | 5 Gate (G0-ML) + 6 | AI/ML | Standard | Implement |
| senior-devops-engineer | 6 Launch | Shared | Standard | Implement |

Full role briefs: `agents/<agent-name>.md`.

## §2. Model Tier Policy

**★ Senior tasks are never delegated to a faster/cheaper model tier**,
regardless of how small they look — the failure mode isn't worse code, it's
a Hard Rule violation that isn't caught until it's already in production
data. Everything else can run on a standard tier.

## §3. File Ownership

Adjust paths to the actual chosen stack at bootstrap. Defaults:

```
{{schema/migrations path}}         → senior-database-architect only (★)
{{backend services path}}          → senior-backend-engineer, senior-system-architect (★ only)
{{frontend components/pages path}} → senior-frontend-engineer, ui-designer
{{ml/ training+eval path}}         → the relevant senior-*-engineer AI/ML role
{{data/ pipelines path}}           → senior-data-engineer
{{design-system/}}                 → senior-product-designer, ui-designer
                                      (generated via ui-ux-pro-max /
                                      design-system-skill, not hand-edited)
{{ci/deploy config path}}          → senior-devops-engineer, senior-mlops-engineer
{{tests path}}                     → senior-qa-architect (writes tests, never
                                      fixes production code)
docs/, ADRs                        → the coordinator or whichever agent
                                      produced the artifact being documented
plan.md, ToDos.md, PROGRESS.md     → the coordinator only, never a
                                      delegated task
```

Two tasks touching overlapping files never run in the same wave.

## §4. Standing Rules (every task, every agent, no exceptions)

1. Every Hard Rule in `plan.md` §3 applies regardless of which agent wrote
   the line.
2. Validate every external input at the boundary. Never concatenate
   untrusted input into a query or shell command.
3. Multi-step writes that must succeed or fail atomically run inside a
   transaction.
4. Every privileged action re-checks authorization server-side.
5. Money, legally/financially exact quantities, and anything requiring
   exact decimal arithmetic is never floating point.
6. AI/ML: every model artifact traces to a versioned dataset and a logged
   set of hyperparameters. No untracked training run ships.
7. UI work reads `design-system/MASTER.md` (and page overrides) before
   writing markup — never invents visual decisions ad hoc.
8. Touch only the files a task lists. Pre-existing issues noticed along the
   way go in `PROGRESS.md`, not into an unscoped fix.
9. State assumptions explicitly. Genuine ambiguity gets a QUESTION entry,
   not a guess.

## §5. Escalation

Hard Rule conflict, credential/physical-action need, or genuine costly
ambiguity → HANDOFF or QUESTION in `PROGRESS.md`. See `ToDos.md` §0 and
`PROMPT_LIBRARY.md` §5.
