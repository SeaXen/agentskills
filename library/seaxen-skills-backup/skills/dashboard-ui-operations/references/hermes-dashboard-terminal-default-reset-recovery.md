# Hermes dashboard terminal: default-reset recovery after dashboard reload

Use this when the user says terminal sessions are "gone" after reloading the dashboard, but backend Hermes terminal screens may still exist.

## Failure shape

A browser reload or dashboard-shell reset can leave terminal `localStorage` in the default local state:
- `main`
- `work`
- `logs`
- `scratch`

If backend `screen` sessions still exist beyond that set, a weak recovery path makes them look lost by putting them only under `Previous` instead of restoring them into the visible tab model.

Operator experience:
- shell still exists server-side
- browser tab list looks reset
- user concludes the terminal session vanished

## Durable fix

When `/api/terminal/sessions` returns backend sessions not present in the current local tab list:

1. detect whether the current local tab list is merely the default 4-session set
2. if yes, treat this as a browser-state reset, not an intentional curated tab list
3. auto-merge the missing backend sessions back into `sessions`
4. show a small banner such as `Recovered N terminal session(s) from backend after dashboard reload.`
5. only use `Previous` for genuinely detached/recoverable sessions when the current local session list is not obviously a default-reset fallback

## Why this matters

If you only add the missing backend sessions to `Previous`, the operator still experiences the state as broken:
- the session they were actively using is absent from the main tabs
- it looks like data loss even though the shell process survived

The correct UX is:
- browser state reset → restore missing backend sessions directly into tabs
- intentional local cleanup/removal → keep backend survivors under `Previous`

## Verification pattern

When the bug does not reproduce naturally, force it:

1. create an extra terminal session backed by Hermes `screen`
2. confirm `/api/terminal/sessions` lists it
3. overwrite browser `localStorage` terminal session state back to the default 4 sessions
4. reload `/terminal`
5. verify:
   - the missing backend session is restored into tabs
   - a recovery banner appears
   - `localStorage` now contains the restored session
   - the session is not only stranded under `Previous`

## Key distinction to preserve in reasoning

Three layers are different:
1. backend shell sessions — server-side persistent `screen` sessions
2. command history chips — server-side shared history
3. tab arrangement / dropdown state — browser-local UI state

This bug is about layer 3 losing shape while layer 1 still exists.
