# Real-Query Stress Test for Obsidian Vault Recall (2026-06-17)

## Why this matters

A curated 26-case recall eval can return `hit_at_k=1.0` and `mrr=1.0` while
real user queries still fail 80% of the time. The eval cases are hand-picked
and tend to match the cases the agent already knows how to handle. The user's
actual questions — drawn from real sessions — surface the gaps.

This reference documents the stress test methodology that took the vault from
"8/35 canonical hits" to "34/35 canonical hits" on real queries in one
session.

## When to run this

- After any recall ranking change to `query_hybrid_recall()`.
- After adding a new canonical note to `RECALL_CANONICAL_NOTES`.
- After expanding `RECALL_INTENT_PHRASES`.
- Before declaring a recall pass "done" to the user.

## The methodology

### 1. Pull real user queries from the Hermes state DB

```bash
sqlite3 /root/.hermes/state.db "
  SELECT content FROM messages
  WHERE role='user' AND length(content) > 25 AND length(content) < 300
  ORDER BY RANDOM() LIMIT 60
"
```

This gives you 60 actual user messages, which is the right size for a
single-session audit. Filter for substantive questions by length.

### 2. Filter to queries that should match vault content

Drop queries that are:
- OAuth callbacks, URLs only, system notes, model-switch notifications
- Pure greetings or one-word acks
- Pure task execution ("run this command")

Keep queries that:
- Ask about past work, decisions, or fixes
- Reference projects (Hermes, vault, mdsagar.com, plugins, models)
- Ask medical / study questions
- Reference specific entities (model names, ports, file names)

A 60-message sample typically yields 25–40 testable queries.

### 3. Run each through `/api/recall`

```python
import json
import urllib.parse
import urllib.request

def recall(query, limit=5):
    params = urllib.parse.urlencode({"query": query, "limit": limit})
    with urllib.request.urlopen(
        f"http://127.0.0.1:6065/api/recall?{params}", timeout=8
    ) as r:
        return json.loads(r.read())

for q in TEST_QUERIES:
    r = recall(q, limit=3)
    top1 = r.get("results", [{}])[0].get("title", "NONE")
    print(f"[{top1:30}] {q[:60]}")
```

### 4. Judge top-1 by canonical-match, not literal-match

The right answer is whichever canonical note would actually help the agent
respond to the query. Pattern:

| Query type | Right top-1 |
|---|---|
| Hermes dashboard / plugin / model config | `Hermes Operations` |
| Decision about a project / convention | `decisions` |
| Technical fix / error / what was the fix | `issues-fixes-log` |
| FCPS / MRCP / medical study / Davidson | `Medical Study System` |
| Personal preferences | `preferences` |
| "How does the system work" | `AGENT` |
| Generic vague query | any canonical OK (don't be strict) |

A query that returns a daily note when a canonical should win is a real
failure. A query that returns the "wrong" canonical is also a failure if a
more specific canonical would be more helpful.

### 5. Track score and identify failure modes

For each failing query, look at:
- Top 5 results and their scores (clustered scores = scoring too flat)
- Reasons listed (intent fit, keyword match, recent note, token overlap)
- Whether the right canonical is in the FTS5 candidate set at all

If the right canonical is not in the candidate set → **canonical injection**
fix (separate reference). If it's in the set but ranked low → **boost
calibration** fix. If it's ranked low because the lexical baseline dominates
→ **intent-specific boost** fix.

## What this surfaces that the curated eval does not

The curated eval tends to use the same wording the agent expects to see
(e.g. "decision: how to add openai-codex credentials"). Real user queries
are messier:

- Mixed languages ("but mine already round robin , still not auto rotate")
- Spelling errors ("kn o", "possble", "enviroment")
- Truncation ("for physiology use Ganong's Review of Medical Physiology...")
- Indirect references ("that thing we did with the dashboard")
- Multiple intents in one query ("fix: openai-codex credentials without overwriting other slots")

Each of these breaks the eval-time heuristics differently. Stress test
catches them.

## Acceptance bar

A recall pass is "done" only when:
- Curated eval: `hit_at_k=1.0` AND `mrr=1.0` (or 0.977 for the structurally
  tag-query case)
- Stress test: ≥30/35 hits a canonical note (≈85%+)
- No new failures introduced vs the previous stress test

## Reference script

See `templates/recall_stress_test.py` for a copy-paste runnable stress test
that targets `http://127.0.0.1:6065` and prints a top-1 summary table.

## Related references

- `recall-tuning-pitfalls-2026-06.md` — the curated-eval fixes
- `canonical-injection-pattern-2026-06.md` — what to do when the right
  canonical is missing from the FTS5 candidate set
- `dashboard-watchdog-pattern-2026-06.md` — catch silent degradation so
  stress-test regressions are detected
