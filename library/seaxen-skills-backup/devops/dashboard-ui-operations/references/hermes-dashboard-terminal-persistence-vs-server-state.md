# Hermes dashboard terminal: refresh persistence vs server-side state

Use this when the browser Terminal tab appears to "lose" sessions or dropdown state after refresh.

## Core distinction
There are three separate persistence layers:

1. **Shell session state**
   - server-side
   - backed by persistent `screen` sessions such as `hermes-dashboard-main`
   - survives page refresh unless explicitly killed

2. **Command history rail**
   - server-side shared history
   - in this deployment, stored at `~/.hermes/terminal-command-history.json`
   - survives refresh and is shared across dashboard terminal tabs

3. **Tab/dropdown UI state**
   - browser-local
   - examples: visible tab list, active tab, split state, `More`, `Previous`
   - must be explicitly persisted/restored with `localStorage` or equivalent

## Durable debugging rule
If the user says:
- `More` disappeared after refresh
- `Previous` no longer shows
- extra sessions seem gone, but they were there before reload

check backend session inventory **and** browser-local state separately.

Do not conclude the backend lost sessions just because the tab strip reset.

## Good repair pattern
- persist local session list
- persist active session id
- persist split/open state
- persist recently-closed list
- on load, fetch `/api/terminal/sessions`
- any detached backend session not already present in local tabs should be surfaced under `Previous`

## Operator-facing explanation pattern
When explaining behavior to the user, separate these clearly:
- **terminal session** = persistent backend shell
- **command history** = shared server-side history
- **tab layout/dropdowns** = browser-local UI state

This prevents wrong answers like "refresh deletes your terminal history" when only the local tab arrangement was resetting.
