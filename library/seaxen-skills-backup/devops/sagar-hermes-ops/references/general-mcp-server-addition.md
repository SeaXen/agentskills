# General MCP Server Addition Workflow

Captures the reusable pattern for adding publicly available MCP servers (via npm/uvx/pip) to Hermes, discovered during TradingView/Bybit MCP setup session.

## Prerequisites

- Server must be available as a runnable CLI (`uvx`, `npx`, `pipx`, direct binary)
- Know the command and args: `uvx tradingview-mcp`, `npx @modelcontextprotocol/server-xxx`, etc.
- For stdio servers needing env vars, prepare them upfront

## Add Command Pattern

```bash
# Accept hooks on the PARENT hermes command, not the subcommand
# Pipe Y to auto-confirm tool enablement prompt
echo Y | hermes --accept-hooks mcp add <name> --command <cmd> --args "<arg1>" "<arg2>" --env KEY=VALUE

# Example: TradingView TA (73 tools, free Yahoo Finance data)
echo Y | hermes --accept-hooks mcp add tradingview-ta --command uvx --args "tradingview-mcp"

# Example: TradingView Chart (needs session cookie)
echo Y | hermes --accept-hooks mcp add tradingview-chart --command uvx --args "tradingview-chart-mcp" --env TRADINGVIEW_SESSION_ID=""
```

## Key Pitfalls Avoided

1. **`--accept-hooks` placement**: Must be on `hermes` CLI, not on `mcp add` subcommand
   - ❌ `hermes mcp add --accept-hooks ...`
   - ✅ `hermes --accept-hooks mcp add ...`

2. **Auto-confirm tool enablement**: `hermes mcp add` prompts "Enable all N tools? [Y/n/select]". Pipe `Y` or `printf 'Y\n'` to run unattended.

3. **Env vars with empty defaults**: For servers needing cookies/secrets (like TradingView Chart), add with placeholder then update via `hermes config set`:
   ```bash
   hermes config set mcp.servers.tradingview-chart.env.TRADINGVIEW_SESSION_ID "your_cookie_value"
   hermes mcp test tradingview-chart
   ```

## Verification Sequence

```bash
# 1. List shows enabled
hermes mcp list | grep <name>

# 2. Test discovers tools (but note pitfalls below)
hermes mcp test <name>

# 3. Restart session to use in chat
# New Hermes session required for tools to be callable
```

## Test vs Chat Usage Caution

**Critical**: `hermes mcp test` starts a **fresh OAuth flow** each run. For OAuth-based servers (Cloudflare, Notion, etc.), test will fail with "connection closed" but **actual chat usage works via cached tokens** in `~/.hermes/mcp-tokens/`.

For stdio servers (no OAuth), `hermes mcp test` is reliable.

Real verification for OAuth servers: manual JSON-RPC with cached token, or just start a chat session.

## Discovered Servers This Session

| Server | Command | Tools | Auth | Status |
|--------|---------|-------|------|--------|
| tradingview-ta (atilaahmettaner) | `uvx tradingview-mcp` | 73 | Optional (Yahoo Finance free) | ✅ Enabled |
| tradingview-chart (LangDB) | `uvx tradingview-chart-mcp` | Chart images | **Required**: TV session cookie | ⚠️ Needs cookie |
| bybit (sammcj/bybit-mcp) | `node /mnt/tb/hermes/scripts/mcp-servers/bybit-mcp/build/index.js` | Market data, charts, positions | **Required**: Bybit API key/secret | ⚠️ Installed, disabled |

## TradingView Session Cookie Extraction

1. Login to TradingView in browser
2. F12 → Application → Cookies → `https://www.tradingview.com`
3. Find `sessionid` → copy value
4. `hermes config set mcp.servers.tradingview-chart.env.TRADINGVIEW_SESSION_ID "<value>"`

## Bybit MCP Enable Path (When Ready)

```bash
# Add read-only API key on Bybit first
# Then set in Bitwarden or .env:
# BYBIT_API_KEY=***
# BYBIT_API_SECRET=***
# BYBIT_USE_TESTNET=false

hermes mcp enable bybit
hermes mcp test bybit
```

## Session Restart Required

After `hermes mcp add` or `hermes mcp enable`, **start a new Hermes session** before tools are available in chat. The CLI output explicitly states this.