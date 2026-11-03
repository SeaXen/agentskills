# Usage & Analytics table sorting (upstream vs period PR)

## Upstream (`decolua/9router` master)

Sorting is **implemented and intended**:

- `src/shared/components/UsageStats.js` — `sortBy` / `sortOrder` from URL, `toggleSort()`, `sortData()` before `groupDataByKey()`
- `src/app/(dashboard)/dashboard/usage/components/UsageTable.js` — clickable `<th>`, `onToggleSort`, `SortIcon` (↕/↑/↓)

## Period / layout work (PR #2361, `feat/usage-analytics-extended-periods`)

- `UsageTable.js` — **unchanged** vs upstream for sort handlers
- `UsageStats.js` — sort block unchanged; periods move to `USAGE_PERIOD_OPTIONS` import
- `usage/page.js` — tab/period **layout** only (`handleTabChange` preserves existing query params including `sortBy`)

**Conclusion:** Extended periods are **not** a deliberate removal of sorting logic. If headers do nothing on a **live Docker** instance, suspect:

1. Stale cached `.next` chunk (hard refresh)
2. Layout overlay blocking header clicks (minified bundle patch era)
3. URL not updating on click (`router.replace` / query params)

## PR quality

Fix sorting on live instance if user-visible regression exists, but do **not** claim upstream never had sorting. Compare fork to master on `UsageStats.js` + `UsageTable.js` before adding sort-specific commits.

## User asks "just answer"

Answer directly: **main repo and fork are the same for sorting source**; period patch did not intentionally change it; broken UX on box = runtime/regression, not missing upstream feature.