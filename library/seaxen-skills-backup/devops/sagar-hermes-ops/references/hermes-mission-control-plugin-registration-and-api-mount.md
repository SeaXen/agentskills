# Hermes Mission Control plugin registration and API-mount debugging

Use when a dashboard plugin route exists in the nav but the page says the plugin did not register, appears briefly then disappears, loads an empty shell, or shows **404 `No such API endpoint: /api/plugins/<name>/...`** on data fetches (Memory, Cronalytics, Mission Control, 3rd Party, etc.).

## High-value split
Treat these as separate layers:
1. **`plugins.enabled` gate (user plugins)** — is the slug in `plugins.enabled` and not in `plugins.disabled`? Without this, the sidebar omits the tab and `_mount_plugin_api_routes()` skips importing `plugin_api.py` at startup (#46435). Fix: `hermes plugins enable <name>`.
2. **Manifest / plugin discovery** — does `plugins/<name>/dashboard/manifest.json` exist? Does `/api/dashboard/plugins` list the plugin with expected `name`, `tab.path`, `entry`, `has_api`?
3. **Static bundle / SDK contract** — does `/dashboard-plugins/<name>/dist/index.js` register and fetch correctly?
4. **Backend API mount (startup-only)** — routes mount **once** at dashboard process start. Enabling a plugin after startup updates the sidebar via live config but **does not** add `/api/plugins/<name>/...` until restart. `/api/dashboard/plugins/rescan` does **not** remount Python APIs. Fix: `sudo systemctl restart hermes-dashboard.service` (or stop/start `hermes dashboard` on the live port). Confirm in `agent.log` or journal: `Mounted plugin API routes: /api/plugins/<name>/`.
5. **Authenticated browser fetch** — in-browser requests need the dashboard session token (`SDK.fetchJSON` / `X-Hermes-Session-Token`).

## Durable findings from this session
- **Sidebar can work while APIs 404:** After `hermes plugins enable`, tabs like `/memory` and `/cronalytics` may appear immediately, but calls to `/api/plugins/hermes-memory-ui/snapshot` or `/api/plugins/cronalytics/summary` 404 until the dashboard process restarts.
- Hermes dashboard already mounts plugin routers under `/api/plugins/<name>`. If `plugin_api.py` also sets `APIRouter(prefix='/api/plugins/<name>')`, the effective path becomes doubled and the expected frontend path 404s.
- A plugin can appear in the sidebar and still have a dead backend. Static asset discovery and backend route mounting are separate.
- Unnecessary backend imports can kill only the API mount. In this case, `from hermes.agent.plugins import get_plugin_manager` caused `ModuleNotFoundError` under the dashboard runtime.
- Plain browser `fetch(...)` from plugin code can fail against auth-gated plugin APIs even while the same path works with the dashboard session token. Prefer `window.__HERMES_PLUGIN_SDK__.fetchJSON(...)`.
- The injected dashboard SDK may expose fewer components than older plugin examples assume. If table/tab primitives are missing, rewrite to plain HTML instead of forcing absent SDK widgets.

## Practical probe order
1. `hermes plugins list` — confirm **enabled** (not just installed). Compare `plugins.enabled` in `config.yaml` to manifest `name` (slug must match).
2. Read `dashboard/manifest.json` and confirm `api`: `plugin_api.py` when the tab needs backend data.
3. Check dashboard **start time** vs when plugins were enabled; if enable was later, plan a restart before debugging code.
4. After restart, grep logs for `Mounted plugin API routes: /api/plugins/<name>/` or `skipping API mount (not in plugins.enabled)`.
5. Import `plugin_api.py` directly in Python to catch import errors (Cronalytics loads sibling modules via importlib).
6. Probe the failing path with `X-Hermes-Session-Token` (raw curl without auth may 401/404 misleadingly).
7. `/api/dashboard/plugins/rescan` — refreshes discovery count only; not a substitute for restart.

## Operator explanation shape
If the user asks "why did it appear then disappear?", answer in layers:
- discovery/sidebar registration worked,
- backend route mount or frontend registration failed,
- rebuild/rescan alone is not enough if the plugin API import path is broken or the router prefix is doubled.
