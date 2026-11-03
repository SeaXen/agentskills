# Hermes dashboard terminal: history selector persistence and Top 50 preset

## What changed
This session extended the terminal command-history visibility selector with a `Top 50` preset and re-verified the persistence model.

Selector set now:
- `Top 6`
- `Top 10`
- `Top 25`
- `Top 50`
- `All`
- `Custom`

## Durable lesson
There are two different requests that sound similar but are not the same feature:

1. **Remember my last chosen history view on this browser/device**
   - solved with browser `localStorage`
   - current implementation already does this
   - verification pattern: switch selector, reload `/terminal`, confirm the same preset comes back

2. **Remember my last chosen history view server-side across browsers/devices**
   - not solved by `localStorage`
   - needs a real backend preference store/API
   - do not claim this exists unless you actually added and verified that backend path

## Why this matters
Operators often say "remember permanently" when they really mean one of two scopes:
- device-local permanence
- account/server-wide permanence

Do not blur them. If you blur them, the feature sounds finished when it is only local.

## Implementation notes
For the selector state in `TerminalPage.tsx`:
- include `"50"` in the `historyViewMode` union
- accept stored value `"50"` from `HISTORY_VIEW_MODE_KEY`
- map `"50"` to visible limit `50`
- add `<option value="50">Top 50</option>` to the selector

## Live verification shape
- build frontend
- open `/terminal`
- confirm selector shows `Top 50`
- set selector to `Top 50`
- reload `/terminal`
- confirm `Top 50` persists after reload

## Scope rule for future sessions
If the user asks for cross-device/server-side persistence, treat that as a backend feature request, not a wording tweak on the existing localStorage behavior.
