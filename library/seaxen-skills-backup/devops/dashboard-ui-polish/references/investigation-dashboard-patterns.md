# Investigation Dashboard Patterns — hermes-telemetry

Concrete patterns discovered during the hermes-telemetry dashboard build. These are reusable investigation/forensic UI patterns for telemetry dashboards.

---

## Dual-table pattern: Recent feed vs Investigation workspace

**Problem:** A dashboard needs both a quick recent-activity feed and a deep filtered investigation view.

**Solution:** Keep two tables on different pages/tabs:

| Table | Purpose | Behavior |
|-------|---------|----------|
| **Recent Sessions** (Home) | Broad feed for scanning | Click row → open detail drawer |
| **Session Investigation** (Breakdown) | Filtered forensic workspace | Driven by clicks from charts/tables; shows active filter chips; has always-visible search |

**Do not:**
- Leave both on the same page
- Treat them as duplicates — they serve different workflows

**Verification:**
- Recent table: unfiltered, limited rows, no search, no chips
- Investigation table: filter chips visible, search always visible, combines with chips, rows open drawer

---

## Filter chips with granular remove

**Pattern:** Each active drill-down dimension (provider, model, day, status, platform, cron, search) renders as an individual removable chip.

```html
.chip-list {
  display: flex; flex-wrap: wrap; gap: 8px; align-items: center;
}
.filter-chip {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 6px 10px; border-radius: 999px;
  background: #1f2937; border: 1px solid #364152;
  color: #e6edf3; font-size: 12px; font-weight: 600;
}
.chip-close {
  background: transparent; border: 0; color: #8b949e;
  cursor: pointer; font-size: 13px; line-height: 1; padding: 0;
}
.chip-close:hover { color: #e6edf3; }
```

```js
// State
let currentDrilldown = {}; // {provider, model, day, status, platform, cron_job_id, q}

// Render chips from current state
function renderFilterChips() {
  const defs = [
    ['provider', 'Provider'], ['model', 'Model'], ['day', 'Day'],
    ['status', 'Status'], ['platform', 'Platform'],
    ['cron_job_id', 'Cron'], ['q', 'Search'],
  ];
  return defs
    .filter(([k]) => currentDrilldown[k])
    .map(([k, label]) =>
      `<span class="filter-chip">${label}: ${currentDrilldown[k]}
        <button class="chip-close" onclick="removeFilter('${k}')">×</button>
      </span>`
    ).join('');
}

// Replace vs accumulate
function setDrilldown(filter) {          // REPLACE all
  currentDrilldown = { ...filter };
  loadAll();
}

function addDrilldown(filter) {          // ACCUMULATE
  currentDrilldown = { ...currentDrilldown, ...filter };
  loadAll();
}

function removeFilter(key) {
  const next = { ...currentDrilldown };
  delete next[key];
  currentDrilldown = next;
  loadAll();
}
```

**Key distinction:**
- `setDrilldown` = chart click, clicks from summary tables → fresh filter
- `addDrilldown` = clicks inside investigation table/search drawer → layer on

---

## Session drawer with navigable inline chips

**Pattern:** Detail drawer shows status, provider, model, platform as clickable inline buttons that:
1. Close the drawer
2. Add that filter to the investigation workspace
3. Switch to Breakdown tab

```html
<span class="inline-btn" onclick="closeDrawer(); addDrilldown({provider:'...'})">
  Provider Value
</span>
```

**Inside drawer sections:**
| Section | Clickable chips |
|---------|----------------|
| Run totals | status, provider, model, platform |
| Provider/model mix | provider, model (per row) |
| Recent LLM calls | provider, model (per call row) |

**Why:** Lets analysts jump from a single session's detail directly to "show me all sessions like this one" without manual filter assembly.

---

## Search inside investigation workspace

**Pattern:** Always-visible search box at top of investigation table that:
- Combines with existing filter chips (doesn't replace them)
- Submits on Enter + has Search/Clear buttons
- Shows precise empty-state reason

```js
function applySearch() {
  const q = searchInput.value.trim();
  if (q) addDrilldown({ ...currentDrilldown, q });
  else { /* clear search only */ }
}

function renderEmptyReason() {
  if (!rows.length) {
    if (onlySearch) return `No sessions match search “${q}”.`;
    if (hasFilters) return `No sessions match filters and search “${q}”.`;
    return 'No sessions available for this time range.';
  }
}
```

**Empty-state variants:**
| State | Message |
|-------|---------|
| Only search term, no hits | `No sessions match search “xyz”.` |
| Filters + search, no hits | `No sessions match the current filters and search “xyz”.` |
| Filters only, no hits | `No sessions match the current filters.` |
| No filters, no data | `No sessions available for this time range.` |

---

## Chart slice drill-down (Chart.js doughnut)

**Pattern:** Add `onClick` handler to doughnut chart to capture slice label and drill down.

```js
function drawDoughnutChart(canvasId, labels, data, colors, onSliceClick) {
  destroyChart(canvasId);
  charts[canvasId] = new Chart(ctx, {
    type: 'doughnut',
    data: { labels, datasets: [{ data, backgroundColor: colors, borderWidth: 0 }] },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      onClick: (_, elements, chart) => {
        if (!elements?.length || !onSliceClick) return;
        const idx = elements[0].index;
        onSliceClick(chart.data.labels[idx], idx);
      },
      plugins: { legend: { position: 'right', labels: { color: '#8b949e', font: { size: 11 }, padding: 12 } } }
    }
  });
}

// Usage:
drawDoughnutChart('chart-providers', providerNames, callCounts, colors,
  (label) => addDrilldown({ provider: label === '(unknown)' ? '—' : label })
);
```

---

## Custom SVG charts with segment-level drill-down

**Pattern:** For exact geometry (touching split bars), use custom SVG. Wire `onclick` on individual `<rect>` elements.

```js
svg += `<rect x="${leftX(i)}" y="${yy}" width="${barW}" height="${h}"
  fill="${color}" style="cursor:pointer"
  onclick='addDrilldown({day:${JSON.stringify(day)}})'
><title>${day} · ${label}: ${value}</title></rect>`;

// Model side (two-key filter):
svg += `<rect x="${rightX(i)}" y="${yy}" width="${barW}" height="${h}"
  fill="${modelColor}" style="cursor:pointer"
  onclick='addDrilldown({day:${JSON.stringify(day)}, model:${JSON.stringify(model)}})'
><title>${day} · Model: ${model}: ${value}</title></rect>`;
```

**Benefits over Chart.js:**
- Exact adjacent geometry (no gap between left/right same-day bars)
- Native `<title>` hover tooltips
- Per-segment onclick with arbitrary payload
- Full control over legend, axes, stacking

---

## Backend filter endpoints

**Pattern:** Single `/api/runs` endpoint accepting all filter dimensions:

```python
def api_runs(limit=50, window_hours=0, day=None, model=None,
             provider=None, platform=None, status=None,
             session_id=None, cron_job_id=None, q=None):
    where, params = _build_run_filters(window_hours, day, model, provider,
                                        platform, status, session_id,
                                        cron_job_id, q)
    rows = query(f"SELECT ... FROM runs WHERE {where} LIMIT ?", (*params, limit))
    total = query(f"SELECT COUNT(*) FROM runs WHERE {where}", params)
    return {"filters": {...}, "total_runs": total, "rows": rows}
```

**Search (q) implementation:**
```python
if q:
    like = f"%{q}%"
    clauses.append("("
        "session_id LIKE ? OR COALESCE(model,'') LIKE ? OR "
        "COALESCE(provider,'') LIKE ? OR COALESCE(cron_job_id,'') LIKE ? OR "
        "COALESCE(platform,'') LIKE ? OR COALESCE(status,'') LIKE ?"
    ")")
    params.extend([like]*6)
```

---

## Page tab navigation with conditional render

**Pattern:** Single HTML, SPA-style tabs, page title reflects active tab.

```html
<!-- Header -->
<div class="page-tabs">
  <button class="page-tab active" onclick="switchPage('home')">Home</button>
  <button class="page-tab" onclick="switchPage('breakdown')">Breakdown</button>
</div>
```

```js
function switchPage(page) {
  currentPage = page;
  $('#tab-home').classList.toggle('active', page === 'home');
  $('#tab-breakdown').classList.toggle('active', page === 'breakdown');
  loadAll(); // re-renders based on currentPage
}

// In loadAll():
let html = `<div class="page-title">${currentPage === 'home' ? 'Home' : 'Breakdown'}</div>`;
if (currentPage === 'home') {
  // stat cards, budgets, charts, cron table, recent sessions
} else {
  // token breakdown, provider table, cache efficiency, model table, daily table, SVG chart, investigation
}
```

**Verify:** Inactive page sections are absent from DOM, not just hidden below fold.

---

## Color palette for matching dashboard style

**Colors used in hermes-telemetry:**

| Purpose | Hex |
|---------|-----|
| Blue (primary, token in) | `#58a6ff` |
| Green (output, ok, cache write) | `#3fb950` |
| Yellow (cache read, warning) | `#d29922` |
| Red (reasoning, error, hard) | `#f85149` |
| Purple (model accent) | `#bc8cff` |
| Gray (other, muted) | `#8b949e` |
| Background card | `#161b22` |
| Border | `#30363d` |
| Input bg | `#21262d` |
| Text primary | `#c9d1d9` |
| Text muted | `#8b949e` |

**Model series palette (for daily combined chart):**
```js
const modelColors = ['#bc8cff', '#8b949e', '#58a6ff', '#3fb950', '#d29922', '#f85149'];
```

**Token series:**
```js
const tokenSeries = [
  { label: 'Input', color: '#58a6ff', key: 'tokens_in' },
  { label: 'Output', color: '#3fb950', key: 'tokens_out' },
  { label: 'Cache Read', color: '#d29922', key: 'cache_read_tokens' },
  { label: 'Reasoning', color: '#f85149', key: 'reasoning_tokens' },
];
```

---

## Verification checklist for investigation dashboards

After any change, verify in live browser:

- [ ] Chart click → adds chip, switches to Breakdown, filters investigation table
- [ ] Table row click (provider/model/day) → adds chip, filters investigation
- [ ] Investigation table row click → opens drawer
- [ ] Drawer inline chip click → closes drawer, adds to chips, switches to Breakdown
- [ ] Search box → combines with existing chips, shows correct empty reason
- [ ] Chip × button → removes only that filter, others persist
- [ ] Clear filters button → removes all chips, resets table
- [ ] Clear search button → clears search chip only
- [ ] Page tabs → correct sections render per page, inactive sections absent from DOM
- [ ] SVG chart segments → onclick works, hover title shows day/label/value
- [ ] Provider doughnut slice click → chip added, investigation filtered
- [ ] Recent Sessions / Cron Jobs / Provider table → drill-down clicks work
- [ ] No JS errors in console

---

## Files referenced from this session

- `dashboard/index.html` — full implementation
- `dashboard/serve.py` — backend `/api/runs` with q, cron_job_id, all filters