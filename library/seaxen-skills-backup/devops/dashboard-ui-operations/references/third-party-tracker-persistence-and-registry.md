# Third-party tracker persistence, registry, and live verification

Use this when extending a Hermes dashboard tracker tab that inventories plugins, skills, and git repos.

## Durable patterns from this session

### 1) For read-heavy tracker tabs, show the operator exactly how repo discovery works
If the user asks "how do I know a repo was added?" the page needs an explicit confirmation surface, not just hidden scan logic.

Good default UI:
- a visible **Tracked external repos** list
- a visible **Dashboard registry entries** list
- a short **How new repos get tracked** explainer
- an **Add external git repo root** input for outside repos

This prevents the common operator complaint: "there is no list of installed repo".

### 2) Split repo intake into auto-discovery vs registry
Useful tracker shape:
- auto-discover git plugins under `/root/.hermes/plugins`
- auto-discover git repos under `/root/.hermes`
- auto-discover repos referenced by Hermes config / MCP paths
- allow manual registration of outside repo roots in a small registry file

The registry should be additive, not a replacement for normal discovery.

### 3) Persist tracker review state server-side once the workflow matters
LocalStorage is fine for a first pass, but once the user wants a serious operator board:
- persist manual-known state in a backend JSON state file
- expose a plugin API route like `/state`
- keep the frontend status honest: `persisted` vs `local fallback`

This lets the operator know whether the dashboard is using real saved state or browser-only fallback.

### 4) Distinguish frontend-live from backend-live
A useful failure shape on Hermes dashboard plugins:
- new JS/CSS bundle is clearly live
- but plugin API routes still return SPA HTML, stale JSON, or 405

Interpretation:
- frontend deployment succeeded
- backend plugin router is stale
- restart `hermes-dashboard.service`
- do **not** restart gateway unless the issue is actually gateway-related

### 5) Best verification sequence for tracker persistence work
After changing plugin API + dist bundle:
1. syntax-check JS and Python
2. run the generator script and inspect generated payload fields
3. load the live 9120 tracker route
4. browser-fetch the new plugin API routes directly with dashboard session token
5. confirm inventory mode shows the new operator surfaces
6. confirm no JS console errors

### 6) Good operator phrasing for repo tracking
Keep the page explicit:
- `Tracked external repos` = currently detected by config/scan
- `Dashboard registry entries` = manually added paths
- `State: persisted` = backend state route working
- `State: local fallback` = frontend is using local-only state

That language helps the user immediately understand whether repo registration actually landed.
