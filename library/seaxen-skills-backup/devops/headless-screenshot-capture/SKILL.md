---
name: headless-screenshot-capture
description: Use when capturing local HTML. CLI or puppeteer fullPage.
---

# Headless screenshot capture

Use when you need a PNG of a local HTML file: Designmd preview.png, doc mockup verification, visual regression checks, contact-sheet inputs.

## Two capture paths

| Path | Tool | When it works | When it fails |
|------|------|---------------|---------------|
| CLI | chromium --headless ... --screenshot | Static-height pages, no full-viewport sections | Silently truncates anything past the captured viewport when hero uses 100svh / 100dvh / 100vh / min-height 100% |
| Puppeteer fullPage | page.screenshot({fullPage: true}) | Anything, including full-viewport heroes, JS-rendered fonts, SPA shells | Slower (Node startup), needs puppeteer installed somewhere |

## Path A — chromium CLI

```bash
chromium --headless --disable-gpu --no-sandbox --hide-scrollbars \
  --window-size=1440,2600 --virtual-time-budget=8000 \
  --screenshot="/abs/path/to/preview.png" \
  "file:///abs/path/to/page.html"
```

Notes:
- `--virtual-time-budget=8000` gives fonts and CSS ~8s to settle.
- `--window-size` defines the **viewport**, not the capture height. Anything past `window-size.height` is **not captured**.
- Escape `#` in file URLs as `%23` (e.g. `/mnt/tb/#Sea/...` → `/mnt/tb/%23Sea/...`).

## Path B — puppeteer fullPage (use when Path A will fail)

Tell-tale signs the page needs fullPage capture:
- `.latyx-hero { min-height: calc(100svh - 3.5rem); }` or any 100svh / 100dvh / 100vh hero
- A hero `<section>` that fills the viewport
- Animated or canvas hero that depends on real layout
- Tall page where the only content above the fold is the hero

Locate puppeteer (it may be transitively installed under another package):

```bash
find /usr/local/lib/node_modules /usr/lib/node_modules -maxdepth 5 -name puppeteer -type d 2>/dev/null
```

On the Latyx host it was at `/usr/local/lib/node_modules/medical-mcp/node_modules/puppeteer`.

Write `/tmp/snap.js`:

```javascript
const puppeteer = require('<absolute-path>/puppeteer');
(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    executablePath: '/usr/bin/chromium',   // use system chromium, not puppeteer's bundled one
    args: ['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 1 });
  await page.goto('file:///abs/path/page.html', { waitUntil: 'networkidle0', timeout: 30000 });
  await page.evaluate(async () => { await document.fonts.ready; });   // wait for fonts
  await new Promise(r => setTimeout(r, 800));                         // tail for web-font swap
  await page.screenshot({ path: '/tmp/preview.png', fullPage: true });
  console.log(await page.evaluate(() => ({
    w: document.documentElement.scrollWidth,
    h: document.documentElement.scrollHeight,
  })));
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
```

Run:

```bash
node /tmp/snap.js && cp /tmp/preview.png "/abs/path/preview.png"
```

## Why the CLI path fails for full-viewport heroes

Chromium's `--screenshot` captures **the viewport rectangle**, not the document. With `--window-size=1440,2600`, the viewport is 1440×2600. If a hero has `min-height: calc(100svh - 3.5rem)`, on a 1440×2600 viewport that becomes ~2560 px tall — i.e. the hero fills (or overflows) the entire viewport, and every section below it is off-screen and **not captured**.

The browser gives no warning. You only notice when the resulting PNG is shorter than expected or a vision check reports missing sections. Bumping `--window-size` to 1440×4000 does not help — the browser resizes the viewport and the hero expands with it.

## Verify the capture

Always follow a screenshot capture with a vision check that names each expected section and reports which are missing. For Designmd theme folders, the contact-sheet script is a good secondary check — blank or missing sections show as large white blocks.

## Pitfalls

- **Assuming `--window-size=H` captures the whole page.** It captures `H` pixels, period.
- **Not waiting for fonts.** Web-font swap shows FOUT; add `await document.fonts.ready` plus ~800ms tail.
- **Puppeteer's bundled Chrome missing.** Use `executablePath: '/usr/bin/chromium'` to fall back to the system browser.
- **Forgetting `--no-sandbox`.** Required when running as root in containers.
- **Not escaping `#` in file URLs.** `/mnt/tb/#Sea/...` becomes a URL fragment; the browser may load a directory listing or blank page. Use `%23`.
- **Capturing a `file://` URL that loads cross-origin resources.** Some pages block under `file://`; use `--allow-file-access-from-files` or `--disable-web-security` if needed.

## Decision rule

```
Does any top-level section use 100vh / 100svh / 100dvh / min-height: 100%?
├── yes → puppeteer fullPage (Path B)
└── no  → chromium CLI is fine (Path A)
```

## Reuse triggers

"capture preview.png", "render HTML to PNG", "full page screenshot", "headless chromium screenshot", "chromium --window-size fails", "puppeteer fullPage", "Designmd preview missing", "verify theme render", "contact sheet screenshot".
