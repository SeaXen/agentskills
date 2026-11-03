#!/usr/bin/env python3
"""Download one DrBeen course (all lectures). Resume + thermal pacing."""
import json
import os
import re
import subprocess
import sys
import time
import requests

if len(sys.argv) < 4:
    print("usage: download_course.py <account> <course_slug> <course_id>", file=sys.stderr)
    sys.exit(1)

ACCOUNT, COURSE_SLUG, COURSE_ID = sys.argv[1], sys.argv[2], sys.argv[3]
BASE = os.environ.get("DRBEEN_OUT", "/mnt/tb/drbeen")
OUT_DIR = os.path.join(BASE, COURSE_SLUG)
COOKIE_FILE = os.environ.get("DRBEEN_COOKIE_FILE", "/tmp/drbeen_cookies.txt")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
SLEEP = int(os.environ.get("SLEEP", "45"))
COOLDOWN_EVERY = int(os.environ.get("COOLDOWN_EVERY", "4"))
LONG_COOLDOWN = int(os.environ.get("LONG_COOLDOWN", "120"))

def load_cookies():
    cookies = {}
    if not os.path.isfile(COOKIE_FILE):
        return cookies
    with open(COOKIE_FILE) as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            p = line.split("\t")
            if len(p) >= 7:
                cookies[p[5]] = p[6]
    return cookies

def sanitize(n):
    n = re.sub(r'[\\/\:*?"<>|\r\n\t]', "_", n)
    return re.sub(r"\s+", " ", n).strip().rstrip(".")[:180]

sess = requests.Session()
for k, v in load_cookies().items():
    sess.cookies.set(k, v, domain=".drbeen.com", path="/")
HEADERS = {"User-Agent": UA, "Referer": "https://www.drbeen.com/"}

course_url = f"https://www.drbeen.com/courses/{COURSE_SLUG}/{COURSE_ID}"
r = sess.get(course_url, headers=HEADERS, timeout=30)
if r.status_code != 200:
    print(f"course page failed: {r.status_code}")
    sys.exit(1)

lectures = []
for m in re.finditer(
    r'href="(/learn/[^"]+/[A-Za-z0-9_-]+)\?topic=([^&"]+)(?:&subTopic=([^"]*))?"',
    r.text,
):
    lectures.append({"path": m.group(1), "topic": m.group(2), "subtopic": m.group(3) or ""})
seen = set()
unique = []
for l in lectures:
    if l["path"] not in seen:
        seen.add(l["path"])
        unique.append(l)
lectures = unique
print(f"[+] {len(lectures)} lectures")

os.makedirs(OUT_DIR, exist_ok=True)
meta_path = os.path.join(OUT_DIR, "_lectures.json")
lecture_data = []
if os.path.isfile(meta_path):
    with open(meta_path) as f:
        lecture_data = json.load(f)
    have = {x["path"] for x in lecture_data}
    for l in lectures:
        if l["path"] in have:
            continue
        rr = sess.get(f"https://www.drbeen.com{l['path']}", headers=HEADERS, timeout=30)
        if rr.status_code != 200:
            continue
        vm = re.search(r"player\.vimeo\.com/video/(\d+)", rr.text)
        tm = re.search(r"<h[12][^>]*>([^<]+)</h[12]>", rr.text) or re.search(
            r"<title>([^<]+)</title>", rr.text
        )
        title = tm.group(1).strip().split("|")[0].strip() if tm else os.path.basename(l["path"])
        lecture_data.append(
            {
                "path": l["path"],
                "vimeo_id": vm.group(1) if vm else None,
                "title": title,
                "topic": l["topic"],
                "subtopic": l["subtopic"],
            }
        )
        time.sleep(0.5)
else:
    for i, l in enumerate(lectures):
        rr = sess.get(f"https://www.drbeen.com{l['path']}", headers=HEADERS, timeout=30)
        if rr.status_code != 200:
            continue
        vm = re.search(r"player\.vimeo\.com/video/(\d+)", rr.text)
        tm = re.search(r"<h[12][^>]*>([^<]+)</h[12]>", rr.text) or re.search(
            r"<title>([^<]+)</title>", rr.text
        )
        title = tm.group(1).strip().split("|")[0].strip() if tm else os.path.basename(l["path"])
        lecture_data.append(
            {
                "i": i,
                "path": l["path"],
                "vimeo_id": vm.group(1) if vm else None,
                "title": title,
                "topic": l["topic"],
                "subtopic": l["subtopic"],
            }
        )
        time.sleep(0.5)

with open(meta_path, "w") as f:
    json.dump(lecture_data, f, indent=2, ensure_ascii=False)

for n, ld in enumerate(lecture_data):
    if n > 0 and n % COOLDOWN_EVERY == 0:
        print(f">>> cooldown {LONG_COOLDOWN}s <<<")
        time.sleep(LONG_COOLDOWN)

    title = ld["title"]
    fname = f"{n+1:02d} - {sanitize(title)}.mp4"
    out_path = os.path.join(OUT_DIR, fname)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 1024 * 1024:
        print(f"[{n+1}/{len(lecture_data)}] skip exists {title[:50]}")
        continue

    embed_url = f"https://www.drbeen.com{ld['path']}"
    print(f"[{n+1}/{len(lecture_data)}] {title[:60]}")
    cmd = [
        "yt-dlp",
        "--no-update",
        "--no-mtime",
        "-S",
        "res:1080,ext:mp4:m4a",
        "--merge-output-format",
        "mp4",
        "--cookies",
        COOKIE_FILE,
        "--referer",
        "https://www.drbeen.com/",
        "-o",
        out_path,
        embed_url,
    ]
    subprocess.run(cmd, timeout=1800)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 1024 * 1024:
        print(f"  ok {os.path.getsize(out_path)/1024/1024:.1f} MB")
    else:
        print("  FAIL — run auth.py and retry")
    time.sleep(SLEEP)

print(f"done -> {OUT_DIR}")