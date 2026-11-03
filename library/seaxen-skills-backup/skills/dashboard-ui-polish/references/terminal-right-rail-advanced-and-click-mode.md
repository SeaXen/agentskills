# Terminal right rail: advanced placement + click mode

Use this when a terminal page already has a compact right rail with tabs such as `History / Presets / Files`, but the user complains that lower-priority controls are sitting in the wrong place or that clicking a command should not auto-run.

## Problem shape
Common bad state:
- History tab shows the command list
- then a second always-open block sits below it with things like:
  - Safety / dangerous-command confirmation
  - cwd preset
  - extra terminal behaviors
- clicking history or preset rows always injects `cmd + Enter`

This feels wrong in a terminal-adjacent rail because:
- History loses its prime scanning space
- the rail becomes taller/heavier than needed
- users cannot quickly stage and edit a command before running it

## Better layout rule
Split rail content by frequency:

### High-frequency
Keep these in the main visible command-selection tabs:
- History rows
- Preset rows
- search inputs
- pin/copy row actions

### Lower-frequency / operational controls
Move these into `Files` behind a compact `advanced` toggle:
- Safety toggle
- cwd preset per session
- command click semantics

Optional top-toolbar pattern:
- if there is already a wrench/tools button in the terminal toolbar, make it:
  1. switch the rail to `Files`
  2. open the advanced block

This is better than rendering a detached advanced block below History.

## Click semantics rule
If the user wants history/preset clicks to **insert only**:

### Add a persistent mode
Two modes are enough:
- `run` — click inserts and executes (`cmd + Enter`)
- `stage` — click inserts only; user presses Enter manually

### Apply it consistently
Use the same mode for:
- history rows
- preset command rows

Avoid mixed behavior where one surface stages and the other runs.

### Preserve explicit Enter flows
If there is a search/input box with Enter-to-run, leave that behavior alone unless the user asked to change it.

That keeps a fast path:
- row click = safe staging
- search Enter = immediate run

## Persistence pattern
If the page already persists terminal preferences:
- store the mode in localStorage
- also store it in server-side terminal preferences

Suggested key names:
- local: `hermes-dashboard-terminal-command-click-mode`
- server field: `command_click_mode`

Accepted values:
- `run`
- `stage`

## UX confirmation pattern
When staging instead of running, show a small banner/message:

`Inserted into terminal. Press Enter to run: <cmd>`

That confirms the action worked and teaches the new behavior.

## Critical implementation pitfall
Do **not** fake staging by only updating some sidebar/search state.

Correct behavior means the command is inserted into the **actual live terminal input buffer**, so the user can:
- see it at the prompt
- edit it
- then press Enter

## Verification checklist
1. Build passes.
2. Browser snapshot confirms advanced controls are no longer hanging below History by default.
3. Files tab shows an `advanced` toggle.
4. Opening `advanced` reveals Safety / click mode / cwd preset in a compact block.
5. Toggling click mode to `stage` persists after tab switches/reload.
6. Clicking a History row in `stage` mode inserts text into the terminal without execution.
7. Clicking a Preset row in `stage` mode behaves the same.
8. A visible banner/message confirms staged insertion.
