# MedSea exam UI — filters, queues, modals (2026-06-24)

## `/exam/` setup

| Feature | Behavior |
|---------|----------|
| Topic filter | `#topic-filter` — `topic_slug` prefix or exact |
| Authored only | Hides `pastest-autogen` in pool |
| MRCP mock | `#ch-mrcp` — ch 1–15, 180 Q, 180 min, both |
| Weak queue only | `#ch-weak` — `MedSea.Flagged` IDs only |
| Bookmarks only | `#ch-bookmarks` — `MedSea.Bookmarks` IDs only |
| URL params | `?ch=&topic=&authored=1&mode=&count=` |
| Quality hint | `#quality-hint` — `index.quality` + queue counts |

`availableCount()` uses index totals (and authored_* when checkbox on); topic/bookmark/weak filters apply at **Start** after chunk load.

## Review + runner

- Rationales: `explanation` when authored `**Answer: X** — …`
- **Each Q** toggle: `data-showafter="each"` (not `"0"`)
- Dynamic options A–E from `q.options` keys
- Review: flag, bookmark, report issue, practice topic links

## Modals

`MedSea.showModal` — submit, quit, clear history. Requires `#medsea-modal` in `exam/index.html` and `flashcards/index.html`.

## Flashcards parity

Topic/authored URL params, due-only (SpacedRep), finish modal, `explanation` on flip.

## Cross-links

- Weak/bookmark/report/export: `references/study-ux-bookmarks-reports-export-2026-06.md`
- Deploy: `references/release-ops-and-quality-gates-2026-06.md`

Verify: `node --check site/assets/exam-engine.js` after edits; bump SW on deploy.