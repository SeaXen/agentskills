# Mnemosyne ↔ Obsidian Vault Cross-link (2026-06)

Concrete pattern for bridging the two memory layers that the agent
and vault operate on:

- **Mnemosyne** (hot memory): `~/.hermes/mnemosyne/data/mnemosyne.db`,
  tables `working_memory`, `facts`, `triples`. Fast FTS5 access, but
  lives outside the Obsidian vault and is invisible to `/api/recall`.
- **Obsidian vault** (warm memory): `/mnt/tb/hermes/obsedianvault`,
  served by `obsidian_dashboard.py` on port `6065`. Visible to recall
  but does not auto-receive anything Mnemosyne knows.

The cross-link is three pieces: a mirror script, a unified recall
endpoint, and a guard against the mirror poisoning the review queue.

## 1. Mirror script — `~/.hermes/scripts/mnemosyne_to_vault.py`

Purpose: project durable Mnemosyne items into two vault notes on a
schedule, so the same facts become searchable from `/api/recall`
without manual copying.

Schedule: every 6 hours via a `no_agent: true` cron
(`hermes cron create 0 */6 * * * --script mnemosyne_to_vault.py --no-agent`).

Behaviour:

- reads `working_memory` with `source != 'conversation'` and
  `importance >= 0.6` (filters chat noise; conversational rows are
  97% of working memory and drown signal)
- reads `facts` with `confidence >= 0.7`
- reads top 120 `triples` by confidence
- writes two idempotent files:
  - `Knowledge/Mnemosyne Mirror.md` — high-importance working
    memory + stable facts + top 60 triples + cross-references
  - `Knowledge/Mnemosyne Triples.md` — full triple list
- **idempotent:** if the rendered content is byte-identical to the
  existing file, no write. This keeps the mtime stable so the
  mirror notes do not pollute the dashboard's "recently changed"
  list every 6 hours.

Cross-reference format in the mirror notes must use the **dashboard's
wikilink resolution** — it resolves by note title/stem, not path.

```markdown
- [[Memory System Architecture]]   # works
- [[Hermes Operations]]            # works
- [[context]]                      # works (title of System/Assistant/context.md)
- [[preferences]]                  # works
- [[System/Assistant/context]]     # BROKEN — path not in title resolver
```

If you write `[[System/Assistant/context]]` the dashboard flags a
broken link in `/api/memory-health` and drops `link_health` below
100. Always check the actual title in
`curl http://localhost:6065/api/graph | jq '.notes[].title'`.

## 2. Unified recall endpoint — `/api/recall-unified`

The plugin should hit `/api/recall-unified` first, then fall back to
`/api/recall` if the unified endpoint is unreachable.

Shape of the endpoint:

- runs `query_hybrid_recall()` for the vault side (unchanged)
- runs `query_mnemosyne_recall()` for hot memory side
- tags every result with `"source": "obsidian"` or `"source": "mnemosyne"`
- sorts merged list by score
- returns `vault_count` and `mnemosyne_count` plus results

Mnemosyne query construction:

- tokenize with `re.findall(r"[A-Za-z0-9_]+", query)`
- FTS5 query string: `" OR ".join(f'"{t}"' for t in tokens[:8])`
- score = `max(0, 10 - bm25_rank) + importance_or_confidence * weight`
- **filter** to `source != 'conversation'` AND `importance >= 0.6`
  BEFORE FTS5 search. Without this, the working-memory table
  (97% chat noise) returns garbage fact strings like
  `"This is clean"` and `"Nephrology is those"`. The user
  will see this nonsense at the top of recall and lose trust
  in the whole feature.

## 3. FTS5 column-aliasing pitfall (this WILL bite you)

When you join a FTS5 virtual table to the source table, FTS5
**re-exposes the indexed columns by their original names** in the
projection. If the source table also has those columns (which it
must — that's where the values came from), you get
`ambiguous column name: id` and the query fails with no rows
returned. The endpoint then returns empty results and the recall
appears to "just not work" — silent failure.

Mnemosyne FTS schema (this is the actual schema you will hit):

```sql
CREATE VIRTUAL TABLE fts_working USING fts5(
    id UNINDEXED,       -- exposed as fts_working.id
    content             -- exposed as fts_working.content
);
-- working_memory also has columns named `id` and `content`.
```

Fix: **alias every projected column** on the source-table side:

```sql
SELECT working_memory.id AS wm_id,
       working_memory.content AS wm_content,
       working_memory.importance AS wm_importance,
       working_memory.source AS wm_source,
       working_memory.created_at AS wm_created_at,
       bm25(fts_working) AS rank_score
FROM fts_working
JOIN working_memory ON fts_working.rowid = working_memory.id
WHERE fts_working MATCH ?
  AND working_memory.source != 'conversation'
  AND working_memory.importance >= ?
ORDER BY rank_score LIMIT ?
```

Same shape for `fts_facts` / `facts` — alias as `f_id`, `f_subject`,
`f_predicate`, etc.

General rule for any future cross-table FTS join: if a column is in
both the FTS projection and the source table, alias the source side.

## 4. The review-queue poisoning trap

The Mnemosyne mirror notes are projections, not new memory. But the
dashboard's `generate_memory_review_candidates()` scans every
`*.md` file for high-signal keywords and emits candidates to
`/api/memory-candidates`. As soon as the mirror script lands its
first note, you get ~12–15 false candidates per run, e.g.:

- `[preference] conf=0.76` — `Dr. Sagar — prefers — Markdown (.md)`
- `[fix] conf=0.82` — "If a fact here is wrong or stale, the source
  of truth is Mnemosyne's..."

`review_flow` drops to 94 and the user has to reject all of them.
This is a self-referential feedback loop: mirror script → candidates
→ manual reject → next run of the script → new candidates.

**Fix:** add the mirror notes to `MEMORY_REVIEW_SKIP_PATHS` in
`obsidian_dashboard.py`:

```python
MEMORY_REVIEW_SKIP_PATHS = {
    "Dashboard.md",
    "System/Assistant/context.md",
    # ...existing skips...
    "Knowledge/Mnemosyne Mirror.md",
    "Knowledge/Mnemosyne Triples.md",
    "Knowledge/Memory System Architecture.md",
}
```

Also add any other **meta-architecture or projection notes** you
create later (cross-link documentation, agent-facing schema notes,
seed-script outputs). They will get the same treatment.

## 5. Plugin wiring

`obsidian-auto-recall/__init__.py` should:

1. Use `submit_recall_feedback(vote, query, result)` after every
   turn where `/api/recall` or `/api/recall-unified` surfaced
   results. Vote `up` for the result that contributed to the
   answer, `down` for results that were off-topic or contradicted
   by a higher-ranked result. Submission is best-effort and
   silently no-ops on network failure.
2. Hit `/api/recall-unified` first, fall back to `/api/recall`.
3. Render Mnemosyne-sourced results with a `[mnemosyne]` tag in
   the context block so the agent can tell which layer the hit
   came from.

The unified recall returns `mode: "unified"` (or `"vault"` after
fallback) so a future watchdog can detect when Mnemosyne is down
and the agent is silently running on vault-only recall.

## Verification recipe

After any change here:

```bash
# 1. Compile-check
python3 -m py_compile /mnt/tb/hermes/obsidian_dashboard.py
python3 -c "import py_compile; py_compile.compile('~/.hermes/plugins/obsidian-auto-recall/__init__.py', doraise=True)"

# 2. Restart dashboard
systemctl --user restart obsidian-vault-dashboard.service
sleep 2

# 3. Mirror script smoke test
python3 ~/.hermes/scripts/mnemosyne_to_vault.py
# Expect: "[mnemosyne-mirror] working=N facts=N triples=N mirror_written=True|False triples_written=True|False"

# 4. Unified recall live
curl -s "http://localhost:6065/api/recall-unified?query=FCPS%20nephrology%20preparation&limit=4&mnemosyne_limit=2" | python3 -m json.tool | head -40
# Expect: vault_count >= 1, mnemosyne_count >= 1, results tagged with source

# 5. Health
curl -s "http://localhost:6065/api/memory-health" | python3 -c "import sys, json; d = json.load(sys.stdin); print(d['overall_score'], d['scores'])"
# Expect: review_flow=100, link_health=100, no broken links, candidates.kept=0 from mirror notes
```
