# Mnemosyne triple count not increasing — operator diagnosis

Use when the user asks why SQL `triples` stopped growing while working memory / facts still increase.

## Live shape (verified pattern)

| Store | Typical behavior |
|-------|------------------|
| `working_memory` | Grows every turn via `sync_turn()` |
| SQL `triples` | Grows only via **`mnemosyne_triple_add`** (or bulk curation) |
| `memoria_facts` / `memoria_kg` | Regex/LLM side paths on `remember()` — separate from dashboard graph |
| `facts` / `annotations` | `extract=true` and auto-annotation paths — **not** the SQL `triples` table |

## Why triples stall after a bulk import

1. **`sync_turn()` never sets `extract=true`** — only `extract_entities=True` for conversation snippets.
2. **`mnemosyne_remember` defaults `extract=false`** — LLM SPO extraction goes to facts/annotations, not guaranteed `triples` inserts.
3. **Post-E6:** `_add_temporal_triple()` writes to **annotations**, not SQL `triples`.
4. **Only `add_triple()`** (tool `mnemosyne_triple_add`) inserts into the Knowledge Graph backing table.

A large one-day spike (e.g. 300+ triples) usually means a **manual ontology pass** (Discord channels, study schema), not passive chat learning.

## Quick verification

```bash
sqlite3 /root/.hermes/mnemosyne/data/mnemosyne.db \
  "SELECT COUNT(*) total, MAX(created_at) latest FROM triples;
   SELECT date(created_at), COUNT(*) FROM triples GROUP BY date(created_at) ORDER BY 1 DESC LIMIT 5;"
```

Compare to `mnemosyne_stats` working-memory totals.

## What to tell the user

- Memory **is** accumulating (working/episodic/memoria).
- **Graph triple count** is opt-in — not broken if flat.
- To grow triples: curated `mnemosyne_triple_add`, selective `remember(..., extract=true)` (fills other stores first), or a nightly promotion cron from high-signal memories.

## Daily Hermes full backup vs dedicated Mnemosyne backup

- `hermes_daily_full_backup.py` archives **`/root/.hermes` entire tree** with `EXCLUDE_PREFIXES = []` — **includes** `mnemosyne/data/mnemosyne.db` as a SQLite snapshot inside the encrypted tar.
- `mnemosyne_backup.py` is an **extra** gzip copy to `/mnt/tb/hermes-backups/mnemosyne/` with its own retention — faster restore, longer keep, separate Discord channel.

Both layers are intentional, not duplication by mistake.