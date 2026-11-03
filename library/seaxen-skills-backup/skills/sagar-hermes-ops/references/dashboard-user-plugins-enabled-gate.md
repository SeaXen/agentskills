# Dashboard user plugins — `plugins.enabled` gate

## Symptom
- Custom tabs **missing from nav** (Mission Control, 3rd Party, Cronalytics, Memory, …) while `~/.hermes/plugins/<name>/` still exists.
- **OR** tabs **visible** but the page errors with `404 {"detail":"No such API endpoint: /api/plugins/<name>/..."}` (e.g. `/api/plugins/hermes-memory-ui/snapshot`, `/api/plugins/cronalytics/summary`).

## Root cause (Hermes #46435 behavior)
Two layers — do not conflate them:

| Layer | What controls it | When it updates |
|-------|------------------|-----------------|
| **Sidebar / `/api/dashboard/plugins` list** | `plugins.enabled`, `plugins.disabled`, `dashboard.hidden_plugins` | Per request (live config) |
| **`plugin_api.py` routes** (`/api/plugins/<name>/...`) | Same enablement gate, but `_mount_plugin_api_routes()` runs **once at dashboard process start** | Only after **dashboard restart** |

`GET /api/dashboard/plugins` returns discovered plugins **minus**:
- names in `dashboard.hidden_plugins`
- user plugins **not** listed under `plugins.enabled`
- any plugin in `plugins.disabled`

Bundled dashboard plugins (e.g. kanban, hermes-achievements) only check `plugins.disabled`.

Discovery scans `plugins/<name>/dashboard/manifest.json` (not root `plugin.yaml` alone).

## Diagnosis order
1. List manifests: `ls ~/.hermes/plugins/*/dashboard/manifest.json`
2. Compare enabled set: `hermes plugins list` or read `plugins.enabled` in `config.yaml`
3. Live API (unauthenticated endpoint still reflects enablement filter):
   ```bash
   curl -s http://127.0.0.1:9119/api/dashboard/plugins | python3 -m json.tool
   ```
4. Optional full discovery in a fresh Python import:
   ```python
   from hermes_cli.web_server import _discover_dashboard_plugins
   ```
   If discovery count > API count → enablement/hidden, not missing files.

## Fix
```bash
hermes plugins enable mission-control
hermes plugins enable third-party-tracker
hermes plugins enable cronalytics
hermes plugins enable hermes-memory-ui
# repeat per custom tab (manifest `name` slug)
```

Then **restart the dashboard** so plugin APIs mount (required for Memory/Cronalytics data, not optional):
```bash
sudo systemctl restart hermes-dashboard.service   # :9119 on this host
```

Verify in `~/.hermes/logs/agent.log` or journal:
`Mounted plugin API routes: /api/plugins/<name>/`

Hard-refresh browser. `/api/dashboard/plugins/rescan` refreshes discovery count only — **it does not remount Python APIs**.

Agent hooks from newly enabled plugins may need a **new gateway session** (CLI prints "Takes effect on next session").

## Edge cases
| Case | Behavior |
|------|----------|
| `hermes-personal-dashboard` in `enabled` but no `dashboard/manifest.json` | Enabled for agent; **no nav tab** |
| `sovereign-ops-dashboard` — manifest only, no `plugin.yaml` | `hermes plugins enable` → "not installed"; needs proper plugin install or manual enablement strategy |
| Stale process cache | Rare; `rescan` or restart dashboard if API disagrees with disk after enable |

## Verified (2026-07-03, :9119)
Before enable: API list returned 4 tabs; plugin APIs for user plugins not mounted at prior dashboard start.  
After `hermes plugins enable` + **`systemctl restart hermes-dashboard`**: API list 8 tabs; log lines for `cronalytics` and `hermes-memory-ui` API mounts; Memory/Cronalytics fetches succeed.

See also `references/hermes-mission-control-plugin-registration-and-api-mount.md`.