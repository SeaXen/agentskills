# Mission Control Phase 5 dashboard pattern

Use this when extending the Hermes companion dashboard beyond session control into compact analytics and operational awareness.

## Goal
Add a premium "mission center" layer without modifying core dashboard pages:
- lightweight telemetry
- workflow-level insight panels
- model usage visibility
- cron health visibility
- session timeline context

## APIs to reuse
Prefer existing dashboard SDK APIs:
- `SDK.api.getAnalytics(7)` for recent usage totals and daily activity
- `SDK.api.getModelsAnalytics(30)` for model/provider mix and leaderboard-style summaries
- keep existing calls for sessions, model info, skills, toolsets, profiles, and cron jobs

Recommended load pattern:
- extend the existing `Promise.all([...])` dashboard load path
- fetch analytics together with status/model/session data
- store analytics in local React state; do not add new backend routes unless existing APIs are insufficient

## Default Phase 5 sections

### 1) Mission telemetry
Compact summary strip with:
- 7d sessions
- 7d API calls
- 7d tokens
- 7d cost

Then add:
- **Daily pulse**: last few analytics daily entries as compact sparkbars
- **30d model mix**: model/provider usage bars from `getModelsAnalytics(30)`

### 2) Workflow radar
Useful high-signal cards:
- **Session timeline**: selected session last active / messages / tool calls / tokens
- **Model leaderboard**: top recent models with token volume, provider, session count, cost
- **Cron health**: last run / next run / paused-attention state / brief error snippet
- **Top skills**: recent skill usage with counts and last used time

## UI guidance
Keep the Phase 5 layer compact and premium:
- use grid cards, not giant charts
- prefer sparkbars / meters over heavy chart libraries
- keep everything visually scannable in one viewport when possible
- reuse card vocabulary from earlier phases (`detail-card`, `chip-title`, `small`, badges)

Suggested CSS blocks:
- `.mc-telemetry-grid`
- `.mc-analytics-strip`
- `.mc-sparkline`
- `.mc-model-meter`
- `.mc-radar-grid`
- `.mc-timeline-list`

## Formatting helpers worth adding
Small helpers improved readability in this session:
- `formatMoney(value)` for compact spend display
- `formatDayLabel(day)` for daily activity labels
- normalized percent-based sparkbar rendering for telemetry and leaderboards

## Browser verification pattern
After edits:
1. rescan plugins from the dashboard using absolute URL + dashboard session token
2. reload `/mission-control`
3. confirm these labels render:
   - `Mission telemetry`
   - `Workflow radar`
   - `Session timeline`
   - `Model leaderboard`
   - `Cron health`
   - `Top skills`
   - `30d model mix`
   - `Daily pulse`

## Testing pattern
Extend the plugin smoke test to assert:
- `SDK.api.getAnalytics(7)` present in bundle
- `SDK.api.getModelsAnalytics(30)` present in bundle
- the new Phase 5 section labels exist in bundle text
- the analytics CSS blocks exist in stylesheet

## Pitfalls
- Do not build a separate analytics backend if the dashboard SDK already exposes enough data.
- Do not jump to heavyweight charts for this companion dashboard; compact meters are faster to ship and fit the premium dense UI better.
- Keep analytics time windows explicit in labels (`7d`, `30d`) so the user can trust what they are seeing.
