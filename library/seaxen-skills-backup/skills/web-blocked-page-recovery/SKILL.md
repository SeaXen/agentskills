---
name: blocked-page-recovery
description: "Use when a fetch fails: 403/429, paywall, WAF, bot wall, or a CF-gated page whose real file lives behind a viewer iframe on a separate host (Google Drive, S3, CDN)."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Research, Archives, Wayback, Paywall, WAF, Fallback]
    related_skills: [grounded-citations]
---

# Blocked-Page Recovery

When a page won't fetch — 403/429, Cloudflare "Just a moment...", a paywall,
or a bot-detection interstitial — don't give up and don't loop on the same
URL. Third-party services often hold a **copy** of the page. Work down this
ladder, cheapest first.

## The ladder

```
1. Wayback Machine  — archive.org "available" API  (snapshot + timestamp)
2. archive.today    — domain rotation: archive.ph → .md → .li → .is
3. Jina Reader      — only if JINA_API_KEY is set  (live server-side render)
4. API-first pivot  — look for /api/, /graphql, .json, or RSS on the same host
5. Browser → find file URL → plain HTTP — when the real file lives behind
   a viewer iframe on a separate host (Drive/S3/CDN)
```

Run it in one shot with the bundled script:

```bash
python3 scripts/recover_page.py "https://example.com/blocked-article" --json
```

The script tries each route in order, validates every body (see "Fake
successes" below), and prints the first genuine hit with its provenance.

## Provenance discipline (non-negotiable)

Every recovered copy carries a provenance you MUST preserve when citing:

| Route | Provenance | How to cite |
|-------|-----------|-------------|
| Wayback / archive.today | `snapshot` | Cite WITH the snapshot date: "as archived 2026-08-06". Never present a snapshot as the live page — it may be stale. |
| Jina Reader | `live` | Server-side re-render of the live page; cite normally. |
| Live fetch / browser | `live` | Cite normally. |

If the user needs *current* data (prices, availability, breaking news), a
snapshot is context, not an answer — say so explicitly and note its age.

## Manual routes

### 1. Wayback Machine (best provenance, try first)

```bash
# Discovery: returns closest snapshot URL + timestamp as JSON
curl -sL "https://archive.org/wayback/available?url={URL}"
# Then fetch archived_snapshots.closest.url
```

For enumerating many snapshots (or recovering deleted pages), the CDX index:

```bash
curl -sL "https://web.archive.org/cdx/search/cdx?url={URL}&output=json&limit=10"
```

CDX intermittently returns 503 under load — if it does, fall back to the
`available` API; don't retry-hammer it.

Works for: any publicly crawled URL. Fails for: robots-blocked sites,
never-crawled URLs, JS-only SPAs (snapshots don't render).

### 2. archive.today (paywalls, deleted content)

User-submitted archives — often has paywalled news articles Wayback lacks.
Rate-limits aggressively (429) and rotates domains, so iterate:

```bash
for d in archive.ph archive.md archive.li archive.is; do
  curl -sL --max-time 20 "https://$d/newest/{URL}" -o /tmp/page.html \
    -w "%{http_code}" && break
done
```

**Validate the body, not the status code** — a 429 still ships several KB of
rate-limit HTML that looks like a success to a size check alone.

### 3. Jina Reader (requires JINA_API_KEY)

`r.jina.ai` re-renders the live page in a real browser server-side and
returns markdown. Anonymous access is dead (401 → Turnstile); a key is
required:

```bash
curl -s -H "Authorization: Bearer $JINA_API_KEY" "https://r.jina.ai/{URL}"
```

Handles JS SPAs that archives can't. Skip this route entirely when the env
var is unset.

### 4. API-first pivot

WAFs protect the HTML surface far more aggressively than the data endpoints
behind it. After 2-3 blocked attempts on a site, stop fighting the HTML and
look for:

- `/api/...`, `/graphql`, or `.json` variants of the page URL
- An RSS/Atom feed (`/feed`, `/rss`, `<link rel="alternate">` in any copy
  you did recover)
- A sitemap (`/sitemap.xml`) revealing canonical URLs that may not be gated

### 5. Real browser to find the underlying file, then plain HTTP

Some CF-gated sites never expose the actual asset URL in static HTML
or the API. Instead, the public page embeds an iframe / viewer that
streams the real file from a **separate host** (Google Drive, S3,
Cloudflare R2, custom CDN). A real browser gets you the iframe URL;
once you have it, plain HTTP works because the file host is usually
unguarded.

This is what worked on **boimate.com** (266 PDFs, CF-gated). Pattern:

```text
book page (CF)  →  /read page  →  /read/view page  →  <iframe src=…drive.google.com…>
                                                            ↓
                              curl drive.google.com/uc?export=download&id=…
```

#### Recipe (boimate case, generalises to similar sites)

1. **Open the public page in a real browser** (Playwright Firefox
   works without `pip install playwright` browser deps on Debian —
   `pipx install playwright` + `playwright install firefox` is enough).
   CF passes once the browser is honest.
2. **Click "Read"/"Preview"** — this usually opens a second page whose
   only purpose is the iframe viewer.
3. **Read the JS for an inline redirect** (e.g. `function startRead()
   { window.location.href = "..." }`) and call the target URL via
   `await page.evaluate("() => startRead.toString().match(/href\\s*=\\s*\"([^\"]+)\"/)[1]")`.
4. **Find the real file URL inside an iframe**:
   `await page.wait_for_selector("iframe#pdfIframe")` then
   `el.src`. For Google Drive, extract the ID with
   `re.search(r'/file/d/([^/]+)', src)`.
5. **Download with plain `curl`** (not Playwright) — Google's
   `uc?export=download&id=…` serves the file directly, 303 redirect +
   content-type `application/octet-stream`, ~2s per file vs 30+s
   per file through the browser.
6. **Sanitise filename** from the original book page URL slug (NOT
   from the iframe URL, which is opaque). Example:
   `https://boimate.com/nazatul-muslimeen-pdf` → `nazatul-muslimeen.pdf`.

#### Why two phases (Playwright then curl)

The browser is only needed to find the file URL. Once you have the ID,
`curl` is:
- 5–10× faster (no headless startup, no CF challenge per request)
- Resumable (`curl -C -` works on partials)
- Parallelisable (xargs -P 4)
- Detectable as a real download (Playwright `expect_download` often
  misses iframe-loaded content; the navigate to `uc?export=download` is
  not a Content-Disposition download event)

#### Pitfalls

- **Tokens are one-time / session-bound.** Boimate's `/server/gotodl?link=…`
  token re-renders the book page HTML on second hit (Google-Drive-style
  "confirm download" was the same with the iframe route). Use the
  iframe URL (e.g. the Google Drive `/preview` URL) — those IDs are
  stable per book and re-fetchable.
- **File size threshold.** Google Drive serves direct download only
  for files under ~25 MB without a virus-scan interstitial. Validate
  the downloaded magic bytes (`b"%PDF"`) — anything else, log the URL
  and move on; the URL is salvageable.
- **Site throttles the headless browser.** After 30–50 page loads, the
  "Read" button may stop appearing (CF escalation). Cache
  `book_url → drive_id` to a JSON file after every successful resolve;
  the second pass is just `curl` from the cache and never re-hits the
  throttled endpoint.
- **Naming.** If you name files from the iframe URL you'll get
  opaque hashes. Always name from the canonical public page slug.

#### When NOT to use this route

- Site requires login for the viewer (OTP, captcha) — Playwright gets
  stuck on the same wall as you would.
- The iframe host (e.g. Drive, S3) blocks your IP / region.
- File is a live stream, not a static asset (HLS, WebSocket).

## Fake successes — routes that LIE

These return HTTP 200 with a plausible body that is NOT the page. The script
rejects them automatically; reject them manually too:

- **Google Cache is dead** (since mid-2024). `webcache.googleusercontent.com`
  returns 200 + tens of KB, but it's a Google Search interstitial with a JS
  redirect, not a cache. Never use it.
- **AMP caches** (`*.cdn.ampproject.org`) mostly return a ~300-byte
  `<title>Redirecting</title>` meta-refresh stub pointing back at the
  original (blocked) URL. Treating that as success creates a fetch loop.
- **Rate-limit bodies**: archive.today 429 pages are multi-KB HTML. Check for
  the target's actual content (title words, expected strings), not just size.

Detection heuristics the script applies: body under a per-route byte floor;
meta-refresh/JS-redirect stubs whose target is the original host; interstitial
titles ("Just a moment", "Redirecting", "Google Search", "Attention Required").

## Proxy relays: don't

Generic "web proxy" relays are man-in-the-middle by construction. Never send
cookies or Authorization headers through one, and don't use them for anything
the user will rely on — provenance is unverifiable. Prefer archives, which at
least timestamp their copies.
