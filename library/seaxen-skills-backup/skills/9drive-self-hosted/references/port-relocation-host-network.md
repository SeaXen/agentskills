# Port Relocation in Host-Network Mode + Dockerfile Build Fix

When the user requires Docker **host network mode** but the default service ports (80, 3306, 4000) are already used by other host services, the only escape hatch is to relocate the app's ports onto a free range. This file covers the recipe and the two failure modes that hit during this work.

## 1. Port discovery

```bash
for p in 80 443 3306 4000 8080 8081 9080 9001 3307 9400; do
  if ss -tlnp | grep -q ":$p "; then echo "$p IN USE"; else echo "$p FREE"; fi
done
```

Pick a coherent set, e.g. for 9Drive: **frontend 9080, backend 9001, mysql 3307**. Keep gaps so future migrations are easy.

## 2. Compose patch (host network + relocated ports)

The defaults live in `/mnt/tb/1Apps/9drive/docker-compose.yml`. Apply this exact diff:

```yaml
services:
  mysql:
    network_mode: host
    # backend now reaches it on localhost:3307

  backend:
    network_mode: host
    environment:
      DATABASE_URL: mysql://${MYSQL_USER}:${MYSQL_PASSWORD}@localhost:3307/${MYSQL_DATABASE}
      APP_PORT: 9001
      FRONTEND_URL: ${FRONTEND_URL:-http://localhost:9081}     # user's browser-facing URL
      GOOGLE_REDIRECT_URI: ${GOOGLE_REDIRECT_URI:-http://localhost:9001/connected-accounts/google/callback}

  frontend:
    network_mode: host
    build:
      args:
        VITE_API_URL: ${VITE_API_URL:-http://localhost:9001}
```

`network_mode: host` means **no `ports:` mapping is allowed** — the container binds directly to the host port. State this loudly to the user when collecting preferences.

## 3. Frontend nginx port

The default `frontend/nginx.conf` listens on 80. Patch:

```nginx
server {
  listen 9080;
  ...
  location /api/ {
    proxy_pass http://backend:4000/;   # keep as 4000 — the BACKEND's APP_PORT is the canonical API port
    ...
  }
}
```

Note: `proxy_pass http://backend:4000` here refers to **what nginx thinks the API base is**, but the backend's actual listen port is `APP_PORT`. The frontend nginx image's nginx config does not need to match `APP_PORT` if the build arg `VITE_API_URL` is correct and the browser hits the API directly. **Verify by `curl http://localhost:9081/api/health` from the host.**

## 4. .env consistency

```
FRONTEND_URL=http://localhost:9081
VITE_API_URL=http://localhost:9001
GOOGLE_REDIRECT_URI=http://localhost:9001/connected-accounts/google/callback
```

All three URLs must agree — `FRONTEND_URL` is for OAuth callback whitelist, `VITE_API_URL` is baked into the frontend bundle at build time, `GOOGLE_REDIRECT_URI` must match exactly what Google Cloud Console has registered.

## 5. Dockerfile build fix (`tsc: not found`)

`backend/Dockerfile` originally had:

```dockerfile
RUN npm ci
...
RUN npm run build && npx prisma generate
```

`node:20-alpine` base sets `NODE_ENV=production` which makes `npm ci` skip devDependencies. `typescript` is in `devDependencies` of `package.json`, so `tsc` is missing at build time.

Fix:

```dockerfile
RUN npm ci --include=dev
...
RUN npx tsc && npx prisma generate
```

`--include=dev` is the explicit opt-in. `npx tsc` calls the locally installed TypeScript compiler (works because the prior `npm ci --include=dev` installed it into `node_modules/.bin/`).

**This is a recurring pattern** across Next.js / TypeScript Docker images: any build that needs `tsc` at build time must use `--include=dev`. Affects many apps, not just 9Drive.

## 6. Verification

```bash
docker compose up -d --build
# Wait ~30s for healthchecks
docker ps --filter "name=9drive" --format "table {{.Names}}\t{{.Status}}"
curl -sf http://localhost:9080/ | head -c 200      # frontend
curl -sf http://localhost:9001/health             # backend health (if exposed)
docker exec 9drive-mysql-1 mysqladmin ping -h localhost -u root -p$MYSQL_ROOT_PASSWORD
```

## Pitfalls

- **Don't add `ports:` mapping in compose when using `network_mode: host`** — Docker rejects the config or silently ignores.
- **`localhost` in browser URL ≠ `localhost` in container** — the browser hits the host, the container's `localhost` is itself. For a browser-facing URL like `GOOGLE_REDIRECT_URI`, use the host's IP or `localhost` as the user would type it in their browser.
- **Build arg changes need `--build`** — `docker compose up -d` without `--build` keeps the old `VITE_API_URL` baked into the frontend bundle.
- **Multi-service build with `npm ci` defaulting to prod** — if `frontend` uses the same Node image, the same `tsc: not found` symptom can hit the Vite build. Apply the same fix if needed.
