# Docker image update checks

Use this when the user asks "is this updated?" or "which Docker apps need updates?"

## What to compare
For public images, compare:
1. Local installed RepoDigest
2. Remote manifest digest for the same tag

Example:
```bash
docker image inspect ghcr.io/searxng/searxng:latest --format '{{json .RepoDigests}}'
docker buildx imagetools inspect ghcr.io/searxng/searxng:latest --format '{{json .Manifest.Digest}}'
```

If equal → up to date.
If different → update available.

## Running container vs local tag
Also inspect the running container itself:
```bash
docker inspect <container> --format '{{.Config.Image}} {{.Image}}'
```

This catches digest-pinned services such as:
```text
postgres:16-alpine@sha256:20edbde...
```

In that case:
- the service is pinned to a specific digest
- `docker compose pull` may fetch a newer tag upstream
- but the running service will stay on the pinned digest until the compose file changes or the image reference is rewritten

## Compose project discovery
When you only know the container name, get the real compose workdir from labels:
```bash
docker inspect <container> --format 'project={{index .Config.Labels "com.docker.compose.project"}} workdir={{index .Config.Labels "com.docker.compose.project.working_dir"}} config={{index .Config.Labels "com.docker.compose.project.config_files"}} service={{index .Config.Labels "com.docker.compose.service"}}'
```

Useful on mixed hosts where some stacks live in custom directories and others under dashboard-managed paths like `/var/lib/casaos/apps/...`.

## Verification pattern after update
After `docker compose pull && docker compose up -d`:
1. verify the container is back up with `docker ps`
2. inspect the container image digest again
3. compare against remote digest again
4. if healthchecks exist, wait for healthy
5. verify HTTP/service reachability

## Important interpretation rule
A healthy container is not proof it updated.
Digest comparison is the proof.

## Session-derived example
Observed pattern:
- `manifestdotbuild/manifest:latest` updated successfully
- `postgres:16-alpine` remained on an older digest because the running container image reference was pinned as `postgres:16-alpine@sha256:20edbde...`
- result: app stack healthy, but only part of the stack actually moved to the newest remote revision
