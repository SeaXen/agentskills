---
name: hermes-dashboard-restore
description: "Recover the main Hermes Agent dashboard (port 9119) after an update wipes auth/config — restore basic_auth from backup, keep new password hash, verify login. Triggers on 'Refusing to bind dashboard to 0.0.0.0 — the auth gate engages' errors or 'dashboard not opening after hermes update'."
version: 1.1.0
author: SeaXen + Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, dashboard, auth, restore, recovery, basic_auth, backup, splice, redactor]
    related_skills: [hermes-agent, hermes-dashboard-customization, hermes-backup-watchers, hermes-git-config-snapshots]
---

# Hermes Dashboard Restore

Recover the main Hermes Agent web dashboard (`http://<host>:9119`) when a `hermes update` wipes or invalidates the auth/config block. This is **not** the standalone products skill — that covers separate `9120`-class products. This skill is specifically for the main `hermes dashboard` command bound to `9119` by default.

## When to use

Trigger on any of these symptoms:

- `hermes-dashboard.service` restart loop with status `activating (auto-restart)` and exit code `1/FAILURE`
- Journal shows: `Refusing to bind dashboard to 0.0.0.0 — the auth gate engages on non-loopback binds, but no auth providers are registered.`
- Dashboard URL returns `connection refused` or `502` after a Hermes update
- `~/.hermes/config.yaml` `dashboard.basic_auth` block is all empty strings after an update

## Quick restore (90 seconds)

The backup source of truth on this user's machine is:
```
/mnt/tb/hermes-backups/#plain/hermes-plain-*/config.yaml
```
The most recent pre-update snapshot typically lives in `state-snapshots/<timestamp>-pre-update/config.yaml` inside the active `~/.hermes/`.

### Step 1: Stop the failing service and confirm the error

```bash
systemctl status hermes-dashboard.service --no-pager -l
journalctl -u hermes-dashboard.service -n 30 --no-pager -l | grep -i 'auth gate\|refusing'
```

### Step 2: Set basic_auth via hermes CLI (NOT patch/write_file)

`patch` and `write_file` **refuse to write to `~/.hermes/config.yaml`**. Always use:

```bash
hermes config set dashboard.basic_auth.username <user>
```

To set the password hash, generate it first using the Hermes venv's bundled scrypt helper:

```bash
PYTHONPATH=/usr/local/lib/hermes-agent \
  /usr/local/lib/hermes-agent/venv/bin/python -c \
  "import secrets; from plugins.dashboard_auth.basic import hash_password; print('HASH=' + hash_password('<password>')); print('SECRET=' + secrets.token_hex(32))"
```

Then push the values in:

```bash
hermes config set dashboard.basic_auth.username sagar
hermes config set dashboard.basic_auth.password_hash 'scrypt$N$N$8$1$...$...'
hermes config set dashboard.basic_auth.password ''
hermes config set dashboard.basic_auth.secret '<32-byte hex>'
hermes config set dashboard.basic_auth.session_ttl_seconds 43200
```

### Step 3: Restart and verify

```bash
systemctl restart hermes-dashboard.service
sleep 5
ss -tlnp | grep ':9119\b'                 # must show hermes listening
curl -sI http://127.0.0.1:9119/ | head -3 # must return 302 -> /login?next=%2F
```

End-to-end login probe (proves the hash actually verifies):

```bash
rm -f /tmp/hermes-cookies.txt
curl -sS -c /tmp/hermes-cookies.txt \
  -H 'Content-Type: application/json' \
  -d '{"provider":"basic","username":"sagar","password":"<password>","next":"/"}' \
  http://127.0.0.1:9119/auth/password-login
# expect: {"ok":true,"next":"/"}

curl -sS -b /tmp/hermes-cookies.txt http://127.0.0.1:9119/api/auth/me
# expect: {"user_id":"sagar","provider":"basic",...}
```

## Restore the wider config drift (optional)

A Hermes update can also flip `approvals.mode` from `smart` to `manual`, wipe `command_allowlist`, drop custom providers, etc. To bring the whole config back without losing the new password hash:

```bash
# 1. Save current pre-restore copy as a safety net
cp -a ~/.hermes/config.yaml ~/.hermes/config.yaml.pre-restore-$(date +%Y%m%d-%H%M%S)

# 2. Splice: backup head through session_reset block, then keep current valid tail
python3 <<'PY'
from pathlib import Path
cur = Path('/root/.hermes/config.yaml').read_text().splitlines()
bak = Path('/mnt/tb/hermes-backups/#plain/hermes-plain-YYYY-MM-DD_HH-MM/config.yaml').read_text().splitlines()
# backup had valid content through the session_reset block,
# then stray malformed lines (duplicated api_server_key, broken or-auto-* aliases).
# Current valid tail starts at the API_SERVER_KEY line.
# Inspect both files first; the exact line numbers depend on the backup.
Path('/root/.hermes/config.yaml').write_text('\n'.join(bak[:HEAD_END] + cur[TAIL_START:]) + '\n')
PY

# 3. Re-pin the new password hash + secret (splice loses them)
hermes config set dashboard.basic_auth.password_hash '<new-hash>'
hermes config set dashboard.basic_auth.secret '<32-byte hex>'

# 4. Verify
hermes config check
systemctl restart hermes-dashboard.service
```

Use `diff -u <backup> <current>` to see exactly what changed before doing this.

### Common drift to expect after a Hermes update

Diff observations from a real 2026-07-08 update (use as a sanity checklist):

| Field | Before (backup) | After (update) | Action |
|---|---|---|---|
| `approvals.mode` | `smart` | `manual` | restore from backup |
| `command_allowlist` | populated | `[]` | restore from backup |
| `dashboard.basic_auth.username` | preserved | preserved | keep |
| `dashboard.basic_auth.password_hash` | old hash | `""` (wiped) | keep **new** hash if already set by user, else generate |
| `dashboard.basic_auth.secret` | `""` | `""` | set non-empty so /login can mint sessions |
| `dashboard.basic_auth.session_ttl_seconds` | `86400` | `0` | restore from backup |
| `session_reset.mode` | `none` | `none` | **do not touch** unless user asks for auto-reset |
| `hooks_auto_accept` | `false` | `false` | **do not touch** |
| custom providers (Bynara, OmniRoute, 9router, etc.) | populated | gone | restore from backup; preserve user-defined `model.provider` / `model.default` |

Decision rule: restore everything from backup EXCEPT
1. The new password hash (if user already rotated)
2. `model.default` / `model.provider` (if user intentionally switched models)
3. `API_SERVER_KEY` (if user rotated it — backup shows the previous value)

### Diff the configs before you splice

```bash
diff -u /mnt/tb/hermes-backups/#plain/hermes-plain-YYYY-MM-DD_HH-MM/config.yaml \
        /root/.hermes/config.yaml > /tmp/hermes-final.diff
wc -l /tmp/hermes-final.diff
# fewer than ~200 changed lines: light drift, splice is safe
# 500+ changed lines: structural change, do full restore from backup + re-apply new hash only
```

When the backup's YAML is malformed at the tail, line-based `diff` is reliable but `yaml.safe_load` is not — never trust `safe_load` on the backup file. See `references/auth-gate-failure-transcript.md` for the actual failure transcript that drove this recipe.

## Pitfalls

- **`patch` / `write_file` cannot edit `~/.hermes/config.yaml`** — the tools refuse with `Refusing to write to Hermes config file`. Always go through `hermes config set <key> <value>`. `hermes config` itself uses `yaml.safe_dump`, so quoting rules apply for special chars.
- **Backup YAML files may be malformed at the tail** — the `hermes-plain-*/config.yaml` snapshots often have stray lines after `session_reset` (duplicated `api_server_key`, broken `or-auto-...` aliases) that break `yaml.safe_load`. Use `diff -u` for comparison and a line-based redactor for any sanitized sharing — never trust `yaml.safe_load` on these files.
- **The auth gate binds ONLY to `127.0.0.1` if `--insecure` is passed** — so a 9119 listening on `0.0.0.0` without configured auth means the service **will not start** (it exits with code 1). This is intentional fail-closed behavior since v0.18. Don't add `--insecure` to dodge it; just configure `basic_auth` properly.
- **Don't disable `hermes-dashboard-9120.service` blindly** — check `systemctl list-unit-files | grep hermes-dashboard`. The 9120 unit is a separate optional backup dashboard on a different port; the user often runs only 9119.
- **`API_SERVER_KEY` change vs backup drift** — if `hermes config show` shows `opop@9900` but the backup shows a different value, that's expected (the user rotates it). Don't auto-restore it.
- **`session_reset.mode: none`** — this is intentional default and not changed by updates. Don't touch unless the user explicitly asks for auto-reset.
- **`Session automatically reset (inactive for 24h)` can still appear even with `session_reset.mode: none` on Hermes v0.18.1+** — this is not proof the config flipped. The v0.18.1 freshness gate (`resume_pending_expired`) can reset a restart-interrupted `resume_pending` session after `agent.gateway_auto_continue_freshness` elapses, and older builds mislabel that path as generic `inactive for 24h`. First verify `session_reset.mode` in config before blaming config drift. Practical local mitigation: `hermes config set agent.gateway_auto_continue_freshness 86400`. Upstream split fix pattern from this incident: one PR for the misleading notice text, a second PR for the actual behavior (`mode:none` should bypass the freshness gate).
- **Removing nginx front** — user explicitly does NOT want nginx in front of 9119. Earlier they had `9119 -> nginx basic auth -> 127.0.0.1:9120 (hermes --insecure)` and removed it. The Hermes built-in basic_auth now does that job. Don't re-add nginx unless asked.
- **Glob expansion can leak raw files in git-snapshot scripts** — when scripting around `*.raw.yaml` patterns, the shell glob `snapshots/*.yaml` matches BOTH `*.yaml` and `*.raw.yaml`, so `git add snapshots/*.yaml` will stage ignored raw files. Rename raw files to `*.raw` (no `.yaml` extension) so `*.raw` is the only ignored suffix and the shell glob stays clean. Document this in any companion git-snapshot script.

## Verification checklist

- [ ] `systemctl status hermes-dashboard.service` shows `active (running)` (not `activating`)
- [ ] `ss -tlnp | grep ':9119\b'` shows `hermes` listening on `0.0.0.0:9119`
- [ ] `curl -sI http://127.0.0.1:9119/` returns `302` with `location: /login?next=%2F`
- [ ] `POST /auth/password-login` with correct creds returns `{"ok":true,"next":"/"}`
- [ ] `POST /auth/password-login` with wrong creds returns `401` with `{"detail":"Invalid credentials"}`
- [ ] `GET /api/auth/me` after login returns the configured username and `provider:"basic"`
- [ ] No nginx site enabled on 9119 (`grep -r 'listen 9119' /etc/nginx/conf.d/ 2>/dev/null` returns empty)

## Common follow-up requests

- "Restore from previous backup" → see "Restore the wider config drift" above
- "Add second user" → not supported by built-in basic_auth; needs OAuth or a custom provider
- "Switch to OAuth" → `hermes dashboard register` (Nous Portal) or a DashboardAuthProvider plugin
- "Snapshot config to git for history" → see `hermes-git-config-snapshots` skill (class-level) for the redactor + private GitHub repo + 6h cron + pre-update hook pattern. The `references/config-snapshot-to-git.md` here is the legacy note.

## References

- `references/auth-gate-failure-transcript.md` — exact journalctl snippets for the failing service and the recovery commands
- `references/config-snapshot-to-git.md` — legacy note; the full pattern now lives in the `hermes-git-config-snapshots` skill (templates included).
