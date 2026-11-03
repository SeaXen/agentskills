# SeaDash section controls, colors, presets, and hidden app recovery

Use this reference when polishing or extending SeaDash section/app management after the compact rewrite.

## Durable lessons

### Section color UI
- Do not rely on native `<select>` controls for color selection in SeaDash's dark UI. Browser dropdown popups can render as unreadable white/black mixed UI and cannot be styled reliably.
- Prefer a custom color picker button:
  - visible color swatch
  - color name text
  - dark popover menu
  - per-choice swatches
  - active state
- Section color must be visually obvious, not just a thin left stripe. Apply color to:
  - whole section header gradient
  - section border
  - title text contrast / text shadow
  - picker button border/background

### Mode cycling must not remove controls
When a section cycles `grid -> compact -> table`, the table-mode header must keep the same operational controls:
- collapse
- section name/count
- Select
- Move all
- Pin
- color picker
- grid/compact/table mode button
- Hide all

If table rendering uses a separate function, update that function too. Otherwise users read it as the option disappearing after the third click.

### Hidden app UX
- `Close` should hide an app.
- Hidden tab/cards should show `Unhide`.
- Add a distinct `Remove` action for hidden apps that removes the hidden state without deleting the app.
- Manual-app `Delete` is separate and should remain destructive + confirmed.
- Auto/Docker/host apps should not be deleted; they should be hide/unhide only.

### Section preset UX
SeaDash should expose simple section presets in the Sections modal:
- `Default` = Host / AI / Media / Download / Admin / Docker / Manual / Danger
- `Host + Docker` = non-Docker apps under Host, Docker containers under Docker
- `No sections` = a single `Apps` group with headers visually hidden
- `Save current preset` = stores custom sections, app-section mapping, section colors, and section modes
- Saved custom presets need one-click restore and delete.

`Move` / `Move all` should include `Auto / no manual section` so the user can remove a manual section assignment and return to auto rules.

### Config/default persistence
When adding frontend-only layout keys, also add them to backend `DEFAULT_CONFIG` and example config. Otherwise config merge/reset paths can silently drop or omit the feature.

Keys added during this pattern:
- `app_sections`
- `custom_sections`
- `pinned_sections`
- `collapsed_sections`
- `section_modes`
- `section_preset`
- `custom_section_presets`
- `section_colors`
- `hidden_apps`
- `app_tags`
- `app_notes`

Include `all: slate` in `section_colors` for No sections mode.

### Service worker/cache
After substantial single-file UI changes, bump the service worker cache name. Otherwise browsers may keep serving stale shell assets even after restart.

Pattern:
```js
const CACHE_NAME = 'seadash-compact-vN';
```

### Verification probes
Minimum live browser probes after this class of change:
```js
[...document.querySelectorAll('.appSection')].map(s => ({
  id: s.dataset.section,
  title: s.querySelector('h3')?.textContent,
  color: s.querySelector('.colorPickBtn')?.textContent.trim(),
  bg: getComputedStyle(s.querySelector('.sectionHead')).backgroundImage,
}))

document.querySelectorAll('.sectionHead select').length // should be 0 for color controls
```

Also test:
- color picker opens and persists a color
- `grid -> compact -> table` keeps controls visible
- Hidden tab shows `Unhide` + `Remove`
- section presets switch to Default / Host+Docker / No sections and can restore config
- browser console has zero JS errors
