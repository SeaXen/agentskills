#!/usr/bin/env python3
"""Ad-hoc LAN + public health for tunneled Manifest (mf.xuup.top). Not a test suite."""
import json
import ssl
import sys
import urllib.request
from pathlib import Path

SEADASH = Path("/mnt/tb/1Apps/SeaDash/seadash-config.json")
LAN = "http://192.168.0.222:2099/api/v1/health"
PUBLIC = "https://mf.xuup.top/api/v1/health"
UA = "curl/8.0 hermes-verify"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20, context=ssl.create_default_context()) as r:
        return r.status, r.read().decode(errors="replace")[:300]


def main():
    fails = []
    if SEADASH.exists():
        routes = (json.loads(SEADASH.read_text()).get("cloudflare") or {}).get("routes") or []
        if not any(r.get("public_url") == "https://mf.xuup.top" for r in routes):
            fails.append("SeaDash mf route missing")
    for label, url in (("LAN", LAN), ("public", PUBLIC)):
        try:
            code, body = fetch(url)
            if code != 200 or "healthy" not in body:
                fails.append(f"{label} bad: {code}")
        except Exception as e:
            fails.append(f"{label} {e}")
    if fails:
        print("FAIL", fails)
        sys.exit(1)
    print("OK ad-hoc health")
    sys.exit(0)


if __name__ == "__main__":
    main()