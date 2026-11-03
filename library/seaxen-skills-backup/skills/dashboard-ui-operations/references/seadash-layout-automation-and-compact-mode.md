# SeaDash layout automation, batch curation, and compact mode

Session-learned additions for the category/layout editor.

## What to add when the user wants heavier dashboard curation

### 1) Batch selection and drag/move
- In the category app picker, support **Shift-click range selection** on app checkboxes.
- Visually mark checked rows so the operator can see the batch before moving it.
- When dragging from a category or from the main inventory into a category, if the dragged app is already part of the checked set, treat the drag as a **batch move/add** instead of single-item drag.
- Keep single-item drag behavior when the dragged item is not in the checked set.

### 2) Duplicate handling
- Do **not** allow save-with-warning for duplicate category membership when the user asked to block duplicates.
- Show an inline warning box listing the conflicting apps and stop the save.
- Apply the same duplicate block to drag/add flows where possible, not only the manual save button.

### 3) Preset gallery
- A preset dropdown alone is weaker UX than the user expects.
- Add a **visual preset gallery** with cards that show:
  - icon
  - title
  - short note
  - badge/style hints
  - auto-rule hints when present
- Keep the dropdown for compatibility/import-export, but let clicking a preset card apply it directly.

### 4) Per-category auto-rules
Support auto-populating categories from live app metadata.

Good durable first rules:
- `monitor` → metrics / observability / monitor apps
- `public` → apps with public URL
- `offline` → stopped / exited / dead / offline apps

Implementation pattern:
- Store `auto_rules` on the category object.
- Compute **effective refs** as `manual refs + auto rule refs`.
- Use effective refs, not only manual refs, for:
  - duplicate detection
  - category rendering
  - row/card counts
- Keep manual refs editable even when auto-rules are active.

### 5) Compact dashboard mode
When the user asks for a denser dashboard:
- Add a quick-action toggle, not just a buried settings option.
- Persist `layout.compact_dashboard` in config.
- Apply a body class such as `compact-dashboard` and shrink:
  - header spacing
  - quick-action spacing
  - section margins/padding
  - card padding
  - badge/stat sizing
  - table cell padding
- Verify the compact state persists after reload and that the toggle label reflects on/off state.

## Verification checklist
- Layout modal shows preset gallery cards.
- Auto-rule chips/buttons render and toggle active state.
- Shift-click checks a range in the app picker.
- Dragging a checked app moves/adds the full checked batch.
- Duplicate category save is blocked with inline conflict list.
- Compact mode toggles on the live page and updates the button text/state.

## Pitfall
- Large monolithic `index.html` files may have older duplicated functions earlier in the file. Patch the **active later runtime copy** too, especially for drag/drop, layout modal actions, save/export flows, and window exports.