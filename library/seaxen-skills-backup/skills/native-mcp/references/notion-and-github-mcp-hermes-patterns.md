# Hermes patterns: GitHub + Notion MCP

## GitHub MCP in Hermes without storing a token in config

When `gh auth status` is already logged in, prefer a wrapper script over embedding `GITHUB_PERSONAL_ACCESS_TOKEN` in `config.yaml`.

Example:

```bash
#!/usr/bin/env bash
set -euo pipefail
export GITHUB_PERSONAL_ACCESS_TOKEN="$(gh auth token)"
exec npx -y @modelcontextprotocol/server-github
```

Hermes config then points `mcp_servers.github.command` to that script.

Why this is useful:
- avoids storing the token directly in `config.yaml`
- reuses the current `gh` login state
- keeps the MCP setup easy to rotate by changing GitHub CLI auth only

## Official remote Notion MCP

Remote endpoint:

```text
https://mcp.notion.com/mcp
```

This uses OAuth rather than a pasted token.

Practical Hermes behavior discovered in session:
- `hermes mcp add notion --url https://mcp.notion.com/mcp --auth oauth` can start the browser auth flow successfully
- if authorization is not fully completed before the connection attempt times out, Hermes may offer to save the config anyway
- if saved in that state, the server can appear in config with `enabled: false`
- the follow-up action is to complete auth and re-run `hermes mcp test notion`

## Local token-based Notion MCP

Useful fallback package:

```text
@notionhq/notion-mcp-server
```

Token shape seen working:

```text
NOTION_TOKEN=ntn_...
```

## Important `.env` parsing pitfall

Do not use a wrapper like this when your shared `.env` may contain unquoted values with spaces:

```bash
set -a
. /path/to/.env
set +a
```

Why:
- unrelated env lines can fail shell parsing
- the MCP wrapper can exit before the server starts
- the failure can look like a generic `Connection closed`

Safer pattern:
- extract only the needed variable (`NOTION_TOKEN`) with Python or another deterministic parser
- export that one variable
- exec the MCP server

Working pattern:

```bash
#!/usr/bin/env bash
set -euo pipefail
TOKEN=$(python3 - <<'PY'
from pathlib import Path
for line in Path('/path/to/.env').read_text().splitlines():
    if line.startswith('NOTION_TOKEN='):
        print(line.split('=',1)[1])
        break
else:
    raise SystemExit('NOTION_TOKEN not found')
PY
)
export NOTION_TOKEN="$TOKEN"
exec npx -y @notionhq/notion-mcp-server
```

## Verification pattern

After wiring an MCP server, verify with:

```bash
hermes mcp list
hermes mcp test <name>
```

Expected outcomes from this session:
- GitHub MCP: connected and discovered tools
- Notion MCP (local token-based): connected and discovered tools after switching from naive `.env` sourcing to single-variable extraction
