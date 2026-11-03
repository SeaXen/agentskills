---
name: youtube-content
description: "YouTube transcripts to summaries, threads, blogs."
platforms: [linux, macos, windows]
---

# YouTube Content Tool

## When to use

Use when the user shares a YouTube URL or video link, asks to summarize a video, requests a transcript, or wants to extract and reformat content from any YouTube video. Transforms transcripts into structured content (chapters, summaries, threads, blog posts).

Extract transcripts from YouTube videos and convert them into useful formats.

## Setup

```bash
pip install youtube-transcript-api
```

## Helper Script

`SKILL_DIR` is the directory containing this SKILL.md file. The script accepts any standard YouTube URL format, short links (youtu.be), shorts, embeds, live links, or a raw 11-character video ID.

```bash
# JSON output with metadata
python3 SKILL_DIR/scripts/fetch_transcript.py "https://youtube.com/watch?v=VIDEO_ID"

# Plain text (good for piping into further processing)
python3 SKILL_DIR/scripts/fetch_transcript.py "URL" --text-only

# With timestamps
python3 SKILL_DIR/scripts/fetch_transcript.py "URL" --timestamps

# Specific language with fallback chain
python3 SKILL_DIR/scripts/fetch_transcript.py "URL" --language tr,en
```

## Output Formats

After fetching the transcript, format it based on what the user asks for:

- **Chapters**: Group by topic shifts, output timestamped chapter list
- **Summary**: Concise 5-10 sentence overview of the entire video
- **Chapter summaries**: Chapters with a short paragraph summary for each
- **Thread**: Twitter/X thread format — numbered posts, each under 280 chars
- **Blog post**: Full article with title, sections, and key takeaways
- **Quotes**: Notable quotes with timestamps

### Example — Chapters Output

```
00:00 Introduction — host opens with the problem statement
03:45 Background — prior work and why existing solutions fall short
12:20 Core method — walkthrough of the proposed approach
24:10 Results — benchmark comparisons and key takeaways
31:55 Q&A — audience questions on scalability and next steps
```

## Workflow

1. **Fetch** the transcript using the helper script with `--text-only --timestamps`.
2. **Validate**: confirm the output is non-empty and in the expected language. If empty, retry without `--language` to get any available transcript. If still empty, tell the user the video likely has transcripts disabled.
3. **Chunk if needed**: if the transcript exceeds ~50K characters, split into overlapping chunks (~40K with 2K overlap) and summarize each chunk before merging.
4. **Transform** into the requested output format. If the user did not specify a format, default to a summary.
5. **Verify**: re-read the transformed output to check for coherence, correct timestamps, and completeness before presenting.

## Error Handling

- **Transcript disabled**: tell the user; suggest they check if subtitles are available on the video page.
- **Private/unavailable video**: relay the error and ask the user to verify the URL.
- **No matching language**: retry without `--language` to fetch any available transcript, then note the actual language to the user.
- **Dependency missing**: run `pip install youtube-transcript-api` and retry.
- **YouTube blocks the host IP / 429 / bot check**: on this host, use the local fallback script `~/.hermes/scripts/yt_transcript_fallback.py` (actual path `/root/.hermes/scripts/yt_transcript_fallback.py`). It first tries `youtube-transcript-api`, then falls back to `yt-dlp --cookies-from-browser firefox` using the local Firefox profile cookies. Example:
  ```bash
  /root/.hermes/scripts/yt_transcript_fallback.py "https://www.youtube.com/watch?v=VIDEO_ID"
  ```
  This path does not require a YouTube API key for public videos, but it does depend on a usable local Firefox cookie jar on this machine.

## Retrieval-first durable lesson

Do not split transcript retrieval and transcript transformation into separate mental workflows unless a debugging session truly requires it. The stable umbrella behavior is:
1. try the light transcript path first
2. fall back to cookie-backed `yt-dlp` if YouTube blocks the host IP
3. only call retrieval "working" when you actually have transcript text, not just metadata
4. then continue into summaries / chapters / blogs / notes inside the same skill

## Host-specific notes (Debian 13, June 2026 onward)

- `youtube-transcript-api` is **not** installed system-wide (PEP 668 / externally-managed). `pip install` fails. But it installs cleanly in a uv venv — and that path is **more reliable than the yt-dlp fallback** because YouTube's subtitle endpoint frequently rate-limits (HTTP 429) when yt-dlp hits it.
- **Preferred path on this host — `uv` venv + `youtube-transcript-api`:**
  ```bash
  uv venv /tmp/ytvenv
  uv pip install --python /tmp/ytvenv/bin/python youtube-transcript-api
  /tmp/ytvenv/bin/python -c "
  from youtube_transcript_api import YouTubeTranscriptApi
  api = YouTubeTranscriptApi()
  t = api.fetch('VIDEO_ID', languages=['hi','en','bn'])
  print('GOT', t.language, t.language_code, len(list(t)), 'segments')
  "
  ```
  No YouTube API key needed. No Firefox cookies needed. No 429.
- `youtube-transcript-api` 1.2.x API shape:
  - `YouTubeTranscriptApi()` — instantiate with no args
  - `api.fetch(video_id, languages=[...])` returns a `FetchedTranscript` (iterable of `FetchedTranscriptSnippet`)
  - Each snippet has `.text`, `.start`, `.duration` attributes (NOT a dict)
  - The result object has `.language` (display name) and `.language_code` (ISO code) — always check what you got back
- **Fallback script `/root/.hermes/scripts/yt_transcript_fallback.py` is hit-or-miss** on this host. It tries `youtube-transcript-api` first (will fail because not installed), then falls back to `yt-dlp --cookies-from-browser firefox`. The yt-dlp path can succeed, but YouTube's `/youtubei/v1/.../subtitles` endpoint regularly returns **HTTP 429: Too Many Requests** even with valid cookies. Treat 429 as a transient retry-or-skip signal, not a hard error — pivot to the venv+uv path instead.
- The bundled `fetch_transcript.py` (under `scripts/`) works fine inside the venv — run with `/tmp/ytvenv/bin/python fetch_transcript.py URL` instead of `python3`.

## Non-English transcripts on English-titled videos (very common)

Indian education channels (UPSC, NEET, SSC, etc.) frequently upload videos with English titles but Hindi speech. In those cases:
- The video has **no English caption track** at all
- It has an auto-generated Hindi (or sometimes Tamil/Telugu) caption track
- The Hindi transcript is what you can fetch

**Workflow for non-English speech → user-language summary:**
1. Probe language list: `languages=['en', 'hi', 'bn', 'en-US', 'en-GB']` — `en` will raise `NoTranscriptFound`, but `hi` (auto-generated) will succeed
2. Capture the actual language from the result (`t.language_code`) and mention it in the summary header
3. Translate/summarize into the user's target language — for Bangla output from Hindi/English speech, write a fresh Bangla summary, do not literal-translate the transcript

This pattern matters for any user whose target language differs from the video's spoken language. Don't fail the task when the only available transcript is in a third language — pivot to translate-from-language-X.
