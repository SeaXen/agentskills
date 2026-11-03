# Summary stats — force one horizontal row

Use when the user wants **Skills** / **Journey** (or similar) KPI strips on **one line**, not wrapped 2×4 grids.

## AceRoute pattern (verified)

```css
#skillsSummary,#journeySummary{
  display:grid;
  gap:8px;
  margin-bottom:16px;
}
#skillsSummary{ grid-template-columns: repeat(8, minmax(0, 1fr)); }
#journeySummary{ grid-template-columns: repeat(5, minmax(0, 1fr)); }
#skillsSummary .mini-stat,#journeySummary .mini-stat{
  padding:10px 6px;
  text-align:center;
}
#skillsSummary .mini-stat .val,#journeySummary .mini-stat .val{
  font-size:1.05rem;
}
```

## HTML

Remove conflicting `skill-grid` class (3-column grid) from `#skillsSummary` / `#journeySummary`. Use `stats-inline-row` or id-only styling.

## Mobile

Prefer **one row + horizontal scroll**, not 2×2 wrap:

```css
#skillsSummary,#journeySummary{
  grid-auto-flow: column;
  grid-auto-columns: minmax(96px, 1fr);
  overflow-x: auto;
}
```

## Verify (browser console)

```javascript
(() => {
  const el = document.getElementById('skillsSummary');
  const cards = [...el.querySelectorAll('.mini-stat')];
  const tops = new Set(cards.map(c => c.getBoundingClientRect().top));
  return { count: cards.length, rows: tops.size };
})();
```

`rows` must be **1** for desktop layout.

## Distinct from Tools tab

Tools uses **two-row** layout (toolbar card + `#toolsSummary.tools-stats-row` with 6 stats). See `references/two-row-toolbar-and-stats-strip.md` — do not merge Skills/Journey stats into explorer toolbars.