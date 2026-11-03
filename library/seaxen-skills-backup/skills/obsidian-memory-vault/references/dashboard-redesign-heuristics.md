# Obsidian vault dashboard redesign heuristics

Use when the user says the dashboard looks bad, crowded, noisy, or needs rearrangement.

## Primary aesthetic diagnosis pattern
If the dashboard feels visually heavy, check these first before inventing new panels:

1. Secondary controls visible by default
   - Collapse low-frequency controls by default.
   - Prefer `<details>` / disclosure for legends, quick actions, and explanatory rails.
2. Stacked action rows
   - Keep one primary row visible.
   - Move utility actions into a collapsed section rather than adding another always-open row.
3. Metadata density in cards
   - Shorten to one compact line where possible.
   - Prefer `timestamp · count` over path-heavy or multi-line metadata.
   - Show fewer tags on normal cards; reserve richer badges for selected/important states.
4. Right-rail noise
   - Collapse legends/auxiliary explanations by default.
   - Make the graph view earn attention; do not compete with the content column.

## Safe redesign sequence
1. Make a plan first: identify the visually loud regions.
2. Reduce default-visible UI before adding new styling.
3. Collapse rarely used controls.
4. Trim text and metadata on repeated card components.
5. Keep primary navigation/actions visible.
6. Verify the new default state in the browser after restart.

## Concrete proven changes
- Graph legend: collapsed by default.
- Reader quick actions: moved into a collapsed disclosure.
- Note cards: shorter metadata and fewer tags.

## Verification targets
After the change, confirm:
- legend/details starts closed
- quick actions/details starts closed
- note card metadata renders as one short line
- the page feels cleaner without losing core actions

## Scope note
This is a polish/rearrangement pattern, not a full information architecture rewrite. Start with density reduction before proposing new routes or large component changes.
