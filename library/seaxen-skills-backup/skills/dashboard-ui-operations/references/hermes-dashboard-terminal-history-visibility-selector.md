# Hermes dashboard terminal: history visibility selector

## When to use
Use this pattern when the user wants **all command history retained** but does **not** want the history rail to render every clickable command row all the time.

Typical ask shapes:
- "show total history, but only some clickable commands"
- "6 cmds clickable or all?"
- "keep all history stored, but let me expand"

## Core rule
Separate these two concepts:

1. **Stored/shared history**
   - server-side command history exists in full
   - total count should stay visible and honest (`N cmds`)

2. **Visible clickable rows**
   - purely a UI rendering limit
   - changing the selector must **not** delete or trim stored history

If those two concepts get mixed together, users think history was lost when it was only hidden.

## Recommended selector shape
Default compact presets:
- `Top 6`
- `Top 10`
- `Top 25`
- `All`
- `Custom`

Semantics:
- `Top 6/10/25` = show that many visible clickable rows after filtering
- `All` = render every stored history row
- `Custom` = reveal a numeric input and use that count as the visible limit

Good default:
- start at `Top 6`
- keep total count visible beside the history label
- persist the selector in browser `localStorage`

## UI wording to keep clear
Explain it simply:
- `7 cmds` = there are 7 stored command entries in shared history
- `Top 6` = only the first 6 are shown as direct clickable rows
- `All` = show all 7 clickable rows right now

That wording avoids the common confusion between "history exists" and "history is currently rendered."

## Implementation notes
Useful state split:
- `historyViewMode`: `"6" | "10" | "25" | "all" | "custom"`
- `historyViewCustom`: numeric custom fallback
- `historyVisibleLimit`: derived from the mode

Recommended localStorage keys:
- `hermes-dashboard-terminal-history-view-mode`
- `hermes-dashboard-terminal-history-view-custom`

If the operator wants the preference to follow them across browsers/devices too, keep the browser-side localStorage persistence **and** add a small server-side preference surface. Good shape:
- `GET /api/terminal/preferences`
- `POST /api/terminal/preferences`
- persist a tiny JSON file such as `~/.hermes/terminal-ui-preferences.json`
- on page load: prefer local browser state when present, otherwise hydrate from server-side prefs
- on selector change: update both localStorage and the server-side prefs

Findability rule:
- do not leave the selector as an unlabeled tiny combobox in the rail header
- add a short explicit chip/label such as `show` or `show clickable` immediately before the selector
- put it in the **Command history header row** so the operator can discover it without hunting in advanced menus

Rendering rule:
- filter/search first
- then apply the visible limit slice
- keep the total count badge based on the full stored/shared history set, not the sliced view

## Verification pattern
Live-verify all 4 cases:
1. `Top 6` shows exactly 6 visible delete/click targets
2. `All` shows the same number of visible rows as the history API/store count
3. `Custom` reveals the numeric input
4. changing custom to `3` shows exactly 3 rows

Also verify:
- selector choice survives reload in the same browser
- total count badge does not change just because the visible limit changed
- no history rows are deleted by switching selector modes

## Why this is the best default
This pattern gives:
- compact rail by default
- honest total-count visibility
- full expansion when needed
- low ambiguity for operators

It is better than forcing either:
- always-all rows (too noisy), or
- permanently truncated rows with no explicit expansion path (looks like data loss)
