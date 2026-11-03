---
name: docker-app-data-migration
description: Use when moving a Dockerized app's persistent host data to another disk or mount point without moving Docker image layers, and when you need to verify the running container really uses the new location before deleting the old copy.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [docker, containerd, storage, migration, bind-mounts, disks, verification]
    related_skills: [systematic-debugging, hermes-agent-skill-authoring]
---

# Docker App Data Migration

## Overview

This skill covers the common case where a user says “move this Docker app to another disk,” but the container is using a host bind mount for persistent data while Docker image layers remain under Docker/containerd-managed storage. The right move is often to migrate the app's host data directory, recreate the container with the new bind mount, verify the app is healthy from the new disk, keep a temporary backup, then delete the old copy after confirmation.

It also teaches the important distinction between:
- **app data**: host bind mounts or named volumes that can often be moved directly, and
- **Docker image/layers**: managed by Docker/containerd and not safely “moved one image at a time” by dragging folders around.

## When to Use

Use this skill when:
- A containerized app should run from another disk such as `/mnt/tb`, `/data`, or an external drive.
- The user specifically wants an app “moved” but the real target is its persistent data/config/database/cache.
- You need to explain why free space on the source disk did not improve after copying data.
- You must verify whether the running container is using the new mount before deleting the old directory.

Do **not** use this for:
- Full Docker Engine / containerd storage relocation. That is a broader daemon migration.
- Cases where the app uses Docker named volumes only and no host bind mount; inspect volume mappings first.
- Swarm/Kubernetes-managed deployments where the container should be changed via orchestration manifests instead of ad hoc `docker run` recreation.

## Core Principle

When a user says “move app X to HDD,” first determine which of these they actually mean:

1. **Move persistent app data**
   - Usually achievable by migrating the host directory bound into the container.
   - Typical examples: config, SQLite DB, embeddings cache, downloads, uploads.

2. **Move Docker image/layer storage**
   - Not a per-image drag-and-drop operation.
   - Requires moving Docker/containerd storage globally or reconfiguring the engine.

Never tell the user an image has been “moved” when only the bind-mounted host data moved.

## Discovery Checklist

Before making changes, inspect:

```bash
docker inspect <container_name> --format 'Name={{.Name}}\nImage={{.Config.Image}}\nRestart={{.HostConfig.RestartPolicy.Name}}\nNetworkMode={{.HostConfig.NetworkMode}}\nBinds={{json .HostConfig.Binds}}'
```

Also inspect mounts in a more readable form:

```bash
docker inspect <container_name> --format '{{range .Mounts}}{{.Source}} -> {{.Destination}} ({{.Type}})\n{{end}}'
```

Check where the source paths live:

```bash
findmnt -T /path/to/current/data -o TARGET,SOURCE,FSTYPE -n
findmnt -T /path/to/new/data -o TARGET,SOURCE,FSTYPE -n
```

Check sizes and free space before/after:

```bash
du -sh /path/to/current/data
 df -h / /mnt/tb
```

If the user is worried about root-disk pressure, also inspect Docker/containerd storage separately:

```bash
docker info --format '{{json .}}'
du -sh /var/lib/containerd 2>/dev/null
du -sh /mnt/dietpi_userdata/docker-data 2>/dev/null
```

## Standard Migration Procedure (host bind mount)

### 1. Create destination and do first copy while app is live

```bash
mkdir -p /new/disk/app-data
rsync -aHAX --info=stats1,progress2 /old/path/ /new/disk/app-data/
```

This minimizes downtime because most bytes copy before stopping the container.

### 2. Stop the container and do a final sync

```bash
docker stop <container_name>
rsync -aHAX --delete /old/path/ /new/disk/app-data/
```

Use the second sync to catch last-minute writes.

### 3. Preserve rollback path

Rename the old directory instead of deleting immediately:

```bash
mv /old/path /old/path.bak.$(date +%Y%m%d-%H%M%S)
```

### 4. Recreate the container with the new bind mount

If the container was created via `docker run`, reproduce the original runtime settings exactly:
- image
- restart policy
- network mode
- environment variables
- published ports or host networking
- bind mounts
- command/entrypoint if customized

Typical pattern:

```bash
docker rm <container_name>
docker run -d \
  --name <container_name> \
  --restart unless-stopped \
  ...original options... \
  -v /new/disk/app-data:/container/path \
  <image>
```

If the app is defined in Compose, update the compose file and recreate via Compose instead of raw `docker run`.

## Verification Steps

Do **all** of these before deleting the old copy:

### 1. Confirm the container is up

```bash
docker ps --filter name='^<container_name>$' --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}'
```

### 2. Confirm the mount source is the new disk path

```bash
docker inspect <container_name> --format '{{range .Mounts}}{{.Source}} -> {{.Destination}}\n{{end}}'
```

### 3. Confirm the new path is really on the destination filesystem

```bash
findmnt -T /new/disk/app-data -o TARGET,SOURCE,FSTYPE -n
```

### 4. Probe the service itself

Use the app's real health check when possible. For HTTP apps:

```bash
curl -fsS http://127.0.0.1:<port>/ >/dev/null && echo ok
```

If startup takes time, poll rather than failing immediately:

```bash
for i in $(seq 1 24); do
  status=$(docker inspect <container_name> --format '{{if .State.Health}}{{.State.Health.Status}}{{else}}{{.State.Status}}{{end}}' 2>/dev/null || true)
  if curl -fsS http://127.0.0.1:<port>/ >/dev/null 2>&1; then
    echo "app_ok status=$status"
    break
  fi
  sleep 5
done
```

### 5. Only then remove the backup

```bash
rm -rf /old/path.bak.<timestamp>
df -h / /new/disk
```

## Explaining Disk-Space Results to Users

If the user asks “why didn't SSD free space increase?” check for both of these:

1. **Backup still exists on source disk**
   - Example: `/old/path.bak.<timestamp>` still occupies the old space.

2. **Docker image/layers are still on source-disk Docker/containerd storage**
   - The app may now use HDD for its data, but image layers remain under paths like:
     - `/var/lib/containerd`
     - Docker `data-root`

Use plain language:
- “The app data moved.”
- “The old copy was still present as backup.”
- “The Docker image itself still lives in Docker/containerd storage, so only part of the footprint moved.”

## Open WebUI-Specific Notes

Open WebUI commonly stores persistent data under `/app/backend/data`. If launched with a bind mount, moving that host path moves:
- config
- SQLite DB
- embeddings/model caches under the app data tree
- secrets generated into the data directory

But the container image `ghcr.io/open-webui/open-webui:*` remains in Docker storage unless the whole Docker/containerd store is relocated.

See `references/open-webui-host-bind-migration.md` for a concrete example and wording patterns that helped explain why HDD usage went up before SSD usage went down.

See `references/manifest-docker-compose-deployment.md` for a reusable Docker Compose deployment pattern for self-hosted services with Postgres backends (Manifest LLM router on port 2099, similar to Hermes Dashboard on port 8009).

See `references/omniroute-docker-management.md` for OmniRoute's safe update procedure, encryption key gotchas, and backup script.

## Compose-managed named volume → HDD bind-mount pattern

A common migration shape is: the app currently stores persistent data in a **Docker named volume on SSD** (under Docker's data-root), but you want that data on **HDD as a host bind mount**. The safe pattern is:

1. Create the HDD destination directory first.
2. Do an initial live `rsync` from the named-volume mountpoint to the HDD path.
3. Patch the compose file so the service uses the HDD bind mount instead of the named volume.
4. Stop the container briefly.
5. Run a final `rsync --delete` from the old named-volume mountpoint to the HDD path.
6. Recreate the container from compose.
7. Verify both:
   - the app responds normally
   - `docker inspect` shows the new HDD bind mount
8. **Keep the old named volume until verification is complete.** Delete it only after the new container has been stable and verified.

This is the right move for apps where the image stays on SSD but the important state should move to HDD.

## CasaOS app migration pattern

CasaOS-managed apps commonly keep compose files under `/var/lib/casaos/apps/<app>/docker-compose.yml` while their persistent data may live on SSD paths like `/DATA/AppData/...` or `/srv/...`. Safe migration means:

1. Back up the CasaOS compose file before editing it.
2. Copy the existing data to `/mnt/tb/1Apps/<app>/...`.
3. Patch the CasaOS compose bind source to the new HDD path.
4. Stop the app, do a final sync, rename the old SSD path to `*.bak.<timestamp>`, and create an empty placeholder directory only if the compose/tooling expects the original path to exist.
5. Recreate with `docker compose up -d --force-recreate --no-deps <service>`.
6. Verify endpoint health and `docker inspect` mount sources before deleting the old SSD backup.

This pattern worked cleanly for LinuxServer/CasaOS-style apps (`librespeed`, `vnstat`, `alist`, `portainer`) and avoids the classic "copy happened but container still writes to SSD" mistake.

## Mixed-location apps: move the persistent state, not the whole illusion

Some apps are already partly on HDD and partly on SSD. Example pattern:
- compose file and `.env` already live on HDD
- database/data volume still lives on SSD via Docker volume or bind mount

In those cases, the meaningful migration is usually the **database or persistent app-data path**, not every file related to the app. Do not claim the whole app moved just because the compose file was already on HDD; verify the database/data mount specifically.

See `references/casaos-hdd-migration-patterns.md` for concrete examples from successful CasaOS + compose migrations.

See `references/casaos-anonymous-volume-to-bind-mount.md` for the pattern where a CasaOS app is implicitly using Docker-managed SSD volumes and must be converted to explicit HDD bind mounts in compose before recreation.

## Common Pitfalls

0. **Removing a container that holds runtime-generated secrets.**
   Many self-hosted apps (OmniRoute, Authelia, etc.) auto-generate encryption keys, JWT secrets, or TLS certs on first boot. These may be stored INSIDE the container filesystem (not in the bind-mounted volume). If you `docker stop` + `docker rm` the container without extracting those secrets first, the new container generates fresh keys that **cannot decrypt the old database**. The result: "Internal Server Error" or silent data loss.
   
   **Pre-update checklist for any self-hosted app:**
   - `docker exec <container> cat /path/to/secret.env` — extract generated keys
   - `docker inspect <container> --format '{{json .Config.Env}}'` — check for env vars
   - Backup the data volume: `cp -r /host/data /host/data.bak.$(date +%s)`
   - If using `docker compose`: `docker compose pull && docker compose up -d` (preserves config)
   - If using `docker run`: record the full `docker run` command BEFORE removing
   
   **If keys were lost:** the database is likely unrecoverable without the original encryption key. Restore from backup or start fresh. This is not fixable by restarting.

1. **Saying the whole app moved when only host data moved.**
   Be explicit about the split between bind-mounted data and image layers.

2. **Deleting the old directory before verifying the new mount.**
   Always keep a rollback copy until the service is healthy and responding.

3. **Forgetting to preserve original runtime options.**
   Missing env vars, host network mode, restart policy, or ports can cause a false “migration failure.”

4. **Checking only `docker ps`.**
   A container can be “Up” while the app is still starting; verify health and actual HTTP/service response.

5. **Using `rm -rf` immediately after recreation.**
   Pause for verification first; users often want confidence before irreversible cleanup.

6. **Misreading automount output from `findmnt`.**
   On systems using `autofs`/systemd automount, `findmnt -T` may show both the autofs stub and the actual mounted device. Read both lines before concluding which disk is in use.

## Verification Checklist

- [ ] Container inspected and current bind mounts identified
- [ ] Source and destination filesystems confirmed with `findmnt -T`
- [ ] Initial `rsync` completed before downtime
- [ ] Container stopped and final `rsync --delete` completed
- [ ] Old path retained as timestamped backup
- [ ] Container recreated with original runtime settings preserved
- [ ] `docker inspect` shows new mount source
- [ ] Service health or HTTP probe passed
- [ ] Backup removed only after explicit verification
- [ ] `df -h` checked to confirm source-disk space changed as expected
