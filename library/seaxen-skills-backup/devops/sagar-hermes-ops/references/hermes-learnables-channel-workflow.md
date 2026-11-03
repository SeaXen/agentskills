# Hermes Learnables channel workflow (Dr. Sagar install)

Research-first rooms on Discord `#learnables` or Telegram forum/reply chains before `skill_manage(create)`.

## Operator setup

1. Create `#learnables` (Discord) or Learnables forum group (Telegram).
2. Set IDs in `~/.hermes/learnables/config.yaml`.
3. `python3 ~/.hermes/learnables/apply_config.py` → patches `~/.hermes/config.yaml`.
4. Restart gateway.
5. `hermes tools enable discord --platform discord` (threads + `fetch_messages`).

## Hermes primitives used

- `channel_prompts` + `channel_skill_bindings` per channel/chat id
- Skill: `learnables-workflow` (productivity)
- Hook: `~/.hermes/hooks/learnables` — commit `/learn` → queued learnables commit prompt

Full procedure: load skill `learnables-workflow` or `references/gateway-wiring.md` under that skill.

## Verify

Post messy topic in learnables room → research pack, no skill. After review, `learn this` → skill in category `learnables` + summary block.