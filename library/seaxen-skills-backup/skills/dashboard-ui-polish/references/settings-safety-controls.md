# Settings safety controls

Durable lessons from Systor Settings polish.

## Exact layout lessons
- If the user says tabs/page names belong in the system-control toolbar, move them into that exact sticky toolbar surface. Do not leave them as a second row underneath.
- For settings pages with two columns, rebalance card order to reduce first-screen scroll. A technically valid but top-heavy column layout is still wrong if the user complains about empty space or wasted scroll.
- On compact admin pages, separate structural fixes from pure visual polish:
  - structure = toolbar placement, column balance, card grouping
  - polish = tighter gaps, brighter chips, shorter labels, premium card treatment

## Settings interaction patterns that worked
- Distinguish clearly between:
  - Reset tab = restore last saved values for the active tab
  - Restore defaults = load built-in factory defaults for the active tab without auto-saving
- Show dirty state explicitly:
  - top chip like `clean` / `N changed`
  - field-level dirty highlighting
  - `unsaved` save-state chip when edits exist
- Add a `last saved` timestamp chip sourced from the real config save time, not a fake client timestamp.

## Import/export UX
- Do not make Import immediate if it overwrites a live settings file.
- Use a confirmation modal that shows the selected filename and requires an explicit confirm click.
- Export/import should return enough backend data for the UI to refresh status chips after success (for example a `saved_at` timestamp).

## Public/private settings safety
- Public-surface toggles must control real route/API behavior, not just hide nav items.
- Keep public toggles conservative: safe read-only pages only.
- If a page has private test buttons, delivery logs, or admin actions, keep those private even if the read-only page is allowed publicly.

## Verification expectations
- Browser-verify structure after changes, not just compile or DOM patch success.
- For screenshot-driven feedback, if the user says the page still looks wrong, treat the work as unfinished even if the layout is technically functional.
