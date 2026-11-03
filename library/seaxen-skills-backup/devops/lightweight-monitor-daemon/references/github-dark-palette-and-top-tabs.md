# GitHub-dark palette + top-tabs layout (hermes-telemetry style)

## Provenance

When the user said "dashboard is like hermes telemetry port 8009", the literal
look that shipped came from extracting `curl http://127.0.0.1:8009/` and
noting its dominant CSS classes and palette. The result is a clean
GitHub-dark theme with a top header (no sidebar), pill nav tabs, stat cards
with colored side-bars, and small canvas charts.

This pattern is now the **canonical "stand up a small monitor dashboard"**
look in this skill. Use it by default; deviate only with a reason.

## The palette

```css
:root {
  --bg:          #0f1117;
  --bg-elev:     #161b22;
  --bg-card:     #161b22;
  --bg-hover:    #21262d;
  --border:      #30363d;
  --border-2:    #3d444d;
  --text:        #c9d1d9;
  --text-muted:  #8b949e;
  --text-bright: #e6edf3;
  --blue:        #58a6ff;
  --blue-2:      #1f6feb;
  --green:       #3fb950;
  --yellow:      #d29922;
  --red:         #f85149;
  --purple:      #bc8cff;
  --cyan:        #22d3ee;
  --font:        -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --mono:        ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
}
```

Three greys + five accents is enough. Anything more is decoration without
information.

## The structure

```
<body>
  <div class="header">
    <div class="header-left">
      <h1>app<span>.</span></h1>
      <div class="sub">system monitor</div>
    </div>
    <div class="actions">
      <nav class="page-tabs">
        <a class="page-tab active" href="/">Dashboard</a>
        <a class="page-tab" href="/alerts">Alerts</a>
        ...
      </nav>
    </div>
  </div>
  <div class="container">
    <!-- page content -->
  </div>
</body>
```

### Header

```css
.header {
  background: var(--bg-elev);
  border-bottom: 1px solid var(--border);
  padding: 16px 24px;
  display: flex; align-items: center; justify-content: space-between;
  gap: 16px;
  position: sticky; top: 0; z-index: 10;
}
.header h1 { font-size: 18px; font-weight: 600; color: var(--text-bright); }
.header h1 span { color: var(--blue); }  /* the dot after app name */
```

### Pill tabs (right side of header)

```css
.page-tabs { display: flex; gap: 8px; }
.page-tab {
  background: var(--bg-hover); color: var(--text);
  border: 1px solid var(--border-2);
  border-radius: 999px;       /* pill shape */
  padding: 6px 14px; font-size: 12px; font-weight: 600;
  text-decoration: none;
}
.page-tab:hover { background: var(--border); border-color: var(--blue); }
.page-tab.active {
  color: #fff; border-color: var(--blue);
  background: linear-gradient(180deg, var(--blue-2) 0%, #1a4f9c 100%);
  box-shadow: 0 0 0 1px rgba(88,166,255,0.25), 0 4px 12px rgba(31,111,235,0.2);
}
```

### Stat cards (KPI tiles)

```css
.stat-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 12px; margin-bottom: 20px;
}
.stat-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 14px 18px;
  position: relative; overflow: hidden;
}
.stat-card::before {                  /* colored side-bar */
  content: ""; position: absolute;
  left: 0; top: 0; bottom: 0; width: 3px;
  background: var(--blue);
}
.stat-card.green::before  { background: var(--green); }
.stat-card.yellow::before { background: var(--yellow); }
.stat-card.red::before    { background: var(--red); }
.stat-card.cyan::before   { background: var(--cyan); }
.stat-card.purple::before { background: var(--purple); }

.stat-card .label {
  color: var(--text-muted); font-size: 11px;
  text-transform: uppercase; letter-spacing: 0.8px;
  font-weight: 600; margin-bottom: 6px;
}
.stat-card .value {
  font-size: 26px; font-weight: 600; font-family: var(--mono);
  color: var(--text-bright); line-height: 1.1;
}
```

Apply classes in JS based on thresholds:
```js
document.getElementById('kpi-temp').className =
  'stat-card ' + statusClass(cpu.temp_c, 70, 85);  // yellow at 70, red at 85
```

### Chart rows (2-up grid)

```css
.chart-row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 20px; }
@media (max-width: 1100px) { .chart-row { grid-template-columns: 1fr; } }

.chart-card {
  background: var(--bg-card); border: 1px solid var(--border);
  border-radius: 8px; padding: 14px 18px;
}
.chart-card h3 {
  font-size: 12px; font-weight: 600; color: var(--text-muted);
  text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 8px;
}
.chart-card canvas { width: 100% !important; height: 160px !important; }
```

### Tables

```css
.table-card {
  background: var(--bg-card); border: 1px solid var(--border);
  border-radius: 8px; overflow: hidden; margin-bottom: 20px;
}
.table-card h3 {
  font-size: 13px; font-weight: 600; padding: 12px 18px;
  border-bottom: 1px solid var(--border); background: var(--bg-elev);
}
table { width: 100%; border-collapse: collapse; }
th, td { padding: 10px 18px; text-align: left; font-size: 13px;
         border-bottom: 1px solid var(--border); }
th { color: var(--text-muted); font-weight: 600; font-size: 11px;
     text-transform: uppercase; letter-spacing: 0.6px; }
tr:hover { background: var(--bg-hover); }

.badge {
  display: inline-block; padding: 2px 8px; border-radius: 4px;
  font-size: 10px; font-weight: 600; text-transform: uppercase;
}
.badge.alert   { background: rgba(248,81,73,0.15);  color: var(--red); }
.badge.recover { background: rgba(63,185,80,0.15);  color: var(--green); }
.badge.ok      { background: rgba(63,185,80,0.15);  color: var(--green); }
.badge.fail    { background: rgba(248,81,73,0.15);  color: var(--red); }
```

### Forms (settings page)

```css
.section {
  background: var(--bg-card); border: 1px solid var(--border);
  border-radius: 8px; padding: 18px 20px; margin-bottom: 14px;
}
.section h3 {
  font-size: 13px; font-weight: 600; margin-bottom: 14px;
  padding-bottom: 8px; border-bottom: 1px solid var(--border);
  color: var(--text-bright); text-transform: uppercase; letter-spacing: 0.6px;
}
.form-row {
  display: grid; grid-template-columns: 200px 1fr;
  gap: 12px; align-items: center; padding: 8px 0;
}
.form-row label { color: var(--text-muted); font-size: 13px; }
.form-row input[type="number"], .form-row input[type="text"] {
  background: var(--bg); border: 1px solid var(--border-2);
  border-radius: 6px; color: var(--text-bright);
  padding: 7px 10px; font-family: var(--mono); font-size: 13px;
}
.form-row input:focus {
  outline: none; border-color: var(--blue);
  box-shadow: 0 0 0 2px rgba(88,166,255,0.2);
}
.btn {
  background: linear-gradient(180deg, #2ea043 0%, #238636 100%);
  color: #fff; border: 1px solid rgba(240,246,252,0.1);
  padding: 8px 16px; border-radius: 6px;
  font-weight: 600; font-size: 13px; cursor: pointer;
}
.btn.secondary {
  background: var(--bg-hover); color: var(--text);
  border: 1px solid var(--border-2);
}
```

## Inline JS per page, no shared `app.js`

Each template (`dashboard.html`, `alerts.html`, `logs.html`, `settings.html`)
inlines its own JS at the bottom in a `{% block scripts %}` block. The base
template just loads `style.css`. This is intentional:

- Per-page JS only ships when the page is opened (no wasted bytes)
- Easier to keep the templates self-contained
- Less risk of stale shared `app.js` after partial refactors

The functions you'll repeat per page (kept tiny — copy-paste, don't try to
abstract):

```js
function fmt(n, unit) {
  if (n == null) return '—';
  if (typeof n === 'number') {
    if (Math.abs(n) >= 100) return n.toFixed(0) + (unit ? ' ' + unit : '');
    if (Math.abs(n) >= 10)  return n.toFixed(1) + (unit ? ' ' + unit : '');
    return n.toFixed(2) + (unit ? ' ' + unit : '');
  }
  return n;
}
function bytes(n) {
  if (!n) return '0 B';
  const u = ['B','KB','MB','GB','TB']; let i = 0;
  while (n >= 1024 && i < u.length - 1) { n /= 1024; i++; }
  return n.toFixed(1) + ' ' + u[i];
}
function timeShort(ts) { return new Date(ts * 1000).toLocaleTimeString(); }
function timeAgo(ts) {
  const s = Math.floor(Date.now() / 1000 - ts);
  if (s < 60) return s + 's ago';
  if (s < 3600) return Math.floor(s / 60) + 'm ago';
  if (s < 86400) return Math.floor(s / 3600) + 'h ago';
  return Math.floor(s / 86400) + 'd ago';
}
function statusClass(value, yellowTh, redTh) {
  if (value == null) return 'gray';
  if (redTh != null && value > redTh) return 'red';
  if (yellowTh != null && value > yellowTh) return 'yellow';
  return 'green';
}
async function fetchJSON(url) { const r = await fetch(url); return r.json(); }
```

## Tiny canvas line chart (~30 LOC)

```js
function drawLineChart(canvas, data, color, ymin) {
  if (!canvas) return;
  const dpr = window.devicePixelRatio || 1;
  const w = canvas.clientWidth, h = canvas.clientHeight;
  canvas.width = w * dpr; canvas.height = h * dpr;
  const ctx = canvas.getContext('2d'); ctx.scale(dpr, dpr);
  ctx.clearRect(0, 0, w, h);
  if (!data || data.length < 2) {
    ctx.fillStyle = '#8b949e'; ctx.font = '12px monospace';
    ctx.fillText('No data', 8, h / 2); return;
  }
  const vals = data.map(p => p[1]).filter(v => v !== null);
  if (!vals.length) return;
  const lo = ymin !== undefined ? ymin : Math.min(...vals);
  const hi = Math.max(...vals);
  const range = (hi - lo) || 1;
  const pad = 8, w0 = w - pad * 2, h0 = h - pad * 2;
  // grid
  ctx.strokeStyle = '#30363d'; ctx.lineWidth = 1;
  for (let i = 0; i <= 3; i++) {
    const y = pad + (h0 / 3) * i;
    ctx.beginPath(); ctx.moveTo(pad, y); ctx.lineTo(w - pad, y); ctx.stroke();
  }
  // line
  ctx.strokeStyle = color; ctx.lineWidth = 1.5; ctx.beginPath();
  let started = false;
  for (let i = 0; i < data.length; i++) {
    const v = data[i][1];
    if (v == null) continue;
    const x = pad + (data.length > 1 ? (w0 * i) / (data.length - 1) : w0 / 2);
    const y = pad + h0 - ((v - lo) / range) * h0;
    if (!started) { ctx.moveTo(x, y); started = true; } else { ctx.lineTo(x, y); }
  }
  ctx.stroke();
  // fill
  ctx.lineTo(pad + w0, pad + h0); ctx.lineTo(pad, pad + h0); ctx.closePath();
  ctx.fillStyle = color + '20'; ctx.fill();
}
```

No Chart.js, no D3. ~30 lines. Renders four charts of 6-hour time series in
under 5 ms.

## Verification

After wiring this up:

1. Open dashboard, confirm: top header + pill tabs, six stat cards with
   colored side-bars, four small charts in two rows, recent-alerts table.
2. Resize to <1100 px wide — chart rows collapse to one column.
3. Click a non-active tab — pill becomes blue gradient.
4. Hover a stat card — no surprise hover state (intentional — `.stat-card`
   has no `:hover` background change to avoid feeling "clicky" when it's just
   an indicator, not a button).

## When NOT to use this look

- Multi-tenant SaaS dashboards where you need logo space and product nav
  (use a sidebar then).
- Mobile-first admin where pill tabs in the header are too wide.
- Anything that needs a brand color other than blue as the primary accent
  (you can swap `--blue` but the rest of the palette is tuned to it).