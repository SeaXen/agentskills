# Exam + flashcard answers and rationales (2026-06-24)

## Exam (MCQ/SBA)

| Field | Source | UI |
|-------|--------|-----|
| `answer` | Parsed from `**Answer: X**` / bold option | Scored; shown in review + **Each Q** after pick |
| `explanation` | Text after `**Answer: X** — …` in same block | **Rationale** in result review and runner reveal |

**Not every item has `explanation`.** Report `index.quality` after rebuild — do not guess.

**Explicit `—` lines in source** plus **rebuild backfill** (2026-06-24):

| Source | Mechanism |
|--------|-----------|
| `**Answer: X** — …` | `parse_explanation_from_block` |
| PasTest `> **Answer:**` blockquote | `parse_blockquote_answer_rationale` |
| `**Correct Answer:**` paragraph | same parser chain |
| Bold correct option (authored only) | `explanation_from_correct_option` → `explanation_source: correct_option` |

**Do not backfill autogen** (`pastest-autogen`) from longest-option heuristic — only non-autogen rows get the relaxed “longest option ≥22 chars” pass.

Typical coverage **after backfill** (honest band, re-measure each rebuild):

- SBA: **~70–76%** · MCQ: **~75–78%** · FC: **~53%** (topic QA copy + `A: —` in flash sections)
- `sba_expl_from_option` / `mcq_expl_from_option` counts in `index.quality`

**80% target:** still needs explicit `—` lines in `topic.md` for remaining gaps — run `scripts/chapters_needing_rationales.py` and `scripts/suggest_rationale_stubs.py`.

### Authoring pattern (grow coverage)

```markdown
**Answer: B** — One-line why B is correct (exam teaching point).
```

### Rebuilder (`rebuild_question_bank_v5.py`)

- `parse_explanation_from_block` + `enrich_parsed_block` on MCQ/SBA parsers
- `clean_explanation_text` — strip tables, `>`, `*Source:*`
- PasTest: `expl = parse_explanation_from_block(block)`

### Exam UI (`exam/app.js`)

- End review + **Each Q** after pick: Correct letter + Rationale or *No written rationale in source*
- Practice link: `/exam/?ch=&topic=&authored=1`

## Flashcards

| Field | Role |
|-------|------|
| `back` | Short **answer** on flip |
| `explanation` | Optional rationale under answer (`#c-expl`) |

Sources: `A: ans — rationale` (`split_fc_answer`); `enrich_flashcards_from_topic_qa` from same-topic MCQ/SBA.

## Verify counts

```bash
python3 site/scripts/rationale_coverage_report.py
python3 site/scripts/chapters_needing_rationales.py   # sprint order (Ch 17, 26, 22…)
python3 site/scripts/suggest_rationale_stubs.py       # paste-ready **Answer: X** — lines
```

After rebuild, `site/assets/quality-snapshot.json` mirrors `index.quality` + totals for dashboards/cron.

Or:

```python
import json
idx=json.load(open('site/assets/questions-index.json'))
print(idx.get('quality'))
```

Per-file:

```python
import json
for path, key in [('questions-sba.json','explanation'),('questions-flashcard.json','explanation')]:
    rows=json.load(open(f'site/assets/{path}'))
    n=sum(1 for x in rows if (x.get(key) or '').strip())
    print(path, n, '/', len(rows))
```

## Honest reply to user

- Exam: correct answer always when bank valid; rationale **when field populated**.
- Flashcards: answer = `back`; explanation **optional** on flip.