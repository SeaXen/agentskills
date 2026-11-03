# Hermes dashboard third-party audit and feature-port pattern

## Use this when
- Dr. Sagar asks whether a Hermes dashboard repo is safe to install
- a third-party repo may be theme-only or may also ship plugin/backend code
- a repo has useful ideas but collides with an existing built-in Hermes tab

## Durable workflow
1. Audit the repo tree first.
   - Check root contents.
   - Read `README.md`.
   - Read dashboard/plugin manifests.
   - Inspect raw shipped assets when needed (`dist/index.js`, `plugin_api.py`, theme YAMLs).
2. Classify the package honestly.
   - Theme-only
   - Plugin + theme
   - Full dashboard/plugin pack
3. Verify against the local Hermes runtime.
   - Check `hermes --version` if compatibility matters.
   - Confirm the active config path / Hermes home used by the running dashboard.
   - Verify local support for the integration surface (theme loader, plugin API, manifest behavior, etc.).
4. If installing, verify live behavior instead of trusting file copy success.
   - Check the live dashboard route.
   - Rescan plugins if needed.
   - When direct API calls return 401, retry from the browser context with the session token instead of declaring the route broken.
5. If the upstream plugin collides with an existing built-in Hermes surface or its shipped frontend is broken, stop trying to sell a renamed install as success.
   - Say plainly what is broken.
   - Pivot to feature-porting the useful ideas into the existing working built-in surface.
6. Port incrementally.
   - pick one feature group
   - add tests first
   - patch backend and dist bundle minimally
   - verify live on the real dashboard

## Mission Control-specific lesson
When a third-party Mission Control plugin duplicates the built-in `mission-control` identity/path or ships a broken bundle, the right move is usually:
- do not install a fake second tab
- port the useful operator features into the built-in Mission Control tab
- verify through the live route and authenticated browser-side API fetches

## Good feature-port order
1. Safe config snapshot + redaction
2. Snapshot diff / change tracking
3. Operator notes + checklist
4. Activity timeline / operator refresh actions
5. Theme/style borrowing only after functional value is landed

## What not to save as a lesson
- transient dashboard stop/restart oddities
- one-time path mismatches that were specific to this environment
- temporary upstream bundle errors after they have already been translated into the durable rule: feature-port instead of fake clone
