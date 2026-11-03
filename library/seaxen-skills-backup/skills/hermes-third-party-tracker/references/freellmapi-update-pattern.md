# FreeLLMAPI Update Pattern

FreeLLMAPI is an OpenAI-compatible proxy for free LLM tiers (OpenRouter free models + 15 others). It runs as a Docker container on a dedicated port (default 3055, exposed via LAN as 3055).

## Installation (Already Done)

- Repo: `https://github.com/tashfeenahmed/freellmapi`
- Local clone: `/root/freellmapi/`
- Docker Compose: `/root/freellmapi/docker-compose.yml`
- Dashboard: `http://192.168.0.222:3055`
- Registry entry: `third_party_tracker_registry.json` with name `FreeLLMAPI`

## Update Workflow

FreeLLMAPI publishes pre-built images to `ghcr.io/tashfeenahmed/freellmapi:latest`. **Do not build from source** — the Dockerfile pulls Debian packages and frequently fails due to network/apt issues in this environment.

```bash
# 1. Check for updates
cd /root/freellmapi
git fetch
git log --oneline HEAD..origin/main -5

# 2. Pull latest image
docker pull ghcr.io/tashfeenahmed/freellmapi:latest

# 3. Restart container with new image
docker compose up -d --pull always

# 4. Verify health
sleep 5
curl -s http://192.168.0.222:3055/api/ping
# Expected: {"status":"ok","timestamp":"..."}
```

## Why Not Build Locally

The `Dockerfile` uses `debian:bookworm-slim` and runs `apt-get install -y python3 make g++` which hits `deb.debian.org` and frequently times out or fails with 404s on package versions. The pre-built GHCR image avoids this entirely.

## Registry Tracking

The tracker registry entry:
```json
{
  "name": "FreeLLMAPI",
  "url": "https://github.com/tashfeenahmed/freellmapi",
  "local_path": "/root/freellmapi",
  "port": 3055,
  "dashboard_url": "http://192.168.0.222:3055",
  "notes": "OpenAI-compatible proxy for free LLM tiers (OpenRouter free models + 15 others). Docker install on server. Unified key from dashboard header."
}
```

The scan script detects this via the registry, runs `git_repo_status()` on `/root/freellmapi`, and reports update status as `up_to_date` or `update_available` based on git commit comparison.

## Version History

- **v0.3.0** (commit `7f86131`): Multi-language support (EN/ES/FR/PT-BR/ZH-CN), Agnes AI provider, profiles, premium features, analytics, embeddings, major proxy/routing improvements
- Previous: commit `663b3d5` (PR #203)