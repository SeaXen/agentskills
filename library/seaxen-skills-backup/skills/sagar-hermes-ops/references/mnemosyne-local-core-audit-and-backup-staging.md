# Mnemosyne local-core audit and backup staging

Use this when Dr. Sagar asks whether Mnemosyne is really local/core, whether it matches docs expectations, or whether the install is healthy without Docker.

## Runtime classification

Check these in order:

1. Hermes config path and provider
   - `hermes config path`
   - verify `memory.provider: mnemosyne`
2. Real path semantics
   - verify `/root/.hermes/...` vs `/mnt/tb/hermes/...` with `os.path.samefile()` / `realpath`
   - on this host they can be the same live tree
3. Live runtime class
   - `docker ps` to confirm Mnemosyne is **not** the active runtime if the user said forget Docker
   - check for local DB under `~/.hermes/mnemosyne/data/mnemosyne.db`
4. Core health
   - `mnemosyne_diagnose()`
   - SQLite `PRAGMA integrity_check`
   - `mnemosyne verify <db> --quick`
   - `mnemosyne stats` and `hermes mnemosyne stats`

## Docs-parity standardization

If Hermes is using a vendored/local Mnemosyne tree and core storage already works, the remaining docs-gap may be the **standard Python import / CLI surface**, not the provider itself.

Useful checks:
- Hermes-facing path works: `hermes memory status`, `hermes mnemosyne --help`, `hermes mnemosyne stats`
- Standard package path works: Hermes venv `python -c 'import mnemosyne'`
- Standard CLI works from shell: `mnemosyne --help`

If provider works but standard package/CLI is missing, standardize it without changing the live provider design:
1. install the vendored package into the Hermes venv (editable is fine)
2. verify `import mnemosyne` in the Hermes venv
3. if the venv CLI exists but PATH does not expose it, add a tiny wrapper such as `/usr/local/bin/mnemosyne` that execs the venv binary
4. re-check `mnemosyne --help` and `mnemosyne verify ...`

This keeps the current local/runtime shape while making the install line up better with docs and operator expectations.

## Backup pitfall that looks like a Mnemosyne failure

If encrypted full-Hermes backups fail with `database or disk is full`, do **not** assume Mnemosyne DB corruption.

First compare:
- source tree size (`du -sh ~/.hermes`)
- temp staging filesystem (`df -h /tmp`)
- backup destinations (`df -h <destinations>`)

Observed durable pattern:
- full Hermes home was ~11G
- `/tmp` was tmpfs ~6.8G
- backup script used `tempfile.TemporaryDirectory()`
- failure string was `database or disk is full`
- real cause was staging the whole archive under `/tmp`, not destination capacity and not Mnemosyne integrity

## Fix shape for backup scripts

For full-home encrypted backups:
- avoid default `/tmp` staging for large Hermes homes
- create a temp root on a real disk/mount with headroom (for example `/mnt/tb/.tmp-hermes-backup`)
- point `TemporaryDirectory(..., dir=that_path)` there
- then re-run the script directly before trusting cron

Also check scheduler realism:
- if the archive is large, a 120s cron timeout is usually too short even after staging is fixed
- separate `backup script failed` from `delivery to Discord failed`; they are different failure classes

## Reporting shape

Report Mnemosyne honestly as two layers:
- **core/provider health** — DB path, integrity, stats, CLI/diagnose status
- **backup/ops health** — whether point-in-time backup automation is actually succeeding

Do not say "all perfect" if the core is healthy but the backup path is still failing.