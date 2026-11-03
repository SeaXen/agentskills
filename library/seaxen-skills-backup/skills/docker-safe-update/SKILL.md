---
name: docker-safe-update
description: Safe Docker container update pattern — never lose data, keys, or config
tags: [docker, update, backup, compose]
---

# Docker Safe Update Pattern

## Golden Rule
NEVER `docker stop` + `docker rm` + `docker run` without preserving state first.

## Safe Update Steps (universal)

### 1. Backup BEFORE touching anything
```bash
# Find the data volume
docker inspect <container> --format '{{json .Mounts}}' | jq .
# Backup data volume + any env files
cp -r /path/to/volume /path/to/backups/$(date +%Y%m%d_%H%M%S)
```

### 2. Check current run config
```bash
docker inspect <container> --format '{{json .Config.Env}}' | jq .
docker inspect <container> --format '{{json .HostConfig.PortBindings}}' | jq .
docker inspect <container> --format '{{json .HostConfig.NetworkMode}}' | jq .
docker inspect <container> --format '{{json .Mounts}}' | jq .
```

### 3. Check whether an update actually exists
For public images, compare the **local RepoDigest** to the **remote manifest digest** before restarting anything.

```bash
# Local digest currently installed
docker image inspect <image>:<tag> --format '{{json .RepoDigests}}'

# Remote digest published upstream
docker buildx imagetools inspect <image>:<tag> --format '{{json .Manifest.Digest}}'
```

Interpretation:
- If the digests match: the image is already up to date.
- If they differ: an update is available.
- If the running container uses `image: repo:tag@sha256:...`, the stack is **digest-pinned**. Pulling may update the tag remotely, but your container will stay on the pinned digest until the compose file is changed.

For compose-managed containers, also inspect the running container labels to find the real project directory before updating:

```bash
docker inspect <container> --format 'project={{index .Config.Labels "com.docker.compose.project"}} workdir={{index .Config.Labels "com.docker.compose.project.working_dir"}} config={{index .Config.Labels "com.docker.compose.project.config_files"}} service={{index .Config.Labels "com.docker.compose.service"}}'
```

This matters on hosts that mix hand-managed stacks and dashboard-managed stacks (e.g. CasaOS), where the compose files may live under `/var/lib/casaos/apps/...` instead of your usual app directory.

### 4. Pull new image WITHOUT stopping anything
```bash
docker pull <image>:<tag>
```

### 5. Recreate safely

**If docker-compose.yml exists:**
```bash
cd /path/to/compose && docker compose up -d --force-recreate
```

**Hermes agent pitfall:** Foreground `docker compose up -d` or `docker compose pull && docker compose up -d` may be hard-rejected as starting a long-lived process. Recreate still finishes in seconds — run it in background if needed, then verify with a follow-up `docker ps` / health `curl`. Do not skip recreate because the first foreground invocation was blocked.

**Another Hermes runtime pitfall:** after starting a background compose update, `process wait` may time out while layers are still downloading or extracting. That is not a failed update by itself. Poll or wait again, then verify container status and health before concluding anything is broken.

### PITFALL: `docker compose restart` does NOT reload `env_file`

If you edit an entry under `env_file:` in `docker-compose.yml` (e.g. `data/server.env`), then run `docker compose restart`, the container comes back up with the **old** env vars. The same is true for `docker stop` + `docker start` on a single container.

`Config.Env` in the container spec is baked at **create** time, not start time. To make `env_file` edits take effect you must either:

- `docker compose up -d --force-recreate --no-deps <service>` (preferred — also handles image updates)
- or `docker rm -f <container>` then `docker compose up -d` (manual but works when compose refuses the recreate)

**Quick symptom checklist** (use when "I added the env var but the app doesn't see it"):

```bash
# 1. Is the new var in the *file*?
grep MY_NEW_VAR /path/to/server.env
# 2. Did the container get recreated?
docker inspect <container> --format '{{.State.StartedAt}}'   # compare to before edit
# 3. Is the var actually in PID 1's environ?
docker exec <container> sh -c 'cat /proc/1/environ | tr "\0" "\n" | grep MY_NEW_VAR'
# 4. If 1=yes, 2=no: run recreate. If 2=yes but 3=no: the file the container
#    mounts is not the one you edited (path mismatch on host vs bind mount).
```

**Working real-world fix:** when foreground `docker compose up -d --force-recreate` is hard-rejected as "long-lived process", use `docker rm -f <container>` first, then `docker compose up -d --no-deps`. Recreate finishes in seconds — run it in background and verify with `docker ps` / health `curl`. Do not skip recreate just because the first invocation was blocked.

This is especially nasty on hosts that use a long-lived process model (containers started months ago) — `StartedAt` may report a date that matches the original boot, proving the var was never loaded even though the env file was edited.

**If plain docker run (no compose):**
```bash
docker stop <container> && docker rm <container>
docker run -d --name <container> <same flags as before> <image>:<tag>
```

### 5. Verify
```bash
docker ps --filter name=<container> --format "table {{.Names}}\t{{.Status}}"
# Check health endpoint if available
# Check data still present
# Check logs for errors
docker logs --tail 20 <container>
```

## CRITICAL Rules
- **ALWAYS** backup data volume + env/config files first
- **NEVER** assume volumes persist without compose — plain `docker run` volumes survive `docker rm` only if named volumes, bind mounts are fine
- **NEVER** delete containers that store encryption keys without extracting keys first
- If the container auto-generates secrets on first run, those secrets are GONE if you recreate without the volume
- Prefer `docker compose` over plain `docker run` for anything persistent
- After update, verify: container healthy, data intact, keys present, app responds

## Backup Retention
Keep only 2 most recent backups per app. Auto-delete older ones on each backup run. Old backups are waste after a successful update.

## TB gateway apps (use app `update.sh` or skill)

| App | Update | After pull |
|-----|--------|------------|
| 9router | `/mnt/tb/1Apps/9router/update.sh` | `patches/apply-usage-periods.py` until upstream merges |
| OmniRoute | `/mnt/tb/1Apps/omniroute/update.sh` | Confirm `env_file` / `STORAGE_ENCRYPTION_KEY`; re-test relays if used |
| hermes-telemetry | Skill **`learnables/hermes-telemetry`** § TB update runbook: backup → `git fetch/merge origin/main` → Hermes venv pytest → gateway restart **outside** gateway | Data in `~/.hermes/telemetry/` |

See `9router-self-hosted`, `omniroute-update`, **`learnables/hermes-telemetry`** (not `devops/`).

## PITFALL: Data-Loss Incident (2026-06-29, OmniRoute)
**What happened:** `docker stop` + `docker rm` was run without backing up encryption keys first. New container auto-generated new keys. Old database encrypted with old keys became unreadable. Then `data/` was wiped trying to "fix" it. All providers, usage history, and settings were permanently lost.

**Root cause:** Destructive operations performed without backup, followed by escalation (wiping data) instead of rollback.

**Lesson:** 
- ALWAYS backup `server.env` (or equivalent) BEFORE `docker rm`
- If a container auto-generates secrets, those secrets live INSIDE the container or volume — removing the container without extracting them = permanent loss
- When recovery goes wrong, STOP and restore from backup. Never escalate to "wipe and start fresh" unless the user explicitly agrees to data loss

## Backup Retention
- Keep only the **last 2 backups** max — user does not want old junk piling up
- Auto-delete older backups on each new backup run

## References
- `references/docker-image-update-checks.md` — digest-based method to prove whether a public image is actually outdated, how to detect digest-pinned services, and how to find the real compose workdir from container labels.
- `references/safe-cleanup-prune-walkthrough.md` — pre-cleanup listing checklist and accepted-flow pattern for `docker container/image/volume prune`. Required reading before any prune.

## PITFALL: Pruning without listing first (user correction 2026-07-11)

Running `docker container prune -f` removed 13 stopped containers including long-lived tools (jellyfin, plex, termix, ttydbridge, big-bear-dockpeek) without listing them first. Images mostly survived but the user was unhappy — they had to reverse-engineer the work to find out what was gone.

**Hard rule before ANY prune** (`container prune`, `image prune`, `system prune`):

1. **List candidates with size + age first:**
   ```bash
   docker ps -a --filter "status=exited" --format "table {{.Names}}\t{{.Size}}\t{{.Status}}" --size
   docker images --format "table {{.Repository}}:{{.Tag}}\t{{.Size}}\t{{.CreatedSince}}\t{{.ID}}"
   docker volume ls --format "{{.Name}}\t{{.Driver}}"
   ```
2. **Show the list to the user and ASK** before running `-f`. Default is "no".
3. **Skip container prune entirely** if the user just said "clean up junk" without explicitly authorizing container removal. Prefer safer ops: dangling image prune (`docker image prune` no `-a`), build cache prune (`docker builder prune`), and cache cleanup (npm/pip/cargo).

**Why containers are special:** Even with images preserved, recreating `docker run` containers means remembering or reconstructing the original flags, ports, env vars, and volume mounts. For tools like `jellyfin`, `plex`, `termix` that the user pulls up occasionally, this is real friction. Random scratch containers (`glances`, `gopeed`, `watchyourlan`) are safe; long-lived apps are not.

## PITFALL: Image can disappear after container prune even though container prune "doesn't remove images"

Observed (2026-07-11): pulled `lbjlaq/antigravity-manager:latest` (1.6 GB), ran a container, container exited, ran `docker container prune -f`, image vanished from `docker images`. `docker container prune` does NOT remove images by design, but:

- If the container you removed was the **last reference** to an image, the image becomes **dangling** (untagged → `<none>:<none>`).
- Subsequent `docker image prune` (no `-a`) or background containerd GC can reap it.
- A `docker pull` or `docker compose pull` is then needed to bring it back.

**Implication for restart-after-prune:** don't assume the image is still there. Always:
```bash
docker images <repo>:<tag> --format "{{.ID}}\t{{.Size}}" 2>/dev/null \
  || echo "MISSING - need to pull"
```
If missing, re-pull before declaring cleanup safe.

## PITFALL: Non-trivial install workflows need user confirmation before running

User injected out-of-band "wait for next instruction" (2026-07-11) after starting a background `docker compose pull` for a 1.6 GB image without explicit "go". The runtime let it run, but the user wanted to confirm details (volume path, network mode, auth) first.

**Rule:** When the install workflow is non-trivial (pulls a large image, creates volumes, binds privileged ports, requires API keys, persists data to host), **show the plan, get confirmation, THEN run**. Do not start background downloads on inference alone.

**Safe scaffolding commands** (always fine before confirmation):
- `docker images`, `docker ps`, `docker inspect`, `docker logs`, `curl http://...` (read-only)
- `mkdir -p`, `cat > file`, writing compose/env templates to disk
- Reading README, GitHub pages, skill docs

**Hold for confirmation:**
- `docker compose up/pull/down`
- `docker run -d`, `docker rm`, `docker rmi`
- Any `install.sh` / `setup.sh` that mutates host state
- Database migrations, `chmod`/`chown` on persistent data
- Port changes, network policy changes, anything touching `/mnt/tb`

## When Things Go Wrong
- If new image breaks: `docker compose down && docker compose up -d` (uses cached image)
- If keys lost: restore from backup, then recreate
- If DB corrupted: restore from backup sqlite file

## PITFALL: Upstream image may start validating previously-empty env vars

Observed on CasaOS `linuxserver/qbittorrent:latest` (2026-07-11): the compose file had

```yaml
TORRENTING_PORT: ""
```

A newer image began passing that through as an explicit CLI arg and qBittorrent refused to start:

```text
Parameter '--torrenting-port' must follow syntax '--torrenting-port=<integer value>'
```

**Fix:** set an explicit integer before recreate, e.g.

```yaml
TORRENTING_PORT: "6881"
```

then run:

```bash
cd /var/lib/casaos/apps/linuxserver-qbittorrent
docker compose up -d --force-recreate --no-deps app
```

and verify `http://127.0.0.1:8181/` returns 200.

**General lesson:** when an update pulls successfully but the app never becomes ready, check container logs immediately for new startup-time validation of formerly-blank env vars. Do not assume the recreate itself failed.
