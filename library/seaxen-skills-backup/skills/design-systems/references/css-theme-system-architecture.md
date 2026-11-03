# CSS Variable Theme System for Multi-Brand Dashboards

Architecture for dashboards that need switchable themes (e.g., brand themes, user themes) without JavaScript style manipulation.

## File Structure

```
static/
├── themes/
│   ├── default.css      ← Default theme CSS variables
│   ├── tinybird.css     ← Alternative theme CSS variables
│   └── <name>.css       ← More themes
├── js/
│   └── theme.js         ← Theme manager (load/save/switch)
└── index.html           ← All styling uses var() references
```

## Theme CSS File Pattern

Each theme file defines CSS variables on `:root` (for default) or `[data-theme="name"]` (for alternatives):

```css
/* themes/default.css — loaded always as base */
:root {
  --bg: #0a0a0f;
  --card: #12121a;
  --card-border: rgba(255,255,255,.08);
  --accent: #ffac02;
  --text: #f1f5f9;
  --muted: #94a3b8;
  --radius: 10px;
  --font-base: 15px;
  /* ... all tokens */
}
```

```css
/* themes/tinybird.css — loaded on demand */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;600&display=swap');

[data-theme="tinybird"] {
  --bg: #000000;
  --card: #111113;
  --card-border: #27272A;
  --accent: #00E67A;
  --text: #FFFFFF;
  --muted: #A1A1AA;
  --radius: 16px;
  --font-base: 16px;
  /* ... all tokens */
}

/* Override component styles that can't be pure CSS variables */
[data-theme="tinybird"] body {
  font-family: 'Inter', sans-serif;  /* Theme-specific font */
}
[data-theme="tinybird"] .card {
  backdrop-filter: none;  /* Kill glassmorphism for flat themes */
  border-radius: 20px;
}
```

## Theme Manager JS

```javascript
(function() {
  const THEMES = {
    default: { name: 'Amber Dark', css: '/static/themes/default.css' },
    tinybird: { name: 'Tinybird', css: '/static/themes/tinybird.css' },
  };

  function getTheme() { return localStorage.getItem('theme') || 'default'; }
  
  function setTheme(id) {
    localStorage.setItem('theme', id);
    applyTheme(id);
  }

  function applyTheme(id) {
    document.querySelectorAll('link[data-theme-css]').forEach(l => l.remove());
    
    if (id === 'default') {
      document.documentElement.removeAttribute('data-theme');
    } else {
      document.documentElement.setAttribute('data-theme', id);
    }

    if (id !== 'default' && THEMES[id]) {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = THEMES[id].css;
      link.setAttribute('data-theme-css', id);
      document.head.appendChild(link);
    }

    // Re-render charts with new colors
    if (typeof refreshAll === 'function') setTimeout(refreshAll, 100);
  }

  // Auto-apply on load
  applyTheme(getTheme());
  window.ThemeManager = { getTheme, setTheme, applyTheme, THEMES };
})();
```

## Chart.js Theme Integration

Charts must read CSS variables at render time (not at load time), since themes change dynamically:

```javascript
function cv(name) { 
  return getComputedStyle(document.documentElement).getPropertyValue(name).trim(); 
}

function updateChartDefaults() {
  Chart.defaults.color = cv('--muted');
  Chart.defaults.borderColor = cv('--card-border');
}

// In chart creation:
new Chart(el, {
  data: { datasets: [{
    borderColor: cv('--chart-line'),      // Read variable at render time
    backgroundColor: cv('--chart-fill'),
  }]}
});
```

## Critical Rules

1. **NEVER hardcode colors in index.html** — ALL colors must reference `var(--token)`.
2. **Default theme loads via `<link>`** in `<head>`. Alternative themes load via JS `appendChild`.
3. **Fonts per theme** — use `@import` inside theme CSS + override `body { font-family }`.
4. **Component overrides** that need more than CSS variables (removing glassmorphism, changing border-radius, disabling text-shadow) go as `[data-theme="name"] .class { }` rules in the theme CSS file.
5. **localStorage persistence** — user's choice survives page refresh.
6. **Chart.js colors** — always read via `cv()` at render time, never cached.
7. **Re-render charts** after theme switch — `setTimeout(refreshAll, 100)` after applying.
