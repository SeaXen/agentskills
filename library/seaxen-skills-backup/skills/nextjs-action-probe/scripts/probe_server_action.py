#!/usr/bin/env python3
"""Reusable safe scanner for a Next.js Server Action that returns available items.

Usage:
  python3 probe_server_action.py

Edits you must make per site:
  - URL, ACTION_ID
  - build_inputs(): the candidate input strings (match the site's expected FORMAT)
  - query(): the JSON body keys (digits/brand/manual_action_id are examples)
  - rank(): how to score/rank returned items

Safe defaults: 1.2s gap, concurrency 1, checkpoint-resume, browser headers.
"""
import json, time, urllib.request, urllib.error, os, threading, re

URL = "https://TARGET/page"
ACTION_ID = "PASTE_ACTION_ID_HERE"
RESULTS = "/tmp/probe_found.txt"
CKPT = "/tmp/probe_done.json"
H = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "*/*", "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://TARGET", "Referer": "https://TARGET/page",
}
lock = threading.Lock()
done = set(json.load(open(CKPT))) if os.path.exists(CKPT) else set()
found = []

def query(payload):
    b = json.dumps(payload).encode()
    req = urllib.request.Request(URL, data=b, method="POST", headers=H)
    try:
        return json.loads(urllib.request.urlopen(req, timeout=30).read())
    except urllib.error.HTTPError as e:
        return {"status": f"HTTP{e.code}"}
    except Exception:
        return {"status": "ERR"}

def build_inputs():
    # EXAMPLE: 8-digit tails (the part after a 016 prefix)
    out = [str(d) * 8 for d in range(10)]
    # add your VIP patterns here
    return out

def rank(item):
    # EXAMPLE: score an MSISDN for VIP patterns
    nat = item.get("msisdn", "")[5:]
    s = 0
    if re.search(r"(\d)\1{3,}", nat): s += 6
    if re.search(r"(\d)\1(\d)\2", nat): s += 5
    if nat == nat[::-1]: s += 7
    return s

def main():
    inputs = [x for x in build_inputs() if x not in done]
    print(f"remaining={len(inputs)}", flush=True)
    for i, inp in enumerate(inputs):
        j = query({"digits": inp, "brand": "AIRTEL", "manual_action_id": ACTION_ID})
        time.sleep(1.2)
        if j.get("status") == "SUCCESSFUL":
            for n in j.get("numbers", []):
                with lock:
                    found.append((n.get("msisdn"), rank(n), inp))
                    with open(RESULTS, "a") as f:
                        f.write(f"{n.get('msisdn')} | score={rank(n)} | from {inp}\n")
        with lock:
            done.add(inp)
            json.dump(sorted(done), open(CKPT, "w"))
        if i % 20 == 0:
            print(f"progress {i+1}/{len(inputs)} found={len(found)}", flush=True)
    found.sort(key=lambda r: r[1], reverse=True)
    print(f"DONE. collected={len(found)}", flush=True)

if __name__ == "__main__":
    main()
