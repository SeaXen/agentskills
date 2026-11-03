# Standalone Obsidian graph dashboard patterns

Use this when a vault graph or knowledge-map UI lives as a single Python/HTML/JS service rather than a normal built frontend.

## Why keep it standalone
- If the main dashboard already carries chat, PTY, websocket, or other operator-heavy runtime load, keep a canvas-heavy animated graph as a separate service.
- This reduces render jank, lowers regression risk, and makes restart/debug cycles simpler.
- Prefer linking to the graph app over embedding it into the main dashboard unless the user explicitly wants tight integration and accepts higher fragility.

## Implementation patterns that worked
- Single-file service can still support meaningful polish:
  - smoother animated force layout
  - minimap with viewport box
  - drag-to-pin nodes
  - collision tuning and label overlap avoidance
  - folder-colored clusters
  - curved links
- If users want layout persistence across browsers/devices, localStorage is not enough. Add a server-backed shared layout file plus API routes.
- Save shared layouts atomically with a temp file + replace pattern to reduce corruption risk.
- Store shared layout close to the vault, e.g. `.obsidian-dashboard-layout.json`, so it travels with the vault context.

## Verification pattern
Do all three:
1. syntax check host language and embedded JS
2. restart the real service and verify listener/process state
3. inspect the live browser page visually and via DOM/console/API

Concrete checks:
- `python -m py_compile` for the service file
- extract inline JS and run `node --check` if the page script is embedded in Python/HTML
- confirm service is active and listening on expected port
- inspect browser for expected controls/text/state
- call the layout API and confirm saved positions exist on disk
- refresh and verify persistence still holds

## Graph-specific pitfall
- Synthetic browser events may fail to prove drag behavior on custom canvas/minimap interactions. If this happens, verify the underlying pan/transform function directly in page context and combine that with visual/manual confirmation instead of falsely declaring the feature broken.

## Operational note
- When the same file is reachable from two paths (real path vs mounted path), verify with a real file comparison before claiming they are different copies. This matters for edit target selection and for telling the user where the live artifact actually lives.
