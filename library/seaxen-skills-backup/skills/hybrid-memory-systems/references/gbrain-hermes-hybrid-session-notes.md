# Hermes + GBrain hybrid session notes

## Durable lessons from this setup

### 1. Use a wrapper for the real CLI entrypoint
A working pattern was:
- set `GBRAIN_HOME` in `/usr/local/bin/gbrain`
- load `OPENROUTER_API_KEY` from Hermes's `.env` inside that wrapper
- `cd` into the GBrain repo
- exec `bun run src/cli.ts "$@"`

Reason: the compiled binary path and the MCP child-process env were not reliable enough by themselves for this setup.

### 2. Use a separate MCP wrapper
A tiny MCP target script worked:
- `export MCP_STDIO=1`
- `exec /usr/local/bin/gbrain serve`

That kept Hermes MCP config simple and let the main wrapper own env/home logic.

### 3. If `sync` times out on PGLite lock, inspect running MCP processes first
Observed live processes included:
- `mcp_stdio_watchdog.py -- /root/.hermes/scripts/mcp-servers/gbrain-mcp/run.sh`
- `bun run src/cli.ts serve`

Those held the active PGLite lock. Killing them temporarily allowed `gbrain sync --no-embed` to import pages cleanly.

### 4. `embedding_disabled: true` can survive and silently force deferred mode
After an earlier no-embed init, reinit still behaved like deferred setup until the stale config flag was removed from `.../.gbrain/config.json`.

Signal to check for:
- reinit prints a deferred/no-embedding style message even when an embedding model was supplied

### 5. Distinguish local install success from provider failure
Local hybrid install succeeded even though embeddings failed due to upstream provider quota.

Concrete shape:
- Hermes MCP showed `gbrain` enabled
- GBrain repo imported successfully with `--no-embed`
- pages/chunks existed
- embeddings remained `0` because OpenRouter returned key-limit/quota errors

This is a valid "connected and usable, but not fully semantic" state.

### 6. Do not assume gateway restart is required
In this case Hermes had already loaded the `gbrain` MCP server and started the watchdog/serve process. `hermes mcp list` plus process inspection was enough to prove connection.

## Verification pattern that worked
1. Confirm MCP server enabled in Hermes.
2. Check for live watchdog + serve processes.
3. Stop them only if they block PGLite sync.
4. Import repo with `--no-embed` if provider quota blocks semantic ingest.
5. Verify:
   - `gbrain stats`
   - `gbrain list`
   - `gbrain get <known-page>`

## What not to overlearn
- Do not encode the specific provider quota failure as a permanent constraint.
- Do not encode host-specific path assumptions as universal defaults.
- Keep the lesson at the level of wrappers, locks, deferred-embed flags, and MCP verification.
