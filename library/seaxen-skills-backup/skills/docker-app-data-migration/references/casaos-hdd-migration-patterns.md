# CasaOS + Compose HDD migration patterns

Concrete patterns verified in session.

## Scope

These examples move **persistent app data** from SSD-backed host paths or Docker named volumes to HDD-backed bind mounts under `/mnt/tb/1Apps/...`.

They do **not** move Docker image layers. Docker root stayed on SSD.

## Host disk model

- SSD paths:
  - `/`
  - `/DATA`
  - `/srv`
  - `/mnt/dietpi_userdata/docker-data`
- HDD path:
  - `/mnt/tb`

Rule of thumb:
- `/mnt/tb/...` = HDD
- `/DATA/...`, `/srv/...`, `/mnt/dietpi_userdata/...` = SSD

## Pattern A — named volume to HDD bind mount

### Example: FreeLLMAPI

Old state:
- container: `freellmapi-freellmapi-1`
- source: `/mnt/dietpi_userdata/docker-data/volumes/freellmapi_freellmapi-data/_data`
- compose used named volume:
  - `freellmapi-data:/app/server/data`

New state:
- HDD path: `/mnt/tb/1Apps/freellmapi/data`
- compose changed to:
  - `/mnt/tb/1Apps/freellmapi/data:/app/server/data`

Safe sequence:
1. Back up compose + `.env`.
2. Initial live `rsync` from named-volume mountpoint to HDD path.
3. Stop container briefly.
4. Final `rsync --delete`.
5. Recreate from compose.
6. Verify HTTP health and `docker inspect` mount source.
7. Delete old named volume only after verification.

Verification target:
- `http://127.0.0.1:3055/api/ping`

## Pattern B — CasaOS bind mount on SSD to bind mount on HDD

### Example: LibreSpeed

Old state:
- compose: `/var/lib/casaos/apps/linuxserver-librespeed/docker-compose.yml`
- source: `/srv/lsio/librespeed/config`

New state:
- HDD path: `/mnt/tb/1Apps/librespeed/config`

Safe sequence:
1. Back up CasaOS compose file.
2. Initial live `rsync` to HDD path.
3. Patch compose source path.
4. Stop container.
5. Final `rsync --delete`.
6. Rename old SSD path to rollback backup:
   - `/srv/lsio/librespeed/config.bak.<timestamp>`
7. Create empty placeholder directory only if the original path is expected by tooling.
8. Recreate with compose.
9. Verify endpoint and `docker inspect` mount source.
10. Delete old SSD backup only after explicit confirmation.

Verification target:
- `http://127.0.0.1:8077/`

### Example: vnStat

Old state:
- compose: `/var/lib/casaos/apps/poetic_dave/docker-compose.yml`
- source: `/DATA/AppData/vnstat`

New state:
- HDD path: `/mnt/tb/1Apps/vnstat/data`

Verification target:
- `http://127.0.0.1:8685/`

## Pattern C — app config already on HDD, DB still on SSD

### Example: Manifest

Old state:
- app compose + `.env` already lived on HDD:
  - `/mnt/tb/1Apps/manifest`
- Postgres data still lived on SSD named volume:
  - `manifest_pgdata`
  - `/mnt/dietpi_userdata/docker-data/volumes/manifest_pgdata/_data`

New state:
- Postgres bind mount on HDD:
  - `/mnt/tb/1Apps/manifest/postgres-data:/var/lib/postgresql/data`

Important lesson:
- the meaningful migration was **Postgres data**, not the compose file
- saying "Manifest is already on HDD" was incomplete until the DB mount moved too

Safe sequence:
1. Back up compose + `.env`.
2. Initial live `rsync` from named-volume mountpoint to HDD path.
3. Patch compose Postgres service from named volume to HDD bind mount.
4. Stop **both** app and DB briefly before final sync.
5. Final `rsync --delete`.
6. Recreate `postgres` and `manifest`.
7. Verify DB healthy and app endpoint healthy.
8. Keep old named volume until verification window is over.

Verification target:
- `http://127.0.0.1:2099/api/v1/health`

## Pattern D — CasaOS bind mount plus secondary HDD mount already present

### Example: Alist

Old state:
- app data on SSD:
  - `/DATA/AppData/alist/data`
- separate HDD mount already exposed to the container:
  - `/mnt/tb -> /tb`

New state:
- app data moved to HDD:
  - `/mnt/tb/1Apps/alist/data -> /opt/alist/data`

Lesson:
- an app can already "see" the HDD in one mount while still storing its own settings/database on SSD
- inspect the **actual persistent app-data mount**, not just any HDD mount in the container

Verification target:
- `http://127.0.0.1:5244/`

## Pattern E — Portainer bind mount migration

Old state:
- compose: `/var/lib/casaos/apps/portainer/docker-compose.yml`
- source: `/DATA/AppData/portainer`

New state:
- HDD path: `/mnt/tb/1Apps/portainer/data`

Verification target:
- `http://127.0.0.1:9000/`

## Cleanup rule

Do not delete old SSD sources immediately.

Keep one of:
- old bind path renamed to `*.bak.<timestamp>`
- old named volume left intact

Only remove after all are true:
1. service responds normally
2. `docker inspect` shows the HDD mount source
3. `findmnt -T <newpath>` confirms `/mnt/tb`
4. user confirms cleanup

## Update-related pitfall discovered in same session

CasaOS `linuxserver/qbittorrent` update failed because the compose file had:

```yaml
TORRENTING_PORT: ""
```

Newer image rejected the empty value. Setting:

```yaml
TORRENTING_PORT: "6881"
```

fixed startup.

Lesson:
- when a recreate succeeds but the app never becomes ready, inspect logs for new validation of previously-empty env vars.