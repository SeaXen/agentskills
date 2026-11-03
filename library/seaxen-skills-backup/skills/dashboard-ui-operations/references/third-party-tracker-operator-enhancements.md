# Third-party tracker operator enhancements

Session pattern: improving a dist-only Hermes dashboard plugin used as an update/inventory tracker.

## Durable UI additions

For tracker-style pages that already have scan/copy/dry-run/apply controls, high-value additions are:

- clickable KPI/operator chips that act as filters (`updates`, `manual`, `weak-source`)
- an active filter strip with a clear/reset control
- visible command list in the action block before copy/apply
- scan metadata surfaced near the controls: status, generated timestamp, duration seconds, data freshness, generator path
- scheduler/cron metadata surfaced as operator health: job name, schedule, configured/enabled state
- manual/local item review cards with bulk copy helpers and per-item `Mark known` / `Unmark known`
- weak-source/source-mapping review section with search/copy helpers

## Safe implementation shape

For dist-only plugin bundles:

1. Back up `dist/index.js`, `dist/style.css`, and any generator script before edits.
2. Extend the generator payload when the data belongs to generation time:
   - `scan_health.started_at`
   - `scan_health.duration_seconds`
   - `scheduler.job_name`
   - `scheduler.schedule`
   - `scheduler.status`
3. Keep user-local review state in browser `localStorage` when it is only a UI triage preference. Do not mutate the inventory schema just to remember that a known manual plugin is known.
4. Keep the safe command pool derived from actionable update items only. Inventory/manual rows should not leak fallback commands into bulk copy/apply.
5. Require dry-run/preview before enabling mutating bulk apply, and add a browser confirmation before execution.

## Bugs this pattern caught

- A fallback Hermes core inventory row generated `hermes update -y` even when core had zero updates. Fix at command-target construction: core commands are valid only when `update_status === 'update_available'`.
- A manual hide/show toggle only hid the separate manual section, not manual/local rows inside the plugin inventory list. Fix every visible list, not only the section with the same label.
- A live scan button can legitimately take ~25 seconds if the generator shells out to git/network checks. Test with a long enough wait before calling it stuck.

## Verification checklist

- syntax-check the bundle (`node --check dist/index.js`)
- compile any Python plugin/generator code
- run the generator and inspect the added metadata fields
- verify served route, not only files on disk
- assert visible command text exactly matches the dry-run API plan
- click KPI filters and confirm the right section appears
- test `Mark known` and `Unmark known` persistence in the browser
- inspect browser console after interactions; require zero JS errors
- do not execute mutating apply/run actions without user permission
