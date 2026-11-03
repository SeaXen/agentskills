# AceRoute Tools tab — feature bundle (post state.db sync)

Use after `aceroute-tools-page-state-db-sync.md` is in place. Covers UI/UX expansion on `:8866` Tools tab.

## Layout (user-mandated — do not regress)

Two rows only — see `dashboard-ui-polish` → `references/two-row-toolbar-and-stats-strip.md`:

1. `tools-bar-card` — one line: title, short sync, window, actions, chips.
2. `tools-stats-row` — six inline `mini-stat` cards only.

Never merge bar + stats into one hero card after user correction.

## Backend additions (`aceroute_tools.py`)

- `tool_groups` (core / browser / mcp / other), `tool_stacked`, `hourly`, `tool_pairs`, `heavy_sessions`, `window_delta` on summary.
- `GET /api/tools/tool?tool_name=&days=` — timeline + sessions using tool.
- `GET /api/tools/export?days=&format=csv|json`.

## Frontend highlights (`dashboard.js`)

- Category pills, stacked top-tools/day chart, UTC hour chart, tools table with last-used, common sequences, heavy session cards.
- Session table: search, sort, API column; drawer prev/next in filtered session list.
- Tool drawer mode (`toolsDrawerBodyTool`) with mini timeline chart.
- Export: `⬇` CSV + `{ }` JSON; show `Loading…` on stats during fetch.
- Co-occurrence scan can be slow on first 30d load — acceptable; cache via `ToolsAnalyticsCache`.

## Verification

- `curl /api/tools?days=7` includes `tool_groups`, `tool_stacked`, `heavy_sessions`.
- Browser: `renderToolsCategoryPills` exists (`dashboard.js?v=18+`), stacked + hour charts via `Chart.getChart`.
- Layout: `toolsSummary` is sibling after `.tools-bar-card`, six stats one row.

## Commits (AceRoute)

- `5264311` — expand Tools analytics/filters/drill-downs
- `e4427cd` — Search polish + JSON export + compact empty sections