# SeaDash Professional Header Refactor — Additive Pattern

## Context
SeaDash (Hermes self-hosted dashboard) needed a professional header redesign matching a reference Home Assistant-style dashboard. The original had 189+ class definitions that would be lost if the entire stylesheet was replaced.

## Solution: Additive CSS Overlay

### Technique
Instead of replacing the entire `<style>` block, inject a second `<style id="pro-header">` block **after** the original, before `</head>`.

```python
# In Python or sed:
# 1. Read original CSS from /tmp/seadash_pro_header.css
# 2. Inject before </head>
inject = '\n<style id="pro-header">\n' + css + '\n</style>\n'
html = html.replace('</head>', inject + '</head>', 1)
```

### Why It Works
- Original 189 class definitions remain intact (`.card-stat`, `.card-action-btn`, `.layout-toolbar`, `.settings-group`, `.sysinfo-grid`, `.section-icon`, etc.)
- New CSS overrides visual properties via specificity + `!important` where needed
- Zero risk of losing layout/behavior classes

## Header Redesign Spec (from reference image)

### Layout
```
[Logo + Brand]          [Metrics Pill: Load/RAM/Disk/Servers/Temp/Time]          [Bell | Search | +Add App | Grid | List | Theme | Settings]
```
- Height: 64px fixed
- Sticky, frosted glass backdrop (`rgba(10,10,18,0.92)` + blur(20px))
- Three zones: flex-start / flex:1 / flex-end

### CSS Classes Added
```css
/* Metrics pill */
.stats-bar, .metrics-pill { display:flex; border-radius:999px; max-width:520px; flex:1; }
.metric-item { border-right: 1px solid rgba(255,255,255,0.05); }
.metric-icon { width:22px; height:22px; border-radius:6px; }
/* Colors: load=amber, ram=pink, disk=cyan, servers=blue, temp=orange */

/* Right zone */
.alert-trigger { width:40px; height:40px; } /* bell with badge */
.search-wrapper { flex:0 0 280px; }
.btn-add { gradient cyan→blue; }
.icon-btn-group { gap:6px; }
/* Grid/List/Theme/Settings icons */
```

### HTML Structure
```html
<div class="header">
  <div class="header-left">
    <div class="logo">🌊</div>
    <div class="header-brand">
      <h1>SeaDash</h1>
      <div class="header-subtitle">SERVER DASHBOARD</div>
    </div>
  </div>
  <div class="stats-bar metrics-pill" id="stats-bar">
    <div class="metric-item"><div class="metric-icon load">⚡</div><div class="metric-value" id="stat-load">--</div></div>
    <div class="metric-item"><div class="metric-icon ram">🧠</div><div class="metric-value" id="stat-ram"><span>--</span><span class="metric-sub">/ --</span></div></div>
    <div class="metric-item"><div class="metric-icon disk">💾</div><div class="metric-value ok" id="stat-disk">--</div></div>
    <div class="metric-item"><div class="metric-icon servers">🖥️</div><div class="metric-value" id="stat-servers">--</div></div>
    <div class="metric-item"><div class="metric-icon temp">🌡️</div><div class="metric-value warn" id="stat-temp">--</div></div>
    <div class="metric-time"><span>🕐</span><span id="stat-time">--:--:--</span></div>
  </div>
  <div class="header-right">
    <div class="alert-trigger" onclick="toggleAlerts()"><span class="alert-badge" id="alert-badge">0</span>🔔</div>
    <div class="search-wrapper"><span class="search-icon">🔍</span><input class="search-box" id="search" placeholder="Search apps..."></div>
    <button class="btn-add" onclick="openAddModal()">+ Add App</button>
    <div class="icon-btn-group">
      <button class="icon-btn" onclick="setView('grid')">⊞</button>
      <button class="icon-btn" onclick="setView('table')">☰</button>
      <button class="icon-btn theme" onclick="cycleTheme()">🎨</button>
      <button class="icon-btn settings" onclick="openSettings()">⚙️</button>
    </div>
  </div>
</div>
```

## renderStats() Update

### New Element IDs
```javascript
// Must match HTML IDs exactly
const set = (id, txt, cls) => { const el = q(`#${id}`); if (el) { el.textContent = txt; if (cls) el.className = 'metric-value ' + cls; } };
const setHtml = (id, html) => { const el = q(`#${id}`); if (el) el.innerHTML = html; };

set('stat-load', load.toFixed(2), loadCls);
setHtml('stat-ram', `<span>${memUsed.toFixed(1)}</span><span class="metric-sub">/ ${memTotal.toFixed(1)}GB (${memPct.toFixed(1)}%)</span>`);
set('stat-disk', diskPct.toFixed(1) + '%', 'ok ' + diskCls);
set('stat-servers', `${docker_running}/${docker_total}`);
set('stat-temp', temp + '°C', tempCls);
set('stat-time', now.toLocaleTimeString());
```

### Color Classes
- `ok` = green (#34d399)
- `warn` = amber (#fbbf24)  
- `crit` = red (#f87171)

### Placement Critical: Define BEFORE Export
```javascript
// In main app IIFE (third script block):
function renderStats() { ... }

Object.assign(window, { 
  ..., 
  renderStats  // MUST be in export list
});
```
**Wrong:** Defined after `Object.assign` → not exported
**Wrong:** Defined in wrong IIFE scope → `STATE.stats` undefined

## Verification Checklist (run in browser console)

```javascript
// 1. Function exists
typeof window.renderStats === 'function'

// 2. Elements exist
['stat-load','stat-ram','stat-disk','stat-servers','stat-temp','stat-time'].every(id => !!document.getElementById(id))

// 3. Close modal works
typeof window.closeModal === 'function'

// 4. All modals present
document.querySelectorAll('.modal-overlay').length === 9

// 5. Theme cycle works
cycleTheme(); document.documentElement.getAttribute('data-theme')
```

## Files Modified in This Refactor
- `/mnt/tb/1Apps/SeaDash/index.html` — additive CSS overlay, header HTML replacement, renderStats() update

## Related Patterns
- `references/additive-css-overlay-pattern.md` — generic technique
- `references/surgical-html-replacement.md` — exact-string replacement method
- `references/iife-scope-function-export.md` — IIFE scope rules for function exports