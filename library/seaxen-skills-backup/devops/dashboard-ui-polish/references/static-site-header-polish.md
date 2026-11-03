# Static site header polish (MedSea-style)

**When:** User asks for design 10/10 on a static nginx site — browse all routes first; do not break exam/flashcard logic.

## Pattern (additive)

1. `site-header-polish.css` after `site-header.css`; strip duplicate header CSS from page inline styles.
2. Responsive stats: `stat--optional-*` hide at breakpoints.
3. Mobile bar + drawer on exam/flashcards (match home).
4. Search: one row + Exam/Cards pills (`search-hit-row`, `search-pill`).
5. `medsea-header-stats.js` on all app pages.
6. Chapters: `@import` polish in `chapter.css`; dark mindmap/flowchart (not cream on dark chrome).

## Verify

curl 200 on new assets; bump `sw.js` CACHE_VERSION; hard refresh; mobile + resize. No "10/10 design" without live browse.

Cross-ref: `static-site-performance-optimization` → `references/topic-scoped-exam-flash-load.md`.