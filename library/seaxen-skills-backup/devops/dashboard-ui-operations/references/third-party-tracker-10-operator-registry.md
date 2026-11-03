# Third-party tracker 10/10 operator pattern

Use this when upgrading a Hermes 3rd Party / add-on tracker from “useful dashboard” to “trusted operator surface”.

## What counts as 10/10

Do not rate it 10/10 just because the page looks good. Require all of these:

- served frontend bundle is live on the user-facing route
- browser console has no JS errors
- safe buttons work: view toggles, copy, preview/dry-run, scan
- mutating buttons are guarded by preview/confirmation and are not executed without explicit approval
- backend plugin API routes return JSON, not the SPA shell
- server-side state persists where the UX claims persistence
- generator refresh succeeds and the page data matches the generated JSON
- cron/scheduler status is either live-backed or clearly labeled as configured/static

## High-value 10/10 features

For an add-on/update tracker, prioritize operator truth over decoration:

1. Visible exact commands for every actionable row.
2. Copy buttons for commands/paths/source links.
3. Preview/dry-run before apply-all.
4. Apply-all enabled only after a successful safe plan.
5. Clear blocking of manual/local/weak-provenance items.
6. Scan health: generated time, scan duration, refresh result.
7. Scheduler/cron visibility.
8. Clickable KPI filters: updates, manual review, weak sources, freshness/registry.
9. Server-persisted known/ignored/manual-review state.
10. Custom git repo registry for future external installs.
11. Audit log for run/update/state-change actions.

## Future repo tracking model

Use a layered discovery model:

- Git plugins under `/root/.hermes/plugins` are auto-discovered.
- Git repos under `/root/.hermes` are auto-discovered, excluding caches/logs/profiles.
- Repos referenced by Hermes config, especially `mcp_servers`, are auto-discovered.
- External repos outside these roots need a dashboard registry entry with an absolute repo-root path.
- Registry entries should be scanned by the same generator and shown as external git repos.

A good registry file shape:

```json
{
  "custom_git_repos": [
    {"path": "/absolute/path/to/repo", "label": "optional-name", "added_at": 1770000000, "source": "dashboard"}
  ]
}
```

## Backend route activation pitfall

After editing `dashboard/plugin_api.py`, the live dashboard may still serve the old mounted route table. Symptoms:

- new frontend appears, but new API route returns the SPA HTML shell
- POST route returns `405 Method Not Allowed`
- direct file checks pass but browser-authenticated fetches hit old behavior

Fix/verification path:

1. Restart the dashboard process/service after plugin API changes, with user approval if required.
2. Browser-fetch each new route with `X-Hermes-Session-Token`.
3. Confirm status, content type/body shape, and JSON fields.
4. Only then claim backend persistence or registry actions are live.

## Safe verification scriptlet

In the browser console context:

```js
(async () => {
  const h = {'X-Hermes-Session-Token': window.__HERMES_SESSION_TOKEN__, 'Content-Type': 'application/json'};
  const state = await fetch('/api/plugins/third-party-tracker/state', {headers: h});
  const stateText = await state.text();
  return {status: state.status, text: stateText.slice(0, 200)};
})();
```

Expected: JSON containing `state` and `registry`, not `<!doctype html>`.
