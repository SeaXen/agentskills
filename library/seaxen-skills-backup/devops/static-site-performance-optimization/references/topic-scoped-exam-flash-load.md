# Topic-scoped exam / flashcard load (MedSea v16 pattern)

**When:** User opens `/exam/?topic=16-1-69-doppler-echocardiography` or types a topic filter — session feels slow because the app downloaded **full** `questions-mcq.json` (~6 MB) + `questions-sba.json` (~4 MB) then filtered in JS.

## Root cause

1. `SETUP.chapters` empty when only `?topic=` is set → loader uses monolith path.
2. `SHARD_MAX_CHAPTERS` was 15 → "system-based" (ch 16–32) or "all 32" exceeded cap → monolith again.
3. `availableCount()` used chapter totals from index — misleading for topic filter (showed thousands, Start still slow).

## Fix (four pieces)

### 1. Infer chapter from topic slug

```javascript
// medsea-chapter-filter.js
function chapterNumFromTopicSlug(slug) {
  var m = String(slug || '').trim().match(/^(\d{1,2})[.\-]/);
  return m ? parseInt(m[1], 10) : null;
}
function effectiveChapterNums(setup) {
  if (setup.chapters && setup.chapters.length) return setup.chapters.slice();
  var ch = chapterNumFromTopicSlug(setup.topicFilter);
  return ch ? [ch] : null;
}
```

Slug examples: `16-1-69-doppler-echocardiography`, `16.1.25` → chapter **16**.

On `applyUrlParams` + topic input: `applyTopicChapterScope(setup, refreshChips)` selects the chapter chip.

### 2. Raise shard cap to 32

`site-db.js`: `SHARD_MAX_CHAPTERS = 32` so clinical (1–15), system (16–32), and all-chapter picks still use per-chapter shards.

### 3. Background prefetch

When topic/chapter scope is known, call `loadModeChunks` / `loadCards` **before** Start (debounced on topic input). Repeat visit: cache hit → instant Start.

### 4. `topic-bank-index.json`

Build: `python3 site/scripts/build_topic_bank_index.py` (reads monoliths, writes ~300 KB map `topic_slug → {ch, mcq, sba, fc, authored_*}`).

`medsea-topic-bank.js`: `matchingCount(setup)` for exam, `matchingFlashCount` for flashcards — accurate "N matching" without loading bank.

## Verify

```bash
curl -sS -w 'ch16-mcq:%{size_download}B %{time_total}s\n' -o /dev/null \
  http://127.0.0.1:8855/assets/questions-by-chapter/16-mcq.json
curl -sS -w 'full-mcq:%{size_download}B %{time_total}s\n' -o /dev/null \
  http://127.0.0.1:8855/assets/questions-mcq.json
```

Expect **~50–300 KB** per chapter shard vs **multi-MB** monolith.

## Pitfall

**All chapters, no topic** still loads monoliths — by design. Only topic URL or explicit ≤32 chapter selection avoids full parse.

## Deploy

Bump `sw.js` `CACHE_VERSION` when changing loader scripts. Tar deploy: `site-db.js`, `exam/app.js`, `flashcards/app.js`, `topic-bank-index.json`, filter helpers.

**P0 — engine must load:** If `window.MedSea` is false, `exam-engine.js` may throw before export (e.g. undefined `fmtDateTime` in `Format`). Fix engine + `exam-engine.js?v=N` on HTML. See `sagar-hermes-ops` → `references/medsea-live-browser-verification.md`.

Cross-ref: `medsea-question-bank-audit` → `references/exam-flashcard-mechanical-audit.md`; `chapter-sharded-question-json.md` (Recipe Q).