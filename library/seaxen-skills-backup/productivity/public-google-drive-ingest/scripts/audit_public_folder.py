#!/usr/bin/env python3
"""Compare public Drive folder listing vs local .txt mirror (no OAuth).

Usage:
  python audit_public_folder.py FOLDER_ID /path/to/local/subfolder

Exit 0 when exportable doc count matches local unique file sizes; prints gaps.
"""
import re
import sys
import urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0"}


def clean_id(raw: str) -> str:
    return raw.split("-0-")[0].rstrip("-")


def folder_docs(folder_id: str) -> list[tuple[str, str]]:
    url = f"https://drive.google.com/drive/folders/{folder_id}"
    html = urllib.request.urlopen(
        urllib.request.Request(url, headers=UA), timeout=90
    ).read().decode("utf-8", "ignore")
    items: list[tuple[str, str]] = []
    pat = r"(CARDIOLOGY PHYSIOLOGY|D / [A-Za-z0-9 /:&.-]{3,90}|RHEUMATOLOGY \d+|Chapter \d+[^\"\\]{0,80})"
    for m in re.finditer(pat, html):
        title = m.group(1).strip()
        seg = html[m.start() : m.start() + 700]
        if (
            "document" not in seg
            and "Google Docs" not in seg
            and "vnd.google-apps.document" not in seg
        ):
            continue
        ids = re.findall(r"1[a-zA-Z0-9_-]{25,44}", seg)
        if not ids:
            continue
        doc = clean_id(ids[0])
        if any(d == doc for _, d in items):
            continue
        items.append((title, doc))
    return items


def export_bytes(doc_id: str) -> int:
    url = f"https://docs.google.com/document/d/{doc_id}/export?format=txt"
    data = urllib.request.urlopen(
        urllib.request.Request(url, headers=UA), timeout=60
    ).read()
    if len(data) < 200 or b"<!DOCTYPE" in data[:200].upper():
        raise ValueError("bad export")
    return len(data)


def local_unique_sizes(folder: Path) -> set[int]:
    return {
        p.stat().st_size
        for p in folder.glob("*.txt")
        if p.stat().st_size > 1000
    }


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: audit_public_folder.py FOLDER_ID LOCAL_DIR", file=sys.stderr)
        return 2
    folder_id, local = sys.argv[1], Path(sys.argv[2])
    items = folder_docs(folder_id)
    loc = local_unique_sizes(local)
    export_sizes = []
    missing_titles = []
    for title, doc_id in items:
        try:
            export_sizes.append(export_bytes(doc_id))
        except Exception:
            missing_titles.append(title)
    good = [s for s in export_sizes if s > 0]
    print(f"drive_docs={len(items)} exportable={len(good)} local_unique={len(loc)}")
    if missing_titles:
        print("export_failed:", *missing_titles, sep="\n  ")
    if len(good) != len(loc):
        print("GAP: re-export missing docs (compare titles to filenames on disk)")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())