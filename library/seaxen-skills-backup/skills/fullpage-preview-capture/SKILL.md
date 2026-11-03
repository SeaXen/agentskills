---
name: fullpage-preview-capture
description: Render HTML to a full-page PNG reliably with puppeteer.
---

# Full-Page Preview Capture

Capture a real full-page PNG of a local HTML mockup, reliably. Works around the chromium `--screenshot` limitation that breaks on any hero using `min-height: 100svh`.

## When to Use

- "render this HTML to a PNG" / "generate preview.png"
- "screenshot this local page" / "capture the full mockup"
- after writing a new theme folder (`*.css` + `*.html`) that needs a `preview.png`
- when chromium's `--window-size` approach produced a PNG that only shows the hero (the user's vision check returns "section X not visible")

## The pitfall that motivates this skill

`chromium --headless --screenshot=... --window-size=1440,N` captures **only the viewport**. Bumping `N` to 3600 or 4400 does **not** capture the full document. Worse, for any hero using `min-height: 100svh` (or `calc(100svh - N)`), the hero alone expands to fill the tall viewport, pushing the rest of the page off the captured image.

Reproduced on Latyx (2026-07-28): hero `min-height: calc(100svh - 3.5rem)` consumed 3560px of a 3600px viewport, leaving the report card, feature grid, steps, CTA, and footer entirely outside the PNG.

## Default recipe — puppeteer `fullPage: true` with system chromium

Reliable. Captures the real document height. Works for any hero treatment.

```bash
cat > /tmp/snap.js <<'EOF'
const puppeteer = require('/usr/local/lib/node_modules/medical-mcp/node_modules/puppeteer');
(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    executablePath: '/usr/bin/chromium',
    args: ['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 1 });
  await page.goto('FILE_URL', { waitUntil: 'networkidle0', timeout: 30000 });
  await page.evaluate(async () => { await document.fonts.ready; });
  await new Promise(r => setTimeout(r, 800));
  const dims = await page.evaluate(() => ({ w: document.documentElement.scrollWidth, h: document.documentElement.scrollHeight }));
  await page.screenshot({ path: 'OUTPUT_PATH', fullPage: true });
  console.log('Captured', dims);
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
EOF
node /tmp/snap.js
```

The `FILE_URL` must use `%23` for any `#` in the path (e.g. `/mnt/tb/#Sea/...` → `file:///mnt/tb/%23Sea/...`).

### Why these specific settings

- **`executablePath: '/usr/bin/chromium'`** — puppeteer's bundled chromium is rarely pre-installed on self-hosted hosts; system chromium almost always is. Point puppeteer at it.
- **`headless: 'new'`** — modern headless mode (puppeteer ≥ 20). Falls back to `'shell'` on older versions.
- **`waitUntil: 'networkidle0'`** — waits for fonts and CSS chunks to settle. Critical for `--preconnect` and Google Fonts loads.
- **`document.fonts.ready`** — extra font-readiness barrier. Without this, webfonts can render as fallback fonts in the screenshot.
- **`setTimeout 800ms`** — additional paint-stability buffer for `animation:` and `transition:` properties that need to settle.
- **`deviceScaleFactor: 1`** — produces a 1× screenshot. Use `2` for retina-quality previews (file size ~4×).
- The printed `{w, h}` is the real document height — useful for the contact sheet and for verifying nothing got clipped.

### Host-specific puppeteer location

On this host (`/root/.hermes/`) puppeteer lives inside `medical-mcp`'s node_modules. Adapt:

```bash
# Find it on any host
find /usr/local/lib/node_modules -name 'puppeteer' -maxdepth 4 -type d 2>/dev/null | head -3
# Common alternative locations
# /usr/lib/node_modules/puppeteer
# ~/.npm-global/lib/node_modules/puppeteer
```

If puppeteer isn't installed anywhere, install it system-wide (one-time):

```bash
npm install -g puppeteer
# Or just use the chromium viewport fallback below
```

## Fallback — chromium viewport-only (for short static-height mockups)

When the page is short and there is no full-viewport hero (login screens, single-card dashboards, error pages), the plain chromium command works:

```bash
chromium --headless --disable-gpu --no-sandbox --hide-scrollbars \
  --window-size=1440,2600 --virtual-time-budget=10000 \
  --screenshot=OUTPUT_PATH \
  FILE_URL
```

Tune `--window-size=1440,Y` to slightly exceed the document height. Use `vision_analyze` after capture to confirm all sections are visible; if any are clipped, switch to the puppeteer recipe.

## Wrapper-page trick (when you want to screenshot multiple themes with shared fixes)

Build a temporary wrapper that loads the theme's CSS and HTML together, optionally injecting CSS overrides (e.g. cap hero height, force print background colors):

```bash
cat > /tmp/shot.html <<EOF
<!doctype html><html><head>
<link rel="stylesheet" href="$THEME_CSS">
<style>html,body{margin:0} [class*="hero"],section:first-of-type{min-height:auto!important;height:auto!important}</style>
</head><body><script>
fetch("$FILE_URL").then(r=>r.text()).then(html=>{document.open();document.write(html);document.close();})
</script></body></html>
EOF
chromium --headless --disable-gpu --no-sandbox --hide-scrollbars \
  --window-size=1440,4400 --virtual-time-budget=10000 \
  --screenshot=OUTPUT_PATH \
  "file:///tmp/shot.html"
```

Useful when you specifically want a viewport-sized capture and don't have puppeteer.

## Verification after capture

Always confirm what the screenshot actually contains. A captured PNG that "looks right" can still be missing sections.

1. File size sanity check: a 1440-wide full-page PNG should be **≥ 80KB** for content-rich pages; under 30KB usually means the page rendered blank or only one section.
2. `vision_analyze` the PNG with a specific question listing the sections you expect to see, top-to-bottom. Don't accept "looks fine" — name each section.
3. Cross-check: the puppeteer-printed `{h}` should match the document height you'd expect (a typical landing page is 2500–5000px; a login page is 600–1200px).

## Dark mode

If the theme has a dark variant (separate fixture or `html.dark` toggle):

- Capture both `preview.png` (default mode) and `preview-dark.png` (dark mode toggled on).
- For puppeteer, toggle before screenshot:
  ```js
  await page.evaluate(() => document.documentElement.classList.add('dark'));
  await new Promise(r => setTimeout(r, 200));
  await page.screenshot({ path: 'preview-dark.png', fullPage: true });
  ```
- For chromium viewport, swap the fixture URL or inject a click on the toggle and re-screenshot.

## Common errors

- **`Could not find Chrome (ver. X.X)`** — puppeteer wants its bundled chromium. Either install it (`npx puppeteer browsers install chrome`) or pass `executablePath` to system chromium.
- **`MODULE_NOT_FOUND`** — puppeteer isn't installed at the require path. Update the require or `npm install -g puppeteer`.
- **Blank/black PNG** — usually a `file://` URL with a raw `#` (fragment) in the path. Use `%23`.
- **Page renders unstyled** — CSS link is relative and chromium is loading from a `file://` URL where the relative path resolves wrong. Either render via a temp HTML in the same folder, or use the wrapper-page trick.
- **Section visible in browser but not in PNG** — viewport-only capture (the original pitfall). Switch to puppeteer `fullPage: true`.

## Pairing with contact sheets

After generating previews for many theme folders, build a contact sheet PNG (a grid of thumbnails) as a visual index. Save it as `preview-contact-sheet.png` at the store root. The contact sheet is **only an index**; the real deliverable is the per-folder `preview.png` (and `preview-dark.png` if applicable).
