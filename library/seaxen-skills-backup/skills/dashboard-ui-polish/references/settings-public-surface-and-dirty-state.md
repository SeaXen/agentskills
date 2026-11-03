# Settings public-surface and dirty-state lessons

Durable lessons from Systor Settings/UI polish work.

## Layout
- If Settings has tabs plus a sticky toolbar, put the tabs inside the same sticky control surface. A second row below the toolbar reads as wasted space and visual duplication.
- Balance columns by visible first-screen height, not by number of cards. Move taller cards to fill dead space and reduce scroll on first load.
- For security/auth areas that feel weak, split one long slab into 2–3 grouped cards such as: security core, password, session/lockout.
- When the user asks for a more premium look, shorten labels, brighten chips, and tighten vertical gaps another ~10–15%.

## Operational controls worth adding
- Dirty-state chip with changed-field count.
- Changed-field highlight styling.
- Reset active tab.
- Save active tab.
- Export/import settings.

## Public exposure
- Public page toggles must be explicit and conservative.
- Only enable safe read-only surfaces publicly (for example dashboard, alerts).
- Keep admin controls, test buttons, delivery logs, and write/destructive flows private.
- Verify with real simulated public requests/headers; navbar hiding is not enough.

## Verification
- Browser-verify final visible arrangement.
- DOM-only or geometry-only checks are insufficient when the user is correcting screenshot-driven layout details.
