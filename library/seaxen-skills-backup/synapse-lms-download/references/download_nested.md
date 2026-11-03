# `download_nested.py` — Hierarchical bulk downloader

For Synapse courses with a **section → chapter** hierarchy (e.g., "Basic / MD faculty / Session & Solve Classes"), the flat `download_all.py` dumps every video into a single directory. If the user wants the section/chapter structure preserved on disk, use `download_nested.py` instead.

**Path:** `/root/synapse_dl/download_nested.py` (lives next to `download_all.py`, not in the skill's `scripts/` — because the user customizes it per their account hierarchy and it grew organically out of `download_all.py`).

## When to use it

- Course has a `subject → section → chapter` tree visible on `lms.synapsepg.org/subjects/{subject_id}` pages
- User wants output like `output/Basic/Session_Solve_Classes/Lecture_No_07_Thorax.mp4` instead of everything flat
- Multiple sections (Basic / MD faculty / Session & Solve Classes) where the user has different access per section

## What it does differently from `download_all.py`

| Concern | `download_all.py` (flat) | `download_nested.py` (hierarchical) |
|---|---|---|
| Output structure | `<output_dir>/<title>.mp4` | `<output_dir>/<section>/<chapter>/<title>.mp4` |
| Enumeration | Iterates `localStorage.allLectures` (single subject) | Navigates `subjects/{id}` page, expands each section, then each chapter card |
| State tracking | Same `downloaded_videos` keyed by `stream_id` | Same — schema is identical |
| Skip logic | `is_video_downloaded(state, stream_id)` | Same |
| Resume | If `final_path` exists on disk, re-record state | Same pattern (added 2026-06-19 after a 2x kill incident) |
| 404 handling | Records `permanently_missing_videos` | Same |

## State-file schema (identical to flat)

```json
{
  "downloaded_videos": {
    "<stream_id>": {
      "chapter_id": "69afff828d2df1d11e89e136",
      "chapter_name": "Session & Solve Classes",
      "section": "Basic",
      "subpath": "Basic/Session_Solve_Classes",
      "stream_id": "...",
      "title": "Lecture No:07 Thorax",
      "filename": "Lecture_No_07_Thorax.mp4",
      "size_bytes": 879563069,
      "duration_s": 15565.12,
      "downloaded_at": "2026-06-18T19:43:16+00:00"
    }
  },
  "permanently_missing_videos": {
    "<stream_id>": {"title": "...", "http_code": 404, "failed_at": "..."}
  }
}
```

The `subpath` field records the hierarchical location so a re-run with either script can find the right output directory.

## Invocation

```bash
cd /root/synapse_dl
/root/.venvs/synapse-env/bin/python download_nested.py <account> 2>&1 | tee /root/synapse_dl/<account>_download.log
```

**`--dry-run` limitation:** prints planned section/chapter paths only — not new videos/notes. For Sharif incremental checks, run `scripts/check_sharif_new.py` first, then sync without `--dry-run`. After sync, see `references/sharif-filename-cleanup.md` for `.mp4` / `..mp4` renames.

The first arg is the account name (reads `accounts/<name>.creds` + `accounts/<name>.json`).

## Pair with the progress watcher

This script runs for **2-8 hours** on a typical 50-video course. Pair it with the `synapse_progress.sh` cron recipe in `references/long-running-progress.md` so the user gets a status update every 15 min without burning LLM tokens. Edit those 3 vars in the script to point at this account:
- `STATE=/root/synapse_dl/accounts/<name>.json`
- `LOG=/root/synapse_dl/<name>_download.log`
- `DEST="<output_dir>"` (the parent directory for nested output)

## What broke and got fixed (2026-06-19)

1. **Stale 1-segment failures (not a bug).** The Vidinfra CDN occasionally drops one segment of 3700+ — produces a 0.03% gap in playback. The script logs `⚠ N/M segments failed; glitchy gap` and keeps the file. **The file IS valid** — verify with `ffprobe` before declaring a failure. The author (me) wasted 20 minutes "fixing" a non-bug.

2. **Whole-video 404 (real bug).** When a video is deleted from the LMS, the player returns HTTP 404 on the playlist fetch. The old code retried forever, blocking the entire queue. Fixed: catch `urllib.error.HTTPError` separately, write to `permanently_missing_videos` in state, and skip on every subsequent run.

3. **Per-segment 3-retry (added).** 3 attempts × 30s timeout = ride out CDN blips without re-downloading the whole video.

4. **Resume-from-disk (added).** If the process is killed between remux and state-save, the final `.mp4` exists but state doesn't know. The next run now re-records state from disk if the file is present and >1 MB, instead of re-downloading 1+ GB.

5. **Orphan cleanup.** Crashed runs leave behind `.ts.tmp` and `.remux.mp4` (dot-prefixed) files of 1+ GB each. Clean these up periodically:
    ```bash
    find <output_dir> -name "*.ts.tmp" -o -name "*.remux.mp4" 2>/dev/null | xargs -r rm -f
    ```

## Why this script isn't bundled in the skill

`download_all.py` is the canonical, generic, multi-account entry point — it lives in `scripts/` and is skill-managed. `download_nested.py` is a derivative that was iterated on for the Sharif course specifically. Both share `account_lib.py` for state I/O. If the user runs another hierarchical course, this script can be promoted into the skill with a `--nested` flag on `download_all.py`, but for now keeping it separate avoids bloating the core script.
