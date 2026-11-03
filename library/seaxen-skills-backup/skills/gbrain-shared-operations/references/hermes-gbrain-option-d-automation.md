# Hermes + GBrain Option D — hands-off brain growth

Use when the operator wants GBrain to grow **without manual `put_page` every session**: repo files auto-import, Mnemosyne facts curated into daily pages, and upstream autopilot maintains embed/extract/purge.

**Prerequisite:** shared Postgres topology + `gbrain-shared` wrapper (see `shared-gbrain-operator-pattern.md`). Do **not** touch Mnemosyne/MnemoSync internals — only a read-only digest script.

## The three layers

| Layer | What | Token cost |
|-------|------|------------|
| **A — sync watch** | `sync --watch` on the brain repo | **0** chat tokens; Ollama embed only |
| **B — Mnemosyne digest** | Nightly page `inbox/digest-YYYY-MM-DD` | **0** (script + `gbrain put`, no LLM) |
| **C — autopilot** | `gbrain autopilot --install` maintenance cycles | **0** for sync/embed/extract/purge; dream/synthesize only if a chat API is configured |

Mnemosyne and Hermes sessions **do not** flow into GBrain by default. Option D is the official-style automation stack on top of the shared brain.

## Critical pitfall: stale `/usr/local/bin/gbrain`

Autopilot's generated wrapper calls `which gbrain`. If that shim still sets `GBRAIN_HOME` to an old **PGLite** home while MCP uses **GBrainHome-shared**, sync/autopilot write to the wrong brain.

**Fix:** make the global shim delegate to the verified wrapper:

```bash
#!/usr/bin/env bash
exec /usr/local/bin/gbrain-shared "$@"
```

Verify both paths agree:

```bash
gbrain config show      # must show engine: postgres + shared DB
gbrain-shared config show
```

## A — systemd sync watch (this host)

```ini
# /etc/systemd/system/gbrain-sync-watch.service
[Service]
ExecStart=/bin/bash -lc 'set -a; source .../postgres.env; source /root/.hermes/.env; set +a; \
  export GBRAIN_DATABASE_URL=... OLLAMA_BASE_URL=http://127.0.0.1:11434/v1; \
  exec /usr/local/bin/gbrain-shared sync --watch --interval 90 \
    --repo /mnt/tb/1Apps/GBrain-Repo --no-pull'
Restart=always
```

```bash
systemctl enable --now gbrain-sync-watch.service
tail /var/log/gbrain-sync-watch.log
```

Postgres brains can run watch alongside `gbrain serve` (per-source locks). Prefer `--no-pull` when the repo is local-only.

## B — Mnemosyne digest (Hermes cron)

**Script:** `~/.hermes/scripts/mnemosyne_to_gbrain_digest.py`

- Reads `working_memory` from Mnemosyne SQLite (importance ≥ 0.5, last 24h default).
- Redacts secrets; upserts `inbox/digest-YYYY-MM-DD` via `gbrain-shared put`.
- Content-hash skip → silent exit when unchanged (good for `no_agent` cron).

**Cron shape:**

```yaml
schedule: "0 3 * * *"
script: mnemosyne_to_gbrain_digest.py
no_agent: true
deliver: origin   # only posts when stdout non-empty
```

Remove duplicate mirror jobs (e.g. a second job running the same script every 12h).

One-shot static curated pages can stay in `sync-hermes-memory-mirror.sh`; the digest is the **time-varying** bridge.

## C — autopilot

```bash
/usr/local/bin/gbrain-shared autopilot --install \
  --repo /mnt/tb/1Apps/GBrain-Repo \
  --target linux-systemd
loginctl enable-linger root   # if running as root user unit
systemctl --user enable --now gbrain-autopilot.service
```

Logs: `~/.gbrain/autopilot.log`. Worker runs sync/embed/extract/orphans/purge on cycle.

`autopilot --status` may report "not installed" while the user unit is active — trust `systemctl --user is-active` and the log tail.

## Verification checklist

```bash
systemctl is-active gbrain-sync-watch.service
systemctl --user is-active gbrain-autopilot.service
gbrain-shared stats                    # page/chunk counts rise after repo edits
python3 ~/.hermes/scripts/mnemosyne_to_gbrain_digest.py
gbrain-shared get inbox/digest-$(date +%F)   # CLI get, not MCP name
```

Hermes still reads/writes live brain via **GBrain MCP** (`put_page`, `search`, etc.). Option D keeps the **store** fresh; it does not replace MCP as the agent interface.

## Operator framing (user asked for no paid tokens)

- Storage, sync, local embeddings, digest script: **no chat API spend**.
- Tell the user honestly: GBrain is not "learning the whole repo into Hermes memory" — the **repo is an input format** for `sync`; curated pages + digest are the human-visible growth.