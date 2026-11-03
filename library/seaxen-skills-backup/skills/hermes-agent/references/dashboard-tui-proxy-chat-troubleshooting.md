# Dashboard TUI chat behind LAN/proxy — troubleshooting pattern

Use this when:
- `/chat` loads but shows `events feed disconnected`
- tool calls do not appear in dashboard chat
- `127.0.0.1:9120` works but `:9119` auth-proxy path does not
- LAN IP cannot open the raw dashboard port

## Fast diagnosis

1. Identify which process owns which port:
```bash
ss -ltnp | grep -E ':(9119|9120) '
ps -ef | grep '[h]ermes dashboard'
```

Typical healthy split:
- `9119` = nginx reverse proxy with auth
- `9120` = raw Hermes dashboard app

2. Compare raw app vs proxy paths:
```bash
python3 - <<'PY'
import urllib.request
for url in [
    'http://127.0.0.1:9119/',
    'http://127.0.0.1:9119/chat',
    'http://127.0.0.1:9120/',
    'http://127.0.0.1:9120/chat',
]:
    try:
        with urllib.request.urlopen(url, timeout=8) as r:
            print(url, r.status, r.getheader('content-type'))
    except Exception as e:
        print(url, type(e).__name__, e)
PY
```

Interpretation:
- `9119` returning `401` is expected if nginx basic auth is enabled
- `9120/chat` returning `200` proves the raw app serves the chat route
- if authenticated `9119/chat` still breaks while `9120/chat` works, treat it as a proxy config issue first

3. Confirm the live dashboard process really has TUI enabled:
```bash
hermes dashboard --help | sed -n '1,80p'
hermes dashboard --status
ps -ef | grep '[h]ermes dashboard'
```

The working listener must be started with `--tui`. A stale non-TUI process holding the port is a common cause of `/chat` appearing but not functioning.

## LAN binding fix

If `http://127.0.0.1:9120/` works but `http://<lan-ip>:9120/` does not:
```bash
hermes dashboard --stop
hermes dashboard --host 0.0.0.0 --port 9120 --insecure --tui --no-open
ss -ltnp | grep 9120
hostname -I
```

Expect `0.0.0.0:9120`, not `127.0.0.1:9120`.

## nginx proxy config for chat stability

Known-good baseline when proxying `9119 -> 127.0.0.1:9120`:

```nginx
server {
    listen 9119;
    listen [::]:9119;
    server_name _;

    auth_basic "Hermes Dashboard";
    auth_basic_user_file /etc/nginx/.htpasswd-hermes;

    location / {
        proxy_pass http://127.0.0.1:9120;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_cache_bypass $http_upgrade;
        proxy_buffering off;
        proxy_request_buffering off;
        proxy_read_timeout 86400;
        proxy_send_timeout 86400;
    }
}
```

Reload after edits:
```bash
nginx -t && nginx -s reload
```

## Verification checklist

- `ss -ltnp` shows `0.0.0.0:9120` owned by Hermes
- dashboard process command line includes `--tui`
- `http://<lan-ip>:9120/api/status` returns `200`
- authenticated `http://<proxy-host>:9119/chat` no longer shows `events feed disconnected`
- hard refresh / private window tested after proxy changes

## Common root causes seen together

1. Raw dashboard bound only to localhost
2. Auth proxy forwarding to a non-TUI dashboard process
3. nginx proxy good enough for normal pages but missing settings needed for stable chat websocket/event flow
