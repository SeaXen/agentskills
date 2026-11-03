# Dashboard Connected Platforms env mismatch

## Symptom
The Hermes dashboard "Connected Platforms" card shows only `api_server`, even though Telegram and Discord are actually working.

## Verified diagnostic pattern
Check three sources separately:

1. `hermes status --all`
   - Should show Telegram/Discord configured and gateway running.
2. Gateway runtime status file
   - Read via `gateway.status.read_runtime_status()`.
   - Ground-truth example shape:
     - `telegram: connected`
     - `discord: connected`
     - `api_server: connected`
3. Dashboard API
   - Fetch `/api/status` from the live dashboard.
   - Broken case: `gateway_platforms` only contains `api_server`.

## Root cause
This is a dashboard backend filtering problem, not a gateway outage.

In `hermes_cli/web_server.py`, the dashboard reads runtime platform state, then filters it through:
- `load_gateway_config()`
- `get_connected_platforms()`

That means the dashboard process must itself see the relevant env-backed platform secrets.

If the dashboard process was started without:
- `TELEGRAM_BOT_TOKEN`
- `DISCORD_BOT_TOKEN`

then `load_gateway_config()` thinks only `api_server` is connected/configured and strips Telegram/Discord from the API payload, even while the gateway runtime file shows them as connected.

## Common clues
- Multiple manually started dashboards on different ports
- No `hermes-dashboard.service`
- Gateway PID has valid live runtime state, but dashboard PID environment lacks bot-token vars
- `/api/status` disagrees with `gateway.status.read_runtime_status()`

## Correct operator framing
Say:
- gateway runtime is healthy
- dashboard is under-reporting connected platforms
- root cause is dashboard-process environment mismatch

Do **not** say:
- Telegram/Discord are disconnected
- gateway is down
- config was removed

unless those were separately verified.

## Preferred fix
1. Stop stray/manual dashboard processes.
2. Relaunch dashboard from the proper Hermes/Bitwarden-loaded environment.
3. Recheck `/api/status` and the Connected Platforms card.

## Session-specific verified shape
Observed live state in this case:
- gateway runtime file: Telegram + Discord + API server all connected
- dashboard `/api/status`: only `api_server`
- no `hermes-dashboard.service` was present
