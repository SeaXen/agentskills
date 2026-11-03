# AceRoute Search analytics — empty-state polish

Use when a dashboard analytics page has sections that are technically correct but visually broken when data is absent.

## What changed (latest pass)
- Document title: `AceRoute — Search`; `switchPage()` sets `document.title` per tab (`Search` / `Skills` / `Journey` / `Tools`).
- **Web Extract** is a **one-line head**, not a six-card stats grid:
  - `#extractInlineMeta`: `N extracts • X% ok • Y urls • latency • backend`
  - Optional **Log** button toggles `#extractBody` table; hide body when no rows unless user opens log.
  - One-line orange notice if extract backend not configured (no tall warning box).
- Hermes debug cards use `analytics-card` + `analytics-section-body` + `setAnalyticsCompact(sectionId, headMetaId, msg, true)` so empty sections collapse to **title + inline meta** (no dead chart/table blocks).
- Section IDs: `section-extract`, `section-hermes-activity`, `section-content-size`, `section-domain`, `section-ssrf`, `section-truncation`, `section-tool-timeline`.
- CSS: `.analytics-card.is-empty-compact .analytics-section-body { display:none }`.
- Filter chips: use `.results-chip` inside `.results-chip-row` with `gap:6px` (not `badge()` mashed with `join(' ')`).

## Earlier pass (still valid)
- Nav label `Search` (not `Analytics`).
- `summaryStatCard()` omit empty `sub` lines.
- `extract-empty-row` for table fallback.
- Hide chart wrappers on zero data when section is not in compact mode.

## Why this mattered
Empty charts and stacked stat cards created large dead blocks. User also wanted extract metrics in **one line** like the Tools toolbar, not another mini-dashboard inside the card.

## Practical pattern
1. **One-line metric strip** for secondary analytics (extract): flex head row + monospace meta; defer table to toggle or compact body.
2. **Compact empty analytics**: `is-empty-compact` hides `.analytics-section-body`; put explanation in `.analytics-inline-meta` next to `h2`.
3. Bump `dashboard.js?v=N` after JS changes (immutable cache on static JS).

## Verification cues
- `document.title` → `AceRoute — Search` on Search tab.
- `#extractInlineMeta` is one line; no `#extractStats` grid.
- Empty debug sections: `is-empty-compact` + head meta only.
- Skills chips: separate `.results-chip` elements with gap.

## Good user-facing answer
Distinguish **sparse but acceptable** (compact layout, clear one-line empty meta) vs **visually broken** (merged hero, giant blank chart boxes, duplicate summary prose).