# Hermes dashboard terminal parity polish

Use this when the user wants the Terminal tab to match an older/better version more closely, not just "work".

## Symptoms this reference covers
- terminal background/text colors feel wrong versus the prior version
- extra top card/chrome makes the pane stop feeling full-bleed
- labels should become icons to reduce toolbar noise
- mouse wheel should scroll the page/terminal area, not walk command history
- ArrowUp / ArrowDown history recall is duplicating, concatenating, or cycling incorrectly
- top header gets clipped after layout changes
- stale backend shell sessions pollute the visible UI and make parity checks misleading
- command history captures ANSI garbage or corrupted prompt text

## Practical fix pattern
1. **Start with the real active surfaces**
   - patch the source page (`src/pages/TerminalPage.tsx`) when available, not only built output
   - check route/container padding too (`App.tsx` or equivalent shell layout), because header clipping is often outer-layout chrome, not the terminal component itself

2. **Restore the old visual hierarchy first**
   - darken the xterm host/background to the older near-black/green look (for this case `#050907` worked well)
   - remove redundant top per-pane status lines like `current (primary): ...` when they duplicate tab/session state already shown elsewhere
   - reduce toolbar text density: convert obvious repeated actions to icons where legibility remains clear
   - if the old version felt full-bleed, strip extra card/chip chrome above the pane before tuning minor spacing

3. **Separate wheel behavior from keyboard history behavior**
   - install an explicit xterm wheel handler with `attachCustomWheelEventHandler`
   - wheel should scroll xterm/page, not command-history recall
   - keep command-history navigation keyboard-only via ArrowUp / ArrowDown
   - do not rely on key-handler logic alone to control wheel semantics

4. **Avoid custom history-index logic unless it is truly necessary**
   - if ArrowUp / ArrowDown starts concatenating or walking history incorrectly, suspect the custom local index bookkeeping first
   - removing a brittle `historyNavIndexRef`-style layer can be the correct fix when the shell/input sync already provides enough state
   - verify recall by running a fresh command, pressing ArrowUp once, and checking that exactly one prior command appears with no extra garbage

5. **Clean input/history synchronization**
   - when local command-history chips are built from visible current-line state, strip ANSI escape sequences aggressively before saving/syncing
   - otherwise history suggestions can accumulate CSS fragments, prompt leftovers, or terminal control junk

6. **Fix clipping at the outer layout level**
   - remove negative top margins first
   - then tighten route/page padding if the terminal page inherits extra shell spacing
   - for viewport-fit grids, adjust `min-h: calc(100vh - ...)` carefully; a small shell-offset mismatch is enough to clip the top header or bottom prompt

7. **Reset stale backend state before final QA**
   - kill stale persistent terminal sessions if they are polluting the fresh visual state
   - then reload and verify against a clean session so old prompts/history do not hide whether the UI is actually fixed

8. **Match the old top-bar geometry, not just the colors**
   - if the reference screenshot shows one continuous toolbar across the terminal and side rail, move the toolbar above the content split instead of leaving it inside the left column only
   - this is usually the fix when controls feel cramped or the header does not look full-tab wide even though the page itself fills the screen
   - removing a duplicated inline state row like `current (primary)` can help the right rail align visually with the old compact version

9. **For `clear`, fix both the browser buffer and the shell line discipline**
   - if running `clear` leaves the prompt floating in the middle or leaves `root@...# clear` echoed at the top, browser-side clearing alone is not enough
   - a working pattern is: clear the xterm buffer locally (`term.clear()` plus `\x1b[2J\x1b[H`) and send shell control characters that wipe the typed line before form-feed (`Ctrl+U` + `\f`, i.e. `\u0015\f`)
   - verify with a live browser run: type `clear`, press Enter, and confirm the next prompt lands at the top-left with no stale echoed command line remaining

## Verification pattern
- build frontend and validate backend syntax before UI QA
- browser-verify the live `/terminal` route after deploy
- create or focus a clean session
- type a fresh command, press Enter, then ArrowUp once
- confirm one clean previous command is recalled
- confirm wheel interaction does not mutate command recall state
- inspect visible command history list for ANSI/control-sequence pollution
- if needed, kill stale backend session(s), reload, and repeat the same check on a fresh prompt

## Concrete file touchpoints from this case
- `web/src/pages/TerminalPage.tsx`
- `web/src/App.tsx`
- shared command history file under `~/.hermes/terminal-command-history.json`

## Notes
- Service restart failures or systemd oddities are secondary if the live browser already proves the served frontend changed.
- For parity work, use visual QA plus functional terminal interaction checks together; text snapshots alone are too weak.