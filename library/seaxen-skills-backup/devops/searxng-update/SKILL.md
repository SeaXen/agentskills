---
name: searxng-update
description: Update self-hosted SearXNG Docker with backup/recreate.
version: 0.1.0
author: Hermes
platforms: [linux]
metadata:
  hermes:
    tags: [searxng, self-hosted, docker, update]
    prereqs: [docker, python3]
    category: devops
---

# SearXNG Update — Verified Procedure

Update a self-hosted SearXNG Docker deployment on host network. No custom patches — just safe backup/pull/recreate/verify.

## When to Use
- New upstream image available (`ghcr.io/searxng/searxng:latest` digest changed)
- User asks to update SearXNG

## Inputs
- Container: `searxng`
- App dir: `/mnt/tb/1Apps/searxng`
- Compose: `/mnt/tb/1Apps/searxng/docker-compose.yml` (host network, port 8080)
- Data: `./data` (bind mount)
- Config: `./config` (bind mount)
- Backups: `/mnt/tb/1Apps/searxng/backups/<YYYYMMDD_HHMMSS>_data` + `_config`

## Step-by-Step

### 1. Pre-flight
```bash
cd /mnt/tb/1Apps/searxng
docker images ghcr.io/searxng/searxng:latest --format "{{.ID}}\t{{.CreatedSince}}"
```

### 2. Backup
```bash
ts=$(date +%Y%m%d_%H%M%S)
mkdir -p backups
cp -a data backups/${ts}_data
cp -a config backups/${ts}_config
```

### 3. Pull + Recreate
```bash
docker pull ghcr.io/searxng/searxng:latest
docker compose up -d --force-recreate --remove-orphans
```

### 4. Verify (wait 3-5s, then)
```bash
docker ps --filter name=searxng --format "{{.Names}}\t{{.Status}}"
docker images ghcr.io/searxng/searxng:latest --format "{{.ID}}\t{{.CreatedSince}}"
curl -s "http://127.0.0.1:8080/search?q=test&format=json" | python3 -c "
import sys,json; d=json.load(sys.stdin)
print(f'Results: {len(d.get(\"results\",[]))}, Engines: {sorted(set(r[\"engine\"] for r in d.get(\"results\",[])))}')
"
```

**Expected:** Container `Up N minutes`, new image digest, 30+ results from multiple engines.

## Failure Recovery
```bash
docker compose down
docker compose up -d  # uses cached image
```

## Notes
- Host networking: no port mapping changes needed
- `SEARXNG_BASE_URL` in compose uses port 8080
- Settings in `./config/settings.yml` persist via bind mount
- OmniRoute must have `OMNIROUTE_ALLOW_PRIVATE_PROVIDER_URLS=true` for local SearXNG

## Verification Script
```bash
bash /root/.hermes/skills/searxng-update/scripts/verify-searxng.sh
```