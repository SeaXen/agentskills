# Obsidian dashboard visual polish patterns

Use this when the Obsidian vault dashboard (`obsidian_dashboard.py`) needs a visual upgrade pass — not structural changes, but rendering quality, depth, and polish.

## File location
- `/mnt/tb/hermes/obsidian_dashboard.py` (real path; may also appear at `/root/.hermes/obsidian_dashboard.py` — verify samefile)
- Service: `obsidian-vault-dashboard.service` (systemd user)
- Port: `6065`

## Proven visual upgrades (2025-05-27)

### 1. Simulation stability
- Alpha decay: `0.972` -> `0.995` per frame in `tickSimulation()`
- Spring force: `0.018` -> `0.032` for link attraction
- Same-folder spring distance: `0.12` -> `0.08` (tighter clusters)
- Result: graph settles smoothly without jitter

### 2. Missing/broken-link nodes
- Old: all Missing nodes clustered at fixed slot `(0.84, 0.82)` - looked scattered and orphaned
- New: distribute Missing nodes near the average polar coordinates of their referrer source nodes
- Result: broken links visually connect to their source cluster

### 3. Background
- Old: basic line grid
- New: dot-grid pattern (42px spacing, 1.1px radius dots, `rgba(100,116,139,0.14)`) + radial vignette overlay
- Vignette: center `rgba(4,7,13,0)` -> edge `rgba(4,7,13,0.82)`
- Result: premium dark canvas feel

### 4. Node rendering
- Old: flat solid-color circles with binary shadow (0 or 18px)
- New: glossy 3D radial gradient sphere with highlight at top-left and dark at bottom-right
- Layered shadow: `shadowOffsetY: 3.5dp`, blur 6-24dp by state (selected > pinned > hovered > normal)
- Thin glassy border: `rgba(255,255,255,0.24)` stroke
- Result: nodes look like polished glass spheres

### 5. Link rendering
- Old: heavy bundling (pull 18/26, ratio 0.52/0.48) -> visual noise
- New: gentler bundling (pull 6/10, ratio 0.75/0.25)
- Added arrowheads at target end (triangle at node boundary, sized 4.4-5.5dp)
- Result: cleaner edges with directional cues

### 6. Hull clusters
- Old: fill alpha 0.08, stroke 0.26 - nearly invisible
- New: fill alpha 0.12, stroke 0.35
- Result: folder clusters clearly visible as subtle colored regions

### 7. Label placement
- Old: padding 6dp, no node collision check
- New: padding 12dp, added node-circle collision detection via closest-point distance check
- Result: labels never overlap nodes

### 8. Toast / notifications
- Old: `showToast()` called with empty string on load -> phantom "Layout saved" visible on page load
- New: guard `if (!message) return;` at top of `showToast()`

### 9. Panel glass-morphism
- Added `backdrop-filter: blur(20px)` on `.panel`
- 5-layer drop-shadow system for depth
- Transparent highlight border

### 10. Header
- Height: 60px -> 72px
- Gradient underline via `header::after` pseudo-element (transparent -> accent purple/cyan -> transparent)
- Brand text: gradient fill (`-webkit-background-clip: text`) purple->cyan

### 11. Workspace bar
- Active button: left accent gradient line via `::before` pseudo-element (3px wide, purple->cyan)

### 12. Notes rail toggle
- Old: static "Hide" text
- New: dynamic "Collapse"/"Expand" with proper state tracking

## Verification sequence
1. `python3 -m py_compile /mnt/tb/hermes/obsidian_dashboard.py`
2. Extract inline JS to `/tmp/check_dashboard.js`
3. `node --check /tmp/check_dashboard.js`
4. `systemctl --user restart obsidian-vault-dashboard.service`
5. `systemctl --user is-active obsidian-vault-dashboard.service`
6. `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:6065/`
7. Browser: verify dot-grid background, glossy nodes, visible hulls, no phantom toast
