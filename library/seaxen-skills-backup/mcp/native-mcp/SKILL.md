---
name: native-mcp
description: "MCP client: connect servers, register tools (stdio/HTTP)."
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [MCP, Tools, Integrations]
    related_skills: [mcporter]
---

# Native MCP Client

Hermes Agent has a built-in MCP client that connects to MCP servers at startup, discovers their tools, and makes them available as first-class tools the agent can call directly. No bridge CLI needed -- tools from MCP servers appear alongside built-in tools like `terminal`, `read_file`, etc.

## When to Use

Use this whenever you want to:
- Connect to MCP servers and use their tools from within Hermes Agent
- Add external capabilities (filesystem access, GitHub, databases, APIs) via MCP
- Run local stdio-based MCP servers (npx, uvx, or any command)
- Connect to remote HTTP/StreamableHTTP MCP servers
- Have MCP tools auto-discovered and available in every conversation

This is also the umbrella for remote-MCP operational lessons such as auth mode choice, header hardening, timeout tuning, and transport-vs-real-API verification.

For ad-hoc, one-off MCP tool calls from the terminal without configuring anything, see the `mcporter` skill instead.

## OAuth 2.1 PKCE (for HTTP MCP servers)

Most hosted HTTP MCP servers (`https://mcp.cloudflare.com/mcp`, `https://mcp.notion.com/mcp`, `https://agent.tinyfish.ai/mcp`, etc.) require a one-time OAuth 2.1 PKCE authorization before tool calls work.

**Enable the server (the `patch` tool refuses to edit `config.yaml`, so use the CLI):**
```bash
hermes config set mcp_servers.<name>.enabled true
```

**Quick transport + auth check:**
```bash
hermes mcp test <name>
```

**First-time login (must run from an interactive terminal):**
```bash
hermes mcp login <name>
```
This opens a browser to the authorization URL. Approve the consent screen; the token is cached locally and reused for future chat tool calls.

**When the agent itself runs in a non-interactive environment** (Discord bot, headless service, Docker, SSH without TTY): `hermes mcp test` and `hermes mcp login` both report *"non-interactive environment and no cached tokens found."* Wrapping with `script` reveals the OAuth URL, but the redirect callback target is `http://127.0.0.1:<port>/callback` on the agent's host loopback, so the round-trip cannot close from inside the agent. The user has to run `hermes mcp login <name>` from their own interactive terminal. See `references/mcp-oauth-non-interactive.md` for the full pattern (state matrix, PTY workarounds, what to honestly report back).

## Remote HTTP MCP durable lessons

For hosted MCP servers, especially Cloudflare-style HTTP endpoints:
- keep OAuth and API-token auth as separate entries instead of one magical fallback config
- use browser-like headers when a remote MCP is sensitive to generic client signatures
- raise `timeout` and `connect_timeout` when headless/remote sessions connect inconsistently
- do a **transport test first**, then a **real API-use test**; `Connected` alone is not enough
- if a token works against a provider's REST verification endpoint but not the MCP endpoint, treat that as an MCP-specific auth/hardening problem rather than immediately blaming the token

### Cloudflare MCP endpoint (`https://mcp.cloudflare.com/mcp`) — OAuth only

**Config that works:**
```yaml
mcp_servers:
  cloudflare-api:
    url: https://mcp.cloudflare.com/mcp
    auth: oauth
    enabled: true
```

**Config that does NOT work:**
```yaml
mcp_servers:
  cloudflare-api-token:
    url: https://mcp.cloudflare.com/mcp
    enabled: true
    headers:
      Authorization: Bearer ${CLOUDFLARE_API_TOKEN}
```

**Why:** This endpoint only supports OAuth 2.1 PKCE. Bearer tokens that work against Cloudflare's REST API return `400 Bad Request` at the MCP endpoint.

**One-time setup:** First run `hermes mcp test cloudflare-api` — it opens a browser to the authorization URL. Complete the consent screen ("Allow"). After this, the token is cached and subsequent chat tool calls work automatically.

**Note:** `cloudflare-observability` uses a different URL (`https://observability.mcp.cloudflare.com/mcp`) with OAuth and works separately.

## Prerequisites

- **mcp Python package** -- optional dependency; install with `pip install mcp`. If not installed, MCP support is silently disabled.
- **Node.js** -- required for `npx`-based MCP servers (most community servers)
- **uv** -- required for `uvx`-based MCP servers (Python-based servers)

Install the MCP SDK:

```bash
pip install mcp
# or, if using uv:
uv pip install mcp
```

## Quick Start

Add MCP servers to `~/.hermes/config.yaml` under the `mcp_servers` key:

```yaml
mcp_servers:
  time:
    command: "uvx"
    args: ["mcp-server-time"]
```

Restart Hermes Agent. On startup it will:
1. Connect to the server
2. Discover available tools
3. Register them with the prefix `mcp_time_*`
4. Inject them into all platform toolsets

You can then use the tools naturally -- just ask the agent to get the current time.

## Configuration Reference

Each entry under `mcp_servers` is a server name mapped to its config. There are two transport types: **stdio** (command-based) and **HTTP** (url-based).

### Stdio Transport (command + args)

```yaml
mcp_servers:
  server_name:
    command: "npx"             # (required) executable to run
    args: ["-y", "pkg-name"]   # (optional) command arguments, default: []
    env:                       # (optional) environment variables for the subprocess
      SOME_API_KEY: "value"
    timeout: 120               # (optional) per-tool-call timeout in seconds, default: 120
    connect_timeout: 60        # (optional) initial connection timeout in seconds, default: 60
```

### HTTP Transport (url)

```yaml
mcp_servers:
  server_name:
    url: "https://my-server.example.com/mcp"   # (required) server URL
    headers:                                     # (optional) HTTP headers
      Authorization: "Bearer sk-..."
    timeout: 180               # (optional) per-tool-call timeout in seconds, default: 120
    connect_timeout: 60        # (optional) initial connection timeout in seconds, default: 60
```

### All Config Options

| Option            | Type   | Default | Description                                       |
|-------------------|--------|---------|---------------------------------------------------|
| `command`         | string | --      | Executable to run (stdio transport, required)     |
| `args`            | list   | `[]`    | Arguments passed to the command                   |
| `env`             | dict   | `{}`    | Extra environment variables for the subprocess    |
| `url`             | string | --      | Server URL (HTTP transport, required)             |
| `headers`         | dict   | `{}`    | HTTP headers sent with every request              |
| `timeout`         | int    | `120`   | Per-tool-call timeout in seconds                  |
| `connect_timeout` | int    | `60`    | Timeout for initial connection and discovery      |

Note: A server config must have either `command` (stdio) or `url` (HTTP), not both.

## How It Works

### Startup Discovery

When Hermes Agent starts, `discover_mcp_tools()` is called during tool initialization:

1. Reads `mcp_servers` from `~/.hermes/config.yaml`
2. For each server, spawns a connection in a dedicated background event loop
3. Initializes the MCP session and calls `list_tools()` to discover available tools
4. Registers each tool in the Hermes tool registry

### Tool Naming Convention

MCP tools are registered with the naming pattern:

```
mcp_{server_name}_{tool_name}
```

Hyphens and dots in names are replaced with underscores for LLM API compatibility.

Examples:
- Server `filesystem`, tool `read_file` → `mcp_filesystem_read_file`
- Server `github`, tool `list-issues` → `mcp_github_list_issues`
- Server `my-api`, tool `fetch.data` → `mcp_my_api_fetch_data`

### Auto-Injection

After discovery, MCP tools are automatically injected into all `hermes-*` platform toolsets (CLI, Discord, Telegram, etc.). This means MCP tools are available in every conversation without any additional configuration.

### Connection Lifecycle

- Each server runs as a long-lived asyncio Task in a background daemon thread
- Connections persist for the lifetime of the agent process
- If a connection drops, automatic reconnection with exponential backoff kicks in (up to 5 retries, max 60s backoff)
- On agent shutdown, all connections are gracefully closed

### Idempotency

`discover_mcp_tools()` is idempotent -- calling it multiple times only connects to servers that aren't already connected. Failed servers are retried on subsequent calls.

## Transport Types

### Stdio Transport

The most common transport. Hermes launches the MCP server as a subprocess and communicates over stdin/stdout.

```yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
```

The subprocess inherits a **filtered** environment (see Security section below) plus any variables you specify in `env`.

### HTTP / StreamableHTTP Transport

For remote or shared MCP servers. Requires the `mcp` package to include HTTP client support (`mcp.client.streamable_http`).

```yaml
mcp_servers:
  remote_api:
    url: "https://mcp.example.com/mcp"
    headers:
      Authorization: "Bearer sk-..."
```

If HTTP support is not available in your installed `mcp` version, the server will fail with an ImportError and other servers will continue normally.

### SSE Transport — NOT RECOMMENDED

Hermes SSE client connects but session terminates immediately for many servers. **Use HTTP endpoint instead.**

Known failing SSE endpoints:
- CoinGecko: `https://mcp.api.coingecko.com/sse` — connects then terminates
- Workaround: Use `https://mcp.api.coingecko.com/mcp` (HTTP) instead

## Security

### Environment Variable Filtering

For stdio servers, Hermes does NOT pass your full shell environment to MCP subprocesses. Only safe baseline variables are inherited:

- `PATH`, `HOME`, `USER`, `LANG`, `LC_ALL`, `TERM`, `SHELL`, `TMPDIR`
- Any `XDG_*` variables

All other environment variables (API keys, tokens, secrets) are excluded unless you explicitly add them via the `env` config key. This prevents accidental credential leakage to untrusted MCP servers.

```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      # Only this token is passed to the subprocess
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_..."
```

### Credential Stripping in Error Messages

If an MCP tool call fails, any credential-like patterns in the error message are automatically redacted before being shown to the LLM. This covers:

- GitHub PATs (`ghp_...`)
- OpenAI-style keys (`sk-...`)
- Bearer tokens
- Generic `token=`, `key=`, `API_KEY=`, `password=`, `secret=` patterns

## MCP Installation Patterns

For detailed installation patterns including interactive prompt handling, wrapper scripts, and resource-heavy build alternatives, see `references/mcp-installation-patterns.md`.

Key takeaways:
- **Always pipe confirmations**: `echo -e "Y\n" | hermes mcp add ...`
- **Use wrapper scripts** when direct `--command/--args` fails
- **SSE doesn't work reliably** — prefer HTTP endpoints
- **Some packages aren't on PyPI** — install from source + wrapper script

## Crypto / Blockchain MCP Servers

For tested crypto MCP servers (DexScreener, crypto-data-mcp, CoinGecko, Bybit), Polymarket (`graph-polymarket-mcp`), and free crypto-news RSS sources — plus critical Hermes compatibility pitfalls (CoinGecko SSE failure, `hermes mcp add --env` placeholder trap, `crypto-data-mcp` not on PyPI) — see `references/crypto-mcp-servers.md`. Always check `/mnt/tb/hermes/scripts/mcp-servers/` first; many are pre-built but disabled.

For TradingView-specific MCP setup patterns — including the split between `tradingview-ta` and screenshot-oriented `tradingview-chart`, the need to pipe `Y` into `hermes mcp add`, the local-venv + Chromium pattern for chart capture, and the requirement for both `sessionid` and `sessionid_sign` cookies — see `references/tradingview-mcp-patterns.md`.

For **free third-party community MCPs** (medical-mcp, crypto-indicators-mcp, kukapay/* Python repos, mcp-server-fetch-typescript, graph-polymarket-mcp) and the non-obvious install pitfalls — broken npm bin shims, kukapay's "no executables" Python packages, `hermes mcp add --args` config corruption, 40s first-install timeout, and npm canary package name traps — see `references/free-third-party-mcp-installs.md`.

## Troubleshooting

### "MCP SDK not available -- skipping MCP tool discovery"

The `mcp` Python package is not installed. Install it:

```bash
pip install mcp
```

### "No MCP servers configured"

No `mcp_servers` key in `~/.hermes/config.yaml`, or it's empty. Add at least one server.

### "Failed to connect to MCP server 'X'"

Common causes:
- **Command not found**: The `command` binary isn't on PATH. Ensure `npx`, `uvx`, or the relevant command is installed.
- **Package not found**: For npx servers, the npm package may not exist or may need `-y` in args to auto-install.
- **Timeout**: The server took too long to start. Increase `connect_timeout`.
- **Port conflict**: For HTTP servers, the URL may be unreachable.
- **SSE transport**: Session terminates immediately. Use HTTP endpoint instead.

### "MCP server 'X' requires HTTP transport but mcp.client.streamable_http is not available"

Your `mcp` package version doesn't include HTTP client support. Upgrade:

```bash
pip install --upgrade mcp
```

### Tools not appearing

- Check that the server is listed under `mcp_servers` (not `mcp` or `servers`)
- Ensure the YAML indentation is correct
- Look at Hermes Agent startup logs for connection messages
- Tool names are prefixed with `mcp_{server}_{tool}` -- look for that pattern

### MCP server causing TUI/gateway instability

A misconfigured MCP server (e.g. Discord MCP with no token) can spam the gateway with invalid messages every few seconds, causing the TUI events feed to disconnect. See the "Discord MCP server spamming pydantic errors" pitfall above. General pattern: if the TUI disconnects and gateway logs show repeated pydantic/MCP validation errors, identify the offending MCP server with `ps aux | grep mcp-` and either fix its config or disable it.

### Connection keeps dropping

The client retries up to 5 times with exponential backoff (1s, 2s, 4s, 8s, 16s, capped at 60s). If the server is fundamentally unreachable, it gives up after 5 attempts. Check the server process and network connectivity.

### `hermes mcp test` reports false negatives for some stdio servers

**Symptom:** `hermes mcp test <server>` shows `✗ Connection failed (7285ms): Connection closed` but the server works fine when actually used in chat.

**Root cause:** The `mcp test` command only sends `initialize` and waits for a response. Some MCP servers (Notion `@notionhq/notion-mcp-server`, and potentially others) close stdin if no `tools/list` request follows within ~7 seconds idle.

**Workaround:** Ignore the test failure. Verify by running a real tool call in chat, or manually send `initialize` → `tools/list` via JSON-RPC:

```bash
echo -e '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}\n{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}' | NOTION_TOKEN=*** npx -y @notionhq/notion-mcp-server --transport stdio
```

**Lesson:** `mcp test` is a diagnostic with a brittle handshake. Actual agent usage does the full handshake and works correctly.

### Disable vs Remove — there is no `disable` subcommand

`hermes mcp` does NOT have a `disable` action (only `add`, `remove`, `test`, `list`, `login`). When a user says "disable X", they want the wrapper, source, and config entry preserved (just turned off), not deleted.

**Pattern (preserve, save as disabled):**

```bash
# 1. Remove cleanly (also cleans OAuth tokens)
printf 'y\n' | hermes mcp remove <name>

# 2. Re-add; when the connection prompt comes, choose "Y/n" to save anyway
#    Hermes will save with `enabled: false`
printf 'y\ny\n' | hermes mcp add <name> --command /path/to/wrapper.sh --env "KEY=${KEY}"
```

**Verification:** `hermes mcp list` should show `<name>` with `✗ disabled` status. The wrapper script in `/mnt/tb/hermes/scripts/mcp-servers/<name>-mcp/run.sh` is untouched and the source directory (e.g. `<name>-src/`) is preserved for future rebuilds.

**Anti-pattern:** do not `rm -rf` the wrapper or source directory before removing the config entry. If the user upgrades their plan later, they'll want to re-enable without re-cloning.

## Pitfall: Broken ESM entry-point check silently exits

**Symptom:** `hermes mcp test <name>` reports `✗ Connection failed: Connection closed`. Manual `node <path>/build/index.js` exits immediately with no output and exit code 0. Running `npx -y <pkg>` similarly returns blank output.

**Root cause:** The published npm package's `bin` shim and built `index.js` use this common ESM pattern that fails for some install paths:

```js
if (process.argv[1] === new URL(import.meta.url).pathname) {
    const server = new Server();
    server.run().catch(console.error);
}
export { Server };
```

When `process.argv[1]` (the path Hermes passed) doesn't exactly equal the resolved `import.meta.url` pathname (e.g. due to symlinks, `/mnt/tb` vs `/root/.hermes` resolution, or how `node -e` invokes), the entry-point check is false → the server is never started → the process exits silently.

**Fix:** Wrap the package with a tiny `#!/usr/bin/env node` shim that imports the built module directly and calls the class:

```bash
cat > /path/to/wrapper.sh <<'EOF'
#!/usr/bin/env node
import('<abs/path>/build/index.js')
  .then(mod => new mod.Server().run().catch(e => { console.error('ERR:', e.message); process.exit(1); }));
EOF
chmod +x /path/to/wrapper.sh
```

This bypasses the broken entry-point guard. Real failure mode observed: `mcp-open-library` (8enSmith). Affects any package where the build output relies on `process.argv[1] === new URL(import.meta.url).pathname` for entry-point detection.

**Smell test before applying this fix:** clone the repo, `npm install && npm run build`, then run `node build/index.js` directly. If it exits silently within 5s with code 0 and no output → entry-point check is the issue.

## Pitfall: npm package name typos waste 5+ minutes each

Three near-misses that bite during MCP installs (all hit in one session):

- `@8enSmith/mcp-open-library` (capital S, scoped) → **404**, doesn't exist. Correct: `mcp-open-library` (no scope).
- `@mcp-dockmaster/mcp-server-defillama` → **404**, the dcSpark npm wrapper was never published under that name. Use the GitHub clone path instead.
- Any guess like `mcp-server-coinglass` → not real. Use `GPSxtreme/mcp-coinglass` GitHub repo, no npm wrapper exists.

**Always verify before adding:**

```bash
# For npm:
npm view <pkg> bin     # check if it actually exists + correct entry
npm view <pkg>        # check unpackedSize, maintainer, dist-tags

# For GitHub-only Python:
gh repo view <owner>/<repo>  # check it exists and is maintained
```

**Three-step install policy:**

1. `npm view <pkg>` (or `gh repo view` for GitHub) — confirm package exists and find the real entry point
2. Manual smoke test — `timeout 15 <command>` and look for expected startup output
3. `hermes mcp add` — only after 1 and 2 succeed

## Newly verified free MCPs (Jun 2026 batch)

| Server | Tools | Install pattern | Notes |
|---|---|---|---|
| `brave-search` (official) | 8 | `npx -y @brave/brave-search-mcp-server --transport stdio` | Uses `BRAVE_API_KEY` from Bitwarden. Web, local, video, image, news, summarizer, LLM context, place search. |
| `playwright` (Microsoft) | 23 | `npx -y @playwright/mcp@latest` | Auto-downloads Chromium/Firefox/WebKit on first use (~250MB). browser_click, browser_snapshot, browser_take_screenshot, browser_tabs, browser_run_code_unsafe, etc. |
| `obsidian` (mauricio.wolff) | 14 | `npx -y @mauricio.wolff/mcp-obsidian@latest /path/to/vault` | Vault path is positional arg. Works with any folder of markdown files, no Obsidian plugin required. read/write/patch/list/search/move/frontmatter/tags/stats. |
| `pubmed` (cyanheads) | 10 | `npx -y @cyanheads/pubmed-mcp-server --transport stdio` | Full-text chain: NCBI PMC → Europe PMC → Unpaywall. 10 tools incl. MeSH lookup, citation formatter (APA/MLA/BibTeX/RIS), spell-check, related-article finder. **Slow startup (~5-10s after first install).** Set `NCBI_API_KEY` env to raise rate limit. |
| `openlibrary` (8enSmith) | 6 | Local clone + `node` wrapper (see broken-entry-point pitfall above) | npm `mcp-open-library` exists but the built entry-point exits silently — clone and wrap with `import().then(mod => new mod.OpenLibraryServer().run())`. Book/author/cover search. |

## Discord MCP server spamming pydantic errors — TUI events feed disconnects

**Symptom:** TUI dashboard shows "events feed disconnected", gateway logs flooded with `pydantic` validation errors (`TaskStatusNotification.params.createdAt`, `lastUpdatedAt`, `ttl` missing) every ~10 seconds.

**Root cause:** The **Discord MCP server** (`mcp-discord`) is a separate component from the **Discord chat bot plugin** (`hermes-discord`). The MCP server has no bot token configured (`hasToken:false`, `isReady:false`) and sends malformed MCP notifications that the gateway can't parse. This crashes the events pipeline.

**Key distinction:**
- `hermes-discord` plugin = Discord chat I/O (responds to messages). Works independently.
- `mcp-discord` MCP server = exposes Discord as MCP tools. Unrelated to chat bot function.

**Diagnosis:**
```bash
# Check for the spam pattern in logs
journalctl --user -u hermes-gateway --since "30 min ago" | grep "TaskStatusNotification"

# Check Discord MCP process state
ps aux | grep mcp-discord
```

**Fix (if you don't need Discord MCP tools):**
1. Kill stale MCP processes: `kill <pid>` for each `mcp-discord` process
2. Disable in config: edit `~/.hermes/config.yaml`, find the `discord:` MCP server entry, set `enabled: false`
3. Restart: `hermes gateway restart`

**Fix (if you need Discord MCP tools):**
Configure a Discord bot token for the MCP server so it can connect properly.

**Pitfall:** Don't assume Discord chat bot is broken when the TUI events feed disconnects — they are independent systems. Check which component is actually failing.

## Examples

### Time Server (uvx)

```yaml
mcp_servers:
  time:
    command: "uvx"
    args: ["mcp-server-time"]
```

Registers tools like `mcp_time_get_current_time`.

### Filesystem Server (npx)

```yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/documents"]
    timeout: 30
```

Registers tools like `mcp_filesystem_read_file`, `mcp_filesystem_write_file`, `mcp_filesystem_list_directory`.

### GitHub Server with Authentication

```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_xxxxxxxxxxxxxxxxxxxx"
    timeout: 60
```

Registers tools like `mcp_github_list_issues`, `mcp_github_create_pull_request`, etc.

**Safer local Hermes pattern when `gh auth` is already logged in:** avoid copying a GitHub token into `config.yaml`. Instead, use a tiny wrapper script that reads the token dynamically from GitHub CLI and then execs the MCP server.

```bash
#!/usr/bin/env bash
set -euo pipefail
export GITHUB_PERSONAL_ACCESS_TOKEN="$(gh auth token)"
exec npx -y @modelcontextprotocol/server-github
```

Then point `mcp_servers.github.command` at that script. This keeps the token out of `config.yaml` while still letting Hermes launch the server over stdio.

### Notion MCP Patterns

There are two practical Notion setup paths in Hermes:

1. **Official remote Notion MCP via OAuth**
   - URL: `https://mcp.notion.com/mcp`
   - config shape:

```yaml
mcp_servers:
  notion:
    url: "https://mcp.notion.com/mcp"
```

   - Good when the MCP client can complete the browser OAuth flow cleanly.
   - Practical pitfall: if the auth flow is started from `hermes mcp add ... --auth oauth` but the browser authorization is not completed in time, Hermes may save the server as disabled after a timeout. Re-test with `hermes mcp test notion` after completing auth.

2. **Local token-based Notion MCP**
   - Package: `@notionhq/notion-mcp-server`
   - Requires a Notion token such as `NOTION_TOKEN=ntn_...`
   - Good fallback when remote OAuth is awkward in the current environment.

**Important shell pitfall for token-based wrappers:** do **not** blindly `source` a large shared `.env` file just to get `NOTION_TOKEN`. Other env lines (for example secrets containing spaces) can break shell parsing and make the MCP server exit immediately. Prefer extracting only the needed variable and exporting it.

**Bitwarden env var preference pattern:** When Bitwarden Secrets Manager injects secrets as environment variables, wrapper scripts should check the env var first, then fall back to `.env` file:

```bash
#!/usr/bin/env bash
set -euo pipefail
# Prefer env var (injected by Bitwarden), fall back to .env file
if [[ -z "${NOTION_TOKEN:-}" ]]; then
  TOKEN=$(python3 - <<'PY'
from pathlib import Path
for line in Path('/path/to/.env').read_text().splitlines():
    if line.startswith('NOTION_TOKEN='):
        print(line.split('=',1)[1])
        break
else:
    raise SystemExit('NOTION_TOKEN not found in environment or /path/to/.env')
PY
  )
  export NOTION_TOKEN="$TOKEN"
fi
exec npx -y @notionhq/notion-mcp-server
```

This prevents silent failures when the env var is already set by Bitwarden but the script only reads from the file.

Example wrapper (original):

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

Then configure Hermes to run that wrapper as the stdio command.

See also `references/notion-and-github-mcp-hermes-patterns.md` for the concrete Hermes-oriented setup choices and pitfalls.

### Pitfall: `hermes mcp test notion` False Negatives

**Symptom:** `hermes mcp test notion` reports `✗ Connection failed (7285ms): Connection closed` even when the Notion MCP server is working correctly in chat.

**Root Cause:** The `mcp test` command only sends `initialize` and waits for a response. The Notion MCP server (`@notionhq/notion-mcp-server`) closes stdin if no `tools/list` request follows within ~7 seconds. This causes the test to fail, but the server is actually functional.

**Workaround:** Ignore the test failure. Always verify with a **real tool call in chat** (e.g., `mcp_notion_get_page`).

**Manual Verification:**
```bash
echo -e '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}\n{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}' | NOTION_TOKEN=ntn_*** npx -y @notionhq/notion-mcp-server --transport stdio
```

**Lesson:** `mcp test` is a diagnostic with a brittle handshake. Actual agent usage does the full handshake and works correctly.

### Pitfall: Page Not Shared with Integration

**Symptom:** `403 Forbidden` or `Connection not found` when calling Notion MCP tools (e.g., `mcp_notion_get_page`).

**Root Cause:** The Notion page/database is **not shared with your integration**. Notion requires explicit sharing for API access.

**Fix:**
1. Open the Notion page in your browser.
2. Click **Share** → **Invite a person** → Search for your integration name.
3. **Allow full access** (read/write).
4. Retry the tool call.

**Verification:**
```bash
# Check if the page is accessible via API
curl -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Notion-Version: 2022-06-28" \
  "https://api.notion.com/v1/pages/PAGE_ID"
```

If this returns `403`, the page is not shared with your integration.

- **Verification**: After setup, check if the server is running and tools are available:
  ```bash
  ps aux | grep notion
  hermes tools | grep mcp_notion
  ```
  If the server is configured but not running, **restart Hermes** (`hermes restart`).
  
- **False Test Results**: `hermes mcp test notion` may report `✗ Connection failed` even when the server is working. This is a known limitation of the test command for stdio servers like Notion. **Always verify with a real tool call in chat** (e.g., `mcp_notion_search`).

See also:
- `references/notion-mcp-hermes-setup.md` for detailed Notion MCP setup instructions.
- `references/notion-and-github-mcp-hermes-patterns.md` for broader MCP patterns.
- `references/notion-mcp-false-test-fix.md` for `hermes mcp test` false negative workarounds.
- `references/notion-mcp-page-sharing.md` for troubleshooting `403 Forbidden` errors.

### Remote HTTP Server

```yaml
mcp_servers:
  company_api:
    url: "https://mcp.mycompany.com/v1/mcp"
    headers:
      Authorization: "Bearer sk-xxxxxxxxxxxxxxxxxxxx"
      X-Team-Id: "engineering"
    timeout: 180
    connect_timeout: 30
```

### Multiple Servers

```yaml
mcp_servers:
  time:
    command: "uvx"
    args: ["mcp-server-time"]

  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]

  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_xxxxxxxxxxxxxxxxxxxx"

  company_api:
    url: "https://mcp.internal.company.com/mcp"
    headers:
      Authorization: "Bearer sk-xxxxxxxxxxxxxxxxxxxx"
    timeout: 300
```

All tools from all servers are registered and available simultaneously. Each server's tools are prefixed with its name to avoid collisions.

## Sampling (Server-Initiated LLM Requests)

Hermes supports MCP's `sampling/createMessage` capability — MCP servers can request LLM completions through the agent during tool execution. This enables agent-in-the-loop workflows (data analysis, content generation, decision-making).

Sampling is **enabled by default**. Configure per server:

```yaml
mcp_servers:
  my_server:
    command: "npx"
    args: ["-y", "my-mcp-server"]
    sampling:
      enabled: true           # default: true
      model: "gemini-3-flash" # model override (optional)
      max_tokens_cap: 4096    # max tokens per request
      timeout: 30             # LLM call timeout (seconds)
      max_rpm: 10             # max requests per minute
      allowed_models: []      # model whitelist (empty = all)
      max_tool_rounds: 5      # tool loop limit (0 = disable)
      log_level: "info"       # audit verbosity
```

Servers can also include `tools` in sampling requests for multi-turn tool-augmented workflows. The `max_tool_rounds` config prevents infinite tool loops. Per-server audit metrics (requests, errors, tokens, tool use count) are tracked via `get_mcp_status()`.

Disable sampling for untrusted servers with `sampling: { enabled: false }`.

## Tool Selection: Prefer MCP Tools Over Browser/Web Extraction

When a GitHub repository URL is provided (or any resource exposed by a configured MCP server), **use the MCP tools directly** instead of `browser_navigate`, `web_extract`, or `web_search`. The MCP tools hit the actual API with your authenticated credentials, return structured data, and avoid bot-detection/stealth issues.

**Example — GitHub repo given:**
- ❌ `browser_navigate("https://github.com/owner/repo")` + snapshot parsing
- ✅ `mcp_github_get_file_contents({owner, repo, path})` for files/dirs
- ✅ `mcp_github_search_repositories`, `mcp_github_search_code`, `mcp_github_list_commits`, etc.

This applies generally: if an MCP server exposes tools for a domain (filesystem, GitHub, Notion, crypto APIs, etc.), those tools are the primary interface. Browser/web tools are fallbacks for resources without MCP coverage.

## MCP server with a headless browser pool will leak unless cleaned up

If you are writing or modifying an MCP server that uses Selenium / Playwright / Puppeteer / WebDriver, the server **must** register `atexit` + signal handlers AND track the user-data-dir so it can be removed on close. Without this, each server restart orphans one chromedriver + ~8 chromium children + ~2 crashpad handlers (~250 MiB per pool browser), eventually starving a memory-constrained host into swap-thrashing.

Verified on the `tradingview-chart-mcp` server (June 2026): pre-patch `chromium: 96`, `chromedriver: 12`, `chrome_crashpad: 25`, free RAM 250 MiB, gateway unresponsive. After atexit + signal + user-data-dir tracking patch: `chromium: 12`, `chromedriver: 12`, `crashpad: 0`, free RAM 2.5 GiB.

Full pattern, working code template, and host-side detection checklist: `references/mcp-server-browser-pool-hygiene.md`.

For the live-host memory-pressure diagnostic that surfaces this kind of leak (system hangs, swap thrashing, gateway stops responding), see `devops/sagar-hermes-ops/references/mcp-browser-leak-diagnostic.md`.

## Notes

- MCP tools are called synchronously from the agent's perspective but run asynchronously on a dedicated background event loop
- Tool results are returned as JSON with either `{"result": "..."}` or `{"error": "..."}`
- The native MCP client is independent of `mcporter` -- you can use both simultaneously
- Server connections are persistent and shared across all conversations in the same agent process
- Adding or removing servers requires restarting the agent (no hot-reload currently)
