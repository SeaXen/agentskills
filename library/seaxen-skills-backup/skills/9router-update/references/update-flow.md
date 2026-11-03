# update.sh — Line-by-line annotated walkthrough

This is the canonical 9router update entry point. Lives at
`/mnt/tb/1Apps/9router/update.sh`. **Never** call `docker pull && docker stop && docker run` by hand — the hand-rolled approach drifts env / volumes / network_mode from the compose file and breaks backups.

## Full source

```bash
#!/usr/bin/env bash
# Proper 9router update: backup data, pull upstream image, recreate using
# docker-compose.yml as the single source of truth for env/volume/network.
# Then re-apply the usage-periods UI/API patch (lost on every image recreate).
set -euo pipefail
APP_DIR="/mnt/tb/1Apps/9router"
DATA_DIR="$APP_DIR/data"
IMAGE="decolua/9router:latest"
CONTAINER="9router"
COMPOSE="$APP_DIR/docker-compose.yml"

ts="$(date +%Y%m%d_%H%M%S)"
bk="$APP_DIR/backups/$ts"
mkdir -p "$bk"
echo "==> Backup to $bk"
cp -a "$DATA_DIR" "$bk/"
cp "$COMPOSE" "$bk/" 2>/dev/null || true

echo "==> Pull $IMAGE"
docker pull "$IMAGE"

echo "==> Recreate container (host network, env from docker-compose.yml)"
docker stop "$CONTAINER" 2>/dev/null || true
docker rm   "$CONTAINER" 2>/dev/null || true
docker compose -f "$COMPOSE" up -d --force-recreate --remove-orphans

echo "==> Re-apply usage-periods patch (lost on every image recreate)"
if [ -f "$APP_DIR/patches/apply-usage-periods.py" ]; then
  python3 "$APP_DIR/patches/apply-usage-periods.py"
else
  echo "    WARN: $APP_DIR/patches/apply-usage-periods.py not found" >&2
fi

PORT="$(grep -E '^\s*PORT:' "$COMPOSE" | head -1 | sed -E 's/.*PORT:\s*"?([0-9]+).*/\1/')"
PORT="${PORT:-20111}"

for i in $(seq 1 30); do
  if curl -sf "http://127.0.0.1:${PORT}/api/health" >/dev/null; then
    rev="$(docker inspect "$CONTAINER" --format '{{index .Config.Labels "org.opencontainers.image.revision"}}')"
    echo "==> OK health on :$PORT — revision $rev"
    echo "==> Hard-refresh browser (Ctrl+Shift+R) on /dashboard/usage"
    exit 0
  fi
  sleep 1
done
echo "==> WARN: health check failed on :$PORT" >&2
exit 1
```

## Walkthrough

| Line | Why it matters |
|------|---------------|
| `set -euo pipefail` | Abort on any error, undefined var, or pipe failure. Critical for an update script — never silently half-run. |
| `APP_DIR=/mnt/tb/1Apps/9router` | Hard-coded path. If your install is elsewhere, edit this constant or use the skill's `--app-dir` flag if you wrap it. |
| `IMAGE=decolua/9router:latest` | Always pull `latest`. Do NOT pin a specific tag here — the whole point is to track upstream. |
| `CONTAINER=9router` | Hard-coded. The patch script (`apply-usage-periods.py`) also assumes this name. |
| `cp -a data/ $bk/` | `-a` preserves ownership, perms, symlinks. Backs up the SQLite DB (`storage.sqlite`), env (`server.env`), and any uploaded files. |
| `cp docker-compose.yml $bk/` | Captures the runtime config in case you need to diff after the update. |
| `docker pull` | Can take 2–10 min for a 2.6 GB image on a slow link. `set -e` means a pull failure aborts the whole script — safer than continuing with the old image. |
| `docker stop || true; docker rm || true` | Idempotent: the `|| true` prevents failure when the container is already gone. |
| `docker compose up -d --force-recreate --remove-orphans` | `--force-recreate` destroys the old container even if the config is unchanged. `--remove-orphans` cleans up any stale containers from previous broken runs. **This is the single source of truth for env, volumes, and host network.** |
| `python3 apply-usage-periods.py` | The reason this whole skill exists. Without this, the new image has stock 7d/30d/60d period options and the user loses 90d/180d/365d/all. |
| `PORT="$(grep …)"` | Reads the port from the compose file so the script doesn't hard-code 20111. Falls back to 20111 if the compose file doesn't have it. |
| `curl -sf /api/health` | `-f` fails on HTTP errors, so a 5xx still aborts the loop. The container's `/api/health` is a 1-line `res.json({ok:true})`. |
| `revision $rev` | Pulled from the OCI image label. Lets the user confirm the digest via `docker inspect`. |
| `exit 1` at the end if health never came up | Forces the calling shell to see a non-zero exit code. Don't `|| true` this — a failed health check is a failed update. |

## What it does NOT do (and why)

- It does **not** edit `docker-compose.yml`. The image tag, env, and volumes stay stable across updates. If upstream announces a new required env var, you add it manually.
- It does **not** clean up old Docker images. `docker image prune` is left to the operator.
- It does **not** rotate the `server.env` API keys. The user's API keys survive in `$bk/data/server.env` if needed.
- It does **not** update the local git checkout at `/mnt/tb/1Apps/9router-upstream`. That's a separate concern (read-only reference).

## Failure exit codes

- `0` — update succeeded, health endpoint reachable within 30 s.
- `1` — health endpoint never returned `{"ok":true}` within 30 s. Container is up but app may have crashed; check `docker logs 9router --tail 100`.
- Non-zero from `set -e` — any earlier step failed (pull, backup, recreate, patch). The script aborts at the first failure, leaving the previous version running if recreate hadn't happened yet.
