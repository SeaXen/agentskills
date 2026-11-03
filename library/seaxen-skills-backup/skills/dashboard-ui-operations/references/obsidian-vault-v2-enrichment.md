# Obsidian Vault Dashboard V2 — Lazy-loaded tab enrichment

Use this when the user has an existing self-hosted dashboard (single-file monolith, `BaseHTTPRequestHandler`, or similar) and asks to **add many new tabs at once** with rich per-tab data: stat cards, tables, heatmaps, tag clouds, quick-capture forms, pinned-state UX.

Pattern proven on the Obsidian memory vault dashboard at `:6065`, growing from 6 tabs → 12 tabs and 6 API endpoints → 15 endpoints.

## When to use

- User says "make this a best [thing]" or "add as much as possible" on an existing single-file dashboard
- Existing dashboard has an established `<style>` block + legacy JS that you must not break
- Many new tabs to add at once (5+ tabs with distinct content)
- Each new tab needs to pull from one or more backend endpoints
- Per-tab data is independent (each tab loads its own JSON, no shared cross-tab state besides global)

Do **not** use this for:
- Dist-only bundles where you cannot edit the source (use `references/dist-only-*` instead)
- Dashboards with a React/Vue framework that already has routing (just add routes)
- Single-tab additions (a lazy-load pattern is overkill for one new tab)

## Architecture: the lazy-tab pattern

Each new tab gets:
1. **One HTML page div** with `data-page="<name>"` and stable IDs for the data containers
2. **Tab button** in the `.page-tabs` row with `onclick="switchPage('<name>')"`
3. **One JS function** (`loadX()`) that fetches its endpoints and populates the DOM
4. **switchPage augmentation** that calls the right `loadX()` only when that tab is opened

The page-div-first, then-JS-second, then-CSS-last order matters because:
- Tab buttons need the switchPage handler to exist (so lazy-load fires)
- Page divs need stable IDs the JS will target
- JS needs the DOM structure to exist before populating it

## Step-by-step

### 1. Add tab buttons

Insert in the existing `.page-tabs` row in the order you want them to appear:

```html
<button class="page-tab" data-page="stats"  onclick="switchPage('stats')">Stats</button>
<button class="page-tab" data-page="tags"   onclick="switchPage('tags')">Tags</button>
<button class="page-tab" data-page="folders" onclick="switchPage('folders')">Folders</button>
```

Keep them short (one word) and consistent with existing tab styling.

### 2. Add page divs after the last existing `</div>` of the page section

Use stable IDs that match what your JS will target:

```html
<div class="page" data-page="stats">
  <div class="stat-grid">
    <div class="stat-card"><div class="value" id="statsNotes">—</div><div class="label">Notes</div></div>
    <!-- more stat cards -->
  </div>
  <div class="grid-2">
    <div class="panel"><div class="panel-head"><h3>...</h3></div>
      <div class="panel-body" id="freshnessBuckets"></div></div>
    <div class="panel">...</div>
  </div>
</div>
```

Useful CSS class combinations:
- `.grid-2` — two equal columns responsive to single on narrow viewports
- `.stat-grid` — existing auto-fit stat cards (see existing dashboard)
- `.panel + .panel-head + .panel-body` — existing panel pattern (don't reinvent)
- `.bar-row` — for horizontal-bar lists (folder distribution, freshness buckets)
- `.tag-chip` — colored rounded chips for tags
- `.stale-row`, `.pinned-row`, `.cron-row`, `.lint-row` — named row patterns

### 3. Add the JS loader functions

Each new tab gets one async loader that fetches its endpoint(s) and populates the DOM:

```js
async function loadStats() {
  try {
    const res = await fetch('/api/vault-stats');
    const s = await res.json();
    if (!s) return;
    setText('statsNotes', s.total_notes || 0);
    // ... populate other stat cards
    const fel = document.getElementById('folderDistribution');
    if (fel) {
      fel.innerHTML = Object.entries(s.by_folder || {}).map(([f, c]) => {
        const total = Object.values(s.by_folder).reduce((a,b)=>a+b, 0) || 1;
        const pct = Math.round(100 * c / total);
        return `<div class="bar-row">
          <div class="label">${esc(f)}</div>
          <div class="bar"><div style="width:${pct}%"></div></div>
          <div class="num">${c}</div>
        </div>`;
      }).join('');
    }
  } catch (e) { console.error('loadStats', e); }
}
```

Helper functions to define once:

```js
function setText(id, v) { const el = document.getElementById(id); if (el) el.textContent = v; }
function esc(s) {
  if (s === null || s === undefined) return '';
  return String(s).replace(/[&<>"']/g, c => 
    ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}
```

### 4. Augment switchPage to lazy-load

This is the critical part — do **not** call `loadAll()` on initial page load (it would fetch every endpoint upfront). Instead, intercept `switchPage()`:

```js
const _origSwitchPage = window.switchPage;
window.switchPage = function(name) {
  if (_origSwitchPage) _origSwitchPage(name);
  else {
    document.querySelectorAll('.page-tab').forEach(b => 
      b.classList.toggle('active', b.dataset.page === name));
    document.querySelectorAll('.page').forEach(p => 
      p.classList.toggle('active', p.dataset.page === name));
  }
  // Lazy-load per tab
  if (name === 'stats') loadStats();
  if (name === 'tags') loadTags();
  if (name === 'folders') loadFolderTree();
  if (name === 'activity') loadActivity();
  if (name === 'cron') loadCron();
  if (name === 'capture') renderPinned();
};
```

Why this matters:
- Initial page load stays fast — only the home tab fetches its data
- Tabs fetched on-demand keep memory and CPU low
- A bug in one tab's loader does not block other tabs

### 5. Add the backend endpoints

Add new Python functions **before `class Handler`** and add the `elif u.path == ...` branches **inside the existing `do_GET`**:

```python
def _vault_stats_core(graph: dict) -> dict:
    """Compute total words, reading time, freshness buckets, by-year, etc."""
    # ... return dict

# In class Handler.do_GET:
elif u.path == "/api/vault-stats":
    graph = scan_notes()
    self.send(200, "application/json", json.dumps(_vault_stats_core(graph)).encode())
```

For POST endpoints (e.g. quick-capture), add to `do_POST`:

```python
elif u.path == "/api/quick-capture":
    try:
        payload = self.read_json()
        saved = _create_note_core(payload)
        if "error" in saved:
            self.send(400, "application/json", json.dumps(saved).encode())
        else:
            self.send(200, "application/json", json.dumps(saved).encode())
    except Exception as e:
        self.send(400, "application/json", json.dumps({"error": str(e)}).encode())
```

## Tier-classified tag cloud

This is a clean pattern for visualizing tag frequency. Compute tier from count thresholds:

```python
# Backend
if count >= 10: cat = "primary"
elif count >= 5: cat = "secondary"
elif count >= 2: cat = "minor"
else: cat = "rare"
cloud.append({"tag": tag, "count": count, "weight": round(weight, 3), "category": cat})
```

```css
.tag-chip.primary{background:rgba(88,166,255,.12);border-color:rgba(88,166,255,.4);color:#79b8ff;font-weight:600}
.tag-chip.secondary{background:rgba(63,185,80,.10);border-color:rgba(63,185,80,.35);color:#56d364}
.tag-chip.minor{background:rgba(210,153,34,.10);border-color:rgba(210,153,34,.30);color:#e3b341}
.tag-chip.rare{color:var(--muted);font-size:10px}
```

```js
// Font size scales with weight
const fontSize = 11 + c.weight * 14;
return `<span class="tag-chip ${c.category}" style="font-size:${fontSize.toFixed(0)}px" onclick="searchByTag('${esc(c.tag)}')">${esc(c.tag)} <span class="cnt">${c.count}</span></span>`;
```

Click handler wires to search:

```js
function searchByTag(tag) {
  switchPage('notes');
  const sb = document.getElementById('searchBox') || document.querySelector('input[type=search]');
  if (sb) { sb.value = tag; sb.dispatchEvent(new Event('input')); }
}
```

## GitHub-style activity heatmap

Build day-buckets for the last N days, scale by max:

```js
async function renderHeatmap() {
  const payload = await (await fetch('/api/graph')).json();
  const notes = payload.notes || [];
  const counts = {};
  const today = new Date();
  today.setHours(0,0,0,0);
  for (let i = 0; i < 365; i++) {
    const d = new Date(today);
    d.setDate(d.getDate() - i);
    counts[d.toISOString().slice(0,10)] = 0;
  }
  for (const n of notes) {
    const day = (n.mtime || '').slice(0, 10);
    if (day in counts) counts[day]++;
  }
  const max = Math.max(1, ...Object.values(counts));
  const cells = Object.keys(counts).sort().map(d => {
    const c = counts[d];
    const level = c === 0 ? '' : (c >= max*0.75 ? 'l4' : 
      (c >= max*0.5 ? 'l3' : (c >= max*0.25 ? 'l2' : 'l1')));
    return `<div class="cell ${level}" title="${d}: ${c} edit${c===1?'':'s'}"></div>`;
  }).join('');
  // CSS:
  // .heatmap{display:grid;grid-auto-flow:column;grid-template-rows:repeat(7,12px);gap:3px}
  // .heatmap .cell{width:12px;height:12px;border-radius:2px;background:var(--panel3)}
  // .heatmap .cell.l1{background:rgba(88,166,255,.20)} ...l2..l3..l4
}
```

`grid-auto-flow: column` + 7 fixed rows = GitHub's contribution graph layout.

## Pinned notes via localStorage

Pattern for "save important notes across sessions" without backend:

```js
const PIN_KEY = 'obsmemory.pinned.v1';
function getPinned() { try { return JSON.parse(localStorage.getItem(PIN_KEY) || '[]'); } catch { return []; } }
function setPinned(arr) { localStorage.setItem(PIN_KEY, JSON.stringify(arr)); }
function isPinned(path) { return getPinned().some(p => p.path === path); }
function togglePin(path, title) {
  let pinned = getPinned();
  pinned = isPinned(path) ? pinned.filter(p => p.path !== path) : pinned.push({path, title, pinned_at: new Date().toISOString()});
  setPinned(pinned);
  renderPinned();
  // Refresh any visible note lists so the star state stays in sync
  if (document.querySelector('.page.active')?.dataset.page === 'folders') loadFolderTree();
}
function pinBtn(path, title) {
  if (!path) return '';
  const pinned = isPinned(path);
  return `<button class="pin-btn-inline ${pinned?'pinned':''}" onclick="event.stopPropagation();togglePin('${esc(path)}','${esc(title||'')}')">${pinned?'★':'☆'}</button>`;
}
```

Key versioning (`v1` suffix) lets you migrate the schema later by bumping the version. `event.stopPropagation()` prevents the click from also triggering the row click handler.

## Quick capture POST endpoint

Pattern for "create a new note from the dashboard":

```python
def _create_note_core(payload: dict) -> dict:
    from datetime import datetime, timezone
    folder = (payload.get("folder") or "Inbox").strip().strip("/")
    title = (payload.get("title") or "").strip()
    content = payload.get("content") or ""
    tags = payload.get("tags") or []
    if not title:
        return {"error": "title is required"}
    safe_title = re.sub(r"[^\w\s\-.()]", "", title).strip()
    if not safe_title:
        return {"error": "title contains only invalid characters"}
    folder_path = VAULT / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    note_path = folder_path / f"{safe_title}.md"
    if note_path.exists():
        return {"error": f"note already exists: {note_path.relative_to(VAULT)}"}
    fm_lines = ["---", f"created: {datetime.now(timezone.utc).isoformat()}"]
    if tags:
        fm_lines.append("tags:")
        for t in tags: fm_lines.append(f"  - {t}")
    fm_lines.append("source: dashboard-quick-capture")
    fm_lines.append("---\n")
    body = "\n".join(fm_lines) + f"# {safe_title}\n\n{content}\n"
    note_path.write_text(body)
    return {"ok": True, "path": str(note_path.relative_to(VAULT)), "title": safe_title, "folder": folder}
```

The `re.sub(r"[^\w\s\-.()]", "", title)` strips shell-dangerous chars; explicit folder creation handles missing dirs; duplicate check prevents silent overwrite.

## CRITICAL: timezone-naive datetime pitfall

If your dashboard stores note `mtime` as a date string like `"2026-05-28"` (no Z, no offset), `datetime.fromisoformat(m)` returns a **NAIVE** datetime. Comparing it to an aware `cutoff = datetime.now(timezone.utc)` raises:

```
TypeError: can't compare offset-naive and offset-aware datetimes
```

This silently produces 0 results in any "last N days/hours" endpoint and you only find out when the user says "no recent edits in last year".

**Fix pattern** — in every endpoint that parses note mtime:

```python
from datetime import datetime, timezone
m = "2026-05-28"
try:
    dt = datetime.fromisoformat(m.replace("Z", "+00:00"))
except ValueError:
    dt = datetime.fromisoformat(m)
if dt.tzinfo is None:
    dt = dt.replace(tzinfo=timezone.utc)
# Now safe to compare with aware datetimes
```

The same trap also appears in vault-stats freshness buckets, stale-notes, and recent-activity. Apply the fix in all three. Better yet, centralize it in a helper:

```python
def _parse_note_mtime(s) -> datetime | None:
    from datetime import datetime, timezone
    try:
        if isinstance(s, (int, float)):
            return datetime.fromtimestamp(s, tz=timezone.utc)
        try:
            dt = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
        except ValueError:
            dt = datetime.fromisoformat(str(s))
        return dt.replace(tzinfo=timezone.utc) if dt.tzinfo is None else dt
    except Exception:
        return None
```

**Symptom**: `recent-activity?hours=8760` returns `count=0` even though the vault has notes dated 2026-05-28.
**Quick test**:
```python
from datetime import datetime, timezone, timedelta
datetime.fromisoformat("2026-05-28") >= datetime.now(timezone.utc) - timedelta(days=365)
# TypeError: can't compare offset-naive and offset-aware datetimes
```

## CSS row patterns worth reusing

Add to your existing dashboard CSS once, reuse across many panels:

```css
/* Horizontal bar row (folder distribution, freshness, etc.) */
.bar-row{display:grid;grid-template-columns:140px 1fr 50px;gap:8px;align-items:center;padding:5px 0;font-size:12px}
.bar-row .label{color:var(--text);font-weight:500;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.bar-row .bar{height:8px;background:var(--panel3);border-radius:4px;overflow:hidden}
.bar-row .bar > div{height:100%;background:linear-gradient(90deg,var(--accent) 0%,#79b8ff 100%);border-radius:4px;transition:width .35s}
.bar-row .num{color:var(--muted);font-variant-numeric:tabular-nums;text-align:right}

/* Status pills */
.status-pill{display:inline-block;padding:2px 8px;border-radius:999px;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.4px}
.status-pill.ok{background:rgba(63,185,80,.15);color:#56d364}
.status-pill.error{background:rgba(248,81,73,.15);color:#f85149}
.status-pill.unknown{background:var(--panel3);color:var(--muted)}

/* Cron-style row */
.cron-row{display:grid;grid-template-columns:1fr 130px 100px 110px;gap:10px;padding:8px 10px;border-bottom:1px solid var(--line);font-size:12px;align-items:center}

/* Pinned row */
.pinned-row{display:flex;align-items:center;gap:10px;padding:8px 10px;border:1px solid var(--line);border-radius:6px;background:var(--panel2);margin-bottom:6px}

/* Lint row (error/warn/info) */
.lint-row{padding:7px 10px;border-left:3px solid var(--line);background:var(--panel2);margin-bottom:4px;font-size:12px;border-radius:0 4px 4px 0}
.lint-row.error{border-color:#f85149}
.lint-row.warn{border-color:#e3b341}
.lint-row.info{border-color:var(--accent)}
```

## Folder tree pattern

For showing nested folder structure with click-to-drill:

```js
async function loadFolderTree() {
  const tree = await (await fetch('/api/folder-tree')).json();
  renderFolderNode(tree, document.getElementById('folderTreeView'));
}
function renderFolderNode(node, container) {
  container.innerHTML = '';
  const rootEl = el('div', 'folder-tree');
  // Root
  const rootNode = el('div', 'node', '', { onclick: () => renderFolderNotes(null) });
  rootNode.innerHTML = `<span class="ico">📚</span><span>All notes</span><span class="count">${countAll(node)}</span>`;
  rootEl.appendChild(rootNode);
  // Children with recursive nesting via .children wrapper
  const childrenWrap = el('div', 'children');
  for (const name of Object.keys(node.children || {}).sort()) {
    const child = node.children[name];
    const childEl = el('div', 'folder-branch');
    const childNode = el('div', 'node', '', { onclick: (e) => { e.stopPropagation(); renderFolderNotes(child); } });
    childNode.innerHTML = `<span class="ico">📁</span><span>${esc(name)}</span><span class="count">${child.count}</span>`;
    childEl.appendChild(childNode);
    if (Object.keys(child.children || {}).length) {
      const subWrap = el('div', 'children');
      for (const subName of Object.keys(child.children).sort()) {
        const sub = child.children[subName];
        const subNode = el('div', 'node', '', { onclick: (e) => { e.stopPropagation(); renderFolderNotes(sub); } });
        subNode.innerHTML = `<span class="ico">↳</span><span>${esc(subName)}</span><span class="count">${sub.count}</span>`;
        subWrap.appendChild(subNode);
      }
      childEl.appendChild(subWrap);
    }
    childrenWrap.appendChild(childEl);
  }
  rootEl.appendChild(childrenWrap);
  container.appendChild(rootEl);
}
function el(tag, cls, html, attrs) {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (html) e.innerHTML = html;
  if (attrs) for (const k in attrs) { e.setAttribute(k, attrs[k]); if (k.startsWith('on') && typeof attrs[k] === 'function') e[k] = attrs[k]; }
  return e;
}
```

The `el()` helper avoids `document.createElement` boilerplate and supports both attrs (`'data-x'`) and direct event handlers.

## Browser verification gotcha

`browser_snapshot` does **not** capture lazy-loaded content. If your new tab fetches data only on click, the snapshot will show only the static page heading, not the populated tables.

Verification pattern:

```js
// In browser_console expression:
(async () => {
  await loadStats();  // force-load
  return document.querySelector('div.page[data-page="stats"]').innerText.slice(0, 1500);
})()
```

Note: `(async () => {...})()` returns a Promise. browser_console will await it and return the resolved value.

If the tab has no data loader function visible (e.g. you just added it), also call `switchPage('tabname')` to trigger the lazy-load:

```js
(async () => {
  switchPage('stats');
  await new Promise(r => setTimeout(r, 500));  // let fetch resolve
  return document.querySelector('div.page[data-page="stats"]').innerText.slice(0, 1500);
})()
```

## Common pitfalls

1. **Forgetting to import `timezone` in new endpoint helpers** — every `_core()` function that uses `datetime.now(timezone.utc)` or compares aware datetimes needs `from datetime import datetime, timezone` at the top. A missing import raises `NameError: timezone is not defined` only when the route is hit.

2. **Trusting `browser_snapshot` for lazy-loaded tabs** — see Browser verification gotcha above. Use `browser_console` instead.

3. **Calling `loadAll()` once on page load when you have 6 new tabs** — fetches everything upfront, slow first paint, harder to debug. Use the lazy-load pattern.

4. **Naive datetime comparison crash** — see CRITICAL pitfall above. Affects recent-activity, stale-notes, vault-stats freshness, and any other "last N days" logic.

5. **Editing the source file without restarting** — the systemd unit keeps the old process. Always `systemctl --user restart <service>` after dashboard edits and verify with `curl -s -o /dev/null -w "%{http_code} %{size_download}\n"`.

6. **Tag chip click handler triggers row click** — wrap with `event.stopPropagation()` so clicking a tag does not also click the note row behind it.

7. **Duplicate-canvas bug for new graph instances** — if the existing dashboard has a single `#graph` canvas, do not create `#graph2` for a new page. Either move the same canvas via `appendChild` to the new container, or expose `resizeGraph()` so the page switcher can call it.

8. **Negative `age_minutes` from clock skew** — if a note's mtime is in the future (system clock drifted), naive `now - dt` produces negative minutes. Wrap with `max(0, int(...))` in the API or the UI.

9. **Adding many endpoints without syntax-checking** — `python3 -c "import ast;ast.parse(open('dashboard.py').read())"` between patches catches syntax errors before the systemd restart fails.

10. **Inline patching a giant `<style>` block with `patch`** — use atomic Python regex replacement via `re.sub(r'<style>.*?</style>', new_css, src, flags=re.DOTALL)`. The existing `restyling-to-telemetry-design-language.md` reference covers this in detail.

## Verification checklist

- [ ] New tab buttons appear in `.page-tabs` row in correct order
- [ ] Page divs have stable IDs matching what JS targets
- [ ] Backend endpoints return correct shape (curl each one separately)
- [ ] `systemctl --user restart <service>` succeeds; no journal tracebacks
- [ ] `python3 -c "import ast;ast.parse(...)"` passes
- [ ] `curl http://localhost:<port>/api/<new>` returns expected JSON
- [ ] Browser: switching to each new tab populates content within ~500ms
- [ ] `browser_console` confirms tab innerText shows populated tables, not just headings
- [ ] Quick capture POST creates a real file with proper frontmatter (verify with `find` + `cat`)
- [ ] Pinned notes survive browser refresh (localStorage persistence)
- [ ] No JS errors in browser console on any tab
