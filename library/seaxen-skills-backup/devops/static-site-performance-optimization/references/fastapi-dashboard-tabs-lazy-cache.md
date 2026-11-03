# FastAPI dashboard tab performance pattern

Session learning from extending a monolithic FastAPI/Chart.js dashboard with additional analytics tabs.

## Durable pattern

- **Default to a lightweight Home page.** Avoid loading a legacy heavy analytics page on initial visit.
- **Lazy render tabs.** `switchPage(page)` should fetch/render only the active tab.
- **Current-page refresh.** The global refresh button should call `refreshCurrentPage()`, not refresh every tab/chart.
- **Short TTL aggregate APIs.** Use cached `/api/<tab>/dashboard?days=N&fresh=1` endpoints with bounded payloads rather than raw large lists.
- **Chart cleanup.** Destroy old Chart.js instances before rerender to prevent memory leaks.
- **Package new backend modules.** If `app.py` imports a new helper module, update the Dockerfile `COPY` list; static volume mounts do not help Python imports inside the image.

## Implementation checklist

1. Create/verify a backup and push current branch before wide page work.
2. Add backend collectors as bounded aggregate endpoints, not full-table dumps.
3. Use `fresh=1` only for explicit refresh buttons; ordinary tab loads should use cache.
4. Search the monolithic JS for duplicate global renderer names before adding a new page renderer. Rename legacy section functions when needed, e.g. `renderSearchCosts()` vs top-level `renderCosts()`.
5. Guard background timers by active page:

```js
async function refreshCore() {
  if (currentPage !== 'analytics') return;
  // analytics-only work
}
async function refreshHeavy() {
  if (currentPage !== 'analytics') return;
  // expensive charts/tables
}
async function refreshCurrentPage() {
  if (currentPage === 'home') return renderHome(true);
  if (currentPage === 'analytics') return refreshAll();
  if (currentPage === 'models') return renderModels(true);
}
```

6. For async drawers, add a visible fallback and verify both generated click handlers and direct function calls:

```js
try {
  // fetch detail + render drawer
} catch (e) {
  console.error(e);
  body.innerHTML = '<div class="empty-state">Detail failed: ' + escapeHtml(e.message || String(e)) + '</div>';
}
```

## Verification checklist

```bash
python3 -m py_compile app.py <new_module>.py
node --check static/js/dashboard.js
docker compose up -d --build --force-recreate
curl -sS http://127.0.0.1:<port>/api/healthz
curl -sS http://127.0.0.1:<port>/api/<new>/dashboard | python3 -m json.tool >/dev/null
curl -sS http://127.0.0.1:<port>/ | grep 'dashboard.js?v='
```

Browser smoke-test the cache-busted URL, each new tab, and drawer interactions. If browser-console reports blank/stale errors, install temporary `window.onerror` and `unhandledrejection` hooks to distinguish real new failures from retained tool buffers.
