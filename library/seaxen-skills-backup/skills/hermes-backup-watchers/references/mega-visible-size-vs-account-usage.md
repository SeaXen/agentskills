# MEGA visible-size mismatch and partial plain-backup verification

Use this when MEGA shows a large used quota but the visible Cloud Drive backup folder is tiny, and/or when a supposed plain backup folder is far smaller than `/root/.hermes`.

## Symptom set

Observed pattern:
- `rclone about Mega:` reported about `21.77 GiB used`
- MEGA web UI showed:
  - `Hermes-backups` visible size only ~`325.3 MB`
  - `Rubbish bin` = `0 B`
  - `Device centre` empty
- Plain backup folders in `Hermes-backups/#plain/` showed only ~`178.4 MB` and `146.9 MB`

This combination means the visible Cloud Drive data does **not** explain the quota.

## Interpretation

There are two separate issues to distinguish:

### 1. Account-usage mismatch
If all of these are true:
- Cloud Drive visible backup data is tiny
- Rubbish bin is empty
- Device Centre is empty
- `rclone about Mega:` still shows tens of GB used

then the remaining usage is likely one of:
- hidden/orphaned MEGA-side storage
- version-history / internal-history storage not surfaced clearly in the current UI
- account-side accounting lag

Do **not** keep deleting the visible backup folder expecting that alone to resolve the used-quota number.

### 2. Plain backup integrity failure
A plain backup is a directory copy, not a compressed archive. So if local `/root/.hermes` is multi-GB and the remote plain backup folder is only ~150–200 MB, treat that as evidence the plain backup is partial/incomplete.

## Verification sequence

### Check the actual remote folder size
```bash
rclone size Mega:Hermes-backups/#plain/<folder> --json
```

Example observed result:
- `count`: `362`
- `bytes`: `154024193` (~147 MB)

### Compare remote top-level inventory to local Hermes home
List remote top-level entries:
```bash
rclone lsf Mega:Hermes-backups/#plain/<folder>
```

Then compare with local top-level entries under `/root/.hermes`.

### Probe for must-exist heavyweight paths
These should exist in a real full plain backup:
- `state.db`
- `state-snapshots/`
- `scripts/`
- `sessions/`
- `skills/`
- `venvs/`
- `profiles/`
- `repos/`

If many of these are missing, the backup is not a full plain copy.

## Observed missing top-level items in the bad Mega plain backup
The incomplete remote plain backup was missing many local top-level paths, including:
- `scripts/`
- `sessions/`
- `skills/`
- `state-snapshots/`
- `state.db`
- `venvs/`
- `repos/`
- `profiles/`

This proved the backup was silently partial even though the cron job had reported success.

## Reporting rule
When this happens, be direct:
- say the current Mega plain backup is **partial / incomplete**
- say it is **not trustworthy as a real full backup**
- do not describe the small size as normal compression or UI approximation

## Practical lesson
Retention success and backup integrity are different checks.

A Mega job can:
- prune old folders correctly
- report `STATUS=SUCCESS`
- **and still produce a bad partial backup**

So after any suspiciously small plain backup size, verify both:
1. retention behavior
2. content completeness
