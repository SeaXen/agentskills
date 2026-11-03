# Obsidian dashboard — scan cache, idle graph, loadAll (2026-06)

**File:** `/mnt/tb/hermes/obsidian_dashboard.py`  
**When:** User asks if `:6065` is fast / low CPU-RAM, or after perf work on the vault dashboard.

## Server: graph scan cache

- Module cache `_GRAPH_SCAN_CACHE` + fingerprint `_vault_latest_mtime()` (max mtime of all `*.md` under vault).
- `scan_notes(force=False)` returns cached payload when fingerprint unchanged.
- `invalidate_graph_scan_cache()` after writes that bypass scan (e.g. `POST /api/quick-capture`).
- **Symptom without cache:** every `loadAll` hits full disk read twice (`/api/graph` + `/api/memory-health` each call `scan_notes()`); CPU spikes on Refresh.

**Probe (ad-hoc):**

```bash
python3 -c "
import time, urllib.request
t0=time.time(); urllib.request.urlopen('http://127.0.0.1:6065/api/graph').read()
t1=time.time(); urllib.request.urlopen('http://127.0.0.1:6065/api/graph').read()
t2=time.time()
print('cold_ms', int((t1-t0)*1000), 'warm_ms', int((t2-t1)*1000))
"
```

Expect warm ≪ cold on ~75-note vault after restart with new code.

## Client: browser CPU

- **`pauseGraphSimulation()`** when active tab is not `notes` or `graph` (Home, Learn, Capture, etc.).
- **`reheatSimulation`** returns early if graph page not active.
- **`loadAll`:** parallel `fetch` graph + health; single-flight via `window.__loadAllInflight`.

## Baseline expectations (honest)

- Python process ~**30–40 MB RSS** idle on DietPi-class host is normal.
- **Premium** theme: slightly more GPU (blur/gradients); negligible vs graph sim.
- No auto-refresh polling — user Refresh is the main load event.

## Restart / deploy new Python

- Prefer `systemctl --user restart obsidian-vault-dashboard` from a shell **outside** the Hermes gateway (in-gateway `systemctl restart` may be blocked).
- Fallback: `pkill -f '/mnt/tb/hermes/obsidian_dashboard.py'`; unit `Restart=always` respawns.
- Do **not** start a second `python3 obsidian_dashboard.py` while systemd holds :6065.

## Related

- Note links / themes: `obsidian-dashboard-note-links.md`, `dashboard-dual-theme-2026-06.md`