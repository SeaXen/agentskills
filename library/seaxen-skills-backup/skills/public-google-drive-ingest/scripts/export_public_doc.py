#!/usr/bin/env python3
"""Export public Google Docs/PDFs by file ID (no OAuth)."""
import argparse
import re
import sys
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0"


def clean_id(raw: str) -> str:
    return raw.split("-0-")[0].rstrip("-")


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


def export_doc(doc_id: str, out: Path) -> str:
    doc_id = clean_id(doc_id)
    url = f"https://docs.google.com/document/d/{doc_id}/export?format=txt"
    data = fetch(url)
    if len(data) < 200 or b"<!DOCTYPE" in data[:200].upper():
        return f"fail:not_plain_text:{len(data)}"
    out.write_bytes(data)
    return f"ok:{len(data)}"


def export_pdf(file_id: str, out: Path) -> str:
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    data = fetch(url)
    if len(data) < 1000 or b"<!DOCTYPE html" in data[:300].lower():
        return f"fail:not_pdf:{len(data)}"
    out.write_bytes(data)
    return f"ok:{len(data)}"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--doc", action="append", default=[], metavar="ID:OUT.txt")
    p.add_argument("--pdf", action="append", default=[], metavar="ID:OUT.pdf")
    args = p.parse_args()
    rc = 0
    for spec in args.doc:
        doc_id, _, out_s = spec.partition(":")
        if not out_s:
            print("bad --doc spec (need ID:path)", spec, file=sys.stderr)
            rc = 1
            continue
        print(export_doc(doc_id.strip(), Path(out_s)), out_s)
    for spec in args.pdf:
        fid, _, out_s = spec.partition(":")
        if not out_s:
            print("bad --pdf spec (need ID:path)", spec, file=sys.stderr)
            rc = 1
            continue
        print(export_pdf(fid.strip(), Path(out_s)), out_s)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())