# CSS variable accent theming via `data-accent` attribute

Pattern for per-user accent colors in self-hosted dashboards. The user picks an accent (green/amber/blue/rose) in Settings and the entire app recolors instantly — no Zustand, no React Context, no server round-trip.

## The pattern

1. Define accent tokens in `:root` and per-accent selectors in `globals.css`.
2. Expose a `data-accent` attribute on `<html>` and use CSS selectors `:root[data-accent="…"]` to flip the variables.
3. Mount a small `ThemeApplicator` client component in the root layout that sets the attribute based on `useSettings().settings.accent`.

## Why use `data-accent` instead of `style.setProperty` or Tailwind dark mode

| Approach | Pros | Cons |
|----------|------|------|
| `document.documentElement.setAttribute("data-accent", "amber")` + CSS variables | One DOM write, works without JS, inspectable in DevTools, composes with Tailwind, no `useEffect` per variable | Requires CSS variable discipline |
| `style.setProperty("--accent", "#f59e0b")` per color | Direct | Multiple writes, easy to forget, harder to debug |
| `class="dark"` Tailwind mode | Idiomatic Tailwind | Only two states (dark/light), not 4 accents; needs Tailwind dark variant everywhere |
| Zustand/Context for accent | Familiar | Overkill for one attribute, requires Provider wrapping, hydration cost |

`data-accent` wins because it's one attribute that drives the entire app's accent system via CSS variables, and you can flip it manually in DevTools to verify the cascade works.

## Implementation

### 1. Tokens in `app/globals.css`

```css
@layer base {
  :root {
    --accent-1: #22c55e;        /* main */
    --accent-1-deep: #16a34a;   /* hover/border */
    --accent-1-dim: #0d3a23;    /* background tint */
    --accent-1-soft: #22c55e33; /* ~20% alpha for soft backgrounds */
  }
  :root[data-accent="amber"] {
    --accent-1: #f59e0b;
    --accent-1-deep: #d97706;
    --accent-1-dim: #3a2a08;
    --accent-1-soft: #f59e0b33;
  }
  :root[data-accent="blue"] {
    --accent-1: #3b82f6;
    --accent-1-deep: #2563eb;
    --accent-1-dim: #0d2740;
    --accent-1-soft: #3b82f633;
  }
  :root[data-accent="rose"] {
    --accent-1: #f43f5e;
    --accent-1-deep: #e11d48;
    --accent-1-dim: #3a0d18;
    --accent-1-soft: #f43f5e33;
  }
}

@layer components {
  .accent-text  { color: var(--accent-1); }
  .accent-bg    { background-color: var(--accent-1); }
  .accent-bg-dim{ background-color: var(--accent-1-dim); color: var(--accent-1); }
  .accent-border{ border-color: var(--accent-1); }
}
```

Tailwind tokens (`text-accent-green`, `bg-accent-red`, etc.) **stay as static colors** — keep charts, sparklines, and KPI deltas in their semantic green/red. The dynamic `accent-*` utilities are for **chrome** (active tab border, primary buttons, focus rings, hover borders) that should follow the user's preference.

### 2. `ThemeApplicator` component

```tsx
// components/ThemeApplicator.tsx
"use client";
import { useEffect } from "react";
import { useSettings } from "@/lib/settings";

export function ThemeApplicator() {
  const { settings, hydrated } = useSettings();
  useEffect(() => {
    if (!hydrated) return;
    if (typeof document === "undefined") return;
    document.documentElement.setAttribute("data-accent", settings.accent);
  }, [hydrated, settings.accent]);
  return null;
}
```

The component renders nothing. It only sets the attribute as a side effect.

### 3. Mount in `app/layout.tsx`

```tsx
import { ThemeApplicator } from "@/components/ThemeApplicator";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-bg text-fg">
        <ThemeApplicator />
        <div className="flex min-h-screen flex-col">
          <Topbar />
          <main>{children}</main>
        </div>
      </body>
    </html>
  );
}
```

Mount it once at the body level so it never unmounts.

### 4. Settings UI — accent picker

```tsx
// In app/settings/page.tsx
const { settings, setSettings } = useSettings();
const accents = [
  { id: "green", color: "bg-emerald-500" },
  { id: "amber", color: "bg-amber-500" },
  { id: "blue",  color: "bg-blue-500" },
  { id: "rose",  color: "bg-rose-500" },
] as const;

return (
  <div>
    <span className="text-fg-dim">Accent color</span>
    <div className="flex items-center gap-1.5">
      {accents.map(a => (
        <button
          key={a.id}
          aria-label={`Accent ${a.id}`}
          onClick={() => setSettings({ accent: a.id })}
          className={
            "w-4 h-4 rounded-full " + a.color +
            (settings.accent === a.id ? " ring-2 ring-fg scale-110" : " opacity-50 hover:opacity-90")
          }
        />
      ))}
    </div>
  </div>
);
```

## Verification

```bash
# After clicking each accent swatch, the live HTML attribute should change:
curl -s http://localhost:8799/ | grep -o 'data-accent="[^"]*"'
# "data-accent=\"green\"" (default)

# In a real browser, verify the swap:
browser_console(expression='document.documentElement.getAttribute("data-accent")')
# → "green" / "amber" / "blue" / "rose" depending on user choice

# Verify computed styles actually use the variable:
browser_console(expression='getComputedStyle(document.querySelector(".accent-text")).color')
# green  → "rgb(34, 197, 94)"
# amber  → "rgb(245, 158, 11)"
# blue   → "rgb(59, 130, 246)"
# rose   → "rgb(244, 63, 94)"
```

## Pitfalls

### Setting `data-accent` during SSR with a non-default value

The `ThemeApplicator` runs in `useEffect`, so SSR uses the default `:root` (green) variables. If the user's saved accent is "rose" and they hit refresh, they see one frame of green before the attribute flips. Acceptable for most cases. If it's not, write a small inline script in `<head>` that reads localStorage synchronously before paint:

```html
<script>
  try {
    const raw = localStorage.getItem("myapp:settings:v1");
    if (raw) {
      const accent = JSON.parse(raw).accent;
      if (accent) document.documentElement.setAttribute("data-accent", accent);
    }
  } catch {}
</script>
```

### Multiple ThemeApplicator instances

If you accidentally mount `ThemeApplicator` in both the layout and a sub-component, both will race to set the attribute. Mount it exactly once — in the root layout.

### Re-applying the same attribute does nothing

`element.setAttribute("data-accent", x)` is a no-op if `x` equals the current value. If you find that switching accents doesn't work, the issue is upstream — usually the `useEffect` deps array missing `settings.accent` (a stale closure). Verify with browser devtools that the effect actually fires on accent change.

### Tailwind config tokens override CSS variables

If you set `accent: { green: "#22c55e" }` in `tailwind.config.ts`, classes like `text-accent-green` will use the static color, not the variable. That's intentional for charts/KPIs that must not rebrand. Reserve the `accent-*` (with hyphen, no color name) utilities for chrome that should follow the user's accent. Pick a different class prefix if you need to disambiguate.

## When NOT to use this pattern

- You only have 2 states (light/dark). Tailwind's `class="dark"` is more idiomatic.
- The user can't change the accent (fixed brand color). Just use the static Tailwind tokens.
- You need per-section accent variation. CSS variables are global; you'd need scoped custom properties.
