# Mnemosyne-Hermes Plugin Install / Upgrade Pattern

**Updated:** 2026-06-23 — verified against mnemosyne-memory 3.10.1 + mnemosyne-hermes 0.2.0 on this host.

Older versions of this file (pre-2026) describe a vendor-repo + symlink + manual `config.yaml` install shape. That pattern is deprecated as of `mnemosyne-hermes` 0.2.0. Use the current shape below. For Debian-specific gotchas (PEP 668, apt-owned `click`, `vec0.so` symlink, multi-Python venvs, reindex thermal timing), see `references/mnemosyne-upgrade-debian-pitfalls.md`.

## Core vs Embeddings vs All Extras

| Extra | Install time | Disk | Use case |
|-------|-------------|------|----------|
| `mnemosyne-memory` (base) | <30 sec | ~10 MB | Memory provider, MCP, CLI, basic tools — no local inference, no vector search |
| `mnemosyne-memory[embeddings]` | 1-2 min | ~500 MB | Adds `fastembed` + `sqlite-vec` + `onnxruntime` — what the dashboard needs for vector search |
| `mnemosyne-memory[all]` | 10-20 min | 2-3 GB | Adds ctransformers + llama-cpp-python for local GGUF models — rarely needed |

**Default to `[embeddings]`** unless the user explicitly needs local GGUF inference. `[all]` will hit the 5-min foreground terminal timeout and then some because `llama-cpp-python` compiles C++ from source.

## Install / Upgrade Shape (post-0.2.0)

Three surfaces, all separate:

| Surface | Command | Location |
|---|---|---|
| System pip | `pip install --upgrade "mnemosyne-memory[embeddings]"` (Debian needs `--break-system-packages --ignore-installed click`) | `/usr/bin/python3` (3.13) site-packages |
| Hermes-agent venv | `/usr/local/lib/hermes-agent/venv/bin/python -m pip install --upgrade "mnemosyne-memory[embeddings]"` | hermes-agent venv site-packages (3.11) |
| Plugin | `pipx upgrade mnemosyne-hermes` (or `pipx install mnemosyne-hermes` for first install) | pipx isolated venv at `~/.local/share/pipx/venvs/mnemosyne-hermes` |

**No `~/.hermes/plugins/hermes-mnemosyne/` copy. No `config.yaml` plugin list edit. No symlinks.** Auto-discovery is via `hermes_agent.memory_providers` and `hermes_agent.plugins` entry points.

## What the Plugin Provides

- **Memory Provider:** `memory.provider: mnemosyne` in `~/.hermes/config.yaml`
- **Agent plugin slug:** `hermes-mnemosyne` (symlink under `~/.hermes/plugins/mnemosyne` → pipx `mnemosyne_hermes`). Distinct from **`mnemosyne-dashboard`** (standalone UI on `:8765`, tools only — not a `:9119` nav tab without `dashboard/manifest.json`).
- **23 tools** including `mnemosyne_remember`, `mnemosyne_recall`, `mnemosyne_stats`, `mnemosyne_sleep`, `mnemosyne_triple_add`, `mnemosyne_triple_query`, `mnemosyne_invalidate`, `mnemosyne_export`, `mnemosyne_import`, `mnemosyne_diagnose`, etc.
- **CLI:** `mnemosyne` command available via the pipx-venv binary (not `/usr/local/bin/mnemosyne`, which is the system pip one — both work after the multi-Python upgrade)

## Provider active vs plugin "not enabled"

`hermes memory status` can show **Provider: mnemosyne ← active** while `hermes plugins list` shows **`hermes-mnemosyne` not enabled**. Those are different layers:

| Check | Meaning |
|-------|---------|
| `memory.provider: mnemosyne` | Config-selected external memory backend |
| `hermes memory status` | Provider package installed + selectable |
| `plugins.enabled` contains `hermes-mnemosyne` | Agent runtime loads plugin hooks/tools on new sessions |
| Built-in `MEMORY.md` / `USER.md` | Still inject when `memory.memory_enabled: true` — alongside Mnemosyne |

If the user asks "is Mnemosyne inactive?", answer from **`hermes memory status`** and live `mnemosyne_stats`, not from stale `hermes memory` help text (banner omits mnemosyne). Run `hermes plugins enable hermes-mnemosyne` if the Plugins hub shows not enabled; gateway restart for full hook effect.

Hermes dashboard **Memory** tab (`hermes-memory-ui`) is separate: needs `plugins.enabled` + dashboard restart for `/api/plugins/hermes-memory-ui/snapshot` (see `references/dashboard-user-plugins-enabled-gate.md`).

## Verification Checklist

- [ ] System pip: `pip3 list | grep mnemosyne` → 3.10.x
- [ ] Hermes-agent venv: `/usr/local/lib/hermes-agent/venv/bin/python -c "import mnemosyne; print(mnemosyne.__version__)"` → 3.10.x
- [ ] Plugin: `pipx list | grep mnemosyne-hermes` → 0.2.x
- [ ] Heavy deps in hermes venv: `sqlite_vec`, `fastembed`, `onnxruntime`
- [ ] `hermes memory status` → `Provider: mnemosyne`, `Plugin: installed ✓`
- [ ] Live DB: `/root/.hermes/mnemosyne/data/mnemosyne.db` exists
- [ ] Dashboard: `curl -o /dev/null -w "%{http_code}" http://127.0.0.1:8765/` → `200`
- [ ] Vectors loadable: `python3 -c "import sqlite3, sqlite_vec; db=sqlite3.connect('/root/.hermes/mnemosyne/data/mnemosyne.db'); db.enable_load_extension(True); sqlite_vec.load(db); print(db.execute('SELECT vec_version()').fetchone())"`
- [ ] Gateway + dashboard restarted after install (provider module reload)

## Version Surface Parity

Three surfaces can drift apart if you only upgrade one. Always verify all three after any change:

1. **System pip package** — `pip3 list | grep mnemosyne`
2. **Hermes-agent venv package** — `/usr/local/lib/hermes-agent/venv/bin/python -c "import mnemosyne; print(mnemosyne.__version__)"`
3. **Live runtime** — restart the gateway, then check `hermes memory status`

The running gateway reports the OLD version until restart because the provider module stays loaded in process memory. Disk state and process state are separate — always restart after a provider upgrade.

## Live DB Tables (3.10.x schema)

Content: `working_memory`, `episodic_memory`, `facts`, `triples`. Fallback embeddings: `memory_embeddings`. sqlite-vec virtual tables: `vec_working`, `vec_episodic`, `vec_facts`. FTS5: `fts_working`, `fts_episodic`, `fts_facts`. Derived: `consolidated_facts`, `graph_edges`, `memoria_*`, `gists`, `annotations`, `conflicts`.

`mnemosyne reindex` rebuilds the `vec_*` tables. FTS5 and `memory_embeddings` are not touched.

## Backups

**Do not rely on `mnemosyne backup` in 3.10.x** — it fails with `no such module: vec0` because the library calls `sqlite3.Connection.backup()` without first loading the sqlite-vec extension. Use a manual `cp` of the `.db` file to `~/.hermes/mnemosyne/backups/`. For a proper fix, see the upstream issue pattern in `references/mnemosyne-upgrade-debian-pitfalls.md` §"Upstream bug worth filing".

## Full Recipe

For the complete upgrade sequence (with thermal gaps, vec0 symlink, `ensurepip` bootstrap, and reindex timing), see `references/mnemosyne-upgrade-debian-pitfalls.md`.
