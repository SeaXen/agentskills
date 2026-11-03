---
name: gbrain-shared-operations
description: Operate a shared GBrain backend for Hermes where MCP, admin UI, embeddings, and operator CLI all point to one Postgres-backed brain.
---

# GBrain Shared Operations

## When to use
- Hermes already uses GBrain and you need to improve or repair the **shared** brain only.
- MCP wrapper, admin HTTP launcher, and manual CLI commands must all target the same brain.
- You need to verify embeddings, backfills, or page updates on a live shared brain.
- The user explicitly wants Mnemosyne/MnemoSync left alone while GBrain improves.

## Core rule
Do not touch Mnemosyne or MnemoSync here.

This skill is only for the **deep-brain layer**:
- shared GBrain home
- shared Postgres backend
- MCP wrapper
- admin HTTP launcher
- operator CLI
- embeddings / extraction / page storage

## Preferred topology
One shared brain surface for all GBrain paths:
- Hermes MCP wrapper
- HTTP/admin launcher
- operator CLI

All three must agree on:
- `GBRAIN_HOME`
- `GBRAIN_DATABASE_URL`
- provider env
- CLI entrypoint

If one path differs, you get split behavior and false debugging.

## Mandatory operator wrapper
Create one operator-facing wrapper such as `gbrain-shared` and use it for all manual brain operations.

Minimum wrapper duties:
1. export the exact shared `GBRAIN_HOME`
2. source the Postgres env file
3. source Hermes env if provider keys live there
4. export the exact `GBRAIN_DATABASE_URL`
5. export local embedding env such as `OLLAMA_BASE_URL` when applicable
6. `cd` into the checked-out GBrain repo
7. exec the known-good CLI path

Why:
- avoids drift between MCP/admin/manual commands
- gives one reproducible path for `stats`, `get`, `query`, `embed`, `extract`, `sync`, and `put`
- prevents operators from accidentally using a stale global binary

## Verification order
1. `stats`
2. `config show`
3. `get` a known page
4. `query` a known term
5. `embed` one page, then all pages if needed
6. `extract --stale`
7. verify MCP still connects
8. verify HTTP `/health`

Do not declare success from config edits alone.

## Pitfalls

### 1. Global binary vs repo CLI drift
The installed `gbrain` binary can resolve different config/model state than the source-tree CLI.

If behavior differs:
- trust the path that matches real operations on the target shared brain
- standardize MCP, admin launcher, and operator wrapper on that same path
- verify with both `config show` and a real operation like `embed`, `stats`, or `get`

### 2. Postgres embedding-model change is a migration
For Postgres-backed brains, embedding model and dimensions are schema-sizing fields.

Treat model switches as a migration:
- drop HNSW index
- null embeddings
- alter vector column width
- recreate index
- verify the active CLI sees the new model/dimensions
- run a real embed command
- confirm `Embedded:` rises in `stats`

### 3. Sync can leave the stored page behind the repo file
A repo file can be updated while the brain still serves the older stored page.

If `sync` does not refresh the served page:
- use GBrain's own write path: `put <slug> < file.md`
- then verify with `get <slug>`

This is the reliable write-through path for the stored brain page.

### 4. Importing a single markdown file may do nothing
`import` against a single file path may collect zero markdown files depending on the command path and mode.

If you need to force-update one page, prefer:
- `put <slug> < file.md`

Do not assume single-file `import` is the right hammer.

### 5. Sparse corpora produce clean but small graph growth
`extract links`, `extract timeline`, or `extract --stale` can legitimately create zero new rows when the corpus is small or weakly linked.

Interpret correctly:
- zero new links/timeline is not a plumbing failure by itself
- the next improvement is usually better page structure and richer wikilinks, not more infra work

### 6. Global `gbrain` on PATH with wrong `GBRAIN_HOME`
If `/usr/local/bin/gbrain` still exports an old PGLite home while `gbrain-shared` uses the shared Postgres home, **autopilot and `which gbrain` hit the wrong brain**. Fix: `exec /usr/local/bin/gbrain-shared "$@"` in the global shim; verify `config show` on both paths.

## Hands-off growth (Option D)
Wire on the **shared** brain when the user wants auto growth without daily manual `put`:

1. **A** — `sync --watch` on the brain repo (systemd; Ollama embed only).
2. **B** — token-free Mnemosyne digest cron → `inbox/digest-YYYY-MM-DD` via `gbrain-shared put` (not an LLM cron).
3. **C** — `gbrain autopilot --install` (user systemd).

See **`references/hermes-gbrain-option-d-automation.md`**. Mnemosyne/MnemoSync untouched — digest reads SQLite only.

## High-value follow-on improvements
When infra is already healthy, improve the corpus instead of the plumbing:
- create better people/company/project/concept pages
- add explicit wikilinks
- add structured timeline sections where dates matter
- enrich project pages with stable architecture facts and operational paths

## Success definition
Shared GBrain operations count as healthy when all of these are true:
- one operator wrapper exists and works
- MCP wrapper works
- admin HTTP health works
- embeddings are active on the shared brain
- `get` returns the expected stored page content
- page writes through `put` are visible immediately in the brain

## References
- `references/shared-gbrain-operator-pattern.md` — exact patterns for operator wrapper, embed cutover, and write-through page refresh.
- `references/hermes-gbrain-option-d-automation.md` — Option D (sync watch + Mnemosyne digest cron + autopilot), stale-`gbrain` shim fix, zero-token operator framing.
