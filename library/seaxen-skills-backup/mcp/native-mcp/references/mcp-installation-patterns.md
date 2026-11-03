# MCP Installation Patterns — Hermes Agent

Tested patterns for installing and registering MCP servers with Hermes Agent.

## Interactive Prompt Handling

All `hermes mcp add` commands are interactive. Pipe confirmations:

```bash
# For stdio servers (enable all tools):
echo -e "Y\n" | hermes mcp add SERVER_NAME --command node --args /path/to/index.js

# For URL-based servers (no auth + enable):
echo -e "n\nY\n" | hermes mcp add SERVER_NAME --url https://example.com/mcp

# For servers that fail to connect but you want to save config anyway:
echo -e "y\n" | hermes mcp add SERVER_NAME --command /path/to/run.sh
```

## Wrapper Script Pattern

When direct `--command/--args` fails (npm path issues, uv directory issues, npx arg parsing), create a wrapper:

```bash
#!/bin/bash
cd /path/to/mcp-server
exec node index.js    # or: exec uv run server-name
```

```bash
chmod +x /path/to/run.sh
echo -e "Y\n" | hermes mcp add server_name --command /path/to/run.sh
```

## Transport Types

### Stdio (most common)
```bash
hermes mcp add name --command node --args /path/to/index.js
hermes mcp add name --command uv --args "run --directory /path/to/dir server-name"
```

### HTTP/StreamableHTTP
```bash
hermes mcp add name --url https://example.com/mcp
```

### SSE — DOES NOT WORK RELIABLY
Hermes SSE client connects but session terminates immediately. Use HTTP endpoint instead.

**Example — CoinGecko:**
- ❌ `https://mcp.api.coingecko.com/sse` — connects then terminates
- ✅ `https://mcp.api.coingecko.com/mcp` — works (2 tools: execute JS, search docs)

## Environment Variables

Pass env vars via `--env KEY=VALUE`:

```bash
echo -e "Y\n" | hermes mcp add alphavantage --command /path/to/run.sh --env "ALPHAVANTAGE_API_KEY=your_key"
```

Or via wrapper script:
```bash
#!/bin/bash
export API_KEY="your_key"
exec node index.js
```

## Testing

```bash
hermes mcp test server_name    # Test connection and tool discovery
hermes mcp list                # List all configured servers
```

## Common Failures

| Symptom | Cause | Fix |
|---------|-------|-----|
| "Connection closed" | Server needs API key or env var | Add `--env KEY=VALUE` |
| "Connection closed" | Server binary not found | Use wrapper script with full path |
| "Connection closed" | Python relative import error | Use `python -m package.module` not `python src/package/module.py` |
| "Session terminated" | SSE transport issue | Use HTTP `/mcp` endpoint instead |
| "unrecognized arguments" | `--args` parsing issue | Use wrapper script |
| Tools not appearing | Server disabled (failed connect) | Fix connection, re-test, re-enable via config edit |
| Server saved as disabled | Initial connection failed | Edit `config.yaml`: `cfg['mcp_servers']['name']['enabled'] = True` |

## Resource-Heavy Builds

Some MCP servers require long compile times. Alternatives:

| Server | Build Time | Alternative |
|--------|-----------|-------------|
| Google MCP Toolbox | 5+ min (Go) | Skip or build offline |
| Open-Meteo (Rust) | 3+ min (cargo) | Use `@dangahagan/weather-mcp` (npm, instant) |
| Large Go/Rust projects | Varies | Check for pre-built binaries or npm alternatives |

## Python MCP Server Import Pattern

Many Python MCP servers fail with relative import errors when run directly:
```bash
# ❌ Fails: ImportError: attempted relative import with no known parent package
uv run src/package/server.py

# ✅ Works: Run as module
uv run python -m package.server
```

Always check the server's `pyproject.toml` `[project.scripts]` entry to find the correct module path.
