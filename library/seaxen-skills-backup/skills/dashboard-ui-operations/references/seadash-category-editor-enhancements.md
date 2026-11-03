# SeaDash category editor enhancements

Use this when the user wants richer custom category behavior in the live SeaDash monolith.

## Feature bundle that worked
- Drag-drop apps between custom categories
- Per-category background color (`bg_color`)
- Per-category sort mode:
  - `manual`
  - `alphabetical`
  - `status` (offline first)
- Collapse/expand state persistence via `localStorage`
- Per-category search/filter input with persisted values
- Pin category to top (`pinned: true`)
- Icon picker instead of raw emoji-only typing

## Data model additions
Persist under `config.layout` / `layout.columns[]`:
- `bg_color`
- `sort_mode`
- `pinned`
- `filters` object at `layout.filters`

Typical column shape:

```json
{
  "id": "layout-...",
  "title": "Pinned Ops",
  "icon": "📌",
  "accent": "blue",
  "bg_color": "#1f2937",
  "note": "Ops pinned",
  "badge": "Ops",
  "style": "highlight",
  "sort_mode": "alphabetical",
  "pinned": true,
  "refs": ["custom:big-bear-dashdot", "custom:n8n"],
  "links": []
}
```

## Important implementation detail in the SeaDash monolith
The live `index.html` can contain duplicated helper/render functions from older inline script layers. When a feature seems patched in source but the browser still behaves like the old version, verify whether the active later block is overriding the earlier one.

Concrete case from this session:
- `renderLayoutColumns()` existed more than once.
- Patching only the earlier copy was insufficient.
- The later active rescue/runtime block controlled the real UI.

Rule: if the monolith has duplicate function definitions, patch the active later path too, especially for:
- `renderLayoutColumns()`
- `toggleSection()`
- drag/drop handlers
- `saveConfig()`
- modal/editor loaders

## Better pattern for layout drag-drop
Do not try to inject layout-specific attributes into rendered HTML with brittle string replacements if you can avoid it.

More reliable pattern:
- extend `renderCard(app, idx, section, extraAttrs='')`
- extend `renderRow(app, idx, section, extraAttrs='')`
- pass layout attrs directly from `renderLayoutColumns()`
- include:
  - `data-layout-col-id`
  - `data-layout-ref`
  - `data-layout-item-kind`

This avoided failed post-render attribute injection on cards/rows.

## Persistence pattern that worked
- Category filters: `localStorage['seadash-layout-filters-v1']`
- Collapsed category ids: `localStorage['seadash-collapsed-sections-v1']`
- Keep durable category structure in `/api/config` via `config.layout`
- Keep UI-only transient view state in `localStorage`

## Save-path pitfall
When SeaDash uses `customShadow` + deduped `custom` records, `saveConfig()` must not write only `STATE.custom` back to `custom_apps`, or shadow metadata gets lost.

Use a combined save source such as:
- `[...(STATE.customShadow || []), ...(STATE.custom || [])]`

## Verification pattern
After implementing category features, verify live in browser for all of these:
1. Modal shows new controls:
   - icon picker chips
   - background color field
   - sort mode selector
   - pin toggle
2. Create two temporary categories
3. Add apps to both
4. Confirm pinned category renders first
5. Confirm per-category filter hides non-matching apps
6. Confirm collapse state survives reload
7. Confirm drag-drop moves an app from one category to another
8. Clean up temporary categories after verification if they were only test artifacts

## Operator-facing cleanup
If test categories are only for verification, remove them and restore:
- `layout.columns = []`
- `layout.hide_standard_sections = false`
- `layout.filters = {}`
- clear localStorage filter/collapse keys if they were test-only

This keeps the user’s dashboard clean after validation.