# Shared GBrain operator pattern

## Use case
Hermes already has a shared GBrain backend and you want a reliable manual/operator path that matches the live MCP/admin behavior.

## Known-good wrapper shape
```bash
#!/usr/bin/env bash
set -euo pipefail
export GBRAIN_HOME=/path/to/shared-home
set -a
source /path/to/postgres.env
[ -f /root/.hermes/.env ] && source /root/.hermes/.env || true
set +a
export GBRAIN_DATABASE_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@127.0.0.1:5434/${POSTGRES_DB}"
export OLLAMA_BASE_URL="http://127.0.0.1:11434/v1"
cd /path/to/GBrain
exec /root/.bun/bin/bun run src/cli.ts "$@"
```

## Verify the shared brain through the wrapper
```bash
gbrain-shared stats
gbrain-shared config show
gbrain-shared get projects/hermes-gbrain-hybrid
gbrain-shared query "hybrid memory"
```

## Postgres + local embedding cutover
When changing from one embedding space to another on Postgres:
1. drop `idx_chunks_embedding`
2. set `embedding = NULL, embedded_at = NULL`
3. alter `content_chunks.embedding` to the target `vector(N)`
4. recreate the HNSW index
5. verify the active CLI path sees the target model/dims
6. run a real embed command
7. confirm `Embedded:` increases in `stats`

## Stored-page refresh rule
If the repo file is newer than the served GBrain page, prefer write-through:
```bash
gbrain-shared put <slug> < file.md
gbrain-shared get <slug>
```
This is more reliable than hoping a plain sync or single-file import refreshed the stored page.

## Interpretation rule for extraction
If these all run cleanly but create nothing:
- `gbrain-shared extract links --source db`
- `gbrain-shared extract timeline --source db`
- `gbrain-shared extract --stale`

then the likely problem is **corpus sparseness**, not broken infra.
The next fix is better note structure and richer wikilinks, not more launcher work.
