# Static Site Performance Optimization — Worked Recipe

A real session's recipe for turning a 32-chapter medical study website (MedSea) from "5 min to load a chapter" to "<1s chapter load". Useful as a copy-pasteable worked example for any "make my static site fast" request.

## Stack Context (MedSea, June 2026)

- **Server**: nginx 1.x in Docker container (`medsea`), port 8855 → 80
- **Content**: 32 chapter directories × ~50-300 PNGs each (3,034 total, 876 MB)
- **Search**: monolithic `search_index.json` (4,287 entries, 991 KB) loaded on first keystroke
- **JS**: vanilla, no framework, no build step
- **Deployment**: `docker cp` to running container; full rebuild was too slow

## Final Wins (Before → After)

| Resource | Before | After | Win |
|---|---|---|---|
| Ch 16 HTML (gz) | 17 MB | 28 KB | 600× |
| Image files (PNGs) | 876 MB | 372 MB (WebP) | −58% (504 MB saved) |
| Search "cardio" | 991 KB / 660 KB gz | 21 KB | 30× |
| Search "asthma" (no match) | 991 KB | 95 KB | 10× |
| First chapter HTML (gz) | 18 KB | 2.8 KB | 85% |
| Exam page (gz) | n/a | 6.5 KB | — |

## Recipe (Supplements SKILL.md)

### A. cwebp batch conversion with resume

`scripts/webp_convert.py` is the pattern: skip files where `webp.mtime > png.mtime`, run with `-quiet` to suppress progress (saves CPU on long runs), report per-chapter size savings so the user sees the win.

```python
import subprocess, os
def convert_chapter(chapter_dir, site_root, quality=85):
    pngs = [os.path.join(root, f) for root, _, files in os.walk(chapter_dir)
            for f in files if f.endswith('.png')]
    total_png = sum(os.path.getsize(p) for p in pngs)
    total_webp = 0
    for png in pngs:
        webp = png[:-4] + '.webp'
        if os.path.exists(webp) and os.path.getmtime(webp) > os.path.getmtime(png):
            total_webp += os.path.getsize(webp); continue
        subprocess.run(['cwebp', '-q', str(quality), '-quiet', png, '-o', webp],
                      capture_output=True, timeout=60)
        total_webp += os.path.getsize(webp)
    return (total_png, total_webp, len(pngs))
```

Best per-chapter savings in this session: Ch24 haematology 87% (10 MB → 1.3 MB), Ch26/29/30/31/32 dermatology/psychiatry/maternal/adolescence/older 88-93% (mostly diagrams). Worst: Ch9 palliative -73%, Ch8 oncology -61% (heavily illustrated).

### B. nginx `try_files` falls through when directory has no execute permission

A real session lost 30 min to this:

```bash
# Symptom: 200 OK with the wrong content (usually index.html)
curl -I http://server/assets/search/16-cardiology.json
# Content-Type: text/html, Content-Length: 98964 (the index.html size!)

# Cause: the directory has 644 perms (no execute) so nginx can't traverse
docker exec container stat -c "%a" /path/to/dir/
# 644 — wrong!

# Fix: directory needs 755, files need 644
docker exec container chmod 755 /path/to/dir/
docker exec container find /path -type f -exec chmod 644 {} \;
```

**Symptom signature**: file exists and is correct on disk, but `curl` returns 200 with HTML content from a different file. ETag and Last-Modified headers belong to the fallback, not the file you asked for.

### C. Docker container permissions from `docker cp`

Every `docker cp` writes files as `root:root 600`. nginx workers (often `nginx` user) can't read them. After any `docker cp` burst:

```bash
docker exec CONTAINER find /usr/share/nginx/html -type f -exec chmod 644 {} \;
docker exec CONTAINER find /usr/share/nginx/html -type d -exec chmod 755 {} \;
# Don't chown -R nginx:nginx unless you know the worker user
```

`docker commit` persists the changes across container restarts. Use it during dev, full rebuild for production.

### D. 4-JSON split pattern (exam/flashcard database)

The 17 MB monolithic `questions.json` fetched 3× per page. Split by content type:

```
questions-index.json   5 KB   (always loaded, chapter meta)
questions-mcq.json    10 MB  (lazy on MCQ start)
questions-sba.json   800 KB  (lazy on SBA start)
questions-flashcard.json 5.5 MB (lazy on flashcard start)
```

Shared `site-db.js` exposes `MedSeaDB.loadChunks(['mcq', 'sba'])` that fetches only on user action, not on page load. Win: 100-500× lighter initial page load.

**2026-06 extension — per-chapter shards:** `questions-by-chapter/{num}-{mcq|sba|flashcard}.json`. When user picks ≤**15** chapters (`SHARD_MAX_CHAPTERS` in `site-db.js`), fetch only those shards in parallel; else fall back to monolith. Exam/flashcards pass `SETUP.chapters` into `_loadChunks(mode, chapterNums)`.

**Deploy when `docker build` times out:** `tar cf - . | docker exec -i medsea tar xf - -C /usr/share/nginx/html/` from `site/`; then `chmod 644` files / `755` dirs in container. Bump `sw.js` `CACHE_VERSION` on JS/bank changes.

### E. Search index split with auto-expand (32 chapter files)

```
search-index.json     3 KB   (manifest: {chapters, files: {slug → url}})
search/<slug>.json   ~30 KB each (32 files, 990 KB total)
```

JS uses **lazy per-chapter loading**:

```javascript
let idx = Object.create(null);  // per-chapter cache map
let searchManifest = null;

function loadIdx() {
  if (searchManifest) return Promise.resolve(searchManifest);
  return fetch('/assets/search-index.json').then(r => r.json()).then(m => {
    searchManifest = m; return m;
  });
}

function loadChapterIdx(slug) {
  if (idx[slug]) return Promise.resolve(idx[slug]);
  const url = searchManifest.files[slug];
  return fetch(url).then(r => r.json()).then(arr => { idx[slug] = arr; return arr; });
}

function chaptersMatching(q, m) {
  const ql = q.toLowerCase();
  const out = [];
  for (let i = 0; i < m.chapters.length && out.length < 3; i++) {
    if (m.chapters[i].indexOf(ql) >= 0) out.push(m.chapters[i]);
  }
  return out;
}

function search(q) {
  loadIdx().then(m => {
    let slugs = chaptersMatching(q, m);
    if (!slugs.length) slugs = m.chapters.slice(0, 5);
    return Promise.all(slugs.map(loadChapterIdx));
  }).then(arrs => {
    // ... filter and render hits
  });
}
```

**Auto-expand** for queries that don't match a chapter name: if < 3 hits from initial 5 chapters, lazy-load the remaining 27 in background and re-render. Without this, "asthma" (matches Ch 17 respiratory, not Ch 1-5) returns 0 results.

### F. Service worker version bump invalidates cache

When you push new code but the SW keeps serving old:

```javascript
const CACHE_VERSION = 'medsea-v2';  // BUMP on every deploy
// activate handler deletes old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(k => k !== CACHE_VERSION).map(k => caches.delete(k))
    )).then(() => self.clients.claim())
  );
});
```

### G. `<picture>` element for WebP + PNG fallback

```html
<picture>
  <source srcset="/path/to/image.webp" type="image/webp">
  <img src="/path/to/image.png" alt="..." loading="lazy" decoding="async" width="1280">
</picture>
```

Modern browsers (97%+) use WebP; old browsers fall back to PNG. The `width="1280"` prevents CLS. The `loading="lazy"` defers off-screen images.

In JS, generate the path by string-replace:

```javascript
const webpPath = pngPath.replace(/\.png$/i, '.webp');
return `<picture>
  <source srcset="/${slug}/${webpPath}" type="image/webp">
  <img src="/${slug}/${pngPath}" alt="..." loading="lazy" decoding="async" width="1280">
</picture>`;
```

### H. Strip inlined mobile sections

Many static-site generators inline the mobile-expanded view inside a hidden `<div class="m-only">` — dead weight for desktop users AND a separate copy that doubles HTML size.

**Detection**: look for `.m-only { display: none }` blocks in inline CSS, find the matching HTML section, extract just the heading + first few cards, drop the rest.

**Savings**: 17 MB → 213 KB on Ch 16. 80 MB total across 32 chapters.

**Watch out**: this can break the JS that hydrates the mobile view on click, AND any JS that scans DOM for topic bodies. Strip carefully; verify by clicking topics after.

### I. Git push hangs on large binary (3+ MB)

Mermaid.min.js (3.2 MB) caused `git push` to hang for 3+ min in `pack-objects` with no output. Symptom: `git send-pack` shows the process running indefinitely.

**Fix**: add `*.webp` and any other large binaries to `.gitignore`, ship a `setup.sh` that does `wget URL -O file`. Document the file in README so users know to run setup before first build.

```bash
git config --global http.postBuffer 524288000  # raise buffer to 500 MB if you must push
# But better: just don't commit large binaries
```

### J. Browser cache after JS update

When you deploy new JS, the browser may keep using the OLD version from its HTTP cache (1h default) or the service worker cache. To force a fresh fetch:

1. Bump the service worker `CACHE_VERSION` (see F above)
2. OR add a cache-busting query string: `script.js?v=2`
3. OR instruct the user to hard-refresh (Ctrl+Shift+R)

Best practice: bump a versioned query string in your HTML whenever the JS file changes:
```html
<script src="/assets/app.js?v=20260621"></script>
```

### K. Responsive WebP variants with `<picture srcset>` (mobile/tablet/desktop)

WebP is the first 60% win. The next 30% comes from serving **the smallest variant that fits the viewport**. For sites with ~50-100 large medical/illustration PNGs, add 480w and 960w variants + a single `<picture>` element so the browser picks automatically.

**The `srcset` + `sizes` recipe (works in 97%+ browsers):**

```html
<picture>
  <source srcset="
      /path/topic.webp 1280w,
      /path/topic-960w.webp 960w,
      /path/topic-480w.webp 480w"
    sizes="(max-width: 768px) 480px, (max-width: 1280px) 960px, 1280px"
    type="image/webp">
  <img src="/path/topic.png"
    srcset="/path/topic.png 1x"
    sizes="(max-width: 768px) 480px, (max-width: 1280px) 960px, 1280px"
    alt="..." loading="lazy" decoding="async" width="1280">
</picture>
```

**When to generate 480w/960w**: only for images >200 KB. Smaller ones already fit comfortably. For MedSea's 3,034 PNGs, 33 (the >300 KB ones) needed variants; the rest just got the single WebP.

**Generation script (Pillow)** — only runs on the >200 KB subset, with skip-if-exists so it's safe to re-run:

```python
from PIL import Image
from pathlib import Path

for webp in Path('site').rglob('*.webp'):
    # Skip variants themselves; only process base WebPs
    if any(s in webp.name for s in ['-480w', '-960w', '-1600w', '-800w', '-400w']):
        continue
    if webp.stat().st_size < 200_000:
        continue
    base = webp.with_suffix('')
    for w, suffix in [(480, '-480w'), (960, '-960w')]:
        out = webp.parent / f'{webp.stem}{suffix}.webp'
        if out.exists():
            continue
        img = Image.open(webp)
        ratio = w / img.width
        img.resize((w, int(img.height * ratio)), Image.LANCZOS)\
           .save(out, 'WEBP', quality=75, method=6)
```

**Measured wins (MedSea Ch2 deprescribing):**
- PNG 823 KB → WebP 345 KB (single, -58%)
- WebP 345 KB → **480w WebP 102 KB (mobile, -88% vs original PNG)**
- WebP 345 KB → **960w WebP 339 KB (tablet, -59%)**

**JS dynamic injection** (when the image URL comes from JSON, not static HTML):

```javascript
const imgBase = png.replace(/\.png$/i, '');
const webpBase = '/' + chapterSlug + '/' + imgBase + '.webp';
const srcsetWebp = [
  webpBase + ' 1x',
  webpBase.replace('.webp', '-960w.webp') + ' 960w',
  webpBase.replace('.webp', '-480w.webp') + ' 480w'
].join(', ');

return `<picture>
  <source srcset="${srcsetWebp}"
    sizes="(max-width: 768px) 480px, (max-width: 1280px) 960px, 1280px"
    type="image/webp">
  <img src="/${chapterSlug}/${png}" loading="lazy" decoding="async" width="1280">
</picture>`;
```

**Important: ship the responsive variants in your container, not just the host filesystem.** If you only run the WebP generator on the host and forget to copy the `-480w.webp` / `-960w.webp` files into the running nginx container, the browser will get 404s for those sizes and fall back to the 1x WebP. See pitfall L for the only reliable way to copy many files into a running container.

### L. Docker cp + find path prefix bug

`docker cp HOST_FILE CONTAINER:/dest/` expects the **destination to be a file path**, and when you pipe a list of files via shell globs, the relative path gets mangled:

```bash
# WRONG — docker cp treats this as "create directory tree under /dest/"
find site -name "*.webp" -exec docker cp {} container:/usr/share/nginx/html/ \;
# Result: files land at /usr/share/nginx/html/site/<chapter>/... (extra site/ prefix)

# ALSO WRONG — docker cp with a list of files just errors out
docker cp $(find site -name "*.webp") container:/usr/share/nginx/html/
# Result: "Could not find the file /usr/share/nginx/html/site/..." errors
```

**The reliable pattern — tar pipe preserves paths:**

```bash
# From the directory whose layout you want to preserve
cd /path/to/host
find site -name "*-480w.webp" -o -name "*-960w.webp" \
  | tar --null -cf - -T - \
  | docker exec -i CONTAINER tar -xf - -C /usr/share/nginx/html/
```

If you accidentally created a `site/` prefix inside the container, fix it with:
```bash
docker exec CONTAINER sh -c 'cd /usr/share/nginx/html && cp -r site/* . && rm -rf site'
```

**Always verify after copy** — 404 on a previously-working file path means the prefix is wrong. Quick check:
```bash
docker exec CONTAINER sh -c 'ls /usr/share/nginx/html/2-clinical-therapeutics/diseases/ | head -5'
# If output is empty, you have a prefix bug
```

### M. `chmod 600` on individual assets → 403 Forbidden (re-hits the user every time)

`docker cp` writes files as `600 root:root`. nginx workers (often running as `nginx` user) **cannot read them** and return 403 Forbidden. After any `docker cp` burst, the fix is one of:

```bash
# For all files under the web root
docker exec CONTAINER find /usr/share/nginx/html -type f -exec chmod 644 {} \;
docker exec CONTAINER find /usr/share/nginx/html -type d -exec chmod 755 {} \;

# For a specific asset you just added (faster)
docker exec CONTAINER sh -c 'find /usr/share/nginx/html -name "*-480w.webp" | xargs chmod 644'
```

**This is the most common "I updated the JS but the browser still shows old code" trap.** If you see `HTTP/1.1 403 Forbidden` for a file that exists and you just `docker cp`'d it, it's the permissions, not the SW or the browser cache.

**Symptom signature**: server returns 403 with `Content-Length: 146` (the standard 403 page size), and the file definitely exists on disk. Always check permissions before suspecting the service worker or nginx config.

**Where it bites hardest**: if you write a new JS file via `write_file` on the host, then `docker cp` it, you must also `chmod 644` it inside the container. The skill workflow is: write → cp → chmod → verify. Skip the chmod and the next 10 min becomes a wild goose chase.

### N. Browser automation DOM staleness — verify with curl, not browser_evaluate

In some browser-automation sessions, `browser_snapshot` shows real page content (the accessibility tree is correct), but `browser_console(expression)` returns empty DOM (`document.body.innerHTML === ''`, `querySelectorAll('*').length === 3`). This is a stale-DOM quirk in the automation layer, not a real page bug.

**Symptom signature**: snapshot says "32 chapter cards visible" but `document.querySelectorAll('button').length` returns 0.

**Workaround**: use `terminal(curl ...)` or `process(poll)` for verification instead of `browser_evaluate`. Measure HTTP response sizes, `Content-Type`, and `Content-Length` headers directly — those come from the real server, not the browser layer.

```bash
# Reliable for verifying a fix
curl -s -I http://localhost:8855/assets/chapter.js | head -3
curl -s -H "Accept-Encoding: gzip" -o /dev/null -w "%{size_download} %{time_total}s\n" URL
```

If you must use `browser_evaluate`, reload the page first via `browser_navigate(url?bust=N)` to force a fresh state.

### O. Cloudflare + Service Worker cache-bust — bumping `CACHE_VERSION` alone is not enough

When the site sits behind Cloudflare (or any CDN that caches aggressively by URL), **bumping `const CACHE_VERSION = 'medsea-vN'` in `sw.js` does NOT cause browsers to download the new SW**. Cloudflare serves the cached old `/sw.js` response, the browser sees no change, and the SW never upgrades. The user reports "I pushed the new version but mobile users still see old code".

**Symptom signature**: `curl https://site/sw.js` returns the old `CACHE_VERSION` constant. With cache-bust query (`?v=vN`) it returns the new one. The browser sees only the un-busted URL by default, so it never sees the new version.

**Two-part fix (both required):**

**Part 1 — `Cache-Control: no-cache` on `/sw.js` in nginx.** Without this, the CDN caches the SW for its full TTL and even after you fix Part 2, browsers asking for the un-busted URL still get the cached old version.

```nginx
server {
    # ... other server config ...

    # Service worker must never be cached (force browser to detect updates)
    location = /sw.js {
        add_header Cache-Control "no-cache, no-store, must-revalidate" always;
        add_header Pragma "no-cache" always;
        add_header Expires "0" always;
    }
}
```

After saving, `nginx -t && nginx -s reload`. Verify with `curl -I https://site/sw.js` — should show `cache-control: no-cache, ...`. With Cloudflare in front, the `cf-cache-status` header should be `BYPASS` or `DYNAMIC` (not `HIT`).

**Part 2 — Register SW at a query-busted URL.** This is the part that bypasses CDN cache. Cloudflare caches by URL, so `/sw.js?v=v4` is a different cache key from `/sw.js` and isn't cached:

```javascript
// chapter.js (or wherever the SW is registered)
if ('serviceWorker' in navigator && location.protocol !== 'file:') {
  window.addEventListener('load', function () {
    navigator.serviceWorker.register('/sw.js?v=v4').catch(function (e) { /* silent */ });
  });
}
```

When the user clears cache, hard-refreshes, or visits a new page, the browser fetches `/sw.js?v=v4` → CDN doesn't have it → origin serves the new SW → browser installs it → SW activate handler deletes the old `medsea-v3` cache → next navigation uses the new SW.

**The version string must change on every deploy.** If you re-deploy without bumping `?v=vN`, you're back to the same problem.

**Quick verification recipe after deploying:**

```bash
# Without bust: should serve no-cache
curl -m 5 -sI https://site/sw.js | grep -iE "cache-control|cf-cache-status"

# With bust: should serve the new SW + no-cache
curl -m 5 -sL "https://site/sw.js?v=v4" | grep CACHE_VERSION | head -1
# expect: const CACHE_VERSION = 'medsea-v4';

# Both should now be in sync
```

If the un-busted URL still returns the old SW from CF cache, you need Part 1 (no-cache headers) before Part 2 helps. The two work together: Part 2 forces a different cache key, Part 1 prevents the original key from being a stale forever-cache.

**Pitfall — opening the site from the same browser**: even after fixing both parts, a browser that already has the SW installed will not re-fetch `/sw.js?v=vN` until you either (a) hard-refresh, (b) close all tabs to the site and reopen, or (c) wait for the SW's normal update check (typically 24h). For verification on a live user device, ask them to hard-refresh once. After that one refresh, all subsequent visits pick up new versions automatically.

### P. Mobile sticky bottom action bar — long setup pages hide the CTA below the fold

On mobile, any setup / configuration page with many options (mode toggles, time/count inputs, 27 chapter chips, etc.) ends up with the "Start" / "Submit" / "Continue" button below the fold. The user picks a chapter, looks for the button, doesn't see it, assumes the page is broken. Mobile UX test always fails on first deploy without this.

**Symptom signature**: button is visible in the DOM (`document.getElementById('btn-start')` works), click handler is wired, but on a phone (≤720 px wide) the button is scrolled off-screen and the user can't reach it without scrolling past everything.

**Fix — pin the action bar to the viewport bottom on mobile only.** Apply this at the end of the page CSS:

```css
.start-bar { display: flex; justify-content: space-between; align-items: center; margin-top: 6px; }
.summary-line { font-size: 12px; color: var(--text-dim); }

/* Mobile sticky bottom action bar */
@media (max-width: 720px) {
  .start-bar {
    position: sticky;
    bottom: 0;
    background: linear-gradient(180deg, rgba(10, 14, 26, 0) 0%, rgba(10, 14, 26, 0.95) 24%, rgba(10, 14, 26, 0.98) 100%);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    margin: 14px -20px -20px;       /* bleed to card edges */
    padding: 14px 20px 18px;
    border-top: 1px solid var(--border);
    z-index: 50;
    gap: 12px;
  }
  .start-bar .btn { flex-shrink: 0; min-height: 44px; padding: 12px 20px; }  /* 44px = iOS tap target */
  .start-bar .summary-line { font-size: 11px; line-height: 1.3; }
  #panel-setup { padding-bottom: 16px; }   /* so scroll content can clear the bar */
}
```

The `backdrop-filter: blur(12px)` is what makes this look polished — the page content scrolls behind the bar with a frosted-glass effect, so the user can still see what they're scrolling over.

**Verification on desktop (1280 px)**: bar is `position: static`, sits at the bottom of the setup card. CSS rule exists in stylesheet but doesn't activate (media query doesn't match). Verify with:

```javascript
const sb = document.querySelector('.start-bar');
const s = getComputedStyle(sb);
// On desktop: {position: "static", bottom: "auto"}
// On mobile:  {position: "sticky", bottom: "0px"}
```

**iOS Safari caveat**: `backdrop-filter` requires the `-webkit-backdrop-filter` prefix AND requires the element to have a non-transparent background for the blur to be visible. The gradient background provides both.

**Safe-area-inset for notched phones**: on iPhones with home-indicator, add `padding-bottom: calc(18px + env(safe-area-inset-bottom))` so the bar clears the home indicator.

**Always verify on a real phone**, not just by resizing the browser window. Mobile browser emulation is unreliable for `position: sticky` inside `overflow: auto` ancestors — it works differently than real devices.

## Workflow

This session used the **long-running-batch-workflows** skill to break the work into steps with cool-downs (32 chapters × 3,034 PNGs would have overheated a laptop in one go). When making your website fast, use that skill to avoid thermal throttling during the conversion phase.

## Verification

After every change, measure:

```bash
# HTML only
curl -s -o /dev/null -w "size=%{size_download} time=%{time_total}\n" \
  -H "Accept-Encoding: gzip" URL

# In browser
JSON.stringify(performance.getEntriesByType('resource')
  .map(r => ({n: r.name, size: r.encodedBodySize, dur: Math.round(r.duration)})))
```

Show actual before/after numbers, not adjectives. "10× faster" requires `time_before` AND `time_after`. Honest "8.5/10, here's what isn't 10/10 yet" beats inflated "perfect" claims.

## Anti-pattern: claiming "all done" without re-verification

Dr. Sagar's hard rule: **do not claim a perf pass is complete based on the last edit you made.** A user query like "is all chapter image process complete, no more large image?" deserves a fresh measurement, not a re-statement of what you just changed.

The pattern that loses his trust:
1. You claim "all 3,034 PNGs converted to WebP, 504 MB saved, all good"
2. He asks "is anything still large?"
3. You re-state the same claim without re-measuring
4. He pushes back: "Okk continue check" — meaning *go actually look, don't just re-assert*

**The correct pattern** when asked "is X complete?" or "any more large images?":
1. Re-run the actual measurement (e.g. `find site -name "*.webp" -size +300k | wc -l`)
2. If something new comes up (33 WebPs were still 300-600 KB), admit it and fix it
3. Report new numbers, not old ones

This is a real skill transfer pattern: when the user asks for verification, the verification is a fresh measurement, not a defensive re-statement of prior claims. Even if you're 95% sure nothing changed, a 30-second probe buys you a credibility you cannot buy back from a wrong "yes, all done".
