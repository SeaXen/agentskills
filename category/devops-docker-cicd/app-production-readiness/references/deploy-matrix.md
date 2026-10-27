# Deploy Matrix — free portable targets

All from one repo, env-driven. No paid-only service.

## Env convention

```
PORT=<detected>               # e.g. 3000 (Next/Node) | 5173 (Vite) | 4200 (Angular) | 8080 (Vue/Vite) — auto-detect, never assume
APP_URL=http://localhost:<detected>
STORAGE_DRIVER=memory        # memory | fs | r2
KV_BINDING=                  # optional, Cloudflare only
DATABASE_URL=                # optional, sqlite/postgres url
```

`.env.example` documents every var. App reads only `process.env`.

## Verify the targets — do not trust the file list

```bash
python scripts/deploy_verify.py <app_root>          # parse + validate every platform config
python scripts/deploy_verify.py <app_root> --build  # additionally run `docker build` when Docker exists
```

The script parses each config and checks the fields that decide whether a deploy actually works.
Exit `1` on a blocking problem, `0` when every present config is valid. When Docker is unavailable
the build step is reported as **SKIPPED**, not as a pass.

| Config | Checked |
|--------|---------|
| `Dockerfile` | CMD/ENTRYPOINT present, EXPOSE present, non-root `USER`, HEALTHCHECK, multi-stage, `$PORT` honoured, `.dockerignore` exists |
| `vercel.json` | valid JSON, build command, output directory (and that it exists) |
| `netlify.toml` | valid TOML, build command, publish directory |
| `fly.toml` | app name, `internal_port` (top level or inside `[http_service]`), `http_service`, `http_checks` |
| `render.yaml` | service defined, build + start command, `healthCheckPath` |
| `wrangler.toml` / `wrangler.json` | name, entrypoint, compatibility date |
| `Procfile` | a `web:` process |
| `railway.json` / `railway.toml` | start command / builder |
| any `start` script | must not hardcode a port |

## Per-platform checklist

### localhost
- `$PKG install && $PKG run dev` works on detected `$PORT`
- `$PKG run build && $PKG start` works, respects `PORT`

### Docker
- `Dockerfile` (multi-stage node:20-alpine), `.dockerignore` excludes node_modules/.git
- Test: `docker build -t app . && docker run -p $PORT:$PORT app`, hit `$APP_URL/$HEALTHZ`

### Vercel
- Framework preset or `vercel.json` with `buildCommand`/`outputDirectory`
- Env set in dashboard, same names as `.env.example`

### Netlify
- `netlify.toml`: `[build] command / publish`, functions dir only if needed

### Railway / Render
- `start: node dist/index.js`, listens on `process.env.PORT`
- Health check path `/healthz`, document persistent-disk limits

### Fly.io
- `fly.toml` with `internal_port = <detected PORT>`, `[[services.http_checks]] path="$HEALTHZ"`

### Cloudflare Free (optional, flagged)
- `wrangler.toml` present but NOT required to run elsewhere
- Pages for static, Workers for API; D1/R2/KV/DO/Queues only via adapter:
  ```ts
  if (process.env.KV_BINDING) return kvAdapter();
  return memoryAdapter(); // default
  ```
- Document free-plan quotas in README (see [free-tier-limits.md](free-tier-limits.md)).

## README must include
1. One-command local run
2. Env table (name | required | default | used by)
3. Per-platform steps (copy-paste commands)
4. Free-plan limits + fallback behavior
