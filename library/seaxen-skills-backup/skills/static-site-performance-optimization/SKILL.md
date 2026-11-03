---
name: static-site-performance-optimization
description: 'Use when optimizing a static HTML/CSS/JS site for fast page loads. Covers diagnosing bottlenecks, extracting inline assets, splitting monolithic JSON, self-hosting CDN assets, adding HTTP cache + gzip, and shipping a service worker + PWA manifest. Triggers: make the site fast, site is slow, 10/10 performance, page load is slow, optimize the website, PWA, service worker, make it beast, best 10/10.'
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [performance, web, optimization, pwa, service-worker, image-optimization, nginx]
    related_skills: [long-running-batch-workflows, dashboard-ui-polish, medsea-chapter-audit]
---

# Static Site Performance Optimization

Systematic workflow for turning a slow static site into a sub-100ms experience. Apply the 6-step pattern in order, then verify every change with measured numbers (not adjectives).

## Reference index

The companion `references/web-perf-recipe.md` contains worked recipes A–P:
- **A** WebP batch conversion with resume
- **B** nginx `try_files` permission trap
- **C** Docker container permissions from `docker cp` (the 600 → 403 trap)
- **D** JSON split pattern for large databases
- **E** Search index split with auto-expand
- **F** Service worker version bump invalidates cache
- **G** `<picture>` element for WebP + PNG fallback
- **H** Strip inlined mobile sections
- **I** Git push hang on large binary
- **J** Browser cache after JS update
- **K** Responsive WebP variants with `<picture srcset>`
- **L** Docker cp + find path prefix bug
- **M** `chmod 600` on individual assets → 403 Forbidden
- **N** Browser automation DOM staleness — verify with curl, not browser_evaluate
- **O** **Cloudflare + Service Worker cache-bust** — bumping `CACHE_VERSION` alone fails when CF caches `/sw.js`; needs both `Cache-Control: no-cache` headers AND query-busted registration URL
- **P** **Mobile sticky bottom action bar** — long setup pages hide the CTA below the fold; pin action bar to viewport bottom on `≤720px` with `backdrop-filter: blur`
- **Q** **Chapter-sharded question JSON** — per-chapter exam/flashcard shards for low RAM; see `references/chapter-sharded-question-json.md`
- **R** **Topic-scoped load** — `?topic=` without `?ch=` must not pull monolith JSON; see `references/topic-scoped-exam-flash-load.md`

The most commonly re-hit pitfalls are **C/M** (docker cp permissions — fix is `chmod 644` after cp), **O** (CF+SW cache bust needs both nginx header AND JS registration change), and **P** (mobile sticky bar — verify on a real phone, not browser-resized).

## Quiz / exam apps — chapter-sharded JSON (low RAM + CPU)

When a static site loads **multi‑MB** `questions-*.json` on every exam/flashcard start, mobile browsers pay a large `JSON.parse` + heap cost even if the user only picked one chapter.

**Pattern (MedSea 2026-06-24):**

1. Rebuild writes monoliths **and** `assets/questions-by-chapter/{chapter_num}-{mcq|sba|flashcard}.json`.
2. `questions-index.json` stays ~8 KB (chapter counts only).
3. Loader (`site-db.js`): if `chapterNums.length` is 1–32, `Promise.all` fetch shards; else fetch monolith.
4. Pass **effective** chapters into `_loadChunks(mode, chapterNums)` — include chapter inferred from `topicFilter` when chips are empty (`medsea-chapter-filter.js`).
5. Optional: `topic-bank-index.json` + prefetch on topic input so counts and Start are fast without monolith parse.
5. nginx: `gzip_vary on`, `gzip_min_length 256`, cache headers on `/assets/questions*.json`.
6. Bump service worker `CACHE_VERSION` when loader or bank layout changes.

**Measure:** compare `curl` download size for `10-flashcard.json` vs full `questions-flashcard.json` after gzip.

See also `medsea-question-bank-audit` → `references/exam-flashcard-mechanical-audit.md` (shards + gates).

**Topic URL slow load:** Recipe **R** — `references/topic-scoped-exam-flash-load.md`.

## PWA service worker — v18 immediate-update pattern

When the SW caches aggressively, users see stale assets until ALL tabs close. Three changes make updates instant:

1. **`self.skipWaiting()` on install** — new SW activates immediately, doesn't wait for old one to die.
2. **`self.clients.claim()` on activate** — new SW takes control of all open tabs right away.
3. **`SKIP_WAITING` message handler** — standard API for client-triggered update.
4. **Precache shards** — list all chapter shards in a `PRECACHE_SHARDS` array so they're cached on first SW install, not on first fetch.

```javascript
const CACHE_VERSION = 'medsea-v18';
const PRECACHE_SHARDS = [
  '/assets/questions-by-chapter/1-sba.json',
  '/assets/questions-by-chapter/1-mcq.json',
  // ... all 77 shards
];

self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil(caches.open(CACHE_VERSION).then(c => c.addAll(CORE_ASSETS.concat(PRECACHE_SHARDS))));
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(k => k !== CACHE_VERSION).map(k => caches.delete(k))
    )).then(() => self.clients.claim())
  );
});

self.addEventListener('message', (event) => {
  if (event.data === 'SKIP_WAITING') self.skipWaiting();
});
```

**SW update toast** — listen for `updatefound` on the SW registration and show a non-intrusive banner. Never auto-reload — user choice. See `references/pwa-sw-v18-and-lazy-load-2026-06.md` for the full `sw-update.js` toast implementation.

## Chapter topic list lazy-loading — "Load more" pagination

Chapter pages with 900+ topic links render all at once → slow DOM parse + high memory. Fix with a simple "show first 50, Load more for the rest" pattern:

```javascript
// chapter-topic-lazy.js — included on all chapter pages
const TOPICS_PER_PAGE = 50;
const links = document.querySelectorAll('.topic-sidebar a[href]');
const total = links.length;
links.forEach((link, i) => {
  if (i >= TOPICS_PER_PAGE) link.parentElement.style.display = 'none';
});
// Add "Load more (N remaining)" button
if (total > TOPICS_PER_PAGE) {
  const btn = document.createElement('button');
  btn.textContent = `Load more (${total - TOPICS_PER_PAGE} topics)`;
  btn.onclick = () => { /* show next batch, update count, remove when done */ };
  sidebar.appendChild(btn);
}
```

**Measured:** Ch 16 Cardiology (907 topics) — first paint shows 50 links + "Load more (857 topics)" button instead of rendering 907 `<a>` tags.

## FastAPI dashboard optimization note

For self-hosted FastAPI dashboards, see `references/fastapi-dashboard-phase2-optimization.md` for the proven phase-2 pattern: add `.dockerignore`, externalize large inline JS, self-host CDN assets like Chart.js, enable gzip, set static cache headers, and verify cold-vs-warm endpoint timings after deploy.

When adding multiple dashboard tabs over SQLite/log aggregates, see `references/fastapi-dashboard-tabs-lazy-cache.md`: default to a lightweight Home page, lazy-render tabs, refresh only the current page, cache bounded aggregate endpoints, destroy old Chart.js instances, and update Dockerfile `COPY` when adding imported backend modules.

For all-time operator dashboards over Hermes/SQLite data, add a warm-start pattern: precompute the heaviest all-time dashboard collectors during FastAPI startup, prefer SQL aggregates over Python row scans for totals/by-source/by-model/timelines, cap chart timelines server-side (for example 400 points) and downsample again client-side (for example ~96 points), use AbortController to cancel in-flight page fetches on tab switches, and keep first table loads lighter with short client caches for repeat opens. For cold-load complaints, also ensure SQLite analytics indexes at startup, split dashboard aggregate fetch from row-list fetch so the page paints progressively, and trim first-row loads (AceRoute pass used 50 rows). See `references/aceroute-fastapi-all-time-dashboard-pattern.md` and `references/aceroute-cold-load-perf-pattern.md` for the concrete AceRoute patterns.

Do not let perf work hide layout-system failures. If a dense dashboard still shows giant cards, random spans, or dead areas across many tabs, audit shared CSS/grid rules before more micro-optimization.

For the follow-on packaging pass — BuildKit-ready Dockerfile layout, missing runtime dependency pinning, image-based CasaOS manifests, and beginner-facing README structure — see `references/fastapi-dashboard-packaging-and-casaos.md`.

## Critical CSS inlining

Extract above-the-fold CSS (header, hero, first content card) into a separate `critical.css` file and inline it in `<style>` tags in `index.html`. Non-critical CSS loads async. This eliminates render-blocking on the largest CSS file for first paint.

## Shard prefetch — next chapter

After loading the current chapter's shard, background-fetch the next chapter's shard so the user's next selection is instant:

```javascript
function prefetchChunks() {
  const nextCh = currentChapter + 1;
  if (nextCh > 32) return;
  const kinds = ['sba', 'mcq', 'flashcard'];
  kinds.forEach(k => {
    fetch(`/assets/questions-by-chapter/${nextCh}-${k}.json`, { mode: 'no-cors' }).catch(() => {});
  });
}
```