#!/usr/bin/env python3
"""Compare Sharif LMS chapters vs state; print NEW_VIDEOS / NEW_NOTES only.

Requires host layout: /root/synapse_dl/download_nested.py + accounts/sharif.json.
Run from /root/synapse_dl or set PYTHONPATH.
"""
import asyncio
import sys
from pathlib import Path

HOST_DL = Path("/root/synapse_dl")
if HOST_DL.is_dir():
    sys.path.insert(0, str(HOST_DL))

from account_lib import is_note_downloaded, is_video_downloaded, load_state  # noqa: E402
from download_nested import default_sharif_config, fetch_chapter_files, fetch_chapter_videos, sanitize  # noqa: E402


async def main() -> int:
    account = "sharif"
    state = load_state(account)
    new_v, new_n = [], []

    for sec in default_sharif_config():
        for ch in sec["chapters"]:
            lid = ch["lecture_id"]
            sub = f"{sanitize(sec['section'])}/{sanitize(ch['name'])}"
            try:
                vids = await fetch_chapter_videos(lid, account, sec["section"], ch["name"])
            except Exception as e:
                print(f"ERR videos {sub}: {e}")
                continue
            for v in vids:
                sid = v["stream_id"]
                if state.get("permanently_missing_videos", {}).get(sid):
                    continue
                if not is_video_downloaded(state, sid):
                    new_v.append((sub, v["video_index"], v["title"], sid[:8]))

            try:
                files, _ = await fetch_chapter_files(lid, account)
            except Exception as e:
                print(f"ERR notes {sub}: {e}")
                continue
            for f in files:
                fid = f.get("_id")
                if fid and not is_note_downloaded(state, fid):
                    new_n.append((sub, f.get("title", ""), fid[:8]))

    print(f"NEW_VIDEOS {len(new_v)}")
    for row in new_v:
        print(f"  V | {row[0]} | [{row[1]}] {row[2]} | {row[3]}")
    print(f"NEW_NOTES {len(new_n)}")
    for row in new_n:
        print(f"  N | {row[0]} | {row[1]} | {row[2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))