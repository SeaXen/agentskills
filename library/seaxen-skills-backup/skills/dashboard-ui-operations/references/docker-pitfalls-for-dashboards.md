# Docker Pitfalls for Self-Hosted Dashboards

## Build caching: `COPY . .` layer reuse

When files change on the host but Docker uses a cached `COPY . .` layer, the container runs **old code**. The build output says `---> Using cache` for the COPY step even though source files changed.

**Fix:** `docker compose build --no-cache` followed by `docker compose up -d --force-recreate`.

`docker compose up -d --force-recreate --build` alone may NOT fix this — Docker's layer cache can still reuse the COPY step if the build context hash hasn't changed (e.g., file timestamps in sub-second builds, or `.dockerignore` excluding changed files).

**Verification pattern:**
```bash
# Check if container has the new code
docker exec <container> grep -n '<expected_new_code>' /app/<file>.py
# If empty → cached build, redo with --no-cache
```

## env_file does NOT reload on `restart`

`docker compose restart` does NOT re-read `.env` files. The container keeps its original env vars.

**Fix:** `docker compose up -d --force-recreate` to recreate the container with fresh env.

**Verification:**
```bash
docker exec <container> printenv <VAR_NAME>
```

## Healthcheck requires curl in slim images

`python:3.11-slim` and similar don't include `curl`. Docker healthcheck using `curl -f` will fail silently.

**Fix:** Add to Dockerfile:
```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*
```

## Host networking + Docker env vars

When using `network_mode: host`, the container shares the host's network but NOT its environment variables. Env vars must still be passed via `environment:` or `env_file:` in docker-compose.yml.

## Volume mounts for config detection

When a container needs to detect host-side config (e.g., Hermes `~/.hermes/config.yaml`), mount it explicitly:
```yaml
volumes:
  - /root/.hermes/config.yaml:/data/hermes-config.yaml:ro
environment:
  - HERMES_CONFIG_PATH=/data/hermes-config.yaml
```
The container cannot access host paths unless mounted.
