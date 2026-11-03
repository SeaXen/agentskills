# Schema migration: flat thresholds → nested `{enabled, value, duration_min}`

## Problem

The first release of `systor` had a flat schema — each metric was a bare
scalar with a separate `sustained_samples_*` companion:

```yaml
thresholds:
  cpu_load_1m: 4.0
  cpu_temp_c: 80.0
  sustained_samples_cpu: 4
  sustained_samples_temp: 4
```

This is ugly to edit and exposes an internal concept (`sustained_samples`) the
operator shouldn't need to think about. The user thinks in minutes.

The fix is to switch each metric to a dict with three explicit fields, plus
a single top-level `cooldown_sec`:

```yaml
thresholds:
  cpu_temp_c: { enabled: true, value: 85.0, duration_min: 3 }
  mem_free_mb: { enabled: true, value: 500, duration_min: 2 }
  cooldown_sec: 600
```

But **existing deployments still have the old format on disk**. Forcing
operators to run a converter script is friction. Auto-migrate on load instead.

## The migration code

Add a `_migrate_thresholds()` step in `load_config()` after merging files and
before applying env overrides. It detects old-shape (any non-dict under
`thresholds` except `cooldown_sec`) and converts in-memory:

```python
_THRESHOLD_MIGRATION = {
    "cpu_load_1m":   ("sustained_samples_cpu",  4),
    "cpu_temp_c":    ("sustained_samples_temp", 4),
    "mem_free_mb":   ("sustained_samples_mem",  4),
    "swap_used_mb":  ("sustained_samples_swap", 4),
    "disk_used_pct": ("sustained_samples_disk", 1),
}

def _migrate_thresholds(cfg: dict) -> None:
    th = cfg.get("thresholds", {})
    if not th:
        return
    needs_migration = any(
        k != "cooldown_sec" and not isinstance(v, dict)
        for k, v in th.items()
    )
    if not needs_migration:
        return
    new_th = {}
    for key, val in th.items():
        if key == "cooldown_sec":
            new_th[key] = val
            continue
        if isinstance(val, dict):
            new_th[key] = val
            continue
        # Flat scalar → derive duration from old sustained_samples
        dur_key, default_dur = _THRESHOLD_MIGRATION.get(key, (None, 2))
        if dur_key and dur_key in th:
            try:
                # 4 samples × 30s = 120s = 2 minutes (min 1)
                dur_min = max(1, int(int(th[dur_key]) * 30 // 60))
            except (ValueError, TypeError):
                dur_min = default_dur
        else:
            dur_min = default_dur
        new_th[key] = {"enabled": True, "value": val, "duration_min": dur_min}
    cfg["thresholds"] = new_th


def load_config() -> dict:
    cfg = json.loads(json.dumps(DEFAULT_CONFIG))
    for path in CONFIG_PATHS:
        if path.exists() and path.is_file():
            try:
                cfg = _deep_merge(cfg, _yaml_to_dict(path.read_text()))
            except Exception as e:
                print(f"[warn] failed to parse {path}: {e}", file=sys.stderr)
    _migrate_thresholds(cfg)
    _apply_env(cfg)
    return cfg
```

## Why this works

1. **Default config already has the new shape** — so first-time installs
   never trip the migration.
2. **Old configs migrate silently** — the operator does not run anything.
3. **Save writes the new shape** — `_save_config()` already handles nested
   dicts (each dict field is indented 4 spaces). So the next save upgrades
   the file on disk.
4. **No environment coupling** — env-var overrides land *after* migration,
   so they target the new-shape `cfg["thresholds"]["cpu_temp_c"]["value"]`
   correctly. (You also need the env override map to know about the nested
   shape: pass a `sub=` arg like `"value"` to write into the inner dict.)

## Conversion math

`sustained_samples_cpu: 4` at `poll_interval_sec: 30` = 4 × 30s = 120s = 2 min.
General formula: `duration_min = max(1, samples * poll_sec // 60)`.

The "min 1" matters — old configs with `sustained_samples_disk: 1` (one sample
because disk fills slowly) should not become 0 minutes.

## Pitfalls

- **The old YAML parser must handle nested dicts.** The systor `_yaml_to_dict`
  already does (it walks indentation). If yours doesn't, upgrade the parser
  before introducing nested values, or use PyYAML.
- **Don't drop the env override map's nested-field awareness.** A simple
  `cfg[section][key] = cast(value)` will write `cpu_temp_c: 85.0` and break
  the schema again. Add a `sub=` arg and check `isinstance(cfg[...][...], dict)`.
- **Test migration on a copy of the real `/etc/<app>/config.yaml`** before
  shipping. Run `load_config()` against the live file and assert the result
  is the expected nested shape.

## Verification

```python
# Test 1: first-time install uses defaults
cfg = load_config()  # no files exist
assert cfg["thresholds"]["cpu_temp_c"] == {
    "enabled": True, "value": 85.0, "duration_min": 3
}

# Test 2: old flat config migrates silently
Path("/tmp/test-cfg/etc/systor/config.yaml").parent.mkdir(parents=True, exist_ok=True)
Path("/tmp/test-cfg/etc/systor/config.yaml").write_text("""
thresholds:
  cpu_temp_c: 75.0
  sustained_samples_temp: 6
""")
# patch CONFIG_PATHS to include this temp dir, then load_config()
# expect: cpu_temp_c == {enabled: True, value: 75.0, duration_min: 3}

# Test 3: save writes new shape
save_config(cfg)
assert "duration_min: 3" in Path("/tmp/test-cfg/etc/systor/config.yaml").read_text()
```