# Telemetry Usage Trend SVG pattern

Use when a Hermes telemetry dashboard needs a screenshot-style usage trend card and Chart.js keeps producing bad geometry: clipped dates, compressed left-side line, unwanted legend boxes, x-axis labels in the wrong place, or poor edge-to-edge use.

## Trigger
- User asks for Daily Cost chart style, full-width line/area, visible bottom dates, professional tooltip.
- User repeatedly says the graph looks cut off, dates are not showing, or the chart is not edge-to-edge.
- Chart.js configuration changes are not visually matching the requested layout.

## Preferred structure
- Keep the existing metric header if the user asks to preserve it.
- Render chart body with custom SVG inside a fixed-height wrapper, not Chart.js.
- Use full-width point placement:
  - `x = pad.left + (i * plotWidth) / (n - 1)`
  - first point aligns with left plot edge
  - last point aligns with right plot edge
- Use a filled area path under the line, matching Daily Cost style.
- Use horizontal + vertical grid lines with low-opacity slate/gray.
- Render x-axis labels inside SVG at the bottom, not as a separate HTML row.
- Remove separate legend/footer if the user says the box/metric section below header is ugly.
- Tooltip should be a small black floating box with:
  - date title
  - small blue square marker
  - metric/value line

## Implementation notes
- `preserveAspectRatio="none"` makes the chart fill the available width/height.
- Use an SVG `viewBox` based on wrapper dimensions and compute all coordinates in that coordinate space.
- Default the tooltip to the latest point so the card has meaningful state without hover.
- Attach `mouseenter` / `mousemove` listeners to SVG points for tooltip updates.
- Escape labels/value text before injecting SVG/HTML.

## Verification
- Live browser visual check is required.
- Confirm:
  - line/area is visible
  - first and last points sit near chart edges
  - bottom dates are visible and not clipped
  - no unwanted legend box below the header
  - tooltip text is professional and readable
  - browser console has zero JS errors
- Structural checks alone are not enough; screenshot-level review is required.