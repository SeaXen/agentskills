# Hermes dashboard plugin format (sidebar tab)

Authoritative layout for tabs on the Hermes dashboard SPA (`hermes dashboard`, typically port **9119**). Source: `hermes_cli/web_server.py` → `_discover_dashboard_plugins()`, `_mount_plugin_api_routes()`.

## Directory layout

```
~/.hermes/plugins/<plugin-name>/
├── plugin.yaml              # optional — for hermes plugins list / enabled; NOT what registers the tab
└── dashboard/
    ├── manifest.json        # REQUIRED for tab discovery
    ├── plugin_api.py        # optional — FastAPI APIRouter
    └── dist/
        ├── index.js           # REQUIRED — registers React component
        └── style.css          # optional
```

## manifest.json (minimal)

```json
{
  "name": "my-plugin",
  "label": "My Plugin",
  "description": "Short description for Mission Control",
  "icon": "History",
  "version": "1.0.0",
  "tab": {
    "path": "/my-plugin",
    "position": "end",
    "hidden": false
  },
  "entry": "dist/index.js",
  "css": "dist/style.css",
  "api": "plugin_api.py"
}
```

- **`name`** must match `window.__HERMES_PLUGINS__.register('my-plugin', App)` in `index.js`.
- **`tab.path`** is the SPA route — user opens `http://<host>:9119/my-plugin`, **not** `/plugin/my-plugin/`.

## plugin_api.py

```python
from fastapi import APIRouter
router = APIRouter()

@router.get("/health")
def health():
    return {"ok": True}
```

Mounted at **`/api/plugins/<name>/`** (e.g. `/api/plugins/my-plugin/health`). Load test with Hermes venv Python (system python may lack fastapi).

Expose **`plugin_version`** in `/health` so the tab can show `api 1.2.0` and operators can tell live vs stale backend without guessing.

## index.js pattern

Copy structure from `~/.hermes/plugins/third-party-tracker/dashboard/dist/index.js`:

- `const SDK = window.__HERMES_PLUGIN_SDK__;`
- Build UI with `SDK.React`, `SDK.hooks`, `SDK.components`
- `fetch('/api/plugins/<name>/...', { credentials: 'include' })` for authenticated API
- Final line: `window.__HERMES_PLUGINS__.register('<name>', App);`

Avoid external CDNs in plugin JS unless dashboard CSP allows them — prefer SDK components + inline CSS bars.

**Telemetry-style operator UI:** For dashboard tabs on Dr. Sagar's host, copy layout from `~/.hermes/plugins/hermes-telemetry/dashboard/dist/index.js`: `StatCard` + internal `TabBar`, `const api = (path) => SDK.fetchJSON(\`/api/plugins/${PLUGIN}${path}\`)`, `Badge variant="outline"` on title. Use `fetch(..., { method: 'POST', credentials: 'include' })` for mutating routes — `fetchJSON` is GET-oriented.

## Lifecycle

| Action | Gateway restart? | Dashboard restart? |
|---|---|---|
| New slash command in `__init__.py` | **Yes** | No |
| New/changed `dashboard/manifest.json` | No | **Yes** (full process) |
| Changed `plugin_api.py` | No | **Yes** |

`GET /api/dashboard/plugins/rescan` refreshes the **cached list** in a running process but **does not** re-import `plugin_api.py` routers mounted at startup.

## Verification

```bash
/usr/local/lib/hermes-agent/venv/bin/python3 -c "
import sys; sys.path.insert(0,'/usr/local/lib/hermes-agent')
from hermes_cli.web_server import _discover_dashboard_plugins
print([p['name'] for p in _discover_dashboard_plugins()])
"
```

## Common failures

| Symptom | Cause |
|---|---|
| Tab missing after "enable" | No `dashboard/manifest.json` or dashboard not restarted |
| `/plugin/foo/` → home | Invalid URL; use `tab.path` |
| API 404 from UI | Wrong prefix — must be `/api/plugins/<name>/` |
| Stats all `0`, DB has rows | Dashboard process not restarted after `plugin_api.py` / JS change |
| Models/Providers tab empty, Messages OK | `/breakdown/*` routes missing in running process — restart dashboard; check red error for `404` |
| Table looks blank with long IDs | Avoid `truncate` on every `<td>` — use `break-all` on name column only |
| No `api x.y.z` badge in tab header | Stale mounted API — full dashboard restart |
| `hermes plugin install` error | CLI has `hermes plugins`, not `plugin install` |
| Cron script rejected | Put script in `~/.hermes/scripts/` only |

## Related

- `references/manifest-history-plugin.md` — archive + cron example