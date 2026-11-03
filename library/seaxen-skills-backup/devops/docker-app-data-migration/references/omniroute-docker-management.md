# OmniRoute Docker Management

## Overview
OmniRoute (`diegosouzapw/omniroute`) is an AI gateway router. Self-hosted on DietPi at `/mnt/tb/1Apps/omniroute/`.

## Critical: Encryption Keys
OmniRoute auto-generates encryption keys on first boot into `/app/data/server.env`:
- `JWT_SECRET` — signs session tokens
- `STORAGE_ENCRYPTION_KEY` — encrypts API keys in SQLite
- `API_KEY_SECRET` — additional API key encryption

These are persisted in the **data volume** (`/mnt/tb/1Apps/omniroute/data/server.env`). As long as the volume is mounted, keys survive container recreation.

**Gotcha:** If `server.env` is deleted or regenerated, the existing `storage.sqlite` becomes unreadable. All provider configs, API keys, and usage history are lost.

## Update Procedure (Safe)
```bash
# 1. Backup first
bash /mnt/tb/1Apps/omniroute/backup.sh

# 2. Pull + recreate (preserves data volume + keys)
cd /mnt/tb/1Apps/omniroute
docker compose pull
docker compose up -d

# 3. Verify
docker ps --filter name=omniroute --format "table {{.Names}}\t{{.Status}}"
curl -s -o /dev/null -w "%{http_code}" http://localhost:20128/
```

## Known Issues
- **grok-web cookie validation broken** — OmniRoute's `grok-web` provider fails with `Invalid SSO cookie` even with valid cookies. Known issue: [#3063](https://github.com/diegosouzapw/OmniRoute/issues/3063). Workaround: use xAI API key instead.
- **JWT change = old sessions invalid** — After recreating with new keys, all browser sessions become invalid. Users must clear cookies and re-register.
- **"Internal Server Error" on dashboard** — Usually means JWT mismatch. Fix: clear browser cookies, sign up again.

## Architecture
- Image: `diegosouzapw/omniroute:latest`
- Port: 20128 (host networking)
- Data: `/mnt/tb/1Apps/omniroute/data/`
- DB: `/mnt/tb/1Apps/omniroute/data/storage.sqlite`
- Keys: `/mnt/tb/1Apps/omniroute/data/server.env`
- Backup script: `/mnt/tb/1Apps/omniroute/backup.sh`
- Compose: `/mnt/tb/1Apps/omniroute/docker-compose.yml`

## Backup Script
```bash
#!/bin/bash
BACKUP_DIR="/mnt/tb/1Apps/omniroute/backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
cp /mnt/tb/1Apps/omniroute/data/server.env "$BACKUP_DIR/"
cp /mnt/tb/1Apps/omniroute/data/storage.sqlite "$BACKUP_DIR/"
echo "Backup saved to: $BACKUP_DIR"
```
