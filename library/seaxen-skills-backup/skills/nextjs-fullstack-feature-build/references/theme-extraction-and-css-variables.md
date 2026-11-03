# Theme Extraction & CSS Variable System

## Extracting a competitor's design system from a live website

When the user says "make the theme like [reference URL]", don't guess from a screenshot. Extract the exact values from the live site using `browser_console`.

### The extraction script

```js
(() => {
  // 1. CSS custom properties (root variables)
  const vars = {};
  for (const sheet of document.styleSheets) {
    try {
      for (const rule of sheet.cssRules) {
        if (rule.style) for (let i = 0; i < rule.style.length; i++) {
          const prop = rule.style[i];
          if (prop.startsWith('--')) vars[prop] = rule.style.getPropertyValue(prop);
        }
      }
    } catch(e) {}
  }

  // 2. Key element computed styles
  const body = getComputedStyle(document.body);
  const h1 = document.querySelector('h1');
  const cta = Array.from(document.querySelectorAll('a, button'))
    .find(b => b.textContent.trim() === 'Start free' || b.textContent.trim() === 'Sign up');

  // 3. Collect all unique bg/text colors on the page
  const bgs = new Set(), colors = new Set();
  for (const el of document.querySelectorAll('*')) {
    const s = getComputedStyle(el);
    if (s.backgroundColor !== 'rgba(0, 0, 0, 0)' && s.backgroundColor !== 'transparent')
      bgs.add(s.backgroundColor);
    if (s.color && s.color !== 'rgb(0, 0, 0)') colors.add(s.color);
  }

  return JSON.stringify({
    cssVars: vars,
    body: { bg: body.backgroundColor, color: body.color, fontFamily: body.fontFamily },
    h1: h1 ? { color: getComputedStyle(h1).color, fontSize: getComputedStyle(h1).fontSize, fontWeight: getComputedStyle(h1).fontWeight } : null,
    cta: cta ? { bg: getComputedStyle(cta).backgroundColor, bgImage: getComputedStyle(cta).backgroundImage, color: getComputedStyle(cta).color, borderRadius: getComputedStyle(cta).borderRadius, padding: getComputedStyle(cta).padding } : null,
    uniqueBgs: Array.from(bgs).slice(0, 15),
    uniqueColors: Array.from(colors).slice(0, 15),
  }, null, 2);
})()
```

### What to look for

| Element | What to extract | Example (TraderWaves light) |
|---------|----------------|----------------------|
| Body | backgroundColor, color, fontFamily | `#fff`, `#171717`, `Onest` |
| CSS vars | All `--*` custom properties | `--primary-bright: #1783ff` |
| CTA button | backgroundImage (gradient!) | `linear-gradient(90deg, #1783ff, #4ca9ff)` |
| CTA button | borderRadius | `9999px` (pill) |
| H1 | color, fontSize, fontWeight | `#0b163f`, `60px`, `800` |
| Card bg | backgroundColor on card-like elements | `#f2f6ff` (light blue) |
| All bgs | Unique background colors | `["rgb(255,255,255)", "rgb(15,22,66)", "rgb(242,246,255)"]` |
| All colors | Unique text colors | `["rgb(23,23,23)", "rgb(23,131,255)", "rgb(11,22,63)"]` |

### Key insight: backgroundImage vs backgroundColor

CTA buttons often use `backgroundImage: linear-gradient(...)` with `backgroundColor: rgba(0,0,0,0)` (transparent). If you only check `backgroundColor`, you'll miss the gradient. Always check `backgroundImage` too.

### Key insight: oklab/oklch colors

Modern sites may use `oklab()` or `oklch()` color functions. Convert to hex for your CSS:
- `oklab(0.623 -0.048 -0.199 / 0.12)` ≈ `rgba(99, 102, 241, 0.12)` (indigo with 12% alpha)
- Use an online oklab→hex converter or eyeball it from the RGB values

## ⚠️ CRITICAL: Extract the RIGHT theme variant (dark vs light)

**Pitfall:** If the user says "make it dark like [site]", do NOT extract the site's default landing page colors. Many SaaS sites default to a LIGHT theme on their marketing page even though their product has a dark mode. You will extract white backgrounds and dark text, build a light theme, and the user will be frustrated: *"why light waves theme, I told you make dark."*

**Fix:** Before extracting, check if the reference site has a theme toggle (Light/Dark buttons, often in a "showcase" or "preview" section). Click the DARK button first, THEN extract:

```js
// Step 1: Find and click the dark toggle
const darkBtn = Array.from(document.querySelectorAll('button'))
  .find(b => b.textContent.trim().toLowerCase() === 'dark');
if (darkBtn) darkBtn.click();

// Step 2: Wait a moment for the transition, THEN run the extraction script
// (re-run the full extraction IIFE from above)
```

**If the site has a showcase/preview section** (e.g. "Flow From Day to Night"), the dark mode styles may be scoped to that section, not the full page. Extract from within that section:

```js
// Find the showcase region and get computed styles of its dark children
const showcase = document.querySelector('[aria-label*="Day and night"], [class*="showcase"]');
if (showcase) {
  const darkChildren = showcase.querySelectorAll('*');
  // Filter for elements with dark backgrounds (rgb(11, ...), rgb(15, ...), etc.)
  const darkBgs = [];
  for (let i = 0; i < darkChildren.length; i++) {
    const bg = getComputedStyle(darkChildren[i]).backgroundColor;
    if (bg.includes('11, 16, 37') || bg.includes('15, 22, 66') || bg.includes('0b163f')) {
      darkBgs.push({ tag: darkChildren[i].tagName, bg, color: getComputedStyle(darkChildren[i]).color });
    }
  }
}
```

### Common dark mode patterns to look for

| Pattern | What it looks like | CSS equivalent |
|---------|-------------------|----------------|
| Deep navy bg | `#0b1025` or `#0b163f` | `--bg: #0b1025;` |
| Glassmorphism cards | `rgba(255,255,255,0.05)` bg | `--bg-card: rgba(255,255,255,0.05);` + `backdrop-filter: blur(12px);` |
| Subtle white borders | `rgba(255,255,255,0.10)` | `--bg-line: rgba(255,255,255,0.10);` |
| Off-white text | `#f8fbff` or `rgba(248,251,255,0.8)` | `--fg: #f8fbff;` |
| Opacity-based text hierarchy | 70%/50%/30% alpha of fg color | `--fg-dim: rgba(248,251,255,0.70); --fg-mute: rgba(248,251,255,0.50);` |
| Blue accent | `#1783ff` or `#007aff` | `--accent-1: #1783ff;` |
| CTA gradient | `linear-gradient(90deg, #1783ff, #4ca9ff)` | `--waves-cta: linear-gradient(90deg, #1783ff, #4ca9ff);` |
| Pill-shaped chips | `borderRadius: 9999px` | `border-radius: 9999px;` |
| Backdrop blur on cards | `backdrop-filter: blur(12px)` | `backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);` |

## Light theme contrast pitfalls

If the user reports "light mode box, header and text color are not right", the common cause is too-low contrast:

| Element | Bad (low contrast) | Good (sufficient contrast) |
|---------|-------------------|---------------------------|
| Primary text | `#1a1a1a` on `#fafafa` | `#111827` on `#f8f9fa` |
| Borders | `#d4d4d4` (too faint) | `#d1d5db` (visible) |
| Background | `#fafafa` (too close to white cards) | `#f8f9fa` (slightly cooler, more separation) |
| Dim text | `#525252` | `#4b5563` (warmer, better readability) |

The fix is to use Tailwind's perceptually-tuned gray scale values rather than neutral grays.

## CSS Variable theme system pattern

The TradingX pattern (works for any Next.js + Tailwind app):

### Architecture

```
<html data-theme="dark" data-accent="green">
  └── globals.css defines :root[data-theme="X"] blocks
      └── Each block sets --bg, --fg, --bg-card, --bg-line, --accent-1, etc.
      └── Tailwind config maps bg-bg → var(--bg), text-fg → var(--fg)
      └── ThemeApplicator.tsx reads settings.theme → sets data-theme attribute
```

### Adding a new theme variant

1. **Type:** Widen `theme: "dark" | "light" | ... | "newtheme"` in settings.ts
2. **CSS:** Add `:root[data-theme="newtheme"] { --bg: ...; --fg: ...; }` in globals.css
3. **Overrides:** Add `:root[data-theme="newtheme"] .surface { ... }` for component-specific styles
4. **Applicator:** Handle the new theme as a distinct value (don't map to dark/light)
5. **UI:** Add button to the theme selector array
6. **Meta:** Update `theme-color` meta tag for the new theme

### Why this doesn't conflict

- CSS variables cascade: `:root[data-theme="waves"]` only applies when `data-theme="waves"`
- Existing `:root[data-theme="dark"]` and `:root[data-theme="light"]` blocks are untouched
- Theme-specific component overrides (`:root[data-theme="waves"] .chip { ... }`) only match when the theme is active
- The Tailwind config doesn't change — it maps `bg-bg` → `var(--bg)` which resolves differently per theme

### Verification after theme addition

```js
// In browser_console after switching to the new theme:
const html = document.documentElement;
html.getAttribute('data-theme')  // → "waves"
getComputedStyle(html).getPropertyValue('--bg')  // → "#0b1025" (dark) or "#fff" (light)
getComputedStyle(html).getPropertyValue('--fg')  // → "#f8fbff" (dark) or "#0b163f" (light)
getComputedStyle(html).getPropertyValue('--bg-card')  // → "rgba(255,255,255,0.05)" (glassmorphism)
getComputedStyle(html).getPropertyValue('--accent-1')  // → "#1783ff"
getComputedStyle(document.body).backgroundColor  // → "rgb(11, 16, 37)" (dark navy applied)
getComputedStyle(document.body).color  // → "rgb(248, 251, 255)" (off-white applied)
```

If all values match the extracted reference site values, the theme is correctly applied.

### Pitfall: patch tool quote-escaping

When using `patch` with `old_string` or `new_string` containing quotes (e.g., `["dark", "light"]`), the tool can introduce literal `\"` backslashes into the file. The diff looks correct but the file contains `\"dark\"` instead of `"dark"`.

**Fix:** Use `sed` to strip the backslashes:
```bash
sed -i 's/\\"/"/g' app/settings/page.tsx
```

Or avoid the issue entirely by using `write_file` for files with heavy quote content instead of `patch`.
