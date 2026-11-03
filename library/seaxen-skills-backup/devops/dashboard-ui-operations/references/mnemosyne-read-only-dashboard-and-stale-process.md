# Mnemosyne read-only dashboard extension and stale-process verification

Use this pattern when extending a Hermes dashboard plugin that surfaces Mnemosyne or other read-only SQLite-backed memory data.

## Durable pattern

1. **Inspect the live DB schema first**
   - Check actual tables/columns/counts before shaping payloads.
   - For memory work, verify whether tables like `episodic_memory`, `triples`, `scratchpad`, `graph_edges`, or `memoria_kg` really exist and whether they are empty.
   - Empty-state text in the UI must match live counts.

2. **Treat built dashboard plugin work as two separate surfaces**
   - backend payload/runtime: `dashboard/plugin_api.py`
   - frontend bundle: `dashboard/dist/index.js` and `dashboard/dist/style.css`
   - Do not assume one side being correct proves the other is live.

3. **For read-only operator panels, prefer truth over decoration**
   - Add deeper tabs only if the backing tables really exist.
   - Show honest totals, row counts, provenance/meta, and explicit empty states.
   - Good default upgrade order: summary strip → denser stat row → row-level inspector → copy helpers.

4. **When direct HTTP probes return 401, switch to authenticated browser fetches**
   - Raw local requests can be auth-gated even on localhost.
   - Verify plugin JSON from the browser page context with the dashboard session token instead of calling the route broken.

5. **If on-disk code and live route disagree, compare on-disk execution vs browser fetch**
   - Import the plugin module directly and call the payload/helper function from disk.
   - Then fetch the same route from the authenticated browser session.
   - If those results differ, the runtime is stale even if files are patched correctly.

6. **Suspect a stray manual dashboard process before re-patching**
   - A common failure shape: edited files are correct, but the dashboard port is still held by an older manual process while the managed service cannot bind.
   - In that state the browser keeps showing old API behavior and old UI text, misleading you into thinking the patch failed.
   - Fix sequence:
     - identify the PID listening on the dashboard port
     - stop the stray process
     - start/restart the managed dashboard service
     - repeat the authenticated browser fetch

7. **For dense stat-row tuning, verify geometry, not just markup**
   - After CSS/JS compaction, inspect live DOM dimensions.
   - Check row width, row height, and actual column count to prove the cards stayed on one line.
   - If a breakpoint is too aggressive, lower it instead of piling on more CSS.

8. **For copy buttons, verify the feedback path separately from clipboard success**
   - In dashboard/browser automation contexts, clipboard APIs may fail due to permission or execution-context limits.
   - The durable thing to verify first is that the click path renders honest success/failure feedback.
   - Then improve robustness with a textarea + `execCommand('copy')` fallback or a manual-copy surface.

## Practical verification ladder

- syntax-check Python/JS after edits
- call the backend helper directly from disk
- verify service/process ownership of the live port
- fetch plugin JSON from the authenticated browser session
- click the actual tabs/actions in the browser
- for layout work, measure DOM geometry
- for copy actions, confirm visible status text even if clipboard permission blocks the write

## Good fit

This reference fits read-only Hermes dashboard tabs that expose memory stores, inventories, graph/KG tables, or other operator-facing SQLite-backed state where honesty and live verification matter more than flashy controls.
