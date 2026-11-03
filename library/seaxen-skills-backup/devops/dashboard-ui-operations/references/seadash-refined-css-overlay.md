---
name: seadash-refined-css-overlay
description: Safe CSS polish pattern for SeaDash (or any 189+ class single-file dashboard) — append a second <style> block that overrides the original visually without touching the 822-line original. Used when the user asks for visual refinements but the existing UI structure (modals, layout editor, all 158+ specialized class definitions) must stay intact.
---

# SeaDash refined CSS overlay (preserves all original classes)

## When to use

- User asks for visual polish on SeaDash `:9090` ("make it look better", "cleaner", "more modern", "prettier", "fix the design", "like the HA reference image")
- A previous full CSS replacement on the same file **broke the modal architecture** (`.modal` and `.modal-overlay` collapsed into the same rule) and **deleted 158 specialized class definitions** (`.card-stat`, `.card-action-btn`, `.layout-toolbar`, `.sysinfo-grid`, `.section-icon`, `.settings-group`, `.quick-actions`, `.theme-picker`, `.toast`, `.stats-bar`, etc.)
- The original 189 class selectors in `/mnt/tb/1Apps/SeaDash/index.html` lines 10-832 must remain, but visual properties (colors, radius, padding, hover, focus, gradient backgrounds, transitions) need to look modern and consistent

## The non-negotiable rule

**Never blanket-replace the existing `<style>` block on a file with this many specialized class definitions.** Even a perfectly-written replacement CSS will silently lose classes that the JS depends on. The dashboard will *look* fine but specific modals/cards/controls will be unstyled, and modal Save/Close buttons can become unclickable if the `.modal` and `.modal-overlay` rules conflict.

The safe pattern is **append a second `<style id="refined">` block before `</head>`** that the existing CSS selectors override. Originals stay; new rules win where they apply.

## The append-overlay recipe

```python
import pathlib
src = pathlib.Path('/mnt/tb/1Apps/SeaDash/index.html')
html = src.read_text(encoding='utf-8')
refined = pathlib.Path('/tmp/seadash-refined.css').read_text(encoding='utf-8')

inject = '\n<style id="refined">\n' + refined + '\n</style>\n'
# Insert just before </head>; later rules win on equal specificity
new_html = html.replace('</head>', inject + '</head>', 1)
assert new_html != html, "injection failed"

src.write_text(new_html, encoding='utf-8')
```

This works because:
- The browser parses the first `<style>` block first
- The second `<style id="refined">` block is parsed immediately after
- For any conflicting selector (same name + same specificity), the later rule wins
- All original class definitions that the new block does not touch remain functional
- All JS bindings (`saveLayoutColumn()`, `closeModal('modal-layout')`, `toggleLayoutAutoRule('public')`, `applyLayoutPreset()`) keep firing because their class lookups still resolve

## What to include in the overlay

Override these visual properties only:
- `:root` design tokens (colors, radii, shadows, transitions)
- `.header`, `.actions`, `.btn` / `button` / `[role="button"]` (background, padding, border-radius, hover, focus, primary/secondary/danger/ghost variants)
- `.alert-banner` / `.alerts` / `[class*="alert"]` (background, color, border)
- `.section` / `.section-header` / `h2` (padding, font-weight, color, separator removal)
- `.app-grid` / `[class*="grid"]` / `.cards` (gap, padding)
- `.app-card` / `.card` / `[class*="card"]` (border-radius, padding, background, border, shadow, hover lift)
- `.status-led` / `.status-text` (size, color, glow)
- `.badge` / `.tag` / `[class*="badge"]` (pill chip, semantic colors)
- `.modal` / `.modal-overlay` (only adjust visuals; preserve `display: none / display: flex` toggle on `.modal-overlay.active`)
- `.auth-overlay` / `.auth-box` (these are usually lost when only `:root` is overridden — explicit block needed)
- `.table-*`, `.card-stat`, `.stat-pill`, `.docker-action-btn`, `.card-action-btn`, `.layout-*`, `.settings-*`, `.sysinfo-*`, `.theme-*`, `.toggle` / `.layout-pin-toggle`, `.toast`, `.quick-actions`, `.statusline`, `.live-dot`, `.search-box`, `.empty-state`, `.hint`, `.drag-handle`, `.cf-panel`, `.logs-viewer`

**Be explicit about `.auth-overlay`** — this is the most commonly missed class when doing surgical polish. Original CSS has:
```css
.auth-overlay { display:none; position:fixed; inset:0; z-index:500; ... }
.auth-overlay.active { display:flex; }
```
Without these, the login form shows over the dashboard on every load. Add the rules to the overlay block.

## Modal-architecture preservation rule

The modal architecture is:
```html
<div class="modal-overlay" id="modal-layout">  <!-- backdrop, hidden by default -->
  <div class="modal xl">                       <!-- panel, smaller, scrollable -->
    <h3>...</h3>
    <button onclick="saveLayoutColumn()">Save</button>
    <button onclick="closeModal('modal-layout')">Close</button>
  </div>
</div>
```

- `.modal-overlay` is the fullscreen backdrop with `position: fixed; inset: 0; z-index: 200;`
- `.modal` is the inner panel, sized via `.modal`, `.modal.wide`, `.modal.xl`
- Visibility is toggled by adding/removing `.active` on `.modal-overlay` (`.active` adds `display: flex`)

**NEVER** target `.modal` and `[class*="modal"]` with the same rule that targets `.modal-overlay`. They are different elements. Conflating them will:
- Make the inner panel become a fullscreen overlay itself
- Block pointer events on the actual Save/Close buttons
- Make `classList.add('active')` on the panel set the wrong display state

The safe selectors for modal visuals are:
- `.modal-overlay` and `.modal-overlay.active` for backdrop visuals
- `.modal`, `.modal.wide`, `.modal.xl` for panel visuals
- `.modal h3`, `.modal label`, `.modal input`, `.modal-actions` for inner content

## Verification (mandatory before claiming success)

After the append, verify end-to-end — not just visually:

1. **HTTP 200 + grep for new tokens**
   ```bash
   curl -sS -o /dev/null -w "HTTP %{http_code} | %{size_download} bytes\n" http://localhost:9090/
   curl -sS http://localhost:9090/ | grep -E "refined|--accent:|card-hover" | head -5
   ```

2. **All 9 modals present and have close handlers**
   ```js
   (function(){
     const ids = ['modal-app','modal-sysinfo','modal-docker','modal-logs',
                  'modal-bookmark','modal-settings','modal-sysactions',
                  'modal-alerts','modal-layout'];
     return JSON.stringify(ids.map(id => {
       const m = document.getElementById(id);
       return {id, exists: !!m, hasCloseHandler: !!(m?.querySelector(`[onclick*="closeModal('${id}')"]`))};
     }));
   })()
   ```

3. **Modal opens AND closes on real DOM click**
   ```js
   // open
   document.querySelector('#modal-layout button[onclick*="saveLayoutColumn"]').click();
   // verify modal still open (save does not auto-close)
   // close
   document.querySelector('#modal-layout button[onclick*="closeModal"]').click();
   // verify modal classList no longer contains 'active'
   ```

4. **Critical functions still defined**
   ```js
   ['openAddModal','saveApp','deleteApp','saveConfig','saveRouteMap',
    'saveNotifySettings','openLayoutModal','loadLayoutColumnEditor',
    'newLayoutColumn','deleteLayoutColumn','addLayoutLinkRow',
    'removeLayoutLinkRow','moveLayoutColumn','toggleHideStandardSections',
    'toggleLayoutPinned','toggleLayoutAutoRule','toggleCompactDashboard',
    'setLayoutFilter','selectLayoutIcon','selectLayoutPreset',
    'setAllLayoutChecks','selectDuplicateLayoutRefs',
    'moveCheckedRefsToCategory','applyLayoutPreset','exportLayoutPreset',
    'importLayoutPreset','refreshDocker','refreshAll','rescanApps',
    'refreshLogs','openDockerModal','dockerAction','sysAction',
    'toggleAlerts','toast','cycleTheme','setView','toggleSection']
     .map(f => [f, typeof window[f]])  // all must be "function"
   ```

5. **Programmatic open+close of representative modals**
   ```js
   (function(){
     const tests = [
       {id:'modal-settings', open:'openSettings()'},
       {id:'modal-sysinfo', open:'openSysInfo()'},
       {id:'modal-sysactions', open:'openSystemActions()'},
       {id:'modal-logs', open:'openLogsModal()'},
     ];
     return JSON.stringify(tests.map(t => {
       try {
         eval(t.open);
         const opened = document.getElementById(t.id).classList.contains('active');
         closeModal(t.id);
         const closed = !document.getElementById(t.id).classList.contains('active');
         return {id: t.id, opened, closed, ok: opened && closed};
       } catch (e) { return {id: t.id, error: e.message}; }
     }));
   })()
   ```

6. **Visual confirmation** with `browser_vision` — ask the model to describe colors, card style, button shape, and confirm polished without glaring issues.

## Pitfalls learned the hard way

- **Do not blanket-replace the original CSS block.** Even if your replacement looks better, it will silently delete 100+ class definitions and break specific features. A user saying "make it look better" does not mean "throw away the layout editor styling".
- **Do not use `[class*="modal"]` selectors** — they conflate the backdrop (`.modal-overlay`) and the panel (`.modal`) and break the toggle.
- **Do not use `[class*="alert"]` to style alerts as the default** without checking the real DOM. The string `alert` appears in random classnames like `data-alert-count` and you can accidentally style the wrong things.
- **Do not assume `.auth-overlay` is covered by generic `.modal-overlay` rules** — it has a different `z-index` (500 vs 200) and a separate `.auth-box` child, and it controls the login screen that blocks the dashboard.
- **Do not forget to back up before the edit.** The append-overlay pattern is safe, but a full-replace is not — keep the original at `index.html.bak.<timestamp>` so a quick `cp` restores the working state.
- **Do not stop at HTTP 200 + visual confirmation.** A 200 with broken modals is the worst kind of "fixed" — confirm via DOM `classList`, real `.click()` on Save/Close, and `typeof window[functionName] === 'function'`.
- **Do not let the auth overlay cover the dashboard after the edit.** A missing `.auth-overlay { display: none }` rule shows the login form on every load. Always include the auth overlay rules in any SeaDash CSS edit.
- **Do not ignore the user when they say "all my design and features look are gone".** That complaint means a class definition was deleted. Audit the new CSS against the original by extracting unique class selectors and computing the diff before claiming the result is polished.

## File locations

- Source: `/mnt/tb/1Apps/SeaDash/index.html`
- Service: `/etc/systemd/system/seadash.service` → `/usr/bin/python3 /mnt/tb/1Apps/SeaDash/server.py`
- Working dir: `/mnt/tb/1Apps/SeaDash`
- Backups: `index.html.bak.refined.<timestamp>` (append-overlay) or `index.html.bak.retro.<timestamp>` (atomic-replace)
- Public URL: `https://dash.xuup.top`, local: `http://localhost:9090`
- Server restart: not needed for `index.html` edits; just refresh the browser

The Python `server.py` does not need to be touched — it serves the file as static content. No restart after editing `index.html`.

## Related: when the user shows a Homarr / Home Assistant / layered-card reference

If the user's complaint after the append is "still ugly, my cards don't look like the screenshot", this is a polish pass that needs more than the append-overlay. Move to the layered-card pattern: a `::before` pseudo overlay that creates a "card inside a card" depth effect, with the badge/icon/actions positioned as floating zones (top-left LED, top-right badge, bottom-right actions). The full CSS recipe and the `getComputedStyle(el, '::before')` browser-console check are in `seadash-nested-layered-card-pattern.md`.
