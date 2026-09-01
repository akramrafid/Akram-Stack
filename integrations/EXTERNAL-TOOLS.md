# External Tools — Install & Update

akstack orchestrates these; it doesn't bundle them. Install once globally,
they're then available to every akstack clone.

## Karpathy coding-discipline rules

Global behavioral rules (think-before-coding, simplicity-first, surgical
changes, goal-driven execution). Applies to every action automatically once
installed — no per-project setup needed.

```bash
curl -o /tmp/guidelines.md https://raw.githubusercontent.com/multica-ai/andrej-karpathy-skills/main/CLAUDE.md
cat /tmp/guidelines.md >> ~/.gemini/GEMINI.md    # or Set-Content if the file is fresh
```

## ui-ux-pro-max

Live design-reasoning engine — colors, typography, layout patterns, industry
anti-patterns. Used in Phase 3.

```bash
npm install -g ui-ux-pro-max-cli
uipro init --ai antigravity --global      # ~/.agents/skills/
uipro update --global                     # keep it current
```

## design-system-skill

Generates a design system *from existing brand assets* (PDFs, Figma,
screenshots) rather than inventing one. Use instead of ui-ux-pro-max's
generator when a project already has brand material.

```bash
git clone https://github.com/albertzhangz10/design-system-skill.git ~/.agents/skills/design-system
```

## Impeccable

Anti-AI-slop detector for design and UX — catches generic-AI-design tells
before they ship. Used at the Phase 5 UX/Visual gate.

```bash
npx impeccable install --providers=antigravity --scope=global
```

## gstack (optional)

Multi-agent virtual team with its own planning/review/QA slash commands
(`/office-hours`, `/plan-ceo-review`, `/plan-design-review`, `/review`,
`/qa`, `/ship`). Useful before Phase 1 to stress-test the idea, and for
parallel multi-worker dispatch during Phase 4 if you want it — akstack's
own build loop is sequential by default and works without gstack.

```bash
# Run via Git Bash or WSL, not raw PowerShell
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup --host antigravity
```

Heavier install (browser automation, hooks, opt-in telemetry) — read its
own README before deciding whether to install globally vs. per-project.

## Checking what's installed

```bash
ls ~/.agents/skills/          # ui-ux-pro-max, design-system-skill, akstack, etc.
cat ~/.gemini/GEMINI.md | head -5    # confirms Karpathy rules are present
```
