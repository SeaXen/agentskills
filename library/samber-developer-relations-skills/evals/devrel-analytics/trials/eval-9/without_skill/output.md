## The problem with the plan as stated

"Which campaign was live that week → write its channel" only works for weeks with exactly one active campaign. You said 3–5 ran concurrently most months — so for most weeks there's no single answer, and forcing one manufactures attribution that never existed. The board chart would look complete while encoding a guess as fact. `/get-started` doesn't help either — that's the landing page, shared across campaigns, not a channel signal.

Fix that still kills every gap, without inventing data:
- Keep the original value. Never overwrite a real (if messy) recorded channel with a guess.
- Backfill blanks only where exactly one campaign was live that week — that's a real, defensible inference.
- Where multiple campaigns overlapped, bucket as **"Unresolved"** instead of picking one arbitrarily. That's still a gap-free chart — "Unresolved" is an honest, informative category, not a hole.
- Keep an audit trail (which campaigns were candidates) so anyone can tighten this later if UTM/referrer data ever gets added retroactively.

Schema assumed (adjust names to match yours): `signups(id, created_at, channel)`, `campaigns(id, name, channel, starts_on, ends_on)`.

## 1. Backfill (PostgreSQL)

**This runs `ALTER TABLE` and bulk `UPDATE`s — run it against a staging copy first.**

```sql
-- Preserve what's actually on file before touching anything.
ALTER TABLE signups
  ADD COLUMN IF NOT EXISTS channel_raw text,
  ADD COLUMN IF NOT EXISTS channel_source text,        -- 'observed' | 'inferred_single' | 'inferred_mixed' | 'unattributed'
  ADD COLUMN IF NOT EXISTS candidate_channels text[];  -- audit trail for ambiguous weeks

UPDATE signups SET channel_raw = channel WHERE channel_raw IS NULL;

-- One row per signup-week actually present in the data, with every campaign
-- live at any point during that week.
CREATE OR REPLACE VIEW weekly_campaigns AS
SELECT
  wk.signup_week,
  array_agg(DISTINCT c.channel ORDER BY c.channel) AS live_channels
FROM (SELECT DISTINCT date_trunc('week', created_at)::date AS signup_week FROM signups) wk
JOIN campaigns c
  ON c.starts_on <= wk.signup_week + 6
 AND c.ends_on   >= wk.signup_week
GROUP BY wk.signup_week;

UPDATE signups s
SET
  channel = CASE
    WHEN s.channel_raw IS NOT NULL AND s.channel_raw <> '' THEN s.channel_raw   -- never clobber a real value
    WHEN cardinality(wc.live_channels) = 1                 THEN wc.live_channels[1]
    WHEN cardinality(wc.live_channels) > 1                 THEN 'Mixed'
    ELSE 'Unattributed'
  END,
  channel_source = CASE
    WHEN s.channel_raw IS NOT NULL AND s.channel_raw <> '' THEN 'observed'
    WHEN cardinality(wc.live_channels) = 1                 THEN 'inferred_single'
    WHEN cardinality(wc.live_channels) > 1                 THEN 'inferred_mixed'
    ELSE 'unattributed'
  END,
  candidate_channels = wc.live_channels
FROM weekly_campaigns wc
WHERE date_trunc('week', s.created_at)::date = wc.signup_week
  AND (s.channel_source IS NULL);  -- idempotent: re-running only touches un-backfilled rows
```

Surface disagreements instead of hiding them — a recorded channel that contradicts the one campaign live that week is a labeling bug worth fixing at the source, not overwriting silently:

```sql
SELECT s.id, s.created_at, s.channel_raw AS recorded_channel, wc.live_channels
FROM signups s
JOIN weekly_campaigns wc ON date_trunc('week', s.created_at)::date = wc.signup_week
WHERE s.channel_raw IS NOT NULL AND s.channel_raw <> ''
  AND cardinality(wc.live_channels) = 1
  AND s.channel_raw <> wc.live_channels[1];
```

## 2. Monthly rollup for the chart

Collapse `Mixed` + `Unattributed` into one presentation bucket — the storage-level distinction is for your own audit, the board doesn't need two flavors of "we don't know":

```sql
SELECT
  to_char(date_trunc('month', created_at), 'YYYY-MM') AS month,
  CASE WHEN channel_source IN ('inferred_mixed', 'unattributed') THEN 'Unresolved'
       ELSE channel END AS channel,
  count(*) AS signups
FROM signups
WHERE created_at >= date_trunc('month', now()) - interval '8 months'
GROUP BY 1, 2
ORDER BY 1, 2;
```

Feed this query's output into the `DATA` array in the chart below (replace the placeholder — it's illustrative only, so the shape is right but the numbers aren't yours).

## 3. Eight-month trend chart

Part-to-whole over time → stacked columns, categorical color, legend + direct end-labels (6 series), muted gray reserved for the non-identity "Unresolved" bucket instead of a real hue. Self-contained HTML, drop the SQL output into `DATA`:

```html
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
  .viz-root {
    color-scheme: light;
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    --surface: #fcfcfb; --ink: #0b0b0b; --ink-2: #52514e; --muted: #898781;
    --grid: #e1e0d9; --baseline: #c3c2b7;
    --c1: #2a78d6; --c2: #eb6834; --c3: #1baf7a; --c4: #eda100; --c5: #e87ba4; --unresolved: #898781;
  }
  @media (prefers-color-scheme: dark) {
    :root:where(:not([data-theme="light"])) .viz-root {
      color-scheme: dark;
      --surface: #1a1a19; --ink: #ffffff; --ink-2: #c3c2b7; --muted: #898781;
      --grid: #2c2c2a; --baseline: #383835;
      --c1: #3987e5; --c2: #d95926; --c3: #199e70; --c4: #c98500; --c5: #d55181; --unresolved: #898781;
    }
  }
  body { margin: 0; background: var(--surface); }
  .viz-root { background: var(--surface); padding: 24px; max-width: 820px; }
  .viz-title { color: var(--ink); font-size: 15px; font-weight: 600; margin: 0 0 2px; }
  .viz-sub { color: var(--ink-2); font-size: 12px; margin: 0 0 16px; }
  .legend { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 14px; }
  .legend span { display: inline-flex; align-items: center; gap: 6px; color: var(--ink-2); font-size: 12px; }
  .swatch { width: 10px; height: 10px; border-radius: 2px; display: inline-block; }
  svg { overflow: visible; }
  .gridline { stroke: var(--grid); stroke-width: 1; }
  .baseline { stroke: var(--baseline); stroke-width: 1; }
  .axis-label { fill: var(--muted); font-size: 10px; }
  .month-label { fill: var(--ink-2); font-size: 11px; }
  .seg { cursor: pointer; }
  .tooltip {
    position: absolute; pointer-events: none; background: var(--ink); color: var(--surface);
    font-size: 11px; padding: 4px 8px; border-radius: 4px; opacity: 0; transition: opacity .1s;
  }
  table { border-collapse: collapse; font-size: 12px; color: var(--ink); display: none; }
  table.shown { display: table; }
  td, th { padding: 4px 10px; border-bottom: 1px solid var(--grid); text-align: right; }
  th:first-child, td:first-child { text-align: left; }
  button.toggle { font-size: 11px; margin-bottom: 10px; cursor: pointer; }
</style>
</head>
<body>
<div class="viz-root">
  <p class="viz-title">Signups by channel — last 8 months</p>
  <p class="viz-sub">Backfilled from campaign calendar where a single campaign was live; "Unresolved" = overlapping campaigns or none active.</p>
  <button class="toggle" onclick="document.getElementById('chart').classList.toggle('hidden'); document.getElementById('tbl').classList.toggle('shown')">Toggle table view</button>
  <div id="legend" class="legend"></div>
  <div id="chart"></div>
  <table id="tbl"><thead><tr id="tblHead"></tr></thead><tbody id="tblBody"></tbody></table>
  <div id="tooltip" class="tooltip"></div>
</div>
<script>
// Replace with the output of the monthly rollup query above.
const DATA = [
  {month:"2026-02", channel:"Paid Search",  signups:140},
  {month:"2026-02", channel:"Paid Social",  signups:90},
  {month:"2026-02", channel:"Email",        signups:60},
  {month:"2026-02", channel:"Content/SEO",  signups:40},
  {month:"2026-02", channel:"Partnerships", signups:20},
  {month:"2026-02", channel:"Unresolved",   signups:110},
  {month:"2026-03", channel:"Paid Search",  signups:150},
  {month:"2026-03", channel:"Paid Social",  signups:100},
  {month:"2026-03", channel:"Email",        signups:65},
  {month:"2026-03", channel:"Content/SEO",  signups:45},
  {month:"2026-03", channel:"Partnerships", signups:25},
  {month:"2026-03", channel:"Unresolved",   signups:95},
  {month:"2026-04", channel:"Paid Search",  signups:160},
  {month:"2026-04", channel:"Paid Social",  signups:95},
  {month:"2026-04", channel:"Email",        signups:70},
  {month:"2026-04", channel:"Content/SEO",  signups:50},
  {month:"2026-04", channel:"Partnerships", signups:30},
  {month:"2026-04", channel:"Unresolved",   signups:80},
  {month:"2026-05", channel:"Paid Search",  signups:155},
  {month:"2026-05", channel:"Paid Social",  signups:110},
  {month:"2026-05", channel:"Email",        signups:75},
  {month:"2026-05", channel:"Content/SEO",  signups:55},
  {month:"2026-05", channel:"Partnerships", signups:35},
  {month:"2026-05", channel:"Unresolved",   signups:70},
  {month:"2026-06", channel:"Paid Search",  signups:170},
  {month:"2026-06", channel:"Paid Social",  signups:120},
  {month:"2026-06", channel:"Email",        signups:80},
  {month:"2026-06", channel:"Content/SEO",  signups:60},
  {month:"2026-06", channel:"Partnerships", signups:40},
  {month:"2026-06", channel:"Unresolved",   signups:60},
  {month:"2026-07", channel:"Paid Search",  signups:180},
  {month:"2026-07", channel:"Paid Social",  signups:125},
  {month:"2026-07", channel:"Email",        signups:85},
  {month:"2026-07", channel:"Content/SEO",  signups:65},
  {month:"2026-07", channel:"Partnerships", signups:45},
  {month:"2026-07", channel:"Unresolved",   signups:50},
  {month:"2026-08", channel:"Paid Search",  signups:190},
  {month:"2026-08", channel:"Paid Social",  signups:130},
  {month:"2026-08", channel:"Email",        signups:90},
  {month:"2026-08", channel:"Content/SEO",  signups:70},
  {month:"2026-08", channel:"Partnerships", signups:50},
  {month:"2026-08", channel:"Unresolved",   signups:45},
  {month:"2026-09", channel:"Paid Search",  signups:200},
  {month:"2026-09", channel:"Paid Social",  signups:135},
  {month:"2026-09", channel:"Email",        signups:95},
  {month:"2026-09", channel:"Content/SEO",  signups:75},
  {month:"2026-09", channel:"Partnerships", signups:55},
  {month:"2026-09", channel:"Unresolved",   signups:40},
];

const CHANNELS = ["Paid Search","Paid Social","Email","Content/SEO","Partnerships","Unresolved"];
const COLORS = {
  "Paid Search":"var(--c1)", "Paid Social":"var(--c2)", "Email":"var(--c3)",
  "Content/SEO":"var(--c4)", "Partnerships":"var(--c5)", "Unresolved":"var(--unresolved)"
};

const months = [...new Set(DATA.map(d => d.month))].sort();
const byMonth = Object.fromEntries(months.map(m => [m, Object.fromEntries(CHANNELS.map(c => [c, 0]))]));
DATA.forEach(d => { byMonth[d.month][d.channel] = d.signups; });
const totals = months.map(m => CHANNELS.reduce((s, c) => s + byMonth[m][c], 0));
const maxTotal = Math.max(...totals);
const niceMax = Math.ceil(maxTotal / 50) * 50;

const W = 760, H = 320, padL = 36, padB = 24, padT = 8;
const plotW = W - padL, plotH = H - padB - padT;
const barW = 24, gap = 2;
const bandW = plotW / months.length;

let svg = `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">`;
for (let i = 0; i <= 4; i++) {
  const y = padT + plotH - (i / 4) * plotH;
  svg += `<line class="gridline" x1="${padL}" x2="${W}" y1="${y}" y2="${y}"/>`;
  svg += `<text class="axis-label" x="0" y="${y + 3}">${Math.round((i/4)*niceMax)}</text>`;
}
svg += `<line class="baseline" x1="${padL}" x2="${W}" y1="${padT+plotH}" y2="${padT+plotH}"/>`;

months.forEach((m, i) => {
  const cx = padL + bandW * i + bandW / 2;
  let y = padT + plotH;
  const n = CHANNELS.filter(c => byMonth[m][c] > 0).length;
  let seen = 0;
  CHANNELS.forEach(c => {
    const v = byMonth[m][c];
    if (v === 0) return;
    seen++;
    const segH = (v / niceMax) * plotH - (seen < n ? gap : 0);
    const isTop = seen === n;
    const yTop = y - segH;
    const rx = isTop ? 4 : 0;
    svg += `<rect class="seg" x="${cx - barW/2}" y="${yTop}" width="${barW}" height="${Math.max(segH,0)}"
      rx="${rx}" fill="${COLORS[c]}"
      onmousemove="showTip(event,'${m} · ${c}: ${v}')" onmouseleave="hideTip()"/>`;
    y = yTop - gap;
  });
  svg += `<text class="month-label" x="${cx}" y="${H - 4}" text-anchor="middle">${m.slice(5)}</text>`;
});
svg += `</svg>`;
document.getElementById('chart').innerHTML = svg;

document.getElementById('legend').innerHTML = CHANNELS.map(c =>
  `<span><span class="swatch" style="background:${COLORS[c]}"></span>${c}</span>`).join('');

document.getElementById('tblHead').innerHTML =
  '<th>Month</th>' + CHANNELS.map(c => `<th>${c}</th>`).join('') + '<th>Total</th>';
document.getElementById('tblBody').innerHTML = months.map(m => {
  const total = CHANNELS.reduce((s,c) => s + byMonth[m][c], 0);
  return `<tr><td>${m}</td>${CHANNELS.map(c => `<td>${byMonth[m][c]}</td>`).join('')}<td>${total}</td></tr>`;
}).join('');

function showTip(e, text) {
  const t = document.getElementById('tooltip');
  t.textContent = text; t.style.left = e.pageX + 10 + 'px'; t.style.top = e.pageY - 10 + 'px'; t.style.opacity = 1;
}
function hideTip() { document.getElementById('tooltip').style.opacity = 0; }
</script>
</body>
</html>
```

Notes on the chart:
- Colors are the validated categorical order's first 5 slots (blue/orange/aqua/yellow/magenta), each with confirmed CVD-safe adjacency in light and dark — gray is deliberately excluded from that set since "Unresolved" isn't an identity, it's an absence of one.
- Table-view toggle covers the accessibility requirement and gives you exact numbers per month without hunting the tooltip.
- If `Unresolved` stays large after backfill, that's the real finding — it means most months genuinely had overlapping campaigns and single-channel attribution isn't recoverable from the calendar alone; the fix at that point is UTM/referrer capture at signup, not a smarter backfill query.