# Hermes `mcp test` False Negative — Stdio Handshake Bug

## Issue

`hermes mcp test <server>` shows `✗ Connection failed (7285ms): Connection closed` for working stdio servers.

## Affected Servers (Confirmed)

- Notion: `@notionhq/notion-mcp-server`
- Likely others that close stdin on idle after `initialize`

## Root Cause

The `mcp test` command:
1. Spawns server subprocess
2. Sends `initialize` request
3. Waits for response
4. **Does not send `tools/list`**
5. Times out after ~7s idle → server closes connection

## Evidence

Manual JSON-RPC with full handshake works:
```bash
echo -e '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}\n{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}' | NOTION_TOKEN=ntn_... npx -y @notionhq/notion-mcp-server --transport stdio
# Returns 20+ tools
```

## Impact

| Context | Result |
|---------|--------|
| `hermes mcp test notion` | ❌ False negative |
| Chat tool calls (`mcp_notion_*`) | ✅ Works correctly |
| Agent startup discovery | ✅ Works correctly |

## Workaround

Ignore `mcp test` failure. Verify via:
1. Actual tool call in chat
2. Manual JSON-RPC handshake (as above)

## Fix Needed (Hermes Core)

`mcp test` command should send `initialize` → `tools/list` before declaring success/failure. Current single-request handshake is brittle.