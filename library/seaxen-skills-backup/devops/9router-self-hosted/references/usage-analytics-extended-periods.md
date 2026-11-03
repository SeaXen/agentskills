# 9router — extended Usage & Analytics periods

## Problem
Dashboard **Usage & Analytics** selector stopped at **60D**. Operators wanted **90D, 180D, 365D, All**.

## Upstream fix (preferred)
- **PR:** https://github.com/decolua/9router/pull/2361
- **Module:** `src/lib/usagePeriods.js` — `USAGE_PERIOD_OPTIONS`, validators, `getUsagePeriodDays`, `getChartDayBucketCount`
- **Touch points:** `usage/page.js`, `UsageStats.js`, `api/usage/stats/route.js`, `api/usage/chart/route.js`, `src/lib/db/repos/usageRepo.js`
- **Tests:** `tests/unit/usage-periods.test.js`, extended cases in `tests/unit/db-sqlite-vs-lowdb.test.js`

## Local workaround (pre-merge)
Script patches minified `.next` bundles inside the **running** container, then restarts:

- Host path: `/mnt/tb/1Apps/9router/patches/apply-usage-periods.py`
- Re-run after every `docker compose pull` / recreate

## Data bounds
**All** only includes rows in `usageDaily` / `usageHistory` — no schema migration.