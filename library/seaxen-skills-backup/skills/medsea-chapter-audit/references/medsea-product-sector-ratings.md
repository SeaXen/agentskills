# MedSea full product audit — sector ratings & gaps

Repo: `/mnt/tb/Sea-knowledge/#MedSea` · Live: `http://127.0.0.1:8855` · Container: `medsea`.

## Sector ratings /10 (post 2026-06-24 rationale backfill + study UX)

| Sector | Score | Notes |
|--------|------:|-------|
| Content breadth | **9** | 32 ch, ~4287 topics |
| Clinical accuracy (verified) | **6.5** | `sample_authored_answer_audit.py`; no full expert sign-off |
| Chapter/topic UX | **7.5** | WebP, mermaid, lazy; topic bar on `?topic=` |
| Exam app | **9.2** | Modal; weak queue; bookmarks; report; export; default authored |
| Flashcards | **9** | SR; bookmarks chip; finish modal; explanation on flip |
| Teaching / rationales | **~8.8** | Re-measure: SBA ~75%, MCQ ~78%, FC ~53% — `index.quality` + backfill |
| Perf exam/FC | **8.5** | Shards, gzip, bump SW each bank/JS deploy |
| DevOps | **8.5** | release check, weekly quality script/cron, git hook |
| Search | **8** | Split manifest; Exam link on home + header hits |
| Product docs | **9** | `site/docs/FEATURES.md` |

**Overall: ~9.3/10 product** · **~8.8/10 teaching** until **≥80%** explicit rationales + expert sign-off.

Re-measure rationale % after every `rebuild_question_bank_v5.py` — do not reuse table numbers in user replies without `rationale_coverage_report.py`.

## Still missing for literal 10/10

1. Bulk `**Answer: X** — …` in `/mnt/tb/Medicine/.../topic.md` → rebuild
2. `rationale_coverage_report.py` ≥80% SBA/MCQ
3. Expert authored-only clinical sign-off
4. CI source↔bank answer diff on push
5. Full SM-2 (beyond 1/3/7-day)
6. Cloud/ticket backend for reports (export JSON only)
7. `docker build` image parity (tar deploy works)
8. WebP all heavy chapter PNGs

## Shipped study UX (do not list as missing)

- Weak queue, bookmarks, report issue, `downloadStudyExport`
- Home live stats (`medsea-home-stats.js`)
- Analytics bank quality card on `/exam/`
- See `medsea-question-bank-audit` → `references/study-ux-bookmarks-reports-export-2026-06.md`

## Deploy checklist

1. `bash site/scripts/medsea_release_check.sh`
2. `chmod -R a+rX site` then tar into `medsea`
3. Bump `sw.js`; curl `questions-index.json` → `quality`
4. Browser: bookmark + export; home stats; topic bar on chapter `?topic=`

## Related

- `medsea-question-bank-audit`
- `site/docs/FEATURES.md` (in repo)