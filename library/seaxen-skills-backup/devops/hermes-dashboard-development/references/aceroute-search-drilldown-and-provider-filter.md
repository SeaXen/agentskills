# AceRoute Search page — drill-down and provider-filter pass

## What changed

This pass turned the `Search` page from a passive analytics view into an investigation surface.

### UI changes
- Added a compact filter/meta strip below the overview cards:
  - `Search detail view • all providers`
  - provider chip row
  - `Clear` button when filtered
- Split overview top row so `Searches` and `Extracts` are separate cards.
- Added a unified right-side `Search Detail` drawer with:
  - `Summary`
  - `Signals`
  - `Primary Content`
  - `Related Activity`
  - actions: `Copy Primary`, `Filter Provider`, `Search Query`

### Clickable drill-down entry points
- Provider Breakdown table rows
- Cost by Provider doughnut chart
- Provider Comparison chart bars
- Top Queries list
- Recent Queries rows
- Error rows
- Zero-Result Queries rows
- Extract log rows

## State pattern that worked

Use one shared provider filter state:

```js
let searchState = {
  provider: '',
  data: {
    providers: [],
    queries: null,
    errors: [],
    zeroResults: [],
    extract: null,
    compare: []
  }
};
```

Helpers that mattered:
- `currentSearchProvider()`
- `searchProviderMatches(raw)`
- `renderSearchActiveFilters()`
- `setSearchProviderFilter(provider)`
- `clearSearchDetailFilters()`
- `applyProviderFilterFromDisplay(displayName)`

Rule: every provider-driven interaction must route through the same state path.

## Drawer payload pattern

Keep the drawer generic enough to handle several source types:
- `top-query`
- `recent-query`
- `error`
- `zero-result`
- `extract`

Useful helpers:
- `searchDetailPrimaryText(payload)`
- `searchRelatedRows(payload)`
- `openSearchDetailDrawer(type, payload)`
- `applyDrawerProviderFilter()`
- `applyDrawerQuerySearch()`

The drawer should derive related activity from already-fetched page data instead of requiring a new backend endpoint.

## Empty-state rules

When filtered, empty states must mention the active filter explicitly:
- `No recent queries for current filter`
- `No errors for current filter`
- `No zero-result queries for current filter`
- `No extract calls for current provider filter`

Generic `No data yet` text reads broken once the page supports drill-downs.

## Verification pattern that worked

### Static checks
```bash
cd /mnt/tb/1Apps/AceRoute
node --check static/js/dashboard.js
git diff --check
```

### Live rebuild
```bash
docker compose up -d --build --force-recreate
```

### Browser checks
Use DOM inspection for text state and `Chart.getChart(...)` for chart readiness.

Important reliable checks:
- provider chip text appears after clicking a provider row
- meta text changes to `filtered to <Provider>`
- `Search Detail` drawer opens from recent/top-query rows
- drawer buttons show all 4 actions
- `Chart.getChart(document.getElementById('providerCompareChart'))` exists
- directly invoke `compare.options.onClick(...)` to verify chart-driven filter wiring

Example browser-console checks:
```js
const compare = Chart.getChart(document.getElementById('providerCompareChart'));
compare.options.onClick(null, [{index:0,datasetIndex:0}], compare);
document.getElementById('searchResultsMeta').textContent;
```

## Why this pass matters

The Search page was already visually improved, but it still lacked operator workflow. The big gain was not another chart; it was making existing charts/tables/list items act as controls and converge into one detail drawer.
