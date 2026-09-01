# {{PROJECT_NAME}} — Progress Journal

> Append-only. Never rewritten or trimmed. Read the most recent entries
> FIRST — they record what the environment actually is, which is not
> always what ToDos.md assumed when it was written.

## Entry format

```
### {{date}} — <TASK-ID>: <title>
**Changed:** <what was actually built/modified>
**Verified:** <exact command run and its result>
**Notes for next session:** <anything that saves the next session time>
```

## HANDOFF entry (human-required task)

```
### {{date}} — HANDOFF: <TASK-ID>
**Blocked on:** <exactly what a human must do>
**Why the agent can't:** <credential / physical action / irreversible
  business decision>
**Rest of phase:** <continued around it / n/a>
```

## QUESTION entry (genuine ambiguity)

```
### {{date}} — QUESTION: <TASK-ID>
**The ambiguity:** <what plan.md/ToDos.md didn't specify>
**Why it's not safe to guess:** <which Hard Rule or irreversible
  consequence is at stake>
**Options considered:** <if any>
```

## Phase summary entry (written at each G6 Sign-off)

```
### {{date}} — PHASE <N> COMPLETE
**Built:** <summary>
**Verified:** <full regression result>
**Known gaps:** <anything deferred, with reason>
**Phase <N+1> needs to know:** <handoff context>
```

---

<!-- Entries begin below. -->
