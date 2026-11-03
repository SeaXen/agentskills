# Cmd-K palette + inline SVG sparklines + flat nav

Concrete code, CSS, and verification recipes for the three highest-impact
"feel premium" patterns you can ship on a dense operator dashboard after the
shared layout is settled.

## 1. Cmd-K palette (Ctrl/Cmd+K and `/`)

### Files
- `static/js/cmd-k.js` — owns modal state, fuzzy search, keyboard nav.
- `static/index.html` — modal markup right before `</body>`; trigger button in nav header.
- `static/css/layout-v2.css` (or your layout file) — palette + trigger styles.

### Loading order in `index.html`
```html
<script src="/static/js/core.js?v=N" defer></script>
<script src="/static/js/search-ui.js?v=N" defer></script>
<script src="/static/js/cmd-k.js?v=N" defer></script>   <!-- NEW -->
<script src="/static/js/theme.js" defer></script>
<script src="/static/js/dashboard.js?v=M" defer></script>
```

`cmd-k.js` must come **before** `dashboard.js` so `openCmdK` is on `window`
when nav markup references `onclick="openCmdK()"`.

### Full `static/js/cmd-k.js`
```js
/* AceRoute command palette — Cmd/Ctrl+K */
(function (global) {
  'use strict';
  var AR = global.AceRoute = global.AceRoute || {};
  var PAGES = [
    { id: 'home',       label: 'Home',       group: 'Pages'   },
    { id: 'sessions',   label: 'Sessions',   group: 'Pages'   },
    /* one entry per top-level page */
    { id: '__refresh__', label: 'Refresh current page',        group: 'Actions', action: 'refresh'  },
    { id: '__settings__', label: 'Settings',                   group: 'Actions', action: 'settings' },
    { id: '__export__',  label: 'Export CSV (current window)', group: 'Actions', action: 'export'   }
  ];
  var state = { open: false, items: [], sel: 0, q: '' };

  function score(q, text) {
    if (!q) return 1;
    var i = text.toLowerCase().indexOf(q.toLowerCase());
    return i < 0 ? 0 : (100 - i);
  }
  function refreshItems() {
    var q = (state.q || '').trim();
    var scored = PAGES.map(function (p) {
      return { p: p, s: Math.max(score(q, p.label), score(q, p.id)) };
    }).filter(function (x) { return x.s > 0; });
    scored.sort(function (a, b) { return b.s - a.s; });
    state.items = scored.slice(0, 12).map(function (x) { return x.p; });
    state.sel = 0;
  }
  function render() {
    var list = document.getElementById('cmdkList');
    if (!list) return;
    var lastGroup = '';
    list.innerHTML = state.items.map(function (it, i) {
      var head = it.group && it.group !== lastGroup ? '<div class="cmdk-group">' + it.group + '</div>' : '';
      lastGroup = it.group || lastGroup;
      var cls = 'cmdk-item' + (i === state.sel ? ' active' : '');
      var safeId = String(it.id).replace(/[<>]/g, '');
      return head + '<div class="' + cls + '" data-idx="' + i + '" onclick="window.AceRoute && window.AceRoute.cmdkSelect(' + i + ')">' +
        '<span class="cmdk-item-label">' + AR.escapeHtml(it.label) + '</span>' +
        '<span class="cmdk-item-id">' + AR.escapeHtml(safeId) + '</span></div>';
    }).join('') || '<div class="cmdk-empty">No matches</div>';
  }
  function open() {
    var overlay = document.getElementById('cmdkOverlay');
    if (!overlay) return;
    state.q = '';
    var input = document.getElementById('cmdkInput');
    if (input) input.value = '';
    refreshItems();
    render();
    overlay.hidden = false;
    state.open = true;
    setTimeout(function () { if (input) input.focus(); }, 10);
  }
  function close() {
    var overlay = document.getElementById('cmdkOverlay');
    if (!overlay) return;
    overlay.hidden = true;
    state.open = false;
  }
  function select(i) {
    var it = state.items[i];
    if (!it) return;
    close();
    if (it.action === 'refresh')  { if (window.refreshCurrentPage) window.refreshCurrentPage(); return; }
    if (it.action === 'settings') { if (window.toggleSettingsPopover) window.toggleSettingsPopover(true); return; }
    if (it.action === 'export')   { window.location.href = '/api/export/csv' + (window.dateParams ? window.dateParams() : ''); return; }
    if (window.switchPage) window.switchPage(it.id);
  }
  function isTypingTarget(el) {
    if (!el) return false;
    var tag = (el.tagName || '').toLowerCase();
    return tag === 'input' || tag === 'textarea' || tag === 'select' || el.isContentEditable;
  }
  function onKey(e) {
    var meta = e.metaKey || e.ctrlKey;
    if (meta && (e.key === 'k' || e.key === 'K')) {
      e.preventDefault();
      state.open ? close() : open();
      return;
    }
    if (e.key === '/' && !state.open && !isTypingTarget(e.target)) {
      e.preventDefault(); open(); return;
    }
    if (!state.open) return;
    if (e.key === 'Escape') { e.preventDefault(); close(); return; }
    if (e.key === 'ArrowDown') { e.preventDefault(); state.sel = Math.min(state.items.length - 1, state.sel + 1); render(); }
    else if (e.key === 'ArrowUp')   { e.preventDefault(); state.sel = Math.max(0, state.sel - 1); render(); }
    else if (e.key === 'Enter')     { e.preventDefault(); select(state.sel); }
  }
  document.addEventListener('keydown', onKey, true);
  var overlay = document.getElementById('cmdkOverlay');
  if (overlay) overlay.addEventListener('click', function (e) { if (e.target === overlay) close(); });
  var input = document.getElementById('cmdkInput');
  if (input) input.addEventListener('input', function () { state.q = input.value; refreshItems(); render(); });

  AR.cmdkOpen = open; AR.cmdkClose = close; AR.cmdkSelect = select;
  window.openCmdK = open; window.closeCmdK = close;
})();
```

### Modal markup (paste before `</body>`)
```html
<div id="cmdkOverlay" class="cmdk-overlay" hidden role="dialog" aria-modal="true" aria-label="Command palette">
  <div class="cmdk-panel" role="listbox">
    <input id="cmdkInput" class="cmdk-input" type="text" placeholder="Jump to page, run action…" autocomplete="off" spellcheck="false">
    <div id="cmdkList" class="cmdk-list"></div>
    <div class="cmdk-foot"><span><kbd>↑</kbd><kbd>↓</kbd> navigate</span><span><kbd>↵</kbd> select</span><span><kbd>esc</kbd> close</span></div>
  </div>
</div>
```

### Required CSS
```css
/* Trigger button in nav header */
.cmdk-trigger{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:8px;padding:6px 10px;color:var(--muted);font-size:12px;cursor:pointer;transition:border-color .15s,background .15s}
.cmdk-trigger:hover{border-color:rgba(255,172,2,.35);background:rgba(255,172,2,.05);color:var(--text)}
.cmdk-icon{font-weight:700;font-size:13px;opacity:.7}
.cmdk-text{flex:1;text-align:left;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:140px}
.cmdk-kbd{font-family:var(--font-mono);font-size:10px;padding:2px 6px;border-radius:4px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);color:var(--muted)}
/* Modal */
.cmdk-overlay{position:fixed;inset:0;background:rgba(0,0,0,.55);backdrop-filter:blur(6px);z-index:1000;display:flex;align-items:flex-start;justify-content:center;padding-top:14vh}
.cmdk-overlay[hidden]{display:none}
.cmdk-panel{width:min(560px,92vw);background:var(--card,#1a1d23);border:1px solid rgba(255,255,255,.1);border-radius:12px;box-shadow:0 24px 64px rgba(0,0,0,.5);overflow:hidden}
.cmdk-input{width:100%;background:transparent;border:0;border-bottom:1px solid rgba(255,255,255,.08);padding:16px 18px;font-size:15px;color:var(--text);outline:none;font-family:inherit}
.cmdk-input::placeholder{color:var(--muted)}
.cmdk-list{max-height:52vh;overflow-y:auto;padding:6px}
.cmdk-group{padding:10px 12px 4px;font-size:10px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.6px}
.cmdk-item{display:flex;justify-content:space-between;align-items:center;padding:9px 12px;border-radius:6px;cursor:pointer;font-size:14px;color:var(--text);transition:background .1s}
.cmdk-item.active{background:rgba(255,172,2,.12);color:var(--text)}
.cmdk-item:hover{background:rgba(255,255,255,.04)}
.cmdk-item-label{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.cmdk-item-id{font-family:var(--font-mono);font-size:11px;color:var(--muted);margin-left:12px}
.cmdk-empty{padding:24px;text-align:center;color:var(--muted);font-size:13px}
.cmdk-foot{display:flex;gap:16px;padding:8px 14px;border-top:1px solid rgba(255,255,255,.06);background:rgba(0,0,0,.15);font-size:11px;color:var(--muted)}
.cmdk-foot kbd{font-family:var(--font-mono);background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);padding:1px 5px;border-radius:3px;margin-right:2px;font-size:10px}
```

### Live verification
```js
// In browser_console
var ov = document.getElementById('cmdkOverlay');
JSON.stringify({
  hidden: ov.hidden,
  display: getComputedStyle(ov).display,
  items: ov.querySelectorAll('.cmdk-item').length
});
// After Cmd+K: {hidden: false, display: "flex", items: 12}
```

Trigger via `Meta+K` or `Ctrl+K` in `browser_press`. Verify the panel renders
and select handlers land on the correct page.

## 2. Inline SVG sparklines (no Chart.js)

For hero KPI tiles, a 26px SVG sparkline gives trend context without Chart.js
overhead, race conditions during paint rebuilds, or a second canvas.

### Helper (drop in `dashboard.js` or `core.js`)
```js
function sparklineSvg(values, color) {
  var v = (values || []).filter(function(x){ return typeof x === 'number' && isFinite(x); });
  if (v.length < 2) return '';
  var min = Math.min.apply(null, v), max = Math.max.apply(null, v);
  var range = (max - min) || 1;
  var w = 100, h = 26, step = w / (v.length - 1);
  var points = v.map(function(x, i) {
    return (i * step).toFixed(1) + ',' + (h - ((x - min) / range) * h).toFixed(1);
  }).join(' ');
  var area = '0,' + h + ' ' + points + ' ' + w + ',' + h;
  var stroke = color || 'rgba(255,172,2,.85)';
  var fill = color ? color.replace(/\)/, ',.15)') : 'rgba(255,172,2,.15)';
  return '<svg class="kpi-spark" viewBox="0 0 ' + w + ' ' + h + '" preserveAspectRatio="none">' +
    '<polygon points="' + area + '" fill="' + fill + '"/>' +
    '<polyline points="' + points + '" fill="none" stroke="' + stroke + '" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>' +
    '</svg>';
}
```

### CSS
```css
.kpi-spark{display:block;width:100%;height:26px;margin-top:6px}
```

### Wire into heroHtml builder
```js
var tl7 = (d.timeline || []).slice(-7);
var sessionsSeries = tl7.map(function(x){ return Number(x.sessions || 0); });
var tokensSeries   = tl7.map(function(x){ return Number(x.tokens   || 0); });
var costSeries     = tl7.map(function(x){ return Number(x.cost     || 0); });

$('homeSummary').innerHTML =
  heroHtml('Sessions',   t.sessions||0, 'accent', del.sessions_pct, 'switchPage("sessions")', sessionsSeries, '#ffac02') +
  heroHtml('Tokens',     fmtTok(t.tokens||0), 'purple', del.tokens_pct, 'switchPage("models")', tokensSeries, '#a855f7') +
  heroHtml('Cost today', '$' + (t.cost||0), 'green', del.cost_pct, 'switchPage("costs")', costSeries, '#4ade80') +
  /* secondary/tertiary tiles without sparklines */
  ;
```

`heroHtml` signature becomes:
```js
var heroHtml = function(label, val, color, deltaPct, onclickJs, sparkValues, sparkColor) {
  var dCls = deltaPct == null ? '' : (deltaPct > 0.5 ? 'up' : (deltaPct < -0.5 ? 'down' : 'flat'));
  var dStr = deltaPct == null ? '' : '<span class="kpi-delta ' + dCls + '">' + (deltaPct>0?'+':'') + deltaPct.toFixed(1) + '%</span>';
  var oncl = onclickJs ? ' onclick="' + onclickJs + '" style="cursor:pointer"' : '';
  var spark = sparklineSvg(sparkValues, sparkColor);
  return '<div class="card mini-stat model-stat-glow kpi-hero"' + oncl + '><div class="val ' + (color||'accent') + '">' + val + '</div>' + dStr + spark + '<div class="label">' + label + '</div></div>';
};
```

### Verify a sparkline is rendering real data
In `browser_console`:
```js
var svg = document.querySelector('#homeSummary .kpi-hero .kpi-spark polyline');
JSON.stringify({ points: svg ? svg.getAttribute('points') : 'NO_SPARK' });
```
Expected: a points string like `"0.0,7.9 16.7,26.0 33.3,20.3 ..."`, NOT all-zero
or all-on-baseline (which means the series was empty or the field name was wrong).

## 3. Flat primary nav (drop "More ▾")

### HTML pattern
```html
<nav class="top-nav" aria-label="Primary">
  <div class="nav-primary">
    <button class="nav-btn active" data-page="home"     onclick="switchPage('home')">Home</button>
    <button class="nav-btn" data-page="sessions" onclick="switchPage('sessions')">Sessions</button>
    <!-- one button per page -->
  </div>
  <button class="cmdk-trigger" type="button" onclick="openCmdK()" title="Command palette (Ctrl/Cmd+K)" aria-label="Open command palette">
    <span class="cmdk-icon">⌘</span><span class="cmdk-text">Search pages…</span><kbd class="cmdk-kbd">⌘K</kbd>
  </button>
</nav>
```

### CSS
```css
.top-nav{gap:10px}
.nav-primary{display:flex;flex-wrap:nowrap;gap:4px;align-items:center;flex:1;min-width:0;overflow-x:auto;overflow-y:hidden;scrollbar-width:thin}
.nav-primary::-webkit-scrollbar{height:4px}
.nav-primary::-webkit-scrollbar-thumb{background:rgba(255,255,255,.1);border-radius:4px}
.nav-primary .nav-btn{white-space:nowrap;flex-shrink:0}
/* Hide old More ▾ dropdown remnants */
.nav-more, .nav-more-menu, .nav-more-label, .nav-more-btn { display: none !important; }
```

### When to use flat nav vs "More ▾"
- **Flat (this pattern)** when all pages are peer-importance (Sessions, Requests,
  Messages, Models, Tools are all same-tier in an ops dashboard).
- **More ▾ still fine** when the IA genuinely has primary/secondary tiers (e.g.
  primary: Dashboard, Reports, Admin; secondary: Settings, Audit, Logs).

Hiding peer-importance pages behind "More ▾" is an IA smell — users will find
them via Cmd-K anyway.

## 4. Data-shape verification (do this BEFORE writing the wiring code)

**Trap:** guessed field names that don't match the actual API. Example:
```js
// guessed (wrong)
var tokensSeries = tl7.map(function(_, i){
  return Number(tl7[i].input_tokens || 0) + Number(tl7[i].output_tokens || 0);
});
// actual API:
[{day, sessions, tokens, cost}]   // single 'tokens', single 'cost'
```

Symptom: sparkline renders flat-zero line because every series point is 0.

**Fix (always):** before writing series extraction, curl and inspect:
```bash
curl -sS "http://localhost:8866/api/home/dashboard?days=7&fresh=1" \
  | python3 -c 'import sys,json;d=json.load(sys.stdin); print(list((d.get("timeline") or [{}])[0].keys()))'
# Expected: ['day', 'sessions', 'tokens', 'cost']
```

Then write the JS series extraction against the actual keys. Especially watch
for: `input_tokens` vs `tokens`, `cost_usd` vs `cost`, `latency_ms` vs `latency`.

## 5. Pipeline pitfall: Python heredoc with arrow-function JS

When patching JS via `execute_code` and the JS source contains `=>`:
```python
src = """
return (d.timeline || []).slice(-7).map(x => Number(x[f] || 0));
"""
```
**Symptom:** `SyntaxError: invalid syntax` on the `=>` token even though the
JS itself is fine.

**Fix:** don't use Python heredocs for JS source. Use one of:
- `write_file(path, content)` with the raw JS string
- `patch(mode='replace', old_string=..., new_string=...)` for surgical edits
- Shell `cat > file <<'EOF'` (single-quoted heredoc → no shell interpolation → JS stays intact)

When you must use `execute_code`, write the JS to a temp file via Python's
`open()` then verify with `terminal(command='node --check <tmpfile>')`.
