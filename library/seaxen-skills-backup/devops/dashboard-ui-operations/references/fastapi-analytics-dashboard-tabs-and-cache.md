# FastAPI analytics dashboard tabs + cache pattern

Use when extending a self-hosted FastAPI dashboard with many analytics tabs over SQLite/log data.

## Pattern

1. **Checkpoint first**
   - Create a tarball backup excluding `.git`, DB files, caches, and generated artifacts.
   - Confirm current branch and push status before broad UI/backend work.
   - Keep local SQLite mirrors such as `data/*.db` untracked unless the repo explicitly tracks fixtures.

2. **Backend modules must be packaged**
   - If adding a new Python module imported by `app.py`, update the Dockerfile `COPY` list.
   - Static files may be volume-mounted, but backend modules are baked into the image and require rebuild.
   - Verification signal: container may build/start logs deceptively, but `/api/healthz` or `curl` will fail if import-time `ModuleNotFoundError` crashes uvicorn.

3. **Fast tab expansion without startup bloat**
   - Make a lightweight Home/Overview page the default initial page.
   - Do not render heavy historical Search/Analytics pages on first load.
   - In `switchPage(page)`, lazy-load only the selected tab's data.
   - Global refresh should call `refreshCurrentPage()` instead of refreshing every page/dashboard.

4. **Cheap aggregate endpoints**
   - Add per-tab cached APIs such as `/api/<tab>/dashboard?days=30&fresh=1`.
   - Use a short TTL (30–60s) for dashboards over SQLite/logs.
   - Keep endpoint payloads aggregated and bounded: top N rows, compact timelines, no raw message dumps.
   - Run expensive scans with `asyncio.to_thread(...)` in FastAPI routes.

5. **Chart memory discipline**
   - Keep chart handles in a tab-level state object.
   - Destroy old Chart.js instances before rendering new ones.
   - Avoid hidden-tab chart work; render charts only after tab activation.

6. **Verification**
   - `python3 -m py_compile app.py <new_modules>.py`
   - `node --check static/js/dashboard.js`
   - Docker rebuild and `curl /api/healthz`
   - Curl every new endpoint and check returned keys/totals.
   - Browser smoke test cache-busted URL; check console for JS errors.

## Common pitfall

Adding `aceroute_extra_pages.py`-style backend helpers and importing them in `app.py` works locally, but the Docker image can crash until the Dockerfile copies the new file. Always update packaging in the same commit as the import.
