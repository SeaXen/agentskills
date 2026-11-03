# update.sh — Proper 9router Update Script

## Location
`/mnt/tb/1Apps/9router/update.sh`

## What it does
1. Creates timestamped backup of `data/` directory to `backups/<timestamp>/`
2. Pulls latest `decolua/9router:latest` image
3. Stops and removes existing container
4. Recreates container with:
   - `--network host`
   - `-e PORT=20111` (default, override with `PORT=XXX` env)
   - `-e TZ=Asia/Dhaka` (default, override with `TZ=XXX` env)
   - `-v /mnt/tb/1Apps/9router/data:/app/data`
   - `--restart unless-stopped`
5. Waits up to 30 seconds for `/api/health` endpoint to respond
6. Reports container revision on success

## Usage
```bash
# Default (port 20111, TZ Asia/Dhaka)
bash /mnt/tb/1Apps/9router/update.sh

# Custom port
PORT=20120 bash /mnt/tb/1Apps/9router/update.sh

# Custom timezone
TZ=UTC bash /mnt/tb/1Apps/9router/update.sh
```

## Post-update steps
After `update.sh` completes successfully, apply the usage periods patch:
```bash
python3 /mnt/tb/1Apps/9router/patches/apply-usage-periods.py
```

This patch is **ephemeral** — it modifies files inside the running container and is lost on next `docker pull` + recreate. Re-apply after every update until upstream PR #2361 merges.

## Verification
```bash
# Health check
curl -s http://127.0.0.1:20111/api/health

# Container revision
docker inspect 9router --format '{{index .Config.Labels "org.opencontainers.image.revision"}}'

# Usage page (check extended periods are available)
curl -s http://127.0.0.1:20111/dashboard/usage | grep -o "90D\|180D\|365D\|All"
```

## Script content
```bash
#!/usr/bin/env bash
# Proper 9router update: backup data, pull upstream image, recreate with CasaOS settings.
set -euo pipefail
APP_DIR="/mnt/tb/1Apps/9router"
DATA_DIR="$APP_DIR/data"
IMAGE="decolua/9router:latest"
CONTAINER="9router"
PORT="${PORT:-20111}"
TZ="${TZ:-Asia/Dhaka}"

ts="$(date +%Y%m%d_%H%M%S)"
bk="$APP_DIR/backups/$ts"
mkdir -p "$bk"
echo "==> Backup to $bk"
cp -a "$DATA_DIR" "$bk/"
cp "$APP_DIR/docker-compose.yml" "$bk/" 2>/dev/null || true

echo "==> Pull $IMAGE"
docker pull "$IMAGE"

echo "==> Recreate container (host network, port $PORT)"
docker stop "$CONTAINER" 2>/dev/null || true
docker rm "$CONTAINER" 2>/dev/null || true
docker run -d \
  --name "$CONTAINER" \
  --restart unless-stopped \
  --network host \
  -e DATA_DIR=/app/data \
  -e HOSTNAME=0.0.0.0 \
  -e PORT="$PORT" \
  -e TZ="$TZ" \
  -v "$DATA_DIR:/app/data" \
  "$IMAGE"

for i in $(seq 1 30); do
  if curl -sf "http://127.0.0.1:${PORT}/api/health" >/dev/null; then
    rev="$(docker inspect "$CONTAINER" --format '{{index .Config.Labels "org.opencontainers.image.revision"}}')"
    echo "==> OK health — revision $rev"
    exit 0
  fi
  sleep 1
done
echo "==> WARN: health check failed on :$PORT" >&2
exit 1
```

## First seen
2026-07-20: Used successfully to update 9router from previous version to revision `79918c7830695bbca4a45c9fea4a42c3e9fd73d1`.