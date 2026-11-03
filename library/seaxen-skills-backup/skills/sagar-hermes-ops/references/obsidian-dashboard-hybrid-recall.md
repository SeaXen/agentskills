# Obsidian dashboard hybrid recall

Use this when adding or debugging recall/search in the read-only Obsidian dashboard used as Hermes memory UI.

## Why this pattern
When the environment does not have `sentence_transformers`, `faiss`, or `torch`, do not block on embeddings. A useful local hybrid recall layer can still be built from:
- SQLite FTS5 keyword retrieval
- normalized token overlap
- trigram/Jaccard phrase similarity
- wikilink graph proximity
- shared tags
- same-folder affinity
- recency weighting

This is good enough for dashboard-side recall suggestions and keeps the dependency footprint small.

## Runtime discovery first
Before editing:
1. Read the user service file and treat it as source of truth.
2. Confirm:
   - `ExecStart`
   - vault path env vars
   - dashboard port
   - working directory
3. If there are duplicate-looking paths such as `/root/.hermes/...` and `/mnt/...`, verify whether they are actually the same file before patching both.

## Implementation shape that worked
- Keep the feature inside the existing dashboard script instead of pushing it into the main Hermes memory provider when the goal is vault browsing/recall UX.
- Add a dedicated `/api/recall` endpoint instead of bloating `/api/graph`.
- Persist the local recall index in a SQLite file under `~/.hermes/`.
- Refresh or ensure the index during note-scan lifecycle so the UI does not require a separate manual init step.
- Store a content signature in the SQLite DB and reuse it across process restarts so unchanged vaults do not trigger needless full rebuilds.
- Keep the existing broken-link workflow intact; only replace the top half of the recall panel.
- Cache recall responses in the frontend and invalidate on note/query/folder/list-mode changes.
- Add a lightweight `/api/recall-eval` heuristic harness after the core recall works. Use note-context neighbor cases plus shared-tag query cases so you can measure hit@k/MRR on the live vault without adding embeddings or labeling infrastructure.
- Add a lightweight feedback loop after eval works: persist `up/down` votes for recall results in the same SQLite DB, expose `/api/recall-feedback` + `/api/recall-feedback-summary`, and surface counts/recent misses in the UI. This gives real user labels for future tuning without introducing another service.
- Use feedback as a conservative ranking nudge, not a dominant signal. A useful pattern is per-title `(up - down) / total` capped to a small boost/penalty so bad labels cannot overpower lexical/graph relevance.
- Add a memory lifecycle layer before attempting autonomous memory writes: `/api/memory-health` for structure/link/recall/noise score, `/api/memory-candidates` for high-signal candidate detection, and `/api/memory-review` for approve/reject/edit status. Keep it human-approved; do **not** auto-write vault notes from candidates.
- Candidate routing that worked: root-cause/fix/verified lines → `System/Assistant/issues-fixes-log.md`; decision/policy/rule lines → `Memory/decisions.md`; preference lines → `System/Assistant/preferences.md`; workflow/pipeline lines → project/work notes. Reject noisy lines that look like TODOs, raw logs, templates, already-distilled fixes, or stale progress.
- Preserve support tables when rebuilding the SQLite recall DB. If `ensure_hybrid_recall_index()` deletes/recreates the DB on note-signature changes, first dump and restore `recall_feedback` and `memory_review`; otherwise review decisions appear successful, then vanish after note edits/service restart.
- Treat example wikilinks in templates/docs as real graph edges. Replace placeholder examples like `[[Note Name]]`, `[[like this]]`, or `[[related note]]` with existing notes such as `[[Dashboard]]`, or escape/remove them, otherwise health checks report false broken links.
- For “10/10 memory health” verification, run it after a service restart, not just in-process. Probe `/api/memory-health`, `/api/memory-candidates`, `/api/recall-eval`, and a real `/api/recall?...`; then confirm browser UI renders the Memory Health panel. Target: broken links 0, orphans 0, duplicate headings 0, pending candidates 0, recall Hit@5 1.0, MRR 1.0.
- Do not equate backend `100/100` with dashboard `10/10`. Browser-check that the health/readiness panel is the default visible surface for the relevant tab, that the nav label communicates readiness clearly (for example `Health 100`, not an ambiguous feedback count), and that generic note content does not compete with the health cards.
- If a dashboard workspace is meant to communicate readiness, make the status cards dominate above the fold: expand the meta/content region, hide unrelated markdown body if needed, avoid sticky action bars that overlap cards, and verify with both DOM layout measurements and an unannotated screenshot.
- When browser screenshots show red boxes/labels/overlays, distinguish tool annotations from product UI. Confirm suspected overlays by checking DOM state/computed style and rerunning an unannotated visual pass before treating them as defects.
- When building FTS5 MATCH strings from note titles/tags/dates, quote each token before joining. Hyphenated/date-like tokens such as `2026-05-25` can otherwise be parsed as bare columns/operators and crash live requests with errors like `sqlite3.OperationalError: no such column: 05`.

## Verification sequence
Do not stop after patching code.
1. `python3 -m py_compile <dashboard.py>`
2. Import the module directly and run the scan/query path in Python.
3. Restart the user service.
4. Probe live endpoints such as:
   - `/api/graph`
   - `/api/recall?...`
   - `/api/note?...`
5. Open the real browser UI and confirm the panel renders, loads, and shows clickable ranked results.

## Common pitfalls
- Editing the wrong script path because the service runs a different file.
- Assuming two paths need duplicate edits when they are the same inode.
- Declaring the feature done after unit-level checks without live HTTP/browser verification.
- Forcing an embedding stack into a small dashboard feature where FTS5 + reranking is enough.
