# Slow-loading dashboard auto-refresh pattern

Use for Hermes/self-hosted dashboards where all-time SQLite/chart loads can take noticeable time.

## UI pattern
- Header controls: time range, `Auto` label, auto-refresh select, manual refresh, load status.
- Auto options for Dr. Sagar dashboards: `Off`, `5s`, `10s`, `20s`, `1min`.
- Default can be `20s` unless the user asks otherwise.
- Persist interval in `localStorage`.
- Header status examples: `Loading…`, `Auto loading…`, `Loaded 0.1s · Auto 20s`, `Auto off`, `Load error`.

## Loading behavior
- First load or major range/page change: show a loading shell with skeleton cards/charts and explanatory text.
- Manual refresh / auto refresh: keep existing dashboard visible; only header status changes. Do not blank the app with a spinner.
- Guard against overlapping auto-refresh requests with an `isLoading` flag. If the reason is `auto` and a load is active, skip the tick.

## Verification
- Live browser DOM confirms dropdown options and selected value.
- `setAutoRefresh('0')` disables timer and status says `Auto off`.
- `setAutoRefresh('5000')` creates timer and persists `5000`.
- Background refresh does not create skeletons or erase current cards.
- First-load shell has visible skeletons.
- Browser console has zero JS errors.
