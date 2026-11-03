---
name: learnables-workflow
description: Research-first learnable rooms on Discord/Telegram.
version: 0.1.0
metadata:
  hermes:
    tags: [Learnables, Discord, Telegram, Skills]
    category: productivity
---

# Learnables workflow

Messy topic in → researched context pack → user taste → explicit commit → reusable skill out.

Does **not** replace `/learn` globally; only applies in configured Learnables channels/topics.

## When to Use

- User posts a rough topic in `#learnables` or a Learnables Telegram forum/topic
- User says "learn this" / "save this" after reviewing a research thread
- User wants Stripe disputes, deploy flows, etc. learned without writing perfect notes first

## Prerequisites

- `~/.hermes/learnables/config.yaml` lists Discord channel ID(s) and/or Telegram chat ID(s)
- Run: `python3 ~/.hermes/learnables/apply_config.py` then restart gateway
- Discord: enable `discord` toolset for Discord platform (`hermes tools`) so threads/history work
- Discord bot needs permission to create public threads in `#learnables`

## How to Run

1. User creates `#learnables` (private) on Discord **or** a Telegram forum group named Learnables
2. Set IDs in `~/.hermes/learnables/config.yaml`
3. `python3 ~/.hermes/learnables/apply_config.py`
4. Restart gateway

## Quick Reference

| Platform | Room unit | Hermes behavior |
|----------|-----------|-----------------|
| Discord | 1 thread per top-level post | `create_thread` on seed message → research reply in thread |
| Telegram forum | 1 forum topic | research inside topic |
| Telegram plain group | reply chain | reply with `Learnable ID: LB-…` on seed message |

Commit phrases: `learn this`, `save this`, `turn this into a workflow`, `make this reusable`, `/learn`

## Procedure

### A. Detect context

- Learnables mode is active when channel_prompt says `[LEARNABLES MODE]` or this skill auto-loaded
- One learnable = one Discord thread OR one Telegram topic OR one Telegram reply chain

### B. Research phase (no skill writes)

1. Parse the seed topic (first user message). Do **not** call `skill_manage(create)`.
2. `web_search` for official docs; `web_extract` on primary URLs (vendor docs, not random blogs first).
3. Post a **Research / context pack** with sections:
   - Summary (2–4 sentences)
   - Official sources (links)
   - Examples & commands
   - Common mistakes
   - Rough workflow (bullets)
   - What to ignore
   - Open questions for the user (numbered)
4. If the source is an **image / screenshot / visual reference** rather than docs/text, do a reconstruction pass before any save:
   - extract visible text (vision first; OCR fallback if needed)
   - describe layout, hierarchy, spacing, colors, typography, and components
   - separate **high-confidence facts** from reconstructed/uncertain details
   - keep the original image path/URL in notes so the future skill can cite the source
5. Discord only: if message is top-level in learnables parent channel, call `discord` `create_thread`
   anchored to triggering `message_id`, then continue in that thread.

### C. Review phase

- Merge user replies into a **Working draft** message (tone, constraints, examples, anti-patterns, project facts).
- Still no skill save until commit phrase.

### D. Commit phase

Trigger: commit phrases or `/learn` (empty or with scope).

**No-stall rule (added 2026-07-10 after a user correction):**
Once the user types a commit phrase (`learn this`, `save this`, `turn this into a workflow`,
`make this reusable`, `/learn`), **execute the commit immediately**. Do not ask "want to commit?",
"which shape?", "where to save?", or offer multiple options. The user already gave consent;
asking again stalls them. Only ask ONE clarifying question if the seed is genuinely ambiguous
(e.g. conflicting instructions, missing sources, or a name collision you cannot resolve safely).

**Symmetric no-overreach rule on removal (added 2026-08-19):**
When the user asks to remove / uninstall / delete a service, package, or app, the scope is
**runtime artifacts** (units, processes, binaries, npm/pip install, source clones, MCP wrappers,
config wiring). Do **not** also remove learning artifacts (skill folders under
`~/.hermes/skills/learnables/`, theme folders under `/mnt/tb/#Sea/Designmd/`, manifest entries)
unless the user explicitly says "remove all" / "delete everything". Skills and themes persist as
references for future use; deleting them on a "remove the service" command is overreach and the
user will correct you.

1. `discord` `fetch_messages` for thread `channel_id` OR use session + topic messages on Telegram.
2. `skills_list` / `skill_view` — if a similar skill exists, ask before overwrite OR pick a new
   versioned name and proceed (do not stall on naming).
3. `skill_manage` `create` — category `learnables` (unless user names another).
4. Follow Hermes skill authoring standards (≤60 char description, Hermes-tool framing).
5. Final user-facing summary:
   - **Title**
   - **What Hermes learned**
   - **When to reuse**
   - **Example trigger phrases**
   - **Source links**
   - **User preferences captured**

### E. Safety

- Research first, learn later — never from seed message alone
- Confirm if context unclear before `skill_manage(create)`
- Prefer official/primary sources; practical not academic

## FAQ

**Q: Why does a thread auto-create when I say "learn this" in the learnables channel?**
A: Learnables mode automatically creates a Discord thread for each top-level post to keep research, review, and commit phases organized in one place. This prevents the learnables channel from getting cluttered with long research threads. The thread is anchored to your triggering message ID. This is intentional behavior per Procedure B.5.

**Q: Can I disable thread creation?**
A: Yes, but you must move the discussion to a non-learnables channel. Thread creation is hardwired for learnables channels to maintain workflow organization.

## Pitfalls

- Without `discord` toolset, thread creation/history steps fail — enable tools for Discord
- `channel_ids` empty → `apply_config.py` exits **2** until IDs configured
- Auto-thread on @mention elsewhere ≠ learnables behavior; learnables uses explicit `create_thread`
- `command:learn` gateway hook does not receive `chat_id` — empty `/learn` in learnables relies on channel_prompt + this skill; commit phrases still route via hook → `/queue`
- Do not rewrite empty `/learn` globally in the hook (breaks normal `/learn` in other channels)
- Saving under `devops/` after a Learnables commit — user will correct; path is **`learnables/`** (`~/.hermes/skills/learnables/<name>/`), not “sensible category” elsewhere. **Never** create a one-off runbook skill under `devops/` when the user said “learn this” / “learn this update process” — merge into an existing learnable (e.g. `hermes-telemetry`) or create a new **learnables/** umbrella.
- After commit phrase, **do not** ask where to save — default **`skill_manage` `create` with `category: learnables`** unless the user names another category.
- **Site theme extract** (“save bg/color/fonts like Designmd”) → write files under `/mnt/tb/#Sea/Designmd/` per skill `designmd-store`; do **not** create a one-off learnable unless the user commits to learning the **product/system** (e.g. `/learn` Featherless architecture). Theme CSS is a file-store task, not every `/learn`.
- **Scope rule for "remove X" / "delete Y"** (added 2026-08-19 after a codeburn-removal overreach): "remove service" / "remove package" / "remove install" / "delete the binary" = **runtime artifacts only** (systemd units, processes, npm/pip packages, source clones, MCP wrappers, config wiring, binaries). Do **NOT** also delete learning or design artifacts (skill folders under `~/.hermes/skills/learnables/`, theme folders under `/mnt/tb/#Sea/Designmd/`, manifest entries for the repo, verbatim copies) unless the user explicitly says "remove all" / "remove everything" / "delete the skill too". The user wants skills/themes/manifest entries to persist as references for future use. **When in doubt, ask one clarifying question before removing anything tagged "learned" or "theme".**

## Support files

- `references/gateway-wiring.md` — channel_prompts, skill bindings, hook limits, restart notes
- `references/image-derived-ui-capture.md` — how to turn a screenshot/UI image into reusable Learnables notes with confidence labels
- `references/thread-creation-faq.md` — why threads auto-create in learnables channels and how to control it
- Cross-ref: `designmd-store` + `references/site-theme-extraction.md` for marketing-site CSS extracts to Designmd

## Verification

```bash
python3 ~/.hermes/learnables/apply_config.py
# expect: Updated ~/.hermes/config.yaml
grep -A2 channel_skill_bindings ~/.hermes/config.yaml
```

Post a test topic in `#learnables`; Hermes should return a research pack, not a new skill.