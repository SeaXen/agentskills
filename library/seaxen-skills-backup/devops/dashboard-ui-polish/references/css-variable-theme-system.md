# CSS Variable-Based Multi-Theme System

Pattern for dashboards needing 2+ switchable themes without code duplication.

## Architecture

```
static/
├── themes/
│   ├── default.css    ← :root { --bg: ...; --accent: ...; }
│   └── tinybird.css   ← [data-theme="tinybird"] { --bg: ...; }
├── js/
│   └── theme.js       ← Theme manager (localStorage, apply, dropdown builder)
└── index.html          ← ALL styling uses var() — zero hardcoded colors
```

## Theme CSS File Pattern

Default theme uses `:root` selector. All other themes use `[data-theme="name"]`:

```css
/* default.css */
:root {
  --bg: #0a0a0f;
  --card: #12121a;
  --accent: #ffac02;
  --text: #f1f5f9;
  --muted: #94a3b8;
  --radius: 10px;
  --font-base: 15px;
}
```

```css
/* tinybird.css */
[data-theme="tinybird"] {
  --bg: #0a0a0a;
  --card: #151515;
  --accent: #27f795;
  --text: #ffffff;
  --muted: #8d8d8d;
  --radius: 4px;
  --font-base: 16px;
}
```

## Overrides for Structural Differences

When themes need different component STRUCTURE (not just colors), add overrides in the theme CSS:

```css
/* Tinybird has flat cards, no glassmorphism */
[data-theme="tinybird"] .card {
  backdrop-filter: none;
  background: var(--card);
  box-shadow: none;
}
[data-theme="tinybird"] body {
  font-family: 'Roboto', sans-serif;
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
    if (typeof refreshAll === 'function') setTimeout(refreshAll, 100);
  }
  applyTheme(getTheme());
  window.ThemeManager = { getTheme, setTheme, applyTheme, THEMES };
})();
```

## Key Rules

1. Zero hardcoded colors in index.html — every color/size/radius/font MUST be a CSS variable
2. Chart.js needs runtime color reads — use getComputedStyle() when creating charts
3. Font families can differ per theme — override body font-family in theme CSS
4. Component structure can differ — glassmorphism vs flat, rounded vs sharp
5. Persist choice in localStorage — theme survives refresh
6. Load theme CSS dynamically — don't bundle all themes in head

## Pitfalls

- Don't put backdrop-filter:blur() in base CSS if any theme needs flat cards
- oklab() computed values: Chrome 111+ returns colors as oklab(), convert to hex for theme values
- Chart.js caches colors — must call refreshAll() or destroy/recreate charts after theme switch
