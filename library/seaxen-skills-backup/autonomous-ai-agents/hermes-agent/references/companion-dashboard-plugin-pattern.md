# Companion dashboard plugin pattern

Use this when the user wants a **separate premium dashboard beside the built-in Hermes dashboard**, not a fork or replacement.

## Recommendation

Prefer a **dashboard plugin** instead of patching core pages first.

Why:
- keeps the built-in dashboard intact
- ships as an isolated feature under `plugins/<name>/dashboard/`
- can be iterated quickly on UI/UX
- uses the existing dashboard auth/session model and API surface
- can later graduate into core dashboard features if the pattern proves useful

## Minimal plugin layout

```text
plugins/<plugin-name>/dashboard/
├── manifest.json
└── dist/
    ├── index.js
    └── style.css
```

Optional tests:

```text
tests/plugins/test_<plugin-name>_dashboard_plugin.py
```

## Minimal manifest

```json
{
  "name": "mission-control",
  "label": "Mission Control",
  "description": "Premium companion dashboard for Hermes sessions, model context, skills, toolsets, profiles, and cron health.",
  "icon": "Sparkles",
  "version": "0.1.0",
  "tab": {
    "path": "/mission-control",
    "position": "after:chat"
  },
  "entry": "dist/index.js",
  "css": "dist/style.css"
}
```

## Frontend integration pattern

Inside `dist/index.js`:
- read the host SDK from `window.__HERMES_PLUGIN_SDK__`
- register the page with `window.__HERMES_PLUGINS__.register("<name>", Component)`
- use `SDK.api` for Hermes data instead of rolling custom fetch logic when built-in endpoints already exist

Useful built-in dashboard API calls for a control-center page:
- `SDK.api.getStatus()`
- `SDK.api.getModelInfo()`
- `SDK.api.getSessions(limit, offset)`
- `SDK.api.getSkills()`
- `SDK.api.getToolsets()`
- `SDK.api.getProfiles()`
- `SDK.api.getCronJobs()`

## Good first MVP for a premium companion page

Start with a **read-only control surface**:
- current model/provider/context block
- recent sessions with **visible session IDs**
- `Resume in Chat` links using `/chat?resume=<session_id>`
- `Copy CLI` actions using `hermes --resume <session_id>`
- enabled skills summary
- enabled toolsets summary
- profiles summary
- cron jobs summary

This is the safest first version because it improves continuity and discoverability without adding risky write actions.

## Resume / continuity details

When the user asks for “continue later / resume later”, make session ID visibility a first-class UI element.

Useful link patterns:
- dashboard chat resume: `/chat?resume=<session_id>`
- CLI resume command: `hermes --resume <session_id>`

## Discovery / refresh

After adding a new plugin, rescan dashboard plugins:

```text
GET /api/dashboard/plugins/rescan
```

With a browser session, include the injected `X-Hermes-Session-Token` header.

Expected success shape:

```json
{"ok": true, "count": <number>}
```

Then verify:
- the plugin appears in the sidebar plugin list
- the route loads directly, e.g. `/mission-control`
- the page renders expected headings and resume links

## Verification pattern

Add a focused smoke test that checks:
- manifest fields (`name`, `label`, `tab.path`, `entry`, `css`)
- bundle registers the plugin page
- bundle contains resume affordances (`/chat?resume=` and `hermes --resume `)
- stylesheet includes the main shell classes

Example assertions:
- `Registry.register("mission-control", MissionControlPage);`
- `"/chat?resume=" + encodeURIComponent(session.id)`
- `"hermes --resume " + session.id`

## UI guidance for this class of request

When the user asks for a “beautiful compact premium” Hermes dashboard, optimize for:
- dark premium cards
- compact scannable rows
- session ID legibility with monospace treatment
- card-based overview instead of dense forms
- continuity actions first, configuration actions second

## When to escalate beyond plugin MVP

Only move from plugin to core dashboard edits if the user specifically wants:
- replacement of built-in sessions/models pages
- deeper integration into dashboard navigation/state
- write actions that need new backend endpoints
- cross-page shared components that should live in `web/src/`
