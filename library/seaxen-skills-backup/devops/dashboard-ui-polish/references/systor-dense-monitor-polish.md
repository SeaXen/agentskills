# Systor dense monitor UI polish patterns

Use for lightweight Linux/system monitor dashboards with raw `/proc`, SQLite history, custom canvas charts, Apps/process pages, and Network usage tables.

## Chart refresh vs data sampling
- Distinguish **redraw interval** from **collector sample interval**.
  - Chart refresh = how often the browser refetches/redraws.
  - Collector sample interval = how often new points are written to SQLite.
- If charts are set to 1s/5s but samples are written every 30s, the chart is working but appears frozen for up to 30s.
- Verification probe:
  - fetch a series repeatedly and inspect tail timestamps; expected deltas should match collector sample interval.
  - browser probe canvas `toDataURL().length` to confirm the renderer is not blank.
- UI status should never return to vague `idle` after success. Prefer explicit timestamps: `snapshot 12:33:25 AM`, `charts 12:33:32 AM`.
- If offering true 1s charts, expose both controls honestly:
  - chart refresh 1s
  - sample interval 1s
  - keep 5s default for lightweight operation because 1s increases CPU/disk writes.
- Avoid duplicate Settings controls with the same form name. If a runtime row displays the same value, make it disabled/display-only and put the real saved control in the defaults section.

## Settings source of truth
- Settings page is saved defaults.
- Page controls are temporary live overrides unless the UI explicitly says otherwise.
- Do not silently persist page controls to localStorage if that conflicts with Settings defaults.
- Add copy in Settings explaining this relationship.

## Apps page full-table fit
- Keep default view as four metric cards: CPU / RAM / Disk / Network.
- Fetch one raw Apps snapshot per refresh, then derive all metric cards client-side. Multiple parallel Apps fetches can corrupt delta-based CPU values.
- For mixed host/docker rows:
  - app name left
  - host PID as small muted right tag (`pid ####`)
  - Docker rows omit PID
- For expandable “Show all apps”:
  - table must fit inside the card; verify actual `table.getBoundingClientRect().width <= card.getBoundingClientRect().width`.
  - if it overflows, merge `Kind` into the App column as a small pill and shorten headers (`CPU`, `RAM`, `DSK`, `NET`).
  - use `table-layout: fixed`, fixed metric-column widths, and ellipsis on app names.
  - provide full-table pagination; do not render hundreds of rows as one wall.

## Network usage table pagination
- Usage table should show 10 rows/buckets by default.
- Add pager for more than 10 days/weeks/months.
- Keep a summary TOTAL row above paged rows.
- Verify real data and a synthetic >10-row case if current live DB has fewer than 10 days:
  - inject 25 rows in browser state
  - page 1 should show `10/25 days · page 1/3`
  - page 2 should show `10/25 days · page 2/3`

## Live verification checklist
- Compile backend/templates.
- Re-run installer/sync for deployed `/opt/...` copies.
- Restart `systor-web` and `systor-collector`.
- Verify health endpoint and active services.
- Browser checks:
  - header height and same-line status
  - canvas `toDataURL().length`
  - no `avg` text if user asked to remove it
  - Settings sample/refresh controls and absence of duplicate submitted controls
  - Network usage table row count and pager state
  - Apps full table width <= card width
