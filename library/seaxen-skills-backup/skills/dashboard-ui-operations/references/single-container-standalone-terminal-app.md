# Single-container standalone terminal app pattern

Use this when building a standalone browser terminal/dashboard app where ease of install and management matters more than framework purity.

## Durable lesson

For a small standalone terminal app, a separate `frontend` + `backend` container split is often unnecessary. Prefer a one-container shape unless there is a clear scaling or build reason to split:

```text
one container
├─ GET /       -> static terminal UI
└─ /api/*      -> PTY/session/history API
```

This is especially useful when Docker build networking is unreliable and package installs via apt/pip/npm are blocked or slow.

## Good default implementation

- Python stdlib `ThreadingHTTPServer` serves both static files and JSON API.
- Static frontend lives inside the backend build context, e.g. `backend/static/index.html`.
- Dockerfile copies both:
  - `COPY app /app/app`
  - `COPY static /app/static`
- Compose has one service only:
  - `rexterm` or equivalent app name
  - one public port mapping, e.g. `2344:8080`
  - one data volume, e.g. `./data:/data`
- Use `docker compose up -d --build --remove-orphans` when migrating away from sidecars so old `frontend`/`backend` containers are removed.

## Server static fallback pattern

For HTML single-page apps, route non-API GETs to static files:

- if path does not start with `/api/`, serve static
- default `/` to `index.html`
- normalize/abspath requested path and ensure it stays under `STATIC_DIR`
- if missing, fall back to `index.html`
- keep API routes token-protected separately from public static HTML

## Operator UX implication

If the user asks “why different backend and frontend, can it be only one?”, treat that as a workflow correction. For small self-hosted dashboards, simplify management first unless the user explicitly wants a multi-service architecture.

## Verification checklist

- `docker compose config` shows one service and the expected published port.
- `docker compose up -d --build --remove-orphans` removes old sidecars.
- `docker ps` shows only the new app container.
- `GET /` returns `200 text/html`.
- `/api/health` returns JSON through the same public port.
- Browser loads the UI and console has no JS errors.
- A real command can be sent and read back through the terminal API/UI.
