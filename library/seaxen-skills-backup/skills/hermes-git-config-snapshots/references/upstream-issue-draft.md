# Upstream issue draft — Hermes config silent corruption

Draft issue text for filing against `hermes-agent` upstream. Includes
reproduction, evidence, and 5 proposed fixes with code snippets.

---

## Title

`hermes-agent: config.yaml silently corrupted after update — propose atomic write + pre-update config backup`

## Body

### Summary

On 2026-07-08, an automatic or manual `hermes update` produced a malformed `~/.hermes/config.yaml`. The gateway failed to parse it (error: "while parsing a block mapping") and silently fell back to `.env` / `gateway.json` values. The user noticed only because the dashboard 9119 login stopped accepting the password and `approvals.mode` had silently flipped from `smart` → `manual`.

### Reproduction

1. Start with a working `config.yaml` (~35KB with custom providers, `command_allowlist`, profile-specific overrides).
2. Run `hermes update` (any recent version — observed on 0.18.0 → 0.19.x transition).
3. Inspect `~/.hermes/config.yaml` — file is truncated to 1982 bytes containing only:
   ```yaml
   model:
     provider: openai-codex
     default: gpt-5.4
   _config_version: 33
   agent: {}
   ```
4. Hermes gateway continues running but logs a constant stream of:
   ```
   WARNING gateway.config: Failed to process config.yaml — falling back to .env / gateway.json values.
   ```
5. Cron jobs that depend on `config.yaml` start failing with `RuntimeError: Cron job '...' has no model configured`.

### Evidence

- `~/.hermes/state-snapshots/20260708-023930-pre-update/config.yaml` — 1982 bytes, minimal template, captured at update time but only after the corruption had already occurred.
- `~/.hermes/logs/agent.log` — first parse failure at `2026-07-08 00:00:37,977 WARNING gateway.config`, then continuous failures every ~10s.
- `~/.hermes/logs/hermes-update.log` — last successful update at `2026-07-06 10:43:19`. No record of an update between then and 2026-07-08 08:39:52.

### Root cause analysis

`config.yaml` is written via in-place edit (likely `Path.write_text` or `f.write()` on the open file). When the write is interrupted — disk full, OOM kill, signal during a long write, partial backup restore — the file is left truncated. The YAML parser then fails on the truncated content.

The pre-update snapshot exists in `state-snapshots/20260708-023930-pre-update/` but only contains the *post-corruption* file (1982 bytes) — meaning the snapshot is captured AFTER the config was already broken.

### Proposed fixes (priority order)

#### 1. Atomic config writes (highest priority)

Replace any in-place write of `config.yaml` with the standard temp-file + atomic rename pattern:

```python
# Bad (current):
with open(config_path, "w") as f:
    f.write(new_content)

# Good (proposed):
import os
tmp = config_path + ".tmp"
with open(tmp, "w") as f:
    f.write(new_content)
    f.flush()
    os.fsync(f.fileno())
os.replace(tmp, config_path)  # atomic on POSIX
```

`os.replace()` is atomic on POSIX systems, so readers either see the old file or the new one — never a half-written file.

Applies to:
- `hermes config set <key> <value>`
- `hermes update` (config merge on update)
- Any plugin / dashboard write path

#### 2. Pre-update config backup (second priority)

The snapshot at `~/.hermes/state-snapshots/<ts>-pre-update/` should contain the user's full, working config — not the broken residual. Capturing it via in-place `cp` is fine; the issue is the captured file should not be re-saved over by the update logic before being archived.

Currently `state-snapshots/<ts>/config.yaml` shows the post-corruption 1982-byte state, meaning either:
- The snapshot is captured AFTER the update corrupts the file (raced)
- The snapshot is captured BEFORE the update but the update's "merge" path writes a minimal stub which the next snapshot then captures

Either way, the user has no way to recover their full config from the auto-snapshot.

#### 3. Surface config-parse failures to the user

Currently a malformed `config.yaml` produces only WARNING logs and a silent fallback. The user only notices when something breaks downstream (auth, approvals, cron jobs). Suggested:

- On config parse failure, write a banner to the gateway's `/healthz` or `/status` endpoint.
- Log the parse error to `~/.hermes/logs/config-errors.log` with full context.
- Optionally, emit a one-time desktop notification or webhook if `notif.*` is configured.

#### 4. Make `hermes-update.log` immutable / append-only

The log is currently a regular file in `~/.hermes/logs/hermes-update.log`. If the updater crashes mid-run, the log may also be truncated. Consider:
- Always append, never truncate
- Pre-update: rename `hermes-update.log` → `hermes-update-<ts>.log` and start fresh
- This guarantees the log of every update survives

#### 5. yaml.safe_load round-trip in `hermes config check`

Make `hermes config check` strict:

```python
import yaml
with open(config_path) as f:
    config = yaml.safe_load(f)
# round-trip: serialize back, parse again, compare
roundtripped = yaml.safe_dump(config)
reparsed = yaml.safe_load(roundtripped)
assert reparsed == config, "config has non-round-trippable structure"
```

### Workaround until these are merged

External wrapper at `https://github.com/SeaXen/hermes-snapshots`:
- Snapshots the FULL config to git BEFORE every `hermes update`
- Lints the config before allowing the update to proceed
- Watches for silent drift via 6h diff against the last-known-good mirror
- Posts to Discord on corruption events

Happy to upstream any of those scripts if useful.

### Environment

- `hermes-agent` 0.18.0 (observed)
- Linux 6.12.94+deb13-amd64
- `~/.hermes/config.yaml`: 35KB before, 1982 bytes after
- Gateway: `python /usr/local/lib/hermes-agent/hermes_cli/main.py gateway run`
- Update command: `hermes update`

### Impact

This is a **silent total-loss-of-customization** bug. Users who run `hermes update` may lose:
- Custom providers
- `approvals.mode` and `command_allowlist`
- Dashboard auth credentials
- Profile-specific overrides
- All local comments

…without any error surfaced to them. Recovery requires either an external backup or manual restoration from memory.
