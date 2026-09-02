# Phase 0 — Setup

**Objective:** Ensure all development tools, linters, external skills, and akstack templates are verified in place before project-specific requirements are written.

## Checklist

- [ ] Global coding discipline rules verified: `~/.gemini/GEMINI.md`
- [ ] Python 3.10+ runtime available for orchestrator CLI (`python --version`)
- [ ] Node.js 18+ runtime available (`node --version`)
- [ ] `ui-ux-pro-max` installed globally (`npm i -g ui-ux-pro-max-cli` & `uipro init`)
- [ ] `design-system-skill` available (for projects with pre-existing brand assets)
- [ ] `Impeccable` installed (`npx impeccable install --providers=antigravity --scope=global`)
- [ ] `akstack` CLI verified: run `python -m orchestrator.cli lint`
- [ ] Project initialized:
  ```bash
  python -m orchestrator.cli init "My Project" --track Product/Web
  ```
- [ ] `agents/` present in root (all 35 role briefs + `TEAM.md`)

See `integrations/EXTERNAL-TOOLS.md` for exact tool install and verification commands.

## Exit Criteria

`plan.md`, `ToDos.md`, `PROGRESS.md` exist. `agents/` directory is present and `python -m orchestrator.cli lint` passes with 0 errors. No product-specific feature code is written yet.

## Next Phase

`phases/PHASE-1-DISCOVERY.md`
