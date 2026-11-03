# GBrain Postgres Embedding Cutover: Shared Hermes + Dashboard

Use this when a Hermes↔GBrain hybrid stack has already been moved onto one shared Postgres-backed GBrain home and you need embeddings to work on that shared brain.

## Durable lessons

### 1. Verify the real launcher path
Do not assume `/usr/local/bin/gbrain` and the repo CLI resolve the same config.

On this pattern, the reliable path was:

```bash
cd /mnt/tb/1Apps/GBrain
/root/.bun/bin/bun run src/cli.ts ...
```

Proof pattern:
- compare `config show`
- compare a real write/read operation (`embed index`, `stats`, `serve`)
- standardize wrappers/launchers on the path that matches real shared-brain behavior

### 2. Shared wrappers must agree on all planes
The Hermes MCP wrapper and the HTTP/admin launcher must share:
- `GBRAIN_HOME`
- `GBRAIN_DATABASE_URL`
- provider env from the brain-specific env file
- provider env from `~/.hermes/.env` when child processes need Hermes-side secrets
- `OLLAMA_BASE_URL` (or equivalent embedding endpoint)
- the same CLI path

If one surface uses a different launcher path, it can silently read a different config plane.

### 3. Postgres embedding changes are schema changes
Changing from OpenRouter 1536-dim embeddings to Ollama 768-dim embeddings is not just a config edit.

Minimal safe migration when existing embeddings can be discarded:

```sql
DROP INDEX IF EXISTS idx_chunks_embedding;
UPDATE content_chunks SET embedding = NULL, embedded_at = NULL;
ALTER TABLE content_chunks ALTER COLUMN embedding TYPE vector(768);
CREATE INDEX IF NOT EXISTS idx_chunks_embedding
  ON content_chunks USING hnsw (embedding vector_cosine_ops);
```

Then verify the active CLI path sees the intended embedding model and dimensions before re-embedding.

### 4. Success proof
Do not claim success on config edits alone.

Minimum proof:
- `config show` from the real launcher path shows the intended model/dimensions
- `embed index` or `embed --all` succeeds
- `stats` shows embedded chunk count > 0
- Hermes `mcp test gbrain` still passes after wrapper alignment
- HTTP `/health` still returns OK after launcher alignment

## Known-good pattern from this session
- shared home: one Postgres-backed `GBRAIN_HOME`
- Hermes wrapper switched to repo CLI `bun run src/cli.ts serve`
- HTTP/admin launcher switched to repo CLI `bun run src/cli.ts serve --http ...`
- embeddings switched to local Ollama `nomic-embed-text`
- full embed pass completed successfully after wrapper/path alignment
