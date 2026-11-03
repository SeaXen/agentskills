# Hermes home move recovery: /root/.hermes vs /mnt/tb/hermes

Use this when Hermes suddenly looks like a fresh install after moving data to a new `HERMES_HOME`.

## Fast diagnosis

```bash
printf 'HERMES_HOME=%s\n' "${HERMES_HOME:-}"
hermes config path
hermes config env-path
hermes status --all
hermes dashboard --status
hermes gateway status
systemctl --user cat hermes-gateway --no-pager | grep HERMES_HOME
curl -s http://127.0.0.1:9120/api/status
```

## What split-brain looks like

Observed real-world pattern:
- shell/CLI uses `/mnt/tb/hermes`
- `hermes-gateway.service` still contains `Environment="HERMES_HOME=/root/.hermes"`
- dashboard or gateway then shows:
  - no messaging platforms enabled
  - no allowlists configured
  - empty/near-empty sessions
  - missing plugins / missing keys

The user may think data was deleted. Usually it was not.

## Recovery

1. Confirm real data exists under the target home:
   - `config.yaml`
   - `.env`
   - `auth.json`
   - `plugins/`
   - `sessions/`
   - `state.db`
2. Refresh the gateway unit:
   ```bash
   hermes gateway restart
   ```
3. Confirm the unit now points to the target home:
   ```bash
   systemctl --user cat hermes-gateway --no-pager | grep HERMES_HOME
   ```
4. If dashboard was started from the wrong home, stop and restart it from the correct environment.
5. Verify backend state directly:
   ```bash
   curl -s http://127.0.0.1:9120/api/status
   curl -s http://127.0.0.1:8642/health
   tail -n 40 /mnt/tb/hermes/logs/gateway.log
   ```
6. Hard-refresh the browser tab.

## Good verification signs

- `/api/status` reports:
  - `hermes_home: /mnt/tb/hermes`
  - `config_path: /mnt/tb/hermes/config.yaml`
  - `env_path: /mnt/tb/hermes/.env`
- gateway log says `Session storage: /mnt/tb/hermes/sessions`
- connected platforms reappear
- plugin tabs reappear
- recent sessions reappear

## Extra note

If reverse proxy auth exists on `:9119`, test the raw dashboard backend on `127.0.0.1:9120` first so auth/caching does not hide the real cause.
