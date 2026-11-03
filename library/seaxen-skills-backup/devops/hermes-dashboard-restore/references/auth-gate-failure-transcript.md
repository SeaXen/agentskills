# Hermes 9119 auth-gate failure — exact transcript

This is the canonical failure transcript captured during the 2026-07-08 recovery on DietPi with Hermes Agent v0.18.1. If your journalctl output matches, follow the SKILL.md quick-restore steps.

## Symptoms

`systemctl status hermes-dashboard.service`:
```
● hermes-dashboard.service - Hermes Agent Dashboard (9119 - with auth)
     Loaded: loaded (/etc/systemd/system/hermes-dashboard.service; enabled; preset: enabled)
     Active: activating (auto-restart) (Result: exit-code) since Wed 2026-07-08 09:17:56 +06; 9s ago
 Invocation: 03e56eea12af47bc94c40b76e08f94f4
    Process: 3561942 ExecStart=/usr/local/bin/hermes dashboard --host 0.0.0.0 --port 9119 --skip-build --no-open (code=exited, status=1/FAILURE)
```

`journalctl -u hermes-dashboard.service -n 50`:
```
hermes[...]:   Bitwarden Secrets Manager: applied 25 secrets (BRAVE_SEARCH_API_KEY, CLOUDFLARE_API_TOKEN, ...)
hermes[...]: → Skipping web UI build (--skip-build); using dist at /usr/local/lib/hermes-agent/hermes_cli/web_dist
hermes[...]: Refusing to bind dashboard to 0.0.0.0 — the auth gate engages on non-loopback binds, but no auth providers are registered.
hermes[...]: Configure an auth provider before exposing the dashboard:
hermes[...]:   • Password: set dashboard.basic_auth.username + password_hash in config.yaml
hermes[...]:     (hash with: python -c "from plugins.dashboard_auth.basic import hash_password; print(hash_password('your-password'))")
hermes[...]:   • OAuth: run `hermes dashboard register` (Nous Portal) or install a DashboardAuthProvider plugin.
hermes[...]: There is no unauthenticated public-bind option — to keep it local, bind 127.0.0.1 and tunnel in (SSH / Tailscale).
systemd[1]: hermes-dashboard.service: Main process exited, code=exited, status=1/FAILURE
```

The systemd unit file (`/etc/systemd/system/hermes-dashboard.service`):
```ini
[Service]
ExecStart=/usr/local/bin/hermes dashboard --host 0.0.0.0 --port 9119 --skip-build --no-open
```

The `dashboard.basic_auth` block in `~/.hermes/config.yaml` was all empty:
```yaml
dashboard:
  basic_auth:
    username: ''
    password_hash: ''
    password: ''
    secret: ''
    session_ttl_seconds: 0
```

This is the post-update drift: the update landed before `hermes update -y` finished writing back the auth block, or the user previously set it via a path that the update didn't preserve.

## Recovery commands (exact, copy-paste)

```bash
# 1. Generate the hash and a secret (output is your hash and a fresh secret)
PYTHONPATH=/usr/local/lib/hermes-agent \
  /usr/local/lib/hermes-agent/venv/bin/python - <<'PY'
import secrets
from plugins.dashboard_auth.basic import hash_password
print('HASH=' + hash_password('opop@9900'))
print('SECRET=' + secrets.token_hex(32))
PY

# 2. Apply via the only path the agent is allowed to write config with
hermes config set dashboard.basic_auth.username sagar
hermes config set dashboard.basic_auth.password_hash 'scrypt$N$N$8$1$...$...'
hermes config set dashboard.basic_auth.password ''
hermes config set dashboard.basic_auth.secret '<paste-secret-from-step-1>'
hermes config set dashboard.basic_auth.session_ttl_seconds 43200

# 3. Restart and confirm
systemctl restart hermes-dashboard.service
sleep 5
ss -tlnp | grep ':9119\b'
# expect: LISTEN 0 2048 0.0.0.0:9119 ... users:(("hermes",pid=...,fd=7))
```

## Login probe — proves the hash verifies

```bash
rm -f /tmp/hermes-cookies.txt
curl -sS -c /tmp/hermes-cookies.txt \
  -H 'Content-Type: application/json' \
  -d '{"provider":"basic","username":"sagar","password":"opop@9900","next":"/"}' \
  http://127.0.0.1:9119/auth/password-login
# expect: {"ok":true,"next":"/"}

curl -sS -b /tmp/hermes-cookies.txt http://127.0.0.1:9119/api/auth/me
# expect: {"user_id":"sagar","email":"","display_name":"sagar","org_id":"","provider":"basic","expires_at":...}
```

Wrong-password probe — must be a generic 401 (no user-vs-password oracle leak):
```bash
curl -sS -H 'Content-Type: application/json' \
  -d '{"provider":"basic","username":"sagar","password":"WRONG"}' \
  http://127.0.0.1:9119/auth/password-login
# expect: 401 {"detail":"Invalid credentials"}
```

## Why this happens after `hermes update`

Hermes v0.18 introduced the auth gate as a fail-closed default: if the dashboard binds to a non-loopback address and no provider is registered, it refuses to start (instead of allowing unauthenticated LAN exposure by accident). The pre-update config had a working basic_auth block; the update either:

- replaced it with the empty template during config-migrate (the `_config_version` bumped and key defaults reset), OR
- the user previously set basic_auth via an env-var override (`HERMES_DASHBOARD_BASIC_AUTH_PASSWORD_HASH`) that the update didn't preserve, leaving `password_hash: ''` in YAML while env still worked — except the new gate also rejects empty-YAML providers.

The recovery works either way because we re-populate the YAML block through `hermes config set`.
