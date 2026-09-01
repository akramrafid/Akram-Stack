# akstack

Akram's personal production system. Clone this into any new project, feed it
a product requirement, and it runs the same disciplined pipeline every time —
architecture, backend, frontend, UI/UX, AI/ML, DevOps, QA, security, code
review — regardless of what the project actually is.

## The idea in one paragraph

Most AI-assisted builds fall apart because the plan lives in a chat that
scrolls away. akstack puts the plan on disk instead: `plan.md` (what/why/
hard rules), `ToDos.md` (the task ledger), `PROGRESS.md` (the journal), and
`agents/` (30 role briefs, each with a narrow job and a clear handoff). Every
work session — whether it's the same day or three weeks later — re-reads
these files from scratch. That's what makes a multi-week build survive
context resets, model switches, and long gaps between sessions.

## What's original here vs. what's a dependency

**Original to akstack:** the file-based task ledger, the phase structure,
all 30 agent role briefs, the gate sequence, the prompt library.

**Dependencies — installed separately, referenced not vendored** (see
`integrations/EXTERNAL-TOOLS.md` for install commands):
- **Karpathy coding-discipline rules** — global, already active via
  `~/.gemini/GEMINI.md`
- **ui-ux-pro-max** / **design-system-skill** — design system generation
- **Impeccable** — anti-AI-slop design/code detector
- **gstack** — optional, for `/office-hours`-style idea interrogation before
  Phase 1, and for parallel multi-worker dispatch if you want it

akstack doesn't reinvent any of these — it calls them at the right moment
and stays out of their way otherwise.

## Two tracks, one spine

Every project runs the same six phases. Which **agents** are active in
Phase 4 (Build) depends on the track:

| Track | Used for | Phase 4 agents |
|---|---|---|
| **Product/Web** | CRUD apps, dashboards, marketplaces, SaaS | senior-backend-engineer, senior-frontend-engineer |
| **AI/ML** | Model development, research, ML-driven features | senior-ai-research-engineer, senior-machine-learning-engineer, senior-deep-learning-engineer, senior-llm-engineer, senior-generative-ai-engineer, senior-nlp-engineer, senior-computer-vision-engineer, senior-data-engineer |
| **Hybrid** | A product with an ML feature inside it | both, on their own files, coordinated via `agents/TEAM.md` file ownership |

Track is declared in `plan.md` §0 at bootstrap and decides which
`phases/PHASE-4-BUILD.md` sub-section applies.

## Quick start

```bash
git clone <this-repo> my-new-project
cd my-new-project
rm -rf .git && git init          # detach from akstack's own history
```

Then open it in Antigravity (or Claude Code) and say:

> "Bootstrap this project using akstack. Here's the requirement: <your
> product requirement, in plain language>."

Full walkthrough in `GETTING-STARTED.md`. Every prompt this system runs on
lives in `PROMPT_LIBRARY.md` — nothing is implicit.

## Phase map

| Phase | Doc | Produces |
|---|---|---|
| 0 — Setup | `phases/PHASE-0-SETUP.md` | Dependencies installed, akstack templates in place |
| 1 — Discovery | `phases/PHASE-1-DISCOVERY.md` | `plan.md` §1-3, capability map, personas |
| 2 — Architecture | `phases/PHASE-2-ARCHITECTURE.md` | `plan.md` §4-6, schema, Phase 4 task list |
| 3 — Design | `phases/PHASE-3-DESIGN.md` | `design-system/MASTER.md`, brand sign-off |
| 4 — Build | `phases/PHASE-4-BUILD.md` | The actual product/model, task by task |
| 5 — Quality & Security | `phases/PHASE-5-QUALITY-SECURITY.md` | 6 gates cleared |
| 6 — DevOps & Launch | `phases/PHASE-6-DEVOPS-LAUNCH.md` | Deployed, monitored, signed off |

## Full agent roster (30)

See `agents/TEAM.md` for the complete table with phase, track, model tier,
and file-ownership mapping. Full list of files:

```
agents/
├── TEAM.md                              — roster, tiers, ownership, escalation
├── requirement-analyzer.md              ┐
├── senior-product-manager.md            │ Phase 1 — Discovery
├── ux-researcher.md                     │
├── design-researcher.md                 │
├── pinterest-researcher.md              ┘
├── senior-system-architect.md           ┐
├── senior-system-designer.md            │
├── senior-cloud-architect.md            │ Phase 2 — Architecture
├── senior-database-architect.md         │
├── senior-security-engineer.md          ┘
├── senior-product-designer.md           ┐
├── ui-designer.md                       │ Phase 3 — Design
├── brand-guardian.md                    │
├── senior-ai-engineer.md                ┘ (AI strategy, spans P2-P4)
├── senior-backend-engineer.md           ┐
├── senior-frontend-engineer.md          ┘ Phase 4 — Build (Product/Web)
├── senior-ai-research-engineer.md       ┐
├── senior-machine-learning-engineer.md  │
├── senior-deep-learning-engineer.md     │
├── senior-llm-engineer.md               │ Phase 4 — Build (AI/ML)
├── senior-generative-ai-engineer.md     │
├── senior-nlp-engineer.md               │
├── senior-computer-vision-engineer.md   │
├── senior-data-engineer.md              ┘
├── senior-qa-architect.md               ┐
├── code-reviewer.md                     │
├── visual-qa.md                         │ Phase 5 — Quality & Security
├── senior-performance-engineer.md       │
├── senior-mlops-engineer.md             ┘ (AI/ML eval + registry gate)
└── senior-devops-engineer.md              Phase 6 — DevOps & Launch
```

## Directory layout

```
akstack/
├── README.md                    — this file
├── GETTING-STARTED.md           — step-by-step first use
├── GLOBAL-RULES.md              — the discipline every agent inherits
├── PROMPT_LIBRARY.md            — every prompt, verbatim, copy-paste ready
├── templates/
│   ├── plan.template.md
│   ├── ToDos.template.md
│   └── PROGRESS.template.md
├── agents/                      — 30 role briefs (see above)
├── phases/                      — 7 phase docs, each linking back here
└── integrations/
    └── EXTERNAL-TOOLS.md        — install/update commands for dependencies
```
