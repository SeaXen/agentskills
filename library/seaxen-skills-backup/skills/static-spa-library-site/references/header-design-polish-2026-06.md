# MedSea header design polish (2026-06)

Validated on `:8855` after user asked for **10/10 design without breaking** exam/flashcards/PWA.

## When to use

- Header feels crowded (7 stat pills), exam/flashcards stats mismatch home, search hits look bolted-on, mobile has no drawer on `/exam/` or `/flashcards/`.
- User says: polish header, unify design, browse all pages first.

## Core rule

**Browse live** (`/`, `/exam/`, `/flashcards/`, one chapter `?topic=`) before CSS changes. **Additive CSS** only — do not rewrite home’s 2k-line inline header in one pass.

## File layout (single source of truth)

| Asset | Role |
|-------|------|
| `site/assets/site-header.css` | Base grid header (exam/flashcards/chapters with shared header) |
| `site/assets/site-header-polish.css` | **Additive**: compact stats breakpoints, search-hit row, topic bar, mobile shell |
| `site/assets/site-header.js` | Search (`attachSearch` desktop + mobile), chapter menu, `applyIndex` stats, mobile menu |
| `site/assets/medsea-header-stats.js` | Live counts + unified search placeholder from `questions-index.json` + `topics.json` |

**Do not** duplicate `header.site { ... }` blocks inside `exam/index.html` or `flashcards/index.html` — causes drift. Link both CSS files; keep page-local CSS to `main` + tool panels only.

## Compact stats

Mark pills:

- `stat--optional-1` → Hubs (hide ≤1320px)
- `stat--optional-2` → Topics (hide ≤1180px)
- `stat--optional-3` → Cards (hide ≤1024px)
- `stat--quality` → SBA rationale % (ellipsis on `.num`)

Exam/flashcards must include **`stat-sba`** and **`stat-quality`** like home.

## Search hits

One row per hit (not a second `<a>` row):

```html
<div class="search-hit-wrap">
  <div class="search-hit-row">
    <a class="search-hit-main" href="...">...</a>
    <div class="search-hit-actions">
      <a class="search-pill" href="/exam/?ch=...&topic=...&authored=1">Exam</a>
      <a class="search-pill search-pill--muted" href="/flashcards/?...">Cards</a>
    </div>
  </div>
</div>
```

Home inline search JS must match `site-header.js` `renderSearchHits()` HTML.

## Mobile (≤900px)

On exam/flashcards add after `</header>`:

- `.mobile-bar.medsea-mobile-shell` — logo, menu btn, `searchInputMobile`, tool links
- `.mobile-menu.medsea-mobile-shell#mobileMenu` — panel + `#mobileChapterList`

Polish CSS hides `header.site` and shows mobile bar. `applyIndex()` must fill stats + `mobileChapterList` **before** returning when `#chapterDropdown` is missing.

## `site-header.js` pitfalls

1. **`applyIndex` early return** — if `!$('#chapterDropdown')` returned before stats, mobile-only pages got no counts. Stats + mobile list first; dropdown second.
2. **`stat-mcq`** — must be `totals.mcq` only, not `mcq + sba`.
3. **`MEDSEA_PAGE_HANDLES_HEADER`** on home — index keeps inline search; still load `medsea-header-stats.js` for placeholders.
4. **Refactor search** — use `runSearch(q, resultsEl, boxEl)` + `attachSearch` twice; fix `slugs` scope for lazy chapter load.

## Topic practice bar

Use `#medsea-topic-bar` + classes in polish CSS — not inline `style.cssText` on chapter `?topic=` pages.

## Deploy

```bash
chmod -R a+rX site/
cd site && tar cf - sw.js index.html exam flashcards assets/site-header.js assets/site-header.css assets/site-header-polish.css assets/medsea-header-stats.js | docker exec -i medsea tar xf - -C /usr/share/nginx/html/
docker exec medsea find /usr/share/nginx/html -type f \( -name '*.html' -o -name '*.js' -o -name '*.css' \) -exec chmod 644 {} \;
```

Bump `sw.js` `CACHE_VERSION` (e.g. `medsea-v15`). Hard refresh required.

## Verify (do not claim 10/10 design without)

- `curl` exam HTML contains `site-header-polish`, `stat-sba`, `medsea-mobile-shell`
- `node --check assets/site-header.js`
- Browser: search placeholder matches topic count; resize hides optional stats; mobile menu opens on exam
- **Regression**: Start Exam, flashcard flip, PWA still loads

## Honest design score

Unified header + mobile shell ≈ **9/10** chrome. Remaining: chapter pages still use home-only mobile patterns; mindmap cream panels vs dark chrome; setup chip density.