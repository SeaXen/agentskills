# Subject extraction for pas test stem rewrites

## Problem

When `autogen_scenario_sbas.py` writes the `## PasTest Scenario SBAs`
section, every stem it produces begins with either:

- `Which of the following features is most specific or characteristic of <SUBJECT>?`
- `What is the most appropriate first-line therapy for <SUBJECT>?`

The rebuilder rewrites these to:

- `In a patient with suspected <SUBJECT>, which of the following findings would be most characteristic?`
- `A patient presents with <SUBJECT>. What is the most appropriate initial management?`

The rewrite needs a clean `<SUBJECT>` to splice in.

## Why this fails for `topic.md`-folder topics

In `rebuild_question_bank_v5.py`, `topic_label_from_path(md_path, ch_slug)` returns
`(topic_slug, pretty)` where `pretty` is derived from the **file stem**. For files
of the form `chapters/16-cardiology/diseases/16.1.25-atherosclerosis-pathogenesis/topic.md`,
the stem is literally `"topic"` — so `pretty` is `"Topic"`.

That means `topic_title` is `"Topic"`, not `"Atherosclerosis Pathogenesis"`. If you
naively do:

```python
def rewrite_pastest_stem(stem, topic_title):  # topic_title == "Topic"
    s = stem.strip()
    feature_prefix = 'Which of the following features is most specific or characteristic of '
    first_line_prefix = 'What is the most appropriate first-line therapy for '
    if s.startswith(feature_prefix):
        return f'In a patient with suspected {topic_title}, which of the following findings...'
    # ... WRONG: produces "In a patient with suspected Topic, which..."
```

you get junk like `In a patient with suspected Topic, which of the following findings would be most characteristic?`

## Fix — extract the subject from the original stem itself

The autogen already put the real subject into the stem. Pull it from there, not from `topic_title`:

```python
def rewrite_pastest_stem(stem: str, topic_title: str) -> str:
    s = stem.strip()
    feature_prefix = 'Which of the following features is most specific or characteristic of '
    first_line_prefix = 'What is the most appropriate first-line therapy for '
    if s.startswith(feature_prefix):
        subject = s[len(feature_prefix):].rstrip(' ?.') or topic_title
        return f'In a patient with suspected {subject}, which of the following findings would be most characteristic?'
    if s.startswith(first_line_prefix):
        subject = s[len(first_line_prefix):].rstrip(' ?.') or topic_title
        return f'A patient presents with {subject}. What is the most appropriate initial management?'
    return s
```

`subject = s[len(prefix):].rstrip(' ?.')` strips the prefix and trims trailing punctuation
that the autogen sometimes adds (`?.`). Falls back to `topic_title` only if the prefix was the
entire string (which would be a parsing bug, but the fallback is defensive).

## When the same problem bites `pastest_to_vignette_with_features`

The same issue applies if you take the source-derived frame approach in
`pastest_to_vignette_with_features()`. If `extract_topic_frame()` returns `None` (very common for
folder-based `topic.md` files) and you fall back to `topic_title`, you'll get `"features
consistent with Topic"`-style stems.

**Always extract the subject from the autogen-generated stem** rather than trusting `topic_title`.
`topic_title` is only reliable for flat `*.md` files (e.g. `chapters/3-clinical-genetics/diseases/3.2.03-multifactorial-inheritance.md`)
where the stem is the real topic name.

## Coverage check

```bash
cd /mnt/tb/Sea-knowledge/#MedSea
python3 -c "
import json
sba=json.load(open('site/assets/questions-sba.json'))
hits=[q for q in sba if 'In a patient with suspected Topic' in q['question'] or 'presents with Topic' in q['question']]
print('junk-rewrite hits:', len(hits))  # MUST be 0
"
```

If the count is non-zero, the rewrite function is using `topic_title` instead of extracting from the stem.