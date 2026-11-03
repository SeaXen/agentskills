---
name: hermes-agent
description: "Configure, extend, or contribute to Hermes Agent."
version: 2.1.0
author: Hermes Agent + Teknium
license: MIT
metadata:
  hermes:
    tags: [hermes, setup, configuration, multi-agent, spawning, cli, gateway, development]
    homepage: https://github.com/NousResearch/hermes-agent
    related_skills: [claude-code, codex, opencode]
---

# Hermes Agent

Hermes Agent is an open-source AI agent framework by Nous Research that runs in your terminal, messaging platforms, and IDEs. It belongs to the same category as Claude Code (Anthropic), Codex (OpenAI), and OpenClaw — autonomous coding and task-execution agents that use tool calling to interact with your system. Hermes works with any LLM provider (OpenRouter, Anthropic, OpenAI, DeepSeek, local models, and 15+ others) and runs on Linux, macOS, and WSL.

What makes Hermes different:

- **Self-improving through skills** — Hermes learns from experience by saving reusable procedures as skills. When it solves a complex problem, discovers a workflow, or gets corrected, it can persist that knowledge as a skill document that loads into future sessions. Skills accumulate over time, making the agent better at your specific tasks and environment.
- **Persistent memory across sessions** — remembers who you are, your preferences, environment details, and lessons learned. Pluggable memory backends (built-in, Honcho, Mem0, and more) let you choose how memory works.
- **Multi-platform gateway** — the same agent runs on Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Email, and 10+ other platforms with full tool access, not just chat.
- **Provider-agnostic** — swap models and providers mid-workflow without changing anything else. Credential pools rotate across multiple API keys automatically.
- **Profiles** — run multiple independent Hermes instances with isolated configs, sessions, skills, and memory.
- **Extensible** — plugins, MCP servers, custom tools, webhook triggers, cron scheduling, and the full Python ecosystem.

People use Hermes for software development, research, system administration, data analysis, content creation, home automation, and anything else that benefits from an AI agent with persistent context and full system access.

**This skill helps you work with Hermes Agent effectively** — setting it up, configuring features, spawning additional agent instances, troubleshooting issues, finding the right commands and settings, and understanding how the system works when you need to extend or contribute to it.

**Docs:** https://hermes-agent.nousresearch.com/docs/

## Quick Start

```bash
# Install
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Interactive chat (default)
hermes

# Single query
hermes chat -q "What is the capital of France?"

# Setup wizard
hermes setup

# Change model/provider
hermes model

# Check health
hermes doctor
```

---

## CLI Reference

### Global Flags

```
hermes [flags] [command]

  --version, -V             Show version
  --resume, -r SESSION      Resume session by ID or title
  --continue, -c [NAME]     Resume by name, or most recent session
  --worktree, -w            Isolated git worktree mode (parallel agents)
  --skills, -s SKILL        Preload skills (comma-separate or repeat)
  --profile, -p NAME        Use a named profile
  --yolo                    Skip dangerous command approval
  --pass-session-id         Include session ID in system prompt
```

No subcommand defaults to `chat`.

### Chat

```
hermes chat [flags]
  -q, --query TEXT          Single query, non-interactive
  -m, --model MODEL         Model (e.g. anthropic/claude-sonnet-4)
  -t, --toolsets LIST       Comma-separated toolsets
  --provider PROVIDER       Force provider (openrouter, anthropic, nous, etc.)
  -v, --verbose             Verbose output
  -Q, --quiet               Suppress banner, spinner, tool previews
  --checkpoints             Enable filesystem checkpoints (/rollback)
  --source TAG              Session source tag (default: cli)
```

### Configuration

```
hermes setup [section]      Interactive wizard (model|terminal|gateway|tools|agent)
hermes model                Interactive model/provider picker
hermes config               View current config
hermes config edit          Open config.yaml in $EDITOR
hermes config set KEY VAL   Set a config value
hermes config path          Print config.yaml path
hermes config env-path      Print .env path
hermes config check         Check for missing/outdated config
hermes config migrate       Update config with new options
hermes login [--provider P] OAuth login (nous, openai-codex)
hermes logout               Clear stored auth
hermes doctor [--fix]       Check dependencies and config
hermes status [--all]       Show component status
```

### Model Configuration — Critical Concepts

#### model_catalog.providers vs model_aliases

Two separate mechanisms control model visibility, but the important OpenRouter pitfall is that **`model_catalog.providers.<provider>` is a provider-override URL hook, not an inline `models:` override**.

| Mechanism | What it does | Affects picker? |
|-----------|--------------|-----------------|
| `model_catalog.providers.<provider>.url` | Replaces the remote curated catalog for that provider with a full manifest fetched from that URL | **Yes** — dashboard + CLI picker |
| `model_aliases` | Adds shortcut names for direct selection / CLI switching | **Not by itself** — useful for direct use, but does not populate the dashboard picker |

When curating OpenRouter models, do **not** assume `providers.openrouter.models:` inline YAML will drive Hermes picker behavior. In Hermes, the effective override path is a provider-specific manifest URL.

#### Filtering picker to free-only or curated OpenRouter models

Use a custom manifest file and point the OpenRouter provider override at it:

```yaml
model_catalog:
  enabled: true
  url: https://hermes-agent.nousresearch.com/docs/api/model-catalog.json
  ttl_hours: 24
  providers:
    openrouter:
      url: file:///root/.hermes/cache/free_openrouter_catalog.json
```

Then create `free_openrouter_catalog.json` as a full catalog manifest containing only the OpenRouter models you want Hermes to consider.

Important behavior:
- The OpenRouter picker still applies a **final live filter** against `https://openrouter.ai/api/v1/models`
- A model can exist on an OpenRouter webpage yet still be hidden in Hermes if it is absent from the live models API or fails Hermes tool-capability checks
- This especially affects preview / `:free` models that get deprecated or temporarily removed

#### Adding CLI aliases for quick switching

```yaml
model_aliases:
  or-owl-alpha:
    model: openrouter/owl-alpha
    provider: openrouter
  or-nemotron-3-super:
    model: nvidia/nemotron-3-super-120b-a12b:free
    provider: openrouter
  or-ring-26:
    model: inclusionai/ring-2.6-1t:free
    provider: openrouter
```

These aliases work with `hermes chat -m or-owl-alpha -q "hello"` but do NOT affect the dashboard picker.

#### Free OpenRouter Models Reference

See `references/openrouter-free-models-2026.md` for a curated list of the best free OpenRouter models with context windows, strengths, and important caveats about data logging and rate limits.

### Tools & Skills

```
hermes tools                Interactive tool enable/disable (curses UI)
hermes tools list           Show all tools and status
hermes tools enable NAME    Enable a toolset
hermes tools disable NAME   Disable a toolset

hermes skills list          List installed skills
hermes skills search QUERY  Search the skills hub
hermes skills install ID    Install a skill (ID can be a hub identifier OR a direct https://…/SKILL.md URL; pass --name to override when frontmatter has no name)
hermes skills inspect ID    Preview without installing

Automation/install pitfall: `hermes skills install ...` is interactive by default and prompts `Confirm [y/N]:` even for official/builtin skills. In non-interactive terminal automation, pipe confirmation explicitly, e.g.:
```bash
printf 'y\n' | hermes skills install official/blockchain/solana
```
Use this when the user has already asked you to install a skill and the action is within scope.

Identifier/source pitfall: search results can be slightly confusing about source naming and accepted identifiers. Practical rules:
- `hermes skills search <query>` is good for discovery, but the rendered table may truncate or simplify identifiers.
- `hermes skills inspect <name>` often resolves short names (for example `hyperliquid`, `stocks`, `solana`, `base`) to the full hub identifier.
- Some community items may inspect successfully with a qualified prefix like `clawhub/<id>` even if the search table only shows a short identifier.
- Always inspect first before installing if source/trust matters.

Third-party agent repos often bundle multiple integration styles side-by-side (for example Claude/Codex hooks, AGENTS.md files, IDE rule files, and standalone SKILL.md files). For Hermes, prefer installing the raw `SKILL.md` directly rather than trying to reuse agent-specific plugin installers or hook configs. Example:
```bash
hermes skills install https://raw.githubusercontent.com/<owner>/<repo>/<branch>/path/to/SKILL.md
```
Use the skill content in Hermes; do not assume Claude Code plugins, Codex hooks, slash-command wiring, or MCP glue from that repo will carry over unchanged.
hermes skills config        Enable/disable skills per platform
hermes skills check         Check for updates
hermes skills update        Update outdated skills
hermes skills uninstall N   Remove a hub skill
hermes skills publish PATH  Publish to registry
hermes skills browse        Browse all available skills
hermes skills tap add REPO  Add a GitHub repo as skill source
```

### MCP Servers

```
hermes mcp serve            Run Hermes as an MCP server
hermes mcp add NAME         Add an MCP server (--url or --command)
hermes mcp remove NAME      Remove an MCP server
hermes mcp list             List configured servers
hermes mcp test NAME        Test connection
hermes mcp configure NAME   Toggle tool selection
```

#### HTTP MCP auth pitfall: OAuth MCP vs provider API keys

When a user gives you both:
- an MCP setup URL / `hermes mcp add ... --auth oauth` instruction, and
- a provider API key like `sk-...`

Do **not** assume the API key can authenticate the MCP transport itself.

Practical diagnostic pattern:
1. Add/test the server with the auth mode the provider documents for MCP (`oauth` vs `header`).
2. If the connection times out or stays disabled, probe the MCP endpoint headers and auth challenge.
3. Treat `WWW-Authenticate: Bearer resource=...` plus errors like `Unauthorized: Valid OAuth Bearer token required` as proof that the MCP endpoint wants an **OAuth bearer token**, not the provider's ordinary API key.
4. Do not tell the user the API key is enough for MCP just because their Search/Fetch REST APIs accept it.

Observed durable pattern:
- Some vendors expose free/paid REST APIs with `sk-...` keys, while their `/mcp` endpoint separately requires OAuth PKCE login.
- In Hermes, `hermes mcp add <name> --url <endpoint> --auth oauth` may save the server as **disabled** after a connection timeout if OAuth was not completed successfully yet. That is a configuration/auth completion issue, not proof the server is unsupported.
- If the CLI offers `Save config anyway (you can test later)?`, saving is reasonable; then re-run `hermes mcp test <name>` after completing OAuth.

If you need concrete example details, see `references/tinyfish-mcp-oauth-vs-api-key.md`.

### Gateway (Messaging Platforms)

```
hermes gateway run          Start gateway foreground
hermes gateway install      Install as background service
hermes gateway start/stop   Control the service
hermes gateway restart      Restart the service
hermes gateway status       Check status
hermes gateway setup        Configure platforms
```

Supported platforms: Telegram, Discord, Slack, WhatsApp, Signal, Email, SMS, Matrix, Mattermost, Home Assistant, DingTalk, Feishu, WeCom, BlueBubbles (iMessage), Weixin (WeChat), API Server, Webhooks. Open WebUI connects via the API Server adapter.

Platform docs: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/

### Sessions

```
hermes sessions list        List recent sessions
hermes sessions browse      Interactive picker
hermes sessions export OUT  Export to JSONL
hermes sessions rename ID T Rename a session
hermes sessions delete ID   Delete a session
hermes sessions prune       Clean up old sessions (--older-than N days)
hermes sessions stats       Session store statistics
```

### Cron Jobs

```
hermes cron list            List jobs (--all for disabled)
hermes cron create SCHED    Create: '30m', 'every 2h', '0 9 * * *'
hermes cron edit ID         Edit schedule, prompt, delivery
hermes cron pause/resume ID Control job state
hermes cron run ID          Trigger on next tick
hermes cron remove ID       Delete a job
hermes cron status          Scheduler status
```

#### Cron Scheduling — Fixed Clock Times vs Intervals

When the user wants alerts at specific Dhaka/local times (e.g. 12am, 6am, 12pm, 6pm), always use fixed cron expressions — never interval-based schedules that drift:

```yaml
# ✅ Fixed — fires at exact local times (honors config timezone)
schedule: "0 0,6,12,18 * * *"    # 12am, 6am, 12pm, 6pm every day
schedule: "0 6,18 * * *"          # 6am and 6pm only
schedule: "0 9 * * 1-5"            # 9am weekdays only

# ❌ Avoid — drifts relative to wall clock, user sees "random" times
schedule: "every 360m"             # every 6h from creation time, not aligned to clock
schedule: "every 6h"                # same problem
```

**Rule of thumb:**
- User says "at 6am / at noon / at specific times" → cron expression with fixed hours
- User says "every N hours / check frequently" → interval is fine
- When in doubt, ask — but default to fixed clock times for user-facing alerts

This is especially important when `timezone` is set (e.g. `Asia/Dhaka`), because the user expects "6am" to mean 6am *their* time, not 6am UTC offset by when the job was created.

#### Delivery semantics that matter in practice

When inspecting or updating cron jobs, check the effective `deliver` target instead of assuming alerts go to the current home channel.

- `origin` = deliver back to the exact conversation/topic/thread where the job was created
- `telegram` / `discord` = deliver to that platform's configured home channel
- `telegram:chat_id:thread_id` = deliver to a specific Telegram topic/thread
- comma-separated targets are allowed, for example `telegram,discord` or `origin,telegram,discord`

Practical pitfall: if a user says "send cron alerts to my home thread/channel" and the job currently uses `origin`, that is a config mismatch, not a cron limitation. Update the job's `deliver` field explicitly.

#### no_agent watchdog / watcher formatting

For recurring script-based watcher jobs (`script=...`, `no_agent=True`), prefer human-scannable alert output:

- first print a compact **Summary** block with the key account/status numbers
- then print a **Details** block with changed items and explanatory lines
- keep the most important numbers visible at a glance in home-channel notifications
- continue using the watchdog pattern where empty stdout means silent/no notification

This format works especially well for billing/usage/model-watch jobs where the user mainly wants a fast dashboard-style glance, but still needs details when something changed.

### Webhooks

```
hermes webhook subscribe N  Create route at /webhooks/<name>
hermes webhook list         List subscriptions
hermes webhook remove NAME  Remove a subscription
hermes webhook test NAME    Send a test POST
```

### Profiles

```
hermes profile list         List all profiles
hermes profile create NAME  Create (--clone, --clone-all, --clone-from)
hermes profile use NAME     Set sticky default
hermes profile delete NAME  Delete a profile
hermes profile show NAME    Show details
hermes profile alias NAME   Manage wrapper scripts
hermes profile rename A B   Rename a profile
hermes profile export NAME  Export to tar.gz
hermes profile import FILE  Import from archive
```

### Credential Pools

```
hermes auth add               Interactive credential wizard
hermes auth list [PROVIDER]   List pooled credentials
hermes auth remove P INDEX    Remove by provider + index
hermes auth disable P TARGET  Disable a credential (hold without removing)
hermes auth enable P TARGET   Re-enable a disabled credential
hermes auth reset PROVIDER    Clear exhaustion status
```

- `disable` / `enable` accept **index, entry ID, or exact label** (same as `remove`)
- Disabled entries show `[DISABLED]` in `hermes auth list`
- Disabled entries are skipped by **all rotation strategies** (`fill_first`, `round_robin`, `least_used`, `random`)
- Interactive `hermes auth` menu now includes "Disable a credential" and "Enable a credential" options
- Useful for temporarily holding a credential out of rotation without deleting it (e.g., Codex OAuth quota issues)

#### OpenAI Codex pooled-auth behavior that matters in practice

When a user adds multiple `openai-codex` OAuth logins inside the **same profile**, Hermes treats them as a **credential pool**, not a manual account picker.

What the user will see in `hermes auth list openai-codex`:
- `#N` = pool position
- `←` = the credential currently selected / active
- `rate-limited usage_limit_reached (429) (...)` = that credential is temporarily exhausted and Hermes rotated away from it

Important behavior:
- there is currently **no dedicated `hermes auth use|switch|select` command** for manually choosing `codex3` or another pooled Codex login inside the same profile
- `hermes auth remove` accepts **index, entry id, or exact label**; the help text is broader than the older "index only" mental model
- adding `--label codex1` to `hermes auth add ...` usually creates a **new labeled entry**; it does **not** rename an existing unlabeled pooled credential
- if session continuity matters, keep one profile and multiple pooled Codex logins; separate profiles make manual auth switching easier but break natural continuation of the same session because sessions are profile-scoped

Rotation / recovery behavior:
- default pool strategy is **`fill_first`** = use the first healthy credential until it is exhausted, then rotate to the next healthy one
- after a 429 credential's cooldown or provider reset window passes, Hermes auto-clears the exhausted state and that earlier entry becomes eligible again
- practical consequence: if `#1` was exhausted, Hermes moved to `#2`, and later `#2` exhausts after `#1` has recovered, Hermes will usually return to **`#1`** under the default strategy
- provider-supplied reset times override generic cooldowns, so a Codex entry may show a long wait like `1d 17h left`; do not assume all 429s recover in an hour

If the user wants load spread across multiple Codex accounts instead of hammering the first healthy one, set:
```bash
hermes config set credential_pool_strategies.openai-codex round_robin
```
Then restart Hermes / start a new session so the new strategy is used.

Strategy cheat sheet:
- `fill_first` — use first healthy credential until capped, then next
- `round_robin` — rotate across healthy credentials more evenly
- `least_used` — choose the least-used healthy credential
- `random` — random healthy credential

Best recommendation split:
- **same session continuity** wanted → one profile + pooled Codex auths
- **manual exact account selection** wanted → separate profiles per Codex login

### Other

```
hermes insights [--days N]  Usage analytics
hermes update               Update to latest version
hermes pairing list/approve/revoke  DM authorization
hermes plugins list/install/remove  Plugin management
hermes honcho setup/status  Honcho memory integration (requires honcho plugin)
hermes memory setup/status/off  Memory provider config
hermes completion bash|zsh  Shell completions
hermes acp                  ACP server (IDE integration)
hermes claw migrate         Migrate from OpenClaw
hermes uninstall            Uninstall Hermes
```

---

## Model Catalog Deep Dive

### How the picker works

The `/model` picker (CLI) and dashboard model selector pull from:
1. The **remote model catalog** fetched from `model_catalog.url`
2. Any **local override** in `model_catalog.providers` (if non-empty, replaces the remote catalog for that provider)
3. `custom_providers` entries in config.yaml
4. `model_aliases` entries (CLI only)

### Override the remote catalog to filter models

The remote catalog at `https://hermes-agent.nousresearch.com/docs/api/model-catalog.json` contains both paid and free models. Setting `model_catalog.providers.openrouter.models` to a curated list **replaces** the OpenRouter section entirely:

```yaml
model_catalog:
  providers:
    openrouter:
      models:
        - id: openrouter/owl-alpha
          description: free — agentic
        # ... only these models appear
```

This is the **only** way to hide paid models from the picker. `model_aliases` alone does NOT filter the dashboard.

### Adding models — always do both

```yaml
# 1. Add to catalog (controls picker visibility)
model_catalog:
  providers:
    openrouter:
      models:
        - id: inclusionai/ring-2.6-1t:free
          description: free — 1T params, agentic

# 2. Add alias (for convenient CLI switching)
model_aliases:
  or-ring-26:
    model: inclusionai/ring-2.6-1t:free
    provider: openrouter
```

### Free models reference
- Dashboard vs CLI model-list mismatch: compare the exact serving path, not just config files. There are two distinct layers:

---

## Plugin Sourcing and Install

Hermes plugins are **not limited to the bundled set** shown by `hermes plugins list`. The CLI help confirms:

```bash
hermes plugins install <git-url-or-owner/repo>
```

So when a user asks where to get more plugins, check GitHub/community repos in addition to the built-ins.

Practical guidance:
- **Bundled plugins** come with Hermes and show up in `hermes plugins list`
- **Community plugins** are commonly distributed as GitHub repos and installed with either:
  - `hermes plugins install owner/repo`
  - `hermes plugins install https://github.com/owner/repo.git`
- There does **not** appear to be a broad centralized plugin registry comparable to the skills hub; GitHub is the main discovery surface right now

Safety / quality review before recommending install:
1. Check the repo was updated recently
2. Check for `plugin.yaml` and `__init__.py` at the plugin root (or in each plugin subdir for collections)
3. Prefer repos with README/docs and ideally tests
4. Read install instructions — some repos are a **collection** of plugins and require manual copy into `~/.hermes/plugins/`
5. Tell the user plainly when a repo looks more like an extension/dashboard/integration than a standard drop-in plugin

### Community plugin triage

When a user asks about recommended plugins or says "some may already be installed," do **not** jump straight to installation. First inspect the live system:

```bash
hermes plugins list
find ~/.hermes/plugins -maxdepth 2 -name plugin.yaml
```

Then classify each plugin by **practical usefulness without new credentials**, not just whether it installs.

| Plugin | Needs API key? | Notes |
|--------|---------------|-------|
| `hermes-memory-ui` | No | Dashboard for memory backends — works immediately |
| `icarus` | No (basic) | Fabric memory/recall — training/eval needs TOGETHER_API_KEY |
| `hermes_otel` | Maybe | Needs tracing backend (Langfuse, Phoenix, etc.) |
| `web-search-plus` | Yes | Needs at least one search provider key (Tavily free tier available) |

---

## Dashboard

```bash
hermes dashboard            # Start on localhost:9119
hermes dashboard --tui      # Enable embedded in-browser Chat tab at /chat
hermes dashboard --host 0.0.0.0 --port 9119 --insecure  # Expose to network (NAS mode)
hermes dashboard --stop     # Stop all dashboard processes
hermes dashboard --status   # Check status
```

### Enabling the dashboard Chat tab

Version caveat: first run `hermes dashboard --help`. Some installed builds (observed v0.15.1 / 2026.5.29) **do not accept dashboard-local `--tui`**; adding it after `dashboard` causes a reboot crash loop with `hermes: error: unrecognized arguments: --tui`. In those builds, start the dashboard without `--tui`:

```bash
hermes dashboard --host 0.0.0.0 --port 9120 --insecure --skip-build --no-open
```

If `hermes dashboard --help` explicitly shows a dashboard `--tui` option, then use it for the embedded Chat tab:

```bash
hermes dashboard --host 127.0.0.1 --port 9120 --insecure --tui --no-open
```

Practical verification:
- `hermes dashboard --help` must show `--tui` before putting `--tui` in a systemd unit
- `systemctl status hermes-dashboard.service` should be `active (running)`, not `activating (auto-restart)`
- `ss -ltnp | grep 9120` should show `0.0.0.0:9120`
- opening `/chat` should render the Chat page, not just the generic dashboard shell
- if the page was already open before restart, do a hard refresh

Important pitfall: a dashboard service file with stale `--tui` on a build that no longer supports it will repeatedly exit with status 2 after reboot and port 9120 will never bind.

**Important security note:** the dashboard does **not** provide a built-in browser login page / username-password prompt. If you bind it to `0.0.0.0` with `--insecure`, anyone on the reachable network can open the page unless you add an external access control layer.

Recommended protections when exposing on LAN/NAS:
- **Best:** keep Hermes on `127.0.0.1` and put it behind a reverse proxy with Basic Auth / access control
- **Also set an API key** for the API Server (`API_SERVER_KEY`) so backend API access is authenticated
- **Do not assume** `API_SERVER_KEY` creates a dashboard login form — it protects API access, not the initial browser page load

**Common LAN access pitfall:** if `http://<internal-ip>:<port>/` does not open but `http://127.0.0.1:<port>/` works on the host machine, the dashboard is usually bound only to localhost. Diagnose with:
```bash
hermes dashboard --status
ss -ltnp | grep 9120
hostname -I
```
If the listener shows `127.0.0.1:<port>` instead of `0.0.0.0:<port>`, restart it bound to all interfaces:
```bash
hermes dashboard --stop
hermes dashboard --host 0.0.0.0 --port 9120 --insecure
```
Then verify both the listener and the LAN URL:
```bash
ss -ltnp | grep 9120
# expect 0.0.0.0:9120
```
Open:
```text
http://<internal-ip>:9120/
http://<internal-ip>:9120/mission-control
```
If it is still unreachable after rebinding, check the host/NAS firewall and confirm the client device is on the same LAN.

**Embedded dashboard chat has an extra requirement:** `/chat` only works when the dashboard process itself was started with `--tui` (or `HERMES_DASHBOARD_TUI=1`). A common failure mode is that the operator enables `--tui`, but an older non-TUI `hermes dashboard` process is still the one actually bound to the port, so `/chat` loads the shell/UI but the event feed disconnects and tool calls never appear. Verify the live listener, not just the command you intended to run:
```bash
hermes dashboard --help | sed -n '1,80p'   # confirm --tui exists in this build
hermes dashboard --status
ss -ltnp | grep 9120
ps -ef | grep '[h]ermes dashboard'
```
Healthy shape for a LAN/TUI dashboard:
```text
0.0.0.0:9120  -> hermes dashboard --host 0.0.0.0 --port 9120 --insecure --tui
```
If another dashboard process is holding the port, stop all dashboard processes first, then relaunch the intended one.

**Static-file app proxy pitfall:** Do NOT add static file apps (like Graphify's `graph.html`) as location blocks inside the Hermes dashboard nginx config. Hermes is a SPA — adding proxy_pass for static files under the same server block breaks SPA routing and causes infinite loading. Keep static-file apps on **separate ports** (e.g., Graphify on 8081) or use a **separate nginx server block** with its own port. If you need a unified entry point, create a simple HTML landing page on a new port (e.g., 9090) that links to all apps, or use nginx path-based routing in a **separate server block** that doesn't interfere with Hermes.

**Connecting Hermes Desktop to a remote gateway:** The Desktop app connects to the **Gateway** (WebSocket `/api/ws`, REST `/api/...`), not the Dashboard. Configure via `HERMES_GATEWAY_URL` env var or `gateway.url` in config.yaml. The Desktop app has no built-in Basic Auth UI for the gateway URL — prefer Tailscale/VPN/SSH tunnel for gateway port (9119) and keep 401 auth only on the Dashboard port (9120). See `references/hermes-desktop-remote-gateway.md` for the full pattern.

**Nginx reverse proxy for multiple apps:** When setting up nginx reverse proxy for multiple apps, keep each app on its own port or separate server block. Do NOT mix static file serving with Hermes SPA proxy in the same server block. Use path-based routing only when apps are truly independent (e.g., `/graphify` → port 8081, `/app` → port 8080) and the Hermes dashboard has its own dedicated server block. In practice the raw Hermes app on `:9120` may work while the proxy path does not. When debugging, always compare both surfaces:

**Static-file app proxy pitfall:** Do NOT add static file apps (like Graphify's `graph.html`) as location blocks inside the Hermes dashboard nginx config. Hermes is a SPA — adding proxy_pass for static files under the same server block breaks SPA routing and causes infinite loading. Keep static-file apps on **separate ports** (e.g., Graphify on 8081) or use a **separate nginx server block** with its own port. If you need a unified entry point, create a simple HTML landing page on a new port (e.g., 9090) that links to all apps, or use nginx path-based routing in a **separate server block** that doesn't interfere with Hermes.
```bash
ss -ltnp | grep -E ':(9119|9120) '
python3 - <<'PY'
import urllib.request
for url in ['http://127.0.0.1:9119/','http://127.0.0.1:9119/chat','http://127.0.0.1:9120/','http://127.0.0.1:9120/chat']:
    try:
        with urllib.request.urlopen(url, timeout=8) as r:
            print(url, r.status, r.getheader('content-type'))
    except Exception as e:
        print(url, type(e).__name__, e)
PY
```
If `9119` is an nginx auth proxy in front of `9120`, prefer these proxy settings for chat stability:
```nginx
location / {
    proxy_pass http://127.0.0.1:9120;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_cache_bypass $http_upgrade;
    proxy_buffering off;
    proxy_request_buffering off;
    proxy_read_timeout 86400;
    proxy_send_timeout 86400;
}
```
Then `nginx -t && nginx -s reload`, hard-refresh the browser, and test `/chat` again on both the raw app port and the proxied/auth port.

**Persistence (Server/NAS Setup):**
To keep the dashboard running after terminal close or reboot, use a systemd service. See `templates/hermes-dashboard.service` for a starter config.

### Two-port dashboard pattern: reverse proxy vs raw Hermes app

On NAS/LAN setups it is common to see **two dashboard ports** and think Hermes started twice. Usually they are different layers:

- one port is a **reverse proxy** (often Nginx/Caddy) adding auth or routing
- the other port is the **raw Hermes dashboard server** started by `hermes dashboard`

Example diagnostic shape:
- `9119` served by `nginx` and returns `401 Unauthorized`
- `9120` served by `hermes` and returns `200`

Verification pattern:
```bash
hermes dashboard --status
ss -ltnp | grep -E ':(9119|9120) '
python3 - <<'PY'
import urllib.request
for url in ['http://127.0.0.1:9119/','http://127.0.0.1:9120/']:
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            print(url, r.status)
    except Exception as e:
        print(url, type(e).__name__, e)
PY
```

Interpretation:
- if the proxy port returns `401`, that is usually the protected/public entrypoint
- if the Hermes port returns `200`, that is the direct app server
- do not tell the user the ports are duplicates until you confirm which process owns each socket

### Building a separate companion dashboard beside the built-in one

When the user wants a **premium / compact / beautiful dashboard alongside the built-in Hermes dashboard**, prefer a **dashboard plugin MVP** before patching core pages.

Why this is the default:
- keeps the built-in dashboard intact
- gives the user a separate control-center surface quickly
- reuses Hermes dashboard auth/session handling and built-in REST endpoints
- is easier to iterate on visually without risking core dashboard regressions

Recommended first MVP:
- show **session IDs** prominently
- add `Resume in Chat` links using `/chat?resume=<session_id>`
- add `Copy CLI` / command affordances using `hermes --resume <session_id>`
- surface current model/provider/context
- summarize enabled skills, toolsets, profiles, and cron jobs
- keep the first version mostly read-only; add mutations later

Implementation shape:
- create `plugins/<name>/dashboard/manifest.json`
- create `plugins/<name>/dashboard/dist/index.js`
- optionally create `plugins/<name>/dashboard/dist/style.css`
- use `window.__HERMES_PLUGIN_SDK__` and `window.__HERMES_PLUGINS__.register(...)`
- prefer `SDK.api.getStatus()`, `getModelInfo()`, `getSessions()`, `getSkills()`, `getToolsets()`, `getProfiles()`, `getCronJobs()` instead of inventing new endpoints when existing ones already cover the dashboard card data

Verification pattern:
- rescan plugins via `/api/dashboard/plugins/rescan`
- verify the plugin appears in sidebar navigation
- verify the direct route loads (for example `/mission-control`)
- add a smoke test asserting manifest fields, page registration, and the presence of resume affordances (`/chat?resume=` and `hermes --resume `)

Phase 2 default after the MVP:
- add a **selected-session detail panel** instead of immediately mutating core Hermes pages
- load transcript preview with `SDK.api.getSessionMessages(sessionId)` when the selected session changes
- add client-side **source filters** (`All sources`, Telegram/Discord/CLI/etc.) and sort controls (`Newest`, `Most messages`, `Most tools`)
- persist lightweight priorities like pinned sessions in browser storage before designing server-side persistence
- keep actions simple first: `Resume in Chat`, `Copy CLI`, `Open Sessions`

## Slash Commands (In-Session)

Type these during an interactive chat session.

### Session Control
```
/new (/reset)        Fresh session
/clear               Clear screen + new session (CLI-only)
/retry               Resend last message
/undo                Remove last exchange
/title [name]        Name the session
/compress            Manually compress context
/stop                Kill background processes
/rollback [N]        Restore filesystem checkpoint
/background <prompt> Run prompt in background
/queue <prompt>      Queue for next turn
/resume [name]       Resume a named session
/handoff <platform>  Transfer session to a messaging platform (CLI-only)
```

### Configuration
```
/config              Show config (CLI-only)
/model [name]        Show or change model
/personality [name]  Set personality
/reasoning [level]   Set reasoning (none|minimal|low|medium|high|xhigh|show|hide)
/verbose             Cycle: off → new → all → verbose (CLI-only)
/voice [on|off|tts]  Voice mode
/yolo                Toggle approval bypass
/skin [name]         Change theme (CLI-only)
/statusbar           Toggle status bar (CLI-only)
```

### Tools & Skills
```
/tools               Manage tools (CLI)
/toolsets            List toolsets (CLI)
/skills              Search/install skills (CLI)
/skill <name>        Load a skill into session
/cron                Manage cron jobs (CLI)
/reload-mcp          Reload MCP servers
/plugins             List plugins (CLI)
```

### Gateway
```
/approve             Approve a pending command (gateway)
/deny                Deny a pending command (gateway)
/restart             Restart gateway (gateway)
/sethome             Set current chat as home channel (gateway)
/update              Update Hermes to latest (gateway)
/platforms (/gateway) Show platform connection status (gateway)
```

### Utility
```
/branch (/fork)      Branch the current session
/fast                Toggle priority/fast processing
/browser             Open CDP browser connection
/history             Show conversation history (CLI)
/save                Save conversation to file (CLI)
/paste               Attach clipboard image (CLI)
/image               Attach local image file (CLI)
```

### Info
```
/help                Show commands
/commands [page]     Browse all commands (gateway)
/usage               Token usage
/insights [days]     Usage analytics
/status              Session info (gateway)
/profile             Active profile info
```

### Exit
```
/quit (/exit, /q)    Exit CLI
```

---

## Key Paths & Config

```
~/.hermes/config.yaml       Main configuration
~/.hermes/.env              API keys and secrets
$HERMES_HOME/skills/        Installed skills
~/.hermes/sessions/         Session transcripts
~/.hermes/logs/             Gateway and error logs
~/.hermes/auth.json         OAuth tokens and credential pools
~/.hermes/hermes-agent/     Source code (if git-installed)
```

Profiles use `~/.hermes/profiles/<name>/` with the same layout.

### Config Sections

Edit with `hermes config edit` or `hermes config set section.key value`.

| Section | Key options |
|---------|-------------|
| `model` | `default`, `provider`, `base_url`, `api_key`, `context_length` |
| `model_catalog` | `enabled`, `url`, `ttl_hours`, `providers` — controls picker visibility |
| `agent` | `max_turns` (90), `tool_use_enforcement` |
| `terminal` | `backend` (local/docker/ssh/modal), `cwd`, `timeout` (180) |
| `compression` | `enabled`, `threshold` (0.50), `target_ratio` (0.20) |
| `display` | `skin`, `tool_progress`, `show_reasoning`, `show_cost` |
| `stt` | `enabled`, `provider` (local/groq/openai/mistral) |
| `tts` | `provider` (edge/elevenlabs/openai/minimax/mistral/neutts) |
| `memory` | `memory_enabled`, `user_profile_enabled`, `provider` |
| `security` | `tirith_enabled`, `website_blocklist` |
| `delegation` | `model`, `provider`, `base_url`, `api_key`, `max_iterations` (50), `reasoning_effort` |
| `checkpoints` | `enabled`, `max_snapshots` (50) |

Full config reference: https://hermes-agent.nousresearch.com/docs/user-guide/configuration

### Checkpoints

While checkpoints provide a convenient rollback mechanism, they can consume significant disk space if not managed properly—each snapshot stores copies of every file modified by Hermes tools during the session. In space-constrained environments (e.g., limited `/mnt/tb/hermes` storage), consider these best practices:

- **Limit snapshot count**: Set `checkpoints.max_snapshots` to a low value (e.g., 3 or 5) to keep only the most recent snapshots.
- **Enable auto-pruning**: Turn on `checkpoints.auto_prune: true` so old snapshots are automatically deleted when the limit is reached.
- **Shorten retention**: Reduce `checkpoints.retention_days` (e.g., to 1 or 2) to expire snapshots based on age.
- **Temporarily disable**: For sessions involving large file edits (e.g., importing big medical notes), start Hermes with `--no-checkpoints` or disable the feature in config to avoid unnecessary snapshots.
- **Monitor usage**: Periodically check `~/.hermes/checkpoints/` size with `du -sh ~/.hermes/checkpoints/` and clean manually if needed.

These adjustments let you retain a safety net for small edits while keeping disk usage predictable.

### Providers

20+ providers supported. Set via `hermes model` or `hermes setup`.

| Provider | Auth | Key env var |
|----------|------|-------------|
| OpenRouter | API key | `OPENROUTER_API_KEY` |
| Anthropic | API key | `ANTHROPIC_API_KEY` |
| Nous Portal | OAuth | `hermes auth` |
| OpenAI Codex | OAuth | `hermes auth` |
| GitHub Copilot | Token | `COPILOT_GITHUB_TOKEN` |
| Google Gemini | API key | `GOOGLE_API_KEY` or `GEMINI_API_KEY` |
| DeepSeek | API key | `DEEPSEEK_API_KEY` |
| xAI / Grok | API key | `XAI_API_KEY` |
| Hugging Face | Token | `HF_TOKEN` |
| Z.AI / GLM | API key | `GLM_API_KEY` |
| MiniMax | API key | `MINIMAX_API_KEY` |
| MiniMax CN | API key | `MINIMAX_CN_API_KEY` |
| Kimi / Moonshot | API key | `KIMI_API_KEY` |
| Alibaba / DashScope | API key | `DASHSCOPE_API_KEY` |
| Xiaomi MiMo | API key | `XIAOMI_API_KEY` |
| Kilo Code | API key | `KILOCODE_API_KEY` |
| AI Gateway (Vercel) | API key | `AI_GATEWAY_API_KEY` |
| OpenCode Zen | API key | `OPENCODE_ZEN_API_KEY` |
| OpenCode Go | API key | `OPENCODE_GO_API_KEY` |
| Qwen OAuth | OAuth | `hermes login --provider qwen-oauth` |
| Custom endpoint | Config | `model.base_url` + `model.api_key` in config.yaml |
| GitHub Copilot ACP | External | `COPILOT_CLI_PATH` or Copilot CLI |

Full provider docs: https://hermes-agent.nousresearch.com/docs/integrations/providers

### Together AI — Fabric Training Backend Reality Check

`fabric_train`, `fabric_eval`, `fabric_export`, and `fabric_train_status` are the built-in fabric fine-tuning tools. Important constraints:

- **Together AI is the only supported backend.** There is no config option to switch fabric training to OpenAI, SambaNova, OpenRouter, or any other provider.
- **Requires `TOGETHER_API_KEY`** — set in `~/.hermes/.env`.
- **Free-tier model IDs often have a `-Free` suffix in online docs but the actual Together model ID does NOT include it.** Example: `meta-llama/Llama-4-Scout-Free` (wrong) → `meta-llama/Llama-4-Scout-17B-16E-Instruct` (correct). Always verify by querying `GET https://api.together.xyz/v1/models`.
- **Free credits run out.** When credits are exhausted, inference returns `"Credit limit exceeded"` and training will fail. Check credits at Together AI dashboard → Settings → Billing.
- **Alternatives when Together AI credits are exhausted:**
  1. **Local fine-tuning** via `unsloth` skill (fastest, needs GPU with 16GB+ VRAM)
  2. **Local fine-tuning** via `axolotl` skill (YAML-based, more flexible)
  3. **Local fine-tuning** via `fine-tuning-with-trl` skill (TRL/HuggingFace ecosystem)
  These local options need no API key at all — just a CUDA GPU.

Quick diagnostic when training fails:
```bash
# 1. Verify the API key works
curl -s "https://api.together.xyz/v1/models" -H "Authorization: Bearer $TOGETHER_API_KEY" | python3 -c "import json,sys; d=json.load(sys.stdin); print(f'{len(d)} models visible')"

# 2. Test inference with the exact model ID from config
curl -s "https://api.together.xyz/v1/chat/completions" \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"<exact-model-id>","messages":[{"role":"user","content":"OK"}],"max_tokens":10}'

# 3. If credit_limit error -> credits exhausted. Switch to local training or add billing.
```

See also: `references/together-ai-fabric-training-pitfalls.md`

### OpenRouter Key Sync from Bitwarden Secrets Manager

If `OPENROUTER_API_KEY` is in Bitwarden but `.env` shows a placeholder:
1. **Fetch the key**:
   ```bash
   ~/.hermes/bin/bws secret get "OPENROUTER_API_KEY" \
     --project "56db2237-d1af-4366-9e26-b45900708add" \
     --output json | jq -r '.value'
   ```
2. **Update `.env`**:
   ```bash
   sed -i "s/OPENROUTER_API_KEY=.*/OPENROUTER_API_KEY=$(~/.hermes/bin/bws secret get "OPENROUTER_API_KEY" --project "56db2237-d1af-4366-9e26-b45900708add" --output json | jq -r '.value' | sed 's/\//\\\//g')/" ~/.hermes/.env
   ```
3. **Restart Hermes**:
   ```bash
   hermes gateway restart
   ```
4. **Verify**:
   ```bash
   hermes chat -q "test" -m openrouter/owl-alpha --provider openrouter -Q
   ```

#### Pitfall: OpenRouter API returns `HTTP 401` for invalid keys
- **Symptom**: `curl -s "https://openrouter.ai/api/v1/auth/key" -H "Authorization: Bearer ***` returns `401 Missing Authentication header`.
- **Root cause**: The key is revoked or malformed. Generate a new one at [https://openrouter.ai/keys](https://openrouter.ai/keys).
- **Verification**: Always test with `curl` before updating `.env`.

#### Reference
- Full workflow and API quirks: [`references/openrouter-bitwarden-sync.md`](references/openrouter-bitwarden-sync.md)

---

### Monitoring OpenRouter Usage and Credits

If you are using OpenRouter as your provider, monitor usage from the stable key endpoint:

```bash
curl -s https://openrouter.ai/api/v1/auth/key \
     -H "Authorization: Bearer $OPENROUTER_API_KEY"
```

Useful fields commonly present there include:
- `limit`
- `limit_remaining`
- `usage_daily`
- `usage_monthly`
- `is_free_tier`

Practical notes:
- Some older examples on the web mention `https://openrouter.ai/api/v1/auth/usage`, but this may return `404` on current OpenRouter deployments. Prefer `/api/v1/auth/key` for durable automation.
- `limit` / `limit_remaining` from `/api/v1/auth/key` are commonly the **key-level spend cap and remaining cap**, not the user's total wallet/account balance. If a user says "I still have credits in OpenRouter but Hermes shows $0 remaining," explain that the alert is likely reporting the key's monthly limit, not wallet funds.
- For human-readable watcher alerts, label these fields explicitly as **monthly limit** / **remaining limit** rather than vague "remaining credit" to avoid confusion.
- Free-model limits are request-based and can change. OpenRouter docs commonly document `:free` limits such as **20 requests/minute** and daily request caps that depend on whether the account has purchased credits.
- A model page saying `free` is not enough; the model must also still be present in OpenRouter's live `/api/v1/models` response for Hermes to offer it reliably.
- In auxiliary/compression fallback paths, OpenRouter may surface quota exhaustion as **HTTP 403** with text like `Key limit exceeded (monthly limit)`, not just HTTP 402. Treat this as a quota/payment exhaustion case when troubleshooting fallback behavior; otherwise Hermes may appear to "randomly" fail compression instead of moving to the next provider.
- If the user wants **main model first, but OpenRouter free models as fallback for compression**, keep `auxiliary.compression.provider: auto` and set an explicit free model such as:
  ```yaml
  auxiliary:
    compression:
      provider: auto
      model: openrouter/owl-alpha
  ```
  Intended behavior: main runtime first, then OpenRouter fallback using that free model.

  Important Codex caveat: older Hermes builds could incorrectly pass the OpenRouter slug to the main Codex provider during Step 1 of auto-resolution, producing errors like:
  `The 'openrouter/owl-alpha' model is not supported when using Codex with a ChatGPT account.`
  Fix by patching `agent/auxiliary_client.py` so an `openrouter/...` task override only steers the OpenRouter fallback path and does **not** replace the main provider's model during the primary auto-resolution step.
- OpenRouter sometimes reports key exhaustion as **HTTP 403** with wording like `Key limit exceeded (monthly limit)`, not just HTTP 402. When Hermes auxiliary tasks such as compression fail with that exact pattern, treat it as a key-level quota exhaustion signal on the OpenRouter fallback path, not proof that the user's main model/provider is OpenRouter.

### Automating free-model watch + auto-sync

If the user wants more than alerts — specifically, "notify me when OpenRouter free models change and automatically add/remove them from my Hermes model list" — prefer a `cronjob` with `script=<watcher>` and `no_agent=True` rather than an LLM prompt. The script should:

1. Read `/api/v1/auth/key` and `/api/v1/models`
2. Detect free models from zero pricing, not `:free` suffix alone
3. Compare against a persisted state file
4. Emit stdout only when something changed (for `no_agent=True`, empty stdout = silent/no notification)
5. Rewrite the custom OpenRouter catalog override file (for example `~/.hermes/cache/free_openrouter_catalog.json`) so Hermes picker tracks the live free set
6. Maintain a clearly marked auto-managed alias block in `config.yaml` under `model_aliases:` while preserving the user's manual aliases

Implementation pitfalls that matter in practice:
- **Ignore timestamp-only diffs** such as `updated_at` when checking whether the catalog changed, or the watcher will notify on every run.
- **Insert the managed alias block inside `model_aliases:` and before the fallback-model comment block**; appending it after the section boundary makes the config logically wrong.
- **Preserve non-free curated entries** (cheap/manual picks) when rewriting the catalog; only replace the free-model portion.
- **Verify idempotence** by running the script twice: first run may sync, second run should usually print nothing.

See `references/openrouter-free-watch-automation.md` for a compact implementation/verification checklist.

You can also view Hermes session-level usage with `/usage`.

### Local Ollama as a Non-Default Optional Provider

If the user wants Ollama available for switching **without replacing the main default model**, keep the main `model.default` / `model.provider` unchanged and add Ollama as a custom provider plus explicit aliases.

### Codex OAuth / ChatGPT plan usage visibility

When the user is using Hermes with **Codex auth tied to a ChatGPT Plus/Pro account** and asks things like:
- "how much of my 5-hour limit is left?"
- "how much weekly limit is left?"
- "can Hermes show my Codex remaining usage?"

Do **not** imply Hermes has a built-in live meter unless you verified a current command/UI path in the installed build.

Durable guidance:
- OpenAI's public docs say to check current Codex limits in **Codex Settings → Usage** / **Usage Dashboard**
- This is the authoritative place to see **remaining usage**, **weekly/5-hour buckets**, **credit balance**, and **recent usage**
- There is **not a stable documented Hermes command** for reading those remaining ChatGPT-plan Codex limits directly
- There is **not a stable public CLI meter** you should promise for Codex OAuth / ChatGPT-account quotas unless you verify one exists in the current Codex build

Important framing:
- the **5-hour** and **weekly** limits are separate buckets
- a user can still have some **5-hour** headroom while the **weekly** limit is already exhausted
- newer OpenAI docs also frame Codex usage in **credits/token-based usage**, so remaining usage is no longer well-modeled as simple elapsed wall-clock time

Best response shape:
1. say Hermes itself usually cannot show those numbers directly
2. point the user to **Codex Settings → Usage / Usage Dashboard**
3. mention the 5-hour and weekly meters are independent
4. if relevant, mention that additional **credits** can extend usage beyond included plan limits

### Ollama Cloud

Ollama supports **cloud models** that run on Ollama's hosted infrastructure. Model pages expose cloud tags such as `deepseek-v4-flash:cloud`, `deepseek-v4-pro:cloud`, `gemma4:31b-cloud`.

```bash
ollama signin
ollama run deepseek-v4-flash:cloud
```

Pricing: Free = light usage, 1 concurrent; Pro = 50x more, 3 concurrent; Max = 5x Pro, 10 concurrent. Limits reset every 5 hours and every 7 days. Ollama describes usage qualitatively (not a fixed request count).

### Browser Tools

Browser tools (`browser_navigate`, `browser_click`, `browser_snapshot`, `browser_vision`) enable web navigation, interaction, and content extraction. See existing Hermes docs for full capabilities and limitations.

### Toolsets

Enable/disable via `hermes tools` (interactive) or `hermes tools enable/disable NAME`.

| Toolset | What it provides |
|---------|-----------------|
| `web` | Web search and content extraction |
| `browser` | Browser automation |
| `terminal` | Shell commands and process management |
| `file` | File read/write/search/patch |
| `code_execution` | Sandboxed Python execution |
| `vision` | Image analysis |
| `image_gen` | AI image generation |
| `tts` | Text-to-speech |
| `skills` | Skill browsing and management |
| `memory` | Persistent cross-session memory |
| `session_search` | Search past conversations |
| `delegation` | Subagent task delegation |
| `cronjob` | Scheduled task management |
| `clarify` | Ask user clarifying questions |
| `messaging` | Cross-platform message sending |
| `search` | Web search only (subset of `web`) |
| `todo` | In-session task planning and tracking |

Tool changes take effect on `/reset` (new session). They do NOT apply mid-conversation to preserve prompt caching.

---

## Security & Privacy Toggles

### Secret Redaction

Secret redaction is **off by default**. To enable:

```bash
hermes config set security.redact_secrets true
```

**Restart required** — `security.redact_secrets` is snapshotted at import time. A new session is needed.

### PII Redaction

```bash
hermes config set privacy.redact_pii true    # enable
hermes config set privacy.redact_pii false   # disable (default)
```

### Command Approval

- `manual` — always prompt (default)
- `smart` — auto-approve low-risk, prompt on high-risk
- `off` — skip all approval prompts

```bash
hermes config set approvals.mode smart
```

Per-invocation bypass: `hermes --yolo` or `export HERMES_YOLO_MODE=1`.

---

## Voice & Transcription

### STT (Voice → Text)

1. **Local faster-whisper** — free, no API key: `pip install faster-whisper`
2. **Groq Whisper** — free tier: set `GROQ_API_KEY`
3. **OpenAI Whisper** — paid: set `VOICE_TOOLS_OPENAI_KEY`
4. **Mistral Voxtral** — set `MISTRAL_API_KEY`

### TTS (Text → Voice)

| Provider | Env var | Free? |
|----------|---------|-------|
| Edge TTS | None | Yes (default) |
| ElevenLabs | `ELEVENLABS_API_KEY` | Free tier |
| OpenAI | `VOICE_TOOLS_OPENAI_KEY` | Paid |
| MiniMax | `MINIMAX_API_KEY` | Paid |
| NeuTTS (local) | None | Free |

Voice commands: `/voice on` (voice-to-voice), `/voice tts` (always voice), `/voice off`.

---

## Spawning Additional Hermes Instances

### One-Shot Mode

```bash
hermes chat -q 'Research GRPO papers and write summary to ~/research/grpo.md'
```

### Interactive PTY Mode (via tmux)

```bash
tmux new-session -d -s agent1 -x 120 -y 40 'hermes'
sleep 8 && tmux send-keys -t agent1 'Build a FastAPI auth service' Enter
```

### When to Use Spawning vs delegate_task

| | `delegate_task` | Spawning `hermes` process |
|-|-----------------|--------------------------|
| Isolation | Separate conversation, shared process | Fully independent process |
| Duration | Minutes | Hours/days |
| Interactive | No | Yes (PTY mode) |
| Use case | Quick parallel subtasks | Long autonomous missions |

---

## Troubleshooting

### Voice not working
1. Check `stt.enabled: true` in config.yaml
2. Verify provider: `pip install faster-whisper` or set API key
3. In gateway: `/restart`. In CLI: exit and relaunch.

### Tool not available
1. `hermes tools` — check if toolset is enabled for your platform
2. Some tools need env vars (check `.env`)
3. `/reset` after enabling tools

### Model/provider issues
1. `hermes doctor` — check config and dependencies
2. `hermes login` — re-authenticate OAuth providers
3. Check `.env` has the right API key
4. **Copilot 403**: `gh auth login` tokens do NOT work for Copilot API. You must use the Copilot-specific OAuth device code flow via `hermes model` → GitHub Copilot.
5. **Gemini shows `invalid API key` in `hermes doctor`, but direct Google API calls succeed**: treat this as a possible doctor false alarm / check-path mismatch before rotating keys. Verify the exact live config/env paths first:
6. **OpenRouter picker reality: curated list ∩ live OpenRouter models ∩ tool support**. When a user says “this model is in docs/OpenRouter pages but does not show in Hermes `/model` or dashboard”, do not assume the config edit failed. Hermes’ OpenRouter picker is built by `fetch_openrouter_models()` and only shows models that satisfy all three conditions:
   - present in the curated catalog source (`model_catalog` or fallback list)
   - present in OpenRouter live `https://openrouter.ai/api/v1/models`
   - passes Hermes tool-capability filtering (`supported_parameters` includes tools, or field is absent)

   Practical consequence: a model can be documented on OpenRouter, or even appear on some OpenRouter web pages, yet still be hidden in Hermes if it is absent from the live `/api/v1/models` response at that moment. This especially affects `:free` preview/testing models.

7. **How to override the OpenRouter picker with a custom catalog**: `model_catalog.providers.<provider>` in `config.yaml` does **not** accept inline `models:` overrides for Hermes picker behavior. The effective override path is a provider-specific `url`, because Hermes calls `_fetch_provider_override()` and fetches a full manifest from that URL. A working local pattern is:
   ```yaml
   model_catalog:
     enabled: true
     url: https://hermes-agent.nousresearch.com/docs/api/model-catalog.json
     ttl_hours: 24
     providers:
       openrouter:
         url: file:///root/.hermes/cache/free_openrouter_catalog.json
   ```
   Then place a valid manifest JSON at that file URL. `urllib.request.urlopen()` accepts `file://` URLs, so this works without a web server.

8. **Dashboard vs CLI model-list mismatch: compare the exact serving path, not just config files**. There are two distinct layers:
   - the dashboard REST endpoint `/api/model/options`
   - the CLI / interactive picker helpers in `hermes_cli`

   Good diagnostic sequence:
   - verify `hermes_home` and `config_path` from dashboard `/api/status`
   - verify the gateway/user service `HERMES_HOME`
   - query the live dashboard session token from `/` and then call `/api/model/options` with header `X-Hermes-Session-Token`
   - compare that payload to the Python helper output from the Hermes venv

   If a model is present in OpenRouter live API and in the custom catalog, but still absent only in the dashboard, inspect whether the dashboard inventory builder is calling the picker-aware path.

9. **Hermes contributor pitfall: dashboard model picker must use `list_picker_providers()`**. A real failure mode is that the dashboard backend may call `build_models_payload()` → `list_authenticated_providers()`, while CLI picker logic uses `list_picker_providers()`. That causes OpenRouter differences between dashboard and CLI even with the same config. If fixing Hermes itself, make the dashboard inventory builder use the picker-aware provider path so both surfaces share the same filtered OpenRouter list.

See also: `references/gateway-restart-tempfail-and-gemini-doctor.md` for the exact debugging flow, auth header, and the dashboard-vs-CLI picker divergence fix.

See also: `references/mnemosyne-memory-provider.md` for complete Mnemosyne memory provider installation, upgrade, and troubleshooting (dual-venv architecture, bootstrap pitfalls, patch for missing `__version__`, verification checklist).

---

## Skill Authoring (absorbed from `hermes-agent-skill-authoring`)

### When to Use
- Creating new skills for the Hermes ecosystem
- Editing existing in-repo skills under `skills/<category>/`
- Understanding SKILL.md frontmatter requirements and validator constraints

### Key Concepts
- **User-local vs In-repo**: `skill_manage(create)` writes to `~/.hermes/skills/`; in-repo skills require `write_file` to `skills/<category>/<name>/SKILL.md` and git commit
- **Frontmatter Requirements**: `name`, `description` (≤1024 chars, starts with "Use when..."), `version`, `author`, `license`, `metadata.hermes.{tags, related_skills}`
- **Size Limits**: Description ≤1024 chars, full SKILL.md ≤100,000 chars (aim for 8-15k)
- **Peer-Matched Structure**: `# Title` → `## Overview` → `## When to Use` → body → `## Common Pitfalls` → `## Verification Checklist`

### Directory Placement
```
skills/<category>/<skill-name>/SKILL.md
```
Categories: `autonomous-ai-agents`, `creative`, `data-science`, `devops`, `dogfood`, `email`, `gaming`, `github`, `leisure`, `mcp`, `media`, `mlops/*`, `note-taking`, `productivity`, `red-teaming`, `research`, `smart-home`, `social-media`, `software-development`

### Workflow
1. Survey peers in target category (`ls skills/<category>/`)
2. Check validator constraints in `tools/skill_manager_tool.py`
3. Draft with `write_file`
4. Validate locally
5. Git add + commit

### Common Pitfalls
1. Using `skill_manage(create)` for in-repo skills (writes to wrong location)
2. Leading whitespace before `---` (validator checks `content.startswith("---")`)
3. Generic descriptions — must start with "Use when..." and describe trigger class
4. Missing author/license/metadata block
5. Duplicating existing peer skills

### Verification Checklist
- [ ] File at `skills/<category>/<name>/SKILL.md`
- [ ] Frontmatter starts at byte 0 with `---`, closes with `\n---\n`
- [ ] All required fields present
- [ ] Name ≤64 chars, lowercase + hyphens
- [ ] Description ≤1024 chars, starts with "Use when..."
- [ ] Total file ≤100,000 chars
- [ ] Standard structure followed
- [ ] `related_skills` references resolve in-repo
- [ ] Git committed on intended branch

---

## Credential Pooling (absorbed from `hermes-credential-pooling`)

### When to Use
- Managing multiple API keys/OAuth accounts for the same provider
- Configuring rotation strategies (fill_first, round_robin, least_used, random)
- Setting up Google Gemini OAuth (PKCE flow, paste mode for headless)
- Troubleshooting credential exhaustion and rotation behavior

### Pool Strategies
| Strategy | Behavior | Best For |
|----------|----------|----------|
| `fill_first` (default) | Use first healthy key until exhausted | Single primary, fallback only |
| `round_robin` | Cycle through healthy keys evenly | **Multi-account load spreading** (recommended for Google Gemini) |
| `least_used` | Pick key with lowest request_count | Usage-based balancing |
| `random` | Random healthy key | Unpredictable distribution (avoid) |

Configure in `config.yaml`:
```yaml
credential_pool_strategies:
  openai-codex: round_robin
  google-gemini-cli: round_robin
  openrouter: round_robin
```

### Google Gemini OAuth (`google-gemini-cli`)
**Provider Variants:**
- `google-gemini-cli` — OAuth PKCE, Cloud Code Assist backend (currently HTTP 404)
- `gemini` — API key (`GOOGLE_API_KEY`), official AI Studio (stable)

**Setup:**
```bash
# First account
hermes auth add google-gemini-cli --label account1

# Additional accounts for round-robin
hermes auth add google-gemini-cli --label account2
hermes auth add google-gemini-cli --label account3
```

**Headless/Paste Mode** (SSH or no browser):
```bash
HERMES_HEADLESS=1 hermes auth add google-gemini-cli
```
Paste the full redirect URL or just the `code=` value from any device's browser.

**Current Issue (June 2026):** `google-gemini-cli` returns HTTP 404 from Cloud Code Assist. **Workaround:** Use official `gemini` provider with API key.

### Multi-Account Patterns
**Option A: Credential Pool (Auto-Rotate)**
```bash
hermes auth add google-gemini-cli --label work
hermes auth add google-gemini-cli --label personal
# round_robin strategy auto-rotates per request
```

**Option B: Separate Profiles (Manual Switch)**
```bash
hermes profile create gemini-work --clone
hermes profile create gemini-personal --clone
hermes profile use gemini-work
```

### Verification Commands
```bash
hermes auth list google-gemini-cli
hermes config get credential_pool_strategies.google-gemini-cli
hermes chat -m google-gemini-cli -q "test" -Q
```

**References:** `references/credential-pool-internals.md`, `references/google-gemini-oauth-flow.md`

---

## Third-Party Plugin Operations (absorbed from `hermes-third-party-plugin-operations`)

### When to Use
- Installing, verifying, or evaluating third-party Hermes plugins/dashboards
- Live debugging plugin UI issues (blank routes, broken tabs, auth fallbacks)
- Exposing plugins on LAN/local ports and verifying binding
- Patching plugins locally and deciding whether to upstream PRs

### Workflow
1. **Inspect before touching** — Read repo docs, packaging, manifest. Confirm plugin type, config path, default port, runtime entrypoint.
2. **Check live Hermes first** — Verify Hermes version, plugin/memory status, real DB/storage path. Check built-in Hermes page overlap.
3. **Prefer live startup** — `hermes plugins install && hermes gateway restart` can interrupt shell. Inspect plugin dir directly, start via real entrypoint. Verify listener, health endpoint, page load.
4. **Verify network exposure** — Check bind address (127.0.0.1 vs 0.0.0.0), listening socket. Verify LAN URL after rebind if requested.
5. **QA UI by sections** — Click major tabs/routes. Check browser console and API responses. Compare empty states against backend facts.
6. **Treat empty graphs carefully** — Verify underlying triple/graph store has rows before calling blank views a rendering defect.
7. **Common pitfalls:**
   - False auth fallback: login overlay shown for generic JS/bootstrap failures
   - Stale tab aliases: deep links keep old `?tab=` values after renames
   - Don't stop after homepage success; broken tabs often hide behind landing pages
   - Don't upstream host/IP/path config changes

### Verification Checklist
- [ ] Plugin files exist where expected
- [ ] Runtime config points to intended DB/storage
- [ ] Listener bound on intended host:port
- [ ] Health endpoint returns success
- [ ] Main page loads
- [ ] Each major tab/route exercised
- [ ] Browser console checked on broken routes
- [ ] Empty graph views correlated against backend counts
- [ ] Frontend fixes re-tested on normal load and simulated failure

### Support Files (moved to this skill's references/)
- `references/freellmapi-operations.md` — FreeLLMAPI install/update/config
- `references/mnemosyne-dashboard-live-debugging.md` — Live debugging techniques
- `references/hermes-plugin-structure.md` — Minimum viable plugin skeleton

### Upstreaming Rule
PR warranted when fix is generic (route alias restoration, auth-aware bootstrap fallback, operator boot diagnostics). NOT for local LAN IP/port choices, host-specific DB paths, environment-specific install quirks.

### Slash Command Not Showing in Autocomplete/Picker

When a user says "command X doesn't show in my command line", the issue is usually a visibility flag on `CommandDef`:

- **`cli_only=True`** → command works in CLI+TUI but intentionally hidden from gateway (Telegram/Discord) command menus. This is expected behavior, not a bug.
- **`gateway_only=True`** → command works in gateway but hidden from CLI/TUI autocomplete.
- **`_TUI_HIDDEN`** in `tui_gateway/server.py` → command hidden from TUI catalog regardless of other flags.

Diagnostic flow and full flag reference: `references/command-visibility-filtering.md`

### Auxiliary Model Fallback Behavior

All auxiliary sections (`vision`, `compression`, `session_search`, `title_generation`, etc.) default to:
```yaml
provider: auto
model: ''
```
Empty model → falls back to `GOOGLE_API_KEY` / Gemini. If Gemini lacks access (HTTP 403), aux tasks like title generation fail silently.

**Fix:** Set explicit model to main default:
```bash
hermes config set auxiliary.title_generation.model "openrouter/owl-alpha"
```
Or switch all aux sections at once by setting `model` in each.

### .env File Protection

`.env` is a protected credential file. The `patch` tool will deny writes:
```
Write denied: '/root/.hermes/.env' is a protected system/credential file.
```
Always use `hermes config set KEY VAL` for `.env` values — this works for both `.env` and `config.yaml`.

### Changes not taking effect
- **Tools/skills:** `/reset` starts a new session with updated toolset
- **Config changes:** In gateway: `/restart`. In CLI: exit and relaunch.
- **Dashboard / `/model` still showing stale provider models after config edits:** hard-refresh the dashboard page and restart the gateway/dashboard processes.
- **Dashboard plugin route looks blank but sidebar loads:** distinguish **route-load failure** from **plugin-runtime failure**.
  - First compare `/` versus the direct plugin route (for example `/mission-control`). If `/` renders but the direct route is blank, suspect a plugin runtime bug or stale cached plugin JS rather than a dead dashboard.
  - Check the plugin asset URLs under `/dashboard-plugins/<name>/...` load with `200`.
  - If the app works after opening `/` and then clicking the plugin tab, but direct deep-linking stays blank, do a hard refresh / private window test to rule out cached JS.
  - For dist-only companion dashboards, a small runtime error in the plugin bundle can blank only that route while the rest of Hermes still works.
- **Built-in memory size changes (`memory.user_char_limit`, `memory.memory_char_limit`)**: prefer compressing `USER.md` / `MEMORY.md` first, then make only a modest increase if still needed (for example `hermes config set memory.user_char_limit 1600`). Fresh sessions pick up the new limit only after a CLI relaunch or gateway restart.

### Memory Char Limit — Proactive Consolidation Strategy

`USER.md` has a default limit of 1,600 chars and `MEMORY.md` shares a similar cap. When the `memory` tool returns "would exceed the limit," do NOT just fail — consolidate:

**Consolidation tactics (in order of preference):**
1. **Merge related entries** — e.g. combine "trading platforms" + "dashboard preferences" + "Mission Control preferences" into one entry about Hermes UI preferences
2. **Move agent-internal notes to `MEMORY.md`** — Things like "Hermes dashboard should be premium" or "Mission Control should be separate" are agent operational notes, not user identity. Move them to free space in `USER.md`
3. **Abbreviate** — Use shorter phrasing, remove examples, keep only the essential constraint
4. **Increase limit as last resort** — `hermes config set memory.user_char_limit 2200` (modest increase)

**File locations:**
- `~/.hermes/memories/USER.md` — user profile & preferences (target: user)
- `~/.hermes/memories/MEMORY.md` — agent technical notes (target: memory)

**Preemptive habit:** When adding a new entry, check current usage first. If above 80%, consolidate before adding. The `memory` tool returns current usage in its error message.

**When both USER.md and MEMORY.md need cleanup:** If USER.md is full and contains stale workflow entries (old project paths, completed task details), move truly outdated items to trash rather than MEMORY.md. MEMORY.md should only contain agent technical notes — not old user workflow preferences. When in doubt, ask the user what to keep before deleting.

### Moving `HERMES_HOME` Safely

Changing `HERMES_HOME` can cause **path split-brain** where different components point at different homes.

1. Verify target dir contains: `config.yaml`, `.env`, `auth.json`, `sessions/`, `plugins/`, `state.db`
2. Check live paths: `echo "$HERMES_HOME"`, `hermes config path`, `hermes config env-path`
3. If gateway unit still points to old home: `hermes gateway restart`
4. Hard-refresh browser after restart

See also: `references/hermes-home-move-recovery.md`, `references/symlinked-hermes-home-storage-check.md`.

### Icarus / Fabric recall noise reduction

If the user says the visible `[fabric] ...` recall block is noisy, first distinguish **prompt-internal recall** from **reply-visible leakage**:

- Quiet behavior: recall should stay internal, like `Internal memory note — do not quote or mention this note unless directly relevant:`
- Noisy behavior: startup context or handoff notes are formatted with visible-looking prefixes like `[fabric] ...`, or the literal `Internal memory note ...` line itself leaks into the final reply/output

Practical fix pattern:
1. Inspect the Icarus plugin hook that injects startup context (`~/.hermes/plugins/icarus/hooks.py`)
2. In `on_session_start()`, replace multi-line `[fabric]` pending/review/ticket dumps with a **single compact internal note** per category, ideally only the top item plus `+N more`
3. Keep `pre_llm_call()` recall short (`max_results=1` is a good default) and worded as an internal note, not user-facing output
4. Avoid human-readable bracketed markers like `[assistant-only background memory ...]` in `pre_llm_call()` recall injection — they can still leak verbatim in user-facing replies. Prefer either (a) skipping proactive recall entirely when the current user message looks like a pasted error/log dump, and/or (b) a low-visibility machine-style marker such as an HTML comment (`<!-- hermes-internal-recall: ... -->`) plus aggressive summary sanitization.
5. Verify with a smoke test such as:
   ```bash
   hermes chat -Q -q "say only OK"
   ```
   If the output is clean, the plugin-side noise reduction worked
6. If Telegram/gateway still shows the old block after patching, reload the gateway (`/restart` in chat or `hermes gateway restart`) because plugin code may still be running from the old process

Important framing: do **not** disable memory entirely by default when the complaint is only about noise. Prefer **compressing and internalizing** the recall text so memory remains useful without leaking into normal replies.

See also: `references/icarus-noise-reduction.md` for the concrete patch shape and verification checklist.

### Gateway Issues

```bash
grep -i "failed to send\|error" ~/.hermes/logs/gateway.log | tail -20
```

Common problems:
- **Gateway dies on SSH logout**: `sudo loginctl enable-linger $USER`
- **Gateway crash loop**: `systemctl --user reset-failed hermes-gateway`
- **TEMPFAIL after restart**: `systemctl --user reset-failed hermes-gateway && systemctl --user start hermes-gateway`

### `hermes_otel` + Phoenix local backend

When a user says the OTEL plugin is enabled but `127.0.0.1:6006` is blank, the Hermes OTEL tab shows `502 backend not enabled`, or logs show export failures to `127.0.0.1:6006`, treat it as a **backend availability** problem first, not a plugin-toggle problem.

Fast diagnostic sequence:
1. `hermes plugins list` — confirm `hermes_otel` is enabled
2. Check `~/.hermes/plugins/hermes_otel/config.yaml` for a Phoenix backend like `endpoint: http://127.0.0.1:6006/v1/traces`
3. Check whether anything is actually listening on port `6006`
4. Distinguish the two UIs:
   - Hermes dashboard may be on another port (for example `9119` via nginx or direct app port like `9120`)
   - Phoenix OTEL UI is the tracing backend on `6006`
5. If port `6006` is down, start Phoenix from the bundled compose file:
   ```bash
   docker compose -f ~/.hermes/plugins/hermes_otel/docker-compose/phoenix.yaml up -d
   ```
6. For persistence across reboot/container restart, set both:
   - compose file: `restart: unless-stopped`
   - existing container: `docker update --restart unless-stopped docker-compose-phoenix-1`
7. Re-run compose after changing the file so future recreates keep the policy

Verification:
- `curl http://127.0.0.1:6006/` should return HTML
- GraphQL should respond on `http://127.0.0.1:6006/graphql`
- `docker inspect -f '{{.HostConfig.RestartPolicy.Name}}' docker-compose-phoenix-1` should print `unless-stopped`

First-start nuance: Phoenix can briefly reset connections while migrations finish. If logs show startup/migrations and the port is bound, retry before declaring failure.

See also: `references/phoenix-otel-local-backend.md`.

### Platform-Specific Issues

- **Discord bot silent**: Enable **Message Content Intent** in Bot → Privileged Gateway Intents.
- **Discord require_mention**: Check live config with `sed -n '/^discord:/,/^[^ ]/p' ~/.hermes/config.yaml`
- **Discord skill commands not visible as top-level `/claude-code`, `/codex`, etc.**: This is expected. Hermes Discord does **not** register one top-level slash command per skill. Instead it registers a single `/skill` command and exposes installed skills through autocomplete on the skill name. Tell the user to run `/skill` and then choose/type `claude-code`, `codex`, `crypto-analysis`, `github-pr-workflow`, etc. This design avoids Discord slash-command payload/registration limits.
- **Slack bot only works in DMs**: Must subscribe to `message.channels` event.

---

## Where to Find Things

| Looking for... | Location |
|----------------|----------|
| Config options | `hermes config edit` or [Configuration docs](https://hermes-agent.nousresearch.com/docs/user-guide/configuration) |
| Available tools | `hermes tools list` or [Tools reference](https://hermes-agent.nousresearch.com/docs/reference/tools-reference) |
| Slash commands | `/help` in session or [Slash commands reference](https://hermes-agent.nousresearch.com/docs/reference/slash-commands) |
| Skills catalog | `hermes skills browse` or [Skills catalog](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) |
| Provider setup | `hermes model` or [Providers guide](https://hermes-agent.nousresearch.com/docs/integrations/providers) |
| Platform setup | `hermes gateway setup` or [Messaging docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/) |
| MCP servers | `hermes mcp list` or [MCP guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) |
| Profiles | `hermes profile list` or [Profiles docs](https://hermes-agent.nousresearch.com/docs/user-guide/profiles) |
| Cron jobs | `hermes cron list` or [Cron docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) |
| Memory | `hermes memory status` or [Memory docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) |
| Env variables | `hermes config env-path` or [Env vars reference](https://hermes-agent.nousresearch.com/docs/reference/environment-variables) |
| CLI commands | `hermes --help` or [CLI reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands) |
| Gateway logs | `~/.hermes/logs/gateway.log` |
| Session files | `~/.hermes/sessions/` or `hermes sessions browse` |
| Source code | `~/.hermes/hermes-agent/` |

---

## Contributor Quick Reference

Full developer docs: https://hermes-agent.nousresearch.com/docs/developer-guide/

### Project Layout

```
hermes-agent/
├── run_agent.py          # AIAgent — core conversation loop
├── model_tools.py        # Tool discovery and dispatch
├── cli.py                # Interactive CLI (HermesCLI)
├── hermes_state.py       # SQLite session store
├── agent/                # Prompt builder, context compression, memory, model routing
├── tools/                # One file per tool
├── gateway/              # Messaging gateway
├── tests/                # ~3000 pytest tests
└── website/              # Docusaurus docs site
```

### Adding a Tool (3 files)

**1. Create `tools/your_tool.py`:**

```python
import json, os
from tools.registry import registry

def check_requirements() -> bool:
    return bool(os.getenv("EXAMPLE_API_KEY"))

def example_tool(param: str, task_id: str = None) -> str:
    return json.dumps({"success": True, "data": "..."})

registry.register(
    name="example_tool",
    toolset="example",
    schema={"name": "example_tool", "description": "...", "parameters": {...}},
    handler=lambda args, **kw: example_tool(
        param=args.get("param", ""), task_id=kw.get("task_id")),
    check_fn=check_requirements,
    requires_env=["EXAMPLE_API_KEY"],
)
```

### Testing

```bash
python -m pytest tests/ -o 'addopts=' -q   # Full suite
python -m pytest tests/tools/ -q            # Specific area
```

### Commit Conventions

```
type: concise subject line

Optional body.
```

Types: `fix:`, `feat:`, `refactor:`, `docs:`, `chore:` — keep subject under 72 chars.

### Key Rules

- **Never break prompt caching** — don't change context, tools, or system prompt mid-conversation
- **Message role alternation** — never two assistant or two user messages in a row
- Use `get_hermes_home()` from `hermes_constants` for all paths (profile-safe)
- Config values go in `config.yaml`, secrets go in `.env`
- New tools need a `check_fn` so they only appear when requirements are met
