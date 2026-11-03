# Dockerized dashboard reading host-local config, secrets, and data

When a dashboard runs inside Docker but needs to read files that live on the
host (Hermes config, API keys, log directories, SQLite databases), the
container **cannot see them** unless explicitly mounted or passed.

This pattern applies to AceRoute, telemetry dashboards, and any analytics
service that aggregates from host-local sources.

## Pitfall: container can't see ~/.hermes/config.yaml

**Symptom:** The dashboard's `extract_backend_configured` check returns
`False` even though the host has `extract_backend: tavily` in
`~/.hermes/config.yaml`.

**Root cause:** The container's filesystem is isolated. `~/.hermes/` does
not exist inside the container unless mounted.

**Fix — two parts:**

### 1. Mount the config file as a read-only volume

```yaml
# docker-compose.yml
services:
  dashboard:
    volumes:
      - /root/.hermes/config.yaml:/data/hermes-config.yaml:ro
    environment:
      - HERMES_CONFIG_PATH=/data/hermes-config.yaml
```

### 2. Pass API keys as environment variables

The config file may reference env vars (like `TAVILY_API_KEY`) that are set
on the host but not inside the container. Pass them explicitly:

```yaml
    environment:
      - TAVILY_API_KEY=${TAVILY_API_KEY}
      - EXA_API_KEY=${EXA_API_KEY}
```

Or hardcode them if the compose file is private (not in git):

```yaml
      - TAVILY_API_KEY=tvly-dev-***
```

### 3. In the app code, respect HERMES_CONFIG_PATH

```python
config_path = os.getenv(
    "HERMES_CONFIG_PATH",
    os.path.expanduser("~/.hermes/config.yaml"),
)
```

This way the same code works both on the host (default path) and inside the
container (explicit mount path).

## Pitfall: docker compose up -d blocked by terminal tool

The Hermes terminal tool detects `docker compose up -d` as a "long-lived
server/watch process" and blocks it with an error. This happens because the
tool heuristic sees the compose process and assumes it's a daemon.

**Fix:** Use `background=true` with `notify_on_complete=true`:

```
terminal(command="cd /path && docker compose up -d --force-recreate --build", background=true, notify_on_complete=true)
```

Then verify in a separate foreground command:

```
terminal(command="sleep 10 && curl -s http://localhost:PORT/health")
```

## Multi-source data collection pattern

When a dashboard reads from multiple Docker data sources, mount each one
and use env vars for the container-internal paths:

```yaml
volumes:
  # OmniRoute call logs and SQLite DB
  - /mnt/tb/1Apps/omniroute/data:/data/omniroute:ro
  # Hermes debug logs (web_tools_debug_*.json)
  - /root/logs:/data/hermes-logs:ro
  # Hermes config (for backend detection)
  - /root/.hermes/config.yaml:/data/hermes-config.yaml:ro
environment:
  - OMNIROUTE_CALL_LOGS=/data/omniroute/call_logs
  - OMNIROUTE_DB=/data/omniroute/storage.sqlite
  - HERMES_LOGS_DIR=/data/hermes-logs
  - HERMES_CONFIG_PATH=/data/hermes-config.yaml
  - SEARXNG_URL=http://127.0.0.1:8080  # host networking — container can reach host ports
```

**Key insight:** With `network_mode: host`, the container can reach other
host-network services (like SearXNG on port 8080 or OmniRoute on port
20128) directly via `127.0.0.1`. No Docker networking magic needed.

## AceRoute reference implementation

- **Compose:** `/mnt/tb/1Apps/AceRoute/docker-compose.yml`
- **Config mount:** `~/.hermes/config.yaml` → `/data/hermes-config.yaml:ro`
- **Data mounts:** OmniRoute data + Hermes logs as read-only
- **API keys:** Passed as explicit env vars in compose
- **Network:** `network_mode: host` for SearXNG/OmniRoute access
