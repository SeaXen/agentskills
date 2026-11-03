# CasaOS anonymous-volume to HDD bind-mount pattern

Use this when a CasaOS app is running from Docker-managed anonymous/named volumes on SSD and the user wants the real app state on HDD without moving Docker's global data-root.

## Example shape
- App compose file has **no explicit volumes** for the stateful paths, or Docker inspect shows mount sources under Docker data-root such as:
  - `/mnt/dietpi_userdata/docker-data/volumes/<id>/_data -> /root/.cloudflared`
  - `/mnt/dietpi_userdata/docker-data/volumes/<id>/_data -> /config`
- The practical move is to convert those runtime volumes into explicit HDD bind mounts in the compose file.

## Safe procedure
1. Inspect current mounts with `docker inspect` and record each source/destination pair.
2. Create HDD destinations under `/mnt/tb/1Apps/<app>/...`.
3. Back up the CasaOS compose file.
4. Do an initial live `rsync` from each old Docker volume mountpoint to the matching HDD path.
5. Patch the compose file to add a `volumes:` section with explicit bind mounts to the HDD paths.
6. Stop the container briefly.
7. Run a final `rsync --delete` from old volume mountpoints to the HDD paths.
8. Recreate with `docker compose up -d --force-recreate --no-deps <service>`.
9. Verify both endpoint health and `docker inspect` mount sources.
10. Keep the old Docker volumes until the user confirms cleanup.

## Verified example
Cloudflared-web migrated cleanly by converting SSD Docker volumes to HDD binds:
- `/mnt/tb/1Apps/cloudflared-web/cloudflared -> /root/.cloudflared`
- `/mnt/tb/1Apps/cloudflared-web/config -> /config`

## Why this matters
If you only copy files to HDD but do not patch compose, the recreated container keeps writing to the old SSD Docker volume and no space is actually reclaimed.
