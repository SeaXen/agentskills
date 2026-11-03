# FastAPI dashboard packaging, BuildKit, and CasaOS manifest pattern

Use this when a self-hosted FastAPI dashboard is already performance-optimized and now needs professional packaging for GitHub, Docker, and CasaOS.

## Proven pattern

### Dockerfile structure for better layer reuse
Order the Dockerfile like this:

1. base image
2. OS packages (`curl` for healthchecks, nothing extra)
3. copy `requirements.txt`
4. install Python deps
5. copy only runtime source files (`app.py`, `collectors.py`, `static/`)

This prevents dependency reinstall on every frontend/content edit.

### BuildKit readiness
Use BuildKit syntax and pip cache mounts:

```Dockerfile
# syntax=docker/dockerfile:1.7
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
```

Docs should include both:
- one-shot enable: `DOCKER_BUILDKIT=1 ...`
- persistent enable via `~/.docker/config.json`
- plugin verification: `docker buildx version`

### Dependency pinning
If runtime code imports a package that is missing from `requirements.txt`, add it explicitly even if it happens to exist on the current box.

Concrete example from AceRoute:
- `collectors.py` imports `yaml`
- fix was adding `PyYAML==6.0.2`

### CasaOS custom-app manifest
If CasaOS should expose polished app fields like Docker Image, Title, Port, and Icon URL, do **not** rely on a local `build:` compose service alone.

Provide an image-based manifest with these fields:

```yaml
services:
  appname:
    image: ghcr.io/your-org/appname:latest
    labels:
      icon: https://...
x-casaos:
  icon: https://...
  port_map: "8866"
  scheme: http
  index: /
  title:
    en_us: AppName
```

Key lesson: CasaOS custom app UX behaves much better when the manifest looks like a pullable store app, not a local build recipe.

### Beginner-facing README minimum
A professional README for self-hosted dashboards should include:

- plain-English project description
- Compose install guide
- Docker CLI install guide
- BuildKit/buildx section
- env var table
- path customization notes
- common commands (`up`, `logs`, `down`, `stats`)
- troubleshooting
- CasaOS notes if relevant
- explicit note when image name is still a placeholder and must be published

## Verification standard
After packaging changes, verify at least:

- `docker compose config`
- `python3 -m py_compile app.py collectors.py`
- a real BuildKit `docker build`

Do not claim CasaOS is ready for other machines unless the image is actually published to a registry.
