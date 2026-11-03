For the **next-level cleanest pass** (type-ahead search input inside the graph area, fit-to-view button, clickable cluster labels with folder focus, cluster cohesion force, faster alpha decay, glassmorphism floating panel), see `references/graph-dashboard-cleanest-pass-2026-06.md`.

# Obsidian graph dashboard — advanced polish: focus mode, presets, search pulse

Use this after the base force-layout/minimap/saved-layout upgrade when the user wants the graph to feel more premium and navigable without moving it into the main Hermes dashboard.

## Target
- `/mnt/tb/hermes/obsidian_dashboard.py`
- real path may resolve to `/root/.hermes/obsidian_dashboard.py`

## Proven additions

1. **Focus neighborhood mode**
   - Add a toolbar toggle for `Focus mode`.
   - When enabled, keep the selected node plus its direct neighbors at full opacity.
   - Dim unrelated nodes/clusters/edges instead of deleting them.
   - This preserves context while making local structure readable.

2. **Explicit pin/unpin control**
   - Keep drag-to-pin.
   - Add a `Pin selected` / `Unpin selected` toolbar button tied to the current node.
   - Persist pin state in saved layout data.

3. **Search-highlight pulse on graph**
   - Reuse the note search query.
   - Compute matching note titles from the existing search filter.
   - On matching nodes, draw a pulsing outer ring and optionally a warm highlight color.
   - Continue animation frames while a search query is present so the pulse stays alive even after physics settles.

4. **Preset layouts**
   - Add presets such as `study`, `ops`, `memory`, `clean`.
   - Show them as pill buttons in a dedicated top-center preset bar.
   - Persist each preset separately on the backend, not just in browser storage.

5. **Zoom-based edge fade + label density control**
   - Fade link opacity based on zoom level.
   - In focus mode, heavily fade or skip unrelated edges.
   - Cap labels by zoom tier (example: ~10 / 18 / 28 / 42) to avoid label soup.
   - Always allow labels for selected / hovered / pinned / connected / search-matched nodes.

6. **Convex hull folder clusters**
   - Replace simple soft cluster discs with low-opacity hull-style cluster regions around related nodes.
   - Compute hulls in screen space after zoom/pan so the shape tracks the live graph.
   - Keep fills subtle and borders thin; do not overpower nodes/labels.
   - Fall back gracefully when a cluster has fewer than 3 nodes.

7. **Premium toolbar / legend cleanup**
   - Split graph header into status row and action row.
   - Move help and legend into compact toggles instead of persistent large overlays.
   - Keep legend collapsible and minimal by default.
   - Add search helper text and keyboard hints near the left search box.

8. **Cluster inspector in the reader panel**
   - Add a right-panel cluster inspector under the note facts.
   - Base it on the selected note's folder cluster.
   - Show member count, broken-note count, orphan count, and selected-node degree.
   - Make cluster members clickable pills that open notes directly.
   - Include a quick `Filter folder` action.

9. **Broken-link cleanup mode + orphan lane**
   - Derive per-note health client-side from the existing graph payload: incoming, outgoing, broken outgoing, broken targets, orphan flag.
   - Add a list-mode row with `All / Broken / Orphans` counts.
   - Add a dedicated `Broken cleanup` toolbar toggle that maps to the broken list mode.
   - Surface broken/orphan state in note cards and note facts.
   - Add an `Orphan lane` in the left rail with quick-open pills for isolated notes.

10. **Saved search presets**
   - Persist saved searches in browser storage keyed by vault path.
   - Save query + folder + list mode together, not just raw text.
   - Render them as compact pills with apply/remove actions.
   - Re-render saved-search active state whenever search, folder, or mode changes.

11. **Reader-side recall panels**
   - Under the main note facts, add focused recall panels instead of only raw markdown.
   - Backlinks panel: clickable inbound links + quick broken-out summary.
   - Related-notes panel: rank by shared folder, tags, and direct graph linkage.
   - Cluster recall shortcuts: quick-open sibling notes from the current cluster.
   - Important-notes surfacing: pin durable `decisions` / `issues-fixes-log` style notes into a dedicated panel.

12. **Advanced reader navigation**
   - Split backlinks into `Incoming / Outgoing` tabs.
   - For outgoing missing links, render explicit missing-target pills instead of hiding them.
   - Add a broken-link fix-action row with best-effort replacement suggestions from existing notes.
   - Add a recent-important timeline lane below the important-notes panel.
   - If true embeddings are unavailable, use token-overlap + tags + graph linkage as the semantic ranking fallback and label it honestly.

## Backend persistence pattern

Extend `/api/layout` to support a preset query string:
- `GET /api/layout?preset=study`
- `POST /api/layout?preset=study`

Recommended server payload envelope:

```json
{
  "activePreset": "study",
  "availablePresets": ["study", "ops", "memory", "clean"],
  "presets": {
    "study": {"positions": {...}, "savedAt": "..."},
    "clean": {"positions": {...}, "savedAt": "..."}
  },
  "updatedAt": "..."
}
```

Compatibility rule:
- If the layout file still contains the older single-layout shape, treat it as the `clean` preset and continue working.

## Frontend state additions

Useful state fields:
- `state.focusMode`
- `state.activePreset`
- `graphView.tick` for pulse animation timing

Useful helpers:
- `getFocusRoot()`
- `getFocusSet()`
- `getSearchMatches()`
- `renderPresetBar()`
- `selectPreset()`
- `toggleSelectedPin()`
- `toggleFocusMode()`

## Verification checklist

1. `python3 -m py_compile /mnt/tb/hermes/obsidian_dashboard.py`
2. Extract inline JS and run `node --check`
3. Restart `obsidian-vault-dashboard.service`
4. Confirm page loads on `:6065`
5. Browser-check:
   - focus mode button visible and toggles active state
   - pin/unpin selected button text changes with state
   - preset pills visible
   - selecting a preset changes active pill and loads layout
   - search query changes graph meta hit count and visible highlight pulse
6. API-check:
   - each preset returns separately from `/api/layout?preset=<name>`
   - pinned state persists per preset

## Pitfalls

- If search pulse depends on physics RAF only, the pulse dies once simulation settles. Keep RAF alive while `state.query` is non-empty.
- Do not make focus mode hide unrelated nodes entirely; dimming is better for orientation.
- If preset switching reuses a single saved blob, the feature is fake. Verify per-preset backend storage.
- When adding preset support, keep legacy layout-file compatibility so old saves do not break.
- Graph overlays get crowded fast. Put new controls in the top toolbar/preset bar, not deep inside the canvas.
