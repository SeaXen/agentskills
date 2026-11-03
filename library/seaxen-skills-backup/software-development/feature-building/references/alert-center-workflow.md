# Alert center workflow for self-hosted dashboards

Use when a dashboard has already gained diagnostics/alerts widgets and the next step is to turn those warnings into an actual operator workflow.

## Pattern

Prefer a single persisted alert-state module over stitching current-state APIs directly in the browser.

Recommended pieces:
- one app-local SQLite table for alert events/history
- one mute table keyed by alert family / rule key
- current-state synthesis from existing APIs (errors, ops, diagnostics, provider health)
- one unified route like `/api/alerts/center`
- mutation routes for `ack`, `mute`, `unmute`

## Data model

Minimum event fields:
- `alert_key` — unique current instance id
- `rule_key` — family key used for mute/unmute
- `alert_type`
- `severity`
- `status` — active / acknowledged / muted / resolved
- `title`
- `summary`
- `source_ref`
- `first_seen`
- `last_seen`
- `occurrence_count`
- `last_value`
- `meta_json`
- `acknowledged_at`
- `resolved_at`

Mute table:
- `rule_key`
- `muted_until`
- `created_at`
- `note`

## Good source families

Build current alerts from already-available app signals:
- search/API failures
- ops incidents / handoff issues
- provider-health warnings
- stale cache / bad refresh states
- slow-path thresholds

## UI shape

The page should show:
- active alerts
- muted alerts
- recent history
- compact summary counts
- ack / mute / unmute controls
- existing category slices (search, ops, runtime, provider)

## Verification

Do not stop at route existence.

Exercise a full round trip on the running app:
1. fetch `/api/alerts/center`
2. pick one active alert
3. `POST /api/alerts/ack`
4. re-fetch center and prove status became `acknowledged`
5. `POST /api/alerts/mute`
6. re-fetch center and prove it moved to `muted`
7. `POST /api/alerts/unmute`
8. re-fetch center and prove it returned to `active`
9. verify history rows exist

## Docker pitfall

When a new backend module is added for the feature, update the Docker image copy step immediately. If the module is missing from `COPY ...`, the container will restart-loop with `ModuleNotFoundError` even though local `py_compile` passed.

## When this is the right next wave

Use this after a diagnostics/alerts page already exists and the user wants the app to feel more like a control plane than a passive dashboard.