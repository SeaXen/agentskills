# Hermes Telemetry dashboard — token panels and combined daily chart

Use this when extending the local `hermes-telemetry` dashboard on Dr. Sagar's host.

## Local runtime surface
- Dashboard URL used for live verification: `http://127.0.0.1:8009`
- Service name: `hermes-telemetry-dashboard`
- Main files:
  - `~/.hermes/plugins/hermes-telemetry/dashboard/serve.py`
  - `~/.hermes/plugins/hermes-telemetry/dashboard/index.html`

## Implemented UI shape
Below `Recent Sessions`:
1. `Model Token Usage` table
   - Columns: Model / Calls / In / Out / Cache Read / Cache Write / Reasoning / Total / Cost
2. `Daily Token Usage` table
   - Columns: Day / Calls / In / Out / Cache Read / Cache Write / Reasoning / Total / Cost
   - Paginated, max `15` days per page
3. One full-width chart card
   - Title shape: `Daily Token + Model Breakdown` (and `... (last 90 days)` for all-time)
   - One chart only, not two side-by-side charts
   - For each day:
     - left grouped/stacked bar = token breakdown (Input / Output / Cache Read / Reasoning)
     - right grouped/stacked bar = model breakdown for that same day

## Data/API shape
Endpoints added/used:
- `/api/model-tokens?hours=...&limit=...`
- `/api/daily-tokens?hours=...&page=...&per_page=15`
- `/api/daily-token-chart?hours=...&limit_days=90`
- `/api/daily-model-chart?hours=...&limit_days=90&top_n=5`

### All-time rule
- For the combined daily chart only, `All time` should be capped to the last `90 days`.
- Tables can still use the selected window directly.

## Visual constraints learned from user corrections
- Do not split the final combined chart into two cards when the user asked for one.
- Make the combined chart full width.
- Tighten same-day paired bars so they visually read as one day-group rather than two unrelated bars.
- Add `Cost` columns when token tables are meant for operator accounting, not just raw token counts.

## Verification pattern
1. Restart the service.
2. Probe the new JSON endpoints directly.
3. Open `127.0.0.1:8009` in browser.
4. Confirm headings, columns, and chart count in DOM:
   - `Model Token Usage`
   - `Daily Token Usage`
   - one `Daily Token + Model Breakdown...` card only
5. Confirm no accidental extra chart remains from a prior iteration.
