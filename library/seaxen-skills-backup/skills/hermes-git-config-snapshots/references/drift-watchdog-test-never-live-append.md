# Drift-watchdog test — never append to live config

## What went wrong (2026-07-08)

While validating `drift-watchdog.sh`, an agent ran:

```bash
cp /root/.hermes/config.yaml /root/.hermes/config.yaml.drift-test.bak
for i in $(seq 1 60); do
  printf 'fake_key_%d: "value%d"\n' "$i" "$i" >> /root/.hermes/config.yaml
done
DRIFT_THRESHOLD=50 /root/.hermes-config-snapshots/scripts/drift-watchdog.sh
mv /root/.hermes/config.yaml.drift-test.bak /root/.hermes/config.yaml
```

If the restore step fails, is skipped, or another writer (e.g. `openrouter_free_watch.py`) runs on the corrupted file, `fake_key_*` lines persist in git mirrors and break YAML together with mis-placed OpenRouter alias blocks.

## Safe test pattern

```bash
TMP=/tmp/hermes-drift-test.yaml
cp /root/.hermes/config.yaml "$TMP"
for i in $(seq 1 60); do printf 'fake_key_%d: "value%d"\n' "$i" "$i" >> "$TMP"; done
# Point drift script at TMP only if you add a HERMES_CONFIG override for tests;
# otherwise diff two temp redacted files — do not touch live path.
```

For yaml-lint failure tests, the production script already uses a broken `/tmp/test-config.yaml` in documented examples — keep that pattern.

## Verification after any live-file test

```bash
python3 -c "import yaml; yaml.safe_load(open('/root/.hermes/config.yaml'))"
grep -c '^fake_key_' /root/.hermes/config.yaml || true   # expect 0
hermes config check 2>&1 | grep -i 'Falling back' && echo BAD || echo OK
```