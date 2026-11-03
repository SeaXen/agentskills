# Recall Cross-Block Intent Guards + Pattern-List Iteration (2026-06-17)

Companion to SKILL.md Pitfall 28 (cross-block intent guards) and
Pitfall 32 (effective_intents override). Captures the two patterns
that emerged from the 2026-06-17 recall-engine stress test when the
guard variables were correctly defined but the boost blocks did not
fire as expected.

## Pattern A: `effective_intents` override at the call site

**When `detect_recall_intents(query)` is too narrow to catch the
pattern your cross-block guard matches.**

Setup:
- `detect_recall_intents()` looks at `RECALL_INTENT_PHRASES` and
  matches short substrings like `"fix"`, `"bug"`, `"gotcha"`.
- The cross-block guard at the top of `recall_intent_signal()`
  matches a BROADER pattern list, e.g.
  `fix_intent_strong = any(p in query_low for p in ("what was the fix", "gotcha", "workaround", "the last", "edge case"))`.

Problem: the boost block for `is_aggregate_fix` reads
`if "fix" in intents:`. If `"gotcha"` is in the query but no `"fix"`
token was in `detect_recall_intents`'s phrase list, the boost block
never fires — even though `fix_intent_strong` is True.

**Fix:** build an effective intents set at the call site that
combines the narrow `detect_recall_intents()` output with the broad
guard signals, then pass that into `recall_intent_signal()`:

```python
# in query_hybrid_recall(), right before calling recall_intent_signal:
_q_low_for_fix = (query or "").lower()
_effective_intents = query_intents | (
    {"fix"} if any(
        p in _q_low_for_fix for p in (
            "what was the fix", "what is the fix", "fix for",
            "fix to", "how was", "how did we fix", "bug fix",
            "the fix", "the last", "plugin fix", "api fix",
            "notion fix", "the bug", "this bug", "this fix",
            "gotcha", "workaround", "edge case",
        )
    ) else set()
)
intent_bonus, intent_labels = recall_intent_signal(
    note, row, chunk_text, _effective_intents, query
)
```

Then in `recall_intent_signal()`, the boost blocks (`if "fix" in intents:`)
will fire correctly because the effective set includes `"fix"`.

**Why not just extend `detect_recall_intents` directly?** Because the
guard pattern list is intentionally different from the intent-phrase
list. The intent phrases are what users say to indicate they want a
"fix"-type recall; the guard patterns are the additional phrases that
should *redirect* a competing canonical even when the user didn't use
a fix-intent phrase. Combining them into one set conflates two
different decisions. Keep them separate, inject at the call site.

## Pattern B: Study-workflow tie-breaker between umbrella and domain canonicals

**When two canonicals with overlapping intent both have strong boosts,
and the user wants the more specific one.**

Setup:
- `Medical Study System.md` is the umbrella canonical (`+5.5` on
  `medical` intent).
- `Davidson 24e Study Workflow.md` is the domain-specific canonical
  (`+4.5` on `medical` intent).
- For "FCPS/MRCP exam" queries, the umbrella should win.
- For "how to write a topic file" / "MCQ SBA format" queries, the
  domain-specific should win.

Naive boost (`Davidson +4.5`, `Medical Study System +5.5`) makes the
umbrella win every time. Wrong for workflow queries.

**Fix:** in the medical-intent boost block, gate `Davidson` higher
than the umbrella when the query contains a study-workflow marker:

```python
if "medical" in intents:
    study_marker_in_query = any(
        m in query_low for m in (
            "topic file", "topic files", "study workflow", "study format",
            "mcq", "sba", "viva", "chapter build", "disease flashcard",
            "disease flashcards", "case summary", "case summaries",
            "study plan",
        )
    )
    if path == "Knowledge/Davidson 24e Study Workflow.md" and study_marker_in_query:
        if not fix_intent_strong:
            bonus += 6.0     # > umbrella 5.5
            labels.append("davidson workflow")
    elif path == "Knowledge/Medical Study System.md":
        bonus += 5.5
        labels.append("medical study note")
    elif path == "Knowledge/Davidson 24e Study Workflow.md":
        if not fix_intent_strong:
            bonus += 4.5     # default when no study marker
```

**Why this works:**
- Umbrella (`Medical Study System`) is still the first hit for
  general medical queries (no study marker in query → falls through
  to the `elif` branch, `+5.5`).
- Davidson wins specifically when the query is about the workflow
  (`+6.0` vs `+5.5`).
- The `if not fix_intent_strong` guard prevents Davidson from
  stealing fix queries (where `issues-fixes-log` should still win).

## Pattern-List Iteration Loop (the meta-pattern)

Both Pattern A and Pattern B depend on hard-coded pattern lists.
Those lists go stale as the user asks new phrasings. The 2026-06-17
audit extended `fix_intent_strong` from 8 to 15 patterns in three
iterations:

| Iteration | Added patterns | Triggered by query |
|---|---|---|
| 1 (initial) | "what was the fix", "fix for", "the bug", "this bug" | "what was the FTS5 row-assign bug fix" |
| 2 | "the fix", "the last", "plugin fix", "api fix", "notion fix", "this fix" | "what was the last plugin fix" |
| 3 | "gotcha", "workaround", "edge case" | "Notion API gotcha for sub-pages" |

**The loop:**
1. Run a hand-picked stress test of 20+ real user queries.
2. For each top-1 miss, classify: (a) real bug — wrong canonical wins,
   (b) content gap — right canonical doesn't have the answer yet,
   (c) acceptable disagreement — both are defensible.
3. For (a): look at the failing query. Is the broad pattern list
   matching it? If not, add the new phrasing to the pattern list.
   If yes, the boost values need tuning instead.
4. Re-run the stress test. Confirm the failing case now passes AND
   no other case regressed.
5. Stop iterating when real-bug misses drop below ~10% and adding
   more patterns starts producing false positives (umbrella queries
   losing to domain queries because the marker was too broad).

**Stop condition:** adding patterns to a list should make it
broader, not more aggressive. If extending the list by adding
"viva" starts making "viva preparation" outrank the umbrella
medical study note for unrelated queries, the marker is too
aggressive and should be scoped tighter.

## Cross-references

- SKILL.md Pitfall 28: cross-block guard variables
- SKILL.md Pitfall 30a: restart verification with new-code-path queries
- SKILL.md Pitfall 32: `effective_intents` override at the call site
- `references/recall-stress-testing-2026-06.md`: hand-picked stress
  test methodology and acceptance bar
