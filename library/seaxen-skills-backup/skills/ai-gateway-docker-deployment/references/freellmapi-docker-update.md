# FreeLLMAPI — Docker update (DietPi host)

## Layout
| Item | Value |
|------|--------|
| Clone | `/root/freellmapi` |
| Image | `ghcr.io/tashfeenahmed/freellmapi:latest` |
| Compose | `/root/freellmapi/docker-compose.yml` |
| Container | `freellmapi-freellmapi-1` (name may vary) |
| Network | `network_mode: host` |
| Listen | `PORT` from `.env` (this host uses **3055**) |
| Persistent data | named volume `freellmapi-data` |

## Update sequence

```bash
cd /root/freellmapi

# Optional: preserve local compose tweaks (host network, port)
git stash push -m 'local-compose' -- docker-compose.yml
git pull --ff-only origin main
git stash pop || true

docker pull ghcr.io/tashfeenahmed/freellmapi:latest
docker compose up -d --force-recreate
```

If Hermes blocks foreground `compose up`, run recreate in background and verify separately.

## Verify

```bash
docker ps --filter name=freellmapi --format '{{.Names}} {{.Status}}'
curl -sf "http://127.0.0.1:${PORT:-3055}/api/ping"
```

Expect JSON with `"status":"ok"`.

## Pitfalls

- **Local `docker-compose.yml` drift:** Upstream `git pull` may conflict with host-network/port edits. Stash → pull → pop; resolve conflicts keeping host `PORT` if that is how production runs.
- **Not under `/mnt/tb/1Apps`:** FreeLLMAPI lives in `/root/freellmapi` on this machine — do not search only `1Apps` when the user says “update freellmapi”.
- **DB migrations:** New images may run server migrations on boot; allow ~15–30s before declaring failure.