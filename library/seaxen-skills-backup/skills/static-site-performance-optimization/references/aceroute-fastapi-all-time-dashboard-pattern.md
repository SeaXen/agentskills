# AceRoute FastAPI all-time dashboard performance pattern

Use for dense operator dashboards over SQLite / Hermes state.db where users want default all-time views without lag.

## Pattern

1. **True all-time sentinel**
   - Use a large sentinel like `36500` days.
   - Backend should expose `window_mode: all` and not fake all-time by clamping to 365 unless doing an emergency fallback.

2. **Warm heavy collectors at startup**
   - During FastAPI startup, precompute the heavy all-time dashboard collectors before the app is considered ready.
   - Good warm targets: home, ops, sessions, requests, messages, models.
   - This removes the "first page hit after restart is slow" problem.

3. **Prefer SQL aggregates, not Python full-row scans**
   - Totals, by-source, by-model, and timelines should be grouped in SQL.
   - Python should format the already-aggregated result, not sum thousands of rows in loops.

4. **Cap timeline size twice**
   - Server: cap grouped timeline rows (example: 400 days max).
   - Client: downsample again for Chart.js (example: ~96 points).
   - This keeps all-time charts responsive and reduces RAM / layout thrash.

5. **Light first table loads**
   - Requests/messages initial list loads do not need 100-120 rows.
   - Start around 80 rows unless the page proves it needs more.

6. **Short client cache for repeat opens**
   - Cache dashboard+list payloads for around 60s keyed by page filters/range.
   - Invalidate those caches when the global duration changes.

7. **Abort stale fetches**
   - Use `AbortController` so rapid page switches cancel old requests instead of letting them race and waste work.

## Observed impact in AceRoute

After startup warming and SQL-first aggregation, all-time endpoints dropped into double-digit milliseconds for most dashboard pages, with requests/messages also becoming fast after warm.

## Pitfalls

- If startup warming runs in background tasks only, health may go green before the heavy all-time caches are ready; first user hit can still be slow.
- If all-time timelines are uncapped, Chart.js becomes the bottleneck even when SQL is fast.
- If the UI keeps stale 30d fallbacks, one page can silently ignore the global all-time selector.
