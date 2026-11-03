# Network-constrained terminal bootstrap

Use when building a dashboard/terminal app in Docker and the host has outbound access but build containers cannot reliably reach Debian/PyPI/npm registries.

## Durable pattern

1. Prove the split instead of guessing.
   - host fetch succeeds
   - container/build fetch fails or times out

2. Stop treating dependency installation as the only path.
   - do not keep retrying `apt-get`, `pip install`, or npm builds if the user mainly needs a working artifact

3. Narrow the stack to something that can be built from already-pullable base images.
   - Python stdlib backend
   - static nginx frontend
   - no package install steps in Dockerfile

4. For terminal prototypes, prefer a milestone sequence:
   - `GET /api/health`
   - create/list/read/write terminal session
   - PTY via stdlib (`os.openpty()` works; `pty.openpty()` is the wrong call in Python)
   - browser UI with polling
   - live browser smoke test (`whoami`, `pwd`, etc.)

5. Verify through the public app port, not only internal container routes.

## Why this matters

This converts a blocked build into a real, testable terminal milestone. It is especially useful for clone-first operator UIs where live behavior matters more than framework purity.

## Pitfalls

- Do not call a static shell page "done" until create/read/write works against a real shell.
- Do not claim websocket/xterm parity if the milestone still uses HTTP polling.
- If nginx serves `/` as 403 after copying static files, check file permissions inside the image (`chmod -R a+rX` on the served root can be enough).
- Keep the gap between current milestone and requested parity explicit.
