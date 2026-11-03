#!/usr/bin/env python3
"""Ad-hoc verification after vault audit writes. Not a formal test suite."""
import json
import sys
import urllib.request
from pathlib import Path

VAULT = Path("/mnt/tb/hermes/obsedianvault")
REQUIRED = [
    "Knowledge/Mnemosyne Operations.md",
    "System/Assistant/context.md",
    "Memory/decisions.md",
]
RECALL_QUERY = "Mnemosyne Operations"


def main():
    ok = fail = 0
    for rel in REQUIRED:
        if (VAULT / rel).is_file():
            ok += 1
            print(f"OK  exists {rel}")
        else:
            fail += 1
            print(f"FAIL missing {rel}")
    try:
        url = f"http://127.0.0.1:6065/api/recall?query={RECALL_QUERY.replace(' ', '%20')}&limit=1"
        data = json.loads(urllib.request.urlopen(url, timeout=10).read())
        path = (data.get("results") or [{}])[0].get("path", "")
        if "Mnemosyne Operations" in path:
            ok += 1
            print(f"OK  recall_top {path}")
        else:
            fail += 1
            print(f"FAIL recall_top {path!r}")
    except Exception as e:
        fail += 1
        print(f"FAIL recall_api {e}")
    print(f"AD_HOC passed={ok} failed={fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())