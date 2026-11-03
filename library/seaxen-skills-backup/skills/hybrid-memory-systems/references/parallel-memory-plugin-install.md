# Parallel memory plugin install — when the active provider slot is taken

Hermes Agent has a single memory-provider slot in `config.yaml`:

```yaml
memory:
  provider: <one of: mnemosyne | hybrid | default | ...>
```

Many interesting plugins (e.g. `sheldon904/hermes-hybrid-memory`) **want** to be the active provider. But users often have a working setup they don't want to disturb. The matrix below covers every sane install posture so the next "do I install this plugin?" question gets answered without the user having to think about it.

---

## The 3-option matrix

| | **Option 1 — Replace** | **Option 2 — Parallel side-tool** | **Option 3 — Defer** |
|---|---|---|---|
| Config change | `provider: <plugin>` + full `plugins.<plugin>.*` block | None (plugin present in `$HERMES_HOME/plugins/<name>/`, inert) | None at all (don't install yet) |
| Active provider | Plugin | Stays as before (e.g. mnemosyne) | Stays as before |
| Plugin auto-injects into conversations | ✅ Yes | ❌ No | ❌ No |
| User can run plugin scripts standalone | ✅ | ✅ | ✅ (after install) |
| Auto-prefetch / analogy slot / cron jobs | ✅ | ❌ | ❌ |
| Risk to existing memory | High — new provider takes over, old one stops receiving writes | **Near zero** — plugin file sits there | Zero |
| Reversibility | Flip one config value | `rm -rf` the plugin folder | n/a |
| **Best when** | User says "I want plugin X to be my memory" | User says "keep current provider, just give me the toolkit" | User says "save the skill for later, don't install yet" |

---

## How to present this to the user

When asked "should I install plugin X?" and X would compete with the active provider:

1. **First verify which provider is active** — `grep -A 2 "^memory:" /root/.hermes/config.yaml`. Do not assume.
2. **State the matrix above in one short reply.** Don't ask "which option?" first — show all three.
3. **Highlight the user's likely default** (Option 2 for Dr. Sagar — see user-pref below).
4. **Wait for the user's choice** before doing anything.

---

## Option 2 install — concrete steps (the safe default)

Verified working pattern from hermes-hybrid-memory install on 2026-07-11.

### 1. Install Python deps into the Hermes venv

```bash
uv pip install --python /usr/local/lib/hermes-agent/venv/bin/python <deps>
```

The PEP-668-safe path. Don't try `pip install --user` or `apt install`.

### 2. Drop the plugin into `$HERMES_HOME/plugins/<name>/` (NOT activated)

```bash
mkdir -p /root/.hermes/plugins/<name>
cp plugins/<name>/__init__.py /root/.hermes/plugins/<name>/
cp plugins/<name>/plugin.yaml /root/.hermes/plugins/<name>/
```

Hermes only loads plugins that are listed under `memory: provider:` or explicitly enabled in the `plugins:` block. A plugin file sitting in `plugins/<name>/` is inert.

### 3. Drop standalone scripts into `$HERMES_HOME/scripts/`

```bash
# Defensive: don't clobber existing scripts with the same name
for f in <list-of-script-names>; do
  if [ -f "/root/.hermes/scripts/$f" ]; then
    cp "/root/.hermes/scripts/$f" "/root/.hermes/scripts/${f}.pre-<name>-$(date +%Y%m%d-%H%M%S)"
  fi
done
cp scripts/*.py /root/.hermes/scripts/
```

### 4. Create supporting dirs

```bash
mkdir -p /root/.hermes/<plugin-spools> /root/.hermes/<plugin-index-dirs>
```

### 5. Verify nothing in the active provider was touched

```bash
# Memory provider block unchanged
grep -A 2 "^memory:" /root/.hermes/config.yaml

# Active provider DB untouched
ls -la /root/.hermes/<provider>/data/<provider>.db
stat -c '%y' /root/.hermes/<provider>/data/<provider>.db   # should predate install

# Active provider's dashboard/process still up (if applicable)
ps auxww | grep -E "<provider>-dashboard" | grep -v grep
```

### 6. Run the plugin's own test suite

```bash
# Use a sparse clone of upstream hermes-agent (only `agent/` package needed)
rm -rf /tmp/hermes-agent-sparse
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/NousResearch/hermes-agent.git /tmp/hermes-agent-sparse
cd /tmp/hermes-agent-sparse && git sparse-checkout set agent

# Then the plugin's pytest against a throwaway HERMES_HOME
HERMES_HOME=/tmp/plugin-test-home \
PYTHONPATH=<plugin>/scripts:/tmp/hermes-agent-sparse \
  /usr/local/lib/hermes-agent/venv/bin/python -m pytest <plugin>/scripts/tests/ -q
```

The sparse-clone trick is the same one the plugin's own `.github/workflows/tests.yml` uses — keeps the test run hermetic, no LLM/network calls, no real `$HERMES_HOME`.

---

## What Option 2 actually gives you (and what you lose)

### You get
- All plugin scripts available to run manually or via cron
- Plugin's own tools (e.g. `brain_viz.py` graph browser for hybrid) accessible
- Plugin's persistence layer (own DB file, isolated from active provider)
- Verification that plugin loads, schema initializes, tests pass
- A safe on-ramp: prove the plugin works before promoting it to Option 1

### You lose
- Auto-injection of plugin memories into every conversation (no prefetch)
- The plugin's headline feature (for hermes-hybrid-memory, that's the Hofstadter analogy slot — only fires inside `prefetch()`)
- Cron-driven enrichment (only fires inside the plugin's own pipeline, which only runs when activated)
- Integration with Hermes's existing memory hooks

---

## When to revisit Option 2 → Option 1

Promote to full activation when:

- [ ] User explicitly says "switch to plugin X" or "activate it now"
- [ ] Plugin's standalone scripts have been used enough to confirm the data shape is right
- [ ] The activation cost (patch + config + dependency on upstream changes) is acceptable
- [ ] A rollback plan exists (just flip `provider:` back)

---

## Pitfalls (verified on 2026-07-11 install)

1. **Don't `cp` blindly into `$HERMES_HOME/scripts/`** — always check for name collisions first. The pre-existing `obsmemory_daily_sync.py` would have been clobbered by `cp scripts/*.py` if a hybrid repo had one with the same name.
2. **Don't trust the active provider name from memory** — always `grep` config.yaml first. User said "MnemoSync" twice in a row; the actual active provider was `mnemosyne`. Different product.
3. **Don't apply the patch** (`cron-memory-opt-in.diff` or similar) under Option 2 — it only matters when activating.
4. **Don't add the `plugins.<name>.*` block** under Option 2 — adding it implies activation intent.
5. **Don't forget the `pip install`** into the hermes-agent venv, not the system Python. PEP 668 will block system installs.

---

## Naming clarity — Mnemosyne vs MnemoSync vs hybrid vs memstore

These all get conflated. The differences matter for install posture:

| Name | What it is | Where it lives | Install posture |
|---|---|---|---|
| **Mnemosyne** | Hermes memory plugin; the active provider on this host | `/root/.hermes/mnemosyne/`, plugin at `/root/.hermes/plugins/mnemosyne/` | Default — already active |
| **MnemoSync** | Cross-host sync daemon between Mnemosyne instances | Separate daemon, not installed here | Not relevant to this host |
| **hermes-hybrid-memory** | Concrete MemoryProvider plugin that absorbs all memory into one SQLite file | `/root/.hermes/plugins/hybrid/`, scripts at `/root/.hermes/scripts/` | Drop-in as Option 2 (current state) |
| **GBrain** | Long-form knowledge brain, deep brain for layered setups | `/mnt/tb/1Apps/GBrain/`, separate from Hermes | Layered topology, not a Hermes provider |
| **Mnemosyne vendor DB** | Bundled stock DB inside the hermes-mnemosyne plugin package | `/root/.hermes/vendor/mnemosyne/data/shared/mnemosyne.db` (466 KB, 45 tables) | Reference only — NOT your active memory |
| **Mnemosyne live DB** | The user's real, active memory | `/root/.hermes/mnemosyne/data/mnemosyne.db` (71 MB, 55 tables) | The one that matters — do not touch |

---

## User preference — Dr. Sagar

Dr. Sagar explicitly chose Option 2 for hermes-hybrid-memory (twice confirmed: "do option 2" after I laid out the matrix). When any future plugin competes with the active Mnemosyne provider, **default to Option 2 unless explicitly told otherwise**. Always present the 3-option matrix so the user can override.

Also: when the user says "MnemoSync" in casual language, they almost always mean the active Mnemosyne provider. Confirm with `grep config.yaml` once, then proceed without pedantry.
