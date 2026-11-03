# Reference theme parity + layout-mode pattern

Use when a user wants an app to visually match a reference dashboard/site, especially after screenshot-driven complaints like "still using previous theme", "looks dull", "dropdown not match", or "light mode still wrong".

## Core rule
Do not guess the target palette from memory or from a single screenshot. Inspect the live reference site and the user screenshots together.

## What to compare first
- page background vs card background separation
- text hierarchy: primary / secondary / muted
- border visibility
- shadow depth / glass blur
- accent usage density (accent everywhere vs accent as highlight)
- nav shape: top header vs left sidebar
- dropdown/menu chrome

## Recurrent root causes when theme switching is only partially working
1. Hardcoded Tailwind palette classes remain in old components (`slate`, `zinc`, etc.), so the new theme only affects newer surfaces.
2. Custom theme utility opacity variants are missing (`bg-bg/95`, `bg-bg-alt/70`, `border-bg-line/60`, etc.), so components silently fall back to wrong defaults.
3. Hero panels or gradients use utility combinations unsupported by the current theme layer, causing flat black/gray blocks instead of the intended surface treatment.
4. Public HTML + token-protected `/api/*` pages may look "broken" because widgets fail with `Unauthorized`; fix auth parity before treating it as a pure design issue.

## Durable fix pattern
- Add/expand CSS variable themes at the global layer.
- Add compatibility overrides for legacy hardcoded palette classes so old pages switch correctly before every file is fully refactored.
- Define opacity variants for themed utility classes, not just the base classes.
- Style shared primitives (`surface`, `menu-flyout`, inputs, chips, header) before page-by-page polish.
- For token-protected APIs in browser UIs, inject auth early and patch browser fetch globally for `/api/*` if many legacy components still call raw `fetch`.

## Verification pattern
- Force the target theme in browser storage / DOM and inspect computed styles.
- Verify both the requested custom theme and light mode after compatibility changes.
- Check one page with shared widgets and one legacy page that historically used hardcoded `slate/zinc` classes.
- If the user asks for layout parity too, verify both nav modes (topbar and sidebar) live.

## Useful outcomes from this session
- TraderWaves-style polish required moving from "blue everywhere" to dark neutral surfaces plus accent blue.
- Admin-template-inspired polish required a separate dark theme and a nav layout switch, not mutation of the existing theme.
- A sidebar/topbar layout toggle can be added cleanly by rendering the same nav config in two shells instead of duplicating route definitions.
