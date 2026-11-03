# Mnemosyne Memory Provider for Hermes Agent

## Overview
Mnemosyne is a local-first memory provider for Hermes Agent with SQLite + vector embeddings + FTS5 hybrid search. It replaces the built-in MEMORY.md/USER.md system.

**Key packages:**
- `mnemosyne-memory` (core library) — PyPI: `mnemosyne-memory`
- `mnemosyne-hermes` (Hermes adapter) — PyPI: `mnemosyne-hermes`

**Docs:** https://docs.mnemosyne.site | **GitHub:** https://github.com/AxDSan/mnemosyne

---

## Critical Architecture: Two Python Environments

### Hermes venv (runtime)
```
/usr/local/lib/hermes-agent/venv/bin/python
```
- This is where Hermes actually runs
- **Does NOT have pip** (externally managed environment)
- Mnemosyne core (`mnemosyne-memory`) MUST be importable here

### pipx venv (mnemosyne-hermes adapter)
```
/root/.local/share/pipx/venvs/mnemosyne-hermes/bin/python
```
- This is where `mnemosyne-hermes` CLI lives
- Has its own copy of `mnemosyne-memory` as dependency
- `mnemosyne-hermes install --force` bootstraps by trying to install into Hermes venv

---

## Installation / Upgrade Procedure

### Standard upgrade
```bash
# 1. Upgrade adapter (in pipx venv)
pipx upgrade mnemosyne-hermes

# 2. Upgrade core in Hermes venv (via uv, since Hermes venv has no pip)
uv pip install --python /usr/local/lib/hermes-agent/venv/bin/python -U mnemosyne-memory

# 3. Upgrade adapter in Hermes venv (also via uv)
uv pip install --python /usr/local/lib/hermes-agent/venv/bin/python -U mnemosyne-hermes

# 4. Install plugin (symlinks into ~/.hermes/plugins/mnemosyne)
mnemosyne-hermes install --force

# 5. Configure Hermes to use it
hermes config set memory.provider mnemosyne

# 6. Restart gateway
hermes gateway restart
```

### Fresh install (one-shot)
```bash
pipx install "mnemosyne-hermes[all]"
mnemosyne-hermes install
hermes config set memory.provider mnemosyne
hermes gateway restart
```

---

## Common Pitfalls & Fixes

### 1. "Hermes' Python can't import mnemosyne core"
**Error:**
```
⚠ Hermes' Python at /usr/local/lib/hermes-agent/venv/bin/python can't import mnemosyne core.
   mnemosyne-hermes is installed in YOUR Python (/root/.local/share/pipx/venvs/mnemosyne-hermes/bin/python),
   but Hermes runs from a different venv.
```

**Cause:** `mnemosyne-memory` is installed in pipx venv but not in Hermes venv.

**Fix:** Install into Hermes venv using uv:
```bash
uv pip install --python /usr/local/lib/hermes-agent/venv/bin/python -U mnemosyne-memory
```

### 2. "cannot import name '__version__' from 'mnemosyne_hermes'"
**Error during `mnemosyne-hermes install --force`:**
```
error: cannot import name '__version__' from 'mnemosyne_hermes' (/root/.local/share/pipx/venvs/mnemosyne-hermes/lib/python3.13/site-packages/mnemosyne_hermes/__init__.py)
```

**Cause:** The `mnemosyne_hermes/__init__.py` is missing `__version__` export that `install.py` and `cli.py` import via `from . import __version__`.

**Fix:** Patch `__init__.py` to add version:
```python
# Add after logger = logging.getLogger(__name__)
__version__ = "0.1.8"  # Match pipx_metadata.json version
```

**File location:** `/root/.local/share/pipx/venvs/mnemosyne-hermes/lib/python3.13/site-packages/mnemosyne_hermes/__init__.py`

### 3. Bootstrap timeout building llama-cpp-python
**Error:** `uv pip install ... mnemosyne-hermes[all]` times out building `llama-cpp-python`

**Cause:** The `[all]` extra pulls in LLM dependencies that require compilation.

**Fix:** Install base only (`mnemosyne-hermes` without extras), since core memory doesn't need LLM deps:
```bash
uv pip install --python /usr/local/lib/hermes-agent/venv/bin/python -U mnemosyne-hermes
```

### 4. Gateway restart blocked
**Error:** `BLOCKED: Command timed out without user response`

**Cause:** `hermes gateway restart` requires interactive confirmation.

**Fix:** Run manually when ready, or use `systemctl --user restart hermes-gateway` if running as systemd service.

---

## Verification Commands

```bash
# Check provider status
hermes memory status
# Should show:
#   Provider:  mnemosyne
#   Plugin:    installed ✓

# Test tool registration (23 tools)
hermes tools list | grep mnemosyne

# Direct mnemosyne CLI (from pipx venv)
mnemosyne stats
mnemosyne recall "test query" --limit 3
```

---

## Configuration (Optional)

All optional, via `~/.hermes/config.yaml` or env vars:

```yaml
memory:
  provider: mnemosyne
  mnemosyne:
    auto_sleep: true              # default: false
    sleep_threshold: 30           # default: 50 turns
    profile_isolation: false      # default: false (separate DB per Hermes profile)
    vector_type: "int8"           # float32|int8|bit
    ignore_patterns: []           # regex patterns to filter from memory
    shared_surface_path: ""       # path for shared cross-agent surface
    sync_roles: ["user", "assistant"]  # which roles to autosave
```

**Key env vars:**
| Variable | Default | Description |
|---|---|---|
| `MNEMOSYNE_HOME` | `~/.mnemosyne` | Storage directory |
| `MNEMOSYNE_VEC_WEIGHT` | `0.5` | Vector similarity weight |
| `MNEMOSYNE_FTS_WEIGHT` | `0.3` | Full-text search weight |
| `MNEMOSYNE_IMPORTANCE_WEIGHT` | `0.2` | Importance score weight |
| `MNEMOSYNE_AUTO_SLEEP_ENABLED` | `false` | Auto-consolidate after N turns |
| `MNEMOSYNE_AUTO_SLEEP_THRESHOLD` | `50` | Turns between auto-consolidation |
| `MNEMOSYNE_PROFILE_ISOLATION` | `false` | Separate DB per profile |
| `MNEMOSYNE_SYNC_TURN_USER_LIMIT` | `500` | User content truncation (0 = no limit) |
| `MNEMOSYNE_SYNC_TURN_ASSISTANT_LIMIT` | `800` | Assistant content truncation (0 = no limit) |

---

## Disable Built-in Memory (Important)

When using Mnemosyne, disable Hermes' built-in MEMORY.md/USER.md system to avoid duplication:

```yaml
# ~/.hermes/config.yaml
memory:
  memory_enabled: false
user_profile_enabled: false
```

**Do NOT use** `hermes tools disable memory` — that also kills all 23 Mnemosyne-registered tools (the memory toolset gates both built-in AND provider injection).

---

## Mnemosyne Tools (23 total)

| Category | Tools |
|---|---|
| **Core memory** | `remember`, `recall`, `sleep`, `stats`, `get`, `update`, `forget`, `invalidate`, `validate` |
| **Knowledge graph** | `triple_add`, `triple_query`, `graph_query`, `graph_link` |
| **Multi-agent** | `shared_remember`, `shared_recall`, `shared_forget`, `shared_stats` |
| **Working notes** | `scratchpad_write`, `scratchpad_read`, `scratchpad_clear` |
| **Ops** | `export`, `import`, `diagnose` |

All surfaced through Hermes' tool system automatically when provider is active.

---

## Troubleshooting Checklist

- [ ] `mnemosyne-memory` importable in Hermes venv: `/usr/local/lib/hermes-agent/venv/bin/python -c "import mnemosyne; print(mnemosyne.__version__)"`
- [ ] `mnemosyne-hermes` importable in pipx venv
- [ ] Symlink exists: `ls -la ~/.hermes/plugins/mnemosyne`
- [ ] `hermes memory status` shows Provider: mnemosyne, Plugin: installed ✓
- [ ] Built-in memory disabled: `memory.memory_enabled: false`, `user_profile_enabled: false`
- [ ] Gateway restarted after config change