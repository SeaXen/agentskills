# Mnemosyne Upgrade on Debian — Pitfalls and Recipe

**Session:** 2026-06-23 — Upgrade mnemosyne-memory 3.5.0/3.7.0 → 3.10.1 + mnemosyne-hermes 0.1.8 → 0.2.0 on a DietPi/Debian 13 (trixie) host with the firmware emergency-cutoff at ~88°C.

## Current install shape (post-0.2.0)

| Surface | Location | What it holds |
|---|---|---|
| System Python | `/usr/bin/python3` (3.13.5) | `mnemosyne-memory` 3.10.1 + `[embeddings]` extras |
| Hermes-agent venv | `/usr/local/lib/hermes-agent/venv` (3.11) | `mnemosyne-memory` 3.10.1 + `[embeddings]` extras (its own copy, not shared with system) |
| Plugin | `pipx` isolated venv at `/root/.local/share/pipx/venvs/mnemosyne-hermes` | `mnemosyne-hermes` 0.2.0 |
| Live DB | `/root/.hermes/mnemosyne/data/mnemosyne.db` (~35-43 MB) | 2990 working + 113 episodic + 352 triples + 2653 fallback embeddings |
| Backups | `/root/.hermes/mnemosyne/backups/` | Manual `.db` copies (NOT `mnemosyne backup` output until upstream fix lands) |
| Dashboard | `http://127.0.0.1:8765/` | `mnemosyne-dashboard` plugin via hermes-agent venv python |

Auto-discovery is via `hermes_agent.memory_providers` and `hermes_agent.plugins` entry points. No `~/.hermes/plugins/hermes-mnemosyne/` copy. No `config.yaml` plugin list edit.

## Debian-specific gotchas

### 1. PEP 668 + apt-owned `click`

```bash
pip install --upgrade --break-system-packages --ignore-installed click "mnemosyne-memory[embeddings]"
```

### 2. `[embeddings]` not `[all]`

`[all]` pulls LLM compile deps (5+ min, 2-3 GB RAM). Use `[embeddings]` for fastembed + sqlite-vec + onnxruntime.

### 3. Hermes-agent venv has no `pip`

```bash
/usr/local/lib/hermes-agent/venv/bin/python -m ensurepip --upgrade
/usr/local/lib/hermes-agent/venv/bin/python -m pip install --upgrade "mnemosyne-memory[embeddings]"
```

### 4. `vec0` backup bug (3.10.x) — two failure points

`mnemosyne/dr/recovery.py::create_backup`:

1. `src.backup(dst)` needs vec0 loaded on **src**
2. `dst.iterdump()` needs vec0 loaded on **dst** (`:memory:`) or dump fails with `no such module: vec0` even when step 1 passes

**Workarounds on host:**

```bash
ln -sf /usr/local/lib/python3.13/dist-packages/sqlite_vec/vec0.so /usr/local/lib/vec0.so
mnemosyne reindex --no-backup --yes   # skip broken auto-backup; manual cp first
```

**Upstream fix:** load sqlite-vec on both connections (mirror `core/beam.py` graceful fallback). PR: https://github.com/AxDSan/mnemosyne/pull/374

**Separate issue (not fixed in that PR):** `restore_backup()` via `iterdump` + `executescript` can fail on FTS5+vec0 ordering (`no such table: fts_episodes`). Backup gzip content can still be valid for manual recovery.

### 5. Upgrade does not delete memories

Compare row counts before/after on `working_memory`, `episodic_memory`, `triples`, `memory_embeddings`. Counts should stay same or increase after upgrade/reindex partials.

### 6. Thermal pacing (Dr. Sagar laptop)

`sleep 60-90` between: stop services → pip upgrades → reindex → restart. Reindex 5-10 min can hit 87-88°C; terminal timeout can kill mid-reindex (`vec_working` partial e.g. 960/2990). FTS5 still covers full working set.

## Safe upgrade sequence

Stop gateway + dashboard → manual `cp` DB → cool gap → system pip + venv pip + `pipx upgrade mnemosyne-hermes` → vec0 symlink → reindex `--no-backup --yes` → restart → verify three version surfaces (system pip, venv import, `hermes memory status` after restart).

## Reference

- PyPI: mnemosyne-memory, mnemosyne-hermes
- GitHub: https://github.com/AxDSan/mnemosyne
- PR #374: backup sqlite-vec load on src+dst

## Vault cross-link (Dr. Sagar)

After upgrade, mirror durable **facts** into Obsidian: `Knowledge/Mnemosyne Operations.md`, `issues-fixes-log.md`, superseding `decisions.md` if provider is live (not sandbox-only). Audit workflow: `obsidian-memory-vault` → `references/vault-audit-sessions-and-mnemosyne.md`.