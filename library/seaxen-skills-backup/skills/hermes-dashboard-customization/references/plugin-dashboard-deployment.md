# Plugin Dashboard Deployment Pattern

## Overview

Some Hermes plugins (e.g., `hermes-telemetry`) ship with their own standalone Python dashboard servers (`serve.py`). These are NOT the built-in Hermes dashboard — they are separate HTTP services that read the plugin's SQLite database. Deploy them as systemd services on dedicated ports.

## hermes-telemetry Dashboard Deployment

### 1. Install & Enable Plugin

```bash
hermes plugins install nujovich/hermes-telemetry
hermes plugins enable hermes-telemetry
# Restart gateway FROM OUTSIDE the gateway process:
hermes gateway restart
```

### 2. Systemd Service Template

```ini
# /etc/systemd/system/hermes-telemetry-dashboard.service
[Unit]
Description=Hermes Telemetry Dashboard
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/.hermes/plugins/hermes-telemetry/dashboard
# Wait for telemetry DB to exist (created after gateway restart + first session)
ExecStartPre=/bin/bash -c 'while [ ! -f /root/.hermes/telemetry/telemetry.db ]; do sleep 2; done'
ExecStart=/usr/bin/python3 serve.py --host 0.0.0.0 --port 8009
Restart=on-failure
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

**Key points:**
- `ExecStartPre` waits for `/root/.hermes/telemetry/telemetry.db` — the dashboard crashes if DB doesn't exist
- `--host 0.0.0.0` enables LAN access (default is 127.0.0.1 only)
- `--port` explicitly set to avoid auto-increment surprises
- Service auto-starts on boot (`systemctl enable`)

### 3. Enable & Start

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now hermes-telemetry-dashboard
```

### 4. Verify

```bash
# Local check
curl -s http://127.0.0.1:8009/api/summary?hours=24 | jq '.runs.total_runs'

# LAN check
curl -s http://192.168.0.222:8009/ | head -5

# Service status
sudo systemctl status hermes-telemetry-dashboard
```

---

## Extending Time Range Options (90 days / All Time)

The stock dashboard has 3 options: 24h, 7d, 30d. To add 90d and All Time:

### HTML (index.html) — Add Dropdown Options

```html
<select id="windowSelect" onchange="loadAll()">
  <option value="24">Last 24h</option>
  <option value="168" selected>Last 7 days</option>
  <option value="720">Last 30 days</option>
  <option value="2160">Last 90 days</option>      <!-- 90 * 24 = 2160 hours -->
  <option value="0">All time</option>              <!-- 0 = no filter -->
</select>
```

### Python API (serve.py) — Helper Functions

```python
def _since_clause(window_hours):
    """Return SQL WHERE clause for runs.started_at. 0 = all time (no filter)."""
    wh = int(window_hours)
    if wh == 0:
        return "1=1"
    return f"started_at >= datetime('now', '-{wh} hours')"

def _since_clause_ts(window_hours):
    """Return SQL WHERE clause for llm_calls.ts. 0 = all time (no filter)."""
    wh = int(window_hours)
    if wh == 0:
        return "1=1"
    return f"ts >= datetime('now', '-{wh} hours')"
```

### Use in API Handlers

```python
def api_summary(window_hours=24):
    since_clause = _since_clause(window_hours)
    since_clause_ts = _since_clause_ts(window_hours)

    runs = _one(f"""
        SELECT ... FROM runs WHERE {since_clause}
    """)

    llm = _one(f"""
        SELECT ... FROM llm_calls WHERE {since_clause_ts}
    """)

    top_tools = _rows(f"""
        SELECT ... FROM tool_calls tc
        JOIN runs r ON tc.session_id = r.session_id
        WHERE {since_clause.replace("started_at", "r.started_at")}
        GROUP BY tool_name ORDER BY calls DESC LIMIT 10
    """)

    # Daily cost chart: dynamic window based on selection
    daily_window = int(window_hours)
    if daily_window == 0:
        daily_window = 2160  # default 90 days for "all time"
    daily_cost = _rows(f"""
        SELECT DATE(started_at) AS day, ROUND(SUM(cost_usd),4) AS cost, COUNT(*) AS runs
        FROM runs
        WHERE started_at >= datetime('now', '-{int(daily_window/24)} days')
        GROUP BY DATE(started_at) ORDER BY day
    """)

def api_cron(window_hours=168):
    since_clause = _since_clause(window_hours)
    return _rows(f"""
        SELECT ... FROM runs
        WHERE cron_job_id IS NOT NULL AND {since_clause}
        GROUP BY cron_job_id ORDER BY cost_usd DESC
    """)

def api_providers(window_hours=24):
    since_clause_ts = _since_clause_ts(window_hours)
    return _rows(f"""
        SELECT ... FROM llm_calls WHERE {since_clause_ts}
        GROUP BY provider ORDER BY total_calls DESC
    """)
```

---

## PR #22 Improvements (Consolidated Helpers, Unbounded Chart, Budget Editor)

### 1. Consolidated Time Clause Helpers

**Before:** Two duplicate functions `_since_clause` and `_since_clause_ts` — fragile `.replace()` hack in SQL.

**After:** Single parameterized helper:

```python
def _since_clause(window_hours, col="started_at"):
    """Return SQL WHERE clause for time window. 0 = all time (no filter).
    Args:
        window_hours: 0 = all time (no filter), otherwise hours back
        col: column name (default 'started_at', use 'ts' for llm_calls)
    """
    wh = int(window_hours)
    if wh == 0:
        return "1=1"
    return f"{col} >= datetime('now', '-{wh} hours')"

# Use in handlers:
since_clause = _since_clause(window_hours, "started_at")
since_clause_ts = _since_clause(window_hours, "ts")
top_tools_where = _since_clause(window_hours, "r.started_at")  # no .replace() hack
```

### 2. Integer Division Fix

**Before:** `int(daily_window/24)` — truncates incorrectly for non-multiples of 24 (e.g., 47h → 1 day instead of 2).

**After:** `daily_window // 24` — proper integer division.

### 3. Unbounded Chart for "All Time"

**Before:** Chart capped at 90 days even when user selected "All time" — summary cards showed all-time totals but chart didn't match.

**After:** For `hours=0`, query without WHERE clause — chart matches summary totals.

```python
if daily_window == 0:
    daily_cost = _rows("""
        SELECT DATE(started_at) AS day, ROUND(SUM(cost_usd),4) AS cost, COUNT(*) AS runs
        FROM runs
        GROUP BY DATE(started_at) ORDER BY day
    """)
else:
    daily_cost = _rows(f"""
        SELECT DATE(started_at) AS day, ROUND(SUM(cost_usd),4) AS cost, COUNT(*) AS runs
        FROM runs
        WHERE started_at >= datetime('now', '-{daily_window // 24} days')
        GROUP BY DATE(started_at) ORDER BY day
    """)
```

### 4. Dynamic Chart Titles

```javascript
let dailyTitle;
switch (hours) {
  case '24': dailyTitle = 'Daily Cost (last 24h)'; break;
  case '168': dailyTitle = 'Daily Cost (last 7 days)'; break;
  case '720': dailyTitle = 'Daily Cost (last 30 days)'; break;
  case '2160': dailyTitle = 'Daily Cost (last 90 days)'; break;
  case '0': dailyTitle = 'Daily Cost (all time)'; break;
  default: dailyTitle = 'Daily Cost';
}
html += renderChartCard('dailyCost', dailyTitle, 'chart-daily');
```

### 5. Fixed `/api/providers` Time Window

**Before:** Handler ignored `hours` param, hardcoded to 24h.

**After:**
```python
if path == "/api/providers":
    qs = parse_qs(parsed.query)
    return self._json(api_providers(int(qs.get("hours", [24])[0])))
```
And in `index.html`: `fetchJSON(\`/api/providers?hours=${hours}\`)`

---

## Budget Editor Modal (Dashboard)

The stock dashboard is read-only for budgets. To add an editor:

### 1. Backend — POST `/api/budget` Endpoint

```python
def api_budget_update(payload):
    """Update budget.yaml from POST payload. Returns updated budget status or error."""
    budget_path = DB_PATH.parent / "budget.yaml"
    if not budget_path.exists():
        return {"enabled": False, "error": "budget.yaml not found"}
    try:
        import yaml
    except ImportError:
        return {"enabled": False, "error": "PyYAML not installed"}
    try:
        cfg = yaml.safe_load(budget_path.read_text()) or {}
    except Exception as e:
        return {"enabled": False, "error": f"Failed to parse budget.yaml: {e}"}

    scope = payload.get("scope", "global")
    window = payload.get("window", "daily")
    limit_usd = payload.get("limit_usd")
    if limit_usd is None:
        return {"enabled": False, "error": "limit_usd is required"}
    try:
        limit_usd = float(limit_usd)
    except (ValueError, TypeError):
        return {"enabled": False, "error": "limit_usd must be a number"}
    if limit_usd < 0:
        return {"enabled": False, "error": "limit_usd must be >= 0"}

    if "budgets" not in cfg:
        cfg["budgets"] = {}
    if scope not in cfg["budgets"]:
        cfg["budgets"][scope] = {}
    cfg["budgets"][scope][f"{window}_usd"] = limit_usd

    # Optional thresholds
    if "soft_pct" in payload:
        try:
            soft = float(payload["soft_pct"])
            if 0 <= soft <= 1:
                cfg.setdefault("thresholds", {})["soft_pct"] = soft
        except (ValueError, TypeError):
            pass
    if "hard_pct" in payload:
        try:
            hard = float(payload["hard_pct"])
            if 0 <= hard <= 1:
                cfg.setdefault("thresholds", {})["hard_pct"] = hard
        except (ValueError, TypeError):
            pass
    if "on_estimated_mode" in payload:
        mode = payload["on_estimated_mode"]
        if mode in ("warn_only", "enforce"):
            cfg.setdefault("on_estimated", {})["mode"] = mode

    try:
        budget_path.write_text(yaml.safe_dump(cfg, default_flow_style=False, sort_keys=False))
    except Exception as e:
        return {"enabled": False, "error": f"Failed to write budget.yaml: {e}"}

    return api_budget()  # return updated status
```

In `Handler` class:
```python
def do_POST(self):
    parsed = urlparse(self.path)
    path = parsed.path.rstrip("/") or "/"
    if path == "/api/budget":
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")
        try:
            payload = json.loads(body) if body else {}
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")
            return
        result = api_budget_update(payload)
        return self._json(result)
    self.send_response(404)
    self.end_headers()
    self.wfile.write(b"Not Found")
```

### 2. Frontend — Modal Form (index.html)

**Add Edit button to each budget row:**
```javascript
html += `<div class="budget-item">
  <div class="info"><span>${s.scope}</span><span>${fmtCost(s.spent)} / ${fmtCost(s.limit)} (${s.pct}%)</span></div>
  <div class="bar-bg"><div class="bar-fill ${cls}" style="width:${Math.min(s.pct, 100)}%"></div></div>
  <button class="budget-edit-btn" onclick="openBudgetModal('${s.scope}')">Edit</button>
</div>`;
```

**Modal HTML (before </script>):**
```html
<div class="modal-overlay" id="budgetModal" onclick="if(event.target===this) closeBudgetModal()">
  <div class="modal" onclick="event.stopPropagation()">
    <h3>Edit Budget</h3>
    <div class="form-group"><label>Scope</label>
      <select id="budgetScope">
        <option value="global">Global</option>
        <option value="per_cron_job">Per Cron Job (default)</option>
        <option value="per_sender">Per Sender</option>
      </select>
    </div>
    <div class="form-group"><label>Window</label>
      <select id="budgetWindow"><option value="daily">Daily</option><option value="monthly">Monthly</option></select>
    </div>
    <div class="form-group"><label>Limit (USD)</label>
      <input type="number" id="budgetLimit" step="0.01" min="0" placeholder="e.g. 5.00">
    </div>
    <div class="form-row">
      <div class="form-group"><label>Soft threshold (%)</label><input type="number" id="budgetSoftPct" step="0.01" min="0" max="1" placeholder="0.80"></div>
      <div class="form-group"><label>Hard threshold (%)</label><input type="number" id="budgetHardPct" step="0.01" min="0" max="1" placeholder="1.00"></div>
    </div>
    <div class="form-group"><label>On estimated data</label>
      <select id="budgetOnEstimated">
        <option value="warn_only">Warn only (degrade hard to soft)</option>
        <option value="enforce">Enforce hard limits</option>
      </select>
    </div>
    <div class="modal-error" id="budgetModalError"></div>
    <div class="modal-actions">
      <button class="modal-btn cancel" onclick="closeBudgetModal()">Cancel</button>
      <button class="modal-btn save" onclick="saveBudget()">Save</button>
    </div>
  </div>
</div>
```

**Modal CSS:**
```css
.budget-edit-btn { background: #21262d; color: #58a6ff; border: 1px solid #30363d; border-radius: 4px; padding: 2px 8px; font-size: 11px; cursor: pointer; margin-left: 8px; }
.budget-edit-btn:hover { background: #30363d; }
.modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.7); display: none; align-items: center; justify-content: center; z-index: 1000; }
.modal-overlay.open { display: flex; }
.modal { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 24px; width: 100%; max-width: 400px; margin: 16px; }
.modal h3 { color: #e6edf3; margin-bottom: 16px; font-size: 16px; }
.modal .form-group { margin-bottom: 16px; }
.modal label { display: block; color: #8b949e; font-size: 12px; margin-bottom: 4px; }
.modal select, .modal input { width: 100%; background: #21262d; color: #c9d1d9; border: 1px solid #30363d; border-radius: 6px; padding: 8px 12px; font-size: 13px; box-sizing: border-box; }
.modal select:focus, .modal.input:focus { outline: none; border-color: #58a6ff; }
.modal .form-row { display: flex; gap: 8px; }
.modal .form-row .form-group { flex: 1; }
.modal-actions { display: flex; justify-content: flex-end; gap: 8px; margin-top: 24px; }
.modal-btn { padding: 8px 16px; border-radius: 6px; font-size: 13px; cursor: pointer; border: 1px solid #30363d; }
.modal-btn.cancel { background: #21262d; color: #c9d1d9; }
.modal-btn.cancel:hover { background: #30363d; }
.modal-btn.save { background: #238636; color: #fff; }
.modal-btn.save:hover { background: #2ea043; }
.modal-error { color: #f85149; font-size: 12px; margin-top: 8px; display: none; }
.modal-error.show { display: block; }
```

**Modal JS:**
```javascript
let currentBudgetScope = 'global';
function openBudgetModal(scope) {
  currentBudgetScope = scope;
  $('#budgetScope').value = scope;
  $('#budgetModalError').classList.remove('show');
  $('#budgetModalError').textContent = '';
  $('#budgetWindow').value = 'daily';
  $('#budgetLimit').value = '';
  $('#budgetSoftPct').value = '';
  $('#budgetHardPct').value = '';
  $('#budgetOnEstimated').value = 'warn_only';
  $('#budgetModal').classList.add('open');
}
function closeBudgetModal() { $('#budgetModal').classList.remove('open'); }
async function saveBudget() {
  const payload = {
    scope: $('#budgetScope').value,
    window: $('#budgetWindow').value,
    limit_usd: parseFloat($('#budgetLimit').value),
    soft_pct: parseFloat($('#budgetSoftPct').value) || undefined,
    hard_pct: parseFloat($('#budgetHardPct').value) || undefined,
    on_estimated_mode: $('#budgetOnEstimated').value
  };
  if (isNaN(payload.limit_usd)) { showModalError('Limit (USD) is required'); return; }
  $('#budgetModalError').classList.remove('show');
  try {
    const response = await fetch('/api/budget', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    const result = await response.json();
    if (result.error) { showModalError(result.error); return; }
    closeBudgetModal(); loadAll();
  } catch (err) { showModalError('Request failed: ' + err.message); }
}
function showModalError(msg) { const el = $('#budgetModalError'); el.textContent = msg; el.classList.add('show'); }
```

### Usage
```bash
# Set global daily to $10
curl -X POST /api/budget -H 'Content-Type: application/json' -d '{"scope":"global","window":"daily","limit_usd":10}'

# Set monthly with custom thresholds
curl -X POST /api/budget -H 'Content-Type: application/json' -d '{"scope":"global","window":"monthly","limit_usd":200,"soft_pct":0.7,"hard_pct":0.95,"on_estimated_mode":"enforce"}'
```

---

## Budget Config Hot-Reload via File Watcher

Plugin-level `watchdog` watcher on `budget.yaml` eliminates manual `/budget set` or gateway restart after dashboard edits.

### Plugin Changes (budget.py)

```python
# Add to budget.py
_budget_observer = None
_budget_watcher_started = False

def start_budget_watcher() -> None:
    """Start a background file watcher on budget.yaml to auto-reload config on changes."""
    global _budget_observer, _budget_watcher_started
    if _budget_watcher_started:
        return
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler, FileModifiedEvent
    except Exception as exc:
        logger.debug("budget watcher unavailable (watchdog not installed): %s", exc)
        return

    class BudgetConfigHandler(FileSystemEventHandler):
        def on_modified(self, event: FileModifiedEvent) -> None:
            if not event.is_directory and event.src_path.endswith("budget.yaml"):
                logger.info("budget.yaml modified — hot-reloading budget config")
                reload_config()

    path = _budget_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    _budget_observer = Observer()
    _budget_observer.schedule(BudgetConfigHandler(), str(path.parent), recursive=False)
    _budget_observer.daemon = True
    _budget_observer.start()
    _budget_watcher_started = True
    logger.info("Budget file watcher started on %s", path)

def stop_budget_watcher() -> None:
    """Stop the budget file watcher (for cleanup/tests)."""
    global _budget_observer, _budget_watcher_started
    if _budget_observer:
        _budget_observer.stop()
        _budget_observer.join(timeout=2)
        _budget_observer = None
    _budget_watcher_started = False
```

### Plugin __init__.py — Start Watcher on Load

```python
def register(ctx) -> None:
    _setup_log_file()
    tele_log = logging.getLogger("hermes_telemetry")

    from . import budget, db, pricing, setup, stats

    # Start budget file watcher (hot-reload on budget.yaml changes)
    budget.start_budget_watcher()

    # Auto-refresh pricing from remote sources (once per 24h)
    _try_pricing_refresh(tele_log)
```

### pyproject.toml — Add Dependency

```toml
dependencies = [
    "watchdog>=3.0",  # budget.yaml file watcher for hot-reload
]
```

### Flow

```
Dashboard Edit → POST /api/budget → budget.yaml modified 
    → watchdog detects change → budget.reload_config() 
    → plugin immediately enforces new limits
```

**No more manual `/budget set` or gateway restart needed** after dashboard edit.

---

## Common Pitfalls

| Issue | Cause | Fix |
|-------|-------|-----|
| Dashboard 500 on `/api/summary?hours=0` | SQL `datetime('now', '-0 hours')` invalid | Use helper: `1=1` when hours=0 |
| `TypeError: unsupported operand / for str` | `window_hours` passed as string from query param | `int(window_hours)` at start of each handler |
| `sqlite3.OperationalError: near ".1": syntax error` | WHERE clause `WHERE r.1=1` from `r.{since_clause}` | Use `_since_clause(window_hours, "r.started_at")` instead of `.replace()` |
| Service stuck in `activating (start-pre)` | Telemetry DB doesn't exist yet | Gateway not restarted, or no sessions run yet |
| LAN connection refused | Router AP/client isolation | Use SSH tunnel: `ssh -L 8009:localhost:8009 server` |
| Chart total ≠ summary card for "All time" | Chart was capped at 90 days | Remove WHERE clause for hours=0 |
| `/api/providers` ignores time window | Handler didn't parse `hours` param | Add `qs.get("hours", [24])[0]` to handler and `?hours=${hours}` to fetch |

---

## Verification Checklist

- [ ] Plugin installed & enabled (`hermes plugins list`)
- [ ] Gateway restarted from shell (not inside gateway)
- [ ] At least one session/cron run completed (creates telemetry.db)
- [ ] Systemd service active (running)
- [ ] `curl http://127.0.0.1:8009/api/summary?hours=0` returns JSON
- [ ] `curl http://192.168.0.222:8009/` returns HTML
- [ ] Dropdown shows 5 options: 24h, 7d, 30d, 90d, All time
- [ ] "All time" and "90 days" return data correctly
- [ ] Chart totals match summary cards for "All time"
- [ ] Budget editor modal opens/saves correctly
- [ ] `curl -X POST /api/budget` updates `budget.yaml` and returns updated status
- [ ] File watcher logs "budget.yaml modified — hot-reloading budget config" on edit
- [ ] Plugin immediately enforces new budget limits without restart