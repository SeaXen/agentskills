# Analytics tabs: one-line toolbar + one-line stats

For Hermes analytics pages (Sessions, Requests, Messages, Models) on compact dark dashboards.

## Toolbar card (single visible row)
- `sessions-bar-row`: `display:flex; align-items:center; gap:8px; flex-wrap:nowrap`
- Title + truncated meta + window/actions on the left/middle
- **Provider/source chips on the same row** — `flex:1; min-width:0; overflow-x:auto; flex-wrap:nowrap` — not a second card row unless user explicitly asked for two-row layout per `two-row-toolbar-and-stats-strip.md`

## Stats strip (separate block below toolbar)
- `tools-stats-row` with `grid-template-columns: repeat(8, 1fr)` and `!important` if legacy CSS fights
- Mobile: same horizontal scroll pattern as Skills/Journey (`grid-auto-flow: column`)
- Short labels: `Input`, `Cost`, `Sess` — not long prose labels

## "Nothing changed after refresh"
1. `curl` served HTML for `dashboard.js?v=` and new markup ids/classes
2. If host file is new but curl is old → **Docker static not mounted** — add `./static:/app/static:ro` or rebuild image
3. Bump `?v=` and hard refresh only after (1) passes

See `feature-building` → `references/hermes-state-analytics-dashboard.md` for full backend/tab grain.