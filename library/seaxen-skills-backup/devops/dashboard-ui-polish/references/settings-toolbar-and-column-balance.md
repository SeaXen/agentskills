# Settings toolbar and column-balance pitfalls

Use for screenshot-driven dashboard settings polish.

## Durable lessons
- If the user says tabs/page names belong in the system-control toolbar, move the tab DOM into that sticky control row. Shrinking CSS while keeping a second row underneath is not enough.
- Treat explicit left/right placement requests literally. Verify that the named cards actually ended up in the requested column after deploy.
- To reduce scroll, rebalance the card distribution across columns; card reordering often matters more than padding tweaks.
- When one panel feels visually weak because it is a single long config slab, split it into purpose-grouped cards instead of only compressing spacing.

## Proven patterns
- General/settings pages:
  - left = presets/defaults/primary setup
  - right = detail tables/history/runtime
- Auth/security pages:
  - card 1 = core enable/mode/username
  - card 2 = password management
  - card 3 = session/lockout
- Notifications pages:
  - stack related delivery channels together in one column, keep history on the other side if space allows.

## Verification checklist
- Confirm tabs live inside the toolbar container, not below it.
- Confirm requested cards are in the intended columns.
- Confirm no JS errors after the structural move.
- If screenshot vision fails, still verify with live DOM structure and browser checks before claiming success.
