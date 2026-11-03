# FastAPI dashboard multi-tab expansion pattern

Use when adding several analytics tabs/pages to a FastAPI + static JS dashboard while preserving fast startup and low CPU/RAM.

## Durable lessons

1. **Checkpoint first**
   - Create a tarball backup excluding `.git`, caches, and large mutable DB files.
   - Confirm `git push origin <branch>` is up to date before wide UI/API edits.
   - Keep runtime DB mirrors like `data/*.db` untracked unless the project intentionally version-controls fixtures.

2. **Backend modules must be copied into the image**
   - If a new Python collector module is added, update `Dockerfile` `COPY ...` immediately.
   - Rebuild can appear successful while the app fails at runtime from `ModuleNotFoundError` if the new module is omitted.
   - Verify with live `curl /api/healthz` after rebuild, not just `docker compose up` output.

3. **Avoid global JS function name collisions**
   - Monolithic dashboards often already have functions like `renderCosts()` for an existing Search section.
   - New top-level pages should use unique names or rename legacy page-section renderers, e.g. `renderSearchCosts()` vs new `renderCosts()`.
   - Search for duplicate function names before finalizing: `function renderX` and `X()` call sites.

4. **Hidden tabs must not refresh heavy charts**
   - Global timers should guard on `currentPage` before running chart-heavy work.
   - Pattern:
     ```js
     async function refreshCore() {
       if (currentPage !== 'analytics') return;
       // existing heavy work
     }
     async function refreshHeavy() {
       if (currentPage !== 'analytics') return;
       // expensive charts/tables
     }
     async function refreshCurrentPage() {
       if (currentPage === 'home') return renderHome(true);
       if (currentPage === 'analytics') return refreshAll();
       // page-specific refreshes
     }
     ```
   - Global Refresh should refresh the active page only, not every dashboard surface.

5. **Use cached, lazy collectors for new pages**
   - Add small cached read-only collector functions with a short TTL (30–60s).
   - Use `fresh=1` for explicit refresh buttons.
   - Initial page should be a light Home/Command Center; do not eagerly render Search/Providers/long tables at boot.

6. **Drawer interactions need live browser verification**
   - If a drawer opens via generated `onclick`, verify both the click path and direct function call.
   - Add visible error fallbacks inside async drawers:
     ```js
     try { ... } catch (e) {
       console.error(e);
       body.innerHTML = '<div class="empty-state">Detail failed: ' + escapeHtml(e.message || String(e)) + '</div>';
     }
     ```
   - Browser automation can retain prior empty exception entries; install temporary `window.onerror` / `unhandledrejection` hooks if console output is ambiguous.

7. **Verification checklist**
   - `python3 -m py_compile app.py <collectors>.py`
   - `node --check static/js/dashboard.js`
   - live `curl` all new endpoints
   - live `curl /` for cache-busted JS version
   - browser smoke test initial Home + each new tab + any drawer
   - `git diff` secret scan before commit
