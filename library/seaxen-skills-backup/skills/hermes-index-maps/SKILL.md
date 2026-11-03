---
name: hermes-index-maps
description: Curated INDEX.md navigation maps for Hermes and TB.
version: 0.1.0
author: Hermes
platforms: [linux]
metadata:
  hermes:
    tags: [Navigation, Hermes, DietPi, INDEX]
---

# Hermes INDEX.md Maps

`INDEX.md` files are **navigation maps** (where things live). They are **not** instructions, **not** auto-injected memory, and **not** a substitute for `AGENTS.md`. Hermes uses them only when it `read_file`s them. Prefer **one curated master map** plus a few subtree maps—not an `INDEX.md` in every directory.

## When to Use

- User asks where something lives under `/mnt/tb` or `~/.hermes`
- After adding a new app under `/mnt/tb/1Apps/<name>`
- After installing plugins/skills or changing Hermes layout
- User says "refresh INDEX" or "update the disk map"
- Confusion between `INDEX.md` vs `AGENTS.md`

## Prerequisites

- Linux host with `/mnt/tb` mounted and `hermes` symlink at `/mnt/tb/hermes` → `/root/.hermes`
- Regeneration scripts (already on this host):
  - `~/.hermes/scripts/refresh_mnt_tb_index.py`
  - `~/.hermes/scripts/refresh_hermes_indexes.py`
- Weekly cron jobs (no-agent, deliver `local`):
  - `refresh-mnt-tb-index` — `0 4 * * 0`
  - `refresh-hermes-indexes` — `15 4 * * 0`
- Do **not** modify `AGENTS.md` when maintaining indexes unless the user explicitly asks

## How to Run

- Read maps with `read_file` (start at the path below, then drill into subtree `INDEX.md` if present)
- Regenerate manually via `terminal` invoking the Python scripts
- Schedule changes via `cronjob` (list/update existing jobs; do not duplicate)

## Quick Reference

| Path | Role |
|------|------|
| `/mnt/tb/INDEX.md` | Tier **A** — curated top-level TB disk map |
| `/mnt/tb/Medicine/INDEX.md` | Tier **C** — medicine vault entry |
| `/mnt/tb/Sea-knowledge/INDEX.md` | Tier **C** — numbered chapter entry |
| `/mnt/tb/1Apps/INDEX.md` | Tier **C** — all self-hosted apps |
| `/root/.hermes/INDEX.md` | Tier **B** — Hermes home high-signal map |
| `/root/.hermes/skills/INDEX.md` | Skills subtree |
| `/root/.hermes/plugins/INDEX.md` | Plugins subtree |
| `/root/.hermes/repos/INDEX.md` | Repos subtree |
| `~/.hermes/cron_state/refresh_mnt_tb_index.json` | SHA256 state for TB index |
| `~/.hermes/cron_state/refresh_hermes_indexes.json` | SHA256 state for Hermes indexes |

**INDEX vs AGENTS**

| File | Purpose |
|------|---------|
| `INDEX.md` | Folder/file navigation |
| `AGENTS.md` | Project instructions, conventions, how to work |

## Procedure

1. **Orient (3-tier)** — `read_file` tier **A** `/mnt/tb/INDEX.md`; tier **B** `/root/.hermes/INDEX.md` for Hermes; tier **C** work-area index (`Medicine/`, `Sea-knowledge/`, `1Apps/`) when doing that work.
2. **Drill down** — When working in a subtree, `read_file` that folder's `INDEX.md` if it exists (`skills/`, `plugins/`, `repos/`).
3. **Regenerate TB maps (A + C)** — invoke through `terminal`:
   ```bash
   python3 /root/.hermes/scripts/refresh_mnt_tb_index.py
   ```
   Updates: `INDEX.md`, `Medicine/INDEX.md`, `Sea-knowledge/INDEX.md`, `1Apps/INDEX.md`.
4. **Regenerate Hermes maps** — invoke through `terminal`:
   ```bash
   python3 /root/.hermes/scripts/refresh_hermes_indexes.py
   ```
5. **After material layout changes** — run the relevant script(s) immediately; do not wait for Sunday cron.
6. **Manual curation** — If auto output is too long or noisy, edit the generator script logic (exclusions, `TOP` table, app list caps)—not tens of thousands of per-folder files.
7. **New self-hosted apps** — Default path convention: `/mnt/tb/1Apps/<appname>`; ensure `1Apps/` section reflects new app on next regen.

## Pitfalls

- **Not in memory** — `INDEX.md` is not Mnemosyne/legacy memory; stale until regen or edit.
- **Cron is silent** — Scripts print stdout **only when content hash changes**; empty stdout on cron tick means unchanged (not failure).
- **No timestamps in generated body** — Live timestamps in file content break hash stability and cause weekly rewrites; keep maintenance lines static.
- **Excluded from `/mnt/tb` map** — `2dl/`, `3movie/`, `4show/`, cache/backup/temp/trash/VCS/build/vendor trees (see script `skip_top` / `exclude_dir_names`).
- **Per-folder INDEX everywhere** — Avoid regenerating INDEX in every directory under `/mnt/tb`; use curated master + Hermes subtree indexes only.
- **Symlink** — `/mnt/tb/hermes` points at `/root/.hermes`; editing either path is the same tree.

## Verification

Invoke through `terminal`:

```bash
python3 /root/.hermes/scripts/refresh_mnt_tb_index.py
python3 /root/.hermes/scripts/refresh_hermes_indexes.py
python3 /root/.hermes/scripts/refresh_mnt_tb_index.py
python3 /root/.hermes/scripts/refresh_hermes_indexes.py
```

Second pair should produce **no stdout**. Confirm files exist with `read_file` on `/mnt/tb/INDEX.md` and `/root/.hermes/INDEX.md`.