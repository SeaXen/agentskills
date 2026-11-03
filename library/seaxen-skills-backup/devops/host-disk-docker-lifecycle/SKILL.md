---
name: host-disk-docker-lifecycle
description: Analyze SSD/HDD pressure on dual-disk Docker hosts, reclaim space safely (images/caches/Hermes without killing live stacks), and fully tear down a self-hosted app (compose + install dir + Hermes hooks). Use when the user asks for storage analysis, disk cleanup, docker prune, SSD full, or remove/uninstall an app and its containers.
tags: [docker, disk, ssd, reclaim, prune, teardown, dietpi, containerd, storage]
related_skills: [docker-safe-update, docker-app-data-migration, linux-host-performance-diagnosis]
---

# Host Disk + Docker Lifecycle

Class skill for **storage analysis**, **safe reclaim**, and **full app teardown** on self-hosted Docker boxes (especially DietPi: small SSD root + large HDD `/mnt/tb`).

Companion to `docker-safe-update` (update/backup rules) and `docker-app-data-migration` (move bind data to HDD). This skill owns **cleanup and uninstall** flows.

## When to use

- "analyze my SSD / disk / storage"
- "clean up / reclaim space / prune docker"
- "remove X all files and docker" / uninstall a self-hosted app
- Root filesystem climbing toward full while `/mnt/tb` still has room

## Host model (this server)

| Mount | Device | Holds | Pressure |
|-------|--------|-------|----------|
| `/` | ~120G SSD | OS, `/var/lib/containerd`, `/root`, Hermes | **Usual bottleneck** |
| `/mnt/tb` | ~1TB HDD | `/mnt/tb/1Apps/*` app data, downloads, big backups | Bulk |

**Fact:** Docker **image layers live on SSD** even when app data is on HDD. Moving "the app" to HDD does not free image layers — reclaim images/caches on root, or relocate Docker data-root (global, rare).

Default new app install path: `/mnt/tb/1Apps/<appname>/`.

## Part A — Storage analysis (always first)

```bash
df -hT /
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT,MODEL,ROTA
du -xh --max-depth=1 / 2>/dev/null | sort -hr | head -15
du -xh --max-depth=1 /var/lib /root /root/.hermes 2>/dev/null | sort -hr | head -25
docker system df
docker images --format 'table {{.Repository}}:{{.Tag}}\t{{.Size}}\t{{.ID}}\t{{.CreatedSince}}'
docker ps -a --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}'
smartctl -H /dev/sda 2>/dev/null
```

Report **SSD and HDD separately**. Lead with free/used and top consumers. Distinguish:

1. containerd/images on SSD  
2. Hermes (`state.db`, snapshots, mnemosyne)  
3. regenerable caches (`~/.npm`, playwright, pip/uv)  
4. HDD bulk (`2dl`, hermes-backups, etc.)

## Part B — Safe reclaim tiers

### Hard rules (user corrections)

1. **List candidates with size/age before any prune.** Default is no.
2. After a full analysis, user **"okk do" / "do it"** authorizes the **named safe plan only** — not silent `container prune` / `volume prune` / `system prune -a`.
3. Never remove images still referenced by running **or** kept stopped containers unless the user named those apps for deletion.
4. After cleanup: `df -h /`, container count/status, before→after free GB.
5. Shared layers: trust `df -h /` over summing image tag sizes.

### Tier A — low risk (after list + OK)

```bash
docker image prune -f          # dangling only — NO -a
docker builder prune -af       # build cache
npm cache clean --force
rm -rf ~/.npm/_cacache ~/.npm/_npx
rm -rf ~/.cache/pip ~/.cache/uv ~/.cache/ms-playwright
apt-get clean
# journal only if on disk (often tmpfs here)
journalctl --vacuum-time=3d 2>/dev/null || true
```

### Tier B — unused image tags

Compare `docker ps -a` image set vs `docker images`. Remove **explicit** unused tags (old OmniRoute hotfixes, test images, unused tools). Skip any ID still attached to a container (including digest-pinned postgres).

### Tier C — Hermes on SSD

| Target | Action |
|--------|--------|
| Huge `~/.hermes/state.db` | `hermes sessions optimize-storage` (needs ~DB-size free for VACUUM; resumable) |
| `state-snapshots/` | Delete old pre-update snapshots only with OK |
| `mnemosyne/backups/` | Trim by policy |
| `/root/*-pr` worktrees | Optional; ask if uncommitted work possible |

### Tier D — require explicit per-item OK

- `docker container prune`, `volume prune`, `system prune -a`
- Deleting live `/mnt/tb/1Apps/*` data
- Stopping/removing production containers as "cleanup"

### Observed reclaim (2026-07-22)

SSD ~70%/32G free → after Tier A–C (unused tags, builder, caches, one 2.8G state-snapshot): **~54%/48G free**; live containers stayed up. containerd ~25G→~15G.

Details: `references/safe-cleanup-prune-walkthrough.md`.

## Part C — Full app teardown

When user wants the product **gone** (not prune):

1. **Discover** containers, images, volumes, networks, compose `working_dir` label, `/mnt/tb/1Apps/<app>`, Hermes plugin/cron/scripts.
2. **`docker compose down -v --remove-orphans`** from workdir if wiping data; else without `-v` if keeping DB (rare for full remove).
3. **`docker rmi`** app image; dependency images only if unreferenced.
4. **`rm -rf`** install dir + obvious clones/worktrees. **Do not** wipe unrelated filename collisions (medical "manifestation", `MANIFEST.in`, Next build manifests).
5. **Hermes:** remove plugin, scripts, local history DB/logs/config; edit `cron/jobs.json` after `jobs.json.bak-*`; clear `cron/output/<job_id>/`.
6. **`cd /root`** before next commands if shell cwd was the deleted tree (`getcwd` fails otherwise).
7. **Verify** no containers/images, port free, other stacks still up; durable memory "removed on DATE"; tell user about Cloudflare/proxy leftovers.

Full checklist + Manifest/mnfst worked example: `references/full-app-teardown-checklist.md`.

## Part D — What not to capture as permanent "broken"

- Transient prune reclaim 0B when already clean  
- Environment one-offs  

Prefer procedures and verification over "tool X does not work."

## Related skills

- `docker-safe-update` — backup before recreate; prune listing rules (manual skill may duplicate list-first rule)
- `docker-app-data-migration` — move bind mounts to HDD; does not free image layers
- `linux-host-performance-diagnosis` — CPU/thermal, not disk
- `hermes-sessions-prune-archive` — session DB content prune (when installed)

## References

- `references/safe-cleanup-prune-walkthrough.md` — analysis commands, tiers, DietPi notes
- `references/full-app-teardown-checklist.md` — uninstall checklist + Manifest removal example
