# Notion MCP Setup for Hermes Agent

## Overview
Notion MCP can be configured in Hermes in **two ways**:
1. **Official Remote Notion MCP via OAuth** (recommended for most users)
2. **Local Token-Based Notion MCP** (fallback for environments where OAuth flow is awkward)

Both approaches expose Notion as MCP tools (e.g., `mcp_notion_search`, `mcp_notion_get_page`, etc.) that can be called directly from Hermes.

---

## Option 1: Remote Notion MCP (OAuth)

### Configuration
```yaml
# ~/.hermes/config.yaml
mcp_servers:
  notion:
    url: "https://mcp.notion.com/mcp"
    auth: oauth
    enabled: true
```

### Setup Steps
1. **Enable the server**:
   ```bash
   hermes config set mcp_servers.notion.enabled true
   ```

2. **Test the connection**:
   ```bash
   hermes mcp test notion
   ```
   - This opens a browser to complete OAuth authorization.
   - If the browser doesn't open, manually visit the URL shown in the terminal.

3. **Complete OAuth flow**:
   - Approve the consent screen in your browser.
   - The token is cached locally and reused for future sessions.

4. **Restart Hermes**:
   ```bash
   hermes restart
   ```

### Pitfalls
- **Timeout during auth**: If the OAuth flow isn't completed in time, Hermes may save the server as disabled. Re-run `hermes mcp test notion` after completing auth.
- **Non-interactive environments**: `hermes mcp test` and `hermes mcp login` fail in headless environments (Docker, SSH without TTY). Run from an interactive terminal.
- **False negatives in `hermes mcp test`**: The test may report `✗ Connection failed` even when the server works in chat. This is because the test only sends `initialize` and some servers (like Notion) close stdin if no `tools/list` follows within ~7 seconds. **Always verify with a real tool call in chat** (e.g., `mcp_notion_search`).

---

## Option 2: Local Token-Based Notion MCP

### Prerequisites
- A **Notion integration token** (`NOTION_TOKEN=ntn_...`).
  - Create one at: [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)
  - Share your Notion pages/databases with the integration.
- **Node.js** installed (for `npx`).

### Configuration
Use a **wrapper script** to pass the token securely. **Do not** blindly source large `.env` files (shell parsing may break on lines with spaces).

#### Wrapper Script Template
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

Save this as `/root/.hermes/scripts/mcp-notion.sh` and make it executable:
```bash
chmod +x /root/.hermes/scripts/mcp-notion.sh
```

#### Hermes Config
```yaml
# ~/.hermes/config.yaml
mcp_servers:
  notion:
    command: "/root/.hermes/scripts/mcp-notion.sh"
    enabled: true
    timeout: 60
    connect_timeout: 30
```

### Setup Steps
1. **Save the wrapper script** (above).
2. **Add to Hermes config** (above).
3. **Restart Hermes**:
   ```bash
   hermes restart
   ```
4. **Verify tools**:
   ```bash
   hermes tools | grep mcp_notion
   ```
   Should list tools like `mcp_notion_search`, `mcp_notion_get_page`, etc.

---

## Common Issues

### 1. `hermes mcp test notion` Fails but Tools Work in Chat
**Symptom**: `hermes mcp test notion` shows `✗ Connection failed (7285ms): Connection closed` but tools work fine in chat.

**Root Cause**: The `mcp test` command only sends `initialize` and waits for a response. The Notion MCP server closes stdin if no `tools/list` request follows within ~7 seconds.

**Workaround**: Ignore the test failure. Verify by calling a real tool in chat (e.g., `mcp_notion_search`).

**Manual Verification**:
```bash
echo -e '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}\n{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}' | NOTION_TOKEN=ntn_*** npx -y @notionhq/notion-mcp-server --transport stdio
```

---

### 2. Notion MCP Server Not Starting
**Symptom**: No `mcp_notion_*` tools appear after restarting Hermes.

**Debug Steps**:
1. Check if the process is running:
   ```bash
   ps aux | grep notion
   ```
2. Manually run the wrapper script to see errors:
   ```bash
   bash /root/.hermes/scripts/mcp-notion.sh
   ```
3. Common fixes:
   - Ensure `NOTION_TOKEN` is set (check with `echo $NOTION_TOKEN`).
   - Install `@notionhq/notion-mcp-server`:
     ```bash
     npm install -g @notionhq/notion-mcp-server
     ```
   - Check Node.js version (`node --version`). Requires Node.js 18+.

---

### 3. Permission Errors
**Symptom**: `Error: Notion API error: 403 Forbidden` or `401 Unauthorized`.

**Fix**:
1. Verify your `NOTION_TOKEN` is correct and not expired.
2. Ensure the **Notion integration** has access to the target page/database.
   - Go to the page in Notion → **Share** → **Invite a person** → Search for your integration name.
3. Regenerate the token if needed.

---

### 4. Rate Limiting
**Symptom**: `Error: Notion API error: 429 Too Many Requests`.

**Fix**:
- Notion’s free tier has **rate limits** (3 requests per second).
- Reduce request frequency or upgrade to a paid plan.
- Use `timeout` in Hermes config to avoid retries on rate-limited calls.

---

## Tool Reference
Once configured, the following tools become available (prefix: `mcp_notion_`):

| Tool | Description | Example |
|------|-------------|---------|
| `search` | Search Notion pages/databases | `mcp_notion_search({"query": "Hermes"})` |
| `get_page` | Get a page by ID | `mcp_notion_get_page({"page_id": "37a5588e846f8081b37df1bd6436b3fa"})` |
| `get_database` | Get a database by ID | `mcp_notion_get_database({"database_id": "..."})` |
| `query_database` | Query a database | `mcp_notion_query_database({"database_id": "...", "filter": {...}})` |
| `create_page` | Create a new page | `mcp_notion_create_page({"parent_id": "...", "properties": {...}})` |
| `update_page` | Update a page | `mcp_notion_update_page({"page_id": "...", "properties": {...}})` |

---

## Best Practices
1. **Use Remote OAuth for Simplicity**: Prefer the remote MCP server (`https://mcp.notion.com/mcp`) unless you have a specific reason to use the local token-based approach.
2. **Secure Token Storage**: Store `NOTION_TOKEN` in Bitwarden or a secure `.env` file. Never commit it to Git.
3. **Test with Real Calls**: `hermes mcp test` is brittle for Notion. Always verify with a real tool call in chat.
4. **Monitor Usage**: Notion’s free tier has limits. Use `mcp_notion_search` sparingly in automated workflows.

---

## Migration from 9router/OmniRoute
If you previously used Notion with **9router** or **OmniRoute**, DurinDoor inherits the same MCP setup. No changes are needed—just ensure the server is enabled in `~/.hermes/config.yaml`.

---

## References
- [Official Notion MCP Server](https://github.com/notionhq/notion-mcp-server)
- [Notion Integration Tokens](https://www.notion.so/my-integrations)
- [Hermes MCP Documentation](https://hermes-agent.nousresearch.com/docs/mcp)
