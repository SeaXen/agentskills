# Host-built standalone (no Docker) — resource-constrained hosts

When Docker builds time out on resource-constrained hosts (4-core/7.6GB), run the Next.js standalone output directly on the host instead of fighting buildx.

## When to use

- Docker `build` hangs in buildx for 60+ min with no progress
- Host has Node.js 18+ and can run `node` directly
- The app uses `output: "standalone"` in `next.config.ts`
- You need the app running NOW, not after a 2-hour Docker build

## Procedure

### 1. Build on the host

```bash
cd <app-dir>/web
npm install --no-audit --no-fund --legacy-peer-deps
npm run build
# Expect: .next/standalone/ created
```

### 2. Copy static assets into standalone

The standalone server looks for `.next/static` relative to its own directory. Copy it:

```bash
cp -r .next/static .next/standalone/web/.next/static
```

**Critical:** Without this, the page loads as HTML but CSS/JS return 404 (the browser gets a blank page with no styling).

### 3. Start the web server

```bash
cd <app-dir>/web
PORT=3009 API_URL=http://127.0.0.1:4009 node .next/standalone/web/server.js
```

**Path is `.next/standalone/web/server.js`** — NOT `server.js` at the web root. The standalone output nests everything under `.next/standalone/web/`.

### 4. Start the API server (if separate)

```bash
cd <app-dir>/server
API_PORT=4009 node dist/index.js
```

### 5. Verify

```bash
# Web page
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:3009/
# CSS (must be 200, not 404)
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:3009/_next/static/css/*.css
# JS chunks
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:3009/_next/static/chunks/main-app-*.js
# API
curl -s http://127.0.0.1:4009/api/status
```

All must return 200. If CSS/JS returns 404, you forgot step 2.

## Pitfall: CSS/JS return 404 but HTML loads

**Symptom:** `curl http://localhost:3009/` returns 200 with full HTML, but the page renders blank/no styling. Browser console shows 404s on `/_next/static/css/*.css` and `/_next/static/chunks/*.js`.

**Why:** The standalone server resolves `.next/static` relative to its own location (`.next/standalone/web/`). It looks for `.next/standalone/web/.next/static/` but the build only created `.next/static/` at the web root.

**Fix:**

```bash
cp -r .next/static .next/standalone/web/.next/static
```

**Lesson:** Always copy `.next/static` into the standalone output after every `npm run build`. The standalone server won't find it otherwise.

## Pitfall: `Cannot find module 'server.js'`

**Symptom:** `node server.js` fails with `Cannot find module '/path/to/web/server.js'`.

**Why:** The standalone server is at `.next/standalone/web/server.js`, not at the web root. There is no `server.js` at the web root after a standalone build.

**Fix:**

```bash
node .next/standalone/web/server.js
```

**Lesson:** The standalone output nests everything under `.next/standalone/web/`. The entry point is always `.next/standalone/web/server.js`.

## Pitfall: Port already in use after host reboot

**Symptom:** After a reboot, the old process is still holding the port.

**Fix:**

```bash
# Find and kill
ss -tlnp | grep 3009
kill <PID>
# Or use a process manager like pm2/pm2-logrotate
```

**Lesson:** Host-run processes don't auto-restart. Use `pm2` or a systemd service for persistence.

## When to switch back to Docker

Once the host has resources to build Docker images (more RAM, faster CPU, or a build cache), switch back to Docker for:

- Process isolation
- Auto-restart
- Reproducible builds

The Docker build pattern is in the parent SKILL.md.

## Real-world example

**OpenTerminal** (ErTasselli/OpenTerminal) on a 4-core/7.6GB DietPi host:
- Docker `build` hung in buildx for 60+ min (multiple attempts)
- Solution: `npm run build --prefix web` on host, then `node .next/standalone/web/server.js` on port 3009
- API: `node dist/index.js` on port 4009
- Required `cp -r .next/static .next/standalone/web/.next/static` for CSS/JS to load
- Result: Full dashboard with working CSS/JS, no Docker needed