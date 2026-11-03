# Gateway restart + Bitwarden cache expiry can drop Telegram/Discord

Use when Hermes gateway was previously connected to Telegram/Discord, then after a restart only `api_server` comes back even though the user says Bitwarden still contains the bot tokens.

## Durable pattern

A gateway restart can expose a Bitwarden auth problem that was masked by already-loaded secrets.

Typical sequence:
1. Gateway is running with Telegram/Discord already connected.
2. Hermes had a successful Bitwarden fetch earlier and wrote `~/.hermes/cache/bws_cache.json`.
3. `secrets.bitwarden.cache_ttl_seconds` expires.
4. Gateway restarts.
5. Hermes tries a fresh Bitwarden fetch instead of reusing stale in-memory secrets.
6. Live fetch returns `401 Unauthorized`.
7. `TELEGRAM_BOT_TOKEN` and `DISCORD_BOT_TOKEN` are not injected into the restarted process.
8. Gateway starts with only `api_server` even though cached/disk history proves the tokens existed recently.

## What to verify

- `hermes gateway status` or logs: gateway is running but only `1 platform(s)`.
- `hermes config check`: `TELEGRAM_BOT_TOKEN` and `DISCORD_BOT_TOKEN` show missing.
- `hermes secrets bitwarden status`: token env may still show present while live fetch fails with `401 Unauthorized`.
- `~/.hermes/cache/bws_cache.json`:
  - whether it exists
  - whether it still contains `TELEGRAM_BOT_TOKEN` and `DISCORD_BOT_TOKEN`
  - `fetched_at` timestamp
- compare `fetched_at` against restart time and configured `cache_ttl_seconds`.

## Interpretation rule

If `bws_cache.json` contains both bot tokens and the last successful fetch was only shortly before restart, but the restarted gateway comes up without Telegram/Discord, treat it as:

- **cached secrets existed**, but
- **live Bitwarden fetch failed at restart time**, so
- **platform loss was caused by secret reinjection failure**, not by disabling MCP itself.

## Good user-facing framing

Say plainly:
- disabling MCP was not the direct cause
- restart exposed Bitwarden secret refresh failure
- before restart the gateway was surviving on already-loaded or recently cached secrets
- after TTL expiry and restart, fresh fetch failed, so messaging platforms disappeared

## Safe recovery options

Real fix:
- restore Bitwarden fetch health for the configured project/token path, then restart the gateway.

Temporary recovery:
- increase `secrets.bitwarden.cache_ttl_seconds` so short restarts can reuse disk cache longer, or
- place the specific bot tokens in `.env` as a stopgap.

Do not overstate this as an MCP bug unless logs actually show platform config was removed.