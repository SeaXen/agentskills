# Hermes home cleanup and MCP repo audit

Use this when reclaiming space under `~/.hermes` for Dr. Sagar.

## Safe reclaim order
1. Old `state-snapshots/`
2. `cache/`
3. logs / `.bak` files / backup artifacts
4. abandoned profiles
5. optional script repos only after reference audit

## High-value data — do not delete casually
- `config.yaml`
- `.env`
- `auth.json`
- `state.db`
- `sessions/`
- `skills/`
- `plugins/`
- `memories/`
- `cron/`

## Snapshot cleanup pattern
- Sort snapshot directories by name/date.
- Keep the newest N explicitly requested by the user.
- Delete older ones.
- Verify the remaining set after deletion.

## Mnemosyne local model cache
`~/.hermes/mnemosyne/models/` can hold a local GGUF model for embeddings/LLM inference.
- Observed: `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf` — **638 MB** (4-bit quantized TinyLlama 1.1B)
- Safe to delete if disk space is tight — Mnemosyne will re-download on next use, or fall back to API embeddings if `MNEMOSYNE_EMBEDDING_PROVIDER` is set.
- Actual memory data (`mnemosyne/data/`) is small (~21 MB); the model file dominates.

## Checkpoints vs state-snapshots
| | Checkpoints | state-snapshots |
|---|---|---|
| **Trigger** | Periodic (config: `min_interval_hours`, default 24h) | Pre-update only (manual or `hermes upgrade`) |
| **Auto-prune** | Yes (`max_snapshots`, `retention_days`, `max_total_size_mb`) | **No** — accumulates until manual cleanup |
| **Scope** | `state.db` + SQLite WAL/SHM only | Entire `.hermes/` folder (full backup) |
| **Config location** | `checkpoints:` section in `config.yaml` | Not configurable; created by update script |
| **Current state** | `enabled: false` (disabled) | One snapshot: `20260608-052040-pre-update` (1.1 GB) |

**Key insight**: The 1.1 GB in `state-snapshots/` is a one-off pre-update backup from June 8th. It is safe to delete if the update succeeded. Checkpoints are a separate, disabled system.

## MCP repo-clone audit pattern
When auditing `~/.hermes/scripts/mcp-servers/*`:
1. Get per-repo sizes.
2. Check active `config.yaml` MCP server entries.
3. Mark repos as:
   - enabled + referenced
   - disabled but referenced
   - unreferenced
4. Only call `disabled but referenced` or `unreferenced` repos removable candidates.
5. Ask before deleting repo clones.

## Critical path-identity check
On this system, `/root/.hermes/...` and `/mnt/tb/hermes/...` may be the same live files/directories.

Before deleting any repo clone referenced from config, verify with `os.path.samefile()` or equivalent. Do not assume these are duplicate copies.

## Session-specific result captured here
Observed MCP repo-clone status during this cleanup pass:
- keep: `alpha-vantage-mcp`, `bybit-mcp`, `crypto-data-mcp`, `mcp-dexscreener`, `hn-mcp`
- lower-risk delete candidates: `mcp-server-openmeteo` (unreferenced), `mcp-toolbox` (unreferenced)
- conditional candidate: `mcp-discord` (referenced but disabled)

**Disk usage snapshot (June 9, 2026):**
- Total `~/.hermes`: **4.6 GB**
- `state-snapshots/20260608-052040-pre-update/`: **1.1 GB** (safe to delete)
- `mnemosyne/models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf`: **638 MB** (safe to delete, will re-download or use API)
- `state.db`: **1.1 GB** (core state — keep)
- `sessions/`: **475 MB** (history — keep)
- `scripts/`: **353 MB** (includes MCP repo clones — audit before delete)
- `venvs/`: **332 MB** (Python envs — keep unless rebuilding)
- `skills/`: **114 MB** (keep)
- `lsp/` + `plugins/`: ~207 MB (keep)
