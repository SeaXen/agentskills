#!/usr/bin/env python3
"""
facebook-download wrapper using yt-dlp.

Saves to /mnt/tb/#Sea/fbdown/ with the real Facebook post title in the filename
(post ID kept as prefix for dedup).

Naming pattern:
  facebook_<ID>_<sanitized-title>.mp4
  (falls back to facebook_<ID>.mp4 if title is empty/unusable)

Usage:
  fbdl.py <URL> [URL ...]
  echo <URL> | fbdl.py -        # stdin
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

DEST = Path("/mnt/tb/#Sea/fbdown")
YT_DLP = "/usr/local/bin/yt-dlp"  # absolute path; avoid PATH surprises

MAX_TITLE = 80  # characters (filesystem-safe)


def sanitize_title(raw: str) -> str:
    """Extract real title from Facebook's '<stats> | <title>' format and clean for FS."""
    if not raw:
        return ""
    # Strip engagement prefix: "78K views · 2K reactions | Real Title Here"
    parts = raw.split(" | ", 1)
    real = parts[1].strip() if len(parts) == 2 else raw.strip()
    # Allow Unicode letters/marks/digits, underscore, hyphen, dot, space; collapse spaces → _
    clean = re.sub(r"[^\w\s.\-]", "", real, flags=re.UNICODE)
    clean = re.sub(r"\s+", "_", clean.strip())
    clean = re.sub(r"-+", "-", clean).strip("_-")
    if len(clean) > MAX_TITLE:
        clean = clean[:MAX_TITLE].rstrip("_-")
    return clean


def fetch_meta(url: str) -> dict | None:
    """Call yt-dlp --dump-json (cookie-auth) and return the parsed JSON dict, or None on failure."""
    cmd = [
        YT_DLP, "--no-warnings", "--no-progress",
        "--cookies-from-browser", "firefox",
        "--dump-json", "--skip-download",
        url,
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        print(f"[TIMEOUT] meta fetch: {url}", file=sys.stderr)
        return None
    if result.returncode != 0:
        print(f"[META FAIL] {url}: {result.stderr.strip()[:200]}", file=sys.stderr)
        return None
    # yt-dlp prints one JSON object per line; take the last full one
    lines = [ln for ln in result.stdout.splitlines() if ln.strip().startswith("{")]
    if not lines:
        return None
    try:
        return json.loads(lines[-1])
    except json.JSONDecodeError:
        return None


def download(url: str, dest_template: str) -> tuple[int, str]:
    """Call yt-dlp with the given -o template. Returns (returncode, output_path)."""
    cmd = [
        YT_DLP, "--no-warnings", "--no-progress",
        "--cookies-from-browser", "firefox",
        "-o", dest_template,
        url,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    return proc.returncode, (proc.stdout + proc.stderr)


def process(url: str) -> None:
    url = url.strip()
    if not url:
        return
    print(f"[>] {url}")
    meta = fetch_meta(url)
    if not meta:
        # Fall back to ID-only naming
        print("[!] no meta; using ID-only filename via simulate")
        sim = subprocess.run(
            [YT_DLP, "--no-warnings", "--no-progress",
             "--cookies-from-browser", "firefox",
             "--simulate", "--print", "%(id)s", url],
            capture_output=True, text=True, timeout=120,
        )
        fb_id = (sim.stdout.strip().splitlines() or ["unknown"])[-1]
        dest_template = str(DEST / "facebook_%(id)s.%(ext)s")
        rc, _ = download(url, dest_template)
        print(f"[{'OK' if rc == 0 else 'FAIL'}] facebook_{fb_id}.* (fallback)")
        return

    fb_id = meta.get("id") or "unknown"
    raw_title = meta.get("title") or ""
    clean = sanitize_title(raw_title)

    if clean:
        fname = f"facebook_{fb_id}_{clean}.%(ext)s"
    else:
        fname = f"facebook_{fb_id}.%(ext)s"
    dest_template = str(DEST / fname)

    # Dedupe: if a file matching facebook_<ID>_* already exists, skip
    if any(DEST.glob(f"facebook_{fb_id}.*")):
        existing = list(DEST.glob(f"facebook_{fb_id}.*"))
        print(f"[SKIP] already exists: {existing[0].name}")
        return

    rc, output = download(url, dest_template)
    # yt-dlp returns 0 on success even when --no-progress hides the final line; check for output file
    # Use prefix match (not "facebook_<id>.*") because new naming uses underscore, not dot
    produced = sorted(DEST.glob(f"facebook_{fb_id}*"))
    if produced:
        size = produced[0].stat().st_size
        print(f"[OK]   {produced[0].name}  ({size/1_048_576:.1f} MB)")
    else:
        print(f"[FAIL] exit={rc}; tail: {output.strip()[-300:]}")


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    urls = []
    if len(sys.argv) > 1 and sys.argv[1] != "-":
        urls = sys.argv[1:]
    else:
        urls = [ln.strip() for ln in sys.stdin if ln.strip()]
    if not urls:
        print("usage: fbdl.py <URL> [<URL> ...]   (or: echo URL | fbdl.py -)", file=sys.stderr)
        sys.exit(2)
    for u in urls:
        process(u)


if __name__ == "__main__":
    main()
