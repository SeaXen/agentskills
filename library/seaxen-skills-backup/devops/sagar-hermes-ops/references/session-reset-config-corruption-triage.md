# Session reset looked re-enabled, but config was corrupted

Use this reference when Hermes seems to have turned automatic session reset back on after it was disabled earlier.

## Key points
- Do not trust a single `session_reset` symptom at face value.
- First determine whether `~/.hermes/config.yaml` is valid YAML.
- A truncated/corrupted config can cause fallback behavior and misleading status displays.
- `Invalidated run generation ... (session_reset)` is an umbrella lifecycle marker, not proof of idle/daily auto-reset.

## Fast triage checklist
1. Inspect Hermes logs for config parse failures:
   - `errors.log`: `Failed to parse /root/.hermes/config.yaml`
   - `update.log`: parse errors during update/migration
2. Compare active `config.yaml` size/content against:
   - `config.yaml.bak`
   - `config.yaml.corrupt.*.bak`
   - `config.yaml.bak-move-*`
   - state snapshots under `~/.hermes/state-snapshots/`
3. Search backups for explicit prior reset policy, especially:
   ```yaml
   session_reset:
     at_hour: 4
     idle_minutes: 1440
     mode: none
   ```
4. Correlate any `session_reset` log line with nearby events:
   - slash `/reset`
   - destructive-reset confirm/cancel logs
   - restart/reload events
5. Only after that decide whether the issue is:
   - true policy change
   - config corruption/truncation
   - manual reset mistaken for automatic reset

## Durable lesson
For modern Hermes builds, the upstream default is `session_reset.mode: none`. If a user says they disabled auto reset long ago and it now looks enabled again, config corruption is a more likely explanation than a silent default change.

## Recommended fix path
1. Restore the latest known-good config backup.
2. Make `session_reset.mode: none` explicit.
3. Validate that Hermes can parse the restored YAML.
4. Restart the gateway.
5. Re-check logs to ensure future `session_reset` events are not just manual `/reset` actions.
