# AceRoute cold-load performance pattern

Use this for FastAPI + SQLite dashboards where users report page-open latency like "10-20 sec" even though warm refreshes feel fine.

## What to measure first

Measure live endpoints separately before changing code:
- base HTML
- main JS bundle
- dashboard aggregate endpoint
- list/table endpoint
- cold (`fresh=1`) vs warm cached path

This distinguishes:
- backend aggregate slowness
- frontend blocking render
- DOM/chart cost
- static asset transfer cost

## Pattern that worked

### 1) Add analytics indexes to the source SQLite DB
For Hermes `state.db` analytics over `messages` and `sessions`, these indexes materially improve query plans:

```sql
CREATE INDEX IF NOT EXISTS idx_messages_role_active_ts
  ON messages(role, active, timestamp DESC);
CREATE INDEX IF NOT EXISTS idx_messages_active_ts
  ON messages(active, timestamp DESC);
CREATE INDEX IF NOT EXISTS idx_messages_role_finish_ts
  ON messages(role, active, finish_reason, timestamp DESC);
CREATE INDEX IF NOT EXISTS idx_messages_role_session_ts
  ON messages(role, active, session_id, timestamp DESC);
CREATE INDEX IF NOT EXISTS idx_sessions_id_model_source
  ON sessions(id, model, source);
```

Important: if the dashboard container reads the DB directly, ensure these indexes at app startup so they survive rebuild/redeploy and do not depend on one manual shell session.

### 2) Stop blocking page paint on dashboard + list
Requests/Messages-style pages should not wait for both aggregate dashboard data and the first row list.

Better pattern:
- fetch dashboard aggregate first
- paint summary/charts immediately
- show loading placeholder for the table
- let list rows fill in after
- cache both results for repeat opens

This makes a still-slow cold aggregate feel much faster because the page stops looking frozen.

### 3) Reduce first table load size
If the first view renders 80-100 rows, trim it.

Practical default that worked:
- first load: 50 rows
- keep deeper drill/search pagination available

This reduces DOM and string-building cost on open.

### 4) Keep all-time totals true, but cap all-time chart timelines
For all-time dashboards, do **not** fake totals with a shorter range.

Do this instead:
- totals/toplists: true all-time
- chart timeline: recent bounded analytic window (e.g. last 400 days)
- client downsample again for chart rendering (e.g. ~96 points)

This preserves correctness while preventing wasteful giant time-series work for charts.

## Diagnostic interpretation

If measurements look like this:
- fresh dashboard endpoint: seconds
- same endpoint cached: milliseconds
- list endpoint: sub-second

then the real issue is the cold aggregate query path, not the list page or the static shell.

## Verification pattern

After changes, verify separately:
- HTML time
- JS time
- dashboard endpoint fresh time
- dashboard endpoint cached time
- list endpoint time
- served asset version bump
- health endpoint after restart/redeploy

## Deployment note

If Python backend code changed inside a Docker image, restart/recreate the service before claiming success. Static bind-mounted JS/HTML may update instantly, but Python collector changes do not.

## Result profile to aim for

- cold dashboard aggregate: reduced as much as possible
- warm aggregate: near-instant
- list endpoint: sub-second
- visible page content appears before the slowest aggregate finishes
