# MedSea exam + flashcard mechanical audit

Run after `rebuild_question_bank_v5.py` and before claiming "all questions correct / display good".

## What this proves vs does not prove

| Proves | Does not prove |
|--------|----------------|
| Answer letter exists in `options` | Clinically correct answer vs Davidson |
| No duplicate options within an item | Distractor rotation still clinically fair |
| IDs unique, index totals match files | `/exam/` HTML works behind nginx auth (403) |
| Flashcard front/back format clean | Every stem is a full PasTest vignette |
| Shard files match per-chapter counts | Literal **10/10 all sectors** (clinical needs expert panel) |

## Hard gates (must be 0)

```bash
cd /mnt/tb/Sea-knowledge/#MedSea/site
python3 scripts/verify_medsea_bank.py
python3 ../../.hermes/skills/productivity/medsea-question-bank-audit/scripts/bank_mechanical_audit.py
```

## Live verification (three truths)

1. Host: `len(json.load(...))` on each `questions-*.json`
2. HTTP: `curl` `questions-index.json` totals + `shards` key
3. `curl -I` `site-db.js` → **200** (not 403 from mode 600)
4. Sample shard: `questions-by-chapter/10-sba.json` → 200

## Answer E / five-option items

Render all non-empty keys from `q.options`, sorted — not hardcoded A–D only.

## Exam UI logic bugs (2026-06-24)

| Bug | Fix |
|-----|-----|
| `data-showafter="0"` on “Each Q” | Use `data-showafter="each"` |
| `text = om.group(2)` in PasTest loop | Use `opt_text` only |
| Stub filter `len<=3` on all MCQs | **Autogen only**; ≥2 acronym wrong opts |

## Post-rebuild filters in `main()`

- `is_definition_autogen_stem()` — all sources
- `has_stub_wrong_options()` — autogen only
- Recompute **mcq/sba/flashcard** counts on index
- `write_chapter_shards()` + `index.shards`

## Low-RAM load

`site-db.js`: ≤**15** chapters → shards. Pass `SETUP.chapters` into `_loadChunks(mode, chapterNums)`.

## Honest report shape

```
Mechanical: PASS (verify_medsea_bank.py)
Live totals: {sba, mcq, fc}; shards meta present
Rationales: SBA N/M, MCQ N/M, FC N/M with non-empty explanation (not 100% unless sourced)
Clinical: NOT FULLY VERIFIED
Exam UI: topic/authored/MRCP; Each Q shows rationale when present; SW version bumped
```