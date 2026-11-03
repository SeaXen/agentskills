#!/usr/bin/env python3
"""
build_manifest.py — Create a Notion "backup manifest" page that records
metadata about a local file/dir (NOT the bytes). Use when the user wants
to "upload X to Notion" but X is too large to actually upload —
see the "Notion is not a file vault" pitfall in SKILL.md.

Produces a single page under a chosen parent with:
  - Filename, size (human + bytes), mtime, path
  - SHA-256 of the file (computed locally; for >100 MB files this takes seconds)
  - OpenPGP metadata (cipher, S2K, salt, iterations) for .gpg files
  - Tarball top-level preview if gpg + tar pipeline available (requires passphrase; skipped otherwise)
  - For directories: file count, total size, top-N largest files, top-level listing, extension breakdown
  - Verification command the user can re-run

Measures wall-clock upload time and prints throughput.

Usage:
    python3 build_manifest.py \\
        --parent PAGE_ID \\
        --title "Manifest YYYY-MM-DD" \\
        --file /path/to/backup.tar.gz.gpg \\
        --dir /path/to/plain-backup-dir

Or just edit the CONFIG block at the bottom and run.
"""
from __future__ import annotations
import argparse, hashlib, json, os, pathlib, subprocess, sys, time, urllib.request, urllib.error
from collections import Counter

DEFAULT_VERSION = "2022-06-28"  # older stable; override if your integration requires newer

# ---------- env loader ----------
def load_env(path: str = "/mnt/tb/hermes/.env") -> None:
    if not os.path.exists(path):
        return
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

# ---------- block builders ----------
def rt(text: str, cap: int = 1900):
    if len(text) > cap:
        text = text[: cap - 3] + "..."
    return [{"type": "text", "text": {"content": text}}]

def heading(level: int, text: str):
    return {"object": "block", "type": f"heading_{level}",
            f"heading_{level}": {"rich_text": rt(text)}}

def para(text: str):
    return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": rt(text)}}

def bullet(text: str):
    return {"object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {"rich_text": rt(text)}}

def code(text: str, lang: str = "plain text"):
    return {"object": "block", "type": "code",
            "code": {"rich_text": rt(text), "language": lang}}

def divider():
    return {"object": "block", "type": "divider", "divider": {}}

def callout(text: str, emoji: str = "📋"):
    return {"object": "block", "type": "callout",
            "callout": {"rich_text": rt(text), "icon": {"type": "emoji", "emoji": emoji}}}

# ---------- metadata gatherers ----------
def sha256_file(path: str, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    n = 0
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
            n += len(b)
    return h.hexdigest(), n

def gpg_list_packets(path: str) -> str:
    """Returns OpenPGP packet metadata without needing the passphrase."""
    try:
        out = subprocess.run(["gpg", "--list-packets", path],
                             capture_output=True, text=True, timeout=10)
        # Filter out passphrase-prompt noise; keep the packet headers
        lines = [l for l in out.stdout.splitlines()
                 if not l.startswith("gpg:") and l.strip()]
        return "\n".join(lines[:20])
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        return f"(gpg not available: {e})"

def dir_summary(root: pathlib.Path, top_n: int = 20) -> dict:
    files = list(root.rglob("*"))
    file_paths = [f for f in files if f.is_file()]
    total_size = sum(f.stat().st_size for f in file_paths)
    sized = sorted(((f.stat().st_size, str(f.relative_to(root))) for f in file_paths),
                   reverse=True)
    top = "\n".join(f"{h:>12,}  {p}" for h, p in sized[:top_n])
    top_level = sorted(p.name + ("/" if p.is_dir() else "")
                       for p in root.iterdir())
    top_level_str = "\n".join(top_level[:60])
    if len(top_level) > 60:
        top_level_str += f"\n… and {len(top_level) - 60} more"
    exts = Counter(f.suffix.lower() or "(none)" for f in file_paths)
    top_exts = "\n".join(
        f"{e:<12} {sum(1 for f in file_paths if f.suffix.lower() == e):>5}  "
        f"{sum(f.stat().st_size for f in file_paths if f.suffix.lower() == e) / 1024 / 1024:>8.1f} MB"
        for e, _ in exts.most_common(15)
    )
    return {
        "file_count": len(file_paths),
        "total_size": total_size,
        "top_files": top,
        "top_level": top_level_str,
        "top_exts": top_exts,
    }

# ---------- notion upload ----------
def call(method: str, path: str, body: dict | None, token: str, version: str):
    url = f"https://api.notion.com{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {token}",
        "Notion-Version": version,
        "Content-Type": "application/json",
    })
    t0 = time.perf_counter()
    try:
        with urllib.request.urlopen(req) as resp:
            payload = resp.read(); status = resp.status
    except urllib.error.HTTPError as e:
        payload = e.read(); status = e.code
    return payload, time.perf_counter() - t0, status

def upload(token: str, version: str, parent_id: str, title: str,
           emoji: str, blocks: list[dict]) -> dict:
    body = {
        "parent": {"type": "page_id", "page_id": parent_id},
        "icon": {"type": "emoji", "emoji": emoji},
        "properties": {"title": [{"type": "text", "text": {"content": title}}]},
        "children": blocks[:100],
    }
    req_bytes = len(json.dumps(body).encode())
    t_start = time.perf_counter()
    resp, dt, st = call("POST", "/v1/pages", body, token, version)
    if st >= 300:
        raise SystemExit(f"POST /v1/pages failed: HTTP {st}\n{resp.decode(errors='replace')[:500]}")
    page_id = json.loads(resp)["id"]
    if len(blocks) > 100:
        more = blocks[100:]
        for i in range(0, len(more), 100):
            chunk = more[i:i + 100]
            r2, _, s2 = call("PATCH", f"/v1/blocks/{page_id}/children",
                             {"children": chunk}, token, version)
            req_bytes += len(json.dumps({"children": chunk}).encode())
            if s2 >= 300:
                raise SystemExit(f"PATCH children failed: HTTP {s2}\n{r2.decode(errors='replace')[:500]}")
    wall = time.perf_counter() - t_start
    return {"page_id": page_id, "req_bytes": req_bytes, "wall": wall,
            "url": f"https://app.notion.com/p/{title.replace(' ', '-')}-{page_id.replace('-', '')}"}

# ---------- main ----------
def build_blocks(args, file_path: pathlib.Path | None, dir_path: pathlib.Path | None) -> list[dict]:
    blocks: list[dict] = [
        callout(f"Manifest generated {time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime())} · "
                "metadata only, no payload bytes uploaded", "📋"),
    ]
    if file_path is not None:
        st = file_path.stat()
        size = st.st_size
        print(f"  hashing {file_path} ({size:,} bytes)...")
        sha, _ = sha256_file(str(file_path))
        blocks += [
            heading(2, f"1. File: {file_path.name}"),
            bullet(f"Filename: {file_path.name}"),
            bullet(f"Size: {size:,} bytes ({size / 1024 / 1024 / 1024:.2f} GiB)" if size > 1024**3
                   else f"Size: {size:,} bytes ({size / 1024 / 1024:.2f} MiB)"),
            bullet(f"Modified: {time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(st.st_mtime))}"),
            bullet(f"SHA-256: {sha}"),
            bullet(f"Path (host): {file_path}"),
        ]
        if str(file_path).endswith(".gpg"):
            blocks += [
                heading(3, "OpenPGP packet metadata"),
                code(gpg_list_packets(str(file_path)), "plain text"),
            ]
        blocks += [
            heading(3, "Verification command"),
            code(f"# Re-verify SHA-256\nsha256sum {file_path}", "shell"),
            divider(),
        ]
    if dir_path is not None:
        print(f"  walking {dir_path}...")
        s = dir_summary(dir_path)
        blocks += [
            heading(2, f"2. Directory: {dir_path.name or dir_path}"),
            bullet(f"Path (host): {dir_path}"),
            bullet(f"Total files: {s['file_count']:,}"),
            bullet(f"Total size: {s['total_size'] / 1024 / 1024 / 1024:.2f} GiB"),
            heading(3, "Top 20 largest files"),
            code(s["top_files"], "plain text"),
            heading(3, "Top-level listing"),
            code(s["top_level"], "plain text"),
            heading(3, "Extension breakdown (top 15)"),
            code(s["top_exts"], "plain text"),
            divider(),
        ]
    blocks += [
        heading(2, "Notes"),
        para("This page records metadata about the artifact, not the artifact itself. "
             "Notion's API is a JSON CRUD pipe, not a file vault — uploading the actual "
             "bytes for multi-GB files would take hours of API calls and overflow workspace "
             "block limits. See the Hermes backup pipeline for the proper offsite path."),
    ]
    return blocks

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--parent", required=True, help="Parent Notion page id (UUID)")
    p.add_argument("--title", required=True, help="Page title")
    p.add_argument("--file", help="Path to a single file (e.g. .tar.gz.gpg)")
    p.add_argument("--dir", help="Path to a directory tree")
    p.add_argument("--token-env", default="NOTION_TOKEN",
                   help="Env var holding the integration token (default: NOTION_TOKEN)")
    p.add_argument("--version", default=DEFAULT_VERSION,
                   help=f"Notion-Version header (default: {DEFAULT_VERSION})")
    p.add_argument("--emoji", default="🗄️", help="Page icon emoji")
    args = p.parse_args()

    if not args.file and not args.dir:
        p.error("at least one of --file or --dir is required")

    load_env()
    token = os.environ.get(args.token_env) or os.environ.get("NOTION_API_KEY")
    if not token:
        sys.exit(f"ERROR: no token in env var {args.token_env} (or NOTION_API_KEY)")

    file_path = pathlib.Path(args.file).expanduser() if args.file else None
    dir_path = pathlib.Path(args.dir).expanduser() if args.dir else None
    if file_path and not file_path.exists():
        sys.exit(f"ERROR: file not found: {file_path}")
    if dir_path and not dir_path.is_dir():
        sys.exit(f"ERROR: dir not found: {dir_path}")

    blocks = build_blocks(args, file_path, dir_path)
    print(f"Built {len(blocks)} blocks. Uploading…")
    result = upload(token, args.version, args.parent, args.title, args.emoji, blocks)
    print()
    print("=" * 50)
    print("UPLOAD STATS")
    print("=" * 50)
    print(f"  Request body sent : {result['req_bytes']:,} bytes "
          f"({result['req_bytes'] / 1024:.1f} KiB)")
    print(f"  Wall-clock time   : {result['wall'] * 1000:.0f} ms ({result['wall']:.2f} s)")
    print(f"  Effective UL rate : {result['req_bytes'] / result['wall'] / 1024:.1f} KiB/s "
          f"({result['req_bytes'] * 8 / result['wall'] / 1e6:.2f} Mbit/s)")
    print(f"  Blocks uploaded   : {len(blocks)}")
    print(f"  Page URL          : {result['url']}")
    print(f"  Page id           : {result['page_id']}")

if __name__ == "__main__":
    main()
