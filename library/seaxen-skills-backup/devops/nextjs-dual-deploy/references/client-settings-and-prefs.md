# Client-side settings + server-rendered content

Pattern for Next.js dashboards where the user toggles preferences (show demo data, compact mode, accent color, base currency) that affect how the server-rendered page displays data. Captured from the Tradingx "Show demo numbers" feature.

## The problem

- The dashboard page is a **Server Component** (faster, no hydration cost).
- The user toggles `showDemoData` in `/settings` — stored in **localStorage** on the client.
- After navigation back to `/`, the server renders demo data by default, because it doesn't know about the user's setting.

Without a pattern, you get flicker: SSR shows demo numbers → hydration runs → client checks localStorage → re-renders without demo numbers. Or worse, the toggle never affects the page.

## Architecture: server renders sensible defaults, client overrides

```
┌──────────────────────────────────────────────────────────┐
│  app/page.tsx (Server Component)                         │
│    → reads DB / APIs, returns structure                  │
│    → renders <DemoAwareDashboardStats />                 │
├──────────────────────────────────────────────────────────┤
│  components/DemoAwareDashboardStats.tsx (Client)         │
│    → "use client" at top                                 │
│    → useSettings() reads localStorage                    │
│    → useEffect() fetches /api/analytics/summary          │
│    → decides what to show: real / demo / empty           │
│    → returns JSX that REPLACES the server fallback       │
├──────────────────────────────────────────────────────────┤
│  lib/settings.ts                                         │
│    → tiny pub-sub store, no Zustand dependency           │
│    → persists to localStorage on every change            │
│    → useSettings() hook in any client component         │
└──────────────────────────────────────────────────────────┘
```

The server component renders the structure (cards, layouts, dividers). The client component inside decides what *content* fills those slots, based on settings + fetched data. No flicker — server renders a "loading-shaped" placeholder, client swaps in the real decision on hydration.

## The settings store (`lib/settings.ts`)

A tiny pub-sub pattern that avoids the Zustand dependency:

```ts
"use client";
import { useEffect, useState, useCallback } from "react";

export type Settings = {
  showDemoData: boolean;
  compactMode: boolean;
  showHelpHints: boolean;
  baseCurrency: "USD" | "EUR" | "GBP" | "BDT" | "USDT";
  dateFormat: "YYYY-MM-DD" | "DD/MM/YYYY" | "MM/DD/YYYY";
  timezone: string;
  defaultRiskPct: number;
  defaultRR: number;
  maxOpenPositions: number;
  accent: "green" | "amber" | "blue" | "rose";
};

const DEFAULTS: Settings = { /* … */ };
const STORAGE_KEY = "myapp:settings:v1";

function loadFromStorage(): Settings {
  if (typeof window === "undefined") return DEFAULTS;
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? { ...DEFAULTS, ...JSON.parse(raw) } : DEFAULTS;
  } catch { return DEFAULTS; }
}

function saveToStorage(s: Settings) {
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(s)); } catch {}
}

// Module-level state + listeners — no React Context needed.
let _state: Settings = DEFAULTS;
const _listeners = new Set<() => void>();
let _hydrated = false;

function ensureHydrated() {
  if (_hydrated || typeof window === "undefined") return;
  _state = loadFromStorage();
  _hydrated = true;
}

function setState(patch: Partial<Settings>) {
  _state = { ..._state, ...patch };
  saveToStorage(_state);
  _listeners.forEach((l) => l());
}

export function useSettings() {
  const [hydrated, setHydrated] = useState(_hydrated);
  const [, setTick] = useState(0);
  useEffect(() => {
    ensureHydrated();
    setHydrated(true);
    setTick((t) => t + 1);                 // re-render with real state
    const l = () => setTick((t) => t + 1); // subscribe to future changes
    _listeners.add(l);
    return () => { _listeners.delete(l); };
  }, []);
  return {
    settings: _state,
    setSettings: setState,
    reset: useCallback(() => setState(DEFAULTS), []),
    hydrated,
  };
}
```

### Why the `hydrated` flag must be exposed (not just module-level)

A `useSettings()` consumer often needs to render a clean placeholder during SSR/first-paint, then swap to the real decision. Without an explicit `hydrated` boolean, the consumer can't tell whether the current `settings.showDemoData` is the **server default** or the **user's localStorage value**. Concretely: if the user turns demo OFF and navigates to `/`, the server renders with `showDemoData: true` (the default), and the consumer's three-state logic will use the wrong branch until the client hydrates — leaking demo numbers for one frame.

Pattern:

```tsx
const { settings, hydrated } = useSettings();
const [checked, setChecked] = useState(false);

useEffect(() => { /* fetch … .finally(() => setChecked(true)) */ }, []);

if (!hydrated || !checked) {
  return <div className="text-center py-6 text-fg-faint">—</div>;
}
```

Render `—` (a clear empty marker) until **both** the localStorage is read AND the data fetch has resolved. Never render demo data in this state.

## The consumer pattern

```tsx
"use client";
import { useSettings } from "@/lib/settings";

export function DemoAwareDashboardStats() {
  const { settings, hydrated } = useSettings();
  const [real, setReal] = useState<Stats | null>(null);
  const [checked, setChecked] = useState(false);

  useEffect(() => {
    let cancelled = false;
    fetch("/api/analytics/summary", { cache: "no-store" })
      .then(r => r.json())
      .then(j => { if (!cancelled) setReal(j.data.overall); })
      .catch(() => {})
      .finally(() => { if (!cancelled) setChecked(true); });
    return () => { cancelled = true; };
  }, []);

  // SSR/first-paint placeholder
  if (!hydrated || !checked) {
    return <div className="surface p-4 text-fg-faint">—</div>;
  }

  // Decide what to render — three-state logic
  let shown: Stats;
  if (real && real.count > 0) {
    shown = mapReal(real);          // real imported trades win
  } else if (settings.showDemoData) {
    shown = DEMO;                   // user wants demo fallback
  } else {
    shown = EMPTY;                  // user turned demo off, no real data
  }

  return <HeroStrip stats={shown} />;
}
```

The server rendered a "loading-shaped" placeholder. On hydration, the client immediately picks the right one. No visible flicker because the server's placeholder height matches the final rendered height.

## The settings page pattern

`/settings` is itself a client component that uses `useSettings()` and writes via `setSettings`:

```tsx
"use client";
export default function SettingsPage() {
  const { settings, setSettings, reset } = useSettings();
  const [saved, setSaved] = useState(false);

  function flash() { setSaved(true); setTimeout(() => setSaved(false), 1500); }

  return (
    <div>
      <Toggle
        label="Show demo numbers"
        checked={settings.showDemoData}
        onChange={(v) => { setSettings({ showDemoData: v }); flash(); }}
      />
      <Toggle
        label="Compact mode"
        checked={settings.compactMode}
        onChange={(v) => { setSettings({ compactMode: v }); flash(); }}
      />
      {/* … */}
      {saved && <span className="text-accent-green ml-1">✓ Saved</span>}
    </div>
  );
}
```

Every toggle writes to localStorage instantly and re-renders any subscriber. No save button needed.

### Server-side settings vs localStorage (notifications)

Discord/Telegram/webhook URLs and enable flags live in **SQLite** + `/api/notifications/*`, not in `lib/settings.ts`. A 3-column settings page should put **column 3 = alerts**: ChannelStatusBar → **Discord first** → Telegram → webhook. Server flags (`browser_notifications`, `sync_interval_min`) use **`/api/settings/runtime`**. Toggles with `checked={false}` and empty `onChange` are bugs. See `references/tradingx-settings-alerts-perf-social.md`.

## CSS variables for accent color

For a per-user accent color, the cleanest pattern is to set `data-accent` on `<html>` and let CSS variables flip the entire app at once.

```tsx
// components/ThemeApplicator.tsx
"use client";
import { useEffect } from "react";
import { useSettings } from "@/lib/settings";

export function ThemeApplicator() {
  const { settings, hydrated } = useSettings();
  useEffect(() => {
    if (!hydrated) return;
    document.documentElement.setAttribute("data-accent", settings.accent);
  }, [hydrated, settings.accent]);
  return null;
}
```

Mount it once in `app/layout.tsx` so it never unmounts.

```css
/* app/globals.css */
:root {
  --accent-1: #22c55e;        /* default = green */
  --accent-1-deep: #16a34a;
  --accent-1-dim: #0d3a23;
  --accent-1-soft: #22c55e33;
}
:root[data-accent="amber"] { --accent-1: #f59e0b; --accent-1-dim: #3a2a08; /* … */ }
:root[data-accent="blue"]  { --accent-1: #3b82f6; /* … */ }
:root[data-accent="rose"]  { --accent-1: #f43f5e; /* … */ }

.accent-text  { color: var(--accent-1); }
.accent-bg-dim { background-color: var(--accent-1-dim); color: var(--accent-1); }
```

Use the `data-accent` attribute on `<html>` (not `style.setProperty`) because:
- It works without JS — the user can set the attribute manually in DevTools and see live changes.
- It composes with Tailwind's cascade and respects the user's OS dark/light mode preferences naturally.
- It's one attribute, not 4 separate property writes.

Combine static Tailwind tokens (`text-accent-green`) with dynamic utilities (`accent-text`) — keep static tokens for charts/KPIs that should never rebrand, and dynamic ones for user-customizable chrome (chips, hover borders, primary buttons).

## Common pitfalls

### "Server-rendered content respects the toggle but the WRONG thing happens"

If the server already rendered demo numbers and the client toggle is OFF, you need to either:
- **Hide** the server-rendered content when the toggle is off (set display:none), OR
- **Replace** it via a client component that renders the empty state.

Hiding causes layout jumps. Replacing is cleaner — see the three-state pattern above.

### localStorage is unavailable in SSR

Always guard `typeof window === "undefined"` and bail out to `DEFAULTS`. The pattern above handles this.

### SSR fallback strings themselves leak demo data

Even with a clean client-only render path, the **server-rendered placeholder** can still leak demo content. Example mistake: a `SummaryCard` server-renders `<div>Trades: 8</div>` because the page wraps the data fetch in a regular render. The client then re-renders, but the SSR text is briefly visible and shows up in the initial DOM snapshot. Fix: the server-rendered fallback should use the same `—` placeholder as the empty state, not the demo number. Audit every `app/*/page.tsx` and `components/*Card*` for hardcoded strings that look like demo data (`Trades: 8`, `$1.8K`, `50.0%`, `+10.7%`).

### KPI deltas and trend arrows leak when value is empty

A common bug: a `Kpi` component takes `value` (the main number) and `delta` (a small `+2.1%` chip). When `value === "—"`, the `delta` still renders the demo `+2.1%`. Fix: gate the delta on value-empty too:

```tsx
const isEmpty = value === "—";
<span className={"num font-medium " + (isEmpty ? "text-fg-faint" : trendColor)}>
  {isEmpty ? "—" : trend === "up" ? "▲" : trend === "down" ? "▼" : "•"} {delta}
</span>
```

The icon and color also need to be `text-fg-faint` when empty — accent colors on placeholder `—` reads as a fake signal.

### Hero strip "+$X all-time" chip leaks when totalPnl is 0

The hero often renders `<span>+$1,800 all-time</span>` only when `totalPnl !== 0`. When the demo toggle is off, the `EMPTY` stats object has `totalPnl: 0` — the conditional holds, no chip. Good. But if you ever change the default to e.g. `0.0` from a real-data response, the chip would render. Audit every `shown.totalPnl !== 0` conditional against the empty state.

### Calendar must use `new Date()`, not a hardcoded seed month

If your calendar/grid demo seed hardcodes "January-2026" in the page, the user will see a stale month forever. Always derive the seed month from `new Date()` and use a `useMemo` so it doesn't re-compute on every render.

```tsx
const { year, month, label } = useMemo(() => {
  const d = new Date();
  const monthNames = ["January", "February", /* … */];
  return {
    year: d.getFullYear(),
    month: d.getMonth(),
    label: `${monthNames[d.getMonth()]}-${d.getFullYear()}`,
  };
}, []);
```

### Settings lost on new browser/profile

localStorage is per-origin per-browser. If the user switches browsers or clears site data, their settings reset to defaults. Acceptable for a personal dashboard; for multi-device sync, store on the server instead.

### Theme flicker on first load

If the accent color depends on localStorage, the page renders with the default accent for a frame before the client applies the saved one. Mitigation: set the CSS variable in an inline `<script>` in `<head>` that reads localStorage synchronously before paint. Only worth it if you have a strong accent-color UX requirement.

## When the user says "remove the sidebar, put nav in the header"

The cleanest translation is **not** to add a header — it's to **make the existing topbar the entire header**. Pattern:

1. **Delete `Sidebar.tsx`** (or whichever side-nav file you have). Remove its render from `app/layout.tsx`.
2. **Expand `Topbar.tsx`** to two rows:
   - **Row 1** = brand block + date/market status + account chip + accent picker
   - **Row 2** = horizontal tab nav (the only navigation)
3. **Make the topbar sticky** with `sticky top-0 z-40` and a backdrop-blur for legibility.
4. **Centralize nav config** in `lib/nav.ts` and drop the `sidebar` group — only `topbar` items remain.

Avoid leaving a sidebar component around "for future use" — dead code is a maintenance hazard. If you keep `SIDEBAR_QUICK` / `SIDEBAR_PROFILE` exports in nav.ts, the temptation to wire them back up later will resurface. Delete the exports.

**Verification standard:** after the swap, grep the codebase for any remaining sidebar import — there should be zero. Run a live page load and confirm the brand block + all tabs are visible in a single full-width header at the top of the viewport.

## Reference implementation

The Tradingx app at `/mnt/tb/1Apps/Tradingx` has:

- `lib/settings.ts` — the pub-sub store with `useSettings()` hook returning `hydrated`.
- `app/settings/page.tsx` — full settings UI with toggle/slider/select/range inputs, import/export, reset.
- `components/ThemeApplicator.tsx` — sets `<html data-accent={settings.accent}>` on settings change.
- `components/Topbar.tsx` — 2-row sticky header (brand+status row, tab nav row). The **only** navigation surface.
- `components/DemoAwareDashboardStats.tsx` — three-state demo/real/empty hero strip gated on `hydrated && checked`.
- `components/DemoAwareCalendar.tsx` — calendar wrapper that derives the displayed month from `new Date()` and renders only day numbers when demo is off.
- `components/DemoAwareRDistribution.tsx` — R-multiple chart that derives from real win/loss counts and renders empty when off.

The Settings → Display section shows the toggle working end-to-end: turn it off in `/settings`, navigate to `/`, and the hero strip switches from demo numbers to dashes, the calendar loses its `+500` / `-100` cell labels, and the R-distribution chart shows an empty state.

## Related patterns

- `references/nextjs-standalone-docker-pitfalls.md` — Dockerfile + standalone output pitfalls.
- `references/exchange-integration-pattern.md` — adapter pattern for authenticated third-party APIs.
- `references/vs-static-spa-library-site.md` — when to use this skill vs the static SPA variant.
- `references/css-variable-accent-theming.md` — full data-accent attribute pattern with palette tokens.
