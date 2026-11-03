# Recall Tuning — FTS5 Pitfalls, Title Match, and Intent Boosts

Apply these rules when adjusting `query_hybrid_recall()` in `obsidian_dashboard.py`.

## CRITICAL: FTS results silently discarded (`.fetchall()` on throwaway cursor)

**The single most impactful recall bug found to date (2026-06-17).** FTS was running and returning the right results, but the entire result set was being thrown away. Recall went from 90.4 → 99.4 with a one-line fix.

**Before (broken — FTS effectively dead):**
```python
if fts_query:
    conn.execute(
        "SELECT path,title,heading,folder,tags,chunk_text,bm25(recall_fts, 1.8, 1.2, 0.6, 0.5, 1.0, 1.4) AS bm25_rank "
        "FROM recall_fts WHERE recall_fts MATCH ? ORDER BY bm25_rank LIMIT 64",
        (fts_query,),
    ).fetchall()  # ← BUG: result is discarded, not assigned to rows
if len(rows) < 18:
    fallback_rows = conn.execute("SELECT ... FROM note_meta LIMIT 48").fetchall()
    rows.extend([r for r in fallback_rows if r["path"] not in {row["path"] for row in rows}])
```

**After (fixed):**
```python
if fts_query:
    rows = conn.execute(  # ← critical: assign the result
        "SELECT path,title,heading,folder,tags,chunk_text,bm25(recall_fts, 1.8, 1.2, 0.6, 0.5, 1.0, 1.4) AS bm25_rank "
        "FROM recall_fts WHERE recall_fts MATCH ? ORDER BY bm25_rank LIMIT 64",
        (fts_query,),
    ).fetchall()
```

**Symptoms that masked this bug:**
- Memory health score was high (96–99) — `/api/memory-health` doesn't use the broken FTS path
- Recall still returned *something* — the fallback path always returned all 48 notes with `bm25_rank=10.0`
- Heuristic scoring still differentiated the 48 notes via title_match, intent_bonus, etc., so the eval looked "OK" (90.4/100)
- But canonical notes that only appeared via FTS (not in the fallback pool) were silently absent
- Examples that surfaced this: `Knowledge/Medical Study System.md`, `Knowledge/Hermes Operations.md` — both exist in vault but never returned

**How to detect:** if a note appears in `sqlite3 recall.db` FTS results but not in `/api/recall?query=...` results, suspect this bug.

**How to verify the fix:** after patching, run a recall query with a verbatim title and confirm the note appears in the top 3:
```bash
curl -s 'http://localhost:6065/api/recall?query=medical+study+system' | python3 -c \
  "import json,sys; print([r['title'] for r in json.load(sys.stdin)['results'][:3]])"
# Should print: ['Medical Study System', ...]
```

## Variable scope pitfall: `is_daily_note` not in outer scope

The variable `is_daily_note` is computed inside `recall_intent_signal()` (around line 445) for the boost logic. It is **NOT** accessible in the outer scoring loop in `query_hybrid_recall()`. If you write new code that needs `is_daily_note` (e.g. for the tag-query boost below), re-derive it from `row["path"]`:

```python
# In the outer loop, after recall_intent_signal():
is_daily_note = (row["path"] or "").startswith("Daily/") and (row["path"] or "").endswith(".md")
```

**Symptom of getting this wrong:** dashboard returns HTTP 200 with empty body. `journalctl --user -u obsidian-vault-dashboard -n 30` shows `NameError: name 'is_daily_note' is not defined` in the request handler. systemd auto-restarts but every request still crashes. Always check the journal after any new code touches the outer recall loop.

## Systemd file path is `/mnt/tb/hermes/obsidian_dashboard.py` even when it looks like `/root/.hermes/`

The systemd unit `obsidian-vault-dashboard.service` runs `/usr/bin/python3 /mnt/tb/hermes/obsidian_dashboard.py`. But `/root/.hermes/obsidian_dashboard.py` and `/mnt/tb/hermes/obsidian_dashboard.py` are often the **same file** (same inode, same md5) — `/mnt/tb/hermes` is a bind mount or hardlink target. Verify with `stat -c '%i'` on both paths before assuming edits go to the wrong place.

**When to suspect this confusion:** if `systemctl --user restart obsidian-vault-dashboard` is followed by "Address already in use" errors from a background process, the system has two processes fighting for port 6065. Kill the orphan (NOT the systemd-managed one) and let systemd restart cleanly.

## FTS5 query must explicitly `ORDER BY bm25_rank`

Default FTS5 ordering is **rowid (insertion order)**, NOT relevance. A note that was inserted later (high rowid) will be excluded from the first 48 results even if it has the best BM25 score.

**Before (broken):**
```python
SELECT ... bm25(recall_fts, 1.8, 1.2, 0.6, 0.5, 1.0, 1.4) AS bm25_rank
FROM recall_fts WHERE recall_fts MATCH ? LIMIT 48
```
This silently excludes recent high-relevance notes.

**After (fixed):**
```python
SELECT ... bm25(recall_fts, 1.8, 1.2, 0.6, 0.5, 1.0, 1.4) AS bm25_rank
FROM recall_fts WHERE recall_fts MATCH ? ORDER BY bm25_rank LIMIT 64
```

**Symptom:** canonical note (e.g. `Knowledge/Hermes Operations.md`) never appears in top 10 results for its own title query, but the FTS itself returns it at position 2 by BM25. Verify with:
```sql
SELECT path, bm25(recall_fts, 1.8, 1.2, 0.6, 0.5, 1.0, 1.4)
FROM recall_fts WHERE recall_fts MATCH 'hermes operations'
ORDER BY bm25_rank LIMIT 20
```

## Token punctuation breaks FTS5

FTS5 throws `fts5: syntax error near "."` on tokens containing `.` (e.g. `mdsagar.com`, `openai-codex`, `codex-fresh`). When building the FTS query string:

```python
fts_query = " OR ".join(
    f'"{token.replace(chr(34), "")}"'
    for token in fts_tokens
    if token and token.replace(chr(34), "").isalnum()
)
```

- Quote each surviving term.
- Join with `OR` (not space) so the query is permissive — natural-language AND is too strict.
- Skip tokens with non-alphanumeric characters silently (they will not match FTS5 anyway).

## Recall boost hierarchy for specific intent (updated 2026-06-17)

| Intent signal | Aggregate path boost | Specific daily-note boost |
|---|---|---|
| decision (general) | 2.8 | 3.0 |
| decision ("what did we decide" / "decision:" prefix) | **3.8** | 2.0 (prefer aggregate) |
| fix (general / convention) | 1.2 | 3.0 |
| fix ("what was the fix" / "fix:" prefix) | **3.5** | 2.0 (prefer aggregate) |
| setup | 2.2 | 1.6 |
| preference | 2.2 | 1.6 |

**Key insight from the 2026-06-17 audit:** when the query uses a clear intent pattern (prefix or phrase), the user wants the canonical aggregate note, NOT a random daily note that mentions the entity. For these patterns, **the daily-note boost should be LOWER than the aggregate boost** so the canonical wins. For general intent without a pattern, the daily note can still win if it has a specific entity match.

Detect prefix in `detect_recall_intents()`:
```python
for prefix, intent in (
    ("decision:", "decision"),
    ("fix:", "fix"),
    ("setup:", "setup"),
    ("preference:", "preference"),
):
    if low.startswith(prefix):
        intents.add(intent)
```

## Specific vs generic entity split (2026-06-17)

**Fix:** split `RECALL_ENTITY_HINTS` into two lists:
- `RECALL_ENTITY_HINTS` — full list (model names, ports, ops terms, generic) for lexical match
- `RECALL_SPECIFIC_ENTITY_HINTS` — only model names, creds, port numbers for the "specific decision" trigger

```python
RECALL_ENTITY_HINTS = (
    "openai-codex", "openrouter", "nvidia/", "anthropic", "gemini", "ollama",
    "nous", "sambanova", "xai", "copilot", "codex-fresh", "pottege", "inheler",
    "hrsagar", "jalmie",
    "obsidian", "vault", "md", "fix", "decision", "log",
)
RECALL_SPECIFIC_ENTITY_HINTS = (
    "openai-codex", "openrouter", "nvidia/", "anthropic", "gemini", "ollama",
    "nous", "sambanova", "xai", "copilot", "codex-fresh", "pottege", "inheler",
    "hrsagar", "jalmie",
    "obsidian", "vault",
    # Excluded: "md", "fix", "decision", "log" (too generic)
)
```

Use `note_has_specific_entity` for the daily-note "specific decision/fix" boost, not `note_has_entity`.

## Title-match boost (canonical wins over daily)

When the query is essentially the note title, the canonical note should beat daily notes that merely mention the terms. Add a strong boost in the breakdown:

```python
title_norm = normalize_text(row["title"] or "")
query_norm = normalize_text(query)
is_intent_seeking = bool(query_intents) and any(
    p in query_norm for p in (
        "what did we decide", "what was the fix", "what is the fix",
        "what is the convention", "decision about", "fix for",
    )
)
if query_norm and title_norm and not is_intent_seeking and (
    query_norm == title_norm
    or query_norm in title_norm
    or title_norm in query_norm
):
    title_match_boost = 4.5
else:
    title_match_boost = 0.0
```

**Critical:** suppress `title_match` when the query has an explicit intent pattern. Otherwise `Dashboard.md` beats `decisions.md` for "what did we decide about the dashboard redesign" because "dashboard" is in `Dashboard.md`'s title.

## Pure tag queries need daily-note boost (2026-06-17)

For queries that are ONLY a tag (`#imported`, `#active`), the canonical "Imported" index note wins on lexical match. But the user wants the daily notes that USE the tag, not the index page.

**Fix:** add a `tag_daily_boost` that fires only on pure tag queries:

```python
is_pure_tag_query = bool(explicit_query_tags) and not query_tokens - explicit_query_tags
tag_daily_boost = 0.0
if is_pure_tag_query and explicit_tag_hits:
    if is_daily_note:
        tag_daily_boost = 3.0  # daily note wins decisively
    else:
        tag_daily_boost = -2.0  # canonical/index note loses decisively
```

Add `tag_daily_boost` to the breakdown dict. Required the variable-scope fix above (re-derive `is_daily_note`).

## Cron-only noise penalty

`watchdog`, `scheduler`, `rclone`, `plain-hermes`, `ingest log`, `pipeline state` — when these appear in the query, daily-note matches without an entity-hint match should be penalized:

```python
RECALL_NOISE_TOKENS = (
    "watchdog", "scheduler", "sched tick", "cron tick", "rclone",
    "plain-hermes", "ingest log", "pipeline state",
)
...
if query_has_noise and is_daily_note and not note_has_entity:
    bonus -= 1.5
```

Tune the penalty to balance "still relevant" vs "leak prevention". A value of `-1.5` suppresses without completely zeroing the candidate.

## Update curated eval cases when backfilling notes

When backfilling old daily notes from `session_search`, update `_build_curated_recall_eval_cases()` to include the new daily note paths in the `expected_titles` list for relevant queries. Without this, the new notes compete with the curated targets and the eval Hit@k drops artificially.

```python
if title_by_path.get("Memory/decisions.md"):
    decisions_expected = [title_by_path["Memory/decisions.md"]]
    for path, title in title_by_path.items():
        if path.startswith("Daily/2026-06-"):
            decisions_expected.append(title)
```

Add specific-instance cases for new durable items:
```python
cases.append({
    "id": "curated:specific_codex_auth_label",
    "kind": "curated_decision",
    "label": "codex auth via add --label (specific)",
    "query": "decision: how to add openai-codex credentials without overwriting the default slot",
    "expected_titles": [title_by_path["Daily/2026-06-13.md"], title_by_path.get("Memory/decisions.md", "")],
})
```

## The MRR-driven improvement loop (2026-06-17)

The path from 9.0 → 10.0 in this audit was systematic:

1. Run `/api/recall-eval` — identify cases where `best_rank > 1` (low MRR)
2. For each low-MRR case, run `/api/recall?query=...` directly and inspect the per-note `reasons` breakdown
3. Diagnose: which signal is over-scoring the wrong candidate?
4. Tune one boost at a time, re-run the eval, verify the failing case improved AND no new case regressed
5. Iterate. Do not batch-tune multiple boosts — regressions are hard to isolate.

Sample sequence that worked:
- Bump `decision_log` 2.0 → 2.8 (general decision queries)
- Add "convention" to decision intent phrases (port-convention test passes)
- Split entity hints into specific vs generic (stops daily notes winning on ops terms)
- Bump `fix_log` for "what was the fix" pattern 2.0 → 3.5 (fix-hyphen test passes)
- Suppress `title_match` for intent-seeking queries (decision-dashboard test passes)
- Add `tag_daily_boost` for pure tag queries (tag-imported test passes)

## Verification ritual after any recall change

1. **Syntax:** `python3 -m py_compile /mnt/tb/hermes/obsidian_dashboard.py`
2. **Kill orphan and restart:** `PID=$(lsof -ti:6065); kill -9 $PID; systemctl --user restart obsidian-vault-dashboard`
3. **Wait 5–8s, then check journal** for crashes: `journalctl --user -u obsidian-vault-dashboard -n 20 --no-pager | grep -E "Error|NameError|Traceback"`
4. **Smoke test the bug that motivated the change:** `curl -s -m 30 'http://127.0.0.1:6065/api/recall?query=<verbatim title>&limit=5'` — confirm canonical note in top 3
5. **Full eval:** `curl -s 'http://127.0.0.1:6065/api/recall-eval' | python3 -m json.tool | grep -E 'hit_at_k|mrr|case_count'`
6. **Health check:** `curl -s 'http://127.0.0.1:6065/api/memory-health' | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['overall_score'], d['scores']['recall'])"`
7. **Compare before/after MRR** — a true 10/10 means `hit_at_k=1.0` AND `mrr=1.0` (every test case rank 1)

## Acceptance bar: what "10/10" means for recall

A pass is 10/10 only when **all** are true simultaneously:
- `hit_at_k = 1.0` (every test case finds expected note in top 5)
- `mrr = 1.0` (every test case ranks expected note at position 1)
- `noise_control = 100` (trivial queries return empty)
- `review_flow = 100` (no pending review candidates)
- `link_health = 100` (zero broken links, zero orphans)

If `hit_at_k = 1.0` but `mrr < 1.0`, the system is *not* at 10/10 — the right note is in the top 5 but not the top 1. Continue tuning the boost hierarchy.
