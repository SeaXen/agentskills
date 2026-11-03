# Curated INDEX maintenance (Hermes + /mnt/tb)

Session distilled pattern for Dr. Sagar's host.

## Final file set (minimal useful)

| Path | Role |
|------|------|
| `/mnt/tb/INDEX.md` | Curated top-level disk map (apps, Medicine, hermes symlink, etc.) |
| `/root/.hermes/INDEX.md` | Hermes home map; points to nested indexes |
| `/root/.hermes/skills/INDEX.md` | Skills subtree |
| `/root/.hermes/plugins/INDEX.md` | Plugins subtree |
| `/root/.hermes/repos/INDEX.md` | Repos subtree |

Do **not** maintain `INDEX.md` in every directory under `/mnt/tb` unless the user explicitly re-requests full recursion after a size warning.

## Scripts

```bash
python3 ~/.hermes/scripts/refresh_mnt_tb_index.py
python3 ~/.hermes/scripts/refresh_hermes_indexes.py
```

- Print stdout **only when content hash changes** (safe for `no_agent` cron).
- Do not embed `datetime.now()` in generated markdown (breaks idempotent weekly runs).

## Cron (this host)

| Job | Schedule | Script |
|-----|----------|--------|
| `refresh-mnt-tb-index` | `0 4 * * 0` | `refresh_mnt_tb_index.py` |
| `refresh-hermes-indexes` | `15 4 * * 0` | `refresh_hermes_indexes.py` |

Both: `deliver: local`, `no_agent: true`.

## Curated /mnt/tb exclusions

Skip listing and skip generating indexes inside:

- Name contains: `cache`, `backup`, `tmp`, `temp`, `trash`
- Exact-ish noisy dirs: `.git`, `node_modules`, `.venv`, `venv`, `.next`, `dist`, `build`, …
- Top-level media download trees: `2dl`, `3movie`, `4show`

## User clarifications from session

- **INDEX.md** = map; read when entering a subtree; **not** auto-loaded into Hermes memory.
- **AGENTS.md** = instructions; leave untouched for index-only tasks.
- “All folders in one index” ≠ “INDEX.md file in every folder.”