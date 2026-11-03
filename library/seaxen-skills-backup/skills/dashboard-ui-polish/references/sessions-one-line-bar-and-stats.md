# Sessions / Requests / Messages / Models — one-line bar + one-line stats (AceRoute)

## User signals

- "make … card **1 line** and beautiful"
- "stats in **1 line** like other page"
- "nothing change even after refresh" → deploy verification below (not a CSS-only fix)

## Layout (two sibling blocks, like Tools)

1. **Bar card** — one horizontal row only (~36px content height + padding)
2. **Stats row** — eight mini-stat cards on one grid row (separate element below the bar)

Do **not** merge bar + stats into one hero card.

## Shared selectors

Apply the same chrome to `#page-sessions`, `#page-requests`, `#page-messages`, `#page-models`:

- `.sessions-bar-card` / `.sessions-bar-row` (`flex-wrap: nowrap`)
- `#sessionsSummary`, `#requestsSummary`, `#messagesSummary`, `#modelsSummary` — `repeat(8, 1fr)` with `!important` if legacy CSS fights you

## Bar card DOM (Sessions example)

```html
<div class="card sessions-bar-card">
  <div class="sessions-bar-row">
    <h2>💬 Hermes Sessions</h2>
    <span class="sessions-bar-meta" id="sessionsMetaNote">…</span>
    <div class="sessions-bar-actions"><!-- window, search --></div>
    <div class="results-chip-row sessions-bar-chips" id="sessionsSourceChips"></div>
  </div>
</div>
```

**CSS keys**

- `.sessions-bar-chips { flex: 1 1 120px; min-width: 0; overflow-x: auto; flex-wrap: nowrap }`
- Chips in **same row** as title/controls — not a second row with `border-top`
- Models tab: often no chip row — only window select in `.sessions-bar-actions` (`margin-left: auto`)

## Stats row

Short labels (`Tools`, `In`, `Out`, `Total`, `Cost`). Values `1.25rem`, uppercase 10px labels.

Mobile: horizontal-scroll stats for all four summary ids in `mobile.css`.

## Meta line

Keep `#*MetaNote` **short** — long copy wraps the bar.

## Deploy verification (mandatory when user says UI unchanged)

```bash
curl -s 'http://127.0.0.1:8866/' | tail -3
curl -s 'http://127.0.0.1:8866/' | grep -E 'page-models|dashboard.js\?v='
```

Stale container serves old `dashboard.js?v=22` while repo has `v=27+`. Fix: `docker compose up -d --build --force-recreate` and/or `./static:/app/static:ro` in compose. Bump `?v=N` after JS edits.

## Repo

`/mnt/tb/1Apps/AceRoute` — `b35482c` (static mount), `0beb3a9` (Models).