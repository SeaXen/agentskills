# TradingView MCP patterns

## Two different TradingView MCP types

### 1) `tradingview-ta`
- Purpose: TA tools, scanners, backtesting, Pine helpers.
- Practical install path in Hermes:
  ```bash
  echo Y | hermes mcp add tradingview-ta --command uvx --args "tradingview-mcp"
  ```
- Result in this environment: Hermes discovered 73 tools and saved the server enabled.
- Note: `hermes mcp add` is interactive; piping `Y` avoids cancellation at the `Enable all tools?` prompt.

### 2) `tradingview-chart`
- Purpose: capture actual TradingView chart images/screenshots.
- Important distinction: this is **not** the same as `tradingview-ta` and was **not** installable here as a simple `uvx tradingview-chart-mcp` package.
- Working pattern used here:
  1. Clone repo locally under Hermes scripts.
  2. Create a venv inside the repo.
  3. Install requirements into that venv.
  4. Install `chromium` and `chromium-driver` on the host.
  5. Point `mcp_servers.tradingview-chart.command` to the venv Python.
  6. Point `args` to `main_optimized.py`.
  7. Set both TradingView cookies in `env`.

## Working config shape for chart MCP

```yaml
mcp_servers:
  tradingview-chart:
    command: /path/to/tradingview-chart-mcp/.venv/bin/python
    args:
      - /path/to/tradingview-chart-mcp/main_optimized.py
    enabled: true
    env:
      TRADINGVIEW_SESSION_ID: "..."
      TRADINGVIEW_SESSION_ID_SIGN: "..."
      MCP_SCRAPER_HEADLESS: "true"
      MCP_SCRAPER_USE_SAVE_SHORTCUT: "true"
```

## Required cookies
The chart scraper needed **both** of these from the user's TradingView session:
- `sessionid`
- `sessionid_sign`

Only setting `TRADINGVIEW_SESSION_ID` was insufficient for this server family.

## Verification pattern
Use a real transport test after config:
```bash
hermes mcp test tradingview-chart
```
Expected successful shape:
- transport shows stdio → local venv python
- tools discovered: `get_tradingview_chart_image`, `get_performance_stats`

Then do a real chart fetch, not just connection success.

## Practical user-facing caveat
This chart MCP borrows the user's active TradingView browser session. If the user logs out, clears cookies, or TradingView rotates the session, the MCP will stop working until `sessionid` and `sessionid_sign` are refreshed.

## Chart content caveat
The chart image reflects the user's TradingView layout/session state (drawings, indicators, theme) rather than agent-added overlays. Do not claim the agent added visible chart indicators unless you actually modified the TradingView layout yourself.