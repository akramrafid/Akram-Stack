# Skills Guide — When to Use What

Every installed skill, mapped to the akstack phase where it actually fires.
Most trigger automatically from natural language — you rarely need to name
them. This is a reference for *why* something triggered, and what to say
when you want to force a specific one.

## Anytime — meta-skills

| Skill | Use when |
|---|---|
| `find-skills` | You're not sure what's installed. "What skills do I have for X?" |
| `choose-subagent` | You're not sure which skill applies. "Which skill should handle this?" |
| `orchestration` | Coordinating multiple skills/agents on one complex task |

---

## Phase 1 — Discovery

Mostly your own akstack agents (`requirement-analyzer`, `ux-researcher`,
`pinterest-researcher`). No installed skills fire here by default.

---

## Phase 2 — Architecture

| Skill | Use when |
|---|---|
| `pick-ui-library` | Choosing a frontend/component library for the stack |
| `ts-best-practices` | Stack is TypeScript — enforces idiomatic patterns from the start |
| `zero-trust-architecture` | Designing auth/access-control approach (supplements `senior-security-engineer`) |

---

## Phase 3 — Design

**Sequence that actually matters (don't let these fire independently on the
same task):**

1. **`tastemaker`** first — grounds the design system in a reference image if you have one
2. **`ui-ux-pro-max`** — generates the system if no reference exists, or refines after tastemaker
3. **`better-ui`, `better-typography`, `better-colors`, `better-layout`** — detail polish on the generated system
4. **`animate`, `improve-animations`** — motion, once the static design is settled

| Skill | Use when |
|---|---|
| `design-system` | Formalizing tokens/components after the above steps |
| `brand` | Checking a screen/asset against brand consistency |
| `apple-design` | Building for iOS/macOS and need platform-native design language |
| `banner-design` | Marketing banners, social assets, ad creative |
| `slides` | Pitch decks, presentations |
| `prototype` | Interactive click-through prototype before real build |
| `variant` | Generating A/B design variants of one screen |
| `explain-interface` | "Explain what this UI does" — for docs or onboarding someone else |
| `interface-review` | Critiquing an existing UI (yours or a reference) before building |
| `better-accessibility` | Accessibility pass on the design *before* build, not just at the G4-A11Y gate |
| `write-swift` | Writing native Swift UI code specifically |
| `ask-sonner` | Implementing toast/notification UI (Sonner library pattern) |
| `better-writing` | UI copy — button labels, empty states, error messages |
| `animation-vocabulary`, `animate-expo`, `find-animation-opportunities`, `review-animations` | Deeper motion work — vocabulary/consistency, Expo-specific, finding where motion would help, auditing existing animations |

**Known overlap:** you have 6 animation-related skills from two packs
(`animate`, `animate-expo`, `animation-vocabulary`, `improve-animations`,
`review-animations`, `find-animation-opportunities`). If Antigravity seems
uncertain which to use, just name one directly rather than letting it guess.

---

## Phase 4 — Build

| Skill | Use when |
|---|---|
| `create-tdd` | "Build this with tests first" — test-driven development flow |
| `fullstack-feature-slice` | Building one feature vertically — DB to UI — in one pass |
| `write-tests` | Writing tests for code that already exists |
| `diagnose-bug` | Something's broken, cause unknown — diagnosis before fixing |
| `fix-bug` | Cause is known — just fix it |
| `upgrade-dependency` | Bumping a package version safely |
| `ts-best-practices` | Ongoing, during any TypeScript work |

---

## Phase 5 — Quality & Security

| Skill | Gate it supplements | Use when |
|---|---|---|
| `review-code` | G2 (Code Review) | Quick code-quality pass mid-build, not a replacement for the real gate |
| `standards-spec-review-loop` | G2 | Automates the fix→re-review loop until no Critical/High findings remain |
| `zero-trust-architecture` | G3 (Security) | Supplementary access-control audit |
| `better-accessibility` | G4-A11Y | Supplementary a11y audit on built (not just designed) UI |
| `rollout-compatibility` | G5/G6 | Checking a change won't break existing users before shipping |
| `doc-fact-check` | — | Verifying docs match actual current code behavior |
| `format-docs` | — | Cleaning up/standardizing documentation formatting |

**Important:** `review-code` and `zero-trust-architecture` are quick
supplementary checks, not substitutes for running the real `code-reviewer`
(G2) and `senior-security-engineer` (G3) gates with their structured,
filed-as-tasks findings. Same relationship Impeccable has to G4.

---

## Phase 6 — DevOps & Launch

| Skill | Use when |
|---|---|
| `create-pr` | Taking local changes through branch/commit/push/PR, following the repo's own conventions |
| `terse-reports` | Writing a short release summary or status report instead of a long one |

---

## Quick decision rule

If you're ever unsure which skill (or whether any skill) applies to what
you're about to ask for: just ask the question plainly first. Most of
these trigger correctly from natural language alone — naming them
explicitly is for the cases above where multiple similar skills could
answer and you want a specific one.

---

## Key takeaways

- **Most triggers are automatic:** You rarely need to name a skill — describing the actual task triggers the right one. The table matters for knowing why something fired, and for the handful of cases (animation, code review) where you have overlapping options and want to be specific.
- **Phase 3 design sequence matters:** Follow the strict order: `tastemaker` → `ui-ux-pro-max` → `better-*` detail passes → `animate` / `improve-animations` last. Everything else is roughly independent.
- **Supplements vs. Gates:** Skills like `review-code` and `zero-trust-architecture` are quick supplements, never substitutes for running real `code-reviewer` (G2) and `senior-security-engineer` (G3) gates with their structured, filed-as-tasks findings.
