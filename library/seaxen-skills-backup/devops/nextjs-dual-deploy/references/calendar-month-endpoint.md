# Per-month calendar endpoints for time-series dashboards

Pattern for adding a "navigate to any month" feature to a calendar/heatmap widget in a self-hosted dashboard. Captured from the **Tradingx** v0.3 build at `/mnt/tb/1Apps/Tradingx`, where the dashboard calendar went from "stuck on a hardcoded January-2026" to "user clicks ‹/› → re-fetches that month from the DB → shows real per-day P&L + trade counts."

Use this when the app needs:

- A monthly calendar / heatmap view that shows data for any past or future month, not just the current one.
- Per-day aggregates derived from a time-series event table (trades, posts, deploys, work items, etc.).
- A consistent response shape the calendar grid can consume (per-day map + weekly buckets + month totals + best/worst day).
- Empty-state handling when the queried month has no data.

## Architecture at a glance

```
┌────────────────────────────────────────────────────────┐
│  Browser                                              │
│  ├─ <CalendarGrid month="June-2026" onMonthChange/>  │ ← prev/next arrows
│  └─ <DemoAwareCalendar />                            │ ← owns month state
│       └─ fetch /api/analytics/calendar?month=YYYY-MM │ ← one request per month
└──────────────────────┬─────────────────────────────────┘
                       │
                       ▼
┌────────────────────────────────────────────────────────┐
│  app/api/analytics/calendar/route.ts                  │
│  ├─ Parse ?month=YYYY-MM (default: current month)     │
│  ├─ SQL: GROUP BY day for that month window           │
│  ├─ Compute: perDay, weeks, monthTotal, bestDay,      │
│  │            worstDay, startCapital                  │
│  └─ Return as JSON                                    │
└──────────────────────┬─────────────────────────────────┘
                       │
                       ▼
              SQLite (better-sqlite3)
              SELECT strftime('%d', ts/1000, 'unixepoch') AS day,
                     SUM(pnl) AS pnl, COUNT(*) AS trades,
                     SUM(pnl>0) AS wins, SUM(pnl<0) AS losses
              FROM trades
              WHERE ts/1000 BETWEEN ? AND ?
              GROUP BY day ORDER BY day
```

## The endpoint

```ts
// app/api/analytics/calendar/route.ts
import { db } from "@/lib/crypto/db";
import { ok, safe } from "@/lib/crypto/api";

export const dynamic = "force-dynamic";

function monthBounds(monthParam?: string) {
  const now = new Date();
  let year = now.getUTCFullYear();
  let month = now.getUTCMonth();                // 0-indexed
  if (monthParam && /^\d{4}-\d{2}$/.test(monthParam)) {
    const [y, m] = monthParam.split("-").map(Number);
    if (!isNaN(y) && m >= 1 && m <= 12) { year = y; month = m - 1; }
  }
  const monthKey = `${year}-${String(month + 1).padStart(2, "0")}`;
  const startTs = Math.floor(Date.UTC(year, month, 1) / 1000);
  const endTs = Math.floor(Date.UTC(year, month + 1, 1) / 1000) - 1;
  return { year, month, monthKey, startTs, endTs };
}

export async function GET(req: Request) {
  return safe(async () => {
    const { year, month, monthKey, startTs, endTs } =
      monthBounds(new URL(req.url).searchParams.get("month") ?? undefined);

    const dailyRows: any[] = db().prepare(`
      SELECT
        strftime('%d', ts / 1000, 'unixepoch') AS day,
        COALESCE(SUM(pnl), 0)              AS pnl,
        COUNT(*)                            AS trades,
        SUM(CASE WHEN pnl > 0 THEN 1 ELSE 0 END) AS wins,
        SUM(CASE WHEN pnl < 0 THEN 1 ELSE 0 END) AS losses
      FROM trades
      WHERE ts / 1000 BETWEEN ? AND ?
      GROUP BY day
      ORDER BY day ASC
    `).all(startTs, endTs);

    const perDay: Record<number, { pnl: number; trades: number; wins: number; losses: number }> = {};
    let totalPnl = 0, totalTrades = 0, totalWins = 0, totalLosses = 0;
    let bestDay: { day: number; pnl: number } | null = null;
    let worstDay: { day: number; pnl: number } | null = null;

    for (const r of dailyRows) {
      const d = parseInt(r.day, 10);
      perDay[d] = { pnl: r.pnl, trades: r.trades, wins: r.wins ?? 0, losses: r.losses ?? 0 };
      totalPnl += r.pnl; totalTrades += r.trades;
      totalWins += r.wins ?? 0; totalLosses += r.losses ?? 0;
      if (!bestDay || r.pnl > bestDay.pnl) bestDay = { day: d, pnl: r.pnl };
      if (!worstDay || r.pnl < worstDay.pnl) worstDay = { day: d, pnl: r.pnl };
    }

    // Weekly aggregates (for sidebar mini-charts). Trivial 1-7 / 8-14 / 15-21 / 22-28 / 29-end split.
    const weeks: { pnl: number; trades: number; days: number }[] = [];
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    for (const ws of [1, 8, 15, 22, 29]) {
      if (ws > daysInMonth) break;
      const we = Math.min(ws + 6, daysInMonth);
      let wPnl = 0, wTrades = 0, wDays = 0;
      for (let d = ws; d <= we; d++) {
        const row = perDay[d];
        if (row) { wPnl += row.pnl; wTrades += row.trades; if (row.pnl !== 0 || row.trades > 0) wDays++; }
      }
      weeks.push({ pnl: wPnl, trades: wTrades, days: wDays });
    }

    const baseRow: any = db().prepare(`SELECT value FROM settings WHERE key = 'starting_capital'`).get();
    const startCapital = baseRow ? parseFloat(baseRow.value) : 0;

    return ok({
      month: monthKey, year, monthIndex: month, daysInMonth, startCapital,
      perDay, weeks,
      monthTotal: { pnl: totalPnl, trades: totalTrades, wins: totalWins, losses: totalLosses,
                    winRate: totalTrades > 0 ? (totalWins / totalTrades) * 100 : 0 },
      bestDay, worstDay,
    });
  });
}
```

## Response shape (stable)

```json
{
  "month": "2026-06",
  "year": 2026,
  "monthIndex": 5,
  "daysInMonth": 30,
  "startCapital": 0,
  "perDay": {
    "3":  { "pnl":  450, "trades": 1, "wins": 1, "losses": 0 },
    "7":  { "pnl": -120, "trades": 1, "wins": 0, "losses": 1 },
    "18": { "pnl": 1200, "trades": 1, "wins": 1, "losses": 0 }
  },
  "weeks": [
    { "pnl":  330, "trades": 2, "days": 2 },
    { "pnl":  780, "trades": 1, "days": 1 },
    { "pnl": 1380, "trades": 2, "days": 2 },
    { "pnl":  340, "trades": 1, "days": 1 },
    { "pnl":  740, "trades": 2, "days": 2 }
  ],
  "monthTotal": { "pnl": 3190, "trades": 8, "wins": 5, "losses": 3, "winRate": 62.5 },
  "bestDay":  { "day": 18, "pnl": 1200 },
  "worstDay": { "day": 25, "pnl": -180 }
}
```

This shape is enough to render the calendar heatmap, the weekly mini-charts, and the "best/worst day" callouts without a second round-trip.

## The grid component (accepts a month change callback)

```tsx
// components/CalendarGrid.tsx
"use client";
import { useState } from "react";

type DayCell = { day: number | null; pnl?: number; trades?: number };
type CalendarGridProps = {
  month: string;                  // e.g. "June-2026"
  weeks: DayCell[][];
  onMonthChange?: (offset: number) => void;   // ← new
};

export function CalendarGrid({ month, weeks, onMonthChange }: CalendarGridProps) {
  const [offset, setOffset] = useState(0);
  const [mIdx, yIdx] = (() => {
    const [name, year] = month.split("-");
    return [monthNames.indexOf(name), parseInt(year, 10)];
  })();
  const totalMonth = mIdx + offset;
  const newYear = yIdx + Math.floor(totalMonth / 12);
  const newMonth = ((totalMonth % 12) + 12) % 12;
  const displayed = `${monthNames[newMonth]}-${newYear}`;

  function shift(delta: number) {
    setOffset((o) => o + delta);
    onMonthChange?.(delta);
  }

  return (
    <div className="surface p-4">
      <button onClick={() => shift(-1)} aria-label="Previous month">‹</button>
      <div>{displayed}</div>
      <button onClick={() => shift(1)} aria-label="Next month">›</button>
      {/* … day grid, identical to before … */}
    </div>
  );
}
```

The grid stays pure/dumb — it doesn't fetch anything. The parent owns the data lifecycle.

## The wrapper (owns the month state, fetches on change)

```tsx
// components/DemoAwareCalendar.tsx
"use client";
import { useEffect, useState } from "react";
import { useSettings } from "@/lib/settings";
import { buildMonth, SAMPLE_PNL } from "@/lib/calendar";
import { CalendarGrid } from "./CalendarGrid";

const MONTH_NAMES = ["January", "February", "March", "April", "May", "June",
                     "July", "August", "September", "October", "November", "December"];

export function DemoAwareCalendar() {
  const { settings, hydrated } = useSettings();
  const [data, setData] = useState<CalendarResponse | null>(null);
  const [offset, setOffset] = useState(0);

  const now = new Date();
  const totalMonth = now.getMonth() + offset;
  const newYear = now.getFullYear() + Math.floor(totalMonth / 12);
  const newMonth = ((totalMonth % 12) + 12) % 12;
  const monthKey = `${newYear}-${String(newMonth + 1).padStart(2, "0")}`;
  const label = `${MONTH_NAMES[newMonth]}-${newYear}`;

  useEffect(() => {
    let cancelled = false;
    setData(null);                              // show loading state cleanly
    fetch(`/api/analytics/calendar?month=${monthKey}`, { cache: "no-store" })
      .then((r) => r.json())
      .then((j) => { if (!cancelled) setData(j.ok ? j.data : null); })
      .catch(() => !cancelled && setData(null));
    return () => { cancelled = true; };
  }, [monthKey]);

  // Demo fallback when toggle ON + no real data for this month
  const hasData = data?.perDay && Object.keys(data.perDay).length > 0;
  const pnlMap = hasData
    ? Object.fromEntries(Object.entries(data!.perDay).map(([k, v]) => [parseInt(k, 10), v]))
    : (settings.showDemoData ? SAMPLE_PNL : {});

  const weeks = buildMonth(newYear, newMonth, pnlMap);

  return (
    <CalendarGrid
      month={label}
      weeks={weeks}
      onMonthChange={(delta) => setOffset((o) => o + delta)}
    />
  );
}
```

The pattern in four lines:

1. **State lives in the parent**, not the grid. `offset` is an integer counter.
2. **URL is derived from state**: `monthKey = ${year}-${MM}`.
3. **useEffect re-fires** on `monthKey` change (note the dep array, not `offset`).
4. **`cancelled` flag** prevents stale responses from overwriting newer ones when the user mashes the prev/next arrows.

## Common pitfalls

### Don't derive the year from `Date` directly when crossing Dec/Jan

Naive code: `new Date(now.getFullYear(), now.getMonth() + offset, 1)` works because the JS Date constructor rolls over automatically. But manual arithmetic fails:

```ts
// BAD — month overflow
const newMonth = now.getMonth() + offset;     // can be 12, 13, -1
if (newMonth > 11) { newYear++; newMonth -= 12; }   // misses < 0 case
```

```ts
// GOOD — let Math.floor do the work
const totalMonth = now.getMonth() + offset;
const newYear = now.getFullYear() + Math.floor(totalMonth / 12);
const newMonth = ((totalMonth % 12) + 12) % 12;     // the +12 handles negatives
```

The Tradingx calendar had this exact bug for the first cut; the `(totalMonth % 12 + 12) % 12` pattern is the cleanest.

### Use `cache: "no-store"` on the fetch

The user is clicking prev/next. Next.js's default fetch cache would otherwise return the first month's response for every subsequent click. Annoying to debug because the first load "works."

```ts
fetch(`/api/analytics/calendar?month=${monthKey}`, { cache: "no-store" })
```

### Reset data to `null` before refetching

When the user clicks from June → July, you want a loading state. If you don't reset, the old June data briefly flashes for July until the new response lands. One line:

```ts
useEffect(() => {
  setData(null);                  // clear before fetch
  fetch(...).then(...);
}, [monthKey]);
```

### Don't fetch the same month twice in a row

If the user double-clicks "Next month" quickly enough that the second click lands on the same month they're already on, you'll fire two requests. Cheap to fix with a small "is this the month I'm already showing?" guard, or just rely on the `cancelled` flag.

### Don't put `cache: "force-cache"` on the SQL query

`db().prepare(...).all(...)` is synchronous and uncached by design. The "cache" in Next.js is the HTTP fetch cache, not SQLite. Don't add wrapper code that tries to memoize per-day aggregates — the query is sub-millisecond and runs on every request already.

### Empty months should return `perDay: {}`, not throw

The user will navigate to a month with no trades. The endpoint should return `perDay: {}` and `monthTotal: { pnl: 0, trades: 0, ... }`. The UI then renders an empty grid with the empty-state hint. The `bestDay` / `worstDay` should be `null`, not synthesized.

### Don't include `monthIndex` in the URL

Some apps use `?monthIndex=5&year=2026` (two params). The single `?month=YYYY-MM` is shorter, sortable, and harder to mismatch (e.g. February=2 vs February=1). The endpoint validates the format and defaults to current month on bad input.

## Reference implementation

Tradingx v0.3:

- `app/api/analytics/calendar/route.ts` — endpoint.
- `components/CalendarGrid.tsx` — dumb grid, accepts `onMonthChange`.
- `components/DemoAwareCalendar.tsx` — owns the month state, fetches per month, falls back to demo seed when toggle ON + no real data.

End-to-end verified: with 8 seeded trades for June 2026, navigating June → July correctly shows June populated and July empty (with the empty-state hint). The `monthTotal.pnl` matches the sum of the per-day P&L values, and `bestDay` / `worstDay` point to the actual extreme days.

The same pattern works for any time-series table: posts per day, deploys per day, work items closed per day, API calls per hour, etc. Just change the SQL aggregation and the field names.
