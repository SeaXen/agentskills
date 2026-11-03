# Skills & Journey summary stats — one row

## User signal

"make skill and journey page stat are 1 line" — they reject 2-row wraps from `repeat(4)` on 8 Skills cards or `skill-grid` (3-col bleed).

## CSS

```css
#skillsSummary,#journeySummary{
  display:grid;
  gap:8px;
  margin-bottom:16px;
  align-items:stretch;
}
#skillsSummary{ grid-template-columns:repeat(8,minmax(0,1fr)); }
#journeySummary{ grid-template-columns:repeat(5,minmax(0,1fr)); }
#skillsSummary .mini-stat,#journeySummary .mini-stat{
  padding:10px 6px;
  text-align:center;
}
#skillsSummary .mini-stat .val,#journeySummary .mini-stat .val{
  font-size:1.05rem;
  font-weight:700;
}
#skillsSummary .mini-stat .label,#journeySummary .mini-stat .label{
  font-size:10px;
}
```

Remove `class="skill-grid"` from `#skillsSummary` / `#journeySummary` — `.skill-grid` forces 3 columns.

## Mobile

Horizontal scroll one row (not 2×2 grid):

```css
#skillsSummary,#journeySummary{
  grid-auto-flow:column;
  grid-auto-columns:minmax(96px,1fr);
  overflow-x:auto;
}
```

## Verify (browser console)

```javascript
(() => {
  var el = document.getElementById('skillsSummary');
  var st = getComputedStyle(el);
  return {
    cols: st.gridTemplateColumns,
    height: el.getBoundingClientRect().height,
    cards: el.querySelectorAll('.mini-stat').length
  };
})();
```

One row ≈ single `rowH` ~59px; `cols` should list 8 equal tracks on desktop.

## Git

AceRoute `aa2b42a` — `style: Skills and Journey summary stats on one row`.