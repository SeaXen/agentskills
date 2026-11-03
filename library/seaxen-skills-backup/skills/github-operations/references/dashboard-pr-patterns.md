# PR Review Handling — Dashboard Plugins

## Common Dashboard PR Patterns

When reviewing PRs for plugin dashboards (API + frontend), watch for these recurring issues:

### 1. Handler Not Passing Params to Called Function

**Symptom:** Frontend sends `?hours=X` but API ignores it.

```python
# BROKEN
if path == "/api/providers":
    return self._json(api_providers())  # no hours passed

# FIXED
if path == "/api/providers":
    qs = parse_qs(parsed.query)
    return self._json(api_providers(int(qs.get("hours", [24])[0])))
```

### 2. Frontend Fetch Not Including Query Params

**Symptom:** Dropdown changes but one panel doesn't update.

```javascript
// BROKEN
fetchJSON('/api/providers')

// FIXED
fetchJSON(`/api/providers?hours=${hours}`)
```

### 3. Fragile String Replacement in SQL

**Symptom:** SQL breaks silently when helper refactored (e.g., `WHERE r.1=1`).

```python
# BROKEN — depends on literal "started_at" in helper output
WHERE {since_clause.replace("started_at", "r.started_at")}

// FIXED — pass column explicitly
def _since_clause(window_hours, col="started_at"):
    wh = int(window_hours)
    if wh == 0:
        return "1=1"
    return f"{col} >= datetime('now', '-{wh} hours')"

# Usage:
WHERE {_since_clause(window_hours, "r.started_at")}
```

### 4. Integer Division Truncation

**Symptom:** `hours=47` → 1 day instead of 2.

```python
# BROKEN
WHERE started_at >= datetime('now', '-{int(daily_window/24)} days')

// FIXED
WHERE started_at >= datetime('now', '-{daily_window // 24} days')
```

### 5. Chart Window Mismatch

**Symptom:** Summary cards show all-time totals but chart capped at 90 days.

```python
# BROKEN — forces 90-day cap for all-time
daily_window = int(window_hours)
if daily_window == 0:
    daily_window = 2160

// FIXED — unbounded query for hours=0
if daily_window == 0:
    daily_cost = _rows("SELECT DATE(started_at) AS day, ... FROM runs GROUP BY DATE(started_at)")
else:
    daily_cost = _rows(f"SELECT ... WHERE started_at >= datetime('now', '-{daily_window // 24} days')")
```

### 6. Missing Input Validation

**Symptom:** 500 on empty POST or invalid JSON.

```python
# Always validate
if limit_usd is None:
    return {"error": "limit_usd is required"}
try:
    limit_usd = float(limit_usd)
except (ValueError, TypeError):
    return {"error": "limit_usd must be a number"}
```

### 7. Older DB Schema Should Degrade, Not 500

**Symptom:** New dashboard widget queries a column that older telemetry DBs do not have yet, and the whole dashboard returns 500.

```python
# BROKEN — uncaught OperationalError kills /api route
return _one("SELECT COALESCE(SUM(reasoning_tokens), 0) ...")

# FIXED — frontend can already hide missing widget
try:
    return _one("SELECT COALESCE(SUM(reasoning_tokens), 0) ...")
except Exception:
    return None
```

Use this for optional panels like token-breakdown/detail widgets: missing schema should hide the panel, not crash the page.

### 8. Atomic Write Changes Watchdog Event Type on Linux

**Symptom:** Switching from `write_text()` to temp-file + `os.replace()` fixes partial-write races, but hot-reload silently stops working on Linux.

Cause: `os.replace(tmp, target)` emits `IN_MOVED_TO` in inotify, which watchdog surfaces as `FileMovedEvent` / `on_moved` (sometimes `on_created`) — not `FileModifiedEvent`.

```python
# BROKEN — only sees direct edits, not atomic replace
class BudgetConfigHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("budget.yaml"):
            reload_config()

# FIXED
class BudgetConfigHandler(FileSystemEventHandler):
    def _reload_if_budget(self, path):
        if os.path.basename(path) == "budget.yaml":
            reload_config()

    def on_modified(self, event):
        if not event.is_directory:
            self._reload_if_budget(event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            self._reload_if_budget(event.src_path)

    def on_moved(self, event):
        self._reload_if_budget(getattr(event, "dest_path", ""))
```

If a dashboard POST writes config atomically and the plugin relies on watchdog reload, review both sides together: **writer** and **watcher**.

### 9. Modal Defaults Must Not Depend on Stale DOM State

**Symptom:** Edit modal prefills the wrong budget because it reads the last-selected dropdown value from a previous modal session.

```javascript
// BROKEN — can carry over 'monthly' from previous open
fetch(`/api/budget/detail?scope=${scope}&window=${$('#budgetWindow').value}`)

// FIXED — choose an explicit default and reset UI first
$('#budgetWindow').value = 'daily';
$('#budgetLimit').value = '';
$('#budgetModal').classList.add('open');
const res = await fetch(`/api/budget/detail?scope=${scope}&window=daily`);
```

Open the modal synchronously first, then populate async. That prevents zero-feedback clicks and cross-request races on slow links.

### 10. Fix Both JS-String and HTML-Content Injection Paths

**Symptom:** Inline `onclick` is fixed, but the same field is still injected raw into `<span>` content.

```javascript
function escHtml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

const safeScope = s.scope.replace(/'/g, "\\'");      // JS string / onclick
const label = escHtml(s.scope);                       // HTML text node
```

When rendering with template literals into `innerHTML`, review **attribute context** and **element-content context** separately.

### 11. Global Settings Must Be Labeled as Global

**Symptom:** Modal shows global thresholds next to a specific scope, so users assume they are editing per-scope values.

At minimum, label them explicitly:
- `Soft threshold (%) (applies to all scopes)`
- `Hard threshold (%) (applies to all scopes)`

If the UI cannot separate global settings into their own panel, the label must carry the truth.

### 12. Weekly Buckets Must Use Stable Week-Start Dates, Not `%W` Labels

**Symptom:** Weekly trend/share charts look fine most of the year but split or mislabel data around New Year boundaries (`W00`, wrong year, or cross-year week fragmentation).

```python
# BROKEN — calendar label, not a stable bucket key
strftime('%Y-W%W', ts)

# BETTER — bucket by Monday start date
DATE(ts, '-' || ((CAST(strftime('%w', ts) AS INTEGER) + 6) % 7) || ' days')
```

Why this matters:
- `%W` is not ISO-week safe for operator analytics
- week labels can drift across year boundaries
- comparison endpoints can silently report misleading deltas if the bucket key itself is wrong

Review rule:
- for weekly aggregation, prefer a **week-start date bucket** (usually Monday) or a fully correct ISO-week implementation
- add at least one regression test that spans late December → early January so the bug cannot re-enter quietly

---

## Review Workflow for Dashboard PRs

1. **Trace one parameter end-to-end**: Pick a dropdown value → frontend fetch → handler → SQL → template render.
2. **Test edge cases**: `hours=0`, `hours=47`, missing param, invalid JSON.
3. **Verify chart totals match summary** for each window.
4. **Check all API endpoints** get the param (providers often missed).
4. **Run the dashboard locally** and click through the UI.

---

## Fork-and-PR Workflow When Upstream Push Denied

```bash
# 1. Fork
gh repo fork <owner>/<repo> --clone=false

# 2. Add fork remote locally
git remote add fork https://github.com/<your-user>/<repo>.git

# 3. Push branch to fork
git push fork <branch-name>

# 4. Create PR pointing to upstream main
gh pr create --repo <owner>/<repo> --head <your-user>:<branch-name> --base main --title "..." --body "..."
```