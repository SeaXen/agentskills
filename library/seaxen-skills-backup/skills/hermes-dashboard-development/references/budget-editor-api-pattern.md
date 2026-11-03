# Budget Editor API Pattern (Dashboard → Plugin Hot-Reload)

This pattern implements a complete budget management workflow: dashboard edit modal → POST to API → writes `budget.yaml` → file watcher hot-reloads plugin config.

## Server-side: serve.py

### 1. Constants & Helpers

```python
# Allowed values for budget config — prevents YAML key injection
ALLOWED_SCOPES = {"global", "per_cron_job", "per_sender"}
ALLOWED_WINDOWS = {"daily", "monthly"}

MAX_BUDGET_PAYLOAD = 1_048_576  # 1 MiB


def _validate_threshold(key: str, value, cfg: dict) -> str | None:
    """Validate and store a threshold (soft_pct/hard_pct). Returns error msg or None."""
    try:
        val = float(value)
    except (ValueError, TypeError):
        return f"{key} must be a number"
    if not (0 <= val <= 1):
        return f"{key} must be between 0 and 1"
    cfg.setdefault("thresholds", {})[key] = val
    return None
```

### 2. Budget Update Handler (POST /api/budget)

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

    # Validate scope/window against allowed sets (prevents YAML key injection)
    if scope not in ALLOWED_SCOPES:
        return {"enabled": False, "error": f"invalid scope: {scope!r}"}
    if window not in ALLOWED_WINDOWS:
        return {"enabled": False, "error": f"invalid window: {window!r}"}

    if limit_usd is None:
        return {"enabled": False, "error": "limit_usd is required"}

    try:
        limit_usd = float(limit_usd)
    except (ValueError, TypeError):
        return {"enabled": False, "error": "limit_usd must be a number"}

    if limit_usd < 0:
        return {"enabled": False, "error": "limit_usd must be >= 0"}

    # Initialize budgets structure if missing
    if "budgets" not in cfg:
        cfg["budgets"] = {}
    if scope not in cfg["budgets"]:
        cfg["budgets"][scope] = {}

    # Update the limit
    key = f"{window}_usd"
    cfg["budgets"][scope][key] = limit_usd

    # Optional: update thresholds (validated, no silent failures)
    for field, yaml_key in (("soft_pct", "soft_pct"), ("hard_pct", "hard_pct")):
        if field in payload:
            err = _validate_threshold(yaml_key, payload[field], cfg)
            if err:
                return {"enabled": False, "error": err}

    if "on_estimated_mode" in payload:
        mode = payload["on_estimated_mode"]
        if mode not in ("warn_only", "enforce"):
            return {"enabled": False, "error": "on_estimated_mode must be 'warn_only' or 'enforce'"}
        cfg.setdefault("on_estimated", {})["mode"] = mode

    # Write back (ATOMIC: temp file + os.replace)
    try:
        import os
        import yaml
        tmp = budget_path.with_suffix(".yaml.tmp")
        with open(tmp, "w") as f:
            yaml.safe_dump(cfg, f, default_flow_style=False, sort_keys=False)
        os.replace(tmp, budget_path)  # POSIX atomic — watchdog never sees partial file
    except Exception as e:
        return {"enabled": False, "error": f"Failed to write budget.yaml: {e}"}

    # Return updated status by calling api_budget()
    return api_budget()
```

### 3. Budget Detail Endpoint (GET /api/budget/detail) — for Modal Pre-fill

```python
def api_budget_detail(scope: str, window: str):
    """Get raw budget config for a specific scope/window for modal pre-fill."""
    if scope not in ALLOWED_SCOPES or window not in ALLOWED_WINDOWS:
        return {"error": "invalid scope or window"}
    budget_path = DB_PATH.parent / "budget.yaml"
    if not budget_path.exists():
        return {"error": "budget.yaml not found"}
    try:
        import yaml
    except ImportError:
        return {"error": "PyYAML not installed"}
    try:
        cfg = yaml.safe_load(budget_path.read_text()) or {}
    except Exception as e:
        return {"error": f"Failed to parse budget.yaml: {e}"}

    budgets = cfg.get("budgets", {})
    thresholds = cfg.get("thresholds", {})
    on_est = cfg.get("on_estimated", {})

    limit = budgets.get(scope, {}).get(f"{window}_usd")

    return {
        "scope": scope,
        "window": window,
        "limit_usd": limit,
        "soft_pct": thresholds.get("soft_pct", 0.8),
        "hard_pct": thresholds.get("hard_pct", 1.0),
        "on_estimated_mode": on_est.get("mode", "warn_only"),
    }
```

Register in `do_GET`:

```python
if path == "/api/budget/detail":
    qs = parse_qs(parsed.query)
    scope = qs.get("scope", ["global"])[0]
    window = qs.get("window", ["daily"])[0]
    return self._json(api_budget_detail(scope, window))
```

### 4. POST Handler with Payload Limit & Proper HTTP Status

```python
def do_POST(self):
    parsed = urlparse(self.path)
    path = parsed.path.rstrip("/") or "/"

    if path == "/api/budget":
        content_length = int(self.headers.get("Content-Length", 0))
        # Enforce 1 MiB max payload (DoS protection)
        if content_length > MAX_BUDGET_PAYLOAD:
            self.send_response(413)
            self.end_headers()
            self.wfile.write(b"Payload too large")
            return
        body = self.rfile.read(content_length).decode("utf-8")
        try:
            payload = json.loads(body) if body else {}
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")
            return
        result = api_budget_update(payload)
        # Return proper HTTP status: 200 for success, 400 for validation errors
        status = 200 if result.get("enabled") or "error" not in result else 400
        return self._json(result, status)

    self.send_response(404)
    self.end_headers()
    self.wfile.write(b"Not Found")
```

### 5. JSON Response Helper with Status Parameter

```python
def _json(self, data, status=200):
    body = json.dumps(data, default=str).encode()
    self.send_response(status)
    self.send_header("Content-Type", "application/json; charset=utf-8")
    self.send_header("Access-Control-Allow-Origin", "*")
    self.send_header("Content-Length", str(len(body)))
    self.end_headers()
    self.wfile.write(body)
```

---

## Client-side: index.html

### 1. XSS-Safe onclick Handler (Fixed — use single quotes)

```javascript
function renderBudget(data) {
  // ...
  for (const s of items) {
    const cls = s.level;
    // Use single quotes in onclick to avoid JSON.stringify double-quote breakage
    const safeScope = s.scope.replace(/'/g, "\\'");
    html += `<div class="budget-item">
      <div class="info"><span>${s.scope}</span><span>${fmtCost(s.spent)} / ${fmtCost(s.limit)} (${s.pct}%)</span><button class="budget-edit-btn" onclick="openBudgetModal('${safeScope}')">Edit</button></div>
      <div class="bar-bg"><div class="bar-fill ${cls}" style="width:${Math.min(s.pct, 100)}%"></div></div>
    </div>`;
  }
  // ...
}
```

**Why not `JSON.stringify()`?** Its output includes double quotes (`"global/daily"`), which breaks the HTML attribute when rendered as `onclick="openBudgetModal("global/daily")"`. Single quotes with escaped single quotes in the value is the robust fix.

### 2. Modal Pre-fill via API Fetch — **Sync-Open First, Then Async-Fetch**

```javascript
let currentBudgetScope = 'global';

async function openBudgetModal(scope) {
  // Parse "global/daily" -> scope="global", window="daily"
  const [parsedScope, parsedWindow] = scope.split('/');
  const actualScope = parsedScope || scope;
  const actualWindow = parsedWindow || 'daily';

  currentBudgetScope = actualScope;

  // Open modal FIRST (synchronous, works even if fetch fails)
  $('#budgetModal').classList.add('open');

  // Reset fields immediately - no waiting
  $('#budgetScope').value = actualScope;
  $('#budgetWindow').value = 'daily';  // reset window dropdown to daily
  $('#budgetLimit').value = '';
  $('#budgetSoftPct').value = '';
  $('#budgetHardPct').value = '';
  $('#budgetOnEstimated').value = 'warn_only';
  $('#budgetModalError').classList.remove('show');
  $('#budgetModalError').textContent = '';

  // Then fetch details for pre-fill (async, non-blocking)
  // Always fetch window=daily as default — avoids stale dropdown state bug
  try {
    const res = await fetch(`/api/budget/detail?scope=${encodeURIComponent(actualScope)}&window=daily`);
    const data = await res.json();
    if (!data.error) {
      $('#budgetLimit').value = data.limit_usd !== null && data.limit_usd !== undefined ? data.limit_usd : '';
      $('#budgetSoftPct').value = data.soft_pct !== undefined ? data.soft_pct : '';
      $('#budgetHardPct').value = data.hard_pct !== undefined ? data.hard_pct : '';
      $('#budgetOnEstimated').value = data.on_estimated_mode || 'warn_only';
      // Set window dropdown to match the fetched data's window if needed
      // Budget config has separate daily/monthly limits per scope
    }
  } catch {
    // Keep defaults on network error - modal already open with empty fields
  }
}
```

**Critical for tunnel/proxy/mobile:** Opening the modal synchronously before the async fetch ensures the UI responds even when:
- Mixed content blocks the fetch (HTTPS page → HTTP API through tunnel)
- Cloudflare Tunnel / Tailscale / reverse proxy has auth/websocket issues
- Mobile browsers have stricter CSP or network timing

The fetch is purely for pre-fill enhancement; the modal works with defaults if it fails.

**Fixed stale dropdown bug:** Previously fetched using `$('#budgetWindow').value` which could hold a value from a previous modal interaction (e.g., user switched to "monthly", closed without saving, then clicked Edit on another scope → fetch would use "monthly" for wrong scope). Now always fetches `window=daily` as the default.

**Removed unused variable:** `currentBudgetWindow` was declared but never read; removed to avoid confusion.

### 3. parseFloat('0') Bug Fix — Explicit Empty-String Check

```javascript
async function saveBudget() {
  // Helper: parse float, return undefined if empty/whitespace
  const parseOptFloat = (v) => {
    const s = v.trim();
    return s === '' ? undefined : parseFloat(s);
  };

  const payload = {
    scope: $('#budgetScope').value,
    window: $('#budgetWindow').value,
    limit_usd: parseOptFloat($('#budgetLimit').value),
    soft_pct: parseOptFloat($('#budgetSoftPct').value),
    hard_pct: parseOptFloat($('#budgetHardPct').value),
    on_estimated_mode: $('#budgetOnEstimated').value
  };

  if (payload.limit_usd === undefined || isNaN(payload.limit_usd)) {
    showModalError('Limit (USD) is required');
    return;
  }
  // ... rest of save logic
}
```

### 4. Modal CSS Hardening (Tunnel/Mobile Visibility)

```css
/* Budget modal */
.modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.7); display: none; align-items: center; justify-content: center; z-index: 99999; }
.modal-overlay.open { display: flex !important; }
.modal { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 24px; width: 100%; max-width: 400px; margin: 16px; box-shadow: 0 8px 32px rgba(0,0,0,0.5); }
```

- `z-index: 99999` — above any injected auth overlays
- `display: flex !important` — overrides any proxy-injected styles
- `box-shadow` — depth cue for mobile viewport

### 5. Threshold Scope Clarification (Global Footgun Prevention)

```html
<div class="form-row">
  <div class="form-group">
    <label>Soft threshold (%) <span class="text-muted" style="font-size:10px;font-weight:400">(global)</span></label>
    <input type="number" id="budgetSoftPct" step="0.01" min="0" max="1" placeholder="0.80">
  </div>
  <div class="form-group">
    <label>Hard threshold (%) <span class="text-muted" style="font-size:10px;font-weight:400">(global)</span></label>
    <input type="number" id="budgetHardPct" step="0.01" min="0" max="1" placeholder="1.00">
  </div>
</div>
```

Thresholds (`soft_pct`, `hard_pct`) live in a single global `thresholds` block in `budget.yaml` — not per-scope. The modal presents them next to a specific scope, making them look scope-local. The `(global)` label prevents users from accidentally changing global thresholds while thinking they're tuning a single job.

---

## Key Security & Robustness Fixes

| Issue | Fix |
|-------|-----|
| XSS via `onclick="openBudgetModal('${s.scope}')"` | Use single quotes in onclick with escaped value: `onclick="openBudgetModal('${safeScope}')"` |
| `JSON.stringify()` in onclick breaks HTML attribute | Replace with single-quote pattern (see above) |
| Budget API expects separate scope/window but button passes "global/daily" | Parse in `openBudgetModal()`: `scope.split('/')` |
| Modal fails to open on tunnel/mixed-content (HTTPS→HTTP) | Open modal **synchronously first**, then fetch async |
| Modal invisible behind proxy/auth layers / mobile viewport | CSS: `z-index: 99999`, `display: flex !important`, box-shadow |
| YAML key injection via unvalidated scope/window | Validate against `ALLOWED_SCOPES` / `ALLOWED_WINDOWS` |
| `parseFloat('0') \|\| undefined` drops 0 | Use `trim() === '' ? undefined : parseFloat()` |
| Silent validation failures | `_validate_threshold()` returns errors; no `pass` on exception |
| No payload size limit | `MAX_BUDGET_PAYLOAD = 1_048_576` (1 MiB); returns 413 |
| Validation errors return 200 | Return 400 for errors; `_json(data, status=200)` |
| Stale dropdown state in modal pre-fill | Always fetch `window=daily`, ignore `$('#budgetWindow').value` |
| Unused `currentBudgetWindow` state variable | Removed; DOM is source of truth |

---

## Flow

```
User clicks "Edit" on budget row
    → openBudgetModal(scope) parses "global/daily" format
    → Opens modal IMMEDIATELY (synchronous classList.add('open'))
    → Resets all fields to defaults
    → fetch(/api/budget/detail?scope=...&window=daily) — hardcoded daily
    → pre-fills modal with current values
User edits, clicks Save
    → saveBudget() builds payload with parseOptFloat()
    → POST /api/budget (1 MiB limit)
    → api_budget_update() validates scope/window/thresholds
    → writes budget.yaml ATOMICALLY (temp + os.replace)
    → returns updated status (200/400)
    → watchdog on_modified fires
    → budget.reload_config() clears caches
    → plugin enforces new limits immediately
```

---

## Atomic YAML Write Pattern (Plugin-side too)

Both dashboard API (`serve.py`) and slash command (`budget.py::_set_budget`) must write atomically to prevent watchdog from reading partial YAML:

```python
import os
import yaml

tmp = path.with_suffix(".yaml.tmp")
with open(tmp, "w") as f:
    yaml.safe_dump(cfg, f, default_flow_style=False, sort_keys=False)
os.replace(tmp, path)  # POSIX atomic — watchdog only ever sees complete file
```

**Why this matters:** `write_text()` truncates then writes. Watchdog fires `IN_MODIFY` on first write to truncated file → `safe_load("")` returns `None` → config resets to "no limits" for milliseconds → budget gate misses enforcement. Atomic replace eliminates this window.

---

## Upstream PR Workflow (Fork → Push → Auto-Update)

```bash
# If push to upstream denied (403):
git remote add fork https://github.com/<your-user>/<repo>.git
git push fork HEAD:feature-branch  # PR auto-updates

# If rebase conflicts on dashboard files after fork sync:
git checkout --theirs dashboard/serve.py dashboard/index.html
git add dashboard/serve.py dashboard/index.html
git rebase --continue
```