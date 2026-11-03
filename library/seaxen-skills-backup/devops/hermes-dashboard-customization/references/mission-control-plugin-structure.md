# Mission Control Plugin Structure Reference

Discovered during session rescuing Dr. Sagar's custom "mission-control" plugin that had directory but no working code.

## Required Plugin Skeleton

```
/root/.hermes/plugins/<name>/
├── plugin.yaml              # Manifest (mandatory)
├── __init__.py              # Python entry with register(ctx) (mandatory)
├── bitwarden_provider_test_state.json   # Any existing state files
├── config_snapshot_state.json           # Any existing state files
└── dashboard/               # Dashboard tab (if UI needed)
    ├── manifest.json        # Tab config (id, label, icon, order)
    ├── plugin_api.py        # FastAPI routes (/api/plugins/<name>/*)
    ├── build.js             # esbuild script → dist/index.js
    ├── src/
    │   ├── index.js         # Entry: PLUGINS.register(name, Component)
    │   ├── lib/sdk.js       # Hermes SDK bridge
    │   └── components/
    │       ├── <Name>Tab.js     # React component using SDK components
    │       └── ErrorBoundary.js # Optional error wrapper
    └── dist/index.js        # Built bundle (IIFE format)
```

## plugin.yaml (Manifest)

```yaml
name: mission-control
version: "0.1.0"
description: "Provider health monitoring and config snapshot dashboard"
author: Dr. Sagar
requires_env: []
provides_tools:
  - mission_control_status
  - mission_control_refresh
provides_hooks: []
```

## __init__.py — register(ctx) Pattern

**Critical:** Use `register(ctx)` function, NOT `@register_tool` decorator.

```python
def register(ctx):
    ctx.register_tool(
        name="mission_control_status",
        toolset="mission-control",
        schema={...},
        handler=_mission_control_status,
        check_fn=lambda: True,
        requires_env=[],
        description="Mission Control status",
        emoji="📊",
    )
```

The `@register_tool` decorator pattern **does not work** for dashboard plugins — the plugin loader expects a `register(ctx)` function.

## Dashboard Entry Point (src/index.js)

```javascript
import { React, PLUGINS } from "./lib/sdk.js";
import { PluginErrorBoundary } from "./components/ErrorBoundary.js";
import { MissionControlTab } from "./components/MissionControlTab.js";

PLUGINS.register("mission-control", function MissionControlWrapped() {
  return React.createElement(
    PluginErrorBoundary,
    null,
    React.createElement(MissionControlTab)
  );
});
```

## SDK Bridge (src/lib/sdk.js)

Hermes injects globals at runtime:

```javascript
const SDK = window.__HERMES_PLUGIN_SDK__;
const PLUGINS = window.__HERMES_PLUGINS__;

export const React = SDK.React;
export const { useState, useEffect, useRef, useMemo } = SDK.hooks;
export const fetchJSON = SDK.fetchJSON;
export const { Card, CardHeader, CardTitle, CardContent, Badge, Button, Table, ... } = SDK.components;
export { PLUGINS };
```

## Build Process

```bash
cd /root/.hermes/plugins/mission-control/dashboard
npm install
npm run build  # runs node build.js → esbuild → dist/index.js
```

## Enabling the Plugin

Add to `/root/.hermes/config.yaml`:

```yaml
plugins:
  enabled:
    - cronalytics
    - mission-control   # add here
    - mnemosyne-dashboard
    ...
```

**Requires gateway restart** to pick up new plugin.

## Verification

```bash
hermes plugins list          # shows "mission-control | enabled | 0.1.0 | user"
hermes tools list            # shows tools under "Plugin toolsets (cli)"
```

---

## Pitfalls Learned

1. **@register_tool decorator fails** — plugin loader only calls `register(ctx)` function
2. **No manifest = invisible** — plugin.yaml is mandatory for plugin discovery
3. **No dashboard/dist = no tab** — UI tab requires built `dist/index.js` bundle
4. **Config changes need gateway restart** — live reload does not pick up new plugin entries
5. **SDK components import from SDK.components** — not from local UI kit; must destructure from SDK