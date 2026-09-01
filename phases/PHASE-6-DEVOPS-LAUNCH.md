# Phase 6 — DevOps & Launch

**Objective:** The gated system, actually running in production, with a
tested rollback path and real observability. This is where the project
stops being a repo and starts being a live system.

## Active agents

| Agent | Role in this phase |
|---|---|
| `senior-devops-engineer` | CI/CD, deployment, monitoring, backups |
| `senior-mlops-engineer` | Model deployment + monitoring (AI/ML or Hybrid track only) |

## Inputs

The fully gated system from Phase 5, `senior-cloud-architect`'s
infrastructure topology from Phase 2.

## Outputs

A deployed environment, CI/CD pipeline, monitoring/alerting, a tested
rollback procedure, backup strategy — see `senior-devops-engineer.md`'s
standard of work for what "done" means here.

## Exit

The system is live. Rollback has been tested, not just documented.
`PROGRESS.md` has the final phase summary. `git tag phase-6-complete`
(or your project's final phase number).

## After this phase

The project is live. Ongoing work — new features, fixes, requirement
changes — goes through the same loop: new tasks in `ToDos.md`, same gate
discipline for anything that reaches production again. Use
`PROMPT_LIBRARY.md` §6.3 for handling a requirement change on a live
system.
