# Settings toolbar, time chips, and desktop/mobile restore controls

Use this when the user says the Settings toolbar still "does not look good" even after basic compaction.

## What to do
- Do not keep status chips, tabs, and all actions in one overloaded row.
- Prefer a 2-row toolbar on desktop:
  - top row = title + state/status chips
  - bottom row = tabs on the left, grouped actions on the right
- Group actions semantically instead of a flat button wall:
  - tab/session actions
  - restart/runtime actions
  - primary save/apply actions
- When the user asks for restore-defaults beside each tab, make those controls desktop-only and keep one fallback restore button on mobile.
- Keep tab-adjacent restore buttons visually secondary (small ghost/chip buttons, not full primary buttons).

## Time chip rule
- Humanize saved-state chips: `saved just now`, `saved 2m ago`, `saved 3h ago`, etc.
- Keep the exact ISO/local timestamp in the hover/title attribute.
- Refresh the relative text periodically on the client so it stays true without a reload.

## Verification rule
- Verify the toolbar structure in the live DOM, not just by reading template code.
- Confirm:
  - two toolbar rows exist
  - desktop tab restore buttons are rendered
  - saved chip text is human-friendly
  - exact timestamp remains available on hover/title
  - the per-tab restore control still switches/applies to the intended tab

## Pitfalls
- A single mixed row of chips + tabs + all buttons looks patched, not designed.
- Putting restore-defaults only in the far-right action stack makes the association with tabs weak.
- Replacing the exact timestamp entirely is a regression; keep it available via hover/title.
- On mobile, duplicating per-tab restore buttons usually adds clutter; prefer one shared restore control there.
