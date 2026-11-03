# Hermes telemetry home chart: settings + range polish

Session-specific pattern captured from dashboard polish work.

## What changed
- Moved `View time`, `Chart view`, and `Auto refresh` into a compact gear dropdown.
- Kept `Refresh` visible in the header.
- Tightened the gear panel: narrower width, less padding, denser label/control spacing.
- Removed the separate `Chart view` control row from beneath the KPI strip.
- Extended `/api/daily-token-chart` with `granularity=day|week|month`.
- Synced home-chart grouping across telemetry metrics and `Messages` from `state.db`.
- Trimmed leading zero-only periods per selected metric, keeping one lead-in bucket before first activity.

## Why this mattered
The user disliked two things:
1. bulky header/settings chrome
2. all-time charts that started at the first historical day even when the first long section was visually empty

For this dashboard, semantic honesty plus visual density beat literal full-history plotting.

## Practical rule
For hero KPI charts on dark dashboards:
- avoid detached control rows when the same controls can live in one gear menu
- avoid plotting long all-zero prefixes when the user is reading trend shape, not archival emptiness
- trim by **selected metric**, not a global first-nonzero date

## Verification probes
Browser checks that were useful:
- confirm gear panel labels in DOM
- confirm old chart-view toolbar is absent
- inspect `Chart.getChart('home-metric-trend-chart').data.labels`
- switch `day/week/month` and verify labels change live

## Caveat
Monthly grouping can still legitimately show early low/zero periods if that month contains the first activity bucket kept as lead-in. The goal is to remove ugly dead prefixes, not fabricate a shorter history.
