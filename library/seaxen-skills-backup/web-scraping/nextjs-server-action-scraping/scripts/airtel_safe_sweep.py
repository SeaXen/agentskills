#!/usr/bin/env python3
"""
Safe Next.js Server-Action sweeper (reusable).
Replays a site's Server Action POST to scan candidate serials/numbers,
writing any SUCCESSFUL values to a results .txt file. Checkpoint-resumable.

Env / edit before run:
  URL, ACTION_ID, BRAND, SUBS, FRAGMENTS, OUT_TXT, CKPT, GAP
"""
import json, time, os, urllib.request, urllib.error, threading

URL = "https://mueagle.com/airtel_new"
ACTION_ID = "60e0f63a693b083fb961b661e6fd775e6ca25dc4ba"
BRAND = "AIRTEL"
SUBS = ["3", "7", "8", "9", "4"]
OUT_TXT = "/tmp/available_list.txt"
CKPT = "/tmp/sweep_done.json"
GAP = 1.0  # seconds between requests

H = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "*/*", "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://mueagle.com", "Referer": "https://mueagle.com/airtel_new",
}
lock = threading.Lock()
done = set(json.load(open(CKPT))) if os.path.exists(CKPT) else set()
available = []

def query(digits):
    b = json.dumps({"digits": digits, "brand": BRAND, "manual_action_id": ACTION_ID}).encode()
    req = urllib.request.Request(URL, data=b, method="POST", headers=H)
    try:
        j = json.loads(urllib.request.urlopen(req, timeout=30).read())
        return j.get("status"), j.get("numbers", [])
    except urllib.error.HTTPError as e:
        return f"HTTP{e.code}", []
    except Exception:
        return "ERR", []

def build_fragments():
    # EDIT: your pattern set. Default = 4-digit quads across SUBS.
    frags = []
    for d in range(1, 10):
        frags.append(str(d) * 4)
    # add more patterns here
    return frags

def main():
    frags = [f for f in build_fragments() if f not in done]
    print(f"remaining={len(frags)}", flush=True)
    hits = 0
    for i, f in enumerate(frags):
        st, ns = query(f)
        time.sleep(GAP)
        if st == "SUCCESSFUL" and ns:
            ms = [x.get("msisdn") for x in ns if x.get("msisdn")]
            with lock:
                available.extend(ms)
                with open(OUT_TXT, "a") as fh:
                    for m in ms:
                        fh.write(m + "\n")
                done.add(f); json.dump(sorted(done), open(CKPT, "w"))
            hits += len(ms)
            print(f"HIT {f}: {ms}", flush=True)
        else:
            with lock:
                done.add(f); json.dump(sorted(done), open(CKPT, "w"))
        if i % 25 == 0:
            print(f"progress {i+1}/{len(frags)} {f} {st} hits={hits}", flush=True)
    print(f"DONE. hits={hits}", flush=True)

if __name__ == "__main__":
    main()
