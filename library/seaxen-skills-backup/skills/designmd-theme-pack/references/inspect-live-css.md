# Inspect Live CSS — Reference

The exact recipe for extracting a real site's design system into the Designmd store. Used by the `designmd-theme-pack` skill.

## Decision tree (per site)

```
curl the home page
├── 404 / blank / GitHub-Pages 404 page
│     └── skip and report
├── < 50KB → static-ish, CSS in linked file → straight to "Find the CSS"
├── 50KB - 500KB → mostly static, design is in the linked CSS → straight to "Find the CSS"
└── > 500KB → SPA, CSS may be in JS bundle
      ├── grep the HTML for the <link rel="stylesheet"> closest to the top
      ├── curl THAT file
      │     ├── if < 5KB → it's preflight, real CSS is in the bundle → "Extract from JS"
      │     └── if > 5KB → real design is here, proceed
      └── if no real CSS file → "Extract from inline styles"
```

## Find the CSS

For a typical Next.js / Vercel-style site, the HTML head has many `<link rel="stylesheet">` tags. The actual design CSS is usually the one with a content hash in the filename, NOT the Tailwind preflight. Look for the largest CSS file and start there.

```bash
# Extract every linked CSS URL from the home page
grep -oE '(href|src)="[^"]+\.css[^"]*"' raw_SITE.html

# Pick the most likely one (largest file by content, often has a hash in name)
curl -sL "https://example.com/_next/static/css/HASHED.css" -o SITE.css
wc -c SITE.css
```

## Extract from inline styles

When a site has no extractable CSS file (Mercury, Linear, many Notion-style sites):

```bash
# Inline style attributes reveal the design tokens
grep -oE '(?:color|background|background-color|fill|stroke)[:=]\s*["\']?(#[0-9a-fA-F]{3,8})' SITE.html | sort | uniq -c | sort -rn
# The top 5-10 colors are usually the real palette

# meta theme-color is the designer's intent
grep -oE '<meta name="theme-color" content="[^"]+"' SITE.html
```

## Tailwind detection

If the CSS is mostly preflight (`*,:before,:after{box-sizing:border-box;border:0 solid #e5e7eb}`) plus utility classes, the **design tokens are in the JS bundle, not the CSS file**.

```bash
# Tailwind preflight pattern in the CSS
grep -c "box-sizing:border-box;border:0 solid" SITE.css
# If > 0, this is Tailwind. The actual design is in the JS bundle.
```

When this happens:
- Look for the largest `.js` chunk (`_next/static/chunks/*.js`)
- `grep` for the design tokens (`--font-`, `--bg-`, `--accent-`, etc.)
- Note: the tokens may be in the form of raw hex (Tailwind 3) or OKLCH (Tailwind 4)

## Worked example (mercury.com, Sept 2026)

```bash
# 1. Fetch home page (850KB — heavy SPA)
curl -sL -A "Mozilla/5.0" "https://mercury.com" -o mercury.html

# 2. Look for inline colors (CSS-in-JS signal)
grep -oE '(?:color|background)[:=]\s*["\']?(#[0-9a-fA-F]{3,8})' mercury.html | sort -u | head
# → #272735 (background), #535461 (mid)

# 3. Confirm via meta theme-color
grep -oE 'meta name="theme-color" content="[^"]+"' mercury.html

# 4. The 463-byte css file is just an empty stub. Don't try to extract from it.
ls -la /tmp/saascan/mercury.css
# → 463 bytes (empty)
```

Result: extracted `mercury.css` is built from scratch using the inline color data + standard Inter typography + the financial-data display pattern (tabular-nums, monospace).

## Worked example (cursor.com, Sept 2026)

```bash
# 1. Fetch home page (645KB)
curl -sL "https://cursor.com" -o cursor.html

# 2. Find linked CSS
grep -oE 'href="[^"]+\.css[^"]*"' cursor.html | head
# → /marketing-static/_next/static/chunks/02ayq8-mo~t3p.css?dpl=...

# 3. Fetch the first (largest) CSS file
curl -sL "https://cursor.com/marketing-static/_next/static/chunks/02ayq8-mo~t3p.css?dpl=dpl_J6Jym4TN1nWvVkFtvQyGM1ZZMH8J" -o cursor.css

# 4. Inspect for :root or distinctive design markers
head -c 3000 cursor.css | head -50
grep -oE '#[0-9a-fA-F]{3,8}' cursor.css | sort | uniq -c | sort -rn | head -10
# → #0000 (transparent — used in many shadows), #000, #26251e (the warm near-black)

# 5. Look at the meta theme-color
grep -oE 'meta name="theme-color" content="[^"]+"' cursor.html
# → #f7f7f4 (warm paper, slightly cream)
```

Result: extracted `cursor.css` is built from real design tokens (`#f7f7f4` bg, `#26251e` fg, BEM-style `.btn--ghost`/`.btn--sm`).

## Detection table

| Signal | Likely source | Action |
|---|---|---|
| CSS > 50KB, has `:root` block with `--token-name: value` | Hand-written CSS, real tokens | Extract from CSS directly |
| CSS > 50KB, all utility classes | Tailwind | Extract from `tailwind.config.js` or build config |
| CSS < 5KB, home page > 200KB | CSS-in-JS, design in JS bundle | Extract from inline styles + bundle |
| meta `theme-color` exists | Use it as the designer's intent for `bg` | Trust it |
| 200 status but body contains `Site not found` | GitHub-Pages 404, repo is dead | Skip and report |
| `<link rel="preload" as="font">` for Geist, Inter, Fraunces, etc. | The design uses a custom font | Note in the .md, link in the HTML |
| Random hex values scattered | Tailwind utility-generated colors | Don't extract these one-by-one, look for the palette in config |
| `oklch(...)` anywhere | The site uses modern color space | Preserve as OKLCH, don't convert to hex |
