---
name: hybrid-memory-systems
description: Design, install, and verify layered memory stacks where Hermes remains the operator interface, hot memory stays separate, and a deep knowledge brain like GBrain is added without collapsing responsibilities.
---

# Hybrid Memory Systems

## When to use
- The user wants Hermes to stay the primary interface but add a deeper knowledge system.
- The stack mixes hot prompt-proximal memory and long-form knowledge storage.
- You are wiring Hermes to an external brain over MCP/CLI instead of replacing Hermes memory outright.
- You need to install or rescue a Hermes + Mnemosyne + GBrain style layered setup.
- **You want to install a competing plugin (e.g. hermes-hybrid-memory) without disturbing the active Mnemosyne provider** — see "Parallel memory plugin install" below.

## Core rule: strict ownership
Do not blur the layers.

- **Hermes**: control plane, tools, sessions, user interaction, orchestration.
- **Mnemosyne / hot memory**: compact durable facts, preferences, operator context, prompt-time recall.
- **MnemoSync / sync layer**: replication of the hot-memory layer across machines.
- **GBrain / deep brain**: long-form project pages, people/companies/concepts, graph-linked knowledge, curated notes.

If you let two layers own the same job, the system degrades into duplication and operator confusion.

---

## Parallel memory plugin install (3-option matrix)

Hermes has a single memory-provider slot. Plugins like `hermes-hybrid-memory` want to occupy it. When the slot is already taken (almost always — Mnemosyne), present this matrix and let the user choose:

| | **Option 1 — Replace** | **Option 2 — Parallel side-tool** | **Option 3 — Defer** |
|---|---|---|---|
| Config change | `provider: <plugin>` + full `plugins.<plugin>.*` block | None (plugin present, inert) | None at all |
| Active provider | Plugin | Stays as before | Stays as before |
| Auto-injects into conversations | ✅ Yes | ❌ No | ❌ No |
| Standalone scripts available | ✅ | ✅ | ✅ (after install) |
| Auto-prefetch / analogy / cron | ✅ | ❌ | ❌ |
| Risk to existing memory | High | **Near zero** | Zero |
| Reversibility | Flip one config value | `rm -rf` the plugin folder | n/a |
| **Best when** | "I want plugin X to be my memory" | "Keep current provider, just give me the toolkit" | "Save the skill for later" |

### User preference — default to Option 2

Dr. Sagar explicitly chose Option 2 for hermes-hybrid-memory (twice confirmed). For any future plugin that competes with the active Mnemosyne provider, **default to presenting the matrix with Option 2 highlighted**. Always verify the active provider with `grep -A 2 "^memory:" /root/.hermes/config.yaml` first.

### Naming clarity — Mnemosyne vs MnemoSync vs hybrid vs memstore

These get conflated. The differences matter:

| Name | What it is | Install posture |
|---|---|---|
| **Mnemosyne** | Hermes memory plugin; active provider on this host | Default — already active |
| **MnemoSync** | Cross-host sync daemon between Mnemosyne instances | Not installed here |
| **hermes-hybrid-memory** | Concrete MemoryProvider plugin (one SQLite file) | Drop-in as Option 2 |
| **GBrain** | Long-form knowledge brain, separate from Hermes | Layered topology |
| **Mnemosyne vendor DB** | Stock DB inside the hermes-mnemosyne plugin package | Reference only — NOT your memory |
| **Mnemosyne live DB** | The user's real, active memory | Do not touch |

When the user says "MnemoSync" they almost always mean the active Mnemosyne provider. Confirm with `grep config.yaml` once, then proceed without pedantry.

### Concrete Option 2 install steps

Full procedure in `references/parallel-memory-plugin-install.md`. Short version:

```bash
# 1. Install Python deps into the hermes-agent venv (PEP 668 safe)
uv pip install --python /usr/local/lib/hermes-agent/venv/bin/python <deps>

# 2. Drop plugin into plugins/<name>/ (NOT activated)
mkdir -p /root/.hermes/plugins/<name>
cp plugins/<name>/__init__.py /root/.hermes/plugins/<name>/
cp plugins/<name>/plugin.yaml /root/.hermes/plugins/<name>/

# 3. Drop scripts into scripts/ (defensive: back up conflicts first)
for f in <list>; do
  [ -f "/root/.hermes/scripts/$f" ] && \
    cp "/root/.hermes/scripts/$f" "/root/.hermes/scripts/${f}.pre-<name>-$(date +%Y%m%d-%H%M%S)"
done
cp scripts/*.py /root/.hermes/scripts/

# 4. Verify mnemosyne + config still untouched
grep -A 2 "^memory:" /root/.hermes/config.yaml
ls -la /root/.hermes/mnemosyne/data/mnemosyne.db

# 5. Run the plugin's own test suite via sparse hermes-agent clone
rm -rf /tmp/hermes-agent-sparse
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/NousResearch/hermes-agent.git /tmp/hermes-agent-sparse
cd /tmp/hermes-agent-sparse && git sparse-checkout set agent
cd - && HERMES_HOME=/tmp/test-home PYTHONPATH=<plugin>/scripts:/tmp/hermes-agent-sparse \
  /usr/local/lib/hermes-agent/venv/bin/python -m pytest <plugin>/scripts/tests/ -q
```

### Pitfalls (verified on 2026-07-11 install)

1. **Don't `cp scripts/*.py` blindly** — always check name collisions first
2. **Don't trust the active provider name from memory** — `grep config.yaml` first; user said "MnemoSync" when the active provider was `mnemosyne`
3. **Don't apply the activation patch** under Option 2 (e.g. `cron-memory-opt-in.diff` only matters when activated)
4. **Don't add the `plugins.<name>.*` block** under Option 2 — implies activation intent
5. **Don't forget PEP 668** — install into the hermes-agent venv, not system Python

---

## Recommended execution order (layered topology)
1. Confirm the role split first.
2. Install the deep brain locally in an isolated home/data path.
3. Verify the deep brain works **standalone** before touching Hermes MCP.
4. Register it into Hermes as an MCP server only after standalone commands succeed.
5. Verify both planes separately:
   - direct deep-brain CLI access
   - Hermes MCP registration and process startup
6. Only then worry about embeddings, rerankers, or richer retrieval.

## Good default topology
For a single main box:
- Hermes local
- Mnemosyne local
- MnemoSync as needed for replication
- GBrain local with its own home and repo paths

For a split topology:
- Hermes + hot memory on the user-facing box
- GBrain on a stable host/VPS if the corpus grows or background jobs matter more than local simplicity

## Practical install pattern for GBrain-style deep brains
Use a wrapper, not a naked binary invocation, when the brain needs a dedicated home and provider env.

Wrapper responsibilities:
- export a fixed home path (for example `GBRAIN_HOME=...`)
- load provider secrets from the real credential plane used by Hermes if child processes do not inherit them
- `cd` into the app repo if the CLI expects repo-relative execution
- exec the real CLI entrypoint

This avoids a common failure mode where the brain works in one shell but not when launched by Hermes/MCP.

## MCP integration rule
Prefer a tiny wrapper script as the MCP command target.

Why:
- keeps YAML simple
- avoids arg quoting drift
- gives one place to export env and working directory
- makes restarts reproducible

Typical shape:
- Hermes MCP server command points to `run.sh`
- `run.sh` sets env and executes `gbrain serve`

## Verification checklist
### Standalone deep-brain checks
- version command works
- config shows the intended home/database/model settings
- sync/import works against the intended repo
- page listing works
- fetching a known page works

### Hermes-side checks
- `hermes mcp list` shows the server enabled
- the MCP watchdog/process is actually running
- the MCP wrapper can start without immediate stderr
- after import, the deep brain still answers direct CLI requests
- if there are multiple installed CLI paths, verify the exact launcher path Hermes uses, not just whichever `gbrain` binary is first on `$PATH`

## Important pitfalls
### 0. Source-tree CLI vs installed binary drift
For repo-driven brains, do not assume the global `gbrain` binary and the source-tree CLI resolve the same config plane or embedding settings.

Observed durable pattern:
- `gbrain` from the global install can resolve stale config/model state
- `/root/.bun/bin/bun run src/cli.ts ...` inside the checked-out GBrain repo can resolve the intended shared-home state correctly

Fix pattern:
- verify both `config show` and a real operation (`embed`, `stats`, `serve`) through the exact path Hermes will use
- for wrappers and launchers, prefer the repo CLI if that is the known-good path
- standardize both the MCP wrapper and the HTTP/admin launcher on the same CLI path, same `GBRAIN_HOME`, same DB env, and same embedding env so Hermes and the dashboard stay on one brain

This is not a generic claim that the global binary is bad. It is a verification rule: when behavior differs, trust the path that matches real operations on the target shared brain and use that exact path everywhere.

### 1. Child-process env drift
A provider key may exist for Hermes yet still be absent for subprocesses launched through MCP or wrappers.

Fix pattern:
- load the key from the actual Hermes credential file/plane inside the wrapper
- export it before execing the deep-brain CLI
- when the brain also needs its own DB env (for example Postgres container credentials), source both the brain-specific env file **and** `~/.hermes/.env` inside every launcher/wrapper that starts GBrain
- after fixing env propagation, re-test the failing path (`sync`, `embed --all`, HTTP admin startup) so you can separate missing-env failures from real upstream quota/key failures

Do not assume the current shell env equals the MCP subprocess env.

### 1b. PGLite split-brain to shared Postgres cutover
If Hermes MCP and the HTTP/admin dashboard both need to see the same GBrain content live, do not leave them on separate long-lived PGLite homes. That only avoids lock contention by splitting visibility.

Preferred cutover pattern:
- create one dedicated Postgres-backed GBrain home
- point both the Hermes MCP wrapper and the HTTP/admin launcher at that same home/database
- keep the old PGLite homes as backup only until verification is complete
- stop the old serve/watchdog processes before comparing old and new brains, otherwise PGLite lock timeouts hide the real data check
- compare `stats` and `list` on the old homes against the new shared brain before declaring success
- re-sync repo content into the shared brain, then re-run extraction/embedding as separate verification steps

This preserves a single deep-brain surface while avoiding PGLite multi-process lock conflicts.

### 1c. Postgres embedding-model cutover is a schema migration, not a normal config toggle
On Postgres-backed GBrain homes, `embedding_model` and `embedding_dimensions` are schema-sizing fields. `gbrain config set embedding_model ...` can be refused or become a no-op because the vector column width has to match the embedding model.

Fix pattern:
- treat embedding-provider/dimension changes as a migration
- if the target brain has no embeddings yet, you can do the minimal safe path:
  1. drop the embedding index
  2. set `embedding = NULL, embedded_at = NULL`
  3. alter `content_chunks.embedding` to the new `vector(N)` width
  4. recreate the HNSW index
  5. update the effective config plane used by the real launcher path
  6. run a real embed command and verify `Embedded:` rises in `stats`
- do not stop at editing one config file; verify the active CLI path sees the new model/dimensions with `config show`
- if `config show` and the database schema disagree, resolve that before re-embedding
- if the repo CLI and the globally installed `gbrain` command disagree, trust the path that passes real operations (`config show`, `embed`, `serve`) on the target shared brain and standardize wrappers/launchers on that path
- after the migration, retest both the MCP wrapper and the HTTP/admin launcher so they inherit the same embedding backend env (for example `OLLAMA_BASE_URL`)

Minimum proof is not "config edited"; it is a successful embed run plus `stats` showing non-zero embedded chunks.

### 1d. Post-cutover housekeeping: remove stale active-looking homes and launchers
After moving from split PGLite homes to one shared Postgres-backed home, do not leave the old homes sitting beside the live home with active-looking names.

Fix pattern:
- verify no live launcher/watchdog/process still points at the old homes
- search launchers and notes for stale references (common leftover: an old localhost-only dashboard script)
- move superseded homes into an archive path outside the active namespace, for example `/mnt/tb/1Apps/GBrainBackups/<date>/...`
- leave a short README in the archive root explaining that these are historical backups only
- update any remaining launcher so every live entrypoint points at the shared home
- verify the top-level app directory now shows only the shared live home plus the archive root, not multiple active-looking homes

This reduces operator confusion and prevents a future session from accidentally reviving an obsolete PGLite home.

### 2. Deferred embedding flags can survive reinit
If a deep brain was first initialized in `no-embed`/deferred mode, a persisted flag like `embedding_disabled: true` can keep reinit on the deferred path even when you later pass an embedding model.

Fix pattern:
- inspect config after reinit if behavior looks wrong
- remove the stale deferred flag
- rerun reinit explicitly with the intended embedding model/dimensions

### 3. PGLite locks are often held by the live serve/MCP process
If sync/import times out waiting for a PGLite lock, inspect for the already-running serve process first.

Fix pattern:
- look for the MCP watchdog / brain serve process
- stop that process temporarily
- run sync/import
- let Hermes reconnect/start it again

Do not treat lock timeouts as a content problem first.

### 4. In-gateway Hermes sessions cannot safely restart the gateway
A gateway restart invoked from inside the running gateway session can be blocked or self-terminate.

Fix pattern:
- first check whether the MCP server is already loaded
- prefer verification via `hermes mcp list` and running processes
- if a true restart is required, run it from a separate shell/session outside the live gateway-controlled session

### 5. Separate "local setup works" from "provider quota works"
A valid integration can still fail to embed because the upstream provider key is rate-limited, over quota, or capped.

Treat these as different states:
- local installation/configuration state
- external provider billing/quota state

Report them separately.

### 6. Embeddings working does NOT mean fact extraction/chat enrichment is working
In GBrain, the embedding path and the chat-gateway path are separate.

Observed durable pattern:
- local/vector retrieval can be healthy after switching to a local embedding backend (for example Ollama `nomic-embed-text`)
- commands like `extract-conversation-facts` can still fail with `Chat gateway unavailable`
- that failure is about the chat model/provider path used by extraction, not about pgvector, not about embeddings, and not about Mnemosyne

Fix/verification pattern:
- verify embeddings with a real `embed` run plus `stats` showing non-zero `Embedded:`
- verify the chat-enrichment path separately with the exact extractor command you care about
- source the same provider env plane used by Hermes when testing extractor commands
- report the split state plainly: "embeddings fixed, fact extraction still blocked by chat gateway config" if that is the truth

Do not imply that a healthy vector index means all higher-level GBrain enrichment flows are operational.

## Operating advice for this user style
- Report exact paths and whether Hermes is truly connected.
- Do not claim the stack is complete if embeddings are blocked by provider limits.
- Mark the stack usable when MCP + import + direct retrieval work, even if semantic embedding is still pending.
- Be explicit about what is locally fixed vs externally blocked.

## Minimum success definition
A hybrid memory install counts as operational when all of these are true:
- Hermes remains the primary interface
- the deep brain is installed in its own isolated home/data paths
- Hermes has a live MCP entry for the deep brain
- curated repo content imports successfully
- a known page can be retrieved directly

Embeddings improve the system, but lack of embeddings due to external quota does not erase a correct local install.

## Support files
- `references/gbrain-hermes-hybrid-session-notes.md` — concrete failure modes and fixes observed during a real Hermes + GBrain hybrid setup.
- `references/gbrain-postgres-embedding-cutover.md` — exact Postgres + Ollama embedding cutover notes: schema resize, repo-CLI verification, and wrapper alignment.
- `references/curated-gbrain-memory-bridge.md` — selective Mnemosyne→GBrain mirroring pattern: local source files, rerunnable sync script, silent cron maintenance, and the rule to leave MnemoSync alone unless explicitly requested.
- `references/parallel-memory-plugin-install.md` — the 3-option matrix (Replace / Parallel / Defer) when installing a plugin that competes with the active Mnemosyne provider. Full Option 2 install + verification procedure, naming clarity (Mnemosyne vs MnemoSync vs hybrid vs memstore), PEP-668-safe Python dep install path, sparse-clone hermes-agent smoke test pattern.
