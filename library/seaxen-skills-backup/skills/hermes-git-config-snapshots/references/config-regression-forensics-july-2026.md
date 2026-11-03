# Config regression forensics — July 2026

Use this when Hermes comes up with a suddenly minimal `~/.hermes/config.yaml` after an update and custom providers/model aliases/Discord settings appear missing.

Key lessons

1. Distinguish `update preserved bad state` from `update caused bad state`.
   - Check the latest pre/post update snapshots in:
     - `/root/.hermes-config-snapshots/snapshots/updates/`
   - If the `*_pre-update_*.yaml` snapshot is already tiny/minimal and missing `custom_providers`, `model_aliases`, or `discord`, the updater is not the original cause. It merely migrated/preserved an already-bad config.

2. Use `update.log` plus timer inventory to separate manual updates from automation.
   - Correlate `/root/.hermes/logs/update.log` timestamps with config `mtime`.
   - Check systemd user timers. If there are no Hermes update timers, do not blame an auto-updater.
   - In this incident, the 07:45 update was manual; no user timers existed.

3. Look for local config writers, not just Hermes core.
   - Enumerate cron jobs and inspect scripts that touch `/root/.hermes/config.yaml`.
   - A high-confidence local culprit class is any cron script that edits the live config in place.
   - In this environment, `openrouter_free_watch.py` was the only active-known config mutator and remained the top suspect for automatic drift/corruption.

4. Verification checklist after restore
   - Config parses cleanly.
   - `_config_version` is current.
   - `custom_providers`, `model_aliases`, and `discord` sections are back.
   - Gateway reconnects and logs show Discord connected.
   - Expected custom provider endpoints are present again.

5. Practical caution
   - `cronjob list` is the scheduler truth for current enabled/paused state.
   - Raw `jobs.json` may look inconsistent enough to confuse quick forensic reads; prefer the scheduler view first, then inspect the JSON only for script names and history details.
