# CSS-Variable Theme System Pattern

Use when a dashboard needs multiple visual themes (light/dark, branded variants) that switch at runtime without page reload.

## Architecture

```
static/
├── themes/
│   ├── default.css    ← :root { --bg: #0a0a0f; ... }
│   └── tinybird.css   ← [data-theme="tinybird"] { --bg: #000000; ... }
├── js/
│   └── theme.js       ← Theme manager (localStorage, CSS loading, chart refresh)
└── index.html          ← All styling uses var() references
```

### default.css
Defines CSS variables on `:root` — the default theme loads always as the base stylesheet via `<link rel="stylesheet" href="/static/themes/default.css">`.

### Variant themes
Each variant uses `[data-theme="name"]` selector on `html` element. Loaded dynamically by theme.js when selected.

### theme.js pattern
```javascript
(function() {
  const THEMES = {
    default: { name: 'Amber Dark', css: '/static/themes/default.css' },
    tinybird: { name: 'Tinybird', css: '/static/themes/tinybird.css' },
  };
  function getTheme() { return localStorage.getItem('app-theme') || 'default'; }
  function setTheme(id) {
    localStorage.setItem('app-theme', id);
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
  applyTheme(getTheme());
  window.ThemeManager = { getTheme, setTheme, applyTheme, buildDropdown, THEMES };
})();
```

## CSS Variable Categories

Every theme must define ALL these variables (no missing = broken UI):

```css
:root {
  /* Backgrounds */
  --bg; --card; --card-border; --glass; --glass-border;
  /* Accent */
  --accent; --accent-bright; --accent-dim; --accent-glow;
  /* Semantic colors */
  --blue; --green; --red; --purple; --cyan; --orange;
  /* Text */
  --text; --text-secondary; --muted; --dim;
  /* Structural */
  --header-border; --th-color;
  /* Badge variants */
  --badge-free-bg; --badge-free-color;
  --badge-paid-bg; --badge-paid-color;
  --badge-active-bg; --badge-active-color;
  --badge-error-bg; --badge-error-color;
  --badge-warn-bg; --badge-warn-color;
  --badge-gray-bg; --badge-gray-color;
  /* Charts */
  --chart-line; --chart-fill; --chart-point; --chart-bar; --chart-bar-border;
  /* Spacing & Shape */
  --radius; --radius-sm; --font-base; --font-small; --font-xs; --font-mono;
  --header-bg; --header-height;
}
```

## Pitfalls

1. **Base styles not in CSS variables need explicit overrides.** If the main stylesheet hardcodes `backdrop-filter: blur(10px)` on `.card`, the variant theme CSS must explicitly override: `[data-theme="tinybird"] .card { backdrop-filter: none; }`. Same for `font-family`, `text-shadow`, `border-radius` on specific components.

2. **Chart.js reads colors at render time.** After theme switch, charts must be destroyed and recreated. Call `refreshAll()` after `applyTheme()`. Use `cv('--chart-line')` helper to read CSS vars into Chart.js config.

3. **Font loading per theme.** If a theme uses a different font family (e.g., Roboto vs Inter), add `@import url(...)` at the top of the theme CSS. Browser will cache it.

4. **Theme switcher dropdown in header.** Keep it simple: `<select>` element styled with theme variables. Persist to `localStorage`. Initialize value on page load from `ThemeManager.getTheme()`.

5. **Don't share color values between themes.** Each theme CSS file should be fully self-contained with ALL variable values. No inheritance assumptions.
