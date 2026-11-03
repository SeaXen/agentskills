# Learnables gateway wiring (Hermes v0.17-class)

## Config surfaces (no core fork)

| Mechanism | Config keys | Effect |
|-----------|-------------|--------|
| Ephemeral mode prompt | `discord.channel_prompts`, `telegram.channel_prompts` | Injected at API time; threads inherit parent forum/channel id |
| Auto-load skill | `discord.channel_skill_bindings`, `telegram.channel_skill_bindings` | `resolve_channel_skills()` in `gateway/platforms/base.py` |
| Discord no-mention | `discord.free_response_channels` + `require_mention: false` | Bot answers in learnables without @mention |
| User hook | `~/.hermes/hooks/learnables/` | `command:learn` → `rewrite` to `/queue` with commit prompt |

## apply_config.py

Reads `~/.hermes/learnables/config.yaml` channel/chat IDs, merges prompt from `prompts.build_channel_ephemeral_prompt()`, writes bindings. Exit code **2** if no IDs configured (intentional guard).

## Discord threads

- `discord.auto_thread` on @mention ≠ learnables behavior.
- Learnables uses explicit `discord` tool `create_thread` with `message_id` anchor (`tools/discord_tool.py`).
- Session context exposes `message_id`, `parent_chat_id`, `thread_id` when `discord` toolset enabled (`gateway/session.py`).

## `/learn` hook limitation

`command:learn` hook context today: `platform`, `user_id`, `command`, `args` — **no `chat_id`**. Implications:

- Empty `/learn` in learnables: handled by **channel_prompt + skill**, not hook room detection.
- Commit phrases (`learn this`, etc.) and `/learn learn this`: hook rewrites to `/queue` with `build_learn_prompt_for_learnables()` globally (safe).

Upstream improvement: pass `chat_id` / `thread_id` into hook_ctx (same fields as `agent:start` in `gateway/hooks.py`).

## Telegram

- Forum: each topic = `thread_id`; parent `chat_id` gets `channel_prompts`.
- No forum: skill uses reply chain + `Learnable ID: LB-<shortid>` on seed reply.

## Restart

Gateway restart required after `apply_config.py` mutates `config.yaml`. Hooks load from `~/.hermes/hooks/` at gateway startup.

## File map (this install)

```
~/.hermes/learnables/config.yaml
~/.hermes/learnables/prompts.py
~/.hermes/learnables/apply_config.py
~/.hermes/skills/productivity/learnables-workflow/SKILL.md
~/.hermes/hooks/learnables/{HOOK.yaml,handler.py}
```