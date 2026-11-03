# Canonical Note Strengthening — 2026-06-17 Workflow

This reference documents the end-to-end workflow for making the Obsidian vault
stronger and more independent by adding new domain canonicals and tuning the
recall engine to surface them. Use this when the user says "improve Obsidian
memory" or "make this topic land at top-1 of recall."

## Step 1 — Find the gap

The vault has 6 established canonicals (Hermes Operations, Medical Study
System, decisions, issues-fixes-log, AGENT, context). Topics the user asks
about 100+ times per real-session-mining pass that have **zero** canonical
coverage are the gaps. Mining recipe:

```python
import sqlite3, re
from collections import Counter

con = sqlite3.connect("/root/.hermes/state.db")
con.row_factory = sqlite3.Row
rows = con.execute("""
    SELECT content FROM messages
    WHERE role='user' AND length(content) > 20
""").fetchall()

# Real product/topic terms
real_terms = {
    "Codex", "Mnemosyne", "Hermes", "Davidson", "Notion", "Termix",
    "Obsidian", "Telegram", "Discord", "WordPress",
    "FCPS", "MRCP", "Nephrology", "MOC", "MCQ", "SBA",
    "SeaDash", "SeaXen", "OpenRouter", "Claude", "GPT", "Gemini",
    "MCP", "BWS", "Bitwarden", "Watchdog", "Backup", "DR",
}

candidates = Counter()
for r in rows:
    low = r['content'].lower()
    for t in real_terms:
        if t.lower() in low:
            candidates[t] += 1

# Print top 30
for t, n in candidates.most_common(30):
    print(f"  {n:5d}  {t}")
```

The 2026-06-17 pass surfaced these gaps (asked 100+ times, 0 canonical hits):

| Term | Asked | Existing canonicals mentioning it |
|---|---|---|
| DR / disaster recovery | 618× | 1 (Hermes Operations) |
| Compact | 278× | 0 |
| Davidson | 214× | 0 |
| MOC / MCQ / SBA | 175-179× each | 0 |
| GPT | 178× | 0 |
| Codex | 203× | 1 (Hermes Operations) |
| Discord | 145× | 1 |
| OpenRouter | 117× | 1 |
| Telegram | 73× | 1 |
| Mnemosyne | 109× | 0 |
| Cardiology / Nephrology / Stroke | 65-82× each | 0 |
| WordPress | 28× | 0 |
| Notion | 51× | 0 |
| AI providers (Claude, Gemini, Mistral) | 20-22× each | 0 |
| BWS / Bitwarden | 22-78× | 0 |
| Watchdog | 13× | 0 |

Each row above is a candidate for a new canonical. The 2026-06-17 pass added
three: **AI Providers & Models** (consolidated providers row), **Davidson 24e
Study Workflow** (consolidated the MOC/MCQ/SBA/Davidson cluster), and
**Backup & Disaster Recovery** (consolidated the DR/backup cluster).

## Step 2 — Write the canonical

Put the new canonical under the right folder:

- Domain knowledge → `Knowledge/<Topic>.md`
- Project state → `Work/<project>.md`
- System state → `System/Assistant/<thing>.md`

Required structure for the recall engine to find it via FTS5 and title-match:

```markdown
# <Exact Title>

<one-paragraph TL;DR so the title and first heading match the topic tokens>

## <Section 1 — must include the topic tokens in section headers>
- ...

## <Section 2>
- ...

## Cross-references
- [[related note 1]] — short description
- [[related note 2]] — short description
```

**Wikilink format:** use simple titles (`[[context]]`, `[[decisions]]`,
`[[issues-fixes-log]]`), not path-prefixed (`[[System/Assistant/context]]`).
The dashboard resolves links by note title/stem; path-prefixed links resolve
to nothing and become broken links that drop `link_health` below 100.

**Title case matters.** The recall engine uses exact-title match (`title_match`
boost) AND `RECALL_CANONICAL_NOTES` keys must match the note's actual title
field. If the file is `Knowledge/AI Providers & Models.md` and the title is
`# AI Providers & Models`, the `RECALL_CANONICAL_NOTES["AI Providers & Models"]`
key matches.

## Step 3 — Register in `RECALL_CANONICAL_NOTES`

In `obsidian_dashboard.py` (~line 278):

```python
RECALL_CANONICAL_NOTES = {
    "Hermes Operations": ("ops", "setup"),
    # ...
    "AI Providers & Models": ("ops", "setup", "model"),
    "Davidson 24e Study Workflow": ("medical", "study", "davidson"),
    "Backup & Disaster Recovery": ("ops", "backup", "dr", "restore"),
}
```

The first item in the tuple is the strongest signal; subsequent items are
secondary intents that also route here.

## Step 4 — Add intent bucket

If the canonical needs a new intent keyword set (e.g. `model`, `backup`),
add it to `RECALL_INTENT_PHRASES` (~line 225):

```python
RECALL_INTENT_PHRASES = {
    # ...
    "model": (
        "model", "provider", "providers", "which model", "what model",
        "use model", "switch model", "model switch", "model fallback",
        "rate limit", "free tier", "free model", "api key", "model key",
    ),
    "backup": (
        "backup", "restore", "disaster recovery", "disaster", "dr",
        "archive", "snapshot", "rsync", "encrypt", "encrypted",
    ),
}
```

## Step 5 — Add intent-aware boost in `recall_intent_signal()`

Add a dedicated boost block at the right place (after the existing `medical`
and `ops` blocks, ~line 798):

```python
# New canonicals (2026-06-17) — boost when the query matches their domain.
# fix_intent_strong and study_intent_strong are defined at the top of this
# function. When the query has explicit fix intent, suppress the content
# boosts so issues-fixes-log wins.
if "model" in intents and path == "Knowledge/AI Providers & Models.md":
    bonus += 5.5
    labels.append("providers canonical")
elif not fix_intent_strong and path == "Knowledge/AI Providers & Models.md" and any(
    term in haystack for term in ("openrouter", "gpt", "claude", "gemini", "mistral", "codex", "model", "provider", "api key", "fallback")
):
    bonus += 4.5
    labels.append("providers content")
```

The pattern: **5.5 boost when the query explicitly triggered the canonical's
intent bucket**; **4.5 fallback when the query lexically matches the canonical
content** (with cross-intent guards like `fix_intent_strong` to suppress when
a more-specific canonical should win).

## Step 6 — Cross-block intent guards (CRITICAL)

When two canonicals compete for the same query space, define a cross-block
guard variable at the **top** of `recall_intent_signal()` so multiple boost
blocks can reference it. The 2026-06-17 pass added two:

```python
# Cross-block guard for fix intent. When the query is clearly about a
# specific fix ("what was the X fix", "the bug fix", etc.), competing
# canonicals (Hermes Operations, AI Providers, Davidson) should back
# off so issues-fixes-log can win.
fix_intent_strong = any(
    p in query_low for p in (
        "what was the fix", "what is the fix", "fix for",
        "fix to", "how was", "how did we fix", "bug fix",
        "the fix", "the last", "plugin fix", "api fix",
        "notion fix", "the bug", "this bug", "this fix",
    )
)
# Similar guard: medical-content boost shouldn't fire when the
# query has explicit study intent.
study_intent_strong = any(
    p in query_low for p in (
        "how to write", "study workflow", "topic file",
        "topic files", "davidson", "chapter build", "moc",
        "viva", "mcq", "sba",
    )
)
```

Then use them in the boost blocks:

```python
if path == "Knowledge/Hermes Operations.md":
    has_strong_competing = (
        # ... existing checks ...
    ) or fix_intent_strong
    boost = 2.0 if has_strong_competing else 5.5
    bonus += boost

# Davidson boost
elif path == "Knowledge/Davidson 24e Study Workflow.md":
    if not fix_intent_strong:
        bonus += 4.5
    else:
        bonus += 1.0  # baseline, don't compete with issues-fixes-log
```

**Critical pitfall:** if you put `fix_intent_strong = ...` inside the `medical`
block at the bottom of the function, and the `ops` block at the top tries to
read it, Python raises `UnboundLocalError: cannot access local variable
'fix_intent_strong' where it is not associated with a value`. The variable
name becomes local to the entire function the moment ANY assignment to it
exists, even if the assignment is in a branch that doesn't run. Always
define cross-block variables at the top of the function.

## Step 7 — Verify, classify misses, iterate

Run a real-query stress test (not the curated eval alone). Pull 20-30
substantive user messages from `state.db`, hand-pick the ones that should
hit each new canonical, run them through `/api/recall?query=...`, and check
the top-1:

```python
import json, urllib.parse, urllib.request

expected = {
    "what was the FTS5 bug fix": "issues-fixes-log",
    "OpenRouter key fallback": "AI Providers & Models",
    "study Davidson chapter 29": "Davidson 24e Study Workflow",
    "backup schedule for hermes": "Backup & Disaster Recovery",
    # ... 20+ more ...
}

correct = 0
for q, exp in expected.items():
    url = "http://localhost:6065/api/recall?query=" + urllib.parse.quote(q) + "&limit=3"
    with urllib.request.urlopen(url) as r:
        d = json.load(r)
    top = d['results'][0]['title'] if d['results'] else ""
    if exp.lower() in top.lower() or top.lower() in exp.lower():
        correct += 1
    else:
        print(f"  ✗ '{q}' expected={exp} got={top}")

print(f"Correct: {correct}/{len(expected)}")
```

Classify each miss as one of:

- **(a) real bug** — wrong canonical won, fix the boost (add to guard patterns,
  bump boost value, etc.)
- **(b) content gap** — the right canonical exists but doesn't have the answer
  yet. Add the content to the canonical.
- **(c) acceptable disagreement** — both are defensible. Leave alone.

The 2026-06-17 pass went 13/24 → 15/24 with these changes. The remaining 9
misses were split: 4 acceptable disagreements, 5 content gaps. Trying to
force 24/24 would over-tune the boost and break previously-correct cases.

## Step 8 — Verify nothing else broke

After the boost changes, run the curated eval:

```bash
curl -s "http://localhost:6065/api/recall-eval" | python3 -c "
import sys, json
d = json.load(sys.stdin)
print(f\"case_count={d['summary']['case_count']} hit_at_k={d['summary']['hit_at_k']} mrr={d['summary']['mrr']}\")
"
```

And check the new canonicals don't make any old test case worse. If the
curated MRR drops after the real-query improvements, the boost is too
aggressive — lower the canonical's specific-intent boost from 5.5 → 4.5
and re-test.

## Step 9 — Document the change

Update the SKILL.md **Recall architecture** section with the new canonical's
filter parameters and the new `source_kind` values. Add a one-line pointer
to this reference doc.

## What NOT to do

- Don't add a new canonical for a topic that already has 80%+ coverage in an
  existing one. Consolidate into the existing canonical first.
- Don't add a boost that fires for the wrong query class (e.g. Davidson boost
  on generic "FCPS" queries — the umbrella Medical Study System should win).
- Don't skip the cross-block guard when adding a new boost that competes
  with an existing one. The UnboundLocalError + wrong-canonical-wins trap
  will surface.
- Don't declare done on curated-eval alone. The 2026-06-17 pass started at
  100/100 curated and 13/24 real-queries; only the real-query test
  surfaced the boost problems.
