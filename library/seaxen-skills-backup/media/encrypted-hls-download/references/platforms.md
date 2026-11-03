# Known encrypted-HLS platforms and their infrastructure

When the user pastes a new LMS URL, check whether their video player uses one of the hostnames below. If yes, this skill's recipe applies with minimal changes — just swap the LMS URL and credentials.

## Synapse Medical Academy (verified 2026-06-18)

| Layer | Host | Notes |
|---|---|---|
| LMS frontend | `lms.synapsepg.org` | React app, session in `localStorage.sessionId` (express-session token, used as `Authorization: s%3A...` Bearer on the API). Real cookies are NOT set. |
| LMS API | `api.synapsepg.org` | `POST /api/student/login` returns a session token used as Bearer. |
| Static assets | `assets.synapsepg.org` | Course thumbnails, profile pictures. |
| Video player iframe | `player.vidinfra.com/stream/{content_id}/default/{stream_id}` | Embed via `<iframe title="Video Player">`. No auth headers in the iframe URL itself — the player JS calls `kms.vidinfra.com` with signed headers. |
| Key server | `kms.vidinfra.com/v1/keys?content_id={stream_id}` | Requires `x-auth-nonce` (random), `x-auth-timestamp` (unix), `x-auth-signature` (HMAC-SHA256). Returns 16 raw bytes (the AES-128 key). **Without signed headers returns `missing authentication headers`.** |
| CDN | `jrgtfb2pnx.tenbytecdn.com/{stream_id}/{quality}/...` | Public — only needs `Referer: https://player.vidinfra.com/` and a real browser User-Agent. Returns 720p / 480p media playlists and 4-second `.ts` segments. |
| RUM | `rumito.tenbyte.io` | Real-user-monitoring; ignore. |
| Player JS | `player.vidinfra.com/stream/public/js/index.global.js` (1 MB minified) | Contains the signing logic but it's minified; reverse-engineering is slower than just letting the browser do it. |

**Course structure hint:** `GET /api/lecture/{lecture_id}` returns the chapter; the chapter has `videoContents` which are the per-video content IDs. `allLectures` in `localStorage` lists every chapter + their `videoContents` arrays — a single page contains the whole course's video index.

**Detection shortcut:** if the user mentions "Synapse", "FCPS P-I", "Davidson", or "Bangladesh medical course", assume this stack.

## How to fingerprint an unknown platform

If the LMS URL is unfamiliar, do these in order before assuming this skill applies:

1. Log in via Playwright, click the video, capture network requests.
2. Look for `kms.*` / `keys?content_id=` in the request URLs.
3. Look for `*tenbytecdn*` / `*cloudfront*` / `*akamaized*` in the segment URLs.
4. Look for the key response — if it's 16 bytes binary with no JSON wrapper, it's AES-128 raw. If it's JSON with a `kid` or `keyId` field, it's CENC/Widevine — different problem.
5. If the manifest has `METHOD=SAMPLE-AES` (not `METHOD=AES-128`), the segments themselves are DRM-encrypted; this skill does not apply.

## Why this class of platforms exists

Bangladesh / South Asia coaching-industry LMSes (medical, engineering, BCS, university prep) overwhelmingly use the same 2-3 white-label HLS stacks: `vidinfra.com` (Bangladesh-based), `moxion.io` (Indian), or `mux.com`. They all bolt onto the LMS with a similar pattern: iframe embed + signed key requests. When a user reports "I can't download a course video", one of these three stacks is involved 80%+ of the time. The recipes are nearly identical — only the hostnames change.
