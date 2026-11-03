---
name: hermes-dashboard-chat-ws-repair
description: Use when Hermes dashboard /chat loads but the embedded TUI chat stays disconnected after an update, especially on LAN/public binds like 0.0.0.0 with --insecure.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, dashboard, tui, websocket, nginx, lan, troubleshooting]
    related_skills: [hermes-agent, dashboard-ui-operations, sagar-hermes-ops]
---

# Hermes Dashboard Chat WS Repair

## Overview
This skill fixes the failure mode where Hermes dashboard `/chat` renders, but the embedded TUI/sidebar stays disconnected.

Typical symptoms:
- `events feed disconnected — tool calls may not appear`
- model badge stays `closed`
- page shell loads, but chat never goes `live`
- often shows up again after `hermes update`

## Why it comes back after updates
If the fix was applied directly inside the installed package under `/usr/local/lib/hermes-agent/...`, a later Hermes update can overwrite those files.

That means the bug is not "randomly returning" — the local patch is being replaced by a fresh package install unless the fix is merged upstream or re-applied automatically.

## When to Use
- Hermes dashboard `/chat` opens but TUI chat is dead
- raw or proxied dashboard works visually but websocket/event feed fails
- LAN/public dashboard was started with `--host 0.0.0.0 --insecure --tui`
- issue appears after updating Hermes

Do not use this skill for:
- dashboard not starting at all
- pure nginx 401/basic-auth problems before page load
- non-TUI dashboards started without `--tui`

## Fast diagnosis
Run these checks first.

```bash
hermes dashboard --status
ss -ltnp | grep -E ':(9119|9120) '
ps -ef | grep '[h]ermes dashboard'
```

Probe raw app paths:

```bash
python3 - <<'PY'
import urllib.request
for url in [
    'http://127.0.0.1:9120/',
    'http://127.0.0.1:9120/chat',
    'http://127.0.0.1:9119/',
    'http://127.0.0.1:9119/chat',
]:
    try:
        with urllib.request.urlopen(url, timeout=8) as r:
            print(url, r.status, r.getheader('content-type'))
    except Exception as e:
        print(url, type(e).__name__, e)
PY
```

Interpretation:
- if `/chat` returns HTML but the UI stays disconnected, keep going
- if loopback websocket works but LAN websocket gets `403`, suspect backend websocket peer policy

## Root-cause patterns
There are two real failure classes here. Check both before declaring the fix.

### Pattern A — websocket peer-policy bug in `web_server.py`
The known bug is in websocket admission logic inside:

- `/usr/local/lib/hermes-agent/hermes_cli/web_server.py`

Bad behavior:
- loopback-only websocket peer checks still apply even when Hermes was explicitly exposed with:
  - `--host 0.0.0.0`
  - `--insecure`

Correct behavior:
- loopback bind → only loopback websocket peers allowed
- auth-gated public mode → remote peers allowed if auth + Host/Origin checks pass
- explicit insecure public bind (`0.0.0.0` / `::` + `--insecure`) → remote peers allowed, while Host/Origin guard stays active

### Pattern B — embedded chat never enabled at dashboard startup
A different breakage looks similar in the browser but the root cause is not websocket peer policy at all.

Files to inspect:
- `/usr/local/lib/hermes-agent/hermes_cli/main.py`
- `/usr/local/lib/hermes-agent/hermes_cli/web_server.py`
- `/usr/local/lib/hermes-agent/web/src/lib/dashboard-flags.ts`

Failure shape:
- `/chat` route renders
- `.xterm` may exist in the DOM because frontend assumes embedded chat is available
- browser console shows PTY/events/ws disconnects or 404s
- HTML bootstrap flag `__HERMES_DASHBOARD_EMBEDDED_CHAT__` is `false`
- backend endpoints like `/api/events`, `/api/ws`, or `/api/pty?mode=chat` return 404

Why it happens:
- frontend currently assumes embedded chat is enabled
- backend startup can still call `start_server(...)` without `embedded_chat=True`
- result: the page shell loads but chat runtime routes are never registered

Fix shape:
- inspect the live `start_server(...)` call in `main.py`
- if dashboard chat is meant to exist, pass `embedded_chat=True`
- restart the dashboard and confirm the bootstrap flag flips to `true`

See `references/embedded-chat-flag-vs-terminal-tab.md` for the exact symptom split and verification sequence.

## Minimal code fix
Patch `_ws_client_is_allowed()` so insecure public bind is treated as explicit opt-in for remote websocket peers.

Target shape:

```python
if getattr(app.state, "auth_required", False):
    return True
bound_host = getattr(app.state, "bound_host", "")
if bound_host in {"0.0.0.0", "::"}:
    return True
client_host = ws.client.host if ws.client else ""
if not client_host:
    return True
return client_host in _LOOPBACK_HOSTS
```

Keep the rest of the security model intact:
- do not remove Host/Origin guard
- do not weaken gated auth flow
- do not make loopback mode remotely reachable

Important inspection rule:
- do **not** stop after a broad grep hit for `0.0.0.0` elsewhere in `web_server.py`
- inspect the live body of `_ws_client_is_allowed()` itself; a nearby helper like `_is_accepted_host()` may already mention all-interfaces binds while the actual websocket peer gate still rejects remote clients
- this exact split can make you think the fix is already present when the live websocket path is still broken

## Regression test
Add a test in:

- `/usr/local/lib/hermes-agent/tests/hermes_cli/test_dashboard_auth_ws_auth.py`

Expected cases:
- gated public auth mode:
  - `auth_required = True`
  - remote `client_host` like `203.0.113.7`
  - valid `Host` + `Origin`
  - `_ws_request_is_allowed(...) is True`
- insecure public bind mode:
  - `auth_required = False`
  - `bound_host = "0.0.0.0"`
  - remote `client_host` like `192.168.0.55`
  - valid `Host` + `Origin`
  - `_ws_request_is_allowed(...) is True`

Run:

```bash
/usr/local/lib/hermes-agent/venv/bin/python -m pytest \
  /usr/local/lib/hermes-agent/tests/hermes_cli/test_dashboard_auth_ws_auth.py -q
```

Important pitfall:
- the pre-existing targeted test file can already pass while still missing the `--host 0.0.0.0 --insecure --tui` case
- do not treat `pytest ... test_dashboard_auth_ws_auth.py` passing as proof the LAN/NAS TUI path is covered until you confirm there is an explicit insecure-public-bind regression case

## Live verification
After patching, verify all three layers.

### 1. Browser/UI
Open:
- `http://<lan-ip>:9120/chat`

Healthy signs:
- badge shows `live`
- no `events feed disconnected`
- model no longer stuck at `closed`

### 2. Raw websocket
Use a valid dashboard session token and verify both endpoints open:
- `/api/ws?token=...`
- `/api/events?token=...&channel=...`

If loopback works but LAN returns `403`, the fix is not really applied.

### 3. Proxy path
If nginx fronts `9119`, confirm websocket proxying is correct and compare raw `9120` vs proxied `9119`.

Known good nginx shape:
- `location /` proxies to `127.0.0.1:9120`
- `/api/(pty|ws|events|pub)` has websocket upgrade headers
- if using basic auth, those websocket paths may need `auth_basic off`

## Operational rule after future Hermes updates
If the bug returns after `hermes update`, assume the package reinstall overwrote the local patch first.

Repair order:
1. verify listener/process state
2. verify `/chat` shell vs websocket behavior
3. inspect `/usr/local/lib/hermes-agent/hermes_cli/web_server.py`
4. re-apply the minimal `_ws_client_is_allowed()` fix if missing
5. rerun the targeted pytest file
6. verify live browser state on `9120/chat`

## Better long-term fix
Best solution is to upstream the patch so updates stop removing it.

Until then, treat this skill as the re-apply playbook.

## Local one-command wrapper
This skill ships a reapply helper script at:

- `scripts/reapply_fix.py`

Recommended operator convenience wrapper:

```bash
#!/usr/bin/env bash
set -euo pipefail
exec python3 /root/.hermes/skills/devops/hermes-dashboard-chat-ws-repair/scripts/reapply_fix.py "$@"
```

Install it as a PATH command, for example `~/bin/fix-hermes-chat` or `~/.local/bin/fix-hermes-chat`.

Why this matters:
- Hermes updates can overwrite local package patches
- the repair workflow should be a single operator command, not a remembered sequence
- the helper should be idempotent: if the fix is already present, it should just run verification and exit cleanly

## Common Pitfalls
1. Blaming nginx first when raw `:9120` already fails the same way.
2. Treating HTML page load as proof chat runtime is healthy.
3. Removing Host/Origin protection instead of fixing peer-policy logic.
4. Restarting the wrong dashboard process while another old process still owns the port.
5. Running `python -m pytest` outside the Hermes venv and concluding tests are broken.

## Verification Checklist
- [ ] `/chat` renders
- [ ] raw LAN websocket to `/api/ws` opens
- [ ] raw LAN websocket to `/api/events` opens
- [ ] browser state shows `live`
- [ ] targeted pytest file passes
- [ ] active dashboard process on the target port is the intended one
