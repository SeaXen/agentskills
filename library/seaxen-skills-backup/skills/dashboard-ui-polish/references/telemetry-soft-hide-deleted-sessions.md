# Telemetry dashboard: soft-hide deleted Hermes sessions

Use when a telemetry dashboard stores historical run rows separately from the primary app's session store and the user expects deleted sessions not to appear in session-facing UI.

## Pattern

Keep telemetry history intact, but hide deleted sessions from interactive session lists by default.

Default visibility rule:
- show runs whose `session_id` still exists in the app's active/session metadata
- show cron/system runs that do not have normal session files, if they are operationally useful
- hide historical rows whose source session was deleted
- preserve aggregate cost/token charts unless the user explicitly asks for hard purge

For Hermes telemetry specifically:
- active IDs come from `HERMES_HOME/sessions/sessions.json` values' `session_id`
- also include `HERMES_HOME/sessions/session_*.json` filenames, stripping `session_` and `.json`
- preserve cron rows with `session_id LIKE 'cron_%'`
- expose an escape hatch such as `/api/runs?include_deleted=1` for debugging/audit
- return `hidden_deleted_runs` so the UI can explain why rows disappeared

## UI copy

Session-facing tables should say deleted sessions are soft-hidden, e.g.:

`89 deleted Hermes session(s) soft-hidden.`

Avoid implying telemetry was deleted. Say explicitly:
- soft-hidden from session lists/investigation
- still preserved in telemetry history/aggregate totals

## Implementation notes

- Put the visibility clause in the backend list endpoint, not only in frontend filtering.
- Compare against the primary session store on every request or via a cheap helper; avoid mutating telemetry rows for soft hide.
- Keep a query flag like `include_deleted=1` for operator debugging.
- Do not apply soft-hide blindly to cost/token summary cards unless the user asks; audit/history totals are usually expected to remain intact.
- Never use `Path.home()` directly in Hermes plugins; derive paths from `HERMES_HOME` with fallback to `~/.hermes`.

## Verification

Check both views:
1. API without `include_deleted` returns fewer rows and a nonzero `hidden_deleted_runs` when deleted rows exist.
2. API with `include_deleted=1` returns the raw telemetry count.
3. Home Recent Sessions and Investigation no longer show deleted session IDs.
4. UI displays the soft-hide count/explanation.
5. Browser console has no JS errors.
