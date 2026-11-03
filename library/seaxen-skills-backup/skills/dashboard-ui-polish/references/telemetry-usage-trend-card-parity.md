# Telemetry Usage Trend card parity notes

Use this when polishing a Hermes telemetry dashboard card that combines a metric header row with a Chart.js line/area plot.

## What went wrong in the session
- Trying to manually place date labels outside Chart.js made the chart look unprofessional: dates appeared disconnected or visually "in the middle" of the chart/card.
- Hiding the native x-axis and adding a separate footer/date row fought the user's reference target.
- A custom footer legend/value row looked less professional when the user explicitly wanted parity with the existing Daily Cost chart.
- `offset: true` made the line not feel edge-to-edge; the user wanted the line to span the full chart width like Daily Cost.

## Preferred fix pattern
1. Keep the metric header requested by the user, but make the plot body follow the existing production chart style.
2. Use the same Chart.js conventions as the good existing chart:
   - native bottom x-axis labels, not a custom date row
   - centered legend above plot
   - area fill under the line when the reference chart has fill
   - tooltip with date title + colored square + metric/value row
   - faint grid lines inside the plot
3. For full-width/edge-to-edge line placement on categorical dates:
   - use `offset: false`
   - keep native x ticks visible
   - verify first and last point x positions are close to chartArea left/right
4. Use full date labels (`YYYY-MM-DD`) when matching Daily Cost exactly; use short labels only when the reference screenshot uses short labels.
5. Do not add duplicate bottom annotations (`DATE`, separate date rows, custom value rows) unless explicitly requested.

## Verification probes
In the browser console after rendering:
```js
const chart = window.Chart.getChart(document.getElementById('home-metric-trend-chart'));
({
  labels: chart.data.labels,
  fill: chart.data.datasets[0].fill,
  legend: chart.options.plugins.legend.display,
  offset: chart.scales.x.options.offset,
  points: chart.getDatasetMeta(0).data.map(p => Math.round(p.x)),
  chartArea: chart.chartArea,
});
```

Expected for Daily Cost-style parity:
- `fill === true`
- `legend === true`
- `offset === false`
- labels are visible on the native x-axis
- first/last point positions align near chartArea left/right
- browser console has zero JS errors
