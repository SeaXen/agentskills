# Hermes config corruption — 2026-07-08 incident transcript

Real failure mode captured 2026-07-08 (Asia/Dhaka). Use this to recognize the
same pattern in future logs and to validate the recovery procedure.

## Symptom chain

1. `hermes update` runs (or partial write of `~/.hermes/config.yaml` happens).
2. `config.yaml` is truncated or partially written.
3. `yaml.safe_load()` fails on parse.
4. **Hermes gateway silently falls back to `.env` / `gateway.json`** — service stays running.
5. Cron jobs that depend on `config.yaml` start failing:
   - `RuntimeError: Cron job '...' has no model configured (job.model=None, HERMES_MODEL='', config.yaml model.default missing or empty)`
6. User only notices when dashboard auth stops working, approvals get stuck, or a custom provider disappears.

## Log signature — what to grep for

```bash
# The primary indicator: continuous parse failures in agent.log
grep 'WARNING gateway.config: Failed to process config.yaml' /root/.hermes/logs/agent.log

# Secondary: cron jobs failing with "no model configured"
grep 'has no model configured' /root/.hermes/logs/agent.log

# Tertiary: the moment of corruption (search for the last successful parse)
grep -nE 'Failed to parse.*config.yaml|yaml|YAML' /root/.hermes/logs/agent.log | tail -50
```

The first parse failure timestamp is the upper bound for when the corruption happened.
Look 1-2 hours before that for `hermes update` activity in `hermes-update.log`.

## 2026-07-08 timeline (reconstructed)

| Time | Event |
|------|-------|
| 2026-07-06 10:43:19 | Last successful `hermes update` (logged in `hermes-update.log`) |
| 2026-07-07 evening | Unclear what happened — no log entry |
| 2026-07-08 00:00:37 | First parse failure logged in `agent.log` |
| 2026-07-08 03:00, 04:00 | Cron jobs start failing for "no model configured" |
| 2026-07-08 08:39:52 | `hermes_cli.backup` auto-creates `state-snapshots/20260708-023930-pre-update/` |
| 2026-07-08 ~10:18 | User reports dashboard 9119 not opening |

## The pre-update snapshot trap

`/root/.hermes/state-snapshots/<ts>-pre-update/config.yaml` exists but is **NOT a
usable restore source**. On 2026-07-08 it contained only:

```yaml
model:
  provider: openai-codex
  default: gpt-5.4
_config_version: 33
agent: {}
```

That's Hermes's minimal-template fallback. **The auto-snapshot captured the
already-broken state, not the pre-corruption state.** Hermes's snapshot tool
either runs AFTER the corruption lands or uses the same broken in-place write.

This is why this skill keeps its own `snapshots/updates/` tree in git — it
snapshots BEFORE invoking the update.

## Drift observed between backup and broken state

`/mnt/tb/hermes-backups/#plain/hermes-plain-2026-07-08_06-00/config.yaml` (working,
1982 bytes of valid YAML through `session_reset`, then malformed tail) versus
the broken `/root/.hermes/config.yaml` (also minimal-template, identical
1982 bytes of stub content).

Full drift between this backup and the eventual restored state:

| Field | Backup | Restored |
|---|---|---|
| `approvals.mode` | `smart` | `smart` (restored) |
| `command_allowlist` | populated | populated (restored) |
| `dashboard.basic_auth.username` | `sagar` | `sagar` (kept) |
| `dashboard.basic_auth.password_hash` | old hash | new hash (kept per user) |
| `dashboard.basic_auth.secret` | `''` | non-empty (set so login works) |
| `dashboard.basic_auth.session_ttl_seconds` | `86400` | `86400` (restored) |
| `model.default` | `gpt-5.4` | `kimchicombo` (kept — user's active model) |
| `model.provider` | `openai-codex` | `custom:9router` (kept) |
| `API_SERVER_KEY` | `3a0963dc...2635` | `opop@9900` (kept — user-rotated) |
| `session_reset.mode` | `none` | `none` (unchanged — do not touch) |
| `hooks_auto_accept` | `false` | `false` (unchanged — do not touch) |
| Custom providers (Bynara, OmniRoute, 9router, ...) | populated | populated (restored) |

## Recovery procedure (worked on 2026-07-08)

```bash
# 1. Identify the most recent WORKING backup
ls -ld /mnt/tb/hermes-backups/#plain/hermes-plain-*/config.yaml | tail -5

# 2. Splice backup head + current valid tail
cp -a /root/.hermes/config.yaml /root/.hermes/config.yaml.pre-restore-$(date +%s)
# ... splice with python (see hermes-dashboard-restore skill) ...

# 3. Re-pin any new credentials that the splice dropped
hermes config set dashboard.basic_auth.password_hash '<new-hash>'
hermes config set dashboard.basic_auth.secret '<32-byte hex>'

# 4. Verify
hermes config check
sudo systemctl restart hermes-dashboard.service

# 5. Take a fresh baseline mirror so the drift-watchdog starts clean
/root/.hermes-config-snapshots/scripts/snapshot-all.sh
```

Total time to recovery: ~3 minutes once you know the procedure.

## Why this incident pushed the silent-corruption safety net into the skill

Before this incident, the snapshot pipeline was a 6h "nice to have". After, it's
a 4-layer mandatory safety net:

1. **Pre-flight YAML check** on every `hermes update` (refuses to update if config is already broken)
2. **Pre-update snapshot** to git (captured BEFORE the update, not after)
3. **Post-flight YAML check** (warns if update broke config)
4. **30-min YAML lint watchdog** (catches silent fallback within 30 minutes)
5. **6h drift watchdog** (catches silent reverts within 6 hours)

Without layers 4-5, the user only finds out hours later when something
downstream breaks. With them, the failure surfaces on Discord within an hour.

## Lessons (encoded in SKILL.md)

- `state-snapshots/<ts>-pre-update/` is **not** a reliable restore source. Always have an external snapshot that captures BEFORE the update runs.
- `hermes config check` should be the first thing you run after any `hermes update`, not the last.
- The drift-watchdog false-positive after a restore is easy to forget — take a fresh baseline mirror immediately after any manual restore.
- The 6h cadence for snapshots is also a natural cadence for drift detection. Same threshold logic, same Discord channel, same failure-only delivery.
