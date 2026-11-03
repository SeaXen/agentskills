# Docker Compose Pitfalls for Dashboard Deployments

## Restart does NOT reload .env files

`docker compose restart` only stops/starts the container process. It does NOT re-read:
- `.env` file
- `env_file:` directives
- Variable substitutions in `docker-compose.yml`

**Implication**: After changing API keys, passwords, or config in `.env`, you MUST use:
```bash
docker compose up -d --force-recreate
```
Not `docker compose restart`.

**Verification**: Check the container actually has the new value:
```bash
docker exec <container> printenv KEY_NAME
```

## Build cache uses stale COPY layers

When `COPY . .` in the Dockerfile uses a cached layer (same file sizes/metadata), the container gets OLD code even after `docker compose up -d --force-recreate --build`.

**Symptoms**: New endpoints return 404, new features missing, old bugs persist.

**Fix**: Force full rebuild:
```bash
docker compose build --no-cache
docker compose up -d --force-recreate
```

**Verification**: Check a new file/endpoint exists inside the container:
```bash
docker exec <container> grep -n 'new_endpoint' /app/app.py
```

## Healthcheck requires curl in slim images

Docker `python:*-slim` and `debian:*-slim` images don't include `curl`.
Add to Dockerfile:
```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lib/*
```

Without this, the healthcheck silently fails and container shows `unhealthy` forever.

## Foreground timeout trap

`docker compose up -d --force-recreate` sometimes triggers the Hermes terminal tool's "long-lived server/watch process" detection. Use `background=true` with `notify_on_complete=true`:
```bash
# This gets blocked:
docker compose up -d --force-recreate

# This works:
terminal(command="cd /path && docker compose up -d --force-recreate 2>&1", background=true, notify_on_complete=true)
```

Alternatively, wrap in a script that exits after compose finishes.
