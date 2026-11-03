#!/usr/bin/env python3
"""DrBeen login -> Netscape cookies for yt-dlp. Password from env or .creds file only."""
import os
import sys
import requests

ACCOUNT = sys.argv[1] if len(sys.argv) > 1 else "default"
SECRETS_DIR = os.path.expanduser("~/.hermes/secrets/drbeen-accounts")
EMAIL = os.environ.get("DRBEEN_EMAIL", "")
pw = os.environ.get("DRBEEN_PASSWORD", "")
if not pw:
    cred_path = os.path.join(SECRETS_DIR, f"{ACCOUNT}.creds")
    if os.path.isfile(cred_path):
        with open(cred_path) as f:
            pw = f.read().strip()
OUT = os.environ.get("DRBEEN_COOKIE_FILE", "/tmp/drbeen_cookies.txt")

if not EMAIL or not pw:
    print("Set DRBEEN_EMAIL and DRBEEN_PASSWORD or ~/.hermes/secrets/drbeen-accounts/<account>.creds", file=sys.stderr)
    sys.exit(1)

ua = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://www.drbeen.com/signin",
}
s = requests.Session()
s.get("https://www.drbeen.com/signin", headers=ua, timeout=30)
r = s.post(
    "https://www.drbeen.com/login",
    data={"username": EMAIL, "password": pw},
    headers=ua,
    allow_redirects=True,
    timeout=30,
)
if r.status_code != 200 or "/signin" in r.url:
    print(f"login failed: {r.status_code} -> {r.url}", file=sys.stderr)
    sys.exit(1)

with open(OUT, "w") as f:
    f.write("# Netscape HTTP Cookie File\n\n")
    for c in s.cookies:
        secure = "TRUE" if c.secure else "FALSE"
        tail = "TRUE" if c.domain.startswith(".") else "FALSE"
        exp = int(c.expires) if c.expires else 0
        f.write(f"{c.domain}\t{tail}\t{c.path}\t{secure}\t{exp}\t{c.name}\t{c.value}\n")
print(f"ok cookies={len(s.cookies)} -> {OUT}")