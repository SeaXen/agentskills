# Hermes reinstall missing web_dist recovery

## Symptom pattern
- gateway comes back on the new `/usr/local/lib/hermes-agent` install
- `hermes_cli.dashboard_auth`, `fastapi`, and `uvicorn` now import successfully
- both services fail with:
  - `--skip-build was passed but no web dist found at: /usr/local/lib/hermes-agent/hermes_cli/web_dist`
- raw ports stay down:
  - dashboard `:9120` connection refused
- nginx/auth proxy port may still answer because proxy is alive even though upstream is down

## Root cause
The official reinstall repaired the Python runtime, but did not leave a built dashboard frontend under:
- `/usr/local/lib/hermes-agent/hermes_cli/web_dist`

If service units still pass `--skip-build`, Hermes refuses to start web surfaces until that dist exists.

## Important diagnostic split
This is a second-layer failure after the earlier service-path / import recovery.

Sequence seen in practice:
1. stale `/usr/local/...` vs uv-tool path mismatch breaks services
2. reinstall fixes imports and reinstalls Hermes under `/usr/local/lib/hermes-agent`

Do not collapse step 3 into "reinstall failed". The Python runtime may already be fixed.

## Recovery pattern
1. Verify imports on the new install first:
   - `/usr/local/lib/hermes-agent/venv/bin/python -c 'import hermes_cli.dashboard_auth, fastapi, uvicorn; print("OK")'`
2. Confirm the actual failure is missing dist from the journal.
3. If a known-good previous packaged dist exists, use it as the fastest recovery path:
   - source example: `/root/.local/share/uv/tools/hermes-agent/lib/python3.12/site-packages/hermes_cli/web_dist`
   - target: `/usr/local/lib/hermes-agent/hermes_cli/web_dist`
5. Verify:
   - `:9120` returns `200`
   - proxy/auth port still points at `:9120`

## Why this workaround is acceptable

## Follow-up note
A source build may still fail later with TS / shared-ui package errors. Capture that as a separate build-path issue; do not undo the runtime recovery while investigating it.
