# Plain-backup config restore triage

Use this when `~/.hermes/config.yaml` has been replaced by a minimal template and you need to restore from `/mnt/tb/hermes-backups/#plain/...`.

## Observed pattern

A newer 6-hour plain backup can already contain the broken/minimal top-level config, while an older backup from the same day still has the last good full config.

Observed shape:
- broken live file: `/root/.hermes/config.yaml`
- bad backup candidate: `/mnt/tb/hermes-backups/#plain/hermes-plain-2026-07-14_06-00/config.yaml`
- good backup candidate: `/mnt/tb/hermes-backups/#plain/hermes-plain-2026-07-14_00-00/config.yaml`

The bad candidate was a tiny fallback-style config with none of:
- `custom_providers`
- `model_catalog`
- `model_aliases`
- `discord`

The good candidate restored all of them.

## Triage rule

Do NOT restore the newest backup blindly.

For each candidate `config.yaml`, verify at minimum whether it contains the sections the user actually cares about. For this deployment the fast litmus test was:
- `custom_providers:`
- `model_catalog:`
- `model_aliases:`
- `discord:`

If those are absent, treat that backup as already-corrupted/minimal even if it is the newest snapshot.

## Practical restore order

1. Check current live file size/shape.
2. Check newest plain backup top-level `config.yaml`.
3. If it is already minimal, walk backward through earlier 6h snapshots until you find the newest candidate containing the expected sections.
4. Make a safety copy of the current broken file.
5. Restore the verified good `config.yaml`.
6. Restart gateway.
7. Verify provider/model-list sections survived parse and Discord reconnects.

## Important nuance

Inside a bad plain backup tree, `state-snapshots/<ts>-pre-update/config.yaml` may still contain a richer historical config. That is useful for forensic diffing, but do NOT assume the state-snapshot copy is the right direct restore source for the active top-level config. Prefer the newest verified-good top-level `config.yaml` first.

## Minimal verification after restore

Confirm all of:
- `custom_providers_count > 0`
- `model_catalog` exists
- `model_aliases_count > 0`
- `discord` exists
- gateway restarts cleanly
- Discord state becomes `connected`

## Why this belongs here

This is the restore side of config drift protection: the snapshot system tells you drift happened, but the plain-backup archive set can be the fastest recovery source if you verify backup quality before copying.