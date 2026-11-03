# MCP wrapper scripts reading Bitwarden-injected secrets

## The problem
On Dr. Sagar's Hermes setup, Bitwarden Secrets Manager injects API tokens as **environment variables** into the Hermes process tree. However, many stdio MCP wrapper scripts (e.g. `/mnt/tb/hermes/scripts/mcp-notion.sh`) only read credentials from a local `.env` file, ignoring the injected env var.

This causes `hermes mcp test <name>` to fail with "Connection closed" even when the token exists in Bitwarden and is being injected.

## The fix pattern
Update wrapper scripts to **prefer the environment variable** (injected by Bitwarden) and **fall back to `.env` file**:

```bash
#!/usr/bin/env bash
set -euo pipefail

# Prefer env var (injected by Bitwarden), fall back to .env file
if [[ -z "${NOTION_TOKEN:-}" ]]; then
  TOKEN=$(python3 - <<'PY'
from pathlib import Path
for line in Path('/mnt/tb/hermes/.env').read_text().splitlines():
    if line.startswith('NOTION_TOKEN='):
        print(line.split('=',1)[1])
        break
else:
    raise SystemExit('NOTION_TOKEN not found in environment or /mnt/tb/hermes/.env')
PY
  )
  export NOTION_TOKEN="$TOKEN"
fi

exec npx -y @notionhq/notion-mcp-server
```

## Debugging checklist
1. Verify token is injected: `env | grep <TOKEN_NAME>` in a Hermes shell
2. Test MCP server manually with JSON-RPC:
   ```bash
   echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}' | <TOKEN_NAME>=*** npx -y <mcp-package> --transport stdio
   ```
3. Follow with `tools/list` to confirm tools are discovered
4. If manual test works but `hermes mcp test` fails: the Hermes test command may have a timeout/handshake issue with that server — the server is functionally connected.

## Applies to
- `@notionhq/notion-mcp-server` (fixed in session)
- Any stdio MCP server where the wrapper script reads from `.env` instead of `env`
- Servers using `NOTION_TOKEN`, `GITHUB_TOKEN`, `DISCORD_BOT_TOKEN`, etc.

## Key lesson
`hermes mcp test` can give **false negatives**. Always verify manually with JSON-RPC before concluding an MCP server is broken.