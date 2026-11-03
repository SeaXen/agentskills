---
name: gbrain-hermes-integration
description: Integrate Hermes with GBrain as a shared deep-memory backend using official upstream patterns, with verified wrappers, shared topology choices, and embedding migration discipline.
version: 1.0.1
---

# GBrain ↔ Hermes integration

## Use when
- Hermes should use GBrain as a shared knowledge/deep-memory layer
- You need the official-ish upstream path instead of a custom sidecar memory system
- You are exposing the GBrain admin/dashboard and Hermes MCP against the same backend
- You are migrating from split local homes to one shared backend
- You need to restore embeddings without breaking an existing Postgres brain

## Core model
Treat the systems as layered, not identical:
- **Hermes native memory (Mnemosyne)** = user preferences, durable operator facts, collaboration context
- **GBrain** = deep knowledge store, pages, graph, repo-backed knowledge, semantic retrieval, MCP-accessible brain

Do **not** claim that wiring Hermes to GBrain means all Hermes memory now lives in GBrain. That is false unless explicitly built.

## Preferred topology
For a serious shared setup, prefer:
- **one shared GBrain home**
- **one shared Postgres-backed brain**
- **Hermes MCP wrapper** pointed at that shared backend
- **HTTP/admin launcher** pointed at that same shared backend

This avoids the classic PGLite split-brain/lock pattern where:
- Hermes MCP uses one home
- dashboard uses another home
- user thinks writes are shared when they are not

### Recommended shape
- shared home: one `GBRAIN_HOME`
- shared DB: one `GBRAIN_DATABASE_URL`
- Hermes wrapper and dashboard launcher should source the same env/material
- use one verified CLI path everywhere

## CLI discipline
On systems where the global `gbrain` binary and the repo source-run path disagree, trust the **repo CLI** if it is the path you actually verified.

Preferred verified pattern:
```bash
cd /path/to/GBrain
/root/.bun/bin/bun run src/cli.ts ...
```

### Pitfall: global binary drift
A machine can have a stale or behaviorally different `/usr/local/bin/gbrain` while the repo CLI resolves the correct config.

Symptoms:
- `bun run src/cli.ts config show` reports one embedding model/dim
- `gbrain config show` reports another
- `init` appears to work but later `embed` still resolves the old provider/dim

If this happens:
1. Stop assuming the installed binary is authoritative.
2. Verify the repo CLI directly.
3. Standardize Hermes wrappers/launchers on the repo CLI path.
4. Re-test MCP after switching the wrapper.

## Wrapper rules
Hermes should talk to GBrain through MCP, not by touching the database directly.

### Hermes MCP wrapper should
- export `MCP_STDIO=1`
- export the shared `GBRAIN_HOME`
- load the shared DB env
- load any relevant Hermes env file if provider/env context is needed
- export `GBRAIN_DATABASE_URL`
- export local embedding endpoint env when used (for example `OLLAMA_BASE_URL`)
- `cd` into the GBrain repo
- `exec /root/.bun/bin/bun run src/cli.ts serve`

### HTTP/admin launcher should
Use the same environment and the same repo CLI discipline, then run:
```bash
/root/.bun/bin/bun run src/cli.ts serve --http --bind 0.0.0.0 --port <port>
```

## Explaining read/write behavior to the user
Be precise.

Hermes does **not** normally read/write GBrain by patching files or SQL directly.
It uses **GBrain MCP tools**.

### Reads happen via tools like
- `get_page`
- `list_pages`
- `search`
- `query`
- `get_links`
- `get_backlinks`
- `get_chunks`
- `get_stats`
- `think`
- `recall`

### Writes happen via tools like
- `put_page`
- `delete_page`
- `add_tag`
- `remove_tag`
- `add_link`
- `remove_link`
- `add_timeline_entry`
- `put_raw_data`
- `sync_brain`

Operationally:
- Hermes = client/orchestrator
- GBrain = memory server
- Postgres = storage backend

## Official-way clarification
Do **not** tell the user that the official way requires paid cloud tokens.

Correct framing:
- GBrain core storage/admin/MCP can run without paid AI
- semantic retrieval / embeddings / synthesis require **some** model backend
- that backend may be **local** (for example Ollama), not necessarily paid cloud

Useful wording:
- database/memory surface: no paid API required
- semantic/vector/LLM features: require a model backend somewhere

## Embedding migration discipline for Postgres brains
Changing embedding model/dimensions on a Postgres brain is **schema work**, not just a config toggle.

### Do not assume this works
```bash
gbrain config set embedding_model ...
```
for Postgres brains whose vector width must change.

### Correct posture
If dimensions change, treat it as an embedding migration:
1. verify current effective model/dimensions
2. verify actual vector column width in Postgres
3. null out stale embeddings before type change
4. alter the vector column width
5. recreate the HNSW index
6. update the effective config path actually used by the verified CLI
7. run embed from the verified CLI path
8. confirm embedded chunk count increased

### Safe SQL shape
```sql
DROP INDEX IF EXISTS idx_chunks_embedding;
UPDATE content_chunks SET embedding = NULL, embedded_at = NULL;
ALTER TABLE content_chunks ALTER COLUMN embedding TYPE vector(<N>);
CREATE INDEX IF NOT EXISTS idx_chunks_embedding
  ON content_chunks USING hnsw (embedding vector_cosine_ops);
```

### Pitfall: config-plane mismatch
A shared Postgres brain can still resolve stale embedding settings if different config planes disagree.

Check all of these if behavior is inconsistent:
- shared home config file
- DB config rows
- environment variables
- repo CLI effective config
- global binary effective config

Do not stop at editing one file if runtime behavior contradicts it.

## Local embeddings path
When hosted embedding quota is blocked or undesirable, local embeddings via Ollama are a valid official-style path.

### Practical pattern
- install/start Ollama locally
- pull a small embedding model such as `nomic-embed-text`
- export `OLLAMA_BASE_URL=http://127.0.0.1:11434/v1`
- migrate the shared brain to the model's dimension width
- run embed from the verified repo CLI

### Verification target
Do not claim success until you have a real embed result such as:
- `Embedded X chunks across Y pages`
- stats showing non-zero `Embedded:` count

## Verification checklist
Before finalizing, verify all of the following with real commands/results:
1. HTTP health reports the expected engine
2. admin URL responds
3. Hermes MCP test connects and discovers tools
4. repo CLI `config show` resolves the expected embedding model/dim
5. embed command actually embeds chunks
6. stats show the expected embedded count

## Common pitfalls
- assuming split homes are shared memory
- assuming Hermes native memory and GBrain are the same store
- trusting the global `gbrain` binary when the repo CLI is the only verified path
- changing embedding provider/dimensions without resizing the vector column
- editing only file config when runtime is being resolved from another layer
- reporting embeddings fixed before verifying chunk counts
- assuming MCP wiring alone auto-grows GBrain — without sync watch, autopilot, or a Mnemosyne digest job, pages appear only on explicit `put_page` / `put`

## Hands-off sync (pointer)
See **`gbrain-shared-operations`** → `references/hermes-gbrain-option-d-automation.md` for Option D (watch + token-free digest cron + autopilot).

## Changelog
- **1.0.1**: Pitfall that MCP alone does not auto-grow GBrain; pointer to Option D reference.
- **1.0.0**: Created from a full Hermes↔GBrain integration session covering shared Postgres topology, repo-CLI wrapper standardization, local Ollama embeddings, Postgres vector-width migration, and precise explanation of Hermes MCP read/write behavior.
