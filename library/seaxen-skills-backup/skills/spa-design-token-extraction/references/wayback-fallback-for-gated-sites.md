# Cloudflare / Bot-Gated Sites — Wayback Machine Fallback

When a live site is behind Cloudflare Turnstile, hCaptcha, or aggressive bot detection, `curl` returns the challenge page, `web_extract` returns nothing useful, and even headless puppeteer hits the gate. **Wayback Machine's CDX replay** bypasses the gate because the snapshot was taken from a whitelisted crawler IP and is served as a static asset.

## When to use

- `curl -s https://example.com/` returns "Just a moment..." or "Verify you are human"
- `web_extract` returns only the challenge HTML
- Puppeteer can navigate but `document.body.innerText` shows the Turnstile widget, not the real site
- Clicking the Turnstile checkbox doesn't auto-resolve (Cloudflare fingerprints headless browsers)

## Recipe

### 1. Find the most recent Wayback snapshot

```bash
# Browse the calendar at web.archive.org/web/2025/https://example.com/
# Look for the most recent "success" row
```

Or via CDX API:

```bash
curl -s "https://web.archive.org/cdx/search/cdx?url=example.com/&limit=-1&output=json&filter=statuscode:200" | tail -1
# Returns: ["20260817155622","https://example.com/","200","-","12345","https://example.com/","-","12345"]
# Use the first timestamp field.
```

### 2. Load via Wayback CDX replay

The snapshot is at `https://web.archive.org/web/<timestamp>/<original-url>` and Wayback's wombat.js rewrites inline links to its own proxy — but the JS bundles load from the original CDN, so the page actually renders.

```js
const puppeteer = require('/usr/local/lib/node_modules/medical-mcp/node_modules/puppeteer');
(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    executablePath: '/usr/bin/chromium',
    args: ['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 1 });
  await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36');

  await page.goto(
    'https://web.archive.org/web/20260817155622/https://example.com/',
    { waitUntil: 'domcontentloaded', timeout: 30000 }
  );
  // SPA hydration takes a few seconds
  await new Promise(r => setTimeout(r, 6000));

  // Verify it's not the Wayback shell:
  const root = await page.evaluate(() => document.getElementById('root')?.innerHTML?.slice(0, 200) || '');
  console.log("Hydrated?", root.length > 100);

  // Now do the normal token extraction
  const data = await page.evaluate(() => { /* getComputedStyle etc */ });
})();
```

### 3. Proceed with normal token extraction

`getComputedStyle`, `:root` CSS vars, computed colors, sampled selectors — all work the same as on the live site because Wayback proxies the original CSS/JS bundles.

## Pitfalls

- **Snapshot may be stale.** Wayback captures are point-in-time. If the site's design changed recently, use the most recent snapshot date from the calendar.
- **Wayback wrapper chrome.** The HTML returned starts with wombat.js injection and Wayback's own CSS. The actual `<body>` may be short — wait for SPA hydration and re-check.
- **Don't `curl` the Wayback URL.** `curl` doesn't run JS, so you'll see the React/Next mount point (`<div id="root"></div>`) and no rendered content. Use puppeteer + browser.
- **Direct assets may break.** Some image/CSS bundles get rewritten by Wayback's proxy. For token extraction this is fine — computed styles resolve regardless.
- **Turnstile widgets inside iframes.** If the live page itself has a Turnstile widget in a frame, you may need to navigate via Wayback's "if_" mode: `https://web.archive.org/web/<ts>if_/<url>` — the `if_` prefix tells Wayback to render without injecting its toolbar.
- **Some Wayback snapshots are missing.** CDX returns `200` for archived HTML but `4xx` for individual asset URLs (JS/CSS). Puppeteer will still render what loaded; missing styles will fall back to defaults.
- **JavaScript might have updated.** Wayback captures static HTML/CSS/JS bundles. If the site uses a service worker or runtime-fetched data, the snapshot will be old.

## Verification

After extraction, sanity-check:

```js
const data = await page.evaluate(() => ({
  title: document.title,
  bodyClasses: document.body.className,
  hasContent: document.body.innerText.length > 200,
  textPreview: document.body.innerText.slice(0, 200),
}));
```

If `hasContent` is true and `title` matches the expected site, you're looking at the real rendered DOM, not the Wayback shell.

## Provenance note

Always cite the Wayback snapshot date in your Designmd theme `.md` file (e.g. "Source: ansem.io (Wayback snapshot 2026-08-17 — live site is behind Cloudflare Turnstile)"). Future readers need to know the tokens come from a snapshot, not the live site.
