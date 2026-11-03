# Host-built standalone packaging for Next.js apps with native Node modules

Use this when a Next.js app has `output: "standalone"`, Docker builds have flaky outbound network, and the app depends on a native Node module such as `better-sqlite3`, `sharp`, or `canvas`.

## Problem shape

Typical failure chain:

1. Docker `npm ci` times out or partially installs packages.
2. Build step fails with `next: not found`.
3. Switching to host-built `.next/standalone/` gets past the build.
4. Runtime then fails because the native module binary does not match the container runtime.

These are different failures. Do not conflate them.

## Reliable pattern

### 1. Build on the host

```bash
npm install --no-audit --no-fund --legacy-peer-deps --ignore-scripts
npm rebuild better-sqlite3     # replace with the actual native module as needed
npm run build
```

For Node-native modules, explicitly rebuilding on the host is important. `--ignore-scripts` avoids fragile postinstall work during install, and `npm rebuild <module>` restores just the native binary step.

### 2. Package only the runtime artifacts in Docker

Copy only:
- `.next/standalone/`
- `.next/static/`
- `public/`

Do not run `npm ci` again in the Dockerfile if Docker networking is the weak point.

### 3. Match runtime to the host build

Check three dimensions:
- **Node major / ABI**
- **libc family** (`glibc` vs `musl`)
- **distro generation** (older Debian vs newer Debian)

#### Failure signatures

- **ABI mismatch**
  - errors like `Could not locate the bindings file`
  - or `node-v115` vs `node-v127` mismatch paths
- **libc mismatch**
  - errors like `GLIBC_2.38 not found`
- **musl/glibc mismatch**
  - common when host builds on Debian/Ubuntu and runtime is `node:alpine`

### 4. Prefer Debian runtime when the host build was Debian

If the host build succeeds on a Debian-family host, prefer a Debian Node image close to the host generation.

Example progression from a real session:
- `node:20-alpine` → wrong ABI + musl mismatch
- `node:25-bookworm-slim` → ABI fixed, glibc still too old
- `node:25-trixie-slim` → runtime healthy

## Healthchecks without package-manager installs

If apt/apk inside Docker is also flaky, do not install `wget` or `curl` just for healthchecks.

Use Node itself:

```yaml
healthcheck:
  test:
    [
      "CMD",
      "node",
      "-e",
      "require('http').get('http://127.0.0.1:8799/api/health',r=>process.exit(r.statusCode===200?0:1)).on('error',()=>process.exit(1))"
    ]
```

This removes a whole class of mirror/apt failures.

## Verification checklist

After packaging:

```bash
docker inspect <container> --format 'Status={{.State.Status}} Health={{.State.Health.Status}} Restarting={{.RestartCount}}'
curl -s -D - http://127.0.0.1:<port>/api/health
curl -s -o /tmp/body -D /tmp/hdr http://127.0.0.1:<port>/
docker logs --tail 50 <container>
```

Success means:
- container is `running`
- health is `healthy`
- restart count is stable at 0
- `/api/health` returns 200 with `db.ok: true`
- home page returns 200
- no native-module loader errors in logs

## LocalStorage caveat during browser verification

If the app stores display/demo preferences in browser localStorage, browser-tool session resets can make it look like a demo-data bug reappeared after deploy.

Verify demo/off behavior **within the same browser session** where you toggle the setting. If you re-navigate in a fresh browser session, defaults may return until localStorage is changed again. That is a test-session artifact, not necessarily an app regression.
