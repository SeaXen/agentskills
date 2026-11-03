---
name: hermes-git-config-snapshots
description: "Version Hermes Agent config.yaml, cron/jobs.json, plugin configs, dashboard themes, profile overrides, and learnables config into a private GitHub repo using a line-based redactor (raw files mode 600 and gitignored). Pair with a 6h cron that posts to Discord only on failure and a pre-update hook that snapshots before any hermes update runs. Use when the user wants git-tracked history of their small Hermes config files, wants to detect config drift after a Hermes update, or asks to back up Hermes config without pulling in the full multi-GB state.db into git. Distinct from hermes-backup-watchers (which archives whole trees to TB/cloud) — this skill is the text-only, git-tracked, redacted, multi-file complement."
version: 1.2.1
author: SeaXen + Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, config, git, github, snapshot, redactor, cron, pre-update, private-repo]
    related_skills: [hermes-agent, hermes-dashboard-restore, hermes-backup-watchers]
---

# Hermes Git Config Snapshots

Keep Hermes Agent's small, committable config files under git so config drift from a Hermes update is detectable, diff-able, and reversible. Distinct from `hermes-backup-watchers` (which archives multi-GB state.db + skills to local TB / cloud): this skill is **text-only, redacted, versioned in a private GitHub repo**, and is meant to complement (not replace) the file-archive backup.

## When to Use

- After a Hermes update wipes or changes config (auth, approvals, command_allowlist, custom providers) and the user wants git history to detect and reverse it.
- The user wants their cron jobs, plugin configs, dashboard themes, and profile overrides version-controlled in a private GitHub repo (not local-only).
- The user wants automatic pre/post snapshots around `hermes update` so they always have a known-good version to restore from.
- The user wants a 6-hourly safety net that pushes to git and only alerts on Discord `#💾│daily-backup` when something breaks.
- User asks if **crons broke config** or if it can **break again** — answer with `references/openrouter-free-watch-config-corruption.md` (cron writer table); keep `hermes-yaml-lint-30m` enabled; note openrouter pre-write YAML gate is still recommended hardening.
- User needs to restore a wiped/minimal `~/.hermes/config.yaml` from `/mnt/tb/hermes-backups/#plain/...` and you must determine which 6-hour snapshot is actually good before copying it back. Use `references/plain-backup-config-restore-triage.md`.

Do NOT use for:
- Backing up `state.db`, `mnemosyne.db`, `*.gguf`, `logs/` — those are large binary blobs and belong in `hermes-backup-watchers` style file archives.
- Single-file `config.yaml` only — use the lighter-weight pattern documented in `references/config-snapshot-to-git.md` inside `hermes-dashboard-restore`.
- Skills authoring — see `hermes-agent` (the bundled skill).

## What Gets Snapshotted (and What Doesn't)

Small, text-only, committable files:

| Path | Source | Treatment |
|---|---|---|
| `~/.hermes/config.yaml` | top-level | redacted; paired with `.raw` (mode 600, gitignored) |
| `~/.hermes/cron/jobs.json` | CRITICAL — your entire automation | redacted for known token prefixes |
| `~/.hermes/profiles/<name>/config.yaml` | per-profile overrides | redacted |
| `~/.hermes/plugins/<name>/plugin.yaml` | plugin manifests | plain — metadata only |
| `~/.hermes/plugins/<name>/config.yaml` | per-plugin config | redacted |
| `~/.hermes/dashboard-themes/*.yaml` | custom themes | plain — CSS, no secrets |
| `~/.hermes/learnables/config.yaml` | learnables workflow | redacted |
| `~/.hermes/profiles/medicine/...` | medicine-profile plugins/skills | redacted |

**Not** snapshotted (too large, belongs in hermes-backup-watchers):

- `state.db` (~2.5 GB), `state.db-wal`
- `mnemosyne/data/mnemosyne.db` (~66 MB)
- `mnemosyne/models/*.gguf` (~1.4 GB)
- `telemetry/telemetry.db`
- `logs/` (rotate)
- Any `*.raw` (real configs, mode 600)

## Architecture

Six layers (first three are mandatory, last three are the safety net that catches silent drift):

1. **Redactor** (`scripts/redact.py`) — line-based. Required because the backup `hermes-plain-*/config.yaml` files are often malformed at the tail and `yaml.safe_load` will fail. Line-based redactor masks values of known secret keys without parsing.
2. **Snapshot scripts** (`scripts/snapshot.sh`, `scripts/snapshot-all.sh`) — copy from live `~/.hermes/...`, run redactor, `git add` + commit + push only if the redacted YAML actually changed (dedup).
3. **Cron + pre-update hook** — `0 */6 * * *` cron calls `snapshot-all.sh`; a shell function in `/etc/profile.d/hermes-pre-update-snapshot.sh` intercepts `hermes update` to capture pre/post snapshots.
4. **YAML lint watchdog** (`scripts/yaml-lint.sh`, cron `*/30 * * * *`) — runs `yaml.safe_load` on `~/.hermes/config.yaml` AND every `profiles/*/config.yaml`. Catches corruption in minutes, not hours.
5. **Drift watchdog** (`scripts/drift-watchdog.sh`, cron `30 */6 * * *`) — compares current `~/.hermes/config.yaml` against the most recent mirror. Alerts if diff > 50 lines. Catches silent reverts (update overwrites custom settings without parse error).
6. **Pre/post-flight YAML check** inside `hermes-update-safe.sh` — refuses to run `hermes update` if config is already broken; warns if update left config malformed.

Full working templates are in this skill's `scripts/`, `templates/`, and `references/` directories. The template layout mirrors the proven implementation at `https://github.com/SeaXen/hermes-snapshots` (private repo).

## Workflow: First-Time Setup

```bash
# 1. Create a private GitHub repo
gh repo create SeaXen/hermes-snapshots --private \
  --description 'Versioned redacted snapshots of Hermes Agent config.yaml'

# 2. Local repo
mkdir -p /root/.hermes-config-snapshots && cd /root/.hermes-config-snapshots
git init -b main
git remote add origin https://github.com/SeaXen/hermes-snapshots.git

# 3. Install the redactor + snapshot scripts
#    (copy templates from this skill's scripts/ to your local repo)

# 4. Initial capture
./scripts/snapshot-all.sh

# 5. Wire the 6h cron (use this skill's templates/cron-snapshot-6h.json)
hermes cron create \
  --name hermes-config-snapshot-6h \
  --schedule "0 */6 * * *" \
  --deliver "discord:<backup-channel-id>" \
  --no-agent \
  --script hermes-snapshot-silent.sh \
  --workdir /root/.hermes-config-snapshots

# yaml-lint cron (script: ~/.hermes/scripts/yaml-lint.sh)
hermes cron create \
  --name hermes-yaml-lint-30m \
  --schedule "*/30 * * * *" \
  --deliver "discord:<backup-channel-id>" \
  --no-agent \
  --script yaml-lint.sh

# drift-watchdog cron (script: ~/.hermes/scripts/drift-watchdog.sh)
hermes cron create \
  --name hermes-drift-watchdog-6h \
  --schedule "30 */6 * * *" \
  --deliver "discord:<backup-channel-id>" \
  --no-agent \
  --script drift-watchdog.sh

# 6. Wire the pre-update hook
# IMPORTANT: do NOT `install` scripts/hermes-update-safe.sh directly to /usr/local/bin —
# that script resolves HERE via $(dirname "$0")/.. and breaks (looks for /usr/local/scripts/snapshot.sh).
# Install the thin launcher from templates/hermes-update-safe-launcher.sh instead.
sudo install -m 0755 templates/hermes-update-safe-launcher.sh /usr/local/bin/hermes-update-safe
sudo install -m 0644 templates/hermes-pre-update-snapshot.sh /etc/profile.d/
# Now `hermes update` in any new login shell will be wrapped automatically.
```

## Workflow: Detect + Reverse Drift After a Hermes Update

```bash
# 1. Diff current config against the most recent pre-update snapshot in the repo
diff -u /root/.hermes-config-snapshots/snapshots/updates/<pre-update-ts>.raw \
        /root/.hermes/config.yaml > /tmp/hermes-drift.diff

# 2. Decide what to restore. Common drift table — see references/config-drift-cheatsheet.md:
#    - approvals.mode smart -> manual  : RESTORE
#    - command_allowlist []              : RESTORE
#    - dashboard.basic_auth.username     : KEEP (user-rotated)
#    - dashboard.basic_auth.password_hash: KEEP (user-rotated)
#    - session_reset.mode                : UNLESS user explicitly asks, do not touch
#    - model.default / model.provider    : KEEP if user switched models intentionally
#    - API_SERVER_KEY                    : KEEP if user rotated

# 3. Splice restore (preserves the new password hash):
cp -a ~/.hermes/config.yaml ~/.hermes/config.yaml.pre-restore-$(date +%s)
python3 <<'PY'
from pathlib import Path
cur = Path('/root/.hermes/config.yaml').read_text().splitlines()
bak = Path('/root/.hermes-config-snapshots/snapshots/updates/<pre-update-ts>.raw').read_text().splitlines()
# backup had valid content through session_reset, then malformed lines.
# Current valid tail starts at API_SERVER_KEY.
Path('/root/.hermes/config.yaml').write_text('\n'.join(bak[:N] + cur[M:]) + '\n')
PY
hermes config set dashboard.basic_auth.password_hash '<new-hash>'
hermes config set dashboard.basic_auth.secret '<32-byte hex>'
hermes config check
sudo systemctl restart hermes-dashboard.service
```

The line-splice pattern (instead of full restore) is documented in `hermes-dashboard-restore` because that's where this pattern originated. Always `cp -a` the current config first so the splice is reversible.

## Line-Based Redactor (Why Not YAML?)

`yaml.safe_load` fails on the malformed backup `hermes-plain-*/config.yaml` files because they have stray lines after `session_reset` (duplicated `api_server_key`, broken `or-auto-...` aliases). A line-based redactor that operates on `key: value` regex matches each line independently, so malformed YAML still gets redacted correctly. The redactor must cover:

- Generic secret keys: `password`, `password_hash`, `secret`, `api_key`, `api_token`, `token`, `client_id`, `client_secret`, `webhook_url`, `drain_secret`, `access_token`, `refresh_token`, `auth_token`, `bearer`, `jwt`, `sig`, `anthropic_api_key`
- Env-var-shaped keys (top-level): anything matching `^[A-Z][A-Z0-9_]+_(KEY|SECRET|TOKEN|PASSWORD)$`
- Known top-level scalars: `API_SERVER_KEY`, `SEARXNG_URL`, `api_server_key`, `ALPHA_VANTAGE_API_KEY`, `COINGLASS_KEY`, `COINMARKETCAP_KEY`, `ARKHAM_API_KEY`, `BRAVE_API_KEY`, `STITCH_API_KEY`
- Value-shape heuristics: any string starting with `sk-`, `gho_`, `om-`, `mnfst_`, `cfut_`, `BSAt...`, `9PPJ...`, `3a09...`, `214b...`, `dbd6...`, `AQ.` → `REDACTED`

The full redactor is in `scripts/redact.py` (template). Run a leak sweep with a long-token regex before each push:

```bash
grep -cE 'scrypt\$16384|sk-3ab|sk-f49|BSAtDfWF|cfut_Wdv|3a0963dc|214b04b732|dbd6c5434|AQ\.Ab8RN6' <redacted.yaml>
# expect: 0
```

## Dedup Logic (No Empty Commits)

`snapshot.sh` should exit with "no snapshot changes since last commit" if `git diff --quiet -- snapshots/` is true after staging. This prevents commit noise when the live config is unchanged. The check happens AFTER the redactor has produced its output but BEFORE `git add`, so a no-op redact still produces no commit.

Critical pitfall: **shell glob expansion can leak ignored raw files**. If raw files are named `*.raw.yaml` and you run `git add snapshots/*.yaml`, the shell expands to BOTH `*.yaml` and `*.raw.yaml`, staging the ignored raw files. Either:

- Name raw files `*.raw` (no `.yaml` extension) and gitignore `*.raw`, OR
- Use `git add snapshots/*/*.yaml` with explicit subdir, OR
- Loop and `git add` only redacted paths.

The templates in this skill use the `*.raw` suffix approach — cleanest.

## Pre-Update Hook (Capture Around `hermes update`)

When a user runs `hermes update`, the live config can change. To always have a known-good version to restore from, intercept the command with a shell function:

```bash
# /etc/profile.d/hermes-pre-update-snapshot.sh
hermes() {
  if [ "${1:-}" = "update" ]; then
    command hermes-update-safe "${@:2}"
  else
    command hermes "$@"
  fi
}
```

The launcher at `/usr/local/bin/hermes-update-safe` (`templates/hermes-update-safe-launcher.sh`) execs `scripts/hermes-update-safe.sh` in the snapshots repo. It then:

1. **Pre-flight YAML check**: refuses to run if `~/.hermes/config.yaml` fails `yaml.safe_load`. Prints the recovery `install -m 600` command using the most recent mirror's `config.yaml.raw`. Exit code `2` distinguishes this from a real update failure.
2. Snapshots current config into `snapshots/updates/<pre-update-ts>` (redacted + raw)
3. Runs the REAL `hermes update` binary (locate via `/usr/local/bin/hermes` / `/root/.local/bin/hermes` — never call `hermes update` recursively inside the wrapper)
4. **Post-flight YAML check**: if update succeeded but config is now malformed, prints the restore command using the pre-update snapshot. Exit code `3` distinguishes this from a real update failure.
5. On success, snapshots again into `snapshots/updates/<post-update-ts>`
6. On failure (update non-zero), prints the exact `install -m 600` command to restore the pre-update snapshot

This works because shell function resolution wins over the binary in `command hermes`. Verified on Hermes Agent v0.18.1.

## YAML Lint Watchdog (`scripts/yaml-lint.sh`)

Hermes silently falls back to `.env` / `gateway.json` when `config.yaml` fails to parse. The user only notices when cron jobs start failing for "no model configured" or dashboard auth stops working — hours after the corruption.

Catches it in minutes. Runs every 30 minutes via cron, alerts Discord `#💾│daily-backup` on failure only.

**Use the tempfile + single-Python-invocation pattern (NOT nested heredocs in a for loop).** Nested `<<PY` heredocs inside a `for` loop under `set -uo pipefail` can corrupt parser state and report spurious `SyntaxError: invalid decimal literal` on configs that parse fine via direct `python3 -c`. Symptom: script reports failure for files that pass `python3 -c 'import yaml; yaml.safe_load(open(...))'`.

```bash
#!/usr/bin/env bash
# Lint main config + every profile config. Silent on success.
set -uo pipefail
HERMES="/root/.hermes"
PY=""
for cand in /usr/local/lib/hermes-agent/venv/bin/python3 /root/.hermes/venv/bin/python3 python3; do
  if command -v "$cand" >/dev/null 2>&1; then PY=$(command -v "$cand"); break; fi
done
[ -z "$PY" ] && PY="python3"

# Build file list into a tempfile (one path per line) — avoid nested heredocs.
FILELIST=$(mktemp)
trap 'rm -f "$FILELIST"' EXIT
{
  [ -f "$HERMES/config.yaml" ] && echo "$HERMES/config.yaml"
  for f in "$HERMES"/profiles/*/config.yaml; do
    [ -f "$f" ] && echo "$f"
  done
} > "$FILELIST"

# Single Python invocation reads file list from $FILELIST, prints alert only on failure.
"$PY" - "$FILELIST" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" <<'PYEOF'
import sys, yaml, glob
files = [line.strip() for line in open(sys.argv[1]) if line.strip()]
ts = sys.argv[2]
errs = []
for f in files:
    try:
        with open(f) as fh: yaml.safe_load(fh)
    except Exception as e:
        errs.append((f, str(e)[:300]))
if errs:
    lines = [f"❌ hermes-yaml-lint FAILED at {ts}", "Files with parse errors:"]
    for f, e in errs:
        lines.append(f"- {f}: {e}")
    mirrors = sorted(glob.glob('/root/.hermes-config-snapshots/mirrors/*/config.yaml.raw'))
    if mirrors:
        latest = mirrors[-1]
        lines.append("")
        lines.append("Recovery:")
        lines.append(f"  sudo install -m 600 {latest} /root/.hermes/config.yaml")
        lines.append("  hermes config check")
        lines.append("  sudo systemctl restart hermes-dashboard.service")
    print("\n".join(lines))
    sys.exit(1)
sys.exit(0)
PYEOF
```

Cron shape: `no_agent=true` with bash script as target. Template at `templates/cron-yaml-lint.sh.txt`.

## Drift Watchdog (`scripts/drift-watchdog.sh`)

YAML parse success ≠ working config. An update can silently revert `approvals.mode: smart` to `manual`, wipe `command_allowlist`, drop custom providers — all while the YAML still parses cleanly.

Catches silent reverts by comparing current config to the most recent 6h mirror. Runs every 6 hours (offset 30 minutes from the snapshot cron), alerts Discord on threshold breach.

```bash
#!/usr/bin/env bash
set -uo pipefail
HERE="/root/.hermes-config-snapshots"   # PIN explicitly — symlinks break $(dirname $0)/..
HERMES="/root/.hermes"
THRESHOLD=${DRIFT_THRESHOLD:-50}
TS=$(date -u +%Y-%m-%dT%H-%M-%S)

PY=$(command -v /usr/local/lib/hermes-agent/venv/bin/python3 2>/dev/null \
     || command -v python3)

# 1. Find latest mirror baseline
LATEST=$(ls -t "$HERE"/mirrors/*/config.yaml 2>/dev/null | head -1)
[ -z "$LATEST" ] && exit 0

# 2. Redact current config to a temp file with AGGRESSIVE 5-pass redaction.
#    Prefix-only redaction leaks bare field names (secret:, password:, token:,
#    hash:, key:) and long hex/base64 strings (dashboard secrets, session
#    cookies). The drift alert is delivered verbatim to Discord — if any
#    redaction pass is missing, secrets end up in the channel.
CUR_TMP=$(mktemp --suffix=.yaml)
trap 'rm -f "$CUR_TMP"' EXIT

"$PY" - "$HERMES/config.yaml" "$CUR_TMP" <<'PYEOF' 2>/dev/null
import sys, re, pathlib

# Pass 1: known secret prefixes
SECRET_PREFIX = re.compile(
    r'(sk-[A-Za-z0-9]{8,}|sk-f49[A-Za-z0-9]+|sk-3ab[A-Za-z0-9]+'
    r'|gho_[A-Za-z0-9]+|om-[A-Za-z0-9]+|mnfst_[A-Za-z0-9]+'
    r'|cfut_[A-Za-z0-9]+|BSAt[A-Za-z0-9]+|9PPJ[A-Za-z0-9]+'
    r'|3a09[A-Fa-f0-9]+|214b[A-Fa-f0-9]+|dbd6[A-Fa-f0-9]+'
    r'|AQ\.[A-Za-z0-9]+|scrypt\$16384\$[A-Za-z0-9\$=]+)'
)

# Pass 2: field-name-based — both suffixed (_KEY/_TOKEN/_SECRET/_PASSWORD/_HASH/API_KEY)
# AND bare names (secret, password, token, hash, key, case-insensitive).
# This is the pass that catches `secret: 364d313ab5bf1843...cf8158`.
FIELD_SECRET = re.compile(
    r'^(\s*(?:[A-Za-z_][A-Za-z0-9_]*_(?:KEY|TOKEN|SECRET|PASSWORD|HASH|API_KEY)'
    r'|(?i:\s*(?:secret|password|token|hash|key)\s*))'
    r'\s*:\s*)([^\s#][^\n#]*?)\s*$',
    re.MULTILINE,
)

# Pass 3: long hex strings (≥32 hex chars) — dashboard secret hashes, scrypt salts
HEX_SECRET = re.compile(r'\b[0-9a-f]{32,}\b', re.IGNORECASE)

# Pass 4: long base64-like strings (≥40 chars) — session cookies, JWTs
B64_SECRET = re.compile(r'\b[A-Za-z0-9+/]{40,}={0,2}\b')

# Pass 5: opop@<digits> pattern (Dr. Sagar's API key style)
OPOP_SECRET = re.compile(r'\bopop@\w+\b')

src = pathlib.Path(sys.argv[1]); dst = pathlib.Path(sys.argv[2])
text = src.read_text()
text = SECRET_PREFIX.sub('REDACTED', text)
text = FIELD_SECRET.sub(r'\1REDACTED', text)
text = HEX_SECRET.sub('REDACTED', text)
text = B64_SECRET.sub('REDACTED', text)
text = OPOP_SECRET.sub('REDACTED', text)
dst.write_text(text)
PYEOF

# 3. Diff
DIFF_OUT=$(diff -u "$LATEST" "$CUR_TMP" 2>/dev/null || true)
CHANGED=$(printf '%s\n' "$DIFF_OUT" | grep -cE '^[+-][^+-]' || echo 0)

if [ "$CHANGED" -gt "$THRESHOLD" ]; then
  ADDED=$(printf '%s\n' "$DIFF_OUT" | grep -cE '^\+[^+]' || echo 0)
  REMOVED=$(printf '%s\n' "$DIFF_OUT" | grep -cE '^-[^-]' || echo 0)
  LATEST_REL="${LATEST#$HERE/}"
  RECOVER_FILE="${LATEST%.yaml}.raw"
  printf '⚠️ hermes-drift-watchdog: %s lines changed since last 6h snapshot at %s\n+%s / -%s (threshold: %s)\nBaseline: %s\n\nTop changes (already redacted):\n' \
    "$CHANGED" "$TS" "$ADDED" "$REMOVED" "$THRESHOLD" "$LATEST_REL"
  printf '%s\n' "$DIFF_OUT" \
    | grep -E '^[+-][^+-]' \
    | grep -vE 'REDACTED' \
    | head -20 \
    | sed 's/^/  /'
  printf '\nFull diff: diff -u %s <current>\nRecovery: sudo install -m 600 %s %s/config.yaml\n' \
    "$LATEST_REL" "$RECOVER_FILE" "$HERMES"
  exit 1
fi
exit 0
```

Cron shape: same failure-only pattern as the snapshot cron. Template at `templates/cron-drift-watchdog.sh.txt`.

### Critical: drift-watchdog output is delivered verbatim to Discord — redaction MUST be aggressive

The drift alert text becomes the Discord message body, character-for-character. If the inline Python redaction misses any pattern, **secrets leak to the channel**. Bare field names like `secret:`, `password:`, `token:`, `hash:`, `key:` are the most common miss because prefix-only redactors only catch things starting with `sk-`, `cfut_`, `BSAt`, etc.

Verified-leak test cases (all MUST produce `REDACTED` in the alert):

- `secret: 364d313ab5bf1843e46ba2e71e77b4eb33fb458c80d23fb6d291961952cf8158` → REDACTED
- `password_hash: scrypt$16384$8$1$Fwv4prHYDSsXC8C56tCpkA==$a7AatEma1CMM2vVrJB1BIM7jBC+J8pHAW/qX51kaBV4=` → REDACTED
- `API_SERVER_KEY: opop@9900` → REDACTED
- `ALPHA_VANTAGE_API_KEY: 9PPJHVB2FTZWU331` → REDACTED
- `api_key: om-3Vd4meAx1N9phTGio2nuXjinnn35FrJ6GchUH6HYwZd` → REDACTED

Verify with a leak sweep after each drift-watchdog edit:
```bash
out=$(DRIFT_THRESHOLD=50 /root/.hermes/scripts/drift-watchdog.sh 2>&1)
echo "$out" | grep -cE 'opop@|9PPJHV|BSAtDfWF|sk-f49|sk-3ab|scrypt\$16384|3a0963dc|364d313ab5bf'
# expect: 0
```

If any pattern returns >0, the redaction missed it — patch the script BEFORE the next cron tick or the cron will deliver the leaked secret to Discord.

### Critical pitfall: take a fresh baseline mirror immediately after restore

If you restore `~/.hermes/config.yaml` from an older mirror (e.g. after a dashboard-restore splice), and then enable the drift watchdog, the **first watchdog run will report 50+ lines of drift** because the restore itself changed the config relative to the most recent mirror. That's a false positive.

Fix: run `./scripts/snapshot-all.sh` ONCE manually after the restore, before the drift watchdog's first tick. The new mirror becomes the clean baseline.

### Drift-watchdog threshold tuning during active editing sessions

The default `DRIFT_THRESHOLD=50` is tuned for routine use, not active editing. During a session where the user is intentionally modifying `config.yaml` (adding a custom plugin, editing approvals, etc.), cumulative edits between 6h snapshots can easily exceed 50 lines and produce a false-positive alert.

Two complementary fixes:

1. **Bump threshold for active-editing sessions.** Set `DRIFT_THRESHOLD=200` (or higher) when you expect heavy editing. Lower it back after the next 6h mirror lands.
2. **Run a manual baseline refresh after intentional bulk edits.** After the user is done editing, run `./scripts/snapshot-all.sh` manually. The new mirror becomes the clean baseline and the next watchdog tick starts fresh.

Do NOT lower the threshold below 30 — the threshold must always exceed the typical per-tick noise (provider refreshes, model metadata updates, harmless settings churn).

### Scripts that resolve their repo via `$(dirname "$0")/..` break under symlinks

`scripts/drift-watchdog.sh` and `scripts/snapshot-all.sh` historically resolve the repo location with `$(cd "$(dirname "$0")/.." && pwd)`. **This breaks when the script is invoked from a symlink.** When Hermes cron runs the script by basename from `~/.hermes/scripts/`, `$0` is the symlink target inside the snapshots repo, but on some systems `$(dirname "$0")/..` resolves to the symlink path (`/root/.hermes/`) instead of the repo (`/root/.hermes-config-snapshots/`). The redactor then can't find `redact.py` and the script fails with `python3: can't open file '/root/.hermes/scripts/redact.py'`.

Fix: pin the path explicitly. Replace the `HERE="$(cd "$(dirname "$0")/.." && pwd)"` line with:

```bash
SNAPSHOT_REPO="/root/.hermes-config-snapshots"
HERE="$SNAPSHOT_REPO"
```

Or detect the real path with `readlink -f "$0"` if you need portability. Never rely on `$(dirname "$0")/..` when the script might be symlinked from `~/.hermes/scripts/`.

## Pre/Post-Flight YAML Check Pattern

The hermes-update-safe wrapper should refuse to run an update on a broken config and warn if the update broke the config. Pattern:

```bash
# Pre-flight
if ! "$PY" -c 'import yaml; yaml.safe_load(open("/root/.hermes/config.yaml"))' 2>/dev/null; then
  echo "❌ REFUSING hermes update: config.yaml has YAML parse errors." >&2
  echo "   Restore first: sudo install -m 600 <latest-mirror>/config.yaml.raw /root/.hermes/config.yaml" >&2
  exit 2
fi

# ... snapshot, run update ...

# Post-flight (only on success path)
if ! "$PY" -c 'import yaml; yaml.safe_load(open("/root/.hermes/config.yaml"))' 2>/dev/null; then
  echo "❌ POST-UPDATE: config.yaml is now malformed." >&2
  echo "   Restore: sudo install -m 600 ${HERE}/snapshots/updates/${TS_PRE}_pre-update-*.raw /root/.hermes/config.yaml" >&2
  exit 3
fi
```

Exit codes `2` (refused: pre-broken) and `3` (update: post-broken) are distinct from update's own non-zero exit, so a future observer can tell why the wrapper failed without parsing its stderr.

## Cron Schedule: Failure-Only Delivery

### Always use `no_agent=true` + bash script (NOT an LLM agent prompt)

The previous design used an LLM agent prompt with "stay silent on success" instructions. **That is broken**: even when the agent produces empty output, Hermes still delivers a wrapper envelope reading `[SILENT]` to the Discord channel. The user will see `[SILENT]` notifications on every successful tick, defeating the whole point.

The correct design is `no_agent=true` with a bash script as the cron target. In script mode:

- Empty stdout = **zero delivery** (true silence)
- Non-empty stdout = that text becomes the Discord message verbatim
- Non-zero exit code = stdout is still delivered (treat as failure)

**Never use the default LLM agent mode for a "silent on success" cron.** The prompt-gated pattern described in earlier revisions of this skill is wrong.

### Cron job shape

```bash
hermes cron create \
  --name hermes-config-snapshot-6h \
  --schedule "0 */6 * * *" \
  --deliver "discord:<backup-channel-id>" \
  --no-agent \
  --script hermes-snapshot-silent.sh
```

Two constraints on `--script`:

1. **Basename only**, no path. Hermes resolves `--script` relative to `~/.hermes/scripts/`. Absolute paths (`/root/.hermes/scripts/foo.sh`) are rejected with: `Script path must be relative to ~/.hermes/scripts/`.
2. The script must live at `~/.hermes/scripts/<name>.sh`. Install with `install -m 0755 ...`. Source can live in the snapshots repo at `scripts/`, but the cron target needs a copy in `~/.hermes/scripts/`.

### Two script patterns

**Pattern A — natively silent script.** The script itself is designed to print nothing on success and a structured alert on failure:

- `scripts/yaml-lint.sh` — runs `yaml.safe_load` on every config file. Exits 0 silently if all parse, prints the failure list + recovery command and exits 1 if any fail.
- `scripts/drift-watchdog.sh` — diffs current config against latest mirror. Exits 0 silently under threshold, prints summary + recovery command and exits 1 over threshold.

Use this pattern for new scripts from scratch.

**Pattern B — silent wrapper around a chatty script.** The original `snapshot-all.sh` prints useful info on success ("pushed mirrors/<ts> -> origin/main"). Wrapping it in a silent shim gives true silence without rewriting the inner script:

```bash
#!/usr/bin/env bash
# Wrapper around hermes-snapshot-all.sh: prints only on failure.
set -uo pipefail
OUT=$(mktemp)
trap 'rm -f "$OUT"' EXIT
if ! /root/.hermes/scripts/hermes-snapshot-all.sh >"$OUT" 2>&1; then
  TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  {
    echo "❌ hermes-config-snapshot-6h FAILED at $TS"
    echo "Output:"
    sed 's/^/  /' "$OUT"
  }
  exit 1
fi
exit 0
```

Use this when you want to keep the inner script's verbose success output visible to humans who run it manually, but still need cron silence.

### Cron schedules used in production

| Job name | Schedule | Script target |
|---|---|---|
| `hermes-config-snapshot-6h` | `0 */6 * * *` | `hermes-snapshot-silent.sh` (Pattern B) |
| `hermes-yaml-lint-30m` | `*/30 * * * *` | `yaml-lint.sh` (Pattern A) |
| `hermes-drift-watchdog-6h` | `30 */6 * * *` | `drift-watchdog.sh` (Pattern A) |

### Always run the cron target script manually after install

Before relying on any `no_agent=true` cron, run the script directly from a shell and confirm:

- Healthy run: `rc=0`, `stdout=[<empty>]`
- Failure run: `rc=1`, `stdout=<non-empty alert>`

If the script prints anything on success, the wrapper is wrong and you'll see `[SILENT]` envelopes (or worse, full noise) in the delivery channel.

### Subtle bash heredoc bug — don't nest `<<PY` inside a `for` loop

If you write a watchdog script with this pattern:

```bash
# WRONG — subshell quoting mangles the heredoc body
for f in $CONFIG_FILES; do
  err=$("$PY" "$f" 2>&1 <<'PY'
import sys, yaml
...
PY
)
done
```

…the inner `<<PY` heredoc can be misinterpreted when `set -uo pipefail` is on or when `$f` contains characters that confuse the parser. Observed symptom: the script reports spurious `SyntaxError: invalid decimal literal` on configs that parse fine in any other context (e.g. `python3 -c "import yaml; yaml.safe_load(open('/root/.hermes/config.yaml'))"` returns `OK`).

Fix: use a single Python invocation that reads the file list from a tempfile, no per-file heredoc:

```bash
FILELIST=$(mktemp)
trap 'rm -f "$FILELIST"' EXIT
{ for f in "$HERMES/config.yaml" "$HERMES"/profiles/*/config.yaml; do
    [ -f "$f" ] && echo "$f"
  done
} > "$FILELIST"

"$PY" - "$FILELIST" "$TS" <<'PYEOF'
import sys, yaml
files = [line.strip() for line in open(sys.argv[1]) if line.strip()]
errs = []
for f in files:
    try:
        with open(f) as fh: yaml.safe_load(fh)
    except Exception as e:
        errs.append((f, str(e)[:300]))
...
PYEOF
```

This eliminates the nested-heredoc footgun entirely.

## Pitfalls

- **`patch` / `write_file` cannot edit `~/.hermes/config.yaml`** — use `hermes config set` for everything. This skill's redactor works on copies, never the live file.
- **Raw secret files must be mode 600** — `install -m 600` not `cp`. Otherwise the live-config secret is world-readable.
- **Never `git add snapshots/*.yaml` if raw files are named `*.raw.yaml`** — shell glob expansion will stage ignored raw files. Use `*.raw` suffix (no `.yaml`) or `git add` per-file.
- **The redactor is heuristic, not bulletproof** — always run a leak sweep with a long-token regex before each push. If a known-bad token prefix appears in committed YAML, the redactor missed it; update `redact.py`. For the **drift-watchdog inline redaction** specifically, the rules are stricter: the alert text is delivered verbatim to Discord, so even ONE missed secret leaks to the channel. Use all 5 passes (prefix + field-name + bare-field + hex + base64 + opop@ pattern). See "Critical: drift-watchdog output is delivered verbatim to Discord" above.
- **Drift watchdog false positive after a restore** — if you restore config.yaml from an older mirror, the first drift-watchdog tick will report drift because the restore itself changed the file vs the most recent mirror. Take a fresh baseline mirror manually before the first watchdog run.
- **Drift watchdog false positive during active editing** — if you're modifying config.yaml interactively, the diff between current and last 6h mirror will exceed 50 lines. Either bump `DRIFT_THRESHOLD=200` for the session, or run `./scripts/snapshot-all.sh` after your edits to refresh the baseline.
- **Cron `--script` paths must be basenames** — `hermes cron create --script /root/.hermes/scripts/foo.sh` fails. Use `--script foo.sh` and ensure the file lives at `~/.hermes/scripts/foo.sh` (use `install -m 0755` to copy from your snapshots repo's `scripts/`).
- **Never use LLM agent mode for "silent on success" crons** — even an empty agent response gets wrapped in a `[SILENT]` envelope and delivered. Always use `--no-agent --script <name>.sh`.
- **Nested `<<PY` heredocs inside `for` loops can corrupt parser state under `set -uo pipefail`** — symptoms include spurious `SyntaxError: invalid decimal literal` on configs that parse fine via direct `python3 -c` invocation. Use a tempfile file list and a single Python invocation instead.
- **YAML lint false negatives on profile configs** — `scripts/yaml-lint.sh` only lints `profiles/*/config.yaml`, not `profiles/*/plugins/*/config.yaml` (those are owned by their plugins). If a plugin's config.yaml is malformed, only the plugin will notice.
- **Don't confuse this skill with `hermes-backup-watchers`** — file-archive backups to TB / cloud vs git-tracked, redacted text snapshots. They run side-by-side: hermes-backup-watchers for the multi-GB state.db / mnemosyne.db / skills tree, this skill for config + cron + plugins + themes.
- **Don't snapshot `state.db` even though it's tempting** — 2.5 GB binary blobs do not belong in git. Hermes's existing 6h plain backup cron (cron id `5be7f96f4d38`, `plain-hermes-local-6h`) covers state.db to `/mnt/tb/hermes-backups/`. Cross-check with `hermes-backup-watchers` skill.
- **Pre-update hook is shell-function only** — only intercepts in interactive shells where `/etc/profile.d` is sourced. Service-launched hermes (e.g. systemd) bypasses the hook. That's fine for this skill because `hermes update` from systemd is the wrong pattern anyway.
- **`hermes-update-safe` must NOT be a copy of `scripts/hermes-update-safe.sh` in `/usr/local/bin`** — the wrapper uses `HERE="$(cd "$(dirname "$0")/.. && pwd)"`. When `$0` is `/usr/local/bin/hermes-update-safe`, `HERE` becomes `/usr/local` and pre-update snapshot fails: `/usr/local/scripts/snapshot.sh: No such file or directory`. With `set -e`, **`hermes update` never runs**. Fix: `sudo install -m 0755 templates/hermes-update-safe-launcher.sh /usr/local/bin/hermes-update-safe`. See `references/hermes-update-safe-wrong-install-path.md`.
- **Don't auto-restore `session_reset.mode`** — it was `none` in the backup AND `none` after the update. Don't touch. **However**, be aware that `mode: none` does NOT silence every "Session automatically reset" notification: see `references/session-reset-mode-none-quirk.md` for the `resume_pending_expired` path that bypasses the policy and produces the misleading "inactive for 24h" message text. If the user complains about reset notifications despite `mode: none`, point them to that reference — it is a Hermes gateway quirk, not a config drift to fix.
- **Don't auto-restore `hooks_auto_accept`** — same. Was `false`, stayed `false`. The drift the user actually saw was in `approvals.mode` / `command_allowlist` / dashboard auth.
- **Hermes's pre-update snapshot at `~/.hermes/state-snapshots/<ts>-pre-update/` is captured AFTER corruption, not before** — observed 2026-07-08: this snapshot was 1982 bytes (the minimal-template fallback config), not the user's full working config. It is **NOT a usable restore source** on its own. That's why this skill keeps its own `snapshots/updates/` tree in git — it snapshots BEFORE invoking the update.
- **Newest 6h plain backup can already be bad.** Before restoring `~/.hermes/config.yaml` from `/mnt/tb/hermes-backups/#plain/hermes-plain-<ts>/config.yaml`, verify the candidate still contains the expected sections (`custom_providers`, `model_catalog`, `model_aliases`, `discord` for this deployment). A newer snapshot may already hold the minimal fallback config while an older same-day snapshot is the newest good restore point. See `references/plain-backup-config-restore-triage.md`.
- **`state-snapshots/<ts>-pre-update/config.yaml` inside a bad plain backup tree may be richer than the top-level config, but do not treat it as the default restore source.** Use it for forensic diffing; prefer the newest verified-good top-level `config.yaml` first. See `references/plain-backup-config-restore-triage.md`.
- **`openrouter_free_watch.py` can break YAML without truncating the file** — see `references/openrouter-free-watch-config-corruption.md`.
- **Never append drift-watchdog test junk to live `~/.hermes/config.yaml`** — see `references/drift-watchdog-test-never-live-append.md`.

## Verification Checklist

- [ ] Private GitHub repo created (`gh repo create ... --private`)
- [ ] `scripts/redact.py` present and works on the malformed backup YAML
- [ ] First `snapshot-all.sh` run produces a `mirrors/<ts>/` directory
- [ ] Leak sweep on committed YAML returns 0 hits
- [ ] No `*.raw` files in `git ls-files` output (they're gitignored)
- [ ] 6h cron job exists with `deliver=discord:<channel-id>` and `workdir=<repo>`
- [ ] First cron tick produced no Discord message (success = silent)
- [ ] Forcing a cron failure (e.g. by deleting the workdir) produces one Discord message
- [ ] `/usr/local/bin/hermes-update-safe` is the **launcher** template (not a raw copy of `scripts/hermes-update-safe.sh`) and `/etc/profile.d/hermes-pre-update-snapshot.sh` installed
- [ ] Running `hermes update` in a new login shell triggers a pre-update snapshot
- [ ] After update, `snapshots/updates/<post-update-ts>` appears in the repo
- [ ] yaml-lint cron (`hermes-yaml-lint-30m`, schedule `*/30 * * * *`) exists, alert-only on failure
- [ ] drift-watchdog cron (`hermes-drift-watchdog-6h`, schedule `30 */6 * * *`) exists, alert-only on failure
- [ ] Drift-watchdog baseline is current: most recent `mirrors/<ts>/config.yaml` matches the live config after any restore

## Related Skills

- `hermes-dashboard-restore` — recovery flow when dashboard auth breaks after an update; uses the splice pattern
- `hermes-backup-watchers` — file-archive backups to TB / cloud for the large binary blobs
- `hermes-agent` (bundled) — main Hermes reference

## References

- `references/config-drift-cheatsheet.md` — exact field-level drift observed after a Hermes update (what to restore, what to keep)
- `references/leak-sweep-regex.md` — the token-prefix regex used to verify redacted files before commit
- `references/setup-recipe.md` — exact step-by-step for first-time setup (no copy-paste drift from this SKILL.md)
- `references/hermes-config-corruption-2026-07-08.md` — full transcript of the silent-corruption incident: agent.log warnings, gateway fallback, drift table, recovery commands
- `references/openrouter-free-watch-config-corruption.md` — structural YAML break; cron culpability; repair and hardening
- `references/drift-watchdog-test-never-live-append.md` — `fake_key_*` from live-file test, not cron
- `references/config-regression-forensics-july-2026.md` — use when a post-update minimal config may actually predate the update; includes the manual-update-vs-config-writer triage pattern and restore verification checklist.
- `references/session-reset-mode-none-quirk.md` — `mode: none` does NOT silence every "Session automatically reset" message; `resume_pending_expired` path bypasses the policy. Misleading "inactive for 24h" text when the actual cause was a gateway restart.
- `references/hermes-update-safe-wrong-install-path.md` — wrong install of the safe wrapper blocks `hermes update` via profile.d hook (`snapshot.sh` under `/usr/local/scripts`).

## Scripts

- `scripts/redact.py` — line-based redactor (template)
- `scripts/snapshot.sh` — single-config snapshot with optional subfolder + `--no-push`
- `scripts/snapshot-all.sh` — comprehensive snapshot of config + cron + plugins + themes + profiles
- `scripts/hermes-update-safe.sh` — pre/post `hermes update` wrapper with YAML pre/post-flight checks
- `scripts/yaml-lint.sh` — runs `yaml.safe_load` on every Hermes config file; silent on success
- `scripts/drift-watchdog.sh` — diffs live config against the most recent mirror; alerts on threshold breach

## Templates

- `templates/cron-snapshot-6h.sh.txt` — `hermes cron create --no-agent --script ...` invocation for the snapshot cron (LLM-agent prompt files removed — they produced `[SILENT]` envelopes on every successful tick)
- `templates/cron-yaml-lint.sh.txt` — same for `hermes-yaml-lint-30m`
- `templates/cron-drift-watchdog.sh.txt` — same for `hermes-drift-watchdog-6h`
- `templates/hermes-pre-update-snapshot.sh` — shell function for `/etc/profile.d/`
- `templates/hermes-update-safe-launcher.sh` — install to `/usr/local/bin/hermes-update-safe` (execs repo `scripts/hermes-update-safe.sh`)
- `templates/README.md` — what each template is for and how to deploy

Note: prior revisions had `cron-*.prompt.txt` files for the LLM-agent pattern. Those are obsolete and have been removed; if you have an older copy of this skill, delete the `.prompt.txt` files and use the `--no-agent --script` invocations instead.
