# Non-ASCII titles — `--title-match` failure mode

Synapse LMS lecture titles often contain **Bengali/Arabic** text. Passing these as `--title-match` arguments silently returns 0 matches.

## Verified failure (2026-06-25)

```bash
$ download_sagar_one.py 6a243060585213c2b6777ef9 --title-match "Gastroenterology - 02"
Found 0 videos in chapter.
```

But the tile **does exist** on LMS under title `"Gastroenterology - 02(বা�ী �ং�)"`.

## Why it fails

- Terminal encoding mangles Unicode when passing as CLI arg.
- Python string comparison `"Gastroenterology - 02" in "Gastroenterology - 02(বাকী অংশ)"` → actually **True** in Python.
- But the failure happens earlier: `playwright` may enumerate a different title format (the LMS API returns Playwright-rendered text where encoding may differ).
- Or the `--title-match` flag in the script uses `if needle in title` — Playwright may render Bengali combining chars differently.

## Workaround: use `--index` instead

```bash
# 1. Enumerate first (dry-run via fetch_chapter_videos)
/root/.venvs/synapse-env/bin/python download_sagar_one.py 6a243060585213c2b6777ef9 --dry-run
# Output: [0] Environmental..., [1] Gastroenterology - 02(বাকী অংশ)...

# 2. Download by index
/root/.venvs/synapse-env/bin/python download_sagar_one.py 6a243060585213c2b6777ef9 --index 1
```

## When to use `--title-match` vs `--index`

| Case | Use |
|------|-----|
| English-only titles | `--title-match "partial"` OK |
| Bengali/Arabic/Unicode titles | `--index <N>` ONLY (verify via enumerate) |
| Unknown | enumerate first, then decide |

## Status message fallbacks

If the script prints `"Found 0 videos in chapter"`:
1. Chapter may genuinely be empty (notes)
2. OR title-match failed on Unicode
3. Re-run without filter; if videos appear → use `--index`