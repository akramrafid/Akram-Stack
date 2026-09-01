# Getting Started

## 1. Clone it for a new project

```bash
git clone <akstack-repo-url> my-new-project
cd my-new-project
rm -rf .git && git init -b main
```

akstack ships with no project-specific content — `plan.md`, `ToDos.md`, and
`PROGRESS.md` don't exist yet in your clone; only their templates do. That's
intentional: every project's plan is written fresh at bootstrap, never
inherited from a previous project.

## 2. (Optional but recommended) Interrogate the idea first

If gstack is installed, run `/office-hours` before anything else — it pushes
back on a vague product idea before it becomes a written plan. Skip this if
your requirement is already well-specified.

## 3. Bootstrap

Open the project in Antigravity and run the **Bootstrap** prompt from
`PROMPT_LIBRARY.md` §1, with your product requirement pasted in. It will:

1. Copy `templates/plan.template.md` → `plan.md`, etc.
2. Ask you (once) which track applies: Product/Web, AI/ML, or Hybrid.
3. Fill in `plan.md` §1-3 from your requirement.
4. Write `plan.md` §3 — **Hard Rules** — this is the section worth reading
   carefully before approving. It's the domain-specific "money is never a
   float" equivalent for whatever you're actually building.
5. Generate `agents/TEAM.md`'s file-ownership section for your actual stack.
6. Generate Phase 1 tasks in `ToDos.md`.
7. **Stop and ask you to review `plan.md`** before writing any code.

## 4. Review the plan

Read `plan.md` in full, especially:
- §3 Hard Rules — did it catch the real domain risks?
- §8 Open Questions — resolve anything genuinely ambiguous before building

Approve, or send corrections and have it re-run just that section.

## 5. Run the phases

```
"Run Phase 1."          → discovery agents produce the capability map
"Run Phase 2."          → architecture agents produce schema + design docs
"Run Phase 3."          → design agents + ui-ux-pro-max produce design-system/MASTER.md
"Run Phase 4."          → build loop, one task at a time or the whole phase
"Run Phase 5."          → the 6 quality/security gates
"Run Phase 6."          → DevOps + launch sign-off
```

Each phase doc in `phases/` tells the agent exactly which role briefs to
read and which gate(s) close out the phase. You don't need to remember which
agents apply to which phase — the phase doc does that.

## 6. Day-to-day: the build loop

Once you're in Phase 4, the unit of work is one task:

> "Run the build loop." → picks the next `- [ ]` task in `ToDos.md`, reads
> the right role brief, implements it, verifies it, commits, stops.

Or for a whole phase unattended:

> "Complete Phase 4." → runs tasks in dependency order, then the phase's
> gates, then stops and reports.

## 7. If something breaks

`PROMPT_LIBRARY.md` §5 has recovery prompts for a blocked task, a stuck
loop, and reverting a bad commit. §6 has ad-hoc prompts for status checks,
re-planning a phase, and handling a requirement change mid-build.

## Using akstack as a global skill instead (optional)

If you'd rather have it available in every project without cloning fresh
each time:

```bash
cp -r akstack ~/.agents/skills/akstack
```

Then reference `~/.agents/skills/akstack/templates/` from any project's
setup step. The clone-per-project flow above is the primary intended use
though — a git history that starts clean per project is worth more than the
convenience of a global skill for something this central to how you build.
