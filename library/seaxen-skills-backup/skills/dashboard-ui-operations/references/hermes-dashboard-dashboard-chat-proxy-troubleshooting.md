# Hermes dashboard chat / proxy troubleshooting

Use this when the dashboard shell loads but the Chat tab says `events feed disconnected`, tool calls do not appear, or the raw dashboard port works while the reverse-proxy port fails.

## Tested endpoint map

The embedded chat uses multiple websocket endpoints, not one:

- `/api/pty?token=<session>` — PTY bridge for the terminal UI
- `/api/ws?token=<session>` — JSON-RPC sidecar for structured metadata
- `/api/pub?token=<session>&channel=<id>` — PTY-side publish channel
- `/api/events?token=<session>&channel=<id>` — browser event feed

The page also exposes runtime globals such as:
- `window.__HERMES_SESSION_TOKEN__`
- `window.__HERMES_DASHBOARD_EMBEDDED_CHAT__`

## What usually breaks

1. Raw dashboard works, proxy path fails
   - nginx auth on the whole server block can block websocket handshakes
   - browsers do not reliably send basic-auth credentials on websocket upgrades

2. PTY opens, event feed is disconnected
   - `/api/pty` is fine but `/api/ws`, `/api/pub`, or `/api/events` is blocked

3. Browser loads old content
   - hard refresh or private window may be needed after changing proxy rules

4. Plugin noise is a red herring
   - a failed plugin load can appear in console, but it is not the same as the embedded chat transport failing

## Fast checks

```bash
ss -ltnp | grep -E ':(9119|9120) '
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

Browser-side websocket probe for the PTY path:

```js
new WebSocket(`ws://127.0.0.1:9120/api/pty?token=${window.__HERMES_SESSION_TOKEN__}`)
```

Expected behavior:
- direct raw app port should open
- proxy path should work only if auth and websocket handling are configured for the chat endpoints

## Proxy fix pattern

If nginx protects the dashboard with basic auth, do not assume websocket upgrades can use the same auth model.
A common fix is:
- keep auth on `/`
- exempt `/api/pty`, `/api/ws`, `/api/pub`, and `/api/events` from auth
- preserve websocket upgrade headers

## Reference notes

See the `hermes-dashboard` skill for the class-level workflow and the exact endpoint split.
