# Static mount vs baked Python (self-hosted dashboards)

## Pattern
Docker Compose often mounts only frontend assets:

```yaml
volumes:
  - ./static:/app/static:ro
```

while the Dockerfile `COPY`s `app.py` and Python modules into the image.

## Failure mode
Agent (or human) edits host `app.py` / collectors / analytics modules, restarts the container with `--no-build`, and sees:
- CSS/JS changes work immediately
- new API routes 404
- timezone / day-window / auth meta stay old

## Fix options (prefer in order)
1. **Dev loop:** bind-mount each runtime module (read-only):
   ```yaml
   - ./app.py:/app/app.py:ro
   - ./collectors.py:/app/collectors.py:ro
   # …all imported app modules
   ```
   Then `docker compose up -d --force-recreate --no-build`.
2. **Release path:** `docker compose up -d --build` so image gets new code.
3. Always verify with a **new** endpoint or field (e.g. `/api/meta` timezone) not just healthz.

## Related verification
- Short smoke: healthz, meta, one dashboard, static assets, timezone field.
- Operator UI polish patterns live in `operator-dashboard-finishing-pass`.
