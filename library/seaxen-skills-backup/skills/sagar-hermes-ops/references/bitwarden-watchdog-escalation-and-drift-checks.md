# Bitwarden watchdog: fetch success vs real Hermes readiness

Use this pattern when Dr. Sagar asks for a Bitwarden watchdog that should be genuinely useful for Hermes operations rather than only proving the Bitwarden CLI works.

## Problem class

A naive Bitwarden watchdog that only runs:

```bash
bws secret list <project_id> --output json
```

can stay green while Hermes still has a practical secrets problem:
- required bot secrets are missing from the project
- gateway runtime lost Telegram/Discord connectivity
- dashboard API disagrees with gateway runtime and only shows `api_server`
- a restart-sensitive environment/secret propagation mismatch exists

So the watchdog must check more than raw fetch success.

## Recommended watchdog checks

Order matters:

1. **Config present**
   - `secrets.bitwarden.project_id`
   - `secrets.bitwarden.server_url`

2. **Bootstrap env present**
   - `BWS_ACCESS_TOKEN` available after loading `~/.hermes/.env`

3. **Bitwarden live fetch works**
   - `bws secret list <project_id> --output json --server-url <server_url>`

4. **Required project secrets exist**
   - at minimum for this setup:
     - `TELEGRAM_BOT_TOKEN`
     - `DISCORD_BOT_TOKEN`
   - optionally extend with other must-have secrets later

5. **Gateway runtime state is healthy**
   - read `~/.hermes/gateway_state.json`
   - require these platforms to be `connected`:
     - `telegram`
     - `discord`
     - `api_server`

6. **Dashboard API reflects reality**
   - fetch `http://127.0.0.1:9120/`
   - extract `window.__HERMES_SESSION_TOKEN__`
   - call `/api/status` with `X-Hermes-Session-Token`
   - check `gateway_platforms.telegram|discord|api_server`

7. **Detect runtime/dashboard drift**
   - if gateway runtime says `telegram=connected` but dashboard says missing/disconnected, alert on the mismatch explicitly

## Notification policy

For Dr. Sagar's watchdog channels, the useful default is:
- **silent on healthy runs**
- **silent on recovery** unless he explicitly asks for recovery posts
- **post only on new errors/problems**
- **dedupe unchanged ongoing failures** so the same fault does not spam every cron interval

This is different from backup-watchdog patterns where success posts may be desirable every day.

## Good alert shape

Use a compact operator-friendly message:

```md
🚨 **Bitwarden Watchdog Problem**

**Time:** 2026-06-01 16:16:20Z
**Project:** `...`
**Server:** `https://vault.bitwarden.com`
**Dashboard:** `http://127.0.0.1:9120`

**Summary**
- ✅ **Config project_id:** ...
- ✅ **Bitwarden live fetch:** OK (20 secrets)
- ❌ **Project secret DISCORD_BOT_TOKEN:** missing
- ✅ **Gateway runtime telegram:** connected
- ❌ **Dashboard API discord:** missing

**Problems detected**
- Required project secrets missing: DISCORD_BOT_TOKEN
- Runtime/dashboard platform drift detected: discord: runtime=connected, dashboard=missing
```

Why this format works:
- easy to scan on mobile/Discord
- separates raw checks from interpreted problems
- makes drift obvious instead of burying it in prose

## Durable lesson

For Hermes secret health, **Bitwarden fetch success is necessary but not sufficient**. The useful watchdog verifies the whole chain:

**Bitwarden fetch → required secrets present → gateway runtime connected → dashboard API agrees**.
