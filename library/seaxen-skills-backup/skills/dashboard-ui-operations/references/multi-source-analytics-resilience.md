# Multi-source analytics data resilience

When building a monitoring/analytics dashboard, NEVER rely on a single data
source. If that source goes down, the entire dashboard is blank.

## Pattern

Identify all independent data sources that carry the metrics you need, then
build collectors for each. The dashboard aggregates across all sources.

```
Dashboard
├── Source A: proxy gateway call_logs (JSON files by date)
├── Source B: proxy gateway SQLite DB (provider health, connections)
├── Source C: upstream service stats API (engine health)
├── Downstream tool debug logs (per-tool call traces)
└── Config file inspection (is backend X configured?)
```

## Why each source is independent

- **Gateway call_logs**: exist only when traffic routes through the gateway.
  If the gateway is down or the user bypasses it, these are empty.
- **Gateway SQLite**: stores provider connection metadata, API keys, health
  checks. Persists across restarts but only has data if the gateway manages
  providers.
- **Upstream stats API**: lives on the upstream service (e.g. SearXNG /stats).
  Available as long as the upstream is running, regardless of gateway state.
- **Tool debug logs**: written by the downstream tool (e.g. Hermes) when
  `WEB_TOOLS_DEBUG=true`. Captures ALL tool calls regardless of which proxy
  they route through. This is the **independent fallback** — works even when
  the gateway is dead.
- **Config inspection**: reads `~/.hermes/config.yaml` and `.env` to detect
  whether a backend is configured at all. Gives context for empty data
  (is it "no backend" or "backend exists but no calls yet"?).

## Implementation checklist

1. **Each collector function returns a normalized list of dicts** with common
   fields: `timestamp`, `provider`, `status`, `duration_ms`.
2. **Combine sources with deduplication** — the same request may appear in
   both gateway logs and tool debug logs. Deduplicate by `(timestamp, query)`
   or `(timestamp, url)`.
3. **Show source attribution** in the UI — "X from gateway, Y from debug logs"
   so the user knows where data comes from.
4. **Show a setup notice** when a critical source is missing, not just an
   empty table. Tell the user exactly what to configure.
5. **Config detection** — check both `config.yaml` settings AND environment
   variables. Some backends need both (e.g. SearXNG needs `SEARXNG_URL` in
   both config.yaml and .env).

## Real-world example: AceRoute

AceRoute analytics dashboard reads from:
- OmniRoute `/mnt/tb/1Apps/omniroute/data/call_logs/YYYY-MM-DD/*.json`
- OmniRoute `/mnt/tb/1Apps/omniroute/data/storage.sqlite`
- SearXNG `http://127.0.0.1:8080/stats` (HTML scrape)
- Hermes `/root/logs/web_tools_debug_*.json` (enabled via `WEB_TOOLS_DEBUG=true`)
- Hermes `~/.hermes/config.yaml` (backend detection)

When OmniRoute went down, the dashboard showed zeros. Fix: enable
`WEB_TOOLS_DEBUG=true` in `~/.hermes/.env` so Hermes writes its own debug
logs independently. Now the dashboard has data from two independent paths.

## Hermes debug logging

```bash
# ~/./.env
WEB_TOOLS_DEBUG=true
```

When enabled, Hermes writes `web_tools_debug_<UUID>.json` to `/root/logs/`
on every web_search and web_extract call. These files contain the full
request/response including provider, latency, results, and errors.

This is the key mechanism for making analytics independent of any proxy
gateway. Always enable it when building monitoring dashboards.
