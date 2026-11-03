# Migration v4: Cache Tokens on Runs Table

## Context
Added `cache_read_tokens` and `cache_write_tokens` columns to `runs` table for per-session/cron token breakdown.

## Migration Pattern

```python
def _migrate_v4(conn: sqlite3.Connection) -> None:
    """Add v4 schema: cache tokens on runs table for per-session/cron breakdown."""
    cur = conn.execute("SELECT version FROM schema_version WHERE version = 4")
    if cur.fetchone() is not None:
        return

    for col in ("cache_read_tokens", "cache_write_tokens"):
        try:
            conn.execute(f"ALTER TABLE runs ADD COLUMN {col} INTEGER DEFAULT 0")
        except sqlite3.OperationalError:
            pass  # already exists

    conn.execute(
        "INSERT OR IGNORE INTO schema_version(version, applied_at) VALUES (4, ?)",
        (_utcnow(),),
    )
```

Call in `_ensure_schema` after existing migrations:
```python
_migrate_v2(conn)
_migrate_v3(conn)
_migrate_v4(conn)  # NEW
```

## Record Function Update

```python
# In record_llm_call, update runs table with cache tokens:
conn.execute(
    """
    UPDATE runs
    SET tokens_in         = tokens_in  + ?,
        tokens_out        = tokens_out + ?,
        cache_read_tokens = cache_read_tokens + ?,
        cache_write_tokens = cache_write_tokens + ?,
        cost_usd          = cost_usd   + ?,
        api_calls         = api_calls  + 1,
        model             = COALESCE(model, ?),
        provider          = COALESCE(provider, ?)
    WHERE session_id = ?
    """,
    (tokens_in, tokens_out, cache_read_tokens, cache_write_tokens, cost_usd, model, provider, session_id),
)
```

## API Updates

Both `/api/runs` and `/api/cron` now return:
- `cache_read_tokens`
- `cache_write_tokens`

## Dashboard Table Updates

Cron Jobs and Recent Sessions tables show In/Out/Cache R/Cache W columns.

## Note
Existing sessions show 0 for cache tokens (pre-migration data). New sessions populate automatically.