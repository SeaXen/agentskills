# GBrain shared operator wrapper

Use this when a shared Hermes + GBrain setup has one verified CLI path and one stale global path.

## Problem shape
- Hermes MCP and the HTTP/admin surface are working.
- A direct global `gbrain ...` invocation resolves different config or embedding state than the known-good repo CLI path.
- Operators need one safe command path for routine direct actions.

## Durable fix pattern
Create or standardize a user-facing wrapper such as `gbrain-shared` that does the same setup as the working MCP/HTTP launchers:
- export the shared `GBRAIN_HOME`
- source the GBrain Postgres env file
- source Hermes env if provider keys live there
- export the shared `GBRAIN_DATABASE_URL`
- export `OLLAMA_BASE_URL` when local embeddings are used
- `cd` into the checked-out GBrain repo
- exec the repo CLI entrypoint, e.g. `/root/.bun/bin/bun run src/cli.ts "$@"`

## Verification
A wrapper is not done when the file exists. Verify real commands through it:
- `gbrain-shared config show`
- `gbrain-shared stats`
- `gbrain-shared get index`
- if embeddings matter: `gbrain-shared embed --stale` or a targeted embed command

The wrapper is valid only if those commands show the same engine, embedding model/dimensions, and page/chunk counts as the Hermes MCP and HTTP/admin surfaces.

## Why this matters
This reduces operator error after a migration or cutover. The user gets one reliable direct CLI path, while Hermes continues to use the MCP wrapper. Both routes then hit the same shared brain.
