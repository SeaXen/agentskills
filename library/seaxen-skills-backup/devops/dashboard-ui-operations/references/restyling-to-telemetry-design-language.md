# Restyling a Hermes dashboard to match `hermes-telemetry` design language

Use this reference when the user asks for a Hermes self-hosted dashboard to look "like `hermes-telemetry`", "like the telemetry dashboard", or any other cross-dashboard visual reference. The pattern below was used to bring the Obsidian vault dashboard (`:6065`) up to par with `hermes-telemetry` (`:8009`) without breaking the legacy JS.

## When to use
- User explicitly names another Hermes dashboard as the design target.
- User gives a screenshot of `hermes-telemetry` (or another Hermes dashboard) and says "make mine look like this".
- A Hermes dashboard still uses the older purple/blue glassmorphic theme and the user calls it "ugly" or "not as clean as telemetry".

## Design-language snapshot of `hermes-telemetry`

`/root/.hermes/plugins/hermes-telemetry/dashboard/index.html` is the reference. Key tokens:
- Background `#0f1117`, panels `#161b22`, panel2 `#1c2128`, panel3 `#21262d`
- Lines `#30363d` / `#484f58` / `#6e7681`
- Text `#c9d1d9` / `#e6edf3` / `#f0f6fc`
- Muted `#8b949e` / `#7d8590` / `#6e7681`
- Accent `#58a6ff` (blue), green `#3fb950`, yellow `#d29922`, purple `#bc8cff`, red `#f85149`
- `border-radius: 8px` for cards, `6px` for chips
- Stat cards: `padding: 16px`, value `font-size: 22-24px`, label `text-transform: uppercase`, color-coded per stat
- Tables: `#30363d` header underline, `font-size: 13px`, hover `#1c2128` row, no zebra striping
- Header: `padding: 14px 24px`, brand left, page-tabs as pill buttons next to it, `Refresh` and gear settings on the right
- Page tabs: pill-shaped, `#21262d` background, gradient `#1f6feb → #1a4f9c` when active, cyan border glow
- Buttons: flat `#21262d`, `border: 1px solid #30363d`, hover `#30363d`

## Step-by-step recipe

### 1. Read the existing file once, plan in one shot
- Find the `<style>` block via regex: `re.search(r'<style>.*?</style>', src, re.DOTALL)`
- Find every HTML class name that the legacy JS produces: `grep -oE 'class="[a-zA-Z][^"]*"' file.py | sort -u`
- Decide: full CSS swap (if file has very few legacy class names) vs append-overlay (if many).

### 2. Full CSS swap pattern (used for Obsidian dashboard at `:6065`)

When the JS uses < ~30 unique class names, do a full swap. The atomic regex approach is the right tool:

```python
import re
src = open('/path/to/dashboard.py').read()
new_css = open('/tmp/new_css.txt').read()
m = re.search(r'<style>.*?</style>', src, re.DOTALL)
assert m, "no <style> block found"
out = src[:m.start()] + new_css + src[m.end():]
open('/path/to/dashboard.py','w').write(out)
```

Do **not** use `patch` for a 200+ line CSS block — `old_string` matching on a giant CSS block is fragile. Python regex is the right tool.

### 3. Add a legacy compatibility shim inside the new `<style>`

If the legacy JS still emits `.item`, `.panelHead`, `.actionBtn`, `.graphAside`, etc., alias them to the new tokens at the bottom of the new CSS:

```css
.note-row,.item{padding:10px 12px;border:1px solid var(--line);border-radius:6px;background:var(--panel2);cursor:pointer}
.actionBtn,.ghostBtn,.chip,.filterBtn,.tabBtn{background:var(--panel3);color:var(--text);border:1px solid var(--line);border-radius:6px;padding:6px 12px;font-size:12px;font-weight:500;cursor:pointer}
.chip.active,.filterBtn.active{background:linear-gradient(180deg,#1f6feb 0%,#1a4f9c 100%);border-color:var(--accent);color:#fff}
```

This keeps the existing JS working (`renderList`, `renderTopStats`, `renderCluster`) without rewriting it.

### 4. Restructure the header + add a page-tab system

Replace the brand-style header with the telemetry pattern:
- Brand on the left (`h1` with `<span class="accent">` for the colored bit)
- Page tabs as a row of pill buttons: `Home / Notes / Graph / Recall / Health / Review`
- Status text + Refresh button + (optional) gear menu on the right

Wrap each page in `<div class="page" data-page="...">` and add JS:

```js
function switchPage(name) {
  document.querySelectorAll('.page-tab').forEach(b => b.classList.toggle('active', b.dataset.page === name));
  document.querySelectorAll('.page').forEach(p => p.classList.toggle('active', p.dataset.page === name));
  // optional per-page data fetch
}
```

### 5. Add a stat-card hero strip

Each stat card:
```html
<div class="stat-card green"><div class="value">98.4</div><div class="label">Overall health</div></div>
```

CSS:
```css
.stat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}
.stat-card{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:16px;text-align:center}
.stat-card .value{font-size:22px;font-weight:700;color:var(--text-strong);font-variant-numeric:tabular-nums}
.stat-card .label{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin-top:4px}
.stat-card.green .value{color:var(--accent2)}
```

Use a small render helper for JS-side population:
```js
function renderStatGrid(id, items) {
  document.getElementById(id).innerHTML = items.map(([v,l,c,s]) =>
    `<div class="stat-card${c?' '+c:''}"><div class="value">${v}</div><div class="label">${l}</div>${s?`<div class="sub">${s}</div>`:''}</div>`
  ).join('');
}
```

### 6. Replace blob cards with proper tables

The telemetry dashboard uses real `<table>` for breakdowns, not stacked cards. Each panel becomes:
```html
<div class="panel">
  <div class="panel-head"><h3>Vault overview</h3><span class="meta">live</span></div>
  <div class="panel-body">
    <table><thead><tr><th>...</th></tr></thead><tbody id="folderTable"></tbody></table>
  </div>
</div>
```

CSS for the panel + table:
```css
.panel{background:var(--panel);border:1px solid var(--line);border-radius:8px;margin-bottom:20px;overflow:hidden}
.panel-head{padding:14px 18px 12px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:center}
.panel-head h3{font-size:14px;font-weight:600;color:var(--text-strong);margin:0}
th{text-align:left;color:var(--muted);font-weight:600;text-transform:uppercase;font-size:10px;letter-spacing:.5px;padding:8px 12px;border-bottom:1px solid var(--line)}
td{padding:10px 12px;border-bottom:1px solid rgba(48,54,61,.5);color:var(--text);font-size:13px}
tr:hover td{background:var(--panel2)}
```

### 7. Populate tables from existing API endpoints

For the Obsidian dashboard, the relevant endpoints are:
- `/api/graph` — returns `{notes, links, folder_counts, tag_counts, vault, vault_display}` (the right one for everything; `/api/notes` does not exist)
- `/api/memory-health` — `{overall_score, scores{structure, link_health, recall, review_flow, noise_control}, counts{notes, links, broken_links, orphans}, recommendations[], recall_eval{case_count, hit_at_k, mrr}, review_queue{pending, reviewed_total}}`
- `/api/recall-eval` — eval cases for the Recall table
- `/api/memory-review` — review queue candidates

In the new `loadAll()` function, fetch all of these once on page load and populate the stat cards + tables.

### 8. Hook legacy functions WITHOUT calling the original

If you wire page tabs to the existing `runMemoryHealth` / `runRecallEval` / `runMemoryReviewQueue`, the original implementations often switch to a legacy `state.workspace` model that hijacks the new tab UI. The fix:

```js
// ❌ DON'T — calls original which switches workspace
window.runMemoryHealth = async function() {
  if (_orig) await _orig();
  // my new logic
};

// ✅ DO — fetch API directly, render into new tables
window.runMemoryHealth = async function() {
  const h = await (await fetch('/api/memory-health')).json();
  // populate new DOM ids
};
```

### 9. Handle init race conditions with legacy code

The legacy `load()` function is fragile — it often throws partway. Wrap new init in a `setTimeout` so it runs after the legacy code has had a chance:

```js
if (typeof window !== 'undefined') {
  setTimeout(() => {
    if (typeof loadAll === 'function') {
      loadAll().catch(e => console.error('initial loadAll failed', e));
    }
  }, 250);
}
```

### 10. Restart and verify live

```bash
systemctl --user restart <service>
sleep 2
curl -s -o /dev/null -w "HTTP %{http_code} | %{size_download} bytes\n" http://localhost:<port>/
```

The service runs from disk. Editing the source file alone does nothing — the systemd unit keeps the old process alive with the old code in memory. Always restart after edits.

## Pitfalls

- **The `wrap` legacy div is layout-critical.** If the old layout uses `<div class="wrap">` for grid arrangement, set `.wrap{display:contents}` in the new CSS so it does not visually take up space, but its children still participate in the parent grid.
- **`/api/notes` may not exist; use `/api/graph`.** Many Hermes dashboards expose only the aggregated `/api/graph` endpoint with everything you need.
- **`renderList()` uses `<div class="item">`, not `.note-row`.** Always check legacy class names in the JS before writing CSS that targets only the new names.
- **The old `setWorkspace()` call can hijack the new tab UI.** When hooking legacy functions, never call the original implementation if it switches to a legacy workspace/state model.
- **A failing legacy `load()` can block the new `loadAll()`.** Always wrap new init in `setTimeout` or `try/catch` so a legacy bug does not freeze the new UI.
- **Color-coded stat values need their own CSS rules.** `stat-card.green .value { color: var(--accent2); }` — do not forget the modifier class.
- **Hex colors with full `#ffffff` for active state are intentional.** Active buttons use solid white text on the blue gradient; do not downgrade to muted text.
- **Do not skip `systemctl --user restart`.** The systemd unit caches the old Python process; an HTTP 200 response before restart means the old code is still serving. Always restart.

## Verification

After the change:
- `curl /` returns HTTP 200 and the response size should drop (CSS got smaller)
- `curl /api/memory-health` returns the same shape as before
- `systemctl --user is-active <service>` is `active`
- Browser navigation to `http://localhost:<port>/` shows:
  - stat cards populated with live numbers
  - all four home-page tables filled (vault overview, health breakdown, recent dailies, top tags)
  - page tabs switching actually swaps content
  - no JS errors in browser console
- `journalctl --user -u <service> -n 50` shows no recent Python tracebacks

## Real-world example: Obsidian dashboard `:6065`

Before: 213KB monolithic Python file, 32KB of purple/blue glassmorphic CSS, single 3-column workspace that looked "ugly" vs `hermes-telemetry`.

After:
- ~220KB file (CSS went from 32KB → 12KB + ~10KB legacy shim)
- 6 telemetry-style page tabs: Home / Notes / Graph / Recall / Health / Review
- Home page has 6 stat cards (98.4 overall, 61 notes, 236 links, 0 broken, 0.91 MRR, 12 review)
- Health page has 6 stat cards + recommendations + broken/orphan tables
- Review page has 4 stat cards + queue cards
- Recall page has a 50-row eval table
- All legacy JS (graph force-sim, notes list, reader, minimap) keeps working unchanged thanks to the shim
- 0 changes to backend Python logic, Mnemosyne integration, cron, or watchdog
