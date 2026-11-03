# Bitwarden 401 after restart: cache vs `.env` vs MCP-edit false lead

## Use when
- User says Bitwarden started 401ing after an unrelated Hermes change such as MCP disable/restart.
- Telegram/Discord still work, so the auth failure looks contradictory.
- Operator insists the token was changed already and suspects Hermes rather than Bitwarden.

## Core diagnostic idea
Do not treat the restart as the root cause by default.

A Hermes restart after MCP edits often only **exposes** a Bitwarden live-auth problem because Hermes:
1. loads `.env`
2. tries Bitwarden
3. prefers fresh cache when available
4. does **not** block startup if Bitwarden fails

So you can see this mixed state:
- `bws secret list ...` -> `401 Unauthorized`
- gateway/runtime still healthy
- dashboard still shows Telegram/Discord connected
- user concludes "Hermes is lying" or "restart broke it"

Often the real explanation is:
- bot tokens are also present directly in `.env`
- or a recent Bitwarden cache is still serving secrets
- while **live** Bitwarden fetch is already broken

## Fast check sequence
1. Confirm direct `.env` presence of fallback keys without printing values:
   - `BWS_ACCESS_TOKEN`
   - `TELEGRAM_BOT_TOKEN`
   - `DISCORD_BOT_TOKEN`
   - `API_SERVER_KEY`
2. Run direct Bitwarden CLI probe:
   - `bws secret list <project_id> --output json --server-url <server_url>`
3. Inspect Bitwarden cache file metadata:
   - `~/.hermes/cache/bws_cache.json`
4. Compare current token fingerprint to the cache key.
5. Compare cache timestamp vs gateway restart time.
6. Check runtime truth separately:
   - `~/.hermes/gateway_state.json`
   - dashboard `/api/status`

## Interpretation rules
### Case A — direct `bws` 401 + gateway still healthy
Usually means live Bitwarden fetch is broken, but runtime survives from:
- direct `.env` secrets
- recent Bitwarden disk cache
- already-running injected process state

### Case B — current token fingerprint matches cache key
This is a very strong clue.

If:
- current `BWS_ACCESS_TOKEN` fingerprint matches `bws_cache.json` key
- cache timestamp is before the restart
- direct `bws` now returns 401

Then the same token worked recently and later lost access.

This points away from:
- MCP edits
- local quote/newline formatting corruption
- Hermes fabricating an error

And points toward:
- Bitwarden-side revocation
- project access loss
- machine-account scope change
- server/account mismatch after a previously valid window

### Case C — bot tokens present in `.env`
Then Telegram/Discord can remain connected even when Bitwarden is fully dead.
Do not misread healthy gateway state as proof Bitwarden is fine.

## What to say clearly
- The restart/MCP edit was the **trigger that exposed** the issue, not necessarily the thing that broke Bitwarden.
- Direct `bws` 401 means the failure is real and upstream of normal Hermes runtime logic.
- If the same token wrote cache earlier, this is best explained as Bitwarden-side access changing after the last successful fetch.

## Relevant Hermes behavior
Hermes Bitwarden integration:
- checks cache before live fetch
- uses disk cache under `~/.hermes/cache/bws_cache.json`
- does not block startup on Bitwarden failure
- continues with whatever `.env` already had

That explains why platform state can remain green while watchdog/direct checks fail.

## Session-specific validated pattern
Observed chain in this session:
- current token in `.env` was format-clean
- direct `bws secret list` returned `401 Unauthorized`
- `TELEGRAM_BOT_TOKEN` and `DISCORD_BOT_TOKEN` were present in `.env`
- current token fingerprint matched the Bitwarden cache key
- cache timestamp predated the Hermes gateway restart
- therefore the same token worked earlier, then later started 401ing
- restart after MCP edits exposed the problem but was not the primary root cause
