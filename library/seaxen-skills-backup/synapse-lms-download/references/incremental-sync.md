# Incremental sync workflow — "check for new lectures + download"

The user asks this repeatedly: *"Is there any new video/note? Check and download."* This is the exact workflow that works.

## Decision tree

```
Is this the FIRST download for this account?
├── YES → use download_all.py --dry-run first, then download_all.py
└── NO → incremental path:
    ├── Option A: download_sagar_one.py <chapter_id> --index <N>
    │   (verified fast: progress every 200 segments, ~1-1.5h per lecture)
    └── Option B: download_all.py --dry-run → identify new by index → run per-video
        (use ONLY when you need to scan multiple chapters at once)
```

## The gold-standard Sagar path (no bulk script)

```bash
# 1. Find what's new (fast, no download)
cd /root/synapse_dl
/root/.venvs/synapse-env/bin/python -c "
import asyncio, sys
sys.path.insert(0, '.')
from download_sagar_one import fetch_chapter_videos
async def main():
    vids = await fetch_chapter_videos('6a243060585213c2b6777ef9', 'sagar', 'x', 'x')
    for v in vids:
        print(f'[{v[\"video_index\"]}] {v[\"title\"][:80]}  stream={v[\"stream_id\"][:12]}')
asyncio.run(main())
" 2>&1 | grep -E "^\["

# 2. Compare with state (oneliner)
python3 -c "import json; s=json.load(open('accounts/sagar.json')); [print(v['filename'], v['title'][:40]) for v in s['downloaded_videos'].values()]"

# 3. Download the NEW ones by index (NOT title-match — see non-ascii-titles.md)
/root/.venvs/synapse-env/bin/python download_sagar_one.py 6a243060585213c2b6777ef9 --index 1

# 4. Download any new notes
/root/.venvs/synapse-env/bin/python download_notes.py sagar 6a251ab2585213c2b6778499
```

## Sagar chapter IDs (may change per batch)

| Chapter | ID | Type |
|---------|-----|------|
| Davidson's Review Batch-02 | `6a243060585213c2b6777ef9` | Videos |
| Davidson's Notes | `6a251ab2585213c2b6778499` | Notes |
| FCPS P-I Basic Classes | `69b13d898d2df1d11e89fb7e` | Usually empty |
| Basic Notes | `6a251aa4585213c2b6778498` | Usually empty |

Verify current IDs via API or dry-run — these change each LMS update.

## When the user says "download is slow"

Diagnosis checklist:
1. **Cpu ~0.2%, VmRSS ~900 MB, no log lines for 30+ min** → `download_all.py` stuck in RAM buffering. **Kill it. Re-run as single-video.**
2. **Steady `200/2390 ... 400/2390 ...`** in log → normal, ~30-60 min remaining. Tell user and back off.
3. **ERR seg [Errno 104] Connection reset** once or twice → normal CDN blip, 30s retry each. If it keeps appearing → network issue.

## Stuck run triage

```bash
# Is the process alive?
ps -p $(pgrep -f download_all.py) -o etime,pcpu,rss

# Is the log growing?
tail -3 /root/synapse_dl/sagar_sync_*.log

# Is there a tmp file on disk? (means segments are being downloaded)
ls -lah /mnt/tb/synapse_26/.*tmp 2>/dev/null
# If tmp file is growing (check ls twice, 30s apart) → still downloading, wait.
# If process is alive, no tmp file, no log growth for >15 min → stuck.
```

If stuck:
```bash
pkill -f download_all.py sagar
# Re-download the ones that DIDN'T finish:
/python3 download_sagar_one.py <chapter_id> --index <N>
```

## After downloading: organize

Use `scripts/organize_by_chapter.py` to move flat files into per-topic folders:
```bash
python3 scripts/organize_by_chapter.py /mnt/tb/synapse_26 /mnt/tb/synapse_26_by_chapter
```

## User-preference memory

- User explicitly said **"previously download was fast"** → they mean single-video, not bulk.
- User expects **"check and download"** to complete in **~30-60 min**, not hours.
- If bulk `download_all.py` hangs, user gets frustrated fast — prefer per-video.
- Sagar account is **flat** (single chapter, no sections) → `download_sagar_one.py` is default, not `download_nested.py`.
