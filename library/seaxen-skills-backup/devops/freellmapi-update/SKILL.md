---
name: freellmapi-update
description: Update self-hosted freellmapi Docker with backup/recreate.
version: 0.1.0
author: Hermes
platforms: [linux]
metadata:
  hermes:
    tags: [freellmapi, self-hosted, docker, update]
    prereqs: [docker]
    category: devops
---

# freellmapi Update — Verified Procedure

Update a self-hosted freellmapi Docker deployment on host network. No custom patches — safe backup/pull/recreate/verify.

## When to Use
- New upstream image available (`ghcr.io/tashfeenahmed/freellmapi:latest` digest changed)
- User asks to update freellmapi

## Inputs
- Container: `freellmapi-freellmapi-1`
- App dir: `/root/freellmapi`
- Compose: `/root/freellmapi/docker-compose.yml` (host network, port 3055)
- Data: `/mnt/tb/1Apps/freellmapi/data` (bind mount)
- Env: `.env` (bind mount)
- Backups: `/root/freellmapi/backups/<YYYYMMDD_HHMMSS>_data` + `_env`

## Step-by-Step

### 1. Pre-flight
```bash
cd /root/freellmapi
docker images ghcr.io/tashfeenahmed/freellmapi:latest --format "{{.ID}}\t{{.CreatedSince}}"
```

### 2. Backup
```bash
ts=$(date +%Y%m%d_%H%M%S)
mkdir -p backups
cp -a data backups/${ts}_data 2>/dev/null || echo "data dir doesn't exist yet"
cp .env backups/${ts}_env 2>/dev/null || echo ".env doesn't exist"
```

### 3. Pull + Recreate
```bash
docker pull ghcr.io/tashfeenahmed/freellmapi:latest
docker compose up -d --force-recreate --remove-orphans
```

### 4. Verify (wait 15-20s for healthcheck)
```bash
docker ps --filter name=freellmapi --format "{{.Names}}\t{{.Status}}"
docker images ghcr.io/tashfeenahmed/freellmapi:latest --format "{{.ID}}\t{{.CreatedSince}}"
curl -s "http://127.0.0.1:3055/api/ping" | python3 -c "import sys,json; print(json.load(sys.stdin))"
```

**Expected:** Container `Up N minutes (healthy)`, new image digest, `{"status":"ok",...}`

## Failure Recovery
```bash
docker compose down
docker compose up -d  # uses cached image
```

## Notes
- Host networking: no port mapping changes needed
- Port 3055 from compose `PORT` env
- Healthcheck in compose hits `/api/ping` every 30s
- Data in `/mnt/tb/1Apps/freellmapi/data` persists via bind mount

## Verification Script
```bash
bash /root/.hermes/skills/freellmapi-update/scripts/verify-freellmapi.sh
```