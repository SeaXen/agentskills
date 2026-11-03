#!/usr/bin/env python3
"""
Safe external sweep runner — reverse-engineered relay pattern.

Adapt per site:
  - URL          : the page the tracker POSTs to (often its own URL)
  - ACTION_ID     : the 42-char Next.js Server Action ID extracted from JS chunks
  - HEADERS       : browser-like headers (Origin/Referer must match the site)
  - build_jobs()  : replicate the site's own candidate generator exactly
  - query() body  : match the JSON keys the site sends (digits/brand/manual_action_id)

Safe by design:
  - concurrency 1, ~1.2s gap between requests
  - 403 backoff: waits and re-probes every 30s up to 10 min, then aborts cleanly
  - checkpoint (done.json) + results (results.json) so re-runs resume and MERGE
  - records ONLY real SUCCESSFUL responses; never fabricates
  - pure outbound POSTs: does NOT touch host network/Discord connection
"""
import json, time, urllib.request, urllib.error, os, threading

URL = "https://TARGET.example/path"          # <-- set
ACTION_ID = "60e0f63a693b083fb961b661e6fd775e6ca25dc4ba"  # <-- set
SUBS = ["3", "7", "8", "9", "4"]               # site-specific prefix blocks
RESULTS = "/tmp/sweep_results.json"
CHECKPOINT = "/tmp/sweep_done.json"
BASE_DELAY = 1.2
MAX_403_WAIT = 600
LOCK = threading.Lock()

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "*/*", "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://TARGET.example",        # <-- match URL origin
    "Referer": "https://TARGET.example/path",  # <-- match page
}

found = json.load(open(RESULTS)) if os.path.exists(RESULTS) else {}
done = set(json.load(open(CHECKPOINT))) if os.path.exists(CHECKPOINT) else set()

def gen_candidates(frag, subs=SUBS):
    c = []
    for sub in subs:
        c.append(sub + frag)
        if len(frag) <= 4:
            for d in range(10):
                c.append(sub + str(d) + frag)
    return c

def build_jobs():
    # Example: triples 111..000 + curated VIP patterns. Adapt freely.
    jobs = [f"{d}{d}{d}" for d in range(1, 10)] + ["000"]
    vip = ["1122","1001","1234","9999"]  # extend as needed
    jobs += vip
    return jobs

def query(frag, wait=0):
    if wait:
        time.sleep(wait)
    body = json.dumps({"digits": frag, "brand": "AIRTEL",
                       "manual_action_id": ACTION_ID}).encode()
    req = urllib.request.Request(URL, data=body, method="POST", headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return {"status": f"HTTP{e.code}"} if e.code == 403 else {"status": f"HTTP{e.code}"}
    except Exception as e:
        return {"status": "ERR", "message": str(e)[:100]}

def wait_out_403():
    waited = 0
    while waited < MAX_403_WAIT:
        time.sleep(30); waited += 30
        try:
            if query("1234").get("status") != "HTTP403":
                print(f"[403 cleared after ~{waited}s]", flush=True); return True
        except Exception:
            pass
        print(f"[still 403 @ {waited}s]", flush=True)
    return False

def main():
    jobs = build_jobs()
    remaining = [j for j in jobs if j not in done]
    print(f"total={len(jobs)} done={len(done)} remaining={len(remaining)}", flush=True)
    for idx, frag in enumerate(remaining):
        res = query(frag, wait=BASE_DELAY)
        st = res.get("status")
        if st == "HTTP403":
            print(f"[403 on {frag}] backing off", flush=True)
            if not wait_out_403():
                print("[aborting - 403 persists]", flush=True); break
            continue
        if st == "SUCCESSFUL":
            ms = [n.get("msisdn") for n in res.get("numbers", []) if n.get("msisdn")]
            if ms:
                with LOCK:
                    found[frag] = ms
                    json.dump(found, open(RESULTS, "w"))
                    done.add(frag); json.dump(sorted(done), open(CHECKPOINT, "w"))
                print(f"HIT {frag}: {ms}", flush=True); continue
        with LOCK:
            done.add(frag); json.dump(sorted(done), open(CHECKPOINT, "w"))
        if idx % 15 == 0:
            print(f"progress {idx+1}/{len(remaining)} frag={frag} status={st} hits={len(found)}", flush=True)
    print(f"DONE. total hits={len(found)}", flush=True)
    print(json.dumps(found, indent=2), flush=True)

if __name__ == "__main__":
    main()
