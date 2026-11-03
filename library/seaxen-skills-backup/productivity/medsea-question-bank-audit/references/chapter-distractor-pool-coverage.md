# Chapter Distractor Pool Coverage

The `autogen_scenario_sbas.py` script keeps a curated per-chapter
`DISTRACTOR_POOLS` dictionary of REAL clinical alternatives for use
as wrong-answer options on pas test SBAs. The rebuilder
(`rebuild_question_bank_v5.py`) consumes this pool to swap generic
placeholder text (`An unrelated condition not matching the clinical
picture of X`, etc.) for real MRCP/FCPS-grade alternatives.

This reference tracks pool coverage, the same-3-distractor repetition
bug that lives below the pool, the cross-topic noise bug that lives
inside the rotator, and the canonical Python snippets to measure each.

## Pool coverage map (post 2026-06-22 answer-quality pass)

**All 32 chapters now have a curated `DISTRACTOR_POOLS` entry.** Live
bank has **0 / 12,774 placeholder distractor slots**.

The answer-quality pass added pools for the remaining 13 chapters:
- `1`: sensitivity / specificity / NNT / RCT / cohort
- `2`: ACE-i / beta-blocker / statin / metformin / ADR types
- `3`: AD / AR / X-linked / mitochondrial inheritance
- `5`: vit A/B12/C/D deficiency, Fe/Zn/Se/Cu, refeeding
- `6`: RCT / cohort / case-control / biases / screening
- `7`: beta-lactam / aminoglycoside / macrolide / fluoroquinolone / MRSA / VRE / ESBL
- `12`: viper / elapid / colubrid / spider / scorpion
- `13`: heat stroke / hypothermia / frostbite / mountain sickness / cholera / typhoid
- `15`: syphilis / chancroid / LGV / gonorrhoea / chlamydia / HIV
- `18` (alias of `15`): AKI / CKD / UTI / stone / GN / RAS
- `19`: respiratory/metabolic acidosis/alkalosis, Na/K disorders, parathyroid
- `29`: MDD / bipolar / GAD / panic / PTSD / OCD / alcohol/opioid use
- `31`: delayed/precocious puberty / Turner / Klinefelter / eating disorders
- `32`: Alzheimer / vascular / Lewy body / frontotemporal / falls / frailty

But adding pools was **only half the answer**. The other half is the
**per-item distractor rotator** — see "Same-3-distractor repetition"
section below. A chapter can have a 20-entry curated pool and still
produce identical `pool[0:3]` distractors on every item. Pools without
rotation = same repetitive items.

## Same-3-distractor repetition — the bug that lives below the pool

The pool upgrade fixes placeholder TEXT (`An unrelated condition not
matching...` → `Constrictive pericarditis`). It does **not** fix the
case where every item in a chapter gets the **same** 3 distractors
picked from the pool.

**Real example from the live bank before the answer-quality pass:**
Ch 16 Cardiology had 639 pas test items. **598 of them** (93.6%) had
the exact same distractor set:

```
('Constrictive pericarditis', 'Pulmonary embolism', 'Tension pneumothorax')
```

The autogen called `get_distractors(ch_slug, topic_kw)[0:3]` and that
returned the same 3 items every time because `topic_kw` mapped to the
same sub-pool (`tamponade`) for most Cardiology items, and `pool[0:3]`
is deterministic.

**The diagnostic that catches this** (count distinct 3-distractor sets
per chapter):

```python
import json
from collections import Counter
sba = json.load(open('site/assets/questions-sba.json'))
for ch in sorted({it['chapter_num'] for it in sba}):
    items = [it for it in sba if it['chapter_num']==ch
             and it.get('source')=='pastest-autogen']
    if not items: continue
    sets = Counter(tuple(sorted([v for k,v in it['options'].items()
                                 if k != it['answer']]))
                   for it in items)
    top, cnt = sets.most_common(1)[0]
    pct = 100*cnt/len(items)
    flag = ' WORST' if pct > 30 else ''
    print(f'Ch {ch:>2}: {len(sets):>3} distinct / {len(items):>4} items, '
          f'top-set {pct:>5.1f}%{flag}')
```

A chapter where the most common distractor set covers > 30% of items is
**broken** even if all distractors are real clinical alternatives.

**The fix — `rotate_distractors_through_pool()` in the rebuilder:**

```python
import hashlib

def rotate_distractors_through_pool(items: list[dict]) -> int:
    """Per-item deterministic offset in the chapter pool, so no two
    items in the same chapter share the same 3 distractors.
    """
    rewritten = 0
    for item in items:
        pool = _resolve_distractor_pool(item['chapter_slug'],
                                       item.get('topic_title',''),
                                       item.get('question',''))
        if len(pool) < 4:
            continue
        opts = item.get('options') or {}
        if len(opts) < 3: continue
        ans_letter = item.get('answer', '')
        ans_text = opts.get(ans_letter, '').strip()
        if not ans_text: continue
        # Stable per-item offset — same item id always gets same distractors
        seed = (item.get('id', '') + '|' + item.get('topic_slug', '') +
                '|' + item.get('question', '')[:40])
        h = int(hashlib.md5(seed.encode('utf-8')).hexdigest(), 16)
        # Rotate the pool, skip the answer text, take the first 3
        n = len(pool)
        rotated = [pool[(h % n + i) % n] for i in range(n)]
        chosen = []
        for cand in rotated:
            if cand.strip().lower() == ans_text.lower(): continue
            if cand in chosen: continue
            chosen.append(cand)
            if len(chosen) == 3: break
        if len(chosen) < 3: continue
        new_opts = dict(opts)
        slots = [k for k in ['B','C','D'] if k != ans_letter][:3]
        for slot, cond in zip(slots, chosen):
            new_opts[slot] = cond
        item['options'] = new_opts
        rewritten += 1
    return rewritten
```

Wire it in at the end of `build()` in `rebuild_question_bank_v5.py`:

```python
sba_rotated = rotate_distractors_through_pool(sba_rows)
mcq_rotated = rotate_distractors_through_pool(mcq_rows)
print(f'Answer-quality pass: rotated {sba_rotated} SBAs, {mcq_rotated} MCQs')
```

**Result on live bank after this pass:**
| Chapter | Before | After |
|---|---|---|
| 16 Cardiology | 31 distinct sets / 639 items, top-set 93.6% | **61 distinct sets**, topic-keyword-aware |
| 17 Respiratory | ~5 distinct sets | **45** |
| 27 Neurology | 4 distinct sets | **31** |
| 22 GI | 1 distinct set | **15** |

## Cross-topic distractor noise — the bug that lives inside the rotator

The flat-merged pool (every entry from every sub-pool concatenated)
gives every item more options, but it also produces **cross-topic
distractors**. An "Acute pancreatitis" item ended up with `Hemorrhoids /
IBS / Ulcerative colitis` because those were in the Ch 22 default pool.
Real differential? No — colon differential, not pancreatic.

**The fix — `_resolve_distractor_pool()` that prefers topic-keyword
sub-pools:**

```python
def _resolve_distractor_pool(ch_dir: str, topic_title: str,
                              question: str = '') -> list[str]:
    """Pick the best distractor pool for an item.

    Tries (in order):
    1. topic_keyword(title) sub-pool — clinically relevant distractors
    2. topic_keyword(question) sub-pool — when title is collapsed
       (e.g. autogen wrote topic_title='Topic' for everything)
    3. chapter-level merged pool — chapter-wide alternates
    """
    from autogen_scenario_sbas import (DISTRACTOR_POOLS, topic_keyword)
    pool = []
    kw_title = topic_keyword(topic_title or '')
    sub = DISTRACTOR_POOLS.get(ch_dir, {}).get(kw_title)
    if sub:
        pool = list(sub)
    # Try question text if title was uninformative
    if (len(pool) < 4 or kw_title == 'default') and question:
        kw_q = topic_keyword(question or '')
        if kw_q and kw_q != kw_title:
            sub_q = DISTRACTOR_POOLS.get(ch_dir, {}).get(kw_q)
            if sub_q:
                seen = set(pool)
                for it in sub_q:
                    if it and it not in seen:
                        seen.add(it); pool.append(it)
    # Fall back to chapter-level merged pool
    if len(pool) < 4:
        seen = set(pool)
        merged = list(pool)
        for area, items in DISTRACTOR_POOLS.get(ch_dir, {}).items():
            if area == kw_title: continue
            for it in items or []:
                if it and it not in seen:
                    seen.add(it); merged.append(it)
        pool = merged
    if len(pool) < 4:
        return CHAPTER_DISTRACTORS.get(ch_dir) or []
    return pool
```

**Key pitfall — `topic_keyword('Topic')` returns `'default'`**, because
no keyword in the regex list matches the literal word "Topic". When
the autogen collapses every topic title to "Topic" (which it does for
many Ch 16 items), the naive resolver falls back to `default` for every
item. The question-text fallback (`topic_keyword(question)`) recovers
most of these because the question still contains clinical keywords
like "ACS classification", "STEMI", "tamponade".

**Trade-off:** topic-keyword-aware rotation produces **fewer distinct
sets** than flat-pool rotation (sub-pools are smaller, e.g. 4–7 entries,
so the rotator is bounded by C(n,3) combinations), but the distractors
are **clinically relevant**. For MRCP/FCPS exam quality, **topic-
relevance wins over distinct-set count**. Don't optimize for the higher
distinct-set number if it comes from cross-topic noise.

## How to measure coverage in one Python snippet

```python
import json, collections
sba = json.load(open('site/assets/questions-sba.json'))
GENERIC = ('an unrelated condition not matching',
           'symptomatic treatment only',
           'empiric broad-spectrum',
           'standard guideline-directed',
           'routine supportive care',
           'symptom-directed treatment',
           'an advanced/surgical therapy',
           'a complication seen late in the disease',
           'a condition that mimics',
           'a feature common to many',
           'a non-specific sign',
           'an investigation finding rather than')
per = collections.Counter()
still = collections.Counter()
for q in sba:
    if q.get('source') != 'pastest-autogen': continue
    per[q['chapter_num']] += 1
    text = ' '.join((v or '').lower() for v in q['options'].values())
    if any(p in text for p in GENERIC):
        still[q['chapter_num']] += 1
print(f'TOTAL still placeholder: {sum(still.values())} / {sum(per.values())}')
for ch in sorted(per):
    if still[ch] > 0:
        print(f'  ch{ch:2d}: still={still[ch]}/{per[ch]}')
```

## Pattern for adding a new pool

```python
'NN-chapter-slug': {
    'keyword1':   ['Real condition A', 'Real condition B',
                   'Real condition C', 'Real condition D'],
    'keyword2':   ['...', '...', '...', '...'],
    'default':    ['Always-available alternative 1',
                   'Always-available alternative 2',
                   'Always-available alternative 3',
                   'Always-available alternative 4'],
},
```

The `default` key is the fallback when no topic keyword matches. The
rebuilder picks the first 3 items from whichever sub-pool matches
(never reuse the same item twice and never let the answer leak into
the distractor set).

## Why this matters

When the distractor pool is missing, the autogen SBAs still ship but
their wrong-answer options read like:

- `An unrelated condition not matching the clinical picture of X`
- `A feature common to many acute inflammatory conditions`
- `Standard guideline-directed first-line therapy`
- `Symptomatic treatment only, no disease-modifying therapy`

These are correct in the trivial sense ("they're wrong") but they
don't *teach*. A real MRCP candidate sees the placeholder text and
immediately rules it out as a non-option, which makes the question
trivial regardless of whether they know the correct answer. The
distractor pool is the difference between a usable practice question
and a templated one.

## Hard-won lessons

- **Chapters with clinical scenarios that are hard to distract** (e.g.
  ch 29 psychiatry, ch 31 adolescent medicine) tend to have many
  placeholder items. Add their pools first when reducing the gap.
- **The `default` sub-pool must be a real clinical alternative** for
  the chapter's domain. Don't reuse it across chapters — it makes
  questions feel interchangeable.
- **Keep pool items short** (≤4 words). Long alternatives look like
  prompt fragments.
- **Never put the topic title itself in its own pool.** Symptom:
  `Tamponade` topic shows `Tamponade` as option B.
- **Chapter mappings must be patched in BOTH autogen scripts** when
  adding a new source chapter family (`autogen_scenario_sbas.py`
  AND `autogen_study_sections.py`). One-mapping drift = chapters
  that show up in one surface (e.g. SBA) but not the other
  (e.g. flashcards).
- **Don't trust "distinct set count" alone** as a quality metric.
  Ch 16 went from 31 → 99 distinct sets with the flat-merged pool,
  but several of those sets were cross-topic noise (an ACS item
  with stroke distractors). After switching to topic-keyword-aware
  resolution, the count dropped to 61 — but every set is
  clinically coherent. The lower number is the better number.
- **`topic_keyword()` is title-biased.** When the autogen collapses
  topic_title to "Topic", the keyword extractor returns 'default'.
  Always try `topic_keyword(question)` as a fallback before giving
  up on the topic-relevant sub-pool.
- **Don't write to source `.md` files and call it a "deploy".** The
  autogen step produces files on disk; the rebuild step produces the
  JSON bank; the docker cp step ships it to the container; the verify
  step proves the live HTTP serves the new bank. All four steps must
  complete before you can claim "live verified". See the *Deploy
  Verification Gate* section in `SKILL.md` for the canonical four-step
  cycle.