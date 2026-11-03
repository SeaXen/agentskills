# Paired bar chart geometry: exact-touch pattern

Use this when the user wants a **single chart** where each day is shown as **one visual bar split into two vertical sections**:
- left section = token breakdown stack
- right section = model breakdown stack
- the two same-day sections must **touch edge-to-edge with no visible gap**

## Do not trust chart-library defaults
If a library like Chart.js keeps inserting category/group gaps, `barPercentage` / `categoryPercentage` tweaks may still fail to produce a true no-gap result.

Signal that the default path is wrong:
- user says the two bars still look separate
- screenshot shows obvious dead space between same-day left/right sections
- grouped-bar math becomes harder than the visual requirement

## Preferred fallback
Render the chart as **custom SVG** inside the dashboard card when exact geometry matters more than library convenience.

Why SVG worked better here:
- exact x/y/width control for both sections
- true no-gap adjacency by setting:
  - left rect `x = center - barWidth`
  - right rect `x = center`
- stacked sections are trivial with cumulative heights
- legend can be rendered as simple HTML above the SVG

## Rendering pattern
1. Build a full-width card host (`div.svg-chart-host`).
2. Compute per-day totals for:
   - token stack: input, output, cache read, reasoning
   - model stack: top models + optional Other
3. Compute chart geometry manually:
   - `groupW = plotWidth / dayCount`
   - `barW = chosen fixed width`
   - `leftX(i) = plotLeft + groupW*i + groupW/2 - barW`
   - `rightX(i) = plotLeft + groupW*i + groupW/2`
4. Draw token rects stacked at `leftX(i)`.
5. Draw model rects stacked at `rightX(i)`.
6. Render a single date label centered under the paired shape.
7. Verify visually that left/right touch with zero gap.

## Important implementation detail
When the user also asks for the chart to be **full width**, keep the SVG responsive via:
- fixed viewBox
- width 100%
- explicit host height

## Related UI lesson from this session
When the user asks for table support around the chart (for example adding a `Cost` column to Daily Token Usage and Model Token Usage), implement the table change explicitly. Do not treat the chart enhancement as covering that request.

## Verification checklist
- exactly one chart, not two
- card spans full dashboard width
- same-day left/right sections touch
- date labels remain readable
- legend still identifies token colors and model colors
- browser screenshot confirms the gap is actually gone
