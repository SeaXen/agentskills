# Mnemosyne analytics strip: live verification and honest metrics

Use this pattern when extending a **read-only Hermes dashboard plugin** backed by Mnemosyne/SQLite and the user wants compact analytics without fake precision.

## What mattered
- Treat Mnemosyne dashboard work as **inspection UI**, not a settings UI.
- Keep analytics honest:
  - `triples_total = 0` is not automatically breakage.
  - `triples` and extracted graph/KG tables are different concepts.
  - only apply rolling time-window growth to tables with reliable timestamps.
- For this class of plugin, compact derived totals worked well:
  - `core_memory_total = working + episodic`
  - `graph_total = triples + graph_edges + memoria_kg`
  - `extracted_total = facts + preferences + instructions`

## Live verification pattern
1. Verify the raw app port and the proxy/auth front separately.
   - Example shape: raw Hermes dashboard on `:9120`, nginx/auth front on `:9119`.
2. Verify the **served plugin assets**, not just local files.
   - Check URLs like `/dashboard-plugins/<plugin>/dist/index.js` and `style.css`.
   - Search for unique markers from the new UI/state classes.
3. Verify the backend route with an **authenticated browser fetch**.
   - Unauthenticated requests can correctly return `401`.
   - In Hermes dashboard context, fetch with `X-Hermes-Session-Token` from `window.__HERMES_SESSION_TOKEN__`.
4. If frontend assets look live but backend payload is stale, restart the **dashboard process** so the plugin router remounts.
5. After the API is live, verify the DOM and then do a visual pass.
   - DOM confirms structure/state.
   - vision/screenshot confirms spacing and visual priority.

## UI pattern that worked
For a compact Mnemosyne strip, the useful order was:
- Growth controls and deltas as the dominant surface
- Extracted and Graph as smaller secondary summaries

A clean layout was:
- **left/main column:** Growth
- **right/side column:** Extracted stacked over Graph

This gave Growth visual priority while keeping the strip compact.

## Good interaction details
- Clickable growth windows: `24h`, `7d`, `30d`, `365d`, `All`
- small delta badges
- tiny percentage chips
- active filter visibility in tabs/header
- separate mini chips for tab label/count/window instead of jammed inline text

## Honest filtering rule
Do not fake time-window behavior for rows without trustworthy timestamp semantics.
- Working / episodic: okay for rolling windows
- KG/facts/triples: only filter by time if the timestamps are actually reliable
- If a section is effectively all-time, show it that way rather than pretending `24h` means something

## Browser checks that are worth doing
- confirm the page shell loads
- confirm the authenticated plugin API returns `200`
- confirm expected payload keys exist
- confirm clickable pills change active state
- confirm tab badges and header badges reflect the active window
- confirm the visual hierarchy still looks balanced after compacting

## Final polish pattern
Once the analytics strip is functionally correct, do a **conservative CSS-only polish pass** before inventing more features.

Good final-pass targets:
- top compact stat-card gap and padding
- spacing between mini-summary and analytics strip
- tiny hint-text line-height cleanup
- subtle balance tweaks for the smaller right-side stacked cards

This is the right move when the UI is already correct and the user asks for "tiny extra spacing polish" or equivalent. Keep it CSS-only, verify the served stylesheet, then confirm the result in the live browser with DOM checks plus vision.

## Row semantics to leave alone
For Mnemosyne conversation-memory rows, not every surprising value is a dashboard bug.

Normal examples:
- `veracity: unknown` for auto-saved conversation/session memories
- low assistant auto-memory importance like `0.20`

If the user asks why those look low or unfinished, verify the backing row and explain the provider semantics before changing labels, defaults, or UI warnings.

## Common pitfall
If the browser fetch still shows old payload fields after an on-disk patch, do **not** immediately re-patch the code. First compare:
- direct helper output from disk
- live authenticated browser fetch

If they differ, the dashboard is still serving an older mounted backend/router/process.
