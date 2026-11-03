# Docker compose redeploy (MedSea + TradingX pattern)

## Problem
Repeated `docker build -t foo:latest` + `docker run` without fixed names leaves **`<none>:<none>`** images and **random container names** (`frosty_robinson`, etc.).

## User rule (Dr. Sagar)
- **Do not** `docker container prune` or bulk-remove stopped containers unless the user explicitly asks.
- Safe cleanup: only drop the **previous `image:latest` ID** after a successful redeploy **if** nothing still references it (`docker image rm <old_id>` may fail — leave it).

## MedSea (`/mnt/tb/Sea-knowledge/#MedSea`)
- `docker-compose.yml`: `image: medsea-site:latest`, `container_name: medsea`, **ports `8855:80`** (nginx listens 80 inside).
- `scripts/redeploy.sh`: compose build → migrate legacy `docker run` medsea (stop/rm **only** name=medsea) → `compose up -d --force-recreate` → optional `docker image rm` previous latest ID.
- Full rebuild ~5+ min (large `site/`); use `terminal` background + notify or run on host.

## TradingX (`/mnt/tb/1Apps/Tradingx`)
- Host `next build` first (`.next/standalone/server.js` required).
- `bash scripts/redeploy.sh` — same old-image cleanup pattern.
- **Deprecated:** `Dockerfile.fast` (chained `FROM tradingx:latest` → extra dangling layers).

## Verify
```bash
docker inspect medsea --format '{{index .Config.Labels "com.docker.compose.service"}}'  # medsea
docker port medsea   # 80/tcp -> 0.0.0.0:8855
curl -sS -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8855/
```

## Audit dangling (no prune)
- `~/.hermes/scripts/docker-dangling-audit.sh` — lists `<none>` images and which containers still reference them.
- `~/.hermes/scripts/docker-dangling-free.sh` — dry report; `--remove-holders` removes **only** exited containers whose image is untagged and whose name is **not** in the protect list (`medsea`, `tradingx`, `mnfst-`, `jellyfin`, `portainer`, …).

**User rule:** do **not** `docker container prune` unless explicitly asked. To free old `<none>` layers pinned by junk one-off names (`frosty_robinson`, `angry_bouman`, …), remove those **specific** exited containers, then `docker image prune -f`.

**Ghost refs:** if `docker image inspect <id>` says "No such image" but exited containers still show bare image IDs, `docker rm <container>` reclaims writable layers (~1 GB typical) without touching running stacks.

## Manifest (`/mnt/tb/1Apps/manifest`)
Add `restart: unless-stopped` on **both** `manifest` and `postgres`. Clean exit (`Exited (0)` + postgres "fast shutdown") = someone ran `compose down` / stop, not OOM. After host reboot, `RestartPolicy=no` leaves **2099** down until manual `docker compose up -d` or `docker start mnfst-postgres-1 mnfst-manifest-1`.

## FreeLLMAPI (`/root/freellmapi`)

When LAN clients cannot reach bridge-published ports, set **`network_mode: host`**, remove `ports:`, bind **`PORT`** (e.g. **3055**) and **`HOSTNAME=0.0.0.0`**. Healthcheck must read `process.env.PORT`. Verify: `curl http://127.0.0.1:3055/api/ping` and `ss` shows **node** on `*:3055` (not `docker-proxy`).