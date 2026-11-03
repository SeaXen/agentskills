# Mnemosyne dashboard: History tab false auth caused by route alias drift

## Symptom
- Opening `?tab=history` showed the `Password required` overlay even though auth status reported:
  - `auth_enabled: false`
  - `authenticated: true`
- No real auth problem existed.

## Root cause
Frontend route naming had drifted:
- nav button used `data-tab="activity"`
- History section id was `activity`
- but deep links could still arrive as `?tab=history`
- frontend routing did **not** normalize `history -> activity`

That caused startup routing to target a non-existent section. The boot sequence then fell into the generic `.catch(() => showLogin())` path, which surfaced the auth overlay as a misleading fallback.

## Fix shape
Patch `static/app.js` so the legacy alias is normalized everywhere it matters:
- `canonicalTab('history') -> 'activity'`
- `sectionFor('history') -> 'activity'`
- `panelFor('history') -> 'activityTimeline'`

## Verification
A real fix should prove all of these:
1. Open `/?tab=history`
2. URL canonicalizes to `?tab=activity`
3. login overlay stays hidden
4. History section renders
5. timeline entries load

## Reusable lesson
When a dashboard shows a password/auth overlay but auth status says disabled, inspect **route aliasing and startup catch paths** before blaming auth config.