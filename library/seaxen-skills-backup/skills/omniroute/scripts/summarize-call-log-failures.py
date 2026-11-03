#!/usr/bin/env python3
"""Summarize OmniRoute call_log failures for a given date (default: today)."""
import argparse
import json
import glob
from collections import Counter
from datetime import date
from pathlib import Path

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--date", default=date.today().isoformat(), help="YYYY-MM-DD")
    p.add_argument("--data-dir", default="/mnt/tb/1Apps/omniroute/data")
    p.add_argument("--model", default=None, help="Filter requestedModel substring")
    args = p.parse_args()
    base = Path(args.data_dir) / "call_logs" / args.date
    if not base.is_dir():
        print(f"No logs: {base}")
        return 1
    fail = []
    for path in glob.glob(str(base / "*.json")):
        try:
            s = json.load(open(path)).get("summary", {})
            st = s.get("status") or 0
            if st < 400:
                continue
            m = s.get("requestedModel")
            if args.model and (not m or args.model not in m):
                continue
            fail.append(
                (
                    s.get("timestamp"),
                    st,
                    m,
                    s.get("provider"),
                    (s.get("account") or "")[:40],
                )
            )
        except Exception:
            pass
    fail.sort(reverse=True)
    print(f"Failures on {args.date}: {len(fail)}")
    by = Counter((m, prov, st) for _, st, m, prov, _ in fail)
    for k, c in by.most_common(25):
        print(f"  {c:4d}  model={k[0]!r} provider={k[1]!r} status={k[2]}")
    print("\nLast 15:")
    for row in fail[:15]:
        print(" ", *row)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())