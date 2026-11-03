#!/usr/bin/env python3
"""Ad-hoc verify Learn tab + /api/learn-bridge on vault dashboard :6065."""
import json
import sys
import urllib.request

BASE = "http://127.0.0.1:6065"


def main() -> int:
    home = urllib.request.urlopen(f"{BASE}/", timeout=15).read().decode()
    if "learn-bridge" not in home or "loadLearnBridge" not in home:
        print("FAIL home missing learn-bridge UI")
        return 1
    api = json.loads(urllib.request.urlopen(f"{BASE}/api/learn-bridge", timeout=15).read())
    if api.get("mode") != "learn-bridge-v1":
        print("FAIL api mode", api.get("mode"))
        return 1
    if len(api.get("matrix") or []) < 5:
        print("FAIL matrix short")
        return 1
    print("OK learn tab", api.get("skill", {}).get("version"))
    return 0


if __name__ == "__main__":
    sys.exit(main())