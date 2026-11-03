# Hermes dashboard terminal: wheel-vs-history, fit, and reload-state notes

Use this when the dashboard terminal tab looks visually fine at first glance but operators report three specific failures:
- mouse wheel still recalls previous commands instead of scrolling the terminal buffer
- the last terminal row is clipped at the bottom edge
- reloading the page revives the previous local terminal session layout instead of starting fresh

## Durable lessons

### 1) Keyboard-only history interception is insufficient
Handling `ArrowUp` / `ArrowDown` with `attachCustomKeyEventHandler` does **not** guarantee mouse wheel safety.

Why:
- xterm mouse/wheel events can still travel through a different path than keyboard events
- the shell may interpret those events as history/navigation input
- the UI can appear "fixed" in keyboard tests while wheel still triggers command recall for the user

Safer pattern:
- keep `attachCustomKeyEventHandler` for command history recall
- also add `attachCustomWheelEventHandler`
- inside the wheel handler:
  - call `term.scrollLines(...)`
  - `preventDefault()`
  - `stopPropagation()`
  - return `false`

Verification:
- test `ArrowUp` and confirm `current (...)` changes to the previous command
- dispatch or manually perform a wheel event and confirm `current (...)` does **not** change
- if possible, verify the wheel event was prevented while xterm scrollback moved

### 2) Bottom-row clipping is often a flex geometry bug, not a font-size bug
Reducing line height alone may mask the symptom without fixing layout.

Common bad shape:
- terminal panel has a header row
- xterm host uses `h-full`
- parent container is not a vertical flex column

Result:
- xterm fits against the wrong height basis
- the bottom row gets clipped or visually pressed into the border

Safer layout:
- terminal card: `flex flex-col`
- terminal host: `flex-1 min-h-0 overflow-hidden`
- avoid `h-full` for the xterm host in header-bearing panels
- then run `fit.fit()` and resize handling

Useful check:
- compare panel bottom, host bottom, and xterm viewport bottom in the DOM
- there should be sane bottom clearance instead of the host overrunning the panel

### 3) Reload semantics matter: local tab restore vs persistent backend sessions
If operators expect reload to feel like a fresh terminal page, do **not** restore old browser-local terminal tabs and split state from `localStorage`.

Preferred behavior for Hermes dashboard terminal:
- local UI starts from default tabs (for example `main`, `work`, `logs`, `scratch`)
- persistent backend `screen` sessions appear under `Previous`
- recover from `Previous` explicitly instead of silently reopening old local UI state

Migration note:
- after removing local restore behavior, also clear stale keys such as:
  - `hermes-dashboard-terminal-sessions`
  - `hermes-dashboard-terminal-active`
  - `hermes-dashboard-terminal-secondary`
  - `hermes-dashboard-terminal-split`
- otherwise old state can keep resurfacing after reload and make the fix look fake

## Practical verification sequence
1. Reload `/terminal`
2. Confirm default local tabs are present
3. Confirm old persistent backend session is listed under `Previous`, not reopened as the active local tab
4. Check browser storage: the old terminal tab/session keys should be absent or cleared
5. Confirm `ArrowUp` still recalls history
6. Confirm mouse wheel no longer changes the current command line
7. Inspect the bottom edge visually and, if needed, with DOM geometry for clipping

## Reporting rule
Do not claim a terminal UI bug is fixed from code inspection alone.
For this class of issue, verify all three separately:
- keyboard history behavior
- wheel behavior
- reload behavior
- visual bottom-edge fit
