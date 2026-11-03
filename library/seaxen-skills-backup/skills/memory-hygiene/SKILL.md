---
name: memory-hygiene
description: Canonical low-noise memory hygiene policy for Hermes. Use before writing USER.md, MEMORY.md, Fabric, or a new skill.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, memory, fabric, skills, policy, hygiene]
    related_skills: [sagar-hermes-ops, fabric-writing-policy, hermes-agent]
---

# Memory Hygiene

Use this skill before any `memory`, `fabric_write`, or skill save.

## Goal

Keep Hermes memory small, durable, and reusable.

The default action is **save less**.
If a note is noisy, temporary, or ambiguous, do not save it.

## Destination decision

Choose exactly one destination:

1. **USER.md** — durable user fact
2. **MEMORY.md** — durable agent/environment fact
3. **Skill** — repeatable workflow, checklist, or playbook
4. **Fabric** — verified reusable case, decision, review, or research conclusion
5. **Nowhere** — temporary chatter, progress, TODO, raw log, stale detail, or conversational residue

If it does not fit cleanly, save nowhere.

## Hard rejection rules

Do **not** save if any are true:

- likely stale within a week
- just a progress update
- raw log without conclusion
- reads like an instruction to the agent
- starts with `todo`, `investigate`, `if you want`, or similar
- duplicates something already in USER.md, MEMORY.md, Fabric, or a skill
- mostly paraphrases the chat without adding a reusable lesson

## What belongs where

### USER.md
Keep only:
- identity
- communication style
- stable preferences
- long-lived routing or channel preferences

Do not keep:
- project status
- temporary tasks
- workflow notes better stored as a skill

### MEMORY.md
Keep only:
- active Hermes/environment facts
- stable tool quirks
- durable technical notes

Do not keep:
- open questions
- TODOs
- chat fragments
- issue-of-the-day notes

### External memory providers
When Hermes is using an external provider such as Mnemosyne, audit both layers separately:
- built-in memory files (`USER.md`, `MEMORY.md`)
- provider-owned storage

Cleanup order:
1. remove obvious validation residue first (smoke-test tokens, dummy identifiers, one-off verification prompts)
2. respect user scope exactly: if the user asked to clean `MEMORY.md` only, do **not** touch `USER.md`
3. back up `MEMORY.md` before any aggressive rewrite, then replace it with a short verified set of durable facts rather than line-editing noisy residue
4. remember that built-in files and external providers can coexist; cleaning `MEMORY.md` does not replace provider cleanup, and provider cleanup does not replace built-in cleanup
5. verify provider cleanup with the provider's own recall/inspect path, not by assumption

Pitfalls:
- a single smoke test token may create multiple provider entries (fact plus echoed user/assistant turns). Deleting only the headline fact may leave retrieval noise behind.
- ambiguous shorthand like "add 1 mnemosyne" is **not** enough to write to an external memory provider. Require a clear write intent before storing provider memory.
- if the dashboard/plugin layer is supposed to expose an external provider, verify both the API route and the rendered UI; a stale plugin load can make on-disk patches look absent until the dashboard process is restarted.

See `references/mnemosyne-cleanup.md` for a concrete provider-cleanup workflow and `references/memory-ui-mnemosyne-dashboard.md` for a dashboard-facing Mnemosyne integration checklist.

### Skill
Use when the note is really a:
- workflow
- checklist
- debugging playbook
- repeatable procedure
- routing/decision rubric

### Fabric
Require:
- concrete problem, decision, review, or research question
- conclusion, fix, or decision
- verification/evidence when available
- enough detail to help solve a similar future case

## Compression rules

Before saving, ask:

- Can this merge into an existing note?
- Can one dense line replace three overlapping lines?
- Should this move to a skill instead of memory?

Operational rule:
- if USER.md is above ~80%, consolidate before adding
- remove duplicates between USER.md, MEMORY.md, and skills
- prefer one durable fact over several chat-shaped fragments

## Final gate

Only save if the note would make a future agent:
- faster
- more correct
- less noisy

If not, do not save it.

## Examples

### Good USER.md entry
- User prefers terse, direct replies and wants verified results.

### Good MEMORY.md entry
- Active Hermes home for the main profile is `/mnt/tb/hermes`.

### Good Skill candidate
- Repeatable workflow for cleaning noisy Hermes memory files and re-auditing them.

### Bad memory entries
- "investigate later"
- "worked on dashboard today"
- "if you want, try this"
- raw error dump with no conclusion

## Related skills

- `fabric-writing-policy` — stricter rules for Fabric writes
- `sagar-hermes-ops` — Dr. Sagar-specific Hermes operational workflow
- `hermes-agent` — Hermes configuration and CLI behavior
