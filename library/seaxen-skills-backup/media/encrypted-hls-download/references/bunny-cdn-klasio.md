# Bunny.net / Klasio (Laravel + Next.js/Alpine.js LMS) — AES-128 HLS download recipe

Verified end-to-end on **ononno.com** (Bangladeshi study-skills course platform, deep-focus-study-work-session-protocol, 15 lessons, 2.5 GB, h264 1080p, ~17 min batch + ~5 min retry).

## Platform fingerprint

- **CMS**: Klasio (`klasio_session` Laravel cookie, XSRF-TOKEN for CSRF)
- **Frontend**: Alpine.js (NOT React/Next.js despite the `next.js` headers — those are Caddy's defaults), axios for HTTP
- **Video CDN**: Bunny.net Stream — embed at `iframe.mediadelivery.net`, playlist + segments on `vz-XXXX.b-cdn.net`
- **Player**: `BunnyEmbedPlayer(container, {embedUrl, autoplay, ...})` from `player-0.1.0.min.js`
- **Encryption**: AES-128 CBC; segments named `*.dts` (NOT `.ts`)
- **Auth**: standard Laravel form auth on `/auth/login`, but the form includes an optional `fingerprint` field (fingerprintjs v4 from CDN) — **skip it**, server doesn't require it

## Step-by-step

### 1. Login

```bash
GET https://www.ononno.com/auth/login   # capture XSRF-TOKEN cookie + <meta name="csrf-token" content="...">
POST https://www.ononno.com/auth/login
  _token=<meta csrf value>     # from <meta>, NOT from XSRF-TOKEN cookie decode
  email=...
  password=...
  # NO fingerprint field needed
→ 302 → /student/dashboard, sets klasio_session cookie
```

The CSRF token in the form is the **decoded `<meta name="csrf-token">` value**, not the XSRF-TOKEN cookie (which is URL-encoded and for JS axios). Both work for Laravel's CSRF check, but the meta tag is what's literally in the form.

### 2. Save cookies in Netscape format (CRITICAL — yt-dlp rejects without header)

```python
import requests, re
# ... do login above ...

with open('/tmp/klasio_cookies.txt', 'w') as f:
    f.write('# Netscape HTTP Cookie File\n')
    f.write('# https://curl.haxx.se/rfc/cookie_spec.html\n')
    f.write('# This is a generated file! Do not edit.\n\n')
    for c in session.cookies:
        secure = 'TRUE' if c.secure else 'FALSE'
        tailmatch = 'TRUE' if c.domain.startswith('.') else 'FALSE'
        f.write(f'{c.domain}\t{tailmatch}\t{c.path}\t{secure}\t{int(c.expires) if c.expires else 0}\t{c.name}\t{c.value}\n')
```

### 3. Enumerate lessons from course overview page

```python
r = session.get('https://www.ononno.com/student/courses/{slug}/overview')
lesson_ids = re.findall(r'/student/chapter-item/redirect/(\d+)', r.text)
# Sort by order in HTML (curriculum order)
```

### 4. For each lesson: extract embed URL → resolve m3u8 via yt-dlp -g

```python
r = session.get(f'https://www.ononno.com/student/chapter-item/redirect/{lesson_id}',
                allow_redirects=True)
m = re.search(r"embedUrl:\s*['\"](https://iframe\.mediadelivery\.net/embed/(\d+)/([a-f0-9-]+)\?token=([^'\"]+)&expires=(\d+))['\"]",
              r.text)
embed_url, lib_id, vid_guid, token, expires = m.groups()
play_url = f"https://iframe.mediadelivery.net/play/{lib_id}/{vid_guid}?token={token}&expires={expires}"

# yt-dlp -g is the ONLY way to get the real m3u8 URL
res = subprocess.run([
    'yt-dlp', '--no-update', '-g',
    '--cookies', '/tmp/klasio_cookies.txt',
    '--add-header', 'Referer:https://www.ononno.com/',
    play_url,
], capture_output=True, text=True)
m3u8_urls = [u for u in res.stdout.strip().split('\n') if u]
```

**Why yt-dlp -g**: the `/play/{libId}/{guid}` endpoint returns an HTML wrapper page when called by `curl`/`requests`. yt-dlp's BunnyCdn extractor internally resolves it to the actual `vz-XXXX.b-cdn.net/.../{quality}/video.m3u8`. Skip trying to fetch `/play/` directly.

### 5. Fetch m3u8 + parse segments and AES key URI

```python
import requests
from Cryptodome.Cipher import AES

# Add Cookie header + Accept header that yt-dlp sends
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.ononno.com/',
    'Accept': 'application/vnd.apple.mpegurl,*/*',
}
mr = session.get(m3u8_urls[0], headers=headers)

# Parse media playlist
key_uri = iv_attr = None
segments = []
for line in mr.text.splitlines():
    line = line.strip()
    if not line: continue
    if '#EXT-X-KEY' in line:
        km = re.search(r'URI="([^"]+)"', line)
        im = re.search(r'IV=0x([0-9a-fA-F]+)', line)
        if km: key_uri = km.group(1)
        if im: iv_attr = bytes.fromhex(im.group(1))
    elif not line.startswith('#'):
        segments.append(line)
```

### 6. Fetch AES key (CRITICAL: from b-cdn.net, not mediadelivery.net)

```python
# Resolve key URI relative to the playlist host (b-cdn.net), NOT mediadelivery.net
if key_uri.startswith('/'):
    key_uri = f"{'/'.join(m3u8_urls[0].split('/')[:3])}{key_uri}"  # scheme + b-cdn host

# Add token + expires query params (Bunny requires this for key auth)
key_url_q = key_uri + (f"?token={token}&expires={expires}"
                        if '?' not in key_uri
                        else f"&token={token}&expires={expires}")

kr = session.get(key_url_q, headers={**headers, 'Origin': 'https://iframe.mediadelivery.net'})
assert len(kr.content) == 16, f"key fetch failed: status={kr.status_code} size={len(kr.content)}"
key = kr.content
```

### 7. Parallel download + AES-128-CBC decrypt

```python
abs_segs = [s if s.startswith('http') else f"{'/'.join(m3u8_urls[0].split('/')[:-1])}/{s.lstrip('/')}"
            for s in segments]

from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_decrypt(i, url, retries=3):
    for attempt in range(retries):
        try:
            rr = requests.get(url, headers=headers, timeout=120)
            if rr.status_code == 200 and rr.content:
                data = rr.content
                # IV = segment number as 16-byte big-endian (HLS spec default)
                iv = iv_attr if iv_attr else i.to_bytes(16, 'big')
                cipher = AES.new(key, AES.MODE_CBC, iv)
                plaintext = cipher.decrypt(data)
                # PKCS7 padding only on the LAST segment
                if i == len(abs_segs) - 1:
                    pad = plaintext[-1]
                    if 1 <= pad <= 16 and plaintext[-pad:] == bytes([pad]) * pad:
                        plaintext = plaintext[:-pad]
                return i, plaintext
        except Exception:
            if attempt == retries - 1: return i, None
    return i, None

results = [None] * len(abs_segs)
with ThreadPoolExecutor(max_workers=12) as pool:
    futs = {pool.submit(fetch_decrypt, i, u): i for i, u in enumerate(abs_segs)}
    for fut in as_completed(futs):
        i, d = fut.result()
        results[i] = d
```

### 8. Concat + remux to true MP4

```python
ts_path = output_path.replace('.mp4', '.ts.tmp')
with open(ts_path, 'wb') as f:
    for chunk in results:
        if chunk: f.write(chunk)

subprocess.run([
    'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
    '-i', ts_path,
    '-c', 'copy',
    '-movflags', '+faststart',
    output_path,
], check=True)
os.unlink(ts_path)
```

### 9. Verify

```bash
ffprobe -v error -show_entries format=format_name,duration:stream=codec_name,width,height \
       -of default=noprint_wrappers=1 output.mp4
# Expect: h264 1920x1080, aac, format_name=mov,mp4,m4a,3gp,3g2,mj2 (NOT mpegts)
# duration should match the lesson page's listed time
```

## Filename pitfall — ext4 255-byte limit

Bengali (and other 3-byte UTF-8 like Hindi, Tamil, Thai) titles blow past ext4's 255-byte path limit when combined with the `NN - ` prefix and `.ts.tmp` suffix. Sanitize to **≤60 chars** for the output filename; store the full Bengali title in a sidecar `MANIFEST.json`.

```python
def sanitize(n):
    n = re.sub(r'[\\/\:*?"<>|\r\n\t]', '_', n)
    n = re.sub(r'\s+', ' ', n).strip().rstrip('.')
    return n[:60]   # ≤60 chars safe for any UTF-8 + prefix + suffix
```

## Non-video lessons — what to expect

Klasio courses often include lessons that look like "chapters" but have no video:

| Type | Indicator | Action |
|---|---|---|
| Supplementary text + YouTube embed | Page has `<iframe src="https://www.youtube.com/embed/...">` but no `BunnyEmbedPlayer` | Extract the YouTube ID and save in MANIFEST; optionally download with yt-dlp |
| "Download Resource File" but tab says "No files available" | `id="material"` tab exists but `<div>No files available</div>` | Mark as text-only; nothing to download |
| Assignment / group-join pages | Title like "Phase Assignments" or "Joining the group", no player | Skip — pure text |

Always probe each lesson for `BunnyEmbedPlayer` or `player-container` in the HTML before declaring the course "done".

## Why the manual pipeline is mandatory for Bunny (and not for Synapse)

| | Synapse (vidinfra/tenbyte) | Bunny.net / Klasio |
|---|---|---|
| Segment extension | `.ts` (normal) | `.dts` (rejected by yt-dlp/ffmpeg HLS demuxers) |
| Key server host | `kms.vidinfra.com` (separate) | Same `b-cdn.net` as playlist (but needs `?token=`) |
| yt-dlp works? | Sometimes, with `--cookies-from-browser` | URL extraction only (`-g`); download always fails |
| Pipeline | Often yt-dlp alone | Always manual decrypt + remux |

## Reference

Verified on: 2026-06-22, course `deep-focus-study-work-session-protocol` on ononno.com.
- 23 lessons total, 15 videos downloaded successfully, 4 supplementary text+YouTube, 4 text-only assignments
- Total output: 2.5 GB across 15 MP4 files (1080p h264+aac)
- Auth: `klasio_session` Laravel cookie, valid for the duration of the batch
- Account being used: `hrsea7@gmail.com` (a known account of the user from prior Synapse work)