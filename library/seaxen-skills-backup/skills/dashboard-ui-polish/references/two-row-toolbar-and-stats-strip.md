# Two-row toolbar + inline stats strip

Class-level pattern for compact dashboard tabs (AceRoute Tools, similar operator pages).

## DOM shape

```html
<div class="card toolbar-card tools-bar-card mb-12">
  <div class="tools-bar-line">
    <h2>🧰 Hermes Tools</h2>
    <span class="tools-bar-sync" id="toolsSyncMeta">—</span>
    <div class="tools-bar-actions"><!-- window select, sync, clear --></div>
    <div class="results-chip-row tools-bar-chips" id="toolsActiveChips"></div>
  </div>
</div>

<div id="toolsSummary" class="tools-stats-row mb-16">
  <!-- six miniStatCard() children -->
</div>
```

## CSS essentials

- Toolbar card: suppress default `h2::after` underline on bar titles; `padding:10px 12px`.
- Bar line: `display:flex; align-items:center; gap:10px`; actions `margin-left:auto`.
- Stats row: `#toolsSummary.tools-stats-row { grid-template-columns: repeat(6, minmax(0,1fr)); gap:10px }`.
- Mobile: stats `repeat(3,1fr)`; bar wraps — still **two blocks**, not re-merge.

## Copy to drop

- Placeholder sync paragraph in HTML (`Synced from Hermes state.db → aceroute.db`).
- `toolsResultsMeta` duplicate summary under the bar.
- Long button labels when icons suffice (`↻ Sync now` → `↻` with `title`).

## JS

```javascript
$('toolsSyncMeta').textContent = sync.hermes_state_exists === false
  ? 'no state.db'
  : ('sync ' + (sync.last_sync_at ? fmtShort(sync.last_sync_at) : 'pending'));
```

Do not set a long results-meta string if stat cards already cover sessions/tool calls/tokens.

## Verification (browser console)

- `document.querySelector('.tools-bar-card')?.nextElementSibling?.id === 'toolsSummary'`
- Six `.mini-stat` elements share one `getBoundingClientRect().top` (one row).
- `!document.getElementById('toolsResultsMeta')` when removed intentionally.

## Filter chips in the bar

Render with `<span class="results-chip">` inside `.results-chip-row` (`gap:6px`). Use `chips.join('')`, not `badge()` + `join(' ')`.

## Anti-pattern

User asked for stats on a **separate line** and **🧰 Hermes Tools** as a **one-line card** — not one merged hero. Revert if you combined them.

Skills/Journey summary stats: one horizontal row (`#skillsSummary` 8 cols, `#journeySummary` 5 cols) — see `references/skills-journey-stats-one-row.md`.

**Sessions tab:** one-line bar + eight-col stats — `references/sessions-one-line-bar-and-stats.md`.

## Repo

AceRoute: `/mnt/tb/1Apps/AceRoute` — `:8866`, commits `04d5818`, `5264311`. Bump `dashboard.js?v=` after JS edits (see `dashboard-ui-operations` → `references/aceroute-hermes-tools-analytics.md`).