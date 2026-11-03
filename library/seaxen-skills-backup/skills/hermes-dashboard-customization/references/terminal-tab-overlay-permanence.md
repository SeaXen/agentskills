# Hermes Dashboard Terminal Tab — Overlay Permanence

## Core Lesson
The Terminal tab (added 2026-06-03) was implemented as an **overlay** (`hermes-dashboard-terminal`). Overlays live in `.hermes/overlays/<name>/` and are copied into the main source via `reapply.sh`.

## Why It Disappears After Updates
- Hermes updates frequently refresh `/usr/local/lib/hermes-agent/web/src/`.
- The overlay directory and files remain on disk but are **not automatically reapplied**.
- `reapply.sh` must be run manually after updates.
- Result: TerminalPage.tsx and route changes are present but not active in the running dashboard.

## Overlay vs Permanent Integration
| Approach       | Survives Updates | Maintenance Burden | Recommendation |
|----------------|------------------|--------------------|----------------|
| Overlay        | No               | High (manual reapply) | Only for experiments |
| Main source    | Yes              | Low                | Preferred for production features |

## Recommended Path for Permanence
1. Copy `TerminalPage.tsx` + `App.tsx` changes directly into `/usr/local/lib/hermes-agent/web/src/`.
2. Register the `/terminal` route in the main router.
3. Remove or deprecate the overlay once integrated.
4. The feature then becomes part of the core build.

## Verification After Restore
- Run `reapply.sh` (or manual copy + `npm run build`).
- Restart `hermes-dashboard.service`.
- Confirm `/terminal` route returns the xterm.js UI with session token.
- Browser verification: tab appears in sidebar and survives page reload.

## Pitfall
Never rely on overlays for features the user expects to persist after Hermes updates. If permanence is requested, treat it as a main-source integration task, not an overlay task.