# Antigravity Model Context Protocol (MCP) & Hooks

## 1. Model Context Protocol (MCP) Configuration

Antigravity natively integrates external tool servers using the Model Context Protocol.

### Workspace Configuration (`.agent/mcp_config.json`):

```json
{
  "mcpServers": {
    "local-tools": {
      "command": "node",
      "args": ["scripts/mcp-server.js"],
      "env": {
        "PORT": "3001"
      }
    },
    "postgres-inspector": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]
    }
  }
}
```

### Server Types:
- **`stdio`**: Standard input/output transport for local CLI commands and script processes.
- **`sse`**: Server-Sent Events over HTTP for remote or containerized tool providers.

---

## 2. Agent Lifecycle Hooks (`hooks.json`)

Hooks allow deterministic script execution at key agent lifecycle events.

### Supported Events:
- **`pre_tool_execution`**: Intercept tool calls before they execute (e.g., blocking dangerous commands or enforcing linting).
- **`post_tool_execution`**: Run verification or automatic formatting after a file edit or bash command.
- **`on_session_start`**: Initialize development environments, pull dependencies, or check local health.

### Format (`.agent/hooks.json`):
```json
{
  "hooks": [
    {
      "event": "post_tool_execution",
      "filter": { "tool": "edit_file", "pathPattern": "*.ts" },
      "command": "npx prettier --write ${path}"
    }
  ]
}
```
