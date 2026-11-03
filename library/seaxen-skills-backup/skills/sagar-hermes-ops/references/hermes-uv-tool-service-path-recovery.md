# Hermes uv-tool service-path recovery

## Symptom pattern
- `hermes --version` works from `~/.local/bin/hermes`
- `hermes gateway status` or systemd shows `status=203/EXEC`
- unit files still reference old paths like:
  - `/usr/local/bin/hermes`
  - `/usr/local/lib/hermes-agent/venv/bin/python`
  - `/usr/local/lib/hermes-agent/venv/bin/hermes`
- nginx/public dashboard port may still answer, but only because the proxy is alive while the upstream Hermes dashboard process is dead

## Root cause
A reinstall changed the live Hermes binary/layout to the uv tool path, while existing systemd units still point at the old source/venv install.

Typical working uv-tool path on this host shape:
- binary: `/root/.local/bin/hermes`
- venv python: `/root/.local/share/uv/tools/hermes-agent/bin/python`
- package root: `/root/.local/share/uv/tools/hermes-agent/lib/python3.12/site-packages`

## Recovery sequence
1. Verify the new live CLI path:
   - `command -v hermes`
   - `readlink -f ~/.local/bin/hermes`
2. Inspect service units before changing anything:
   - `systemctl --user cat hermes-gateway.service`
   - `systemctl cat hermes-dashboard.service`
3. If units still point at `/usr/local/...`, patch them to the current Hermes binary and a sane PATH.
4. Reload both managers:
   - `systemctl --user daemon-reload`
   - `systemctl daemon-reload`
5. Restart and verify separately:
   - gateway status/unit
   - live listeners on expected ports
   - journal output for the next blocking error

## Important diagnostic split
After fixing stale ExecStart paths, the next failure may be a packaging/runtime issue, not a systemd issue.

Examples seen in this class of outage:
- first failure: `status=203/EXEC` because unit points at dead `/usr/local/...` path
- next failure after path fix: Python import errors from the new install

Do not stop after the first fix. Always read the journal again after restart.

## Operator rule
Treat this as a two-layer recovery:
1. service path mismatch
2. package/runtime completeness

If layer 1 is fixed and layer 2 still fails, report them separately so the user knows what was restored and what remains broken.
