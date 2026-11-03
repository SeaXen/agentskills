# Hermes dashboard plugin audit — broken dist recovery

Use when a third-party Hermes dashboard plugin repo looks complete on GitHub but fails at runtime after install.

## Durable pattern
A repo can contain all of these and still ship a bad frontend artifact:
- `dashboard/manifest.json`
- `dashboard/plugin_api.py`
- screenshots
- README/install notes
- `dist/index.js`

That does **not** prove the bundle actually runs.

## Verification sequence
1. Confirm plugin discovery via `/api/dashboard/plugins`
2. Confirm sidebar/tab presence
3. Open the direct route (`/plugin-path`)
4. Check browser text/console for loader failures such as:
   - "The plugin’s script did not call register()"
5. Query backend endpoints separately to distinguish frontend breakage from backend breakage:
   - `/api/plugins/<name>/summary`
   - `/api/plugins/<name>/config-snapshot`

## Specific failure shape seen
A cloned third-party Mission Control-style plugin had:
- valid manifest
- valid backend router
- broken `dist/index.js`
- browser route loaded but rendered only the loader error/fallback shell

The raw bundle also showed corruption/encoding problems, so the failure was not just a missing config step.

## Safe recovery pattern
When the user explicitly wants a working second tab and accepts practical repair over purity:
1. rename plugin identity/path/label/storage namespace to avoid collisions
2. keep the third-party backend/API if it loads cleanly
3. replace only the broken frontend `dist` bundle with a known-good compatible bundle
4. patch the known-good bundle's plugin name, label, route registration, and storage keys
5. cache-bust manifest asset URLs if needed
6. re-verify discovery, route load, visible UI, and backend API

## Reporting rule
Be explicit:
- this is a **working repaired install**
- not a fully untouched upstream install
- upstream repo quality issue is the shipped frontend artifact, not necessarily the backend/router
