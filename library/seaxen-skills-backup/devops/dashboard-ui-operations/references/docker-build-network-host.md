# Docker build vs runtime networking

When `network_mode: host` is set in docker-compose.yml, it only applies at **runtime** (container start). During `docker build`, the build context still uses the default bridge network.

## Symptom
`pip install` fails inside Dockerfile with `Network is unreachable` or `Errno 101`, even though `network_mode: host` is in compose.

## Fix
Pass `network: host` to the build step in docker-compose.yml:

```yaml
services:
  myapp:
    build:
      context: .
      network: host    # <-- forces build-time networking to use host
    network_mode: host  # runtime
```

Or use `docker compose build --build-arg HTTP_PROXY=...` / `docker build --network=host`.

## Gotcha
BuildKit (`DOCKER_BUILDKIT=1`) may not be available on all daemons. The `--mount=type=cache` Dockerfile syntax requires BuildKit. If the daemon doesn't support it, use plain `RUN pip install` and rely on compose build `network: host` instead.

## When this hits
- Self-hosted servers where Docker bridge networking is restricted or has no egress
- Hosts behind corporate firewalls where only host networking has route to the internet
- Any Dockerfile that downloads packages during build
