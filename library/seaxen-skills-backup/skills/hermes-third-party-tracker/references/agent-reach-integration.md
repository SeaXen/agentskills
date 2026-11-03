# Agent-Reach Integration

Agent-Reach is a **capability layer** (CLI + skill installer) that gives AI agents unified read/search access to 14+ web platforms without paid API keys: Twitter/X, Reddit, YouTube, GitHub, Bilibili, 小红书, LinkedIn, V2EX, RSS, Web Search (Exa via mcporter), Jina Reader, 雪球, 小宇宙播客.

## What It Is

| Category | Detail |
|----------|--------|
| **Type** | Python package (`agent-reach`) + downstream CLIs |
| **Install** | `pipx install git+https://github.com/Panniantong/agent-reach.git` |
| **Primary CLIs installed** | `twitter-cli`, `yt-dlp`, `bili-cli`, `gh`, `mcporter`, `OpenCLI`, `rdt-cli`, `xiaohongshu-mcp` |
| **Config** | `~/.agent-reach/config.yaml` (per-channel backend config, 600 perms) |
| **Skill file** | `/root/.agents/skills/agent-reach/SKILL.md` (for OpenClaw) |
| **MCP** | Optional: `agent-reach install --channels mcp` generates MCP configs |

## Hermes Integration Pattern

**Hermes does NOT need a plugin or MCP** — it uses the existing `terminal` toolset to run the installed CLIs directly.

```bash
# Install on host (or in container with CLIs)
pipx install git+https://github.com/Panniantong/agent-reach.git
agent-reach install --env=auto
agent-reach doctor  # verify channels
```

Then in any Hermes session with `terminal` toolset enabled:
```python
# GitHub
terminal(command='gh repo view Panniantong/agent-reach --json description,stargazerCount')

# YouTube subtitles
terminal(command='yt-dlp --write-sub --skip-download -o "/tmp/%(id)s" "https://youtube.com/watch?v=..."')

# Bilibili search
terminal(command='bili search "rust" --type video -n 5')

# Web search (Exa via mcporter)
terminal(command="mcporter call 'exa.web_search_exa(query:\"bitcoin\", numResults:5)'")

# Any web page via Jina Reader
terminal(command='curl -s "https://r.jina.ai/https://github.com/Panniantong/agent-reach"')
```

## Tracker Registry Entry

Since agent-reach is installed via pipx from git (no local `.git` dir), it cannot be auto-discovered by the scan script. Add to dashboard registry:

```json
{
  "name": "agent-reach",
  "url": "https://github.com/Panniantong/agent-reach",
  "local_path": "",
  "notes": "Agent internet capability layer (14+ platforms, zero API keys). Installed via pipx from git. CLIs: twitter-cli, yt-dlp, bili-cli, gh, mcporter, OpenCLI, rdt-cli, xiaohongshu-mcp. Skill file at /root/.agents/skills/agent-reach/"
}
```

- `local_path: ""` signals "no local git repo" — tracker will show `manual_only` update status
- Update manually: `pipx upgrade agent-reach`

## Channel Status (Post-Install)

Run `agent-reach doctor --json` to see active backends per platform:

| Platform | Status | Backend |
|----------|--------|---------|
| GitHub | ✅ | `gh CLI` |
| YouTube | ✅ | `yt-dlp` |
| V2EX | ✅ | Public API |
| RSS/Atom | ✅ | `feedparser` |
| Web Search (Exa) | ✅ | `mcporter` |
| Web Pages (Jina) | ✅ | `curl r.jina.ai` |
| Bilibili | ✅ | `bili-cli` |
| Twitter/X | ⚠️ | Needs `pipx install twitter-cli` + browser login |
| Reddit | ❌ | Needs `rdt-cli` or OpenCLI |
| 小红书 | ❌ | Needs OpenCLI or `xiaohongshu-mcp` |
| LinkedIn | ❌ | Needs `linkedin-scraper-mcp` |
| 小宇宙 | ❌ | Needs `agent-reach install --env=auto` (transcribe tools) |
| 雪球 | ⚠️ | Needs browser login + `agent-reach configure` |

## Optional Channels Installation

```bash
# Twitter (Cookie-based, no API key)
pipx install twitter-cli
# Login to x.com in browser once → twitter search "query" works

# Reddit (rdt-cli fallback)
pipx install git+https://github.com/public-clis/rdt-cli.git@5e4fb3720d5c174e976cd425ccc3b879d52cac66
rdt login

# 小红书 (desktop: OpenCLI; server: xiaohongshu-mcp)
# OpenCLI has install issues on Python 3.13 — use xiaohongshu-mcp for server

# MCP exposure (optional)
agent-reach install --channels mcp
# Adds ~/.agent-reach/mcp/*.json → add to Hermes config.yaml under mcp.servers
```

## Key Distinction

Agent-reach is a **bootstrap layer** that installs the real tools. Hermes talks to those tools directly (shell) or via MCP (optional). It is not a Hermes plugin, not an MCP server by default, and does not require Hermes code changes.