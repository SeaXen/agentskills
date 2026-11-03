# Canonical Injection Pattern for Vault Recall (2026-06-17)

## Problem

FTS5 token matching is exact-stem. When a query contains "stroke" but the
canonical note `Medical Study System.md` uses "cerebrovascular accident" or
"neurology chapter", the canonical is **not** in the FTS5 candidate set at
all. No amount of score boosting will fix this — the row doesn't exist to be
boosted.

Curated evals tend to use wording the canonicals already contain
("davidson", "fcps", "mrcp"). Real user queries use everyday synonyms
("stroke", "physiology book", "cardio chapter") and the canonical is missed.

This pattern was developed to fix the case "Read only Stroke Medicine MOC +
target note + max 1 relevant hub" which was returning a 2026-06-09 daily
note instead of `Medical Study System`.

## The pattern

In `query_hybrid_recall()`, after the FTS5 + fallback candidate set is built,
inject the relevant canonical notes when the matching intent is detected:

```python
RECALL_CANONICAL_NOTES = {
    "Hermes Operations": ("ops", "setup"),
    "Medical Study System": ("medical",),
    "decisions": ("decision",),
    "issues-fixes-log": ("fix",),
    "Obsidian Vault Setup": ("setup", "ops"),
    "AGENT": ("ops", "setup"),
    "context": ("ops",),
    "preferences": ("preference",),
}

# Inside query_hybrid_recall(), after the FTS5 + fallback rows are built:
if query_intents:
    canonical_paths = set()
    for title, intents_required in RECALL_CANONICAL_NOTES.items():
        if any(intent in query_intents for intent in intents_required):
            for note in notes:
                if note.get("title") == title:
                    canonical_paths.add(note.get("path"))
                    break
    if canonical_paths:
        seen_paths = {row["path"] for row in rows}
        for path in canonical_paths:
            if path not in seen_paths:
                canon = next((n for n in notes if n.get("path") == path), None)
                if canon:
                    rows.append({
                        "path": path,
                        "title": canon.get("title"),
                        "heading": canon.get("heading", ""),
                        "folder": canon.get("folder", ""),
                        "tags": " ".join(canon.get("tags", [])),
                        "chunk_text": canon.get("preview", "")[:1200],
                        "bm25_rank": 5.0,  # neutral; ranking is by intent bonus
                    })
```

The injected row has a **neutral** `bm25_rank=5.0` so it doesn't dominate by
lexical score. The intent bonus (added in the scoring loop) is what makes
it win. This is critical — using a high bm25_rank to "cheat" would
over-inject and break the curated eval.

## Why the boost then carries it to the top

The scoring loop adds `intent_bonus` based on detected intent + path:

```python
if "medical" in intents:
    if path == "Knowledge/Medical Study System.md":
        bonus += 5.5
        labels.append("medical study note")
```

Combined: neutral `bm25_rank=5.0` → baseline score of ~2.5
+ 5.5 medical bonus = **~8.0** vs the next-best daily note at ~5.5.
Canonical wins by 2.5 — clear lead, no over-injection.

## Required companion: smart competing-intent boost

A strong canonical boost can backfire when multiple intents are present. See
`dashboard-recall-ranking.md` and the SKILL.md pitfalls for the pattern:

```python
has_strong_competing = (
    bool(intents & {"decision", "fix", "preference"}) and has_intent_prefix
) or (
    "fix" in intents and any(p in query_low for p in ("what was the fix", ...))
) or (
    "decision" in intents and any(p in query_low for p in ("what did we decide", ...))
)
boost = 3.0 if has_strong_competing else 5.5
```

Without this, a query like "what did we decide about the dashboard redesign"
would route to `Hermes Operations` (ops boost 5.5) instead of `decisions`
(decision boost 3.8). Always pair canonical injection with competing-intent
backoff.

## Don't over-inject

The injection is per-intent, not per-query. If you inject **every** canonical
on every query, you flood the candidate set with non-matching notes and
break the curated eval.

Rule of thumb: only inject canonicals for the **specific** intent that
detected. If a note is meta-architecture (e.g. "Memory System Architecture"),
let it be retrieved via content match — don't add it to
`RECALL_CANONICAL_NOTES`.

## Verification

After adding a canonical to `RECALL_CANONICAL_NOTES`:

1. Run a stress test query that **should** hit it (e.g. "stroke" → Medical Study System).
2. Run a stress test query that **shouldn't** hit it (e.g. "davidson chapter 17" → daily note, not necessarily Medical Study System).
3. Run the curated eval to confirm no regression.

If the new canonical wins queries where it shouldn't, it is over-injecting.
Remove it or tighten the intent match.

## Related references

- `recall-tuning-pitfalls-2026-06.md` — the original FTS5 result-assignment fix
- `recall-stress-testing-2026-06.md` — how to detect when canonicals are missing
- SKILL.md pitfall #20 — "Do not over-inject canonicals"
- SKILL.md pitfall #19 — "Do not blast a strong canonical boost without a competing-intent backoff"
