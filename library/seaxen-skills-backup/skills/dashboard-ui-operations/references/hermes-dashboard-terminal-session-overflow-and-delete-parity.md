# Hermes dashboard terminal: session overflow, delete semantics, and prompt-position parity

Use this when the browser Terminal tab must match an older Hermes dashboard terminal UX closely.

## Durable implementation lessons

### 1) Separate stored sessions from visible tabs
If the UI should show only the first N tabs but still preserve older/newer sessions, never trim the actual session array to the visible count.

Correct model:
- `allSessions` / stored session list = source of truth
- `visibleSessions = allSessions.slice(0, visibleLimit)` or equivalent display subset
- `overflowSessions = allSessions.slice(visibleLimit)` for the `More` dropdown

Wrong model:
- `setSessions(next.slice(-maxSessions))`

That destroys recoverability and makes the 5th session look "lost" instead of overflowed.

### 2) Distinguish local remove from backend kill
For persistent browser terminals backed by `screen`, operators need two different actions:
- **remove/delete tab** = remove the browser/local session entry only
- **stop/kill/permanent delete** = terminate the backend persistent shell session too

If the UI only has one delete action, users assume the shell died when it may still be alive in backend recovery lists.

### 3) Overflow and previous-session dropdowns need the same operator affordances
When matching an older terminal UI, the `More` and `Previous` menus should expose the same practical controls the user expects:
- open/restore
- rename
- pin/unpin where applicable
- local remove/delete
- permanent delete / backend kill for persisted sessions

Do not make the overflow menu a passive list. It must be an action surface.

### 4) Full-width toolbar matters more than local pane purity
If the old UI shows the session strip and actions spanning the entire tab, keep that toolbar above the terminal/history split. Do not trap the controls inside only the left pane; users read that as a different product even if the buttons exist.

### 5) Prompt-first-row parity needs connect-time clearing, not just manual `clear`
If the terminal opens with the prompt visually lower in the pane, fixing `clear` alone is insufficient.

Useful pattern on websocket open:
- suppress noisy connection splash text
- after optional cwd/session bootstrap, send shell line-kill + clear/home control (`Ctrl+U` + form-feed / clear-home equivalent)
- resize/fit after the host card has stable geometry

Goal: first prompt should land near the first visible row on fresh open, not only after the user types `clear`.

### 6) Verify the parity request with behavior, not only with static screenshots
Minimum live checks:
1. open 5 sessions
2. confirm only the configured visible count stays on the strip
3. confirm the extra session appears under `More`
4. rename/remove one overflow session from the menu
5. confirm previous/recoverable sessions expose permanent delete / kill
6. reload and confirm prompt starts near the top-left/first row
7. open `More` and `Previous`, then hit-test menu coordinates with `document.elementFromPoint()` to ensure clicks land on menu buttons/divs, not the terminal section underneath

### 7) Dropdown layering: avoid scroll-container clipping
A toolbar using `overflow-x-auto` can clip or block vertical dropdown menus even if `overflow-y-visible` is added. This is easy to miss because screenshots may show part of the menu while pointer events still hit the xterm/terminal panel.

Safer patterns:
- make the toolbar `overflow-visible` when dropdowns must escape vertically
- or render menus through a portal/popover outside the scrolling toolbar
- keep menu wrappers `relative` and the toolbar/menu layer at a higher z-index than the terminal pane
- verify with `elementFromPoint()` at multiple points inside each open menu rectangle

## Common traps
- trimming stored sessions to the visible count
- using one delete action for both local UI removal and backend process termination
- fixing prompt position only in the `clear` command path, not on initial connect
- leaving text-heavy controls in the top row so overflow behavior appears broken simply because the toolbar wraps or clips

## Good UI defaults
- icon-only controls are appropriate for rename/pin/split/stop/cleanup/advanced actions when space is tight
- keep a few critical buttons as text if that prevents operator ambiguity
- `More` should indicate count, e.g. `More · 1`
- recoverable/persistent session controls belong in a dedicated dropdown rather than silently reappearing tabs
