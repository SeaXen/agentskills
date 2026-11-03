# AceRoute Skills page — legibility and chart-action pass

Use when the Skills explorer already has analytics panels but still feels hard to scan or too tall.

## What changed in this pass

The user did not ask for a brand-new panel here. They wanted the existing page to feel cleaner and more operational.

High-value upgrades that landed:
- sticky header on the main `Skills` table
- compact quick-health maintenance chips under the result-count line
- constrained `Skill Details` card with internal scrolling
- clickable `Category Usage` bars that set the category filter

## UI pattern

### 1. Quick-health chips under results meta
Place this directly below the line like:
- `35 / 187 skills • 31 used • 2 stale • 0 pinned`

Good chips:
- `no refs`
- `no tags`
- `no summary`
- `unused`

These are summary counts, not decorative badges. The user should be able to scan maintenance debt before reading the table.

## 2. Sticky table header
For long scrolling tables, make the header sticky inside the panel:

```css
#page-skills #skillsTable thead th {
  position: sticky;
  top: 0;
  z-index: 2;
  background: rgba(7,12,20,.98);
  box-shadow: 0 1px 0 rgba(255,255,255,.04);
}
```

This matters because the Skills table is one of the tallest panes on the page.

## 3. Constrain Skill Details
Do not let `Skill Details` become a giant trailing wall.

Working pattern:
- card gets a bounded height / min-height
- `#skillHighlights` gets `max-height` and `overflow:auto`

Result: the page stays visually balanced and the user can still scan many skill cards.

## 4. Treat charts as filters
If the page already has filter state, charts should participate in it.

For `Category Usage`, clicking a bar should set the category dropdown and re-render:

```js
onClick: function(evt, elements, chart) {
  var point = elements && elements[0];
  if (!point) return;
  var label = chart.data.labels[point.index];
  if (label) setSkillCategoryFilter(label);
}
```

This turned the chart from passive decoration into a real explorer control.

## Verification checklist

Use live DOM checks:
- quick-health chips render with 4 counts
- table header computed style is `position: sticky`
- detail card height is bounded and `#skillHighlights` scrolls internally
- clicking a Category Usage bar changes `#skillsCategoryFilter`
- result meta updates after the chart click

## Important pitfall

Do not fake quick-health filtering with loose text search like `refs`.
That is not a real predicate and it will drift.
If you later make the quick-health chips clickable, wire them to structured filters or dedicated predicates, not a search hack.
