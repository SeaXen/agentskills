# AceRoute diagnostics page pattern

Use for self-hosted dashboard apps that already have multiple cached pages and need an operator trust/observability pass.

## Backend route
Add a compact route like `/api/diagnostics` that returns:
- `health`: status + uptime
- `state_signature`: compact upstream-state fingerprint
- `cache`: TTL, refresh interval, coalesce window, LRU size/capacity, row count, stale keys, bad refresh statuses
- `probes`: per-endpoint timing probes with `label`, `ms`, `size_bytes`, `row_count`, `cache`, `error`
- `slowest`: top slow probes sorted descending by `ms`
- `summary`: counts for probe_count, warm_hits, coalesced, misses, fresh, slow_over_100ms, max_ms

## Probe pattern
Useful probe set for an AceRoute-class app:
- Home
- Costs
- Channels
- Ops
- Sessions
- Requests
- Messages
- Models
- Tools

Each probe should measure wall-clock time around the real cached wrapper, not a fake synthetic timer.

## UI pattern
Add a dedicated `Diag` nav page with:
- KPI summary row
- chips for status / cache rows / TTL / refresh cadence / coalesce window
- lists for endpoint timings, cache health, warnings, runtime/security
- slowest-path table
- explicit `Warm` button wired to `/api/cache/refresh`

## Verification checklist
- `curl -I /` shows security headers live:
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options: SAMEORIGIN`
  - `Referrer-Policy: strict-origin-when-cross-origin`
  - `Permissions-Policy: camera=(), microphone=(), geolocation=()`
- `curl / | grep` confirms:
  - diagnostics nav button
  - diagnostics page container
  - cache-busted JS asset bump
- `curl /api/diagnostics?...` returns valid JSON with expected keys
- `POST /api/cache/refresh` returns a real refresh count and duration

## Important lesson
If the browser runtime crashes on the host, do not conclude the page is broken. Verify with API output, served HTML, headers, and measured timings. Report the browser-runtime failure separately.