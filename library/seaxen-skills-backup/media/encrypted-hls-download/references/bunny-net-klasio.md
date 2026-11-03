# Klasio / Bunny.net — AES-128 HLS with `.dts` segments

Different platform than the vidinfra/tenbyte pattern in the main SKILL.md. Same
class of problem (encrypted HLS from a paid course LMS), but the recipe differs
in three ways: (1) key URI is on the CDN host not a separate `kms.*` server,
(2) segment extension is `.dts` not `.ts`, (3) yt-dlp's native HLS path fails
even with pycryptodomex because ffmpeg's HLS demuxer rejects `.dts`.

## Platform fingerprint

- LMS: **Klasio** — Laravel backend, Alpine.js frontend. Auth is a plain HTML
  form POST to `/auth/login` with `username`, `password`, and `_token` (from
  `<meta name="csrf-token">` on the form page). No Playwright / HMAC signing /
  device fingerprint required despite a hidden `fingerprint` field.
- Video CDN: **Bunny.net Stream** — `iframe.mediadelivery.net/embed/{library_id}/{video_guid}?token=...&expires=...`,
  signed URLs that expire in a few hours, IP+UA bound.
- Course/lesson URLs: `/courses/{slug}/lessons/{title-slug}` and
  `/student/chapter-item/redirect/{id}` (the redirect endpoint resolves to a
  real lesson URL).
- Detection: look for `XSRF-TOKEN` cookie + `klasio_session` cookie in the
  first GET to the login page; HTML contains `BunnyEmbedPlayer` and a JS block
  like `embedUrl: 'https://iframe.mediadelivery.net/embed/...'` on every
  lesson page.

## Why yt-dlp's native HLS path fails

`yt-dlp -g` on the embed URL **does** return the right m3u8 (the 1080p variant
URL on the b-cdn.net edge), so use it for URL discovery only. Then drive the
download yourself because:

1. **`.dts` segments.** Bunny's HLS uses `.dts` (Delta TS) for segment files.
   ffmpeg's HLS demuxer refuses them with
   `URL ... .dts is not in allowed_segment_extensions`. The
   `-allowed_extensions ALL` flag does NOT propagate through yt-dlp's
   `--downloader-args "ffmpeg:..."` for HLS invocations — yt-dlp's
   internal HLS code calls ffmpeg differently.
2. **AES-128 key host.** The `EXT-X-KEY` URI in the playlist is a path like
   `/{guid}/key/{token}`. Resolved against the *CDN host* of the playlist
   (`b-cdn.net`), NOT against `iframe.mediadelivery.net`. yt-dlp picks the
   wrong base some fraction of the time and gets a 404.
3. **No HMAC.** Unlike the vidinfra/tenbyte pattern, no headers need to be
   signed per request. The signed token in the embed URL is the only auth.

## Working pipeline

```python
import re, os, subprocess, requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from Cryptodome.Cipher import AES

sess = requests.Session()
# Load cookies from /tmp/klasio_cookies.txt (Netscape format — see pitfall #1)

# 1. Resolve lesson page → embed URL
r = sess.get(f"https://www.ononno.com/student/chapter-item/redirect/{lesson_id}",
             headers={"User-Agent": "...", "Referer": "https://www.ononno.com/"},
             allow_redirects=True, timeout=30)
m = re.search(r"embedUrl:\s*['\"](https://iframe\.mediadelivery\.net/embed/(\d+)/([a-f0-9-]+)\?token=([^'\"]+)&expires=(\d+))['\"]", r.text)
embed_url, lib_id, vid_guid, token, expires = m.groups()
play_url = f"https://iframe.mediadelivery.net/play/{lib_id}/{vid_guid}?token={token}&expires={expires}"

# 2. yt-dlp -g to extract the actual m3u8 URL (returns 1080p variant direct on b-cdn.net)
res = subprocess.run(["yt-dlp", "--no-update", "-g", "--cookies", "/tmp/klasio_cookies.txt",
                      "--add-header", "Referer:https://www.ononno.com/", play_url],
                     capture_output=True, text=True, timeout=60)
m3u8_url = res.stdout.strip().split("\n")[0]

# 3. Fetch the m3u8
mr = sess.get(m3u8_url, headers={"User-Agent": "...", "Referer": "https://www.ononno.com/",
                                  "Accept": "application/vnd.apple.mpegurl,*/*"}, timeout=30)
# mr.text is the media playlist (Bunny returns 1080p media directly, not master)

# 4. Parse: EXT-X-KEY URI + segment list
key_uri, iv_attr, segments = None, None, []
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

# 5. Fetch AES key — resolved against the CDN host of the m3u8, NOT mediadelivery
if key_uri.startswith('/'):
    key_uri = f"{'/'.join(m3u8_url.split('/')[:3])}{key_uri}"
key_url_q = key_uri + (f"?token={token}&expires={expires}" if '?' not in key_uri else f"&token={token}&expires={expires}")
key = sess.get(key_url_q, headers={"User-Agent": "...", "Referer": "https://www.ononno.com/",
                                     "Origin": "https://iframe.mediadelivery.net"}, timeout=30).content
# key must be exactly 16 bytes; if you got 0 or 404, the host or token was wrong

# 6. Parallel download + AES-128-CBC decrypt
def fetch_dec(i_url):
    i, u = i_url
    rr = requests.get(u, headers={"User-Agent": "...", "Referer": "https://www.ononno.com/"}, timeout=120)
    data = rr.content
    if key:
        iv = iv_attr if iv_attr else i.to_bytes(16, 'big')   # default IV = segment number, 16-byte BE
        data = AES.new(key, AES.MODE_CBC, iv).decrypt(data)
        if i == len(segments) - 1:                          # PKCS7 strip on last segment only
            pad = data[-1]
            if 1 <= pad <= 16 and data[-pad:] == bytes([pad]) * pad:
                data = data[:-pad]
    return i, data

results = [None] * len(segments)
with ThreadPoolExecutor(max_workers=12) as pool:
    futs = {pool.submit(fetch_dec, (i, u)): i for i, u in enumerate(segments)}
    for fut in as_completed(futs):
        i, d = fut.result()
        results[i] = d

# 7. Concat TS → ffmpeg remux to true MP4
tmp_ts = out_path[:-4] + ".ts.tmp"
with open(tmp_ts, 'wb') as f:
    for chunk in results: f.write(chunk)
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                "-i", tmp_ts, "-c", "copy", "-movflags", "+faststart", out_path], check=True)
os.unlink(tmp_ts)
```

## Pitfalls

1. **Cookies file MUST be Netscape format with the `# Netscape HTTP Cookie File`
   header line.** Without the header, yt-dlp's `--cookies file` silently fails
   with `does not look like a Netscape format cookies file` and the entire
   batch errors out at `-g` with no useful trace. Write the header yourself:
   ```python
   f.write('# Netscape HTTP Cookie File\n')
   f.write('# https://curl.haxx.se/rfc/cookie_spec.html\n\n')
   for c in session.cookies:
       f.write(f'{c.domain}\t{...}\t{c.path}\t{...}\t{expires}\t{c.name}\t{c.value}\n')
   ```

2. **Klasio login form** — `_token` is the CSRF token from
   `<meta name="csrf-token">` on the `/auth/login` page. There is a hidden
   `fingerprint` field but it is NOT required server-side; the form accepts
   requests without it. The `fingerprint` field is a fingerprintjs v4 output
   that the LMS computes client-side for analytics.

3. **Re-login on session expiry** — Klasio's session lifetime is short
   (hours). If a later lesson in a batch fails at `yt-dlp -g` with "video
   inaccessible" or empty body, refresh the session (re-POST login) and retry.
   A common pattern is `if yt-dlp -g fails: refresh_cookies(); retry once`.

4. **Filename length on non-ASCII titles** — Bengali / Sinhala / other
   multi-byte scripts hit ext4's 255-byte path limit fast. The combined
   `<output_dir>/<index> - <title>.mp4` path with even short titles can blow
   past 255 bytes. Sanitize titles to ~60 chars OR use an English shortname
   for the file and store the full title in a sibling MANIFEST.json.

5. **Bunny CDN host may vary per video** — different videos in the same
   course can sit on different `vz-xxxx.b-cdn.net` edges. The token in
   the embed URL is host-bound; using a token from one edge against
   another's URLs gives 403. Always fetch a fresh token per video from
   the lesson page.

6. **yt-dlp version** — `yt-dlp < 2024.x` does not have the `BunnyCdn`
   extractor. The recipe here only needs `yt-dlp -g` which works on any
   recent version, but if you try yt-dlp's full HLS download path on an old
   version, you may see `Unsupported URL`.

7. **No DRM** — this is AES-128, not Widevine / SAMPLE-AES. The decrypt
   recipe works. If you see `SAMPLE-AES` instead of `METHOD=AES-128` in
   the playlist, the video is Widevine-protected and this recipe cannot
   help — fall back to screen recording.

## Quick test for a new platform

```bash
# 1. Confirm Klasio
curl -sI https://<site>/auth/login | grep -E "(XSRF|klasio_session|Set-Cookie)"
# 2. Confirm Bunny CDN
curl -s https://<site>/student/courses/.../overview | grep -oE 'iframe\.mediadelivery\.net/embed/[0-9]+'
# 3. Confirm AES-128 (not SAMPLE-AES / no key at all)
yt-dlp -g --cookies /tmp/cookies.txt "<embed_url>" 2>&1 | tail -5
curl -s "<cdn_url>/playlist.m3u8" | grep EXT-X-KEY
```

If all three return as expected, apply the recipe above. If step 3 shows
`SAMPLE-AES` or no `EXT-X-KEY` line, the platform is using a different
encryption scheme and the main SKILL.md patterns (vidinfra/tenbyte,
Playwright HMAC capture) likely apply instead.
