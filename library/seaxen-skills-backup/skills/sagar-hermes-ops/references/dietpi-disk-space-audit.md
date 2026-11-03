# DietPi disk space audit (SSD vs HDD)

Dr. Sagar's server: **system SSD** `/` (~110G) + **bulk HDD** `/mnt/tb` (~916G). Docker junk cleanup does **not** fix most pressure — check both disks.

## Quick commands

```bash
df -hT / /mnt/tb
docker system df
du -xh --max-depth=1 /root 2>/dev/null | sort -hr | head -12
du -xh --max-depth=1 /mnt/tb 2>/dev/null | sort -hr | head -15
du -xh --max-depth=1 /var/lib 2>/dev/null | sort -hr | head -8
```

## Typical SSD (`/` ~60G used)

| Path | What |
|------|------|
| `/var/lib/containerd` | **~13G** — all Docker image layers |
| `/root/.cache` | pip/npm/build caches (~8G) |
| `/root/.hermes` | sessions, plugins, Mnemosyne (~8G) |
| `/root/.npm` | npm cache (~2–3G) |
| `/usr` | packages (~13G) |

Largest **images**: `medsea-site` (~3G), `metube`, `jellyfin`, `nexterm`, `cloudflared-web` (~1G each). Container writable layers are usually **&lt;500MB** after junk cleanup.

Safe SSD reclaims (ask before deleting `.hermes` data): `uv cache clean --force`, `npm cache clean --force`, remove regeneratable `/root/.cache` dirs (go-build, ms-playwright, puppeteer, camoufox); `pip cache purge` often no-op (PEP 668 / cache disabled on this host).

## Typical HDD (`/mnt/tb` ~150G used)

| Path | What |
|------|------|
| `hermes-backups/#plain` | **~8× ~7.4G** cron plain snapshots — **biggest win** if pruning to keep 2–3 |
| `.tmp-hermes-backup` | Staging leak (**~32G** possible) — delete only after confirming encrypted copies exist |
| `2dl`, `Syn MD 26`, `Sea-knowledge`, `drbeen` | user content — do not delete without explicit ask |

See `hermes-backup-watchers` → `references/staging-dir-leak.md` for `.tmp-hermes-backup` cleanup pattern.

## Misleading signals

- `docker system df` **Images reclaimable 0B** while disk feels full → check **HDD backups** and **`/root` caches**, not dangling images.
- `<none>` postgres digest image with 1 container → normal when compose pins `postgres:16-alpine@sha256:...`.