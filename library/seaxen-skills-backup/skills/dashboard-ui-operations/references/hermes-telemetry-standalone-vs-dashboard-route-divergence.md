# Hermes telemetry: standalone dashboard vs embedded plugin divergence

Use when `hermes-telemetry` appears healthy on its standalone port (for example `:8009`) but the Hermes dashboard plugin tab (`/telemetry`) shows backend errors.

## Symptom pattern
- standalone dashboard loads and its APIs return `200`
  - e.g. `/api/summary`, `/api/cron`
- Hermes dashboard sidebar shows the `Telemetry` plugin
- `/telemetry` route opens inside Hermes dashboard
- but authenticated requests to `/api/plugins/hermes-telemetry/...` return `404`
- visible UI error looks like:
  - `Backend not reachable: Error: 404: {"detail":"No such API endpoint: /api/plugins/hermes-telemetry/summary"}`

## What this means
The plugin is **discovered by the dashboard frontend**, but the plugin backend router from `dashboard/plugin_api.py` is **not mounted in the running Hermes dashboard process**.

This is a split-surface problem:
1. standalone `serve.py` surface
2. Hermes dashboard plugin-tab surface

They can diverge after an update.

## Verification sequence
1. Check standalone dashboard separately.
   - verify listener on the standalone port
   - open the page
   - probe its local APIs directly
2. Check Hermes dashboard plugin discovery.
   - confirm the plugin appears in `/api/dashboard/plugins`
   - confirm the sidebar/tab is rendered
3. Check Hermes dashboard plugin backend routes explicitly with an authenticated browser fetch.
   - `/api/plugins/hermes-telemetry/health`
   - `/api/plugins/hermes-telemetry/summary`
4. If plugin tab exists but those endpoints return `404`, treat it as a dashboard process mount-state problem, not a frontend-only bug.

## Likely fix
Restart the Hermes dashboard service/process so plugin API routes are re-mounted from the updated `plugin_api.py`.

## Operational lesson
Do not declare `hermes-telemetry` healthy just because `:8009` works. The standalone server and the embedded Hermes dashboard plugin are different runtime surfaces and must both be verified.