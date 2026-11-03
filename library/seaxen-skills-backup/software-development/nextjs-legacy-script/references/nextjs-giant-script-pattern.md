# Next.js Giant Inline Script — Session Notes (June 2026)

## Observed Pattern
- 969-line `page.tsx` with `const script = String.raw`... containing the entire app logic.
- All interactivity lived in vanilla JS (`$('id').onclick = fn`).
- Adding new buttons (Quick Add) required changes in two places: JSX + `bind()` function.
- `patch` repeatedly failed due to:
  - Duplicate strings inside the giant script literal.
  - Escaping issues with quotes in the tool call.

## What Worked
- Adding new helper functions (`quickAddWatch`, `setBtnLoading`) inside the script block.
- Explicit `document.querySelectorAll('[data-quick-add]')` in `bind()`.
- Removing the hero section with a large enough unique context block.

## What Failed / Was Fragile
- Short-string patches on JSX when the same markup existed inside the script string.
- Multiple attempts to add Quick Add buttons to the Watchlist card.

## Recommended Future Approach
1. For small changes: Use very long, unique `old_string` including surrounding components.
2. For anything > ~3 lines of new UI: Use `write_file` with the full updated `page.tsx`.
3. Consider extracting the script to `lib/pyhox-runtime.js` and importing it.

## User Signals
- User wants buttons to "just work" and hates when functionality is broken.
- Prefers direct action over long explanations when fixing apps.
