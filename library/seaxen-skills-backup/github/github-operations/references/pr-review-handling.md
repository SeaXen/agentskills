# PR Review Handling Patterns

## Overview

When submitting PRs to upstream repos, anticipate and handle review feedback systematically. This reference captures patterns from hermes-telemetry reviews (including PR #22, #53, #58).

## Common Review Categories & Responses

### 🔴 Blockers (Must Fix)

| Issue | Pattern | Fix Approach |
|-------|---------|--------------|
| API endpoint ignores query param | Handler calls function without arguments | Parse query param, pass to handler; update frontend fetch to include param |
| Missing permission to push to upstream | `git push` denied | Fork repo, push to fork, create PR from fork |
| Cache hit freezes forever | `get_rows` is presence-only; no `built_at` TTL | TTL check; serve-stale + async refresh for that key |
| Vendored asset 404 off-cwd | `super().do_GET()` uses process cwd | `Handler(directory=str(SCRIPT_DIR))` or serve bytes |

### 🟡 Refactoring Suggestions

| Issue | Pattern | Fix Approach |
|-------|---------|--------------|
| Duplicate helper functions | Two functions identical except hardcoded column name | Single parameterized function with column argument |
| Fragile string replacement in SQL | `.replace("col", "table.col")` | Pass column name directly to helper |
| Integer division truncation bug | `int(x/24)` | Use `x // 24` |
| Silent data mismatch | Chart capped at 90d but summary shows all-time | Make chart unbounded for all-time, or add explicit label |
| Duplicate cache class | `ModelEfficiencyCache` reimplements base | Subclass base; override `cache_key` / `compute_rows` / storage only |

### 🟢 UX Polish

| Issue | Pattern | Fix Approach |
|-------|---------|--------------|
| Hardcoded UI labels | "Daily Cost (7 days)" regardless of selection | Dynamic labels based on selected window |
| No user-facing config editor | Read-only display of config | Add POST endpoint + modal form |

## Review Response Workflow

1. **Read all comments** — don't miss inline comments on specific lines. If `gh pr view --comments` is empty or stale, use REST: `gh api repos/<owner>/<repo>/pulls/<pr>/reviews`, `gh api repos/<owner>/<repo>/pulls/<pr>/comments --paginate`, and `gh api repos/<owner>/<repo>/issues/<pr>/comments`.
2. **Categorize** — blocker / refactor / UX / nit
3. **Fix in priority order** — blockers first, then refactors, then UX
4. **Check current-head relevance** — compare each comment's `commit_id` to `gh pr view --json headRefOid`; comments anchored to old commits may be stale after a force-push, but still inspect whether the current diff truly addresses them.
5. **Test each fix** — run the narrowest regression test that proves the review concern is gone; add assertions when the review caught a real missing edge case.
6. **Push to fork branch** — use `--force-with-lease` only when amending/replacing the PR commit intentionally.
7. **Reply only when useful** — short GitHub-native replies; use `--body-file` whenever text has backticks.

## Cache / background-refresh blockers

When a reviewer says cache hits can be permanently stale:

| Check | Bad | Good |
|-------|-----|------|
| Hit path | presence-only | `built_at` within TTL |
| Stale path | recompute sync (blocks) or never | serve-stale + async refresh for that key |
| Background set | only static DEFAULT windows | static prime + on-access refresh for dynamic UI keys |
| Growth | never delete keys | age + max-entry eviction |
| Duplication | second full cache class | subclass base; fix once |
| Tests | `elapsed < 0.5` | assert compute fn call count |

See also `learnables/github-pr-maintenance/references/cache-layer-review-patterns.md`.

## Scope contamination

If the open PR is about schema/cache/concurrency, **do not** push Chart.js vendoring, port renames, or auto-refresh UI nits onto the same head. Open a second PR off current `main`. Reply to “still working?” with that split stated explicitly.

## Comment bodies with code/paths

```bash
gh pr comment <n> --repo owner/repo --body-file /tmp/pr-reply.md
```

Never rely on shell-expanded double quotes for backticks.

## Practical Patterns from PR #22

### Fixing "API ignores param" Blocker

**Before:**
```python
# Handler
if path == "/api/providers":
    return self._json(api_providers())  # no argument!

# Frontend
fetchJSON('/api/providers')  # no hours passed
```

**After:**
```python
# Handler
if path == "/api/providers":
    qs = parse_qs(parsed.query)
    return self._json(api_providers(int(qs.get("hours", [24])[0])))

# Frontend
fetchJSON(`/api/providers?hours=${hours}`)
```

### Consolidating Duplicate Helpers

**Before:**
```python
def _since_clause(window_hours):
    wh = int(window_hours)
    if wh == 0: return "1=1"
    return f"started_at >= datetime('now', '-{wh} hours')"

def _since_clause_ts(window_hours):
    wh = int(window_hours)
    if wh == 0: return "1=1"
    return f"ts >= datetime('now', '-{wh} hours')"

# Fragile usage:
WHERE {since_clause.replace("started_at", "r.started_at")}
```

**After:**
```python
def _since_clause(window_hours, col="started_at"):
    wh = int(window_hours)
    if wh == 0: return "1=1"
    return f"{col} >= datetime('now', '-{wh} hours')"

# Clean usage:
WHERE {_since_clause(window_hours, "r.started_at")}
```

### Fixing Chart/Summary Mismatch

**Before:** Chart hardcapped at 90 days for "All time" selection.
```python
if daily_window == 0:
    daily_window = 2160  # 90 days
daily_cost = _rows(f"""... WHERE started_at >= datetime('now', '-{daily_window // 24} days')""")
```

**After:** Unbounded for all-time.
```python
if daily_window == 0:
    daily_cost = _rows("""... FROM runs GROUP BY DATE(started_at)""")  # no WHERE
else:
    daily_cost = _rows(f"""... WHERE started_at >= datetime('now', '-{daily_window // 24} days')""")
```

### Adding POST Endpoint to Python stdlib HTTP Server

```python
class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # ... existing GET routes
    
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

### Modal Form Pattern (Vanilla JS)

```html
<!-- Overlay -->
<div class="modal-overlay" id="budgetModal" onclick="if(event.target===this) closeBudgetModal()">
  <div class="modal" onclick="event.stopPropagation()">
    <h3>Edit Budget</h3>
    <div class="form-group">
      <label>Scope</label>
      <select id="budgetScope">...</select>
    </div>
    <!-- ... more fields ... -->
    <div class="modal-error" id="budgetModalError"></div>
    <div class="modal-actions">
      <button class="modal-btn cancel" onclick="closeBudgetModal()">Cancel</button>
      <button class="modal-btn save" onclick="saveBudget()">Save</button>
    </div>
  </div>
</div>
```

```javascript
function openBudgetModal(scope) {
  $('#budgetScope').value = scope;
  $('#budgetModalError').classList.remove('show');
  $('#budgetModal').classList.add('open');
}
function closeBudgetModal() { $('#budgetModal').classList.remove('open'); }
async function saveBudget() {
  const payload = { scope: $('#budgetScope').value, /* ... */ };
  const response = await fetch('/api/budget', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
  const result = await response.json();
  if (result.error) { showModalError(result.error); return; }
  closeBudgetModal(); loadAll();
}
function showModalError(msg) { const el = $('#budgetModalError'); el.textContent = msg; el.classList.add('show'); }
```

## Bot / Auto-review Pitfalls

### Make safety fixes syntactically obvious

Auto-review bots can flag a line even after the logic is fixed if the safe branch is hidden in a ternary or helper. For destructive operations, prefer explicit control flow:

```ts
if (period === "all") {
  artifactResult = purgeWholeDirectory();
} else {
  artifactResult = deleteOnlyArtifactsForDeletedRows(paths);
}
```

Then add tests for both branches. Example regression shape for reset endpoints:

- seed an old row and recent row
- create file artifacts for both
- period reset deletes only the old DB row and old artifact
- recent DB row and recent artifact survive
- `all` reset deletes the remaining DB row and artifact

### Follow repository layering rules, not just working code

When a review cites style guide boundaries (for example “no raw SQL in route handlers”), move the query into the repo’s domain module (`src/lib/db/...`) and import a small semantic helper in the route. Do not argue that the route query is simple; upstream maintainers care about consistency.

## Verification Before "Resolved"

- [ ] Manual `curl` test for each fixed endpoint, when endpoint behavior changed
- [ ] Browser check for UI changes
- [ ] Focused regression test for each review blocker
- [ ] Edge cases: partial/period-scoped deletes, empty input, invalid JSON, missing params
- [ ] Auto-refresh still works
- [ ] No regression on existing time windows (24h, 7d, 30d)
- [ ] No committed conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
- [ ] PR metadata rechecked: `mergeable`, current `headRefOid`, and status checks
