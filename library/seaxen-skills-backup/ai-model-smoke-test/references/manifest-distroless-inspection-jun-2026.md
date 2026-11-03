---
name: manifest-distroless-inspection
parent: ai-model-smoke-test
---

# Manifest distroless container inspection

Manifest self-hosted image (`manifestdotbuild/manifest`) is **distroless** — no shell, no `ls`, no `grep`. Source is compiled/transpiled and not present in the container.

## What this means

- **No in-place patching** — can’t edit `/app/server/api/history.go` because it doesn’t exist as source.
- **No runtime inspection** — can’t `grep` or `find` inside the container.
- **No shell tools** — `docker exec mnfst-manifest-1 ls` → `OCI runtime exec failed: exec failed: unable to start container process: exec: "ls": executable file not found in $PATH`.

## Workarounds

### 1. Fork + rebuild

```bash
git clone https://github.com/mnfst/manifest
cd manifest
# edit source
docker build -t my-manifest .
docker compose up -d
```

### 2. Proxy the API

Hermes cron job that polls `/api/v1/history` and stores 90+ days in SQLite/Postgres:

```bash
0 3 * * * curl -sS "http://127.0.0.1:2099/api/v1/history?limit=1000" -H "Authorization: Bearer *** | sqlite3 /mnt/tb/manifest/history.db ".import /dev/stdin history"
```

Query 90+ days:

```sql
SELECT * FROM history WHERE created_at > datetime('now', '-90 days');
```

### 3. Postgres direct

```bash
docker exec mnfst-postgres-1 psql -U manifest -c "SELECT COUNT(*) FROM messages WHERE created_at > NOW() - INTERVAL '90 days';"
```

## See also

- `manifest-self-hosted-docker-lan-jun-2026.md` — Docker Compose on LAN
- `manifest-auto-routing-jun-2026.md` — `/v1/models` behavior