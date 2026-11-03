# Hermes telemetry home metric chart: count semantics and verification

Use this when polishing or debugging the homepage SaaS-style metric trend card in `hermes-telemetry`.

## Durable lessons

### 1) Count semantics must match labels
- `Messages` on the homepage should mean **visible non-cron runs/messages**.
- `Runs` is the broader **visible run count**.
- Do not label a run-count card as `Requests` if the Request page is counting **LLM-call rows**; that creates a false mismatch even when queries are correct.

### 2) Home trend payload must honor visible-session filtering
If homepage totals are higher than the session/request tables, check filtering before touching UI.

For `api_daily_token_chart()` in Hermes telemetry, apply the same visible-session / soft-hide logic used by session-facing dashboard tables:
- filter LLM-call aggregates through joined `runs` visibility
- filter run aggregates through the same visible-session helper

This prevents the homepage card from counting hidden/deleted sessions while the detail pages exclude them.

### 3) Token multi-series needs scale separation
`Total` and `Cache read` are often an order of magnitude larger than `Input` and `Output`.

If all four lines share one y-axis, Input/Output become visually invisible.

Preferred pattern:
- left axis: `Total`, `Cache read`
- right axis: `Input`, `Output`
- add a short inline note explaining the split

### 4) Prefer Chart.js parity over brittle custom SVG for this card
When the goal is "make it like Daily Cost," reusing Chart.js is more robust than maintaining a one-off SVG renderer.

Why:
- native x-axis tick behavior
- native tooltip layout
- fewer right-edge clipping problems
- easier live introspection with `Chart.getChart(...)`

## Useful live probes

### Header cards actually rendered
```js
Array.from(document.querySelectorAll('.metric-trend-stat')).map(el => ({
  label: el.querySelector('.metric-trend-label')?.textContent?.trim(),
  value: el.querySelector('.metric-trend-value')?.textContent?.trim(),
  active: el.classList.contains('active')
}))
```

### Inspect live chart datasets / axes / x ticks
```js
(() => {
  const c = Chart.getChart('home-metric-trend-chart');
  return c ? {
    labels: c.data.labels,
    xTicks: c.scales.x.ticks.map(t => t.label),
    yTicks: c.scales.y.ticks.map(t => t.label),
    y1Ticks: c.scales.y1?.ticks?.map(t => t.label),
    datasets: c.data.datasets.map(d => ({
      label: d.label,
      axis: d.yAxisID,
      max: Math.max(...d.data),
      min: Math.min(...d.data),
    })),
  } : null;
})()
```

### Force-check tooltip content for the latest point
```js
(() => {
  const c = Chart.getChart('home-metric-trend-chart');
  if (!c) return null;
  const last = c.data.labels.length - 1;
  c.setActiveElements(c.data.datasets.map((_, i) => ({ datasetIndex: i, index: last })));
  c.tooltip.setActiveElements(
    c.data.datasets.map((_, i) => ({ datasetIndex: i, index: last })),
    { x: c.scales.x.getPixelForValue(last), y: c.scales.y.getPixelForValue(c.data.datasets[0].data[last]) }
  );
  c.update();
  return {
    title: c.tooltip.title,
    lines: c.tooltip.body.map(b => b.lines),
    opacity: c.tooltip.opacity,
  };
})()
```

### Compare API summary vs card sums
Use the daily chart API to sum the same fields the top cards display. Small drift is normal under auto-refresh; large persistent differences imply query/label mismatch.

## Verification checklist
- top-card labels match the actual metric semantics
- token card is first and active by default
- x-axis dates are visible
- token chart has four datasets
- axis split note matches the actual dataset-to-axis mapping
- home aggregate totals use visible-session filtering like the detail tables
- browser console shows zero JS errors
- screenshot/vision pass confirms no clipped tooltip/edge-label regression
