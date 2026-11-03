# PWA SW v18, lazy-load, and critical CSS patterns (2026-06-27)

## SW v18 immediate-update — full sw-update.js toast

The `sw-update.js` file listens for SW `updatefound` events and shows a toast:

```javascript
/* MedSea SW update notifier.
   Listens for serviceWorker registration `updatefound` events and shows a
   non-intrusive toast prompting the user to reload. Never auto-reloads.
*/
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.ready.then(reg => {
    reg.addEventListener('updatefound', () => {
      const newWorker = reg.installing;
      if (!newWorker) return;
      newWorker.addEventListener('statechange', () => {
        if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
          showToast('Update available — reload to refresh');
        }
      });
    });
  });
}

function showToast(msg) {
  const toast = document.createElement('div');
  toast.textContent = msg;
  toast.style.cssText = 'position:fixed;bottom:16px;right:16px;background:#0d9488;color:#fff;padding:8px 16px;border-radius:8px;font-size:14px;z-index:9999;box-shadow:0 2px 8px rgba(0,0,0,0.2);cursor:pointer';
  toast.onclick = () => { window.location.reload(); };
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 8000);
}
```

Include on all pages: `<script src="/assets/sw-update.js"></script>`

## SW v18 sw.js key sections

```javascript
const CACHE_VERSION = 'medsea-v18';
const PRECACHE_SHARDS = [
  // 77 chapter shards — generate programmatically
  ...Array.from({length: 32}, (_, i) =>
    [`/assets/questions-by-chapter/${i+1}-sba.json`,
     `/assets/questions-by-chapter/${i+1}-mcq.json`,
     `/assets/questions-by-chapter/${i+1}-flashcard.json`]
  ).flat()
];

// install: skipWaiting + precache
self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil(caches.open(CACHE_VERSION)
    .then(c => c.addAll(CORE_ASSETS.concat(PRECACHE_SHARDS))));
});

// activate: clear old caches + clients.claim
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_VERSION).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

// message: SKIP_WAITING handler
self.addEventListener('message', (event) => {
  if (event.data === 'SKIP_WAITING') self.skipWaiting();
});
```

## Chapter topic lazy-load — chapter-topic-lazy.js

Included on all 32 chapter HTML pages. Renders first 50 topic links, hides rest, adds "Load more (N topics)" button.

Key pattern:
- `TOPICS_PER_PAGE = 50`
- Query `.topic-sidebar a[href]` links
- Hide links at index >= 50
- Add button with remaining count
- On click: show next batch of 50, update count, remove button when done

Verified on Ch 16 Cardiology (907 topics) — first paint: 50 links + "Load more (857 topics)".

## Critical CSS

`assets/critical.css` (2.1 KB) — header, hero, chapter grid, mobile media queries. Inlined in `index.html` `<style>` tag for fastest first paint. Non-critical CSS loads async.

## Shard prefetch

In `exam/app.js` and `flashcards/app.js`, after loading current chapter shard, `fetch()` the next chapter's 3 shards (sba/mcq/flashcard) with `mode: 'no-cors'` in the background. Silently fails if next chapter doesn't exist.

## One-command deploy script — deploy_medsea.sh

```bash
#!/usr/bin/env bash
# MedSea one-command deploy: release-check → build index → tar → fix perms
# Usage: bash scripts/deploy_medsea.sh [--yes]
#   without --yes: dry-run (release check + index only)
#   with --yes: tar into container + fix perms
```

Steps:
1. `bash scripts/medsea_release_check.sh` (exit if fail)
2. `python3 scripts/build_topic_bank_index.py`
3. `chmod -R a+rX site/`
4. `tar cf - sw.js exam assets flashcards chapters | docker exec -i medsea tar xf - -C /usr/share/nginx/html/`
5. `docker exec medsea find /usr/share/nginx/html -type d -exec chmod 755 {} \;`
6. `docker exec medsea find /usr/share/nginx/html -type f -exec chmod 644 {} \;`
7. Print "Deploy complete: SW version medsea-v18"

## Cache-bust strategy

After deploying new JS/CSS:
1. Bump `CACHE_VERSION` in `sw.js` (e.g. `medsea-v17` → `medsea-v18`)
2. Add `?v=N` query param on `<script>` includes in HTML (e.g. `exam-engine.js?v=18`)
3. This defeats both SW cache AND HTTP cache
4. User sees toast "Update available — reload to refresh" from `sw-update.js`

## DevOps additions

- **Git hooks:** `bash scripts/install_git_hooks.sh` installs pre-push hook → runs release check before push
- **pytest venv:** `python3 -m venv .venv && pip install pytest && .venv/bin/pytest tests/ -v` — 2 tests pass
- **Dead code check:** `for f in assets/*.js; do grep -qr "$f" --include='*.html' . || echo "DEAD: $f"; done` — caught `medsea-home-stats.js` (superseded by `medsea-header-stats.js` but never deleted)
