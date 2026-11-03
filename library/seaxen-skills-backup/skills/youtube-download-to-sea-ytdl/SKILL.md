---
name: youtube-download-to-sea-ytdl
description: "Auto-download YouTube videos to /mnt/tb/#Sea/YTDL."
platforms: [linux]
---

# YouTube Download to /mnt/tb/#Sea/YTDL

## When to use
Use when the user pastes a YouTube URL and wants it downloaded and saved to `/mnt/tb/#Sea/YTDL` automatically.

## Trigger
- User message contains a YouTube URL (`youtube.com/watch?v=...` or `youtu.be/...`)
- User explicitly says "download this" or "save this" with a YouTube link

## Default behavior
1. Detect YouTube URL in the user message.
2. Download the **best available MP4** format (`bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]`).
3. Embed metadata and thumbnail into the MP4 file.
4. Save **video** to `/mnt/tb/#Sea/YTDL/` with filename: `<video_title> [<video_id>].mp4`
5. Save **metadata sidecars** (`.webp` thumbnail + `.info.json`) to `/mnt/tb/#Sea/YTDL/meta/` with the same base filename.
6. Reply with the saved path and file stats (size, duration, resolution).

## Command template
```bash
yt-dlp \
  --no-playlist \
  --format "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" \
  --merge-output-format mp4 \
  --embed-metadata \
  --embed-thumbnail \
  --write-thumbnail \
  --write-info-json \
  -o '/mnt/tb/#Sea/YTDL/%(title)s [%(id)s].%(ext)s' \
  '<youtube_url>' \
  && mv '/mnt/tb/#Sea/YTDL/%(title)s [%(id)s].webp' '/mnt/tb/#Sea/YTDL/meta/' \
  && mv '/mnt/tb/#Sea/YTDL/%(title)s [%(id)s].info.json' '/mnt/tb/#Sea/YTDL/meta/'
```

## Options handled
- `--no-playlist`: only the single video, not a playlist
- `--format "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"`: best MP4 quality
- `--merge-output-format mp4`: force MP4 container
- `--embed-metadata`: title, uploader, duration baked into the file
- `--embed-thumbnail`: cover image inside the MP4 container
- `--write-thumbnail`: standalone thumbnail image
- `--write-info-json`: sidecar JSON with full metadata
- Output path: `/mnt/tb/#Sea/YTDL/` for video, `/mnt/tb/#Sea/YTDL/meta/` for sidecars

## Edge cases
- If the video is age-restricted or private, yt-dlp will error; report the error to the user.
- If the title contains special characters, yt-dlp sanitizes the filename automatically.
- If the download is interrupted, partial files remain; user can retry or clean up.
- If the user wants a different format (e.g., audio-only), they must specify it explicitly.

## Verification
After download, confirm:
- File exists at the expected path
- File size > 0
- Duration metadata is present
- Thumbnail is embedded or sidecar exists in `/mnt/tb/#Sea/YTDL/meta/`

## Example outputs
- Video: `/mnt/tb/#Sea/YTDL/Surah Yasin (Yaseen) | By Zain Abu Kautsar | Full With Arabic Text | 36سورۃ یس [yR83VyigxCg].mp4`
- Meta: `/mnt/tb/#Sea/YTDL/meta/Surah Yasin (Yaseen) | By Zain Abu Kautsar | Full With Arabic Text | 36سورۃ یس [yR83VyigxCg].webp`
- Meta: `/mnt/tb/#Sea/YTDL/meta/Surah Yasin (Yaseen) | By Zain Abu Kautsar | Full With Arabic Text | 36سورۃ یس [yR83VyigxCg].info.json`

## Notes
- yt-dlp on this host is version 2026.03.03; may show "older than 90 days" warning — harmless.
- SABR-only streaming experiment warnings from YouTube are normal; yt-dlp falls back to available formats.
- Embedding uses ffmpeg fallback (neither mutagen nor AtomicParsley installed).