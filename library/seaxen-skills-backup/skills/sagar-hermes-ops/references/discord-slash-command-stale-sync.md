# Discord Slash Command Missing Despite Source Support

## Trigger
Use when a user says a Discord slash command like `/new` is missing from the Discord picker/menu even though Hermes documentation or source suggests it should exist.

## What happened in this session
- Hermes source defined both Discord commands:
  - `@tree.command(name="new", description="Start a new conversation")`
  - `@tree.command(name="reset", description="Reset your Hermes session")`
- Both commands mapped to the same internal action:
  - `/new` -> `"/reset"`
  - `/reset` -> `"/reset"`
- Live logs showed Discord slash sync being skipped with:
  - `Skipping Discord slash command sync: same slash-command fingerprint already synced`
- Live logs also showed `/reset` being invoked successfully on Discord.

## Durable interpretation
If source clearly registers the command but Discord does not show it, the first diagnosis should be **stale slash registration or client cache**, not "Hermes does not support that command".

## Fast diagnostic sequence
1. Check the source registration in `plugins/platforms/discord/adapter.py`.
2. Confirm whether the command exists in `hermes_cli/commands.py` or as an explicit `tree.command(...)`.
3. Check gateway logs for Discord sync behavior.
4. Look specifically for:
   - `Skipping Discord slash command sync: same slash-command fingerprint already synced`
   - successful invocation of an equivalent command like `/reset`
5. If the command exists in source and an equivalent command works, tell the user the command is likely missing from Discord due to stale sync/cache, and give the equivalent workaround.

## Practical answer shape
- State plainly that `/new` is supported in source.
- State that `/reset` is the current working equivalent if both map to the same internal reset path.
- Explain that Discord is likely serving a stale slash-command set or cached UI.
- If appropriate, offer a forced slash-command resync rather than claiming unsupported behavior.

## Evidence from this session
- Source registration: `plugins/platforms/discord/adapter.py` around the explicit `tree.command(name="new")` and `tree.command(name="reset")` definitions.
- Sync skip behavior: gateway log line `Skipping Discord slash command sync: same slash-command fingerprint already synced`.
- Working fallback: `/reset` invoked successfully in Discord logs.
