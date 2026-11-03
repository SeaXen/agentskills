# Docker Build Networking Pitfall

When a Docker Compose service has `network_mode: host`, that only applies at **RUNTIME**. The build phase (`RUN pip install ...`) still uses the default bridge network and may fail with `Network is unreachable` or connection timeouts to PyPI/npm.

## Fix

Add `build: network: host` to docker-compose.yml:

```yaml
services:
  myapp:
    build:
      context: .
      network: host    # ← This passes --network=host to docker build
    network_mode: host  # ← This is runtime only
    restart: unless-stopped
```

## When to apply

- Build fails with `Failed to establish a new connection: [Errno 101] Network is unreachable` during `pip install` or `npm install`
- Build fails with `HTTPSConnectionPool` timeouts during package download
- Host machine has working internet but Docker build containers can't reach external hosts
- Common on hosts with custom DNS, VPN, or firewall rules that don't apply to Docker bridge

## Verification

```bash
# Build should now succeed
cd /project && docker compose build --no-cache 2>&1 | tail -5

# Runtime should also work (host networking)
docker compose up -d
curl -s http://localhost:PORT/health
```

## Also: BuildKit cache mount

If the Dockerfile uses `RUN --mount=type=cache,target=/root/.cache/pip`, this requires BuildKit. The daemon may not support it. Either:
- Set `DOCKER_BUILDKIT=1` (may not work with classic daemon)
- Remove the `--mount` flag and use plain `RUN pip install --no-cache-dir -r requirements.txt`

## Example from AceRoute

Initial docker-compose.yml had `network_mode: host` but no `build: network: host`. Build failed with PyPI connection errors. Adding `build: network: host` fixed it immediately.
