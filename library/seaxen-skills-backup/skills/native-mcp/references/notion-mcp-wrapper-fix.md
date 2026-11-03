# Notion MCP Wrapper Fix — Bitwarden Env Var Pattern

## Problem

Original wrapper script (`/mnt/tb/hermes/scripts/mcp-notion.sh`) read `NOTION_TOKEN` exclusively from `/mnt/tb/hermes/.env` file:

```bash
TOKEN=$(python3 - <<'PY'
from pathlib import Path
for line in Path('/mnt/tb/hermes/.env').read_text().splitlines():
    if line.startswith('NOTION_TOKEN='):
        print(line.split('=',1)[1])
        break
else:
    raise SystemExit('NOTION_TOKEN not found in /mnt/tb/hermes/.env')
PY
)
export NOTION_TOKEN="$TOKEN"
```

But Bitwarden Secrets Manager injects `NOTION_TOKEN` as an **environment variable**, not into the `.env` file. Result: script failed with "NOTION_TOKEN not found" even though `env | grep NOTION` showed `NOTION_TOKEN=ntn_...`.

## Fix

Updated wrapper to check env var first, fall back to `.env` file:

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

## General Pattern for Bitwarden-Injected Secrets

When using Bitwarden Secrets Manager with Hermes wrapper scripts:

```bash
# ALWAYS check env var first
if [[ -z "${SECRET_NAME:-}" ]]; then
  # Fallback: read from .env file
  SECRET_NAME=*** - <<'PY'
...
PY
  )
  export SECRET_NAME="$SECRET_NAME"
fi
```

This prevents silent failures where the secret is available in the environment but the script only reads from a file.

## Verification

After fix, manual JSON-RPC test works:
```bash
echo -e '{"jsonrpc":"2.0","id":1,"method":"initialize",...}\n{"jsonrpc":"2.0","id":2,"method":"tools/list",...}' | NOTION_TOKEN=*** npx -y @notionhq/notion-mcp-server
# Returns 20+ tools (search, pages, databases, blocks, comments, users)
```

`hermes mcp test notion` still reports failure (known diagnostic bug — sends only `initialize`, no `tools/list`), but actual chat tool calls work correctly.