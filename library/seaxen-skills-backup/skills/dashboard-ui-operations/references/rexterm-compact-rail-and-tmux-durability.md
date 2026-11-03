# Rexterm compact rail + tmux durability lessons

Use for standalone Rexterm-style terminal clones after basic Hermes-like parity is working.

## Durable session upgrade

Best high-value next upgrade after visual/xterm parity is usually **tmux-backed sessions**, not SSH inventory or a heavier remote-host platform.

Pattern:
- one app session id maps to one tmux session
- persist metadata under `/data/sessions/<id>.json`
- keep tmux socket/runtime under `/data/tmux/<app>.sock`
- attach browser/backend clients with `tmux attach-session -t <id>`
- set attach env explicitly, especially `TERM=xterm-256color`, or tmux can fail with `open terminal failed: terminal does not support clear`
- verify by killing only the attach/client process, confirming `tmux ls` still shows the session unattached, then reattaching and running another command

If Docker build cannot reach Debian mirrors but the host can, avoid repeated apt retries. Download required `.deb` packages on the host, extract a vendored rootfs containing `tmux` and needed libs, and `COPY vendor-rootfs-tmux/ /` in the Dockerfile. Capture the workaround as packaging, not as a claim that apt/Docker is permanently broken.

## Compact right-rail terminal UX

When the user references the compact Hermes/4th-screen terminal rail, fix density and behavior together:
- right rail tabs should be compact icon + label + count chips: `History`, `Presets`, `Files`
- command rows should be short bars, not tall cards; target roughly low-30px row height, not 40px+
- remove full text button sets like `Stage / Copy / Pin / Run`
- History rows: primary row click stages/runs; trailing icons should be pin, delete, usage count (`×N`)
- Preset rows: primary row click stages/runs; trailing icons should be pin and run-now
- keep the `Stage/Run` selector as the global click behavior control
- if the user asks for faster direct access, default the visibility selector to `All`, not `Top 25`; keep `10/25/50` as short fallback choices
- make the rail section header one compact nowrap row. Remove low-value chips like `clickable`; use short labels (`Clr`, `All`, `Stage`) and trim header height to the high-20px range.
- remove noisy success banners for staging/pinning; the terminal itself is the feedback
- keep the rail visually subordinate to xterm: dark green/black, muted borders, small radii, tight padding

Also verify presets after patching History. A common miss is making History compact while Presets still use the old full-button row family. Verify both header and row heights in the live DOM, not only screenshots.

## Terminal prompt/top-left fixes

If the prompt starts in the middle, inspect two separate causes:
1. stale output/control junk restored into xterm from local/browser state
2. shell redraw/control responses being forwarded as input

Useful fixes:
- do not restore stale localStorage terminal output on reload unless it is intentionally persistent
- filter browser/xterm device-status/OSC replies before forwarding `term.onData` to bash/tmux; otherwise junk like `1;2c0;276;0c` appears in the shell
- use shell line-kill/form-feed for an explicit user-triggered clear/redraw, but avoid sending `Ctrl-U`/`Ctrl-L` automatically on every websocket attach. Attach should be read-only; automatic clear frames can create duplicate prompts, mid-screen gaps, and visible control garbage in persistent tmux shells.
- avoid blindly writing synthetic prompts into xterm; synthetic prompts can duplicate when real tmux output arrives slightly later
- if a fallback prompt is needed after an empty attach, add it only after a short delay and only if xterm rows are still blank

## Terminal geometry / bottom clipping fixes

If the last prompt/output line is not fully visible, fix the flex geometry before guessing at xterm behavior:
- make the pane/card a `flex` column with the terminal host as `flex: 1 1 auto; min-height: 0`
- put top/bottom padding on the terminal host, not inside `.terminal .xterm`, so xterm's own measured height is not silently shortened
- add a little bottom padding on the host when the prompt touches the border
- remove inline rail/card `min-height` overrides that fight the surrounding 100vh grid
- for single-pane mode, set pane gap to `0` if the user reports a remaining “second section/gap” feel
- after reload, verify DOM metrics: `paneCards === 1`, split button is off, row/header heights are compact, xterm host bottom is inside the terminal host, and a browser-vision pass shows no visible lower clipping

## Split pane guard

For standalone terminal clones, do not allow split mode with only one real live session. Otherwise the UI can show a broken/duplicate second section while commands only work in one pane.

Guard:
- if visible live sessions `< 2`, keep split disabled
- make the split button explain that a second live session is required
- do not persist split=true unless there are valid primary and secondary session ids

## Compact terminal header controls

When the terminal already has session state in the main toolbar, a second per-pane header such as `PRIMARY / ws open / alive / focused` is usually redundant chrome. If the user questions whether the terminal header is needed, remove or visually hide that pane header and verify the prompt still starts at the top-left with no new gap.

Operator semantics must be explicit:
- **Tab / Hide / Remove tab** should mean local UI removal only; backend tmux/screen session keeps running
- **Kill / Stop terminal** should mean permanent backend process/session termination
- do not let local tab-hide remove the last visible terminal; show a clear banner telling the operator to use Kill for full removal
- if pinned tabs exist, sort them first and avoid hiding them until unpinned

Dropdown reliability pitfall:
- compact terminal toolbars often use `overflow: hidden` or horizontal scrolling; this can make `More`, `Previous`, or launch-profile menus look broken because they are clipped even when JS click handlers work
- fix with visible overflow or a portal/popover layer, then verify the menu is clickable and not just visually present
- keep `Previous` always clickable: when empty, show an explicit empty-state row like `No locally removed sessions`; when a tab is locally hidden, show the hidden tab name directly in the button/menu

Visual state defaults for dense terminal headers:
- active/primary/enabled = green
- local-hide/warning = amber
- destructive kill/restart = red
- disabled = muted/dim, not invisible
- shorten labels before widening the toolbar (`Stage` → `Stg`, long paths → `/d`, `/r`, `/tb`) so controls remain one row

If the user pushes back that the header looks like short icons or a cramped strip, reverse that compression deliberately. In that case prefer a two-row, full-width header over a one-row icon bar:
- make the active terminal/tab row span edge-to-edge, with explicit text such as `Active terminal: main`
- use full action names (`New`, `Refresh`, `Rename`, `Hide tab`, `Pin`, `Previous`, `Remove`, `Restart`, `Reconnect`, `Profiles`, `Settings`) instead of icon-only labels
- keep local-hide and destructive remove visually and semantically separate: `Hide tab` = local UI only; `Remove` = kill/delete the tmux session
- rename destructive `Kill` to operator-facing `Remove` if the user asks for a remove option, but make the confirmation text explicit that it kills the backend/tmux shell
- restore full cwd labels (`/data`, `/root`, `/mnt/tb`) when legibility matters more than one-row compactness
- allow toolbar wrapping and visible overflow rather than clipping controls or hiding the meaning behind icons

## Header density and action grouping refinement

If a full-name header becomes 2-3 rows, treat that as a UX regression, even if every control works. The better Rexterm pattern is:

- keep the header one line (`flex-wrap: nowrap`, compact fixed height around 44px)
- keep only primary controls visible: active terminal label, New, Refresh, Rename, Hide tab, Pin, More, Previous, Restore, Remove, Tools, and cwd chips
- remove/hide the quick-command input from the header unless the user explicitly wants it; terminal input plus History/Presets usually cover the workflow
- move secondary controls into a `Tools` dropdown: Clear, Copy, Save transcript, Restart, Reconnect, Split, Focus, Profiles, Settings
- keep `Remove` visible and destructive: it kills/deletes the backend tmux terminal session and removes it from the header
- keep `Hide tab` separate and local-only: backend tmux shell remains alive and recoverable through Previous
- if adding live system telemetry to the header, make it compact chips rather than a new row. Good defaults: `CPU`, `RAM`, and `TEMP` chips after cwd chips; poll a small authenticated backend endpoint every ~5s; keep `n/a` for temperature when no readable `/sys/class/thermal` or `/sys/class/hwmon` sensor exists instead of faking a value; use amber/red chip states for high values.
- after patching, verify with both browser DOM metrics and vision: toolbar height one row, `flex-wrap: nowrap`, no quick-command box, Tools dropdown opens, system chips do not cause overflow/wrap, and browser console has zero JS errors

## Single-root organization pattern

When the user rejects separate `frontend/` and `backend/` wrappers for a small standalone terminal app, flatten to a single-root application rather than defending framework-style separation.

Safe pattern:
- create a full timestamped backup outside the app root before moving files
- keep important or old artifacts; move unused/support trees into `_archive/` rather than deleting them
- place live server code under `app/`, active static UI under `static/`, runtime state under `data/`, tests under `tests/`, and vendored runtime assets under explicit directories such as `vendor-rootfs-tmux/`
- keep `Dockerfile`, `docker-compose.yml`, `requirements.txt`, `.env.example`, `.gitignore`, and `.dockerignore` at root
- update Compose to `build.context: .` and the runtime volume to `./data:/data`
- ensure `.dockerignore` excludes `data/`, `_archive/`, caches, pycache, and build artifacts so sockets/runtime files do not enter Docker build context
- rebuild and verify live container, tmux socket/session metadata, browser route, and syntax checks after the move

Report the new root shape plainly and mention where preserved artifacts went. Do not claim cleanup success until the live browser and terminal/tmux path still work.

## Verification checklist

- browser vision confirms prompt is at top-left and no duplicate split pane is visible
- live DOM confirms single-pane state when split is off: `document.querySelectorAll('.pane-card').length === 1`, `#panes` gap is zero/tiny, and the split button says off
- `document.querySelectorAll('#history-list .cmd-row')` rows are compact and have icon buttons/counts
- History selector defaults to `All` after preference hydration/reload unless the user explicitly chose another mode
- History and Presets headers stay one-line/nowrap and compact; verify measured header height, not only text snapshot
- Presets tab also uses compact rows/icons
- click a row in Stage mode and confirm the command appears at prompt without a banner
- click a run icon and wait long enough for tmux/websocket output before judging; terminal output can lag behind the API acknowledgement
- verify terminal bottom visibility with enough output to reach the lower edge; do not rely on an empty prompt screen
- clean test commands from history afterward
- container status and public port are verified after rebuild/restart
