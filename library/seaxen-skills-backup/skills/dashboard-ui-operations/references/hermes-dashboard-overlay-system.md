# Hermes Dashboard Overlay System

## How features are added
- New dashboard pages (e.g. Terminal) are often delivered as **overlays** under `.hermes/overlays/<feature-name>/`
- The overlay contains:
  - `files/web/src/pages/<Page>.tsx`
  - Modified `App.tsx` (routes + nav items)
  - `reapply.sh` script that copies files into the main Hermes source and triggers build

## Why features disappear after updates
- Overlays are **not** automatically reapplied after Hermes updates or service restarts.
- The `reapply.sh` must be manually executed.
- Main source files get overwritten, leaving only the overlay directory on disk.

## Removal process (clean)
1. Delete the overlay directory: `rm -rf /root/.hermes/overlays/<feature-name>`
2. Remove `TerminalPage.tsx` (or equivalent) from `/usr/local/lib/hermes-agent/web/src/pages/`
3. Clean route + nav item + icon references from `App.tsx`
4. Remove unused icon imports

## Permanence recommendation
- For critical features, move code from overlay into the main Hermes source tree instead of relying on the overlay system.
- Overlay system is good for experimentation but fragile for long-term features.

## Related sessions
- 2026-06 session where Terminal tab was added via overlay, polished, then removed after user feedback on appearance.
