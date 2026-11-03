---
name: synapse-lms-download
description: Download encrypted HLS videos and PDF notes from Synapse Medical Academy LMS (lms.synapsepg.org) and similar Vidinfra-powered platforms. Multi-account aware - each account has its own creds + state file, so future runs only download new content. Covers login, AES-128 key capture via headless browser, m3u8/segment download, decryption, MP4 remux, PDF/notes harvesting, per-segment retry with 404 short-circuit, resume-from-disk after crashes, and an auto-triggered post-process pass that re-downloads the 1-2 videos that typically have a single failed segment in a 51-video bulk run. Use when a user shares Synapse LMS credentials and asks to download course videos, lecture PDFs, or batch-grab an entire enrollment. Pitfalls - signed KMS key requests, AES-128-CBC IV per segment, MPEG-TS vs MP4 container, React-bound video tile clicking.
version: 3.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [synapse, lms, video, hls, m3u8, aes-128, vidinfra, download, medical, fcps, mrcp, multi-account, state-tracking]
---

# Synapse LMS (Vidinfra) Downloader

End-to-end recipe for downloading encrypted HLS videos + PDF notes from **lms.synapsepg.org** (Synapse Medical Academy) and any other LMS running the same **Vidinfra** player + custom Node/Express backend.

**Multi-account design:** every script supports an **account name** as the first arg. Each account has its own password file + state file at `accounts/<name>.creds` and `accounts/<name>.json`. State tracks every video (by `stream_id`) and every note (by `file_id`) already on disk, so future runs only download new content.

## When to use this skill

Trigger conditions:
- User has login credentials for `lms.synapsepg.org` (or another Vidinfra-powered LMS — recognizable by `player.vidinfra.com` iframes, `kms.vidinfra.com` key endpoints, `*.tenbytecdn.com` HLS CDNs).
- User wants to download course videos for offline study, or bulk-grab lecture PDFs/notes.
- User wants **study notes / high-yield summary** from a downloaded Synapse lecture (see `references/lecture-study-notes.md` — MP4 usually has no subs; vault-align or offer ASR).
- User has hit "protected stream" or "DRM" errors with IDM, browser DevTools, or `yt-dlp` and given up.
- User has multiple accounts and wants each tracked separately (e.g. personal vs colleague, or own vs sponsored course).

## Architecture (one-time discovery, valid as of 2026-06)

| Layer | Tech | Endpoint pattern |
|---|---|---|
| Frontend | React + Ant Design | `https://lms.synapsepg.org/` |
| Backend API | Node/Express | `https://api.synapsepg.org/api/*` |
| Auth | Session token in **localStorage** (not cookies) | `localStorage.sessionId` = `s:<sig>.<hmac>` URL-encoded; `localStorage.student` = profile JSON; passed as `Authorization: <sessionId>` header on every API call |
| Single-session enforcement | YES — server-side, on login | Logging in from a new context invalidates ALL other sessions of the same user (browser tab gets logged out immediately) |
| Video player iframe | Vidinfra | `https://player.vidinfra.com/stream/{content_id}/default/{stream_id}` |
| HLS CDN | tenbytecdn | `https://<random>.tenbytecdn.com/{stream_id}/{quality}/media.m3u8` |
| AES-128 key | Vidinfra KMS | `https://kms.vidinfra.com/v1/keys?content_id={stream_id}` |
| KMS auth | HMAC-SHA256 signed headers (browser-only — no manual reuse) | `x-auth-nonce`, `x-auth-timestamp`, `x-auth-signature` |
| Static assets | tenbyte / S3 | `https://assets.synapsepg.org/{key}` |

**Critical:** The KMS key endpoint requires a signed request that the Vidinfra JS computes in-browser. You **cannot** sign it manually. The trick is to load the player in a headless browser, wait for it to fetch the key, and **capture the key bytes from the response** — then use those bytes to decrypt segments server-side.

## HLS encryption details

- Method: `AES-128-CBC`
- Key URI: `https://kms.vidinfra.com/v1/keys?content_id={stream_id}` (no `IV=` attribute in `#EXT-X-KEY`)
- **Default IV per HLS spec:** media sequence number as 16-byte big-endian integer
  - segment 0 → IV = `\x00 * 16`
  - segment 1 → IV = `\x00...\x01`
  - segment N → IV = `N.to_bytes(16, "big")`
- Container: **MPEG-TS** (not MP4) — remux to true MP4 with `ffmpeg -c copy -movflags +faststart`
- Segment URLs: `https://<cdn>/{stream_id}/{quality}/segment-{N}.ts`
- Playlist master: `/{stream_id}/playlist.m3u8` (lists 720p/480p/etc.)
- Playlist media: `/{stream_id}/{quality}/media.m3u8` (lists segments)

## Scripts (in this skill's `scripts/`)

All scripts are **account-aware** — first arg is the account name, or omit for default `sagar`.

### `download_all.py <account> [--dry-run] [--videos-only] [--notes-only]`

**Bulk entry point** for first-time full-course sync. Scans every chapter, downloads missing videos + notes. Idempotent.

```bash
/root/.venvs/synapse-env/bin/python scripts/download_all.py sagar              # sync everything
/root/.venvs/synapse-env/bin/python scripts/download_all.py sagar --dry-run     # show plan only
/root/.venvs/synapse-env/bin/python scripts/download_all.py sagar --videos-only # only videos
```

**⚠ Use `download_video.py` (single video) or per-script downloads for incremental syncs.** `download_all.py` buffers all segments in RAM before writing any file — on a 2400-segment lecture this means **>1h with no disk output**, and if it gets stuck you have no progress signal. The single-video script prints progress every 200 segments and is safe to run repeatedly.

This is what you want for "I just want everything from this account that's new" — **first run only**. For subsequent "check for new lectures + download" calls, prefer the per-video path described in pitfall 39 below.

### `download_video.py [<account>] <lecture_id> [video_index] [output_name]`

Downloads ONE video from a specific chapter by index.

```bash
/root/.venvs/synapse-env/bin/python scripts/download_video.py sagar 6a243060585213c2b6777ef9 0
/root/.venvs/synapse-env/bin/python scripts/download_video.py 6a243060585213c2b6777ef9 0  # default account
```

- Skips automatically if `stream_id` is already in state
- Reads creds from `accounts/<account>.creds`
- Output: `<state.output_dir>/<title>.mp4` (or override with 4th arg)
- Auto-remuxes MPEG-TS → MP4

### `download_sagar_one.py` (host: `/root/synapse_dl/`) — **Sagar single new video**

**Default for** "new video in sagar account" when dry-run shows **one** missing lecture in a flat chapter (FCPS). Wraps `download_nested.fetch_chapter_videos` + `download_and_decrypt` (concurrency 12, 30s timeouts, progress every 200 segments). Same pipeline that completed Gastro-02 quickly.

```bash
cd /root/synapse_dl
PYTHONUNBUFFERED=1 /root/.venvs/synapse-env/bin/python \
  download_sagar_one.py 6a243060585213c2b6777ef9 --index 0
# or: --title-match "partial title"
```

- Not bundled in the skill `scripts/` dir — lives next to `download_nested.py` on this host
- Updates `accounts/sagar.json` on success
- See `references/incremental-sync.md` for dry-run → execute workflow and stuck-run triage

### `download_notes.py [<account>] <chapter_id> [output_dir]`

Downloads all PDFs/PPTs from a chapter's "Notes" tab.

```bash
/root/.venvs/synapse-env/bin/python scripts/download_notes.py sagar 6a251ab2585213c2b6778499
```

- Skips files already in state
- Output: `<state.output_dir>/notes/<sanitized_title>.<ext>`

### `account_lib.py`

Shared state I/O library. Other scripts import from it. Don't run directly.

### `inspect_chapter.py`

| `inspect_chapter.py` | Helper to log in and dump the lecture's video card titles + raw API response. Use when first exploring a course or debugging. **NOTE:** doesn't read `.creds` — set `SYNAPSE_USER` and put creds at `scripts/.creds` if you want it to work. |

### `organize_by_chapter.py <source_dir> <target_dir>`

Moves flat Sagar downloads into Davidson chapter folders (`/mnt/tb/synapse_26_by_chapter`). **Auto-runs** `normalize_chapter_filenames.py` at the end. See `references/organize-after-download.md`.

### `normalize_chapter_filenames.py`

Cleans ugly LMS names (double `.mp4`, `_pdf` suffixes, spaces) under the organized tree; updates `accounts/sagar.json` filenames.

### `organize_sagar_after_sync.sh`

Wrapper: organize + normalize. **Run without being asked** after every Sagar incremental download.

### `check_sharif_new.py`

Enumerates Sharif nested chapters vs state (`NEW_VIDEOS` / `NEW_NOTES`). Use before `download_nested.py sharif` — `--dry-run` on nested does **not** list new vs existing items, only planned chapters. Host: needs `/root/synapse_dl/download_nested.py` on `PYTHONPATH`.

### `normalize_sharif_filenames.py`

Post-download cleanup for Sharif's nested tree (`/mnt/tb/Syn MD 26`). Renames `.mp4`, `..mp4`, trailing-dot titles, and `_PDF...pdf` artifacts; syncs `accounts/sharif.json` filenames. Run after `download_nested.py sharif` when LMS titles sanitize badly.

### `setup.sh`

One-time venv install (idempotent). Creates the venv at `$HOME/.venvs/synapse-env` by default (override with `SYNAPSE_VENV_DIR`). **Does NOT use `/tmp`** because /tmp is tmpfs on this host and gets cleared between sessions. See `references/content-counting.md` for how to enumerate actual course content from `localStorage.allLectures`.

### `synapse_session_inject.py <account> <target_url>`

Open a Playwright browser with a pre-captured `localStorage` session (no login form submitted). Use when you want to download without kicking the user out of their live browser. Capture once via the user's browser console: `localStorage.getItem('student')` + `localStorage.getItem('sessionId')`, save to `accounts/<account>.session.json`, then run this script. See `references/synapse-localstorage-auth.md` for the full pattern including the URL-encoding gotcha and session-refresh cadence.

### `backfill_failures.py <logfile> <account>`

Parses a download log for `⚠ N/M segments failed` warnings and marks the corresponding state entries with `has_failures=true`. Use this when the bulk download is **already running with old code** (no `has_failures` state marker being written) — without backfill, `--fix-failures` sees nothing to fix and exits silently. Idempotent. See `references/post-processing-failed-videos.md`.

### `post_process.sh [account]`

End-to-end post-processing pipeline. Runs `backfill_failures.py` then `--fix-failures` mode, then prints a final state summary. Idempotent — safe to re-run.

### `synapse_post_process.sh [account]`

Watchdog script (cron every 5 min). Detects when the main download process has exited AND state has `has_failures` entries; runs `post_process.sh` once and creates a marker file to prevent re-runs. Pair with `cronjob action=create ... no_agent=true schedule="every 5m"`.

## Account layout

```
/root/synapse_dl/accounts/         (or $SYNAPSE_ACCOUNTS_DIR)
├── sagar.creds                    chmod 600, contains password on single line
├── sagar.json                     state: downloaded videos/notes, output dir
├── <other_account>.creds
└── <other_account>.json
```

`state.json` schema:
```json
{
  "account_name": "sagar",
  "username": "01683048886",
  "output_dir": "/mnt/tb/synapse_26",
  "notes_subdir": "notes",
  "created_at": "2026-06-18T23:00:00+06:00",
  "last_run":    "2026-06-18T23:36:00+06:00",
  "downloaded_videos": {
    "<stream_id>": {chapter_id, chapter_name, stream_id, title, filename, size_bytes, duration_s, downloaded_at}
  },
  "downloaded_notes": {
    "<file_id>":    {chapter_id, chapter_name, title, filename, s3_key, size_bytes, downloaded_at}
  }
}
```

Keys:
- `stream_id` = last segment of iframe URL `https://player.vidinfra.com/stream/{content_id}/default/{stream_id}` — unique per video
- `file_id`   = `_id` from the `/api/lecture/{id}` response — unique per note file

## Quickstart (full course, one account)

```bash
# 1. Setup (one-time)
/root/.hermes/skills/synapse-lms-download/scripts/setup.sh

# 2. Register the account: create creds + seed state file
ACCT=sagar
printf '%s' 'LMS_PASSWORD_HERE' > /root/synapse_dl/accounts/${ACCT}.creds
chmod 600 /root/synapse_dl/accounts/${ACCT}.creds

# 3. Seed the state with the right username + output dir (edit the JSON or use a one-liner):
/root/.venvs/synapse-env/bin/python -c "
import json, pathlib
p = pathlib.Path('/root/synapse_dl/accounts/${ACCT}.json')
if not p.exists():
    p.write_text(json.dumps({
        'account_name': '${ACCT}',
        'username': '01XXXXXXXXX',  # ← edit
        'output_dir': '/mnt/tb/${ACCT}',  # ← edit
        'notes_subdir': 'notes',
        'created_at': '2026-06-18T23:00:00+06:00',
        'last_run':    '2026-06-18T23:00:00+06:00',
        'downloaded_videos': {},
        'downloaded_notes': {},
    }, indent=2))
print('Seeded:', p)
"

# 4. Sync everything:
/root/.venvs/synapse-env/bin/python scripts/download_all.py ${ACCT} --dry-run  # preview
/root/.venvs/synapse-env/bin/python scripts/download_all.py ${ACCT}            # do it

# 5. Next month, when new lectures drop, just rerun step 4.
```

## Multi-account pattern

```bash
# Add a second account
printf '%s' 'OTHER_PASSWORD' > /root/synapse_dl/accounts/other.creds
chmod 600 /root/synapse_dl/accounts/other.creds
# (seed its state with a different username + output_dir)

# Sync each account independently
scripts/download_all.py sagar
scripts/download_all.py other
```

Override username/output at runtime without editing state:
```bash
SYNAPSE_USER=01XXXXXXXXX SYNAPSE_OUT=/custom/path scripts/download_all.py sagar
```

## Long-running downloads — progress visibility

A full course sync can take 2–8 hours (51 videos × 15 min each, 16 concurrent). The user will absolutely ask "is it still running? what's the progress?" long before the foreground process ends. Don't make them wait in silence. Set up a progress reporter **before** kicking off the bulk download.

### Pattern: bash status script + no_agent cron job

**1. Write a small status script** at `~/.hermes/scripts/synapse_progress.sh`. It reads the state file, the log tail, and the destination directory, and emits a clean Discord-friendly status block. Bail silently if the download process is gone (read pid from `/tmp/synapse_dl.pid`, then `kill -0 $pid`).

**2. Schedule it with `cronjob` `no_agent=true`** so the script runs every 15 min and auto-delivers to the origin Discord channel. No LLM tokens burned.

```bash
cronjob action=create name="Synapse download progress" \
  no_agent=true script=synapse_progress.sh \
  schedule="every 15m" deliver=origin
```

**3. The user only gets one notification per cron tick** (the script's stdout). When the download process exits, the script detects via PID check and emits a one-line "⛔ process exited" — then stays quiet on subsequent ticks. No spam.

**4. The user may ask for progress updates even more frequently than the natural tick.** In the 2026-06 Sharif run, the user explicitly asked "is those are downloading all ?" mid-run and "what about now ? it will not notify after each file download ? any way to I see progress?" shortly after the first status ping. They wanted visibility into per-video progress, not just per-tick snapshots. Two patterns help:

- The status script should always include the **current downloading title** (parse from `↓ [N] Title...` lines) AND the **latest finished file** (parse from `✓ filename (size MB)` lines) so the user can confirm progress between ticks.
- The script is safe to `tail -f sharif_download.log` interactively. Encourage the user to run that in their own terminal if they want second-by-second visibility — don't poll for them.

When the user says "yes every 15 min" or "yes every X min", they're giving an explicit answer to "do you want more frequent updates?" — set the cron schedule to match. The default every-15m is a good baseline; longer bulk runs (51+ videos) can drop to every-30m to reduce noise, but never less frequent than every-30m for an active multi-hour download.

### What the status block should contain

```
📥 Synapse download progress — 02:32 (uptime 11:04)
✅ Videos done: 3  📝 Notes: 0
💾 Disk used: 2.7G (3 .mp4 files on disk)
🔄 Now downloading:
↓ [3] Review Class:Physiology Masterclass,,.....
3800/3861 segments (1056.4 MB, 98.4%)  failures=0
📌 Latest finished: ✓ Lecture_No_05_Embryology.mp4 (871.0 MB)
```

**Where to read each value:**
- Counts + last run → `accounts/<name>.json` (`downloaded_videos` keys, `last_run`)
- Now downloading title → `grep -E "^\s+↓ \[" log` tail
- Current progress % → `grep -E "segments \(.*%\)$" log` tail
- Latest finished file → `grep -E "✓ Lecture" log` tail
- Disk used → `du -sh $DEST`
- Uptime → `ps -o etime= -p $PID`

See `references/long-running-progress.md` for a complete, copy-pasteable status script and the exact cron job definition. See `references/incremental-sync.md` for the dry-run → background sync workflow when the user asks for new videos/notes only. See `references/lecture-study-notes.md` when the user asks to **learn from / note** a downloaded lecture (no subs → vault high-yield or optional whisper). See `references/download_nested.md` for the hierarchical variant used on multi-section courses (preserves `output/Section/Chapter/` structure on disk). See `references/patching-live-bulk-runs.md` for the in-memory-vs-patch trap (Python doesn't reload modules mid-run) and the delete-then-redownload hazard in `--fix-failures`. See `references/synapse-localstorage-auth.md` for capturing and injecting the user's `localStorage` session without triggering a login (avoids logging them out). See `references/non-ascii-titles.md` when `--title-match` silently returns 0 videos on Bengali/Arabic-titled LMS tiles (fall back to `--index` by dry-run enumeration). See `references/organize-after-download.md` for mandatory Sagar organize+normalize after incremental downloads. See `references/sharif-filename-cleanup.md` after Sharif nested sync when filenames are `.mp4` or have `..` before the extension.

## Post-processing failed videos (re-download pattern)

A 51-video bulk run will produce 1-2 videos with a single failed CDN segment each. The file is technically playable but has a 5-10s gap that can desync audio. The user will want those re-downloaded once at the end, with the old version deleted.

**Pipeline:**

1. `download_nested.py` writes `has_failures: true` + `failure_count: N` to the state entry on every video completion (the new `_dl()` retries each segment 3× with 30s timeout — see pitfall 21).
2. 5-min cron watchdog (`synapse_post_process.sh`) detects when the main download exits AND state has any `has_failures` entries → runs `post_process.sh` once → creates a marker file to prevent re-runs.
3. `post_process.sh` first runs `backfill_failures.py` (parses the log to catch any failures the in-memory old code missed) then `--fix-failures` mode on the main script.
4. `--fix-failures` mode finds all `has_failures=true` entries, deletes their .mp4 + orphan .tmp files, removes them from state, falls through to the normal download loop → re-downloads them with the new retry logic.

**Full reference:** `references/post-processing-failed-videos.md` — includes the post_process.sh script, the watchdog with marker file pattern, and gotchas around re-running when the network is still flaky.

## Discovery workflow (when first encountering an unknown Vidinfra LMS)

1. **Login** → check `localStorage` for the session token
2. **Open a lecture** → find `.student-video-card` divs (or similar)
3. **Click a tile** → an iframe appears with `src="https://player.vidinfra.com/stream/{content_id}/default/{stream_id}"`
4. **Inspect network** in DevTools Network tab — the player will fetch:
   - `GET {cdn}/playlist.m3u8` (master, no auth)
   - `GET {cdn}/{quality}/media.m3u8` (media, no auth)
   - `POST/GET https://kms.vidinfra.com/v1/keys?content_id=...` (with signed headers)
5. **Check the key request** — headers are `x-auth-nonce`, `x-auth-timestamp`, `x-auth-signature`. These are computed in `index.global.js` (the Vidinfra player bundle). **Don't try to replicate them** — capture the key response instead.
6. **Check the `#EXT-X-KEY` tag** in the media playlist — `METHOD=AES-128,URI="..."`. No `IV=` means default IV per spec.
7. **Download segments, decrypt with default IV, concat, remux.**

## Pitfalls (read these first — most failure modes are here)

1. **CDN playlist needs `Referer: https://player.vidinfra.com/` and a desktop `User-Agent`.** Without them, the master playlist still loads (public), but the key endpoint returns 405 / "missing authentication headers". The browser sends these automatically; curl/yt-dlp need them explicit.

2. **KMS endpoint rejects all server-side signed requests** — it checks browser fingerprints (TLS handshake, etc.) via Cloudflare. **You MUST capture the key from a real browser response.** Don't waste time reverse-engineering the JS signing.

3. **AES-128-CBC IV is per-segment, not constant.** When the playlist has no `IV=` attribute, use `segment_id.to_bytes(16, "big")` for each segment's IV. Forgetting this gives garbled output that looks "encrypted" but isn't — the first segment might play and the rest won't.

4. **MPEG-TS ≠ MP4. NEVER claim a file is `.mp4` without `ffprobe` confirming `format_name=mov,mp4,m4a`.** Concatenated `.ts` files give you a `.ts` even if you rename it. Some players (older Android) refuse to play it. Always remux FIRST, then label: `ffmpeg -i input.ts -c copy -movflags +faststart output.mp4` — instant, no quality loss. **The user catches this kind of mislabeling immediately** — run ffprobe and only name the file `.mp4` after the remux succeeds.

5. **PKCS7 padding on the last segment.** The last segment is padded to 16 bytes. Strip it: check `data[-1]`, if 1-16 and `data[-N:] == bytes([N])*N`, truncate. Forgetting this corrupts the last frame but VLC usually plays through.

6. **The CDN URL changes per video.** Don't hardcode the `tenbytecdn.com` subdomain — it's random per stream. Always extract from the iframe URL or the player network log.

7. **React-bound onClick handlers all have the SAME minified source string** like `async()=>{p(!0),g(!0)}` but bind to different data via React closure. There's no `data-id` or `data-vc` attribute on the card. Click by **index** in the `.student-video-card` selector, then look up the title from the same index.

8. **Session is in localStorage, not cookies.** `localStorage.sessionId` is a `s:<sig>.<hmac>` string, and you pass it as the `Authorization: <sessionId>` header (Bearer-style) when calling the API. `document.cookie` will be empty. **The `student` localStorage key holds the profile JSON** (with `_id`, `name`, `phone`, `batch`); both keys must be set together for the session to be considered valid. To capture a session without logging in yourself, run `localStorage.getItem('sessionId')` and `localStorage.getItem('student')` in the user's browser console while they're logged in, then save to `accounts/<name>.session.json`. The script `synapse_session_inject.py` injects these values into a fresh Playwright context before navigation, so no login form is submitted and the user's live browser session is never disturbed. See `references/synapse-localstorage-auth.md` for the full pattern.

28. **Synapse enforces single-session-per-user.** When the script logs in, the user's live browser session is invalidated on the next page load — they see "session expired" and must log in again. This is server-side, not cookie-based, and there's no way to opt out. For bulk downloads: either (a) login from a headless context once, capture all needed keys quickly, then close before the user notices, (b) capture the user's `localStorage.sessionId` + `localStorage.student` from their browser console and inject into the headless context (no login form submitted at all — the user keeps their session), or (c) schedule the download for when the user isn't using the LMS. For the 2026-06 Sharif run, option (a) caused the user to get logged out from their Sagar account during multi-chapter capture — option (b) would have avoided that.

39. **Incremental download: `download_video.py` over `download_all.py` for small batches.** When the user asks "check for new lectures and download", use `download_video.py` (or the account-specific `download_sagar_one.py`) with N `--title-match` rather than bulk `download_all.py`. Reasons:

- `download_all.py` holds **all segments in RAM** before writing the first byte. A 2400-segment lecture takes ~1h+ with zero visible output — the user thinks it's stuck.
- Bulk script piped through `tee` often **buffers stderr**, so progress lines don't appear until the end.
- Single-video script prints `200/2390 segments (x=0` live every ~30s and remuxes immediately on completion.

**Primary entry point**: `download_all.py` = first-time full sync; `download_video.py` / per-account single = incremental additions. Always run `download_all.py --dry-run` (or fetch + inspect the chapter API directly) to enumerate what's new before downloading.

```bash
# Preferred incremental workflow:
cd /root/synapse_dl
/root/.venvs/synapse-env/bin/python download_sagar_one.py 6a243060585213c2b6777ef9 --index 1  # download video by position
/root/.venvs/synapse-env/bin/python download_notes.py sagar 6a251ab2585213c2b6778499  # notes only
```

**40. Bengali / non-ASCII LMS titles break `--title-match`.** Synapse lecture titles may contain Bengali script (e.g., "Gastroenterology - 02(বাকী অংশ)"). Passing these as `--title-match` arguments can fail because terminal encoding mangles the Unicode before Python sees it. **Workaround: match by video index (`--index N`) instead of title.** To find the index, enumerate first, then pass the numeric index. The `--dry-run` output from `download_all.py` shows `[0] Title... [1] Title...` — use that number.

9. **`student-video-card-wrap` vs `student-video-card`:** the outer wrapper is `student-video-card-wrap` (no click), the inner card is `student-video-card` (clickable). Click the inner one.

10. **Two URL patterns per chapter:**
    - `/videos/{chapter_id}/lecture` → video tiles (often empty for notes-only chapters)
    - `/notes/{chapter_id}/lecture` → file tiles (DOWNLOAD buttons)
    The `chapter_id` is the same in both URLs; the path is the only difference.

11. **Lecture API has `isPublished: false` for many files.** Doesn't mean they're unavailable — the DOWNLOAD button still works. Filter by `key` presence, not `isPublished`.

12. **Don't enable sandbox on the headless browser** unless you have `--no-sandbox` flag (root containers need this). `p.chromium.launch(args=["--no-sandbox"])`.

13. **Don't trust marketing copy for content counts.** A course brochure that says "50 Classes" may have only 2 videoContents actually published. **Always enumerate `localStorage.allLectures` and count `videoContents.length` / `fileContents.length` per chapter** before reporting totals. The user explicitly corrected an over-count from "49 other lectures" to "I only see 2" — this kind of inflation destroys trust. See `references/content-counting.md` for the one-liner recipe.

14. **Don't put virtualenvs in `/tmp` on this host.** `/tmp` is tmpfs and gets cleared between sessions — your venv (with chromium + packages) will be wiped and you'll re-install everything next session. Use `/root/.venvs/<name>/` (persistent on `/dev/sdb2`) or any other non-tmpfs location. The setup script defaults to the skill's own `.venv/` dir which is also persistent.

15. **The `write_file` tool can silently corrupt arguments** when the content has special characters (passwords with `@`, function defs whose body looks like a keyword, etc.). After writing a file with sensitive/dynamic content, **always `read_file` it back to verify** before reporting the file as saved. If a password or other critical value looks mangled, store it in a separate `.creds` file with `chmod 600` and have the script read it at runtime instead of inlining it as a string literal in the script.

16. **Always run `download_all.py --dry-run` first when starting on a new account.** Shows every chapter, every video title, and exactly what would be downloaded — no risk of accidentally re-grabbing 1 GB of files you already have.

17. **Don't trust pipeline log error messages about file existence — always verify with `ls` and `ffprobe` before declaring a download failed or proposing destructive fixes.** The pipeline logs `Errno 2: No such file or directory: '...mp4'` at the END of a successful download, because the state-save block runs after a separate code path that doesn't have the final_path variable in scope. The file IS on disk, valid, and the state file IS updated. Proposed "fixes" based on log analysis (delete the file, rewrite the rename logic) corrupt a working pipeline. The authoritative verification is one `ffprobe` call:
    ```bash
    ls -la /path/to/file.mp4                          # exists + non-zero
    ffprobe -v error -show_entries format=format_name,duration,size file.mp4
    ```
    If `format_name=mov,mp4,m4a` and duration looks right, the file is good. **The state file (`accounts/<name>.json` → `downloaded_videos` keys) is the source of truth for "already done"** — not the log, not the pipeline's exit code on a single iteration, not the `tee` output. Run all three before reporting failure: filesystem check, ffprobe, and state-file inspection. This lesson saved a 1.8 GB Sharif run from being nuked.

18. **`bash: [NNNNN: 1 (255)] tcsetattr: Inappropriate ioctl for device` in a `tee`-piped log is harmless noise.** It comes from the shell trying to set terminal modes on a non-TTY stdout (true in any backgrounded process or when piped to a log). Don't kill the run over it; don't grep-and-grep for "real" errors as if it were one. The pipeline is fine if subsequent "Downloaded N/M segments" / "✓ Lecture" lines keep appearing.

19. **The `download_nested.py` variant is for courses with section/chapter hierarchy.** It creates a directory tree like `output/Section_Name/Chapter_Name/Lecture_Title.mp4` based on the `subject → section → chapter` structure in the LMS, instead of dumping everything flat. Use it when a course has multiple sections (e.g., "Basic" / "MD faculty" / "Session & Solve Classes") and the user wants to preserve that organization on disk. The flat `download_all.py` is fine for single-section courses or when output structure doesn't matter. The script lives at `/root/synapse_dl/download_nested.py` (not bundled in the skill) and is invoked as `download_nested.py <account>`. State-file schema is identical to `download_all.py`, so a re-run with either script picks up where the other left off.

20. **A single failed segment (1 out of 3700+) is normal and acceptable.** The Vidinfra CDN occasionally drops one segment request (timeout, 5xx, brief network blip). The pipeline's standard behavior is: log `FAIL seg N`, continue downloading the rest, then at decrypt time **skip** the missing segment and emit a `⚠ N/M segments failed; output will have a glitchy gap` warning. Result: a 0.03% gap in playback (~5-10 seconds) that is barely noticeable and the file is still valid. **Do NOT delete or re-download the file over this warning** — the user will not perceive the gap and the alternative (re-downloading 1.3 GB to get 0.03% more) is wasteful. The `max_failures=20` abort threshold is the right balance: one segment glitch → keep going; CDN clearly broken (>20 fails) → abort with an error.

21. **Per-segment retry with 404 short-circuit.** A single segment that returns HTTP 404 is **permanently gone** (CDN file deleted, not a transient blip) — don't retry it. A timeout or 5xx, on the other hand, is worth retrying. Pattern that works:
    ```python
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return sid, r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:    # permanent — don't retry
                raise
            last_err = e
        except Exception as e:
            last_err = e
    raise last_err
    ```
    3 attempts × 30s timeout = up to 90s of patience per segment, which is enough to ride out CDN blips without blowing the budget.

22. **Whole-video HTTP 404 (entire playlist or stream gone) is a different problem from per-segment 404.** The video has been deleted from the LMS and will never download. The state file must record this so future runs skip it instantly instead of retrying forever. Pattern:
    ```json
    "permanently_missing_videos": {
      "<stream_id>": {"title": "...", "http_code": 404, "failed_at": "2026-..."}
    }
    ```
    Check this set at the top of the download loop and `continue` if present. Catch `urllib.error.HTTPError` separately from generic `Exception` so you can distinguish "permanently missing" from "transient error, try next run".

23. **Resume-from-disk fallback for crashed runs.** If the download process is killed mid-download, the final `.mp4` may already exist on disk from a successful remux but the state file may not have been updated. On the next run, check before re-downloading:
    ```python
    if final_path.exists() and final_path.stat().st_size > 1024 * 1024:
        record_video(state, ...)
        save_state(account, state)
        print(f"      ✓ {out_name} (resumed, {size/1024/1024:.1f} MB)")
        continue
    ```
    Saves hours of re-downloading after a `kill -9` or OOM. Also clean up any orphan `.ts.tmp` and `.remux.mp4` (dot-prefixed) files from the crashed run — they will be 1+ GB and waste disk space.

24. **A patch to the running script is invisible to the running process.** Python loads modules once at startup; `patch` on the .py file does not reload the interpreter. If a 6-hour bulk download is already in flight when you improve `_dl()` with retries or add 404 handling, those improvements only take effect on the **next** run. Three implications: (a) don't bother patching the live process — just queue the changes for the next run; (b) tell the user explicitly that the fix applies to future runs, not the current one; (c) verify with `ls` and the state file that progress is real, not in-memory. The 51-video Sharif run shipped with the old code, accumulated ~5-10 "1 failed segment" warnings, and was then re-downloaded with the new code at the end — and that's the correct workflow, not a bug.

25. **Per-video failure tracking + post-process re-download.** Long bulk runs (51 videos × 15 min) will produce 1-2 videos with a single failed CDN segment each. The file is technically playable but has a 5-10s gap that can desync audio or feel jarring. The user will want those re-downloaded once at the end, deleting the old version. Pattern: add `has_failures: true` and `failure_count: N` to each `downloaded_videos` state entry on completion; add a `--fix-failures` mode to the main script that finds all `has_failures=true` entries, deletes their .mp4s + orphan .tmp files, removes them from state, and falls through to the main download loop (which re-downloads them with the new per-segment retry logic). For runs started before the patch is loaded, use `backfill_failures.py` to parse the log file and mark the same state entries retroactively. Wire it all together with a 5-min cron watchdog (`synapse_post_process.sh`) that triggers post-process the moment the main download exits. See `references/post-processing-failed-videos.md` for the full pattern including the watchdog marker file and the gotchas around re-running post-process when the network is still flaky.

26. **The post-process delete-then-redownload flow can lose data if the new code has a bug.** `--fix-failures` does `old_path.unlink()` then falls through to the main download loop. If the re-download hits any error (e.g. an undefined constant in a refactored helper, network outage, missing key capture), the user is now in a **worse** state than before: the file is gone from disk AND from state, with no immediate re-download. **Before letting `--fix-failures` run for the first time after a code change, dry-run it** by writing the `to_fix` list to stdout and confirming it matches expectations, OR run a smoke test on a single known-broken video. Better: add a `--fix-failures-dry-run` flag that just prints what would be deleted. In the 2026-06-19 Sharif run, the first post-process pass had a `NameError: SEG_URL_TEMPLATE is not defined` in a refactored `_dl()` helper, which wiped the .mp4s of 2 valid videos before they could be re-saved. The damage was repaired by re-running the main script (which picked up the missing videos since they were no longer in state), but only because the `--fix-failures` deletes happened to land in a section that the next run would re-attempt anyway. **Lesson: any new helper that touches segment URLs, the KMS key path, or the remux step must be smoke-tested end-to-end before letting post-process run unattended.**

27. **A "too many 404s" wall in a single chapter is the LMS pruning old content, not a credential or network problem.** In the Sharif 51-video run, an entire chapter produced 7-8 consecutive HTTP 404s on the first attempt — every video in a "Session & Solve Classes" archive had been deleted from the LMS. The download completes in ~1 second per 404 (no segments transferred), so the cost of running through the 404 wall is negligible. The signal is valuable: it tells you which chapters the user can't actually access anymore, which is information the user wants to know. Make sure 404s are persisted to `permanently_missing_videos` in state and the post-process pipeline reports the count so the user can see "8 videos are no longer available on the LMS" at the end. Don't suppress the 404 lines from the progress watcher — the user wants to see them as a status signal, not a hidden failure.

28. **When the user says "videos are in the wrong folder," verify against the live LMS before re-organizing.** The chapter_id → folder name mapping comes from `default_sharif_config()` (or equivalent), which is built from URL → chapter_id → folder-name tuples supplied by the user at setup time. If the original URL list was wrong, the script will faithfully put the right videos in the wrong-named folder. The user only sees "Session_Solve_Classes/" with physiology lectures and concludes the script swapped them — but the LMS itself labels chapter `69afff828d2df1d11e89e136` as "Session & Solve Classes" and chapter `69218e1c373bbf67cff792cd` as "Intensive Care Core Batch-5", and that's what the LMS shows. To verify: log in via Playwright, navigate to each chapter URL from the config, list `.student-video-card` titles, compare with the disk folder contents. In the 2026-06 Sharif run, the user reported videos in the wrong folder; a 90-second re-inspection showed the script was correctly mirroring the LMS — the chapter names are simply misleading. Don't reorganize folders or "fix" the config until you've seen what the LMS actually contains. If the user wants clearer folder names despite the LMS labels, rename the folders in-place (`mv Basic/Session_Solve_Classes Basic/Physiology_Lectures`); the files don't need to be re-downloaded.

29. **Session injection via captured localStorage values does NOT work for Synapse.** During the 2026-06 Sharif run, we tried `synapse_session_inject.py` — inject the user's `localStorage.student` + `localStorage.sessionId` into a fresh Playwright context, also set the `connect.sid` cookie to the URL-decoded sessionId value, then navigate. The server responded by redirecting to `/login` and `localStorage` came back empty. This confirms what pitfall 28 says: the server binds sessions to a browser fingerprint (TLS handshake, IP, UA, or some combination) that can't be replayed from a different headless context. Don't invest time reverse-engineering session injection for Synapse — it won't work. The viable alternative is one-shot scripted login from the headless browser (option A in pitfall 28), accepting the user gets logged out from their live session exactly once per download batch.

30. **The `creds` file stores the password only — the username lives in `state.json`.** `accounts/<name>.creds` is a single line: the password. The matching `accounts/<name>.json` has `"username": "01XXXXXXXXX"` at the top. When writing a quick utility script that needs to log in (e.g. for ad-hoc LMS inspection), read username from `load_state(name)["username"]` and password from `get_password(name)`, not from a single creds file split on `:` or `\n`. The split-on-newline approach fails silently when the creds file has no newline (which it shouldn't, but real files do).

31. **Diff by stream_id, NEVER by title.** Same video can appear under different titles across LMS updates (titles get trimmed, trailing dots/dashes added/removed, typos like "Microbiolology" introduced, words reordered). A title-based diff produces false positives and re-downloads already-downloaded videos. Verified 2026-06-22 on Sharif: 11 "new" titles detected, but only 1 had a genuinely new stream_id; the other 10 had stream_ids already in state and were re-downloaded (3.16 GB wasted). **Always do stream_id-based diff and verify with MD5 before deleting duplicates.** Pattern:
   ```python
   # CORRECT
   new_videos = [v for v in lms_videos if v['stream_id'] not in state_sids]
   # WRONG — false positives
   new_videos = [v for v in lms_videos if v['title'] not in state_titles]
   ```
   When you do re-download duplicates (it happens), find them by **MD5 match** against state-tracked files (same stream_id = same content), then delete the orphan. The match is exact — same stream_id always produces byte-identical AES-decrypted output.

32. **CDN segment URLs include `/720p/` (or other quality) — never strip it.** The m3u8 playlist lives at `{cdn_base}/{quality}/media.m3u8` and segment URLs are `{cdn_base}/{quality}/segment-N.ts`. If you only capture the CDN base (`{cdn_base}`) and append `/segment-N.ts` directly, every segment returns 404. Symptom: key capture works, playlist fetch works, but 100% of segments 404. Fix: parse the playlist and use the actual segment URLs from it, not a reconstructed path. The playlist paths may be relative (`segment-N.ts` → resolve against `media.m3u8`'s directory, which includes `/720p/`) or absolute.

33. **KMS key capture requires `page.on('response')` + `response.body()` — NOT `page.evaluate(fetch(...))`.** Two failure modes:
    - Python `requests.get(kms_url)` with proper headers → 403 (Cloudflare fingerprint check rejects non-browser TLS).
    - `page.evaluate(...)` doing `fetch(kms_url)` from the lms.synapsepg.org page → CORS error (kms.vidinfra.com doesn't send CORS headers, and the iframe origin is different from the parent).
    Correct pattern: register a global `page.on("response", ...)` listener that calls `await response.body()` for any kms.vidinfra.com URL, and pair that KMS URL with the corresponding iframe's content_id/stream_id. The browser's own signed request fetches the key; you just capture the body.

34. **Use a `requests.Session()` with bounded connection pool for segment downloads, not raw urllib.** ThreadPoolExecutor + raw `urllib.request.urlopen` leaks file descriptors under load (urllib doesn't always close connections cleanly) — symptom: `OSError: [Errno 24] Too many open files` after a few videos. Pattern:
    ```python
    SESSION = requests.Session()
    SESSION.headers.update({'User-Agent': '...', 'Referer': 'https://player.vidinfra.com/', 'Origin': 'https://player.vidinfra.com'})
    adapter = HTTPAdapter(pool_connections=4, pool_maxsize=8, max_retries=Retry(total=2, backoff_factor=0.5))
    SESSION.mount('https://', adapter)
    SESSION.mount('http://', adapter)
    ```
    Concurrency of 8 (not 16) is the sweet spot for CDN bandwidth without FD exhaustion.

35. **The `allLectures` localStorage has videoContents/fileContents as lists of 24-char IDs, not full objects.** To get titles + stream_ids, fetch `/api/lecture/{chapter_id}` per chapter. The lecture response gives full video objects with `title`, `URL` (which contains both content_id and stream_id in `https://player.vidinfra.com/stream/{content_id}/default/{stream_id}`), and `key` for the S3 file URL. Don't try to use the IDs from `allLectures` directly — they need a second API call to resolve.

36. **Notes are downloaded without auth — just a public S3 URL.** Pattern: `https://assets.synapsepg.org/{key}` where `key` is the `key` field from the lecture API fileContents (e.g. `directory/775210851440.pdf`). No cookies, no Authorization header, no Referer needed. Just `requests.get(url).content` and write to disk.

37. **State-save bug: skip-on-exists must still update state.** If a download already exists on disk, the script prints "exists" and continues — but if the corresponding state entry was never written (e.g. from a previous failed run that downloaded but didn't save state), the file is orphaned forever. Fix:
    ```python
    if out.exists() and out.stat().st_size > 1024:
        if file_id not in state['downloaded_notes']:
            state['downloaded_notes'][file_id] = {...metadata...}
            save_state(account, state)  # critical: save even on skip
        print(f"  ✓ {title} (exists)")
        continue
    ```
    Verified in the 2026-06-22 Sharif run: 4 notes downloaded in an early failed run, then skipped in later runs, leaving them as disk-only orphans not tracked in state.

38. **Old runs leave orphaned files when state entries are overwritten.** When a re-download happens with the same stream_id but different filename (because LMS title changed), the OLD .mp4 on disk isn't deleted by the new download — only the new file is added to state. Result: two copies of the same video on disk, only one in state. Cleanup: after every download pass, run a MD5-based deduplication that finds files on disk not in state, computes their hash, matches against state-tracked files, and deletes confirmed duplicates. Always show the user the to-delete list before deleting.

39. **Bundled `download_all.py` can look "stuck" on one long lecture** — holds all segments in RAM before writing disk; piped `tee` may buffer stderr so only sporadic `ERR seg` lines appear for 30–90+ minutes while `VmRSS` sits ~900 MB and CPU ~0.2%. v2.6+ adds progress every 200 segments **when stderr is unbuffered** (`PYTHONUNBUFFERED=1`). For a **single new Sagar video**, use host `download_sagar_one.py` instead (verified 2026-06-25: `download_all` hung 1h27m; `download_sagar_one` showed 40%+ within ~1 min). See `references/incremental-sync.md`.

40. **`download_all.py` remux left MP4 bytes on a dotfile** — `remux()` writes MP4 into `.Title.mp4.ts.tmp` but `final_path` was `Title.mp4`; `stat()` on final failed unless renamed. Always `tmp_path.rename(final_path)` after successful remux (v2.6+).

48. **Stop narrating, start executing.** The user will repeat a request 3-4 times with rising frustration while the agent produces patch→read→patch→read loops with no actual run. The correct response to "check+download" is one terminal call, one background launch, one `process wait` or `tail -f`, then a status report. Patches belong in the same turn as the launch that exercises them — never "let me read the file one more time first." If the script compiles, launch it. The state file + `ffprobe` will tell you in 10 seconds whether it worked; spending 20 turns on the patch is worse than running an imperfect version and seeing what it actually does. **Rule of thumb: any task where the agent has issued ≥3 tool calls without changing disk state is a thrashing loop. Stop, launch the best current code, then iterate based on observed output.**

54. **The 6-step gate before any background `download_all.py` sync for the sagar/sharif account class.** The historical failure mode is a 6-12-hour background run that finishes `exit_code 0` but produced `videos recorded: 0` because one of three bugs hit during a 4-day silence: (a) Playwright per-card key capture silently returning empty, (b) `state.downloaded_videos` getting wiped while `output_dir` is also wrong so the seeder can't match on-disk mp4s, (c) sharif-leak 404s being retried for hours. **Never go straight from "user said download" to `terminal(background=true, notify=true)` with `download_all.py`.** Gate the launch with these six steps in order, foreground, with on-disk verify at each step:
    1. **Inventory.** `find` on the target + source. Read `accounts/<name>.json` to ground-truth `downloaded_videos`/`downloaded_notes`/`permanently_missing_videos` counts vs what's on disk. If a previous seeder put `size_bytes=None` in any entry, fix that before step 5 (the dry-run summary will crash on `None + int`).
    2. **Playwright capture proof.** Call `get_video_info_for_chapter` on the largest chapter (Davidson's Review Batch-02 = 32 cards on sagar) and verify it returns `(stream_id, kms_key, title)` tuples with `len(key) == 16` for ≥30 cards. If it returns 0, fix `_dl`/`page.on('response')` first — do not background-run, the failure will be silent.
    3. **Re-curl the permanently-missing stream_ids** with the fresh login session. Confirm 13/13 are still 404 (real dead) or any 200 (token bug = new data). Record results to `step1_recurl_404s.json`. **Identify sharif-leak titles by keyword** ("anatomy master", "back up lecture", "pathology+physiology+pharmacology", "residency_march-2026", "biochemistry\"") and write them to `sagar_sharif_blacklist.json` so step 5's `--dry-run` doesn't re-list them as work.
    4. **Conservative seeder.** Only seed `downloaded_videos` entries where the on-disk filename matches the LMS title via `norm_eq` (lowercase, strip `.mp4`, alphanumeric-only) or `token_eq` (sorted token set). Jaccard ≥ 0.6 is acceptable but must be logged with a `match_method` field. Anything that doesn't match goes to `needs_human_review.json` — do NOT guess.
    5. **Foreground `--dry-run`** with the patch in place for `size_bytes=None`. Verify the would-download count matches the on-disk gap exactly. If the count is wrong, do not launch the real sync.
    6. **Only then**: `terminal(background=true, notify=true, timeout=21600)` (6h cap), with `ulimit -v 6291456` (6 GB virtual memory cap, prevents a runaway from taking the box), and a logfile via `tee`. On the next message after the notify fires, read the `[IMPORTANT: Background process ... exited]` block fully and report a real `=== SAGAR SYNC DONE: N videos / M notes / K failed ===` line. **No auto-retry on SIGTERM/143 or OOM-kill/-9** — the resume-from-disk pattern (pitfall 23) means a killed run picks up the partial .mp4 on next foreground launch, and an unkillable loop is worse than a stalled one.
    Skipping any step in this gate is what produces the "the user thinks I ruined all their data" pattern. The gate is not paranoia — it is the minimum verification between user intent and a 6-hour network commitment.

55. **`cp -a` not hardlink when the user asks to "copy" or "arrange in a new folder".** Hardlinks are tempting (zero extra disk, instant) but they break one of the two paths the user expects: (a) the user edits a file in the new folder expecting the source to stay clean — the source changes too. (b) a backup tool following the new folder sees the source as a duplicate and deduplicates it out. `cp -a` is 20 GB at ~500 MB/s on `/dev/sdb1` (sata SSD), 3-8 minutes for 95 files. `cp -av` is even better for verbose progress. **Watch out for 7-minute `terminal()` foreground timeouts** on the 20 GB copy — use `terminal(background=true, notify=true)` for the actual copy, and `sync` first so reads don't starve against the dirty page cache. Verify post-copy with `find` (count match) and one sha256 sample against a 200 MB+ file (sha256 on a 2 GB file is fast, on 20 GB is ~5 min — sample, don't full-verify).

49. **Never kill a long-running download process that the user is waiting on without a concrete disk-state reason.** A bulk `download_all.py` run shows no stdout for 30-90 minutes on a 2400-segment video because it buffers segments in RAM before writing — the user will think it is stuck, the agent will think it is stuck, and killing it is exactly the wrong move. Before sending any `kill`/`pkill`/`SIGTERM` to a `download_all`/`download_nested`/`download_sagar_one` process, **verify all four**:
    - `tail -50 /path/to/sync.log` shows the last successful line was >2 hours ago AND the last error repeats (not progressing through distinct segments).
    - The destination directory has **no** new `.mp4` written since the last log progress line.
    - `ps -o etime,pcpu,rss -p $PID` shows the process is idle (CPU ~0%, no syscalls in `strace` if available).
    - The user has explicitly said "kill it" OR the script has hit its own `max_failures` abort threshold.
    Missing any one of these four → **do not kill**. Resume-from-disk (pitfall 23) means even after a crash, the next run will see the partial .mp4 and finish it. The user lost 3-4 hours of progress each time this rule was broken.

50. **Trust the existing backfill-failures pipeline instead of adding new retry logic to `_dl()`.** When a long bulk run hits transient CDN errors, the established pattern (pitfall 25 + `scripts/backfill_failures.py` + `references/post-processing-failed-videos.md`) is: let the current run finish with whatever segments it can get, then run the 5-min post-process watchdog to retry just the failed videos. Adding a 5-attempt exponential-backoff retry inside `_dl()` looks like the right fix but causes the entire 30-90-minute buffer to hang on one persistently-bad segment, which then looks exactly like a stuck process. The backfill pattern runs in seconds per failed video and is already battle-tested. Reach for the backfill pipeline first, retry logic only as a last resort.

51. **The skill's `scripts/download_all.py` and the host's `/root/synapse_dl/download_all.py` are two different files.** The skill lives at `~/.hermes/skills/synapse-lms-download/scripts/`, the actual runtime copy lives at `/root/synapse_dl/`. Patches made via `patch /root/synapse_dl/download_all.py` do **not** propagate to the skill, and vice versa. Before editing, confirm which one the user is invoking (read the path the process was launched from via `ps -o cmd= -p $PID`). When a fix is verified on the host, port it to the skill's copy too — otherwise the next session that loads the skill and runs `scripts/download_all.py` will hit the same bug. The two should be kept byte-identical for the `download_all` and `download_nested` modules.

52. **Stream_id-based dedup means a "cleaned" state file still skips already-downloaded videos.** `is_video_downloaded` in `account_lib.py` keys on `stream_id`, and `sagar.json` had 28 stream_ids marked done after the 2026-08-26 sharif-cleanup pass. When the LMS scan returns 32 videos in Davidson's Review Batch-02, only the 4 with **new** stream_ids will actually be downloaded. Don't be surprised by "no new files" — verify with `diff <(jq -r '.downloaded_videos|keys[]' accounts/sagar.json|sort) <(curl -sH "Authorization: $SID" api.synapsepg.org/api/lecture/6a243060585213c2b6777ef9 | jq -r '.data.videoContents[].URL' | awk -F/ '{print $(NF-1)}' | sort)` to see the actual delta. If the LMS side shows N videos and the state shows N stream_ids, the run will correctly do nothing — and that is not a bug.

53. **Read the `notify_on_complete` output before re-launching.** When `terminal(background=true, notify=true)` fires, the process output appears in the next user message as an `[IMPORTANT: Background process ... exited]` block. That block contains the *real* stdout — it is the authoritative source for what happened. Reading the wrapper's `exit_code` alone is not enough: `exit_code 0` from the wrapper can wrap a Python process that ran for 0.2 seconds because the state file was fully up-to-date. Always read the full `Output:` block from the notification before deciding what to do next.

41. **User says "previously download was fast" on Synapse** — they mean `download_sagar_one.py` (or Sharif `download_nested`), not a bulk `download_all.py` run. Dry-run with `download_all`, **execute** single-lecture grabs with `download_sagar_one.py` + `PYTHONUNBUFFERED=1`. Kill stuck bulk runs when triage in `incremental-sync.md` matches.

42. **Non-ASCII video titles (Bengali/Arabic) break `--title-match`** — the Playwright enumeration or Python string comparison can fail silently, printing `Found 0 videos in chapter` even though the LMS tile exists. Verified 2026-06-25: `download_sagar_one.py 6a243060585213c2b6777ef9 --title-match "Gastroenterology - 02"` printed 0 videos, but the tile was on LMS under `Gastroenterology - 02(বাকী অংশ)`. **Fall back to `--index <N>`** (verify index via dry-run or enumerate-without-match). See `references/non-ascii-titles.md`.

43. **`sanitize(title)` can produce `.mp4` or `..mp4` filenames.** Bengali-only titles become an empty stem → literal `.mp4` on disk (Sharif 2026-07). LMS titles ending with `.` or `'` become double dots before the extension (`Lecture_No_09_Inferior_Extremity..mp4`). After download: `ffprobe`, rename to a sane English slug, update `accounts/<name>.json` `filename`. Sagar: `normalize_chapter_filenames.py`. Sharif: `scripts/normalize_sharif_filenames.py`.

44. **Sagar post-download is organize + normalize in the same session.** User expects `/mnt/tb/synapse_26_by_chapter` current without a follow-up ask — run `organize_sagar_after_sync.sh` after `download_sagar_one.py` / `download_notes.py`. If `organize_by_chapter.py` crashes (e.g. bad edit), fix the skill script before closing the task.

45. **Substring keyword matching in `organize_by_chapter.py` silently misfiles titles.** Plain `if kw in lower:` matches anywhere — `"sti"` matches inside `"Question"` and `"estrogen"`, `"on"` matches `"Gastroenterology"`, `"ra"` matches `"Respiratory"`, etc. Verified 2026-07-03: `FCPS P1 JUNE-26 Medicine Question Solve Session.mp4` landed in `Ch15_STIs/` because of the `sti` substring inside `Question`. **Use word-boundary regex** in `classify()`:
    ```python
    import re
    for folder, keywords in keyword_map:
        for kw in keywords:
            if re.search(rf"(?<![a-z]){re.escape(kw)}(?![a-z])", lower):
                return folder
    ```
    Order keywords most-specific → most-generic (`"sexually transmitted"` before `"sti"`, `"heart failure"` before `"heart"`). After any keyword-map edit, **scan `Ch00_Unsorted/` — if it stays empty, the regex is working**.

46. **md5 dedup after organize is mandatory.** The same content lands twice with different filenames when LMS reuses notes (e.g. `Respiratory_Medicine_Davidson.pdf` and `Respiratory_medicine_Davidson.pdf` — byte-identical, both downloaded from the same `file_id` because LMS title formatting changed between batches). After `organize_by_chapter.py`, run:
    ```bash
    cd /path/to/chapter && md5sum *.pdf *.mp4 | sort | awk 'NR%2==0 && $1==prev{print $2}' | xargs -r rm -f
    ```
    Then drop the matching state entries from `accounts/<name>.json` (iterate `downloaded_notes` / `downloaded_videos`, delete any whose `filename` matches a removed file). Pair with pitfall 31 (diff by `stream_id`, never title) — both stem from LMS title churn.

47. **Full-textbook PDFs don't fit any single chapter.** `Davidson's Principles and Practice of Medicine 25th PDF` (227 MB) spans every chapter and gets force-filed by the keyword map into whichever topic's keyword happens to match first. **Convention: `Ch00_Davidson_Textbook/` (or `Ch00_Full_Textbook/`) at the root of the organized tree** — recognize by size >100 MB + title keywords like `"textbook"`, `"principles and practice"`, `"complete"`, `"all chapters"`, or by being the first file from the LMS "Notes" chapter of a course whose primary content is textbook chapters. Add an explicit early-return in `classify()` BEFORE the topic maps:
    ```python
    if re.search(r"(textbook|principles and practice|complete\s+medicine|all\s+chapters)", lower):
        return "Ch00_Davidson_Textbook"
    ```

## Verification checklist

Run these **before** reporting success — the user catches every miss:

- [ ] `ffprobe` shows `format_name=mov,mp4,m4a` (true MP4, **not `mpegts`**) — only then call it `.mp4`
- [ ] Duration matches the LMS page (e.g., 7567.92s for 2h 6m 7.92s)
- [ ] `h264|video|1280x720` for 720p, `aac|audio` for audio
- [ ] First 4 bytes of any `.pdf` are `%PDF`
- [ ] File size > 0 and roughly matches expected (834 MB for 2h 720p ≈ 1 Mbps)
- [ ] **Content-count claim matches `localStorage.allLectures` data**, not marketing copy on the brochure
- [ ] State file updated (`accounts/<name>.json` has the new entry)

## Auth flow diagram

```
User → POST /api/student/login (json: {username, password})
     ← 200 {token: "...", student: {...}}
     Browser stores: localStorage.sessionId = URL-encoded(token)
                   localStorage.student = JSON(student)

User → GET /api/lecture/{id}
     Headers: Authorization: <localStorage.sessionId>
     ← 200 {data: {videoContents: [...], fileContents: [...]}}

User → click .student-video-card[idx]
     Browser renders: <iframe src="https://player.vidinfra.com/stream/{cid}/default/{sid}">
     Iframe loads player JS → computes HMAC → fetches KMS key
                            → fetches CDN playlist → fetches segments → decrypts → MSE → <video>

User → click .DOWNLOAD-button
     → opens https://assets.synapsepg.org/directory/<num>.pdf (no auth needed)
```

## Known limits (as of 2026-06)

- **720p only** in the script — change `quality="720p"` to `"480p"` for a smaller file
- **Resume from disk after crash** — if the process is killed mid-run, the next run detects a final `.mp4` already on disk and re-records state without re-downloading (see pitfall 23)
- **Concurrent = 12-16 threads** — works fine; bump to 50+ for faster if your bandwidth allows
- **No subtitle extraction** — HLS subs would need separate work (not seen on this LMS)
- **No 1080p+** — Vidinfra's CDN only serves 720p and 480p on this LMS

## Security / legal note

This is for **downloading content the user has already paid for and has active access to.** The encryption is for stream protection, not copyright enforcement. Personal offline use is fair use. Don't use this to bypass content you don't have access to, and don't redistribute.

## Worked example (2026-06-18, Dr. Sagar's Synapse enrollment)

```text
Account: sagar  (username 01683048886)
Output:  /mnt/tb/synapse_26/
State:   /root/synapse_dl/accounts/sagar.json
Creds:   /root/synapse_dl/accounts/sagar.creds  (chmod 600)

Course: FCPS P-I Medicine & Allied, December-2026 (Synapse Medical Academy)
URL:   https://lms.synapsepg.org/videos/6a243060585213c2b6777ef9/lecture

Chapters (4 total):
  - 6a243060585213c2b6777ef9  "Davidson's Review Batch-02"     2 videos
  - 69b13d898d2df1d11e89fb7e  "FCPS P-I Basic Classes"         0 videos (empty)
  - 6a251ab2585213c2b6778499  "Davidson's Notes"               0 videos, 16 PDFs
  - 6a251aa4585213c2b6778498  "Basic Notes"                    0 videos (empty)

Downloads (1.05 GB total, all in state):
  /mnt/tb/synapse_26/Gastroenterology-01.mp4              765.8 MB   2h 6m
  /mnt/tb/synapse_26/Orientation_December-26.mp4          110.5 MB    54m
  /mnt/tb/synapse_26/notes/*.pdf                          ~199 MB     16 files

Future sync (one new lecture):\n  $ download_all.py sagar --dry-run\n  $ PYTHONUNBUFFERED=1 /root/synapse_dl/download_sagar_one.py 6a243060585213c2b6777ef9 --index 0\n```\n
### Worked example — second account (Dr. Sagar's colleague, "sharif")

```text
Account: sharif  (username 01903361784)
Output:  /mnt/tb/Syn MD 26/
State:   /root/synapse_dl/accounts/sharif.json
Creds:   /root/synapse_dl/accounts/sharif.creds  (chmod 600)

Course: Synapse MD Residency Nov-26 batch
URL:    https://lms.synapsepg.org/subjects/68f0877da63aae5df6187b66

Hierarchy (4 chapters in 3 sections, 51 videos + 12 notes total):
  Basic/Session_Solve_Classes/        14 videos + 10 notes  (69afff828d2df1d11e89e136)
  Basic/Intensive_Care_Core_Batch-5/  14 videos +  1 note   (69218e1c373bbf67cff792cd)
  MD_faculty/MD_faculty/               1 video  +  1 note   (68f5f3c63b87d19804e874d9)
  Session_Solve_Classes/Session_Solve_Classes/  22 videos +  0 notes  (6948f22647005260db1aa242)

Downloaded (complete, 14.84 GB):
  /mnt/tb/Syn MD 26/Basic/Session_Solve_Classes/        13 videos + 12 notes
    Lecture_No_07_Thorax.mp4                              880 MB   4h 19m
    Lecture_No_06_Head_Neck.mp4                           1.0 GB   4h 47m
    Lecture_No_05_Embryology.mp4                          871 MB   4h 24m
    Review_Class_Physiology_Masterclass_...mp4            995 MB
    Lecture_No_07_Renal_body_fluid_electrolyte...mp4      1.2 GB   4h 8m
    Lecture_No_06_Endocrine_Physiology..mp4               1.2 GB
    Lecture_No_05_GIT_Physiology.mp4                      627 MB
    Lecture_NO_04_Neurophysiology.mp4                     734 MB
    Lecture_No_03_GP_Respiratory.mp4                      539 MB
    Lecture_No_02_CVS_Physiology.mp4                      873 MB
    Lecture_No_01_Blood_Hematology.mp4                    858 MB
    Orientation_Guideline_Session...._..mp4               170 MB
    Free_Class_Anatomy_Masterclass-.mp4                   365 MB

  /mnt/tb/Syn MD 26/Basic/Intensive_Care_Core_Batch-5/   6 videos +  1 note
    Pharmacology_Masterclass.mp4                          138 MB
    Microbiology_Problem_Solving_Class..mp4               251 MB
    Pathology_Problem_Solving_Class...mp4                 331 MB
    Surgery_Batch_Subject_Choice_Session-.mp4             175 MB
    R.March-2026_Question_Solve_Session_Anatomy.mp4       480 MB
    Pathology_Physiology_Question_Solve_Class.mp4         267 MB

  /mnt/tb/Syn MD 26/MD_faculty/MD_faculty/               1 video  +  1 note
    Medicine_Faculty_Subject_Choice_Session--.mp4         161 MB

  /mnt/tb/Syn MD 26/Session_Solve_Classes/Session_Solve_Classes/  9 videos +  0 notes
    Orientation_Guideline_Session_For_Residency_Batch.....mp4  126 MB
    FCPS_Residency.mp4                                    379 MB
    Diploma_Exam_Physiology_Question_Solve........mp4     191 MB
    Orientation_of_April_Month.mp4                        110 MB
    Subject_Choice_Session_Medicine_Faculty.mp4           334 MB
    Residency_Preparation_After_BCS.mp4                  212 MB
    Surgery_Faculty_Subject_choice_session..mp4           198 MB
    Anatomy_Previous_Year_s_Question_Solve..mp4           532 MB
    Offline_Class_Blood_Hematology.mp4                    795 MB

Permanently missing (HTTP 404 from LMS, 24 total): mostly old orientation
sessions, success-story sessions, and a few question-solve classes that the
LMS has deleted. Recorded in sharif.json → permanently_missing_videos and
skipped on every subsequent run.

For this account, the flat `download_all.py` was wrong — the user wanted the
section/chapter hierarchy preserved on disk. Use `download_nested.py sharif`
(separate script at /root/synapse_dl/download_nested.py) instead. The state
file format is identical, so a re-run with either script will pick up where
the other left off.

Progress reporter: see `references/long-running-progress.md` for the
every-15-min bash + cron setup that kept the user informed during the
multi-hour bulk sync.
```

## Chapter-based organization (post-download)

Synapse LMS downloads everything flat into one folder. For study, users typically want **topic-based grouping** (e.g., all gastroenterology videos + notes + exams together). Use `scripts/organize_by_chapter.py` to auto-classify files into per-topic folders:

```bash
/root/.venvs/synapse-env/bin/python scripts/organize_by_chapter.py \
  /mnt/tb/synapse_26 \
  /mnt/tb/synapse_26_by_chapter
```

**How it works:**
1. Reads `accounts/<name>.json` state to get video titles + chapter names.
2. Maps videos to topic folders by keyword matching (configurable in the script).
3. Moves notes PDFs by matching filenames against topic keywords.
4. Moves exam JSONs to root of the target folder.
5. Skips files already organized (idempotent — safe to re-run).

**Default mapping (customize in script):**

| Keyword in title | Target folder |
|---|---|
| Gastroenterology, Hepatology | `Ch22_Gastroenterology_Hepatology/` |
| Environmental, Oncology, Palliative, Ageing, Acute medicine, Nutrition | `Ch08_Oncology_Palliative_Environmental_Ageing/` |
| Orientation | `Ch00_Orientation/` |
| Stroke, Diabetes | `Ch27_Neurology/` |
| Hematology, Haematology | `Ch24_Haematology/` |
| Nephrology | `Ch18_Nephrology/` |
| Psychiatry | `Ch29_Psychiatry/` |
| Falls, Frailty, Continence, Cognitive, Legal, Nutrition & Hydration | `Ch32_Geriatrics/` |
| Cardiology, Arrhythmia, ECG | `Ch16_Cardiology/` |
| Respiratory, Pulmonary | `Ch17_Respiratory_Medicine/` |
| Endocrinology | `Ch20_Endocrinology/` |

Folder numbers follow Davidson's 25th edition chapter order. Full mapping: `references/davidson-25th-chapter-mapping.md`.

**Output:**
```
/mnt/tb/synapse_26_by_chapter/
├── Ch00_Orientation/          (videos)
├── Ch08_Oncology_Palliative_Environmental_Ageing/  (videos + PDFs + study notes)
├── Ch18_Nephrology/           (PDFs)
├── Ch20_Endocrinology/        (videos)
├── Ch22_Gastroenterology_Hepatology/  (videos + PDFs)
├── Ch24_Haematology/          (PDFs)
├── Ch27_Neurology/            (PDFs)
├── Ch29_Psychiatry/           (PDFs)
├── Ch32_Geriatrics/           (empty until content appears)
└── exam_*.json                (exam payloads at root)
```

**Caveat:** This mapping is keyword-based Some notes span multiple topics (e.g., "Acute medicine & critical illness" covers both environmental and geriatrics). The script puts each file in the **first** keyword match — review the output and manually move misfiled items if needed.

**Renumber by Davidson 25th edition:** After organizing, rename folders to match Davidson's 25th edition chapter numbers. See `references/davidson-25th-chapter-mapping.md` for the full mapping. Pattern: `mv "01_Gastroenterology" "Ch22_Gastroenterology_Hepatology"`. Multi-topic lectures (e.g., Oncology + Palliative + Environmental + Ageing in one Synapse lecture) map to the PRIMARY topic's chapter number with all topics in the folder name.

**Pitfall: re-run organize after incremental downloads.** `organize_by_chapter.py` copies files from the flat `synapse_26/` directory into the organized tree. After downloading new videos/notes incrementally, re-run organize to pick them up. But **check what's already organized first** — a video that was previously downloaded, organized, then re-downloaded (e.g., because state tracking lost it) will already exist in the organized folder. Compare file sizes to confirm they're identical before assuming something is missing. In the 2026-06-29 session, "Environmental Medicine, Oncology..." was already in the organized tree from June 25 (identical 802064087 bytes) but had been re-downloaded to the flat folder because the state file had lost track of it.

**Post-organize verify + fix `Ch00_Unsorted`.** After `organize_by_chapter.py` runs (auto-calls `normalize_chapter_filenames.py`), check `Ch00_Unsorted/` — any files there mean the keyword map is missing a topic. Fix by: (1) adding the keyword to `VIDEO_KEYWORD_MAP` / `NOTE_KEYWORD_MAP` in the script, (2) `mv` the files from `Ch00_Unsorted/` to the correct chapter folder, (3) re-run `normalize_chapter_filenames.py`. Verify `Ch00_Unsorted/` is empty before reporting done.

**`normalize_chapter_filenames.py` details.** Two modes: (1) **EXACT map** — hardcoded old→new pairs for known ugly LMS names (double `.mp4`, `_pdf` suffixes, `_davidson_pdf`, spaces, Bengali). (2) **Heuristic** — strips double extensions, replaces spaces with `-` (videos) or `_` (PDFs), removes trailing `_pdf`/`_PDF`/`_davidson_pdf`. Runs against the organized tree (`/mnt/tb/synapse_26_by_chapter`), the flat dir (`/mnt/tb/synapse_26`), and `notes/` subfolder. Updates `accounts/sagar.json` filenames to match. Auto-invoked by `organize_by_chapter.py`.

**Sharif dry-run limitation.** `download_nested.py sharif --dry-run` only lists planned chapters, NOT new vs existing items. For incremental checks, use `scripts/check_sharif_new.py` which enumerates all chapters, compares `stream_id` / `file_id` against state, and prints `NEW_VIDEOS` / `NEW_NOTES`. Then run `download_nested.py sharif` (without `--dry-run`) to download.

```bash
# Find all chapters in a course (after login, in browser DevTools console):
JSON.parse(localStorage.allLectures)
# Returns: [{_id, name, videoContents: [...], fileContents: [...]}, ...]

# Find a video's CDN stream ID (in browser DevTools Network tab):
# Filter:  m3u8  →  click any request to tenbytecdn.com
# Response:  #EXTM3U  ...  (this IS the stream_id in the URL path)

# Strip MPEG-TS to MP4 (if you ever have a .ts file):
ffmpeg -hide_banner -loglevel error -i input.ts -c copy -movflags +faststart output.mp4

# Verify a downloaded file:
ffprobe -v error -of compact=p=0:nk=1 \
  -show_entries format=format_name,duration,size:stream=codec_name,codec_type,width,height file.mp4
```
