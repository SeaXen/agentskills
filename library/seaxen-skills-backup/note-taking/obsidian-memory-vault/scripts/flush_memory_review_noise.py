#!/usr/bin/env python3
"""Reject all pending memory-review candidates (scanner noise after vault edits)."""
import json
import sys
import urllib.request

BASE = "http://127.0.0.1:6065"
NOTE = "flush_memory_review_noise.py — consolidated manually or false positive"


def main():
    with urllib.request.urlopen(f"{BASE}/api/memory-candidates?limit=50", timeout=30) as r:
        data = json.loads(r.read().decode())
    cands = data.get("candidates") or []
    if not cands:
        print("no pending candidates")
        return 0
    for c in cands:
        body = json.dumps({**c, "status": "rejected", "notes": NOTE}).encode()
        req = urllib.request.Request(
            f"{BASE}/api/memory-review",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as r:
            json.loads(r.read().decode())
        print("rejected", c.get("candidate_id", "")[:16])
    with urllib.request.urlopen(f"{BASE}/api/memory-health", timeout=30) as r:
        mh = json.loads(r.read().decode())
    pending = (mh.get("review_queue") or {}).get("pending")
    print("pending", pending, "score", mh.get("overall_score"))
    return 0 if pending == 0 else 1


if __name__ == "__main__":
    sys.exit(main())