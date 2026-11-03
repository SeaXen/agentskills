# Notion MCP: `hermes mcp test` False Negative Fix

## Problem
`hermes mcp test notion` reports **`✗ Connection failed (7285ms): Connection closed`** even when the Notion MCP server (`@notionhq/notion-mcp-server`) is **fully functional** in chat.

## Root Cause
The `mcp test` command only sends:
1. `initialize`
2. Waits for a response

The **Notion MCP server closes stdin** if no `tools/list` request follows within **~7 seconds** of idle time. This causes the test to fail, but the server is actually **working correctly** for real usage.

## Workaround
### 1. Ignore the Test Failure
- **`hermes mcp test` is a diagnostic with a brittle handshake.**
- **Always verify with a real tool call in chat** (e.g., `mcp_notion_get_page`).

### 2. Manual Verification
Send a **full handshake** manually to confirm the server works:

```bash
echo -e '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}\n{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}' | \
  NOTION_TOKEN=ntn_*** npx -y @notionhq/notion-mcp-server --transport stdio
```

**Expected Output:**
- A JSON response with `"result": {...}` containing the list of Notion tools.
- If this works, the server is **healthy** and the `hermes mcp test` failure is a **false negative**.

## Lesson
- **`mcp test` is not a reliable health check for stdio servers like Notion.**
- **Real tool calls in chat are the only reliable verification.**
- This applies to other stdio MCP servers that may have similar idle-timeout behavior.

## Affected Servers
- `@notionhq/notion-mcp-server` (confirmed)
- Potentially other stdio MCP servers with **idle stdin closure** behavior.

## Fix Status
- **No fix needed in Hermes.** This is expected behavior for stdio servers that close idle connections.
- **Documentation only:** This reference exists to prevent confusion when users see `✗ Connection failed` for a working server.
