# Hermes dashboard telemetry vs analytics audit note

Use this when a third-party Hermes dashboard/plugin repo looks "stats-heavy" and the user wants to know whether it actually has analytics depth.

## Core distinction
Do not collapse these into one bucket.

### Operator telemetry
Usually means:
- gateway / system status
- session counts
- health score
- refresh age
- recent sessions
- per-session message/tool/token counters
- recent activity / operator timeline
- config snapshot / diff

### Real analytics
Look for explicit evidence of:
- `getAnalytics(...)`
- `getModelsAnalytics(...)`
- daily or historical trends
- model mix / provider mix
- token-burn history
- cost trend charts
- drilldown across time windows

A UI can feel rich while still being mostly telemetry.

## Verification rule
For Hermes dashboard plugins, do not trust route snapshots alone.

If the browser snapshot only shows the shell/sidebar:
1. verify live page text with `document.body.innerText.includes(...)`
2. count rendered nodes directly, e.g. `querySelectorAll('.mc-telemetry-row').length`
3. confirm the served bundle contains the target marker strings

This is the reliable proof that the plugin page actually rendered.

## Porting implication
If a third-party repo exposes strong telemetry but not deep analytics, port in this order:
1. health + telemetry rail
2. session stats
3. recent activity list
4. notes/checklist
5. timeline

Only after that should you consider broader analytics work.