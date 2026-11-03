# hermes-update-safe wrong install path (blocks `hermes update`)

## Symptom

```text
root@host:~# hermes update -y
==> pre-update snapshot at 2026-07-08T18-22-59Z
/usr/local/bin/hermes-update-safe: line 40: /usr/local/scripts/snapshot.sh: No such file or directory
```

Update does **not** run. Pre-snapshot step fails first (`set -euo pipefail`).

## Why

1. `/etc/profile.d/hermes-pre-update-snapshot.sh` defines `hermes()` so `hermes update` → `command hermes-update-safe …`.
2. Setup doc used to say: `sudo install scripts/hermes-update-safe.sh /usr/local/bin/hermes-update-safe`.
3. That script sets `HERE="$(cd "$(dirname "$0")/.. && pwd)"`. From `/usr/local/bin/hermes-update-safe`, `HERE=/usr/local`.
4. It calls `${HERE}/scripts/snapshot.sh` → `/usr/local/scripts/snapshot.sh` (missing).
5. Real scripts live in `~/.hermes-config-snapshots/scripts/` (e.g. `/root/.hermes-config-snapshots/scripts/snapshot.sh`).

## Fix

```bash
sudo install -m 0755 \
  /root/.hermes/skills/devops/hermes-git-config-snapshots/templates/hermes-update-safe-launcher.sh \
  /usr/local/bin/hermes-update-safe
```

Or from the snapshots repo after syncing the template:

```bash
sudo install -m 0755 templates/hermes-update-safe-launcher.sh /usr/local/bin/hermes-update-safe
```

Launcher `exec`s `${REPO}/scripts/hermes-update-safe.sh` so `$0` stays under `…/scripts/` and `HERE` is the repo root.

Override repo path: `HERMES_SNAPSHOT_REPO=/path/to/repo hermes-update-safe -y`.

## Bypass hook (emergency update without snapshot)

```bash
command hermes update -y
```

Uses the real Hermes binary, not the profile.d wrapper.

## Verify

```bash
bash -n /usr/local/bin/hermes-update-safe
test -x /root/.hermes-config-snapshots/scripts/snapshot.sh && echo OK
```

Then in a login shell: `hermes update --check` or `hermes-update-safe --check` if supported; full `hermes update -y` when ready.