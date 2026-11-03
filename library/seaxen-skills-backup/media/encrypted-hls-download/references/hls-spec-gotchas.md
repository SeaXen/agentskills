# HLS spec gotchas that bite you in production

These are lessons that cost real debugging time. Each one is correct per the HLS spec (RFC 8216) but easy to miss when you're writing a downloader.

## 1. The `IV=` attribute is optional. If missing, the default is the segment number.

From RFC 8216 §4.3.2.4:
> If the IV attribute is not present, then the Media Sequence Number of the segment is used as the IV.

So for an unencrypted-IV manifest like:
```
#EXT-X-KEY:METHOD=AES-128,URI="https://kms.example.com/v1/keys?content_id=ABC"
#EXTINF:4.0,
segment-0.ts
#EXTINF:4.0,
segment-1.ts
```

The IVs are:
- segment-0.ts → `0x00000000000000000000000000000000`
- segment-1.ts → `0x00000000000000000000000000000001`
- segment-N.ts → N as 16-byte big-endian

If you use the wrong IV (e.g. all-zero), the first segment decrypts correctly (because zero IV = segment-0 IV) and **every other segment decrypts to garbage**. Easy to mistake for "AES-128 doesn't work for this platform" when the actual bug is one line of code.

**Fix:**
```python
iv = segment_index.to_bytes(16, "big")
cipher = AES.new(key, AES.MODE_CBC, iv)
```

## 2. Playlists are CRLF, and that breaks `re.MULTILINE` regex

RFC 8216 §4.1:
> Lines in a Playlist file are terminated by either a single line feed character or a carriage return and a line feed character.

The major packagers (Apple, Wowza, AWS MediaConvert) emit `\r\n`. So a typical playlist looks like:
```
#EXTM3U\r\n
#EXT-X-VERSION:3\r\n
...
#EXTINF:4.000000,\r\n
segment-0.ts\r\n
```

Python's `re.MULTILINE` makes `^` and `$` match line boundaries defined by `\n`. But `$` matches **before** `\n`, not before `\r\n`. So:

```python
# ❌ Finds ZERO matches on CRLF playlists
re.findall(r"^segment-(\d+)\.ts$", playlist, re.MULTILINE)

# ✅ Works on both LF and CRLF
re.findall(r"^segment-(\d+)\.ts\s*$", playlist, re.MULTILINE)
```

Always include `\s*$` (or use `re.splitlines()` first, which strips both line endings).

## 3. PKCS7 padding only on the LAST segment

CBC-encrypted segments are padded to a 16-byte block boundary. The padding is PKCS7. **Every segment except the last** is exactly N × 16 bytes (so the next segment can be decrypted independently). The last segment has the padding baked in, and the padding is `0x01` to `0x10` (1 to 16 bytes).

```python
pad = decrypted[-1]
if 1 <= pad <= 16 and decrypted[-pad:] == bytes([pad]) * pad:
    decrypted = decrypted[:-pad]
```

The validation step (`decrypted[-pad:] == bytes([pad]) * pad`) is critical. Without it, any random last-byte value in the 0x01–0x10 range will be mis-stripped, corrupting the last frame. The check costs nothing and saves you from silent corruption.

## 4. Master playlist vs media playlist

The URL `playlist.m3u8` at the root of a stream ID is the **master playlist** — it lists quality variants, not segments:
```
#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=3460352,RESOLUTION=1280x720
720p/media.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=2011232,RESOLUTION=854x480
480p/media.m3u8
```

You must follow up to `<quality>/media.m3u8` to get the actual segment list. The script in this skill does this — pass the stream ID and quality, and the playlist parser handles the second fetch.

## 5. The output is MPEG-TS, not MP4

HLS segments are MPEG-TS, so the concatenated output is also MPEG-TS. Players:
- ✅ VLC, mpv, ffmpeg, all modern browsers, iOS Safari, Android ExoPlayer, MX Player
- ❌ Some Android gallery apps, some strict "MP4 only" hardware players

If the user reports "won't play on my phone" and it's an older or off-brand Android, remux:
```bash
ffmpeg -i input.ts -c copy output.mp4
```
This is a stream copy (no re-encode), completes in seconds, and produces a proper MP4 container.

## 6. The `EXT-X-PLAYLIST-TYPE:VOD` tag is your friend

If the master or media playlist has `#EXT-X-PLAYLIST-TYPE:VOD`, it's a Video-On-Demand file: fixed start, fixed end, no sliding window. **All segments are present from the moment you fetch the playlist** — no need to keep re-polling. This is what you get for recorded lectures. Live streams (`#EXT-X-PLAYLIST-TYPE:EVENT` or no tag) are a different problem and not covered by this skill.

## 7. 4-second segments = ~1.6 KB overhead per segment for HLS

The standard HLS target duration is 6 seconds, but Bangladeshi / South Asian LMS packagers (vidinfra, moxion) tend to use **4-second segments** for lower latency. With 1892 segments × 4 seconds = 7568 s = 2h6m — matches the video duration. Don't be surprised when the segment count looks high.

## 8. AES-128 vs SAMPLE-AES — know the difference

- `METHOD=AES-128` — whole segment is AES-CBC encrypted. **This skill covers this.**
- `METHOD=SAMPLE-AES` — individual audio/video NAL units are encrypted (often with CENC/ctts). Needs a CENC decryptor + demuxer, and the keys are often behind Widevine/PlayReady license servers. **This skill does not cover this.**

If you see `SAMPLE-AES` in the manifest, tell the user: "this is real DRM, not just stream encryption, and the only legal way to view offline is the platform's own app."

## 9. KMS response is RAW bytes, not JSON

A correct key response from `kms.vidinfra.com` is 16 raw bytes — no JSON wrapper, no base64. If you accidentally `await r.text()` and the bytes are interpreted as UTF-8, you'll get Unicode replacement characters and your AES.new() will fail with "key length must be 16, 24, or 32 bytes". Always use `await r.body()` (or `response.content` in requests) to get raw bytes.

## 10. Concurrent downloads need their own HTTPS connection per request

`urllib.request` is not thread-safe for the default opener, but creating a new `urllib.request.Request()` per call inside a ThreadPoolExecutor worker is fine because each worker makes its own connection. Don't share a single `urllib.request.urlopen()` or `requests.Session()` across threads without explicit locking. Or use `httpx` with `Limits(max_connections=N)` — cleaner.
