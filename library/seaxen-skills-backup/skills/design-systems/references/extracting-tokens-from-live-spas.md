# Extracting Design Tokens from Live SPAs (No-Render Approach)

When the site you want to capture is a JavaScript SPA, the initial HTML is usually
`<html><body><div id="app"></div></body></html>` — the real design is built at runtime
by a JS bundle. You can extract it without a browser by following the asset graph
the same way the page does at load time.

## When to use this (vs the `getComputedStyle` approach)

Use this approach when:
- The site is built with React / Vue / Svelte / Preact / Solid (or any framework
  that mounts into a root div)
- A browser tool is not available, or you want a fully reproducible
  scriptable extraction
- You need *the source of truth* — the actual tokens the author wrote,
  not the browser's computed view (which can lie about custom properties
  the page never instantiates)
- The site is reachable over `curl` but not over a real browser

Use the `getComputedStyle()` approach in `Part 1: Extracting Design Tokens
from Live Sites` of the umbrella SKILL.md when:
- The site is mostly server-rendered (HTML contains the visible content)
- A browser tool is available
- You only need a small number of specific values

## Procedure

1. Fetch the initial HTML:
   ```bash
   curl -sL -A "Mozilla/5.0" https://example.com/ -o index.html
   ```
2. Read it. If it contains the visible content (most of the page text is in
   the initial HTML, not a `<div id="app"></div>`), the static-assets
   approach is unnecessary — fall back to the `getComputedStyle` approach.
3. If the HTML is a shell, find the linked assets in `<head>`:
   - `<link rel="stylesheet" ... href="/assets/...css">`
   - `<script type="module" ... src="/assets/...js">`
4. Fetch each one:
   ```bash
   curl -sL https://example.com/assets/index-AbCdEfGh.css -o actual.css
   curl -sL https://example.com/assets/index-AbCdEfGh.js  -o actual.js
   ```
5. Extract design tokens from the CSS (they are almost always in `:root { ... }`):
   ```python
   import re
   props = re.findall(r'--([a-z0-9-]+):\s*([^;]+);', open('actual.css').read())
   # dedupe while preserving first-seen order
   seen, tokens = set(), []
   for name, val in props:
       if name not in seen:
           seen.add(name); tokens.append((name, val))
   ```
6. Extract content from the JS bundle. The visible text and project
   descriptions are almost always embedded as string literals in the
   bundle, even when the site is otherwise framework-driven:
   ```python
   import re
   js = open('actual.js').read()
   # Find long strings (500+ chars) that contain content markers
   for m in re.finditer(r'"([^"\\]{500,5000})"', js):
       s = m.group(1)
       if any(k in s for k in ['Project', 'About', 'Stack', 'linkedin', 'github']):
           print(s.replace('\\n', '\n')[:2000])
   ```
7. Build the duplicate. The CSS gives you exact tokens (often
   `oklch()` values, `color-mix()` calls, real font stacks). The JS
   gives you the real content. Combine them in a single HTML file.

## What you get that `getComputedStyle` doesn't

- **Token NAMES, not just values.** `oklch(43% 0.085 154)` is the value;
  `--accent: oklch(43% 0.085 154)` is the name. The site uses three accents
  (green / teal / rust) with semantic names; only the source CSS tells you
  which is `--accent` vs `--accent-2` vs `--accent-warm`.
- **The full token set, including unused ones.** Browsers only return
  computed values for properties that are actually rendered. The CSS
  bundle has 22 design tokens; only ~6 are visible on the homepage.
- **The full font stack with fallbacks.** Browsers resolve to the active
  font; the CSS gives you the cascade: `"Canela", "Ivy Presto",
  "Bodoni Moda", "Playfair Display", serif` — first one available wins.
- **The full responsive breakpoint set.** All `@media` blocks, not just the
  ones currently matched.
- **The exact `color-mix()` calls** the author used for hover states. The
  browser shows you the resolved color, not the expression.

## What can still go wrong

- **Husky minified bundles** have zero formatting. Use a Python regex pass
  with the target names, not manual scanning.
- **String literals are escaped** in JS bundles (`\n`, `\"`, `\\`). Decode
  before comparing to the live page.
- **Asset filenames are content-hashed** (`index-AbCdEfGh.css`). If you
  see a stale hash from yesterday's cache, you'll get a 404. Always
  fetch the HTML fresh first and read the current `href`/`src`.
- **Multiple bundles.** A non-trivial SPA may have several JS chunks
  (`index-abc.js`, `vendor-def.js`, `page-456.js`). Fetch them all; the
  content you want may be in any of them.
- **Inline SVG icons** (like the washiul.com `.stack-icon` overlay) are
  embedded in the JS as base64 or as inline string literals. They're
  decorative — extract only if they carry brand identity.

## Worked example: washiul.com (2026-09-07)

- Initial HTML: 3.6 KB, contained `<div id="app"></div>` only.
- Found two assets:
  - `https://www.washiul.com/assets/index-_32j-vn7.css` (48 KB, 1,227 lines minified)
  - `https://www.washiul.com/assets/index-tsQBHuDX.js`  (82 KB, minified)
- Extracted 22 unique design tokens from `:root` in the CSS, including
  three semantic accents (`--accent`, `--accent-2`, `--accent-warm`)
  and a serif display font stack with four fallbacks.
- Found project descriptions (Capy, KomfyKitty, Routino, ArthurMorgan) as
  long string literals in the JS bundle.
- Reproduced the design system exactly: same OKLCH values, same
  `color-mix()` hover expressions, same 1px hairline borders, same
  serif/sans split, same responsive breakpoints.

## Related

- `css-theme-system-architecture.md` — how to wire extracted tokens into a
  switchable multi-theme system (`html[data-theme="..."]` pattern).
- `tinybird-design-token-extraction.md` — case study of the same problem
  with a server-rendered reference HTML provided by the user; not a
  pure live-site extraction.
- Part 1: "Extracting Design Tokens from Live Sites" in the umbrella
  SKILL.md — the `getComputedStyle()` browser-based approach for sites
  you can actually render.
