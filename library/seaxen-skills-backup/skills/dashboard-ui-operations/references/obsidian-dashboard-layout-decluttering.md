# Obsidian dashboard layout decluttering

Use this pattern for monolithic/operator dashboards that have become cramped because notes, graph, controls, and reader details all compete on one screen.

## Symptoms
- notes list has scroll but too little visible height
- graph area overlaps with labels, chips, or tool controls
- reader/detail pane cannot show all information without awkward clipping
- too many always-visible controls create visual noise before the main content even loads

## Structural fixes that worked
1. Rebalance the three-panel layout before micro-tweaking colors or spacing.
   - Give the center panel enough width for the graph.
   - Cap side-panel control blocks so the main scroll regions keep usable height.
2. Convert the notes sidebar into a real vertical layout.
   - header
   - filters/tools
   - scrollable note list
3. Collapse low-frequency controls.
   - tag filters inside `<details>`
   - saved views / orphan lanes inside `<details>`
   - secondary graph actions inside a `Graph tools` disclosure tray
4. Split the reader into task-shaped tabs instead of stacking every panel.
   - Overview
   - Links
   - Recall
   - Important
5. Cap metadata/inspector height in the reader so note content still gets real space.
6. Verify with live DOM measurements, not just visual impressions.
   - inspect `clientHeight` / `scrollHeight`
   - confirm notes list, reader meta, and reader content each scroll independently

## Verification pattern
- syntax-check the monolithic file (`py_compile` or equivalent)
- restart the actual service
- load the live page
- verify tabs/disclosure trays are present
- verify `overflowY` and `clientHeight` on the intended scroll containers
- click tabs and confirm only the active section is visible

## Decision rule
If the page is still noisy after collapsing controls and tabbing the reader, stop doing minor CSS tuning. Add a focus mode or split the product into route-level views such as:
- Explore
- Reader
- Maintenance

For single-route dashboards where you do **not** want multiple pages, an effective middle ground is an internal workspace bar with explicit modes such as:
- Workbench — balanced 3-pane triage
- Explore — notes + graph
- Reader — notes + wide reader
- Recall — notes + reader with recall tab forced active

That is the durable remedy when one overloaded screen is the root problem.
