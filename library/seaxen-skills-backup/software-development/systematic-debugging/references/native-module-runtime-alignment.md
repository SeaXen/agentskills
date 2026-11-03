# Native module runtime alignment for host-built Docker packaging

Use this when a Node app builds successfully on the host but fails inside Docker with native-module errors.

## Symptom pattern

Typical chain:
1. App builds on host.
2. Docker image packages host-built artifacts (for example Next.js standalone output).
3. Container starts but routes return 500 or healthcheck fails.
4. Logs show one of these:
   - `Could not locate the bindings file`
   - `ERR_DLOPEN_FAILED`
   - `version 'GLIBC_x.xx' not found`
   - native addon path references like `better_sqlite3.node`

## Root-cause checklist

Check all three axes before changing app code:

### 1) Node ABI mismatch
- Host-built addon compiled for Node A, container runs Node B.
- Clue: binding path mentions the wrong ABI / Node major.
- Fix: align container Node major to the host build OR rebuild the native module inside the container for the target Node version.

### 2) libc mismatch
- Host build on glibc, container on musl (Alpine), or older glibc than host.
- Clues:
  - Alpine container + host-built `.node`
  - `GLIBC_2.38 not found` / similar
- Fix: prefer a runtime base compatible with the host-built binary. If the host built against newer glibc, use a newer Debian/Ubuntu base (for example `node:<major>-trixie-slim` instead of older `bookworm`).

### 3) packaging omission
- Standalone/server bundle copied without its runtime `node_modules` subtree.
- Clue: app starts, then `Cannot find module 'next'` or missing addon folder inside the image.
- Fix: inspect the built artifact tree directly and confirm copied paths survive `.dockerignore` rules.

## Safe debugging order

1. Verify the app boots on the host first.
2. Inspect container logs before touching code.
3. Identify whether failure is:
   - missing JS dependency,
   - missing native binding,
   - ABI mismatch,
   - libc mismatch.
4. Fix runtime alignment before changing application logic.
5. Re-verify with:
   - container health status,
   - home page HTTP 200,
   - health endpoint 200,
   - no restart loop.

## Practical lessons from this session

- Packaging host-built Next standalone output can work well, but only if the runtime image matches the host-built native dependencies.
- Avoid Alpine when reusing host-built glibc artifacts.
- If the container network is flaky for package installs, remove unnecessary `apt/apk` steps and avoid depending on extra healthcheck binaries like `wget`.
- A Node-based healthcheck (`node -e ...`) avoids package-manager dependency for readiness checks.

## Strong default

For host-built Node 25 + glibc artifacts, prefer a matching Debian-family runtime image first, then verify logs and health before any UI debugging.
