# Auto-Generating MCQs and Flashcards from Clinical Content

**Use when the source markdown has clinical content (Viva Questions, High-Yield tables, Definitions, One-Page summaries) but no explicit `## MCQs` / `## SBA Questions` / `## Flashcards` sections.** This is the pattern that got MedSea from 17/32 chapters covered to 32/32.

Validated 2026-06-21 — produced 19,489 MCQs + 2,283 SBAs + 20,813 flashcards across all 32 chapters from existing topic.md content.

## Why this matters

Most clinical notes (Davidson, Oxford Handbook, study packs) have:
- "Viva Questions" — question/answer tables already in the right shape for flashcards
- "High-Yield Summary" / "Key Facts" — Topic/Fact tables that map directly to MCQs
- "Definitions / Key Concepts" — Term/Definition tables
- "One-Page Revision Card" — Domain/Key Points tables

These are already curated exam-prep content. Auto-generating MCQs/flashcards from them requires NO LLM, NO human authoring, and gives 100% chapter coverage immediately.

## The four content shapes you can mine

| Source section | Heading keywords (case-insensitive match) | Maps to | Notes |
|---|---|---|---|
| **Viva Questions** | `viva question`, `viva` | Flashcards | 1:1 Q→front, A→back. Highest signal — already in Q&A form |
| **High-Yield Summary** | `high-yield exam points`, `high-yield summary`, `fcps/mrcp high-yield`, `high-yield pearls`, `exam pearls (fcps`, `key exam points`, `key facts`, `core facts`, `key concepts` | MCQs | Topic/Fact table → "Which of the following is correct about {Topic}?" with chapter-fact distractors |
| **Definitions / Key Concepts** | `definitions / key concepts`, `definitions / concepts` | MCQs + Flashcards | Term/Definition — use for both |
| **One-Page Revision Card** | `one-page revision card`, `one-page revision summary`, `revision summary` | Flashcards | Domain/Key Points → Q: "Domain?", A: "Key points" |

Use the same section detector pattern as the explicit-extraction state machine:

```python
def find_section(sections, *keywords):
    """Return (name, body) of first section whose name contains any keyword."""
    for name, body in sections:
        for kw in keywords:
            if kw in name:
                return name, body
    return None, None
```

## MCQ auto-generation algorithm

For each row `(Topic, Fact)` in a high-yield table:

```
correct_answer = Fact[:120] + ('…' if longer)
question = f'Which of the following is the correct statement about <strong>{Topic}</strong>?'

# Pick 3 distractors from the SAME chapter's fact pool
# (so they're domain-plausible, not random unrelated text)
pool = [f for f in chapter_facts[ch_num] if f != Fact and len(f) > 5]
distractors = random.sample(pool, 3)  # seed by qid for determinism

# Fallback distractors if pool is too small
if len(distractors) < 3:
    fallbacks = ['Not applicable / Not associated with this condition',
                 'Opposite of the correct statement',
                 'A different clinical entity entirely']
    distractors = (distractors + fallbacks)[:3]

options = {'A': correct, 'B': distractors[0], 'C': distractors[1], 'D': distractors[2]}
# Shuffle deterministically (seeded by qid) so A/B/C/D position is stable
random.seed(qid + 'shuf')
shuffled = {letters[i]: options[['A','B','C','D'][i]] for i in range(4)}
answer_letter = next(k for k, v in shuffled.items() if v == correct)
```

**Critical choices:**
- Seed `random` with the question ID so each question has stable A/B/C/D positioning across regenerations
- Always include the correct answer in the options pool first, then sample distractors
- Cap at 8 MCQs per topic — take the first N rows (typically the most foundational)
- **Use the chapter's own fact pool as distractors** — this gives domain-plausible wrong answers instead of obviously unrelated text. "Differentiate SIADH from CSW by volume status" vs random "Diabetes in pregnancy" distractors is a real test; vs "Wrong answer" is trivially easy.

## Flashcard auto-generation algorithm

For each row in a Viva Questions / One-Page Revision table:

```
flashes.append({
    'id': hash_id(prefix, chapter_num, topic_slug, front_text),
    'chapter_num': ch, 'chapter_name': name, 'chapter_slug': slug,
    'topic_slug': topic,
    'front': front_text,  # raw Q text from Viva, or "Term?" for Definitions
    'back': back_text,
    'auto_generated': True,  # mark so UI can show "auto" badge if needed
})
```

For Definitions tables, prepend `?` to the term so the question reads naturally: "Folate (B9)? → Water-soluble; generic term for vitamer family..."

## Sample outputs (validated 2026-06-21)

**Viva → Flashcard:**
- Front: "What is the primary HLA association with T1DM?"
- Back: "HLA-DR3/DR4-DQ2/DQ8; DR3/DR4 heterozygous = highest risk (OR 15-20)"

**High-Yield → MCQ:**
- Q: "Which of the following is the correct statement about **HLA**?"
- A: "DR3/DR4-DQ2/DQ8 = 40-50% risk; DR3/DR4 het = highest; DR15-DQ6 = protective"
- B: "INS VNTR, PTPN22, CTLA4, IL2RA, IFIH1; 50+ loci total"  (random other chapter fact)
- C: "40-50% heritable; prevention trials targeting high-risk"  (random other chapter fact)
- D: "Not applicable / Not associated with this condition" (fallback)

**Definitions → Flashcard:**
- Front: "Folate (B9)?"
- Back: "Water-soluble; generic term for vitamer family (folic acid, DHF, THF, 5-methyl-THF, etc.)"

## Caveats (be honest with the user)

- **Templated questions**: All auto-MCQs use the same "Which of the following is the correct statement about X?" stem. They're useful for **recognition drill** but not real exam-style SBAs.
- **Distractors are random facts**, not curated plausible-but-wrong answers. Better than placeholder text, worse than human-authored.
- **Chapters that lack all four section types** still get 0 questions. MedSea: Ch 18, 22 only have flashcards because their topic.md files don't have any High-Yield / Definitions / Viva sections matching the patterns. (Ch 22 might need source-level content addition.)
- **Real high-quality exam questions** (Ch 11, 19, 26) require human-authored vignettes. The auto-generator gets to 100% chapter coverage at templated quality, not exam simulation quality.

## Performance

- 4,000 topic.md files
- Two-pass extract: ~30 seconds end-to-end
- Output: ~17 MB minified JSON (acceptable; loads in <1s on browser)
- All processing is regex + simple Python — no LLM calls, no external APIs

## Integration with the existing extractor

Replace the single `for ch in chapters: extract()` loop with:

```python
# Pass 1: index (subdirs + flat files)
file_index = index_all_topics(SITE)  # (ch_num, ch_name, slug, topic_slug, text, has_explicit)

# Pass 1.5: collect chapter fact pools
chapter_facts = collect_chapter_facts(file_index)

# Pass 2: extract + auto-generate
for cn, chn, cs, ts, text, has_explicit in file_index:
    facts = chapter_facts.get(cn, [])
    if has_explicit:
        mcqs, sbas, flashes = parse_topic(text, cn, chn, cs, ts)
        amcq, asba, afc = extract_auto_questions(text, cn, chn, cs, ts, global_facts=facts)
        all_mcq.extend(mcqs + amcq)
        all_sba.extend(sbas)
        all_flash.extend(flashes + afc)
    else:
        amcq, asba, afc = extract_auto_questions(text, cn, chn, cs, ts, global_facts=facts)
        all_mcq.extend(amcq)
        all_flash.extend(afc)
```

The `extract_auto_questions` function lives in `scripts/auto_gen.py` — see the full implementation in the skill's scripts directory.
