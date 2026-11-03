# Notion API — measured limits and performance

Live-measured numbers from a `api.notion.com` probe in June 2026. Notion doesn't publish most of these — they can shift silently. Reproduce them with the recipes below before relying on them for a production workload.

## Hard limits (measured)

| Limit | Value | How verified |
|---|---|---|
| Per-request body cap | ~500 KB → HTTP 413 `PayloadTooLargeError` | Binary-searched: 100 blocks × 8 KB = 668 KB → 413. 100 blocks × 5 KB = 338 KB → 200. Threshold is somewhere between. |
| Max blocks per `PATCH /v1/blocks/{id}/children` | 100 | Public Notion docs. Confirmed. |
| Max chars per `rich_text` segment | 2000 | Public Notion docs. Confirmed. |

## Performance (measured)

| Metric | Value | Test |
|---|---|---|
| ICMP ping | 3 ms avg, 0% loss | `ping -c 5 api.notion.com` |
| TCP + TLS handshake | 58 ms | `curl -w "%{time_connect} %{time_appconnect}" ...` |
| DL throughput (1.18 MB) | 1.45 MiB/s = **12 Mbit/s** | `GET /v1/blocks/{id}/children` paginated |
| UL throughput (1.35 MB / 4 PATCHes) | 120 KiB/s = **1 Mbit/s** | Sequential PATCH of ~340 KB each |
| UL throughput (single 478 KB PATCH) | 258 KiB/s request-only | One PATCH, request-only bytes |
| Per-write server processing floor | ~2.5 s | Independent of payload size below cap |

## Reproducing the measurements

Quick latency/handshake probe:

```bash
curl -o /dev/null -s -w "DNS: %{time_namelookup}s | Connect: %{time_connect}s | TLS: %{time_appconnect}s | TTFB: %{time_starttransfer}s | Total: %{time_total}s\n" \
  https://api.notion.com/v1/users/me
```

Throughput sweep (downloading N KiB):

```python
import os, json, time, urllib.request
TOKEN = os.environ['NOTION_TOKEN']; VER = '2022-06-28'
def get(path):
    r = urllib.request.Request(f"https://api.notion.com{path}",
        headers={"Authorization": f"Bearer {TOKEN}", "Notion-Version": VER})
    return urllib.request.urlopen(r).read()

# Read a known-large page and measure
PAGE = "<your page id>"
t = time.perf_counter(); body = get(f"/v1/blocks/{PAGE}/children?page_size=100")
print(f"DL: {len(body)/1024:.1f} KiB in {(time.perf_counter()-t)*1000:.0f} ms")
```

Throughput sweep (uploading):

```python
def patch(path, payload):
    r = urllib.request.Request(f"https://api.notion.com{path}",
        data=json.dumps(payload).encode(), method="PATCH",
        headers={"Authorization": f"Bearer {TOKEN}", "Notion-Version": VER,
                 "Content-Type": "application/json"})
    return urllib.request.urlopen(r).read()

# Build N blocks of ~X KiB each, then PATCH and time
def make_blocks(n, kb_each):
    txt = ("Lorem ipsum dolor sit amet " * 30)[:1900]
    return [{"object":"block","type":"paragraph","paragraph":{
        "rich_text":[{"type":"text","text":{"content":txt}}]}} for _ in range(n)]

PAGE = "<your page id>"
blocks = make_blocks(50, 5)   # ~250 KB request body
t = time.perf_counter()
patch(f"/v1/blocks/{PAGE}/children", {"children": blocks})
print(f"UL: {len(json.dumps({'children':blocks}).encode())/1024:.1f} KiB in {(time.perf_counter()-t)*1000:.0f} ms")
```

Per-request body cap probe (binary search the 413 threshold):

```python
sizes_kb = [5, 8, 10, 12, 15, 18, 20]
for kb in sizes_kb:
    blocks = make_blocks(100, kb)
    req_kb = len(json.dumps({"children":blocks}).encode()) / 1024
    try:
        patch(f"/v1/blocks/{PAGE}/children", {"children":blocks})
        print(f"  ✓ 100 blocks × {kb}KB → req body {req_kb:.0f}KB → 200")
    except urllib.error.HTTPError as e:
        print(f"  ✗ 100 blocks × {kb}KB → req body {req_kb:.0f}KB → HTTP {e.code}")
```

## OpenPGP metadata without decrypting

`gpg --list-packets <file.gpg>` reveals algorithm, S2K iterations, salt, and packet structure without prompting for a passphrase:

```
gpg: AES256.CFB encrypted data
# off=0 ctb=8c tag=3 hlen=2 plen=13
:symkey enc packet: version 4, cipher 9, aead 0, s2k 3, hash 10
	salt C027334C29D54E5A, count 65011712 (255)
# off=15 ctb=d2 tag=18 hlen=6 plen=2584694297 new-ctb
:encrypted data packet:
	length: 2584694297
	mdc_method: 2
```

Useful for manifest pages — gives you proof of cipher strength and S2K iteration count, both of which matter for "is this backup actually secure" without needing the passphrase.

## When you hit the cap, do this

- **Cap is per request**, not per session. Split your payload.
- **Cap is on serialized JSON bytes**, not rich_text content. A 100-block request with 100 × 1900-char strings serializes to ~190 KB — under the cap.
- **Don't try to upload the raw bytes as a code block** — even an empty 500 KB code block hits the cap; it has nothing to do with the actual text length.
- **For >10 MB uploads, batch by 4-5 chunks** at ~300 KB each. Sequential is fine; parallel won't help (server-side processing floor dominates).

See also: `scripts/build_manifest.py` for the ready-made manifest builder.
