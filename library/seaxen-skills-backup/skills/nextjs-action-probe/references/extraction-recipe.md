# Extraction recipe (copy-paste)

## 1. Fetch page + collect chunk URLs
```bash
cd /tmp && curl -s -L "https://TARGET/page" -o page.html
grep -oE '/_next/static/chunks/[A-Za-z0-9_/.-]+\.js' page.html | sort -u > chunks.txt
```

## 2. Download every chunk
```bash
mkdir -p chunks && while read c; do
  fn=$(echo "$c" | sed 's#/_next/static/chunks/##')
  curl -s -L "https://TARGET$c" -o "chunks/$fn"
done < chunks.txt
```

## 3. Extract action IDs
```bash
grep -rhoE 'createServerReference\("([0-9a-f]{40,44})"' chunks/ \
  | sed -E 's/.*"([0-9a-f]+)"/\1/' | sort -u
```
- IDs are 40-42 hex chars. If you see `ffffffff...c90fdaa22168c234c4c6628b` that is the RFC 3526 DH prime, ignore it.
- Sometimes a friendly name trails: `createServerReference("...","socialLogin")`.

## 4. Reverse the call shape
Grep the HTML/JS for `fetch(`:
```bash
grep -aoE 'fetch\(window\.location\.href[^;]{0,400}' page.html
```
Copy the exact `body: JSON.stringify({...})` keys. Field names vary per site (e.g. `digits`, `brand`, `manual_action_id`).

## 5. Validate input format (CRITICAL)
Test with browser headers (bare POST -> 403):
```python
import json,urllib.request
H={"Content-Type":"application/json",
   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
   "Accept":"*/*","Accept-Language":"en-US,en;q=0.9",
   "Origin":"https://TARGET","Referer":"https://TARGET/page"}
def q(d):
    b=json.dumps({"digits":d,"brand":"AIRTEL","manual_action_id":AID}).encode()
    r=urllib.request.Request("https://TARGET/page",data=b,method="POST",headers=H)
    return json.loads(urllib.request.urlopen(r,timeout=30).read())
```
Probe these shapes for ONE expected-success value:
- full `01600502007`
- 8-digit tail `00502007`   <-- usually the real expected format
- short `31111`
If all EMPTY, you have the WRONG format, not "nothing found".
