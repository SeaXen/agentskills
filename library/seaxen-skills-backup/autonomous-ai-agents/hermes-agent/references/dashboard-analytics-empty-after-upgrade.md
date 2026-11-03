# Dashboard analytics/model pages empty after upgrade

Use this when Hermes CLI analytics still works, but the web dashboard's analytics/model pages look blank after an upgrade.

## Durable pattern

This is often a **dashboard frontend/process mismatch**, not missing analytics data.

Typical shape from a live case:
- `hermes --version` shows the new release (for example `v0.14.0`)
- dashboard `/api/status` may initially show an older version/home until restarted
- `hermes insights --days 30` returns full usage/model analytics
- direct unauthenticated API probes to analytics endpoints return `401 Unauthorized`
- browser UI shows empty analytics/model sections

## What it usually means

1. **Data exists** if `hermes insights --days N` works.
2. **Blank dashboard pages do not automatically mean data loss.**
3. The empty page is commonly caused by one or both of:
   - stale dashboard frontend assets/browser cache after upgrade
   - stale dashboard process still serving from an older Hermes home/version
4. On the **Models** page specifically, Hermes `0.14` can intentionally show only model names / providers / session counts while hiding token and cost analytics if `dashboard.show_token_analytics` is disabled.

### Important 0.14 behavior change: token analytics can be hidden by config

In `0.14`, the dashboard Models page gates token/cost surfaces behind:

```yaml
dashboard:
  show_token_analytics: true
```

If it is `false`, the page may still look partially populated:
- model names still appear
- provider badges still appear
- `Models Used` and `Total Sessions` still appear
- but **total tokens, input/output token stats, token bars, and estimated cost fields are hidden**

This is not necessarily a bug. The default was changed because local token accounting can undercount relative to provider billing (auxiliary calls, retries, fallbacks, cache writes).

## Verification sequence

```bash
hermes --version
hermes dashboard --status
curl -s http://127.0.0.1:9120/api/status
hermes insights --days 30
systemctl --user cat hermes-gateway --no-pager | grep HERMES_HOME
```

Interpretation:
- If `hermes insights --days 30` is populated, analytics data is present in `state.db`.
- If `/api/status` reports an old version or wrong `hermes_home`, restart the dashboard from the intended home.
- If analytics endpoints like `/api/insights`, `/api/models`, `/api/provider-models`, or `/api/sessions/stats` return `401` when tested from terminal, do **not** conclude the feature is broken — those routes may require dashboard auth/session context.

## Practical fix order

### 0. Check the token-analytics toggle first on the Models page symptom
When the user says _"before it showed how many tokens I used, now it only shows model names"_, verify the config value first:

```bash
hermes config set dashboard.show_token_analytics true
```

Or inspect `config.yaml` for:

```yaml
dashboard:
  show_token_analytics: true
```

Then hard-refresh the dashboard tab. This is the fastest fix when the page is populated but token-specific fields disappeared.

### 1. Fix backend/process mismatch first
If needed, restart the dashboard from the intended home:

```bash
export HERMES_HOME=/mnt/tb/hermes
hermes dashboard --stop
hermes dashboard --host 127.0.0.1 --port 9120 --insecure
```

Then re-check:

```bash
curl -s http://127.0.0.1:9120/api/status
```

Make sure it now reports the expected:
- Hermes version
- `hermes_home`
- `config_path`
- `env_path`

### 2. Hard refresh the browser
After backend restart, do a **hard refresh** (`Ctrl+Shift+R`) or open the dashboard in a private/incognito tab.

Reason: after upgrades, the browser can keep stale dashboard assets that do not match the new backend/API behavior.

### 3. Align visible home path if there is still split-brain confusion
Even when two paths resolve to the same directory (for example `/mnt/tb/hermes` symlinked to `/root/.hermes`), path-string mismatches between shell, gateway unit, and dashboard can still confuse troubleshooting. Align them if the user keeps seeing inconsistent UI state.

## User-facing explanation to prefer
Use simple wording:
- analytics data is still there
- CLI insights proves it
- blank dashboard page is most likely cache/process mismatch
- hard refresh first, then restart/re-align services if needed

## Do not overclaim
Do **not** say the analytics feature is gone just because:
- `/api/models` or `/api/insights` returned `401` from curl
- the dashboard page is blank once after upgrade

Those are compatible with an auth-protected or cache-stale dashboard, not necessarily a regression in analytics storage.
