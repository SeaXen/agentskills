# Open WebUI host-bind migration example

## Scenario

A live `open-webui` container was running on a DietPi/Debian host. The user asked to move "whole Open WebUI" to `/mnt/tb/1Apps`.

## What inspection showed

- Container image: `ghcr.io/open-webui/open-webui:main`
- Runtime pattern: `docker run` with host networking
- Persistent data bind mount:
  - old: `/opt/open-webui-data -> /app/backend/data`
  - new target: `/mnt/tb/1Apps/open-webui-data -> /app/backend/data`
- Health verification needed because Open WebUI takes time to start and generate/load its secret key.

## Useful commands

Inspect runtime settings:

```bash
docker inspect open-webui --format 'Name={{.Name}}\nImage={{.Config.Image}}\nRestart={{.HostConfig.RestartPolicy.Name}}\nNetworkMode={{.HostConfig.NetworkMode}}\nEnv={{json .Config.Env}}\nBinds={{json .HostConfig.Binds}}'
```

Confirm mount source after recreation:

```bash
docker inspect open-webui --format '{{range .Mounts}}{{.Source}} -> {{.Destination}} ({{.Type}})\n{{end}}'
```

Confirm filesystem ownership of old vs new path:

```bash
findmnt -T /mnt/tb/1Apps/open-webui-data -o TARGET,SOURCE,FSTYPE -n
findmnt -T /opt/open-webui-data.bak.<timestamp> -o TARGET,SOURCE,FSTYPE -n
```

Probe the service:

```bash
curl -fsS http://127.0.0.1:8080/ >/dev/null && echo ok
```

## Startup quirk

Immediately after recreation, `curl` can fail even though the migration is correct. Logs showed early startup lines like:

- `Loading WEBUI_SECRET_KEY from file, not provided as an environment variable.`
- `Generating WEBUI_SECRET_KEY`
- `INFO  [alembic.runtime.migration] ...`

So add a short poll loop instead of treating the first failed HTTP request as a migration failure.

## User-facing explanation that mattered

When the user asked why SSD free space did not increase after moving the app to HDD, the right explanation was:

1. The new HDD copy existed.
2. The old SSD copy still existed as a backup.
3. Docker image/layers were still stored under Docker/containerd storage, so only the app data moved.

This wording helped separate “data path moved” from “image storage moved.”

## Outcome pattern

- Recreate container with new bind mount.
- Verify `running` + `healthy`.
- Verify mount source points to `/mnt/tb/1Apps/open-webui-data`.
- Verify old backup path is on root SSD.
- Delete backup only after confirmation.
- Re-check `df -h / /mnt/tb` to show the root filesystem actually gained space.
