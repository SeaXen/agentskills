#!/usr/bin/env python3
"""
Airtel VIP SIM Tracker - Single Fragment Infinite Search
Runs an infinite loop for one fragment (e.g., 0000, 1111, etc.) with 5-second interval.
Logs to a per-fragment file. Stops only when killed or when numbers are found.

Usage:
  python3 airtel_single_fragment.py 0000
  python3 airtel_single_fragment.py 1111
  ...

For parallel searches, launch multiple instances with different fragments.
"""
import json
import time
import sys
import urllib.request
import urllib.error

FRAGMENT = sys.argv[1] if len(sys.argv) > 1 else "0000"
URL = "https://mueagle.com/airtel_new"
ACTION_ID = "60e0f63a693b083fb961b661e6fd775e6ca25dc4ba"
H = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "*/*", "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://mueagle.com", "Referer": "https://mueagle.com/airtel_new",
}


def query(digits=FRAGMENT, brand="AIRTEL"):
    body = json.dumps({"digits": digits, "brand": brand, "manual_action_id": ACTION_ID}).encode()
    req = urllib.request.Request(URL, data=body, method="POST", headers=H)
    try:
        resp = json.loads(urllib.request.urlopen(req, timeout=45).read())
        return resp.get("status"), resp.get("numbers", [])
    except urllib.error.HTTPError as e:
        return f"HTTP{e.code}", []
    except Exception as e:
        return "ERR", []


def main():
    found = []
    attempt = 0
    logfile = f"/tmp/airtel_{FRAGMENT}.log"

    with open(logfile, "a") as f:
        f.write(f"=== STARTED fragment {FRAGMENT} ===\n")

    while True:
        attempt += 1
        st, nums = query(FRAGMENT)
        msg = f"[{FRAGMENT} Attempt {attempt}] {st}"
        if st == "SUCCESSFUL" and nums:
            for n in nums:
                ms = n.get("msisdn", "")
                if ms and ms not in found:
                    found.append(ms)
                    msg += f" FOUND: {ms}"
            msg += f" | TOTAL: {len(found)}"
        with open(logfile, "a") as f:
            f.write(msg + "\n")
        print(msg, flush=True)
        time.sleep(5)


if __name__ == "__main__":
    main()
