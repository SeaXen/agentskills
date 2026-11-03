# Notion MCP / API troubleshooting

Use this when a user says "Notion is already connected" but the current session cannot write to Notion.

## Distinguish the two integration paths

### 1) Regular Notion API path
- Uses `NOTION_API_KEY`
- Needed for the HTTP/curl or `ntn api ...` workflows in `SKILL.md`
- Missing this key means the standard Notion skill path is not ready even if an MCP server exists

### 2) Notion MCP path
- Separate from the regular API skill flow
- Usually exposed through Hermes via `hermes mcp list`
- Often launched by a wrapper script that exports `NOTION_TOKEN` before starting the Notion MCP server

## Fast verification sequence
1. Check whether the MCP server is configured and enabled:
   - `hermes mcp list`
2. If enabled, inspect the configured command or wrapper script.
3. Verify where the script expects the token from:
   - environment variable
   - `.env` file
   - Bitwarden/secret manager injection
4. Confirm the expected token name exactly:
   - `NOTION_API_KEY` for the standard API path
   - `NOTION_TOKEN` for many MCP wrapper scripts
5. If the user remembers setting it up, verify the secret source instead of assuming it is absent.

## Common pitfall
A session can have:
- Notion MCP **configured**
- but standard Notion API skill **not ready**
- and MCP still **non-functional** because the wrapper script's token source is empty or stale

Do not tell the user "Notion is not connected" until you have separated:
- config presence
- MCP enabled status
- actual token availability
- which credential name each path expects

## Reporting pattern
Report status in layers:
- "MCP configured / not configured"
- "MCP enabled / disabled"
- "token present / missing"
- "standard API key present / missing"

That avoids falsely collapsing all Notion states into one sentence.