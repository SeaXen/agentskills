# SeaDash UI table-parity + cached-hydration notes

Use when the dashboard has both card/grid and table/column modes, and one mode silently lags behind the other.

## What to preserve

- Every section present in grid mode must also render in table mode:
  - Core
  - Docker
  - Public via Cloudflare
  - Internal Only
  - Sensitive/Admin
- Table mode should carry the same operator signals as cards:
  - exposure badges: `PUBLIC`, `LOCAL`, `ZERO TRUST`, `SENSITIVE`
  - issue badges: `OFFLINE`, `PUBLIC DOWN`, `EXPOSED`
- Public-facing utility links (for example cloudflared website cards/rows) must be clickable in both modes.

## Recovery / implementation pattern

1. Audit both render paths separately. Do not assume a working grid renderer implies table mode is complete.
2. Check live DOM counts for each section after switching views. Missing rows usually mean a partial or stale table renderer.
3. If cold reload is blank but manual refresh repopulates the page:
   - remove stacked init hacks (`body onload`, trailing kick scripts, repeated timers)
   - keep one stable init path
   - hydrate immediately from last known cached payload, then refresh live
4. Prefer a cached first paint for dashboards that already poll APIs. This avoids blank cold loads while preserving fresh data after boot.
5. After refactors, verify both:
   - clean reload with cache present
   - explicit view switch between grid and table

## Concrete verification ideas

- card count is non-zero after hard reload
- table mode shows non-zero rows for public/internal/sensitive sections
- grid mode is hidden when table mode is active, and vice versa
- cloudflared/public website rows resolve to the real public URL, not a dead placeholder
- dead apps like N8N/Dashdot remain visually obvious near the top

## Common failure pattern

A large single-file `index.html` accumulates multiple boot paths over time. One path updates cards, another updates tables, and a reload helper masks the breakage. Result: grid looks alive, table is stale or incomplete, and cold load may blank until a timer runs. Fix by collapsing to one init/data flow and keeping cached hydration minimal and explicit.
