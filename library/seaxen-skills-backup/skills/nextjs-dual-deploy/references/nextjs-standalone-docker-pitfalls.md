# Next.js standalone Docker — pitfalls and recovery patterns

Concrete notes from building Next.js apps that deploy to Docker with `output: "standalone"`. Each pitfall below is something that has failed in production builds and has a verified fix.

## Pitfall 1: `COPY failed: stat app/public: file does not exist`

**Symptom:**

```
Step 15/20 : COPY --from=builder /app/public ./public
COPY failed: stat app/public: file does not exist
```

**Why:** Next.js standalone output copies only `public/`, `.next/standalone/`, and `.next/static/` from the builder. If your repo has no `public/` directory at all (not even an empty one), the COPY fails — Docker treats a missing source as a hard error, not a warning.

**Fix:**

```bash
mkdir -p public
touch public/.gitkeep     # OR copy any asset like public/favicon.svg
```

Verify with `ls public/` before `docker build`. The folder must exist at build time, even if empty.

**Lesson:** This bit the Tradingx scaffold on first build. Always create `public/` immediately after `mkdir app`, before any `npm install` or `docker build`.

## Pitfall 2: `npm ci` fails with `ETIMEDOUT` in Docker build

**Symptom:**

```
npm error code ETIMEDOUT
npm error errno ETIMEDOUT
npm error network request to https://registry.npmjs.org/undici-types/-/undici-types-6.21.0.tgz failed
```

**Why:** The Docker bridge network (default) cannot reach `registry.npmjs.org` from inside the build container. The host can (you've been running `npm install` fine on the host), but the bridge subnet has restricted DNS or no outbound NAT to the internet.

**Fix — Option A (preferred, no daemon config):**

```bash
docker build --network=host -t <app>:latest .
```

This forces the build container to use the host's network namespace, including the host's DNS resolver and routing table. `npm ci` then resolves the registry just like it does on the host.

**Fix — Option B (in-Dockerfile registry mirror, works inside CI / buildx / remote daemons):**

```dockerfile
RUN npm config set registry https://registry.npmmirror.com \
 && npm config set fetch-retries 5 \
 && npm config set fetch-retry-mintimeout 20000 \
 && npm config set fetch-retry-maxtimeout 120000

COPY package.json package-lock.json* ./
RUN npm ci --no-audit --no-fund --legacy-peer-deps
```

The `registry.npmmirror.com` (Alibaba) mirror is a fast, drop-in replacement for `registry.npmjs.org` from most regions. Apply the `npm config set` lines BEFORE the `COPY package.json` step so the mirror is used for every package fetch. This is the only fix that works when `--network=host` is unavailable (CI runners, buildx, remote Docker daemons) or when the host's own network is also flaky.

**Fix — Option C (daemon-level):**

Edit `/etc/docker/daemon.json`:

```json
{
  "registry-mirrors": ["https://your-mirror.example.com"]
}
```

Then `sudo systemctl restart docker`. After this, `docker build` (without `--network=host`) hits the mirror.

**Lesson:** Try `--network=host` first. It's a one-flag fix and doesn't require daemon changes. If you control the host, leaving it as default (`bridge`) is correct — only override per-build for offline-isolation scenarios. If the host is also behind a slow link, skip `--network=host` and go straight to Option B (in-Dockerfile mirror) so the build is reproducible on any host.

## Pitfall 2b: `npm ci` "succeeds" but `next: not found` at `npm run build`

**Symptom:** The build advances past the install step (no error, no ETIMEDOUT this time) and dies at `RUN npm run build`:

```
> next build
sh: next: not found
The command '/bin/sh -c npm run build' returned a non-zero code: 127
```

**Why:** The install completed but produced a *partial* `node_modules`. `next` isn't where `npm run build` expects it. Common triggers:

- `(npm ci || npm install)` Dockerfile pattern — when `npm ci` fails once, the `||` falls through to `npm install` which is lenient and "succeeds" with a half-installed tree. You lose the failure signal and only see the downstream `next: not found`.
- `npm ci --legacy-peer-deps` combined with a peer-dep conflict that silently drops a top-level package (rare but possible with `next` itself if the resolved `react` version doesn't match its peer).
- The previous build's `.npm` cache (from a partial install) got reused; some packages extracted, some didn't.
- `npm config set fetch-retries N` with N>0 retries a failed package mid-install, but if the retry eventually "succeeds" with corrupted bytes the install completes without error.

**Fix — diagnose first, then re-install cleanly:**

```bash
# 1. Confirm what's actually missing in the failed build's node_modules
docker run --rm -it <builder-stage-image> sh -c \
  'echo "--- .bin/next ---"; ls /app/node_modules/.bin/next 2>&1; \
   echo "--- next/dist ---"; ls /app/node_modules/next/dist/ 2>&1 | head; \
   echo "--- top-level ---"; ls /app/node_modules/ | head -20'
```

- If `next/dist/` exists but `.bin/next` is missing → the install finished but the bin symlink wasn't created. Run `npm rebuild next` after install.
- If `next/` is missing entirely → install was partial. Wipe caches and re-install.

**Clean Dockerfile fix:**

```dockerfile
RUN npm config set fetch-retries 5 \
 && rm -rf /app/node_modules /root/.npm \
 && npm ci --no-audit --no-fund --legacy-peer-deps \
 && test -x /app/node_modules/.bin/next || npm rebuild next
```

The `test -x` check is a defensive verification: if the bin symlink wasn't created, the build fails *here* with a clear message, not silently downstream at `npm run build`.

**Avoid the silent-fallback pattern:**

```dockerfile
# BAD — masks real errors, gives you `next: not found` downstream
RUN (npm ci --no-audit --no-fund || npm install --no-audit --no-fund)

# GOOD — let npm ci fail loudly so the real error shows
RUN npm ci --no-audit --no-fund --legacy-peer-deps

# GOOD (acceptable) — if you must have a fallback, use the same flags + clean state
RUN rm -rf /app/node_modules \
 && (npm ci --no-audit --no-fund --legacy-peer-deps \
     || npm install --no-audit --no-fund --legacy-peer-deps)
```

**Lesson:** `next: not found` is a load-bearing diagnostic. It always means the install was partial, never a code-side issue. The exit code from `npm ci` is necessary but not sufficient — the only reliable signal is `node_modules/.bin/next` existing on disk before the build step. If you see this error in a CI log, the previous install step is the actual failure; re-run with verbose flags (`npm ci --verbose`) to see what was skipped.

## Pitfall 3: Container listens but host port mapping returns nothing

**Symptom:**

```
$ docker run -d -p 8799:8799 <app>
$ curl http://localhost:8799
curl: (7) Failed to connect to localhost port 8799: Connection refused
```

But:

```
$ docker exec <app> wget -qO- http://127.0.0.1:8799
{"ok":true,"app":"...","version":"0.1.0",...}
```

**Why:** Next.js binds to `localhost` (IPv4 `127.0.0.1`) by default, even when port mapping is configured. The container accepts traffic on `127.0.0.1:8799` from inside, but rejects traffic from outside the container's namespace — including from the host via the mapped port.

**Fix:**

Set `HOSTNAME=0.0.0.0` in either the runner stage env OR the docker-compose `environment:` block:

```dockerfile
ENV HOSTNAME=0.0.0.0
```

```yaml
environment:
  - HOSTNAME=0.0.0.0
```

Or pass it to `next start`:

```bash
HOSTNAME=0.0.0.0 npm run start
```

**Verification after fix:**

```bash
ss -tln | grep 8799
# Should show:
# LISTEN 0  511  *:8799  *:*
# (the "*" means binding to all interfaces, not just 127.0.0.1)
```

If you see `127.0.0.1:8799` or `localhost:8799`, the bind is still local-only.

**Lesson:** This bit Tradingx on first container run. Add `HOSTNAME=0.0.0.0` to both Dockerfile and docker-compose.yml from the start — it's a 30-second fix, but the symptom (silent port refusal) is hard to diagnose without `ss -tln`.

## Pitfall 4: Port already in use — silent picking of a different port

**Symptom:** You bind to 8799, but the previous Tradingx dev server is still running on 8799. The new process either fails to start or the user can't tell which port is actually serving.

**Don't:** Silently switch to 8798 or 8797 — the user asked for 8799, honor it.

**Fix:**

```bash
ss -tln | grep 8799         # what listens on 8799?
fuser 8799/tcp               # which PID?
lsof -i :8799                # alt
# Then kill the conflicting PID:
kill -9 <PID>
```

For trading/dev iteration, the dev server is usually a background process from a previous session. Kill it before starting a new one.

**Lesson:** When the user gives a specific port, treat it as a hard requirement. If the port is in use, surface it (`"Port 8799 is held by another process — should I kill it or pick a different port?"`), don't unilaterally change it.

## Pitfall 5: Docker image is 1 GB instead of expected ~250 MB

**Symptom:** `docker images <app>:latest` shows ~1 GB even though `output: "standalone"` should produce a slim image.

**Why:** You forgot the multi-stage Dockerfile. Without the `runner` stage, Docker builds the full image on top of `node:20-alpine` (~150 MB) plus your source plus `node_modules` plus `.next` build cache (~800 MB). The standalone trick only works if you `COPY --from=builder` selectively.

**Fix:** Use the multi-stage Dockerfile in the parent SKILL.md. Specifically, the runner stage must `COPY` only:

- `public/` from builder
- `.next/standalone/` from builder (contains the bundled `server.js`)
- `.next/static/` from builder (static assets)

Do NOT `COPY .next .next` — that copies the entire build cache including dev server modules.

**Verification:**

```bash
docker images <app>:latest --format "{{.Size}}"
# Expect: ~150-300 MB for a typical app
# If you see 800 MB+, the multi-stage setup is wrong
```

## Pitfall 6: `next build` succeeds but `next start` shows blank page on a route

**Symptom:** Browser navigates to `/trades`, page is white. Browser console shows hydration error like "Hydration failed because the initial UI does not match what was rendered on the server."

**Why:** A Server Component is importing a Client Component without the `"use client"` directive at the top of the Client Component file, OR a Client Component is using browser-only APIs (window, localStorage, document) during initial render.

**Fix:** Check the file tree:

- `app/page.tsx` is a Server Component by default (no directive needed).
- `components/Sidebar.tsx` uses `usePathname()` → must have `"use client"` at the top.
- `components/StatCard.tsx` is pure → can be a Server Component, no directive needed.
- `components/CalendarGrid.tsx` uses `useState`/`useMemo` → must have `"use client"`.

Rule: leaf components that use React hooks or event handlers must be Client Components. Anything else can stay as a Server Component for better perf.

**Verification:** Open browser DevTools → Console → look for hydration errors. They name the exact file/component causing the mismatch.

## Pitfall 7: Healthcheck fails immediately after container start

**Symptom:** `docker ps` shows container as `unhealthy` within seconds of starting. `docker logs <container>` shows the server started, but `wget http://127.0.0.1:8799/api/health` from the healthcheck command times out.

**Why:** Two common causes:

1. `HOSTNAME=0.0.0.0` is not set, so the server binds to localhost only — see Pitfall 3. Healthcheck runs from `127.0.0.1` so it should work, but combined with other binding issues it can fail.
2. `start_period: 15s` is too short. The Next.js standalone image takes 10-15s to initialize the first request (compiling routes on demand, etc.).

**Fix:**

```yaml
healthcheck:
  test: ["CMD", "wget", "-qO-", "http://127.0.0.1:8799/api/health || exit 1"]
  interval: 30s
  timeout: 5s
  retries: 3
  start_period: 15s    # wait 15s before first check
```

If 15s isn't enough, bump to 30s. The healthcheck is informational — don't set it too aggressively or you'll get false negatives during normal startup.

## Pitfall 8: Vercel deploy succeeds, but `npm run build` locally fails

**Symptom:** `vercel --prod` returns success, but `npm run build` on the host throws "Module not found" or "Cannot find package 'X'".

**Why:** Vercel installs dependencies with its own resolver (often a slightly different version of `npm` or a cached lockfile). Your local `node_modules` might be stale or have a different lockfile state.

**Fix:**

```bash
rm -rf node_modules .next
npm ci           # install from package-lock.json exactly
npm run build    # re-test
```

If `npm ci` succeeds but `npm run build` still fails, you have a code issue — Vercel's success was a lucky cache hit. Fix the build locally, then redeploy.

**Lesson:** Don't trust Vercel success as proof of correctness. Always run `npm run build` locally before committing.

## Pitfall 9: Re-running `docker run --rm -d --name X` while the old X still runs — silent stale container

**Symptom:**

```bash
$ docker run --rm -d --name tradingx-test -p 8799:8799 tradingx:latest
$ curl http://localhost:8799
→ HTTP 200 (responds — but from the OLD container)
$ docker ps --filter "name=tradingx-test" --format "{{.Status}}"
→ Up 10 hours           ← old one, not your new build
$ docker logs tradingx-test 2>&1 | tail
→ Error: No such container: tradingx-test
```

The new container's `node server.js` fails to bind 8799, but `-d` daemonizes before the error is printed. The old container keeps serving, so `curl` returns 200 from stale code.

**Why:** `--rm` only triggers when the container *exits*. If the new container fails at start (port bind, OOM, init error), it never reaches the "running" state but it doesn't print to your terminal either. The old container continues untouched.

**Fix — always remove before re-creating:**

```bash
# Pattern 1: throwaway test container
docker rm -f tradingx-test 2>/dev/null || true
docker run --rm -d --name tradingx-test -p 8799:8799 tradingx:latest
sleep 4
docker ps --filter "name=tradingx-test" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
# ↑ verify Status shows "Up X seconds" (not "Up 10 hours" from before)
```

```bash
# Pattern 2: persistent service (use compose)
docker compose -f /path/to/docker-compose.yml up -d --force-recreate <service>
```

**Verification after every restart — three checks:**

1. `docker ps` shows the new container with a fresh `CreatedAt` (e.g. "About a minute ago").
2. `curl http://localhost:PORT/api/health` returns the version string you just bumped.
3. `docker logs <name> --since 30s` shows the new container's startup logs (Next.js ready line, port bound, etc.).

**Lesson:** Never trust `curl 200` after a `docker run` as proof your new image is deployed. The `CreatedAt` column in `docker ps` is the source of truth.

## Verification recipe (paste this after every build)

```bash
# 1. Native build + serve (background)
cd /path/to/app
npm run build && HOSTNAME=0.0.0.0 PORT=8799 npm run start &
APP_PID=$!
sleep 4

# 2. Curl every route
for path in / /<page1> /<page2> /api/health; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8799$path")
  echo "$path → HTTP $code"
done

# 3. Verify /api/health JSON
curl -s http://localhost:8799/api/health | python3 -m json.tool

# 4. Verify port binding (should show *:8799, not 127.0.0.1:8799)
ss -tln | grep 8799

# 5. Stop native, build Docker
kill $APP_PID
docker build --network=host -t <app>:latest .

# 6. Run container (background)
docker run --rm -d --name <app>-test -p 8799:8799 <app>:latest
CONTAINER_PID=$(docker inspect --format '{{.State.Pid}}' <app>-test)
sleep 4

# 7. Re-curl all routes (now through container's port mapping)
for path in / /<page1> /<page2> /api/health; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8799$path")
  echo "[docker] $path → HTTP $code"
done

# 8. Container health
docker ps --filter "name=<app>-test" --format "{{.Names}} {{.Status}}"

# 9. Cleanup
docker stop <app>-test
```

If every step prints HTTP 200 and the container status is `Up X minutes (healthy)`, you're done. Any 5xx, blank page, or `unhealthy` is a real bug — debug before claiming success.