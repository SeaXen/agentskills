# Journey drawer, radial graph, and mutation gating

Session lesson:
- Clickable journey nodes work best as a radial graph with a detail drawer, not inline expanded cards.
- Keep the timeline cards clickable too so keyboard/mouse affordances match.
- When edit/delete actions are exposed, gate them on a live capability probe instead of assuming Hermes CLI mutability.
- For Hermes journey CLI, use `hermes journey --help` and the subcommand help to verify `list`, `edit`, and `delete` exist before wiring UI actions.
- Treat read-only mounts as a first-class state: disable mutation buttons, show a short reason in the drawer, and keep inspect/copy/reload actions usable.
- If a drawer opens with a raw buffer, preserve the editable content in a textarea and keep the node metadata visible beside it.

Verification pattern:
- open a journey node from the graph
- confirm the drawer title/subtitle match the selected node
- confirm graph nodes are clickable and keyboard reachable
- confirm edit/delete buttons are disabled when capability probe says read-only
- confirm browser console stays clean after open/close interactions
