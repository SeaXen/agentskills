# Synapse LMS — API & Architecture Notes

## Base URLs (Synapse Medical Academy)

| Service | URL | Notes |
|---|---|---|
| LMS frontend | `https://lms.synapsepg.org` | React SPA, Ant Design UI |
| API backend | `https://api.synapsepg.org` | Node/Express, all `/api/*` |
| Static assets CDN | `https://assets.synapsepg.org` | S3-backed, public files |
| Profile pictures | `https://assets.synapsepg.org/directory/<phone>.jpeg` | Pattern: 880 + mobile |
| Video player iframe | `https://player.vidinfra.com/stream/{content_id}/default/{stream_id}` | Vidinfra player |
| HLS CDN | `https://<random>.tenbytecdn.com/{stream_id}/{quality}/media.m3u8` | Random subdomain per stream |
| KMS (AES key) | `https://kms.vidinfra.com/v1/keys?content_id={stream_id}` | Signed request required |
| Telemetry (Cloudflare) | `https://player.vidinfra.com/cdn-cgi/rum?` | Ignore, noise |
| Telemetry (Tenbyte) | `https://rumito.tenbyte.io/dist/rum.v1.0.0.min.js` | Ignore, noise |

## Authentication

**Type:** Session token (express-session) stored in **localStorage**, NOT cookies.

```js
// After login:
localStorage.sessionId  // = "\"s%3A<sig>.<hmac>\""  (URL-encoded, double-quoted)
localStorage.student    // = JSON of student profile
localStorage.allLectures  // = JSON array of all chapters
```

The token is used as a Bearer token in the `Authorization` header:

```http
GET /api/lecture/{id} HTTP/1.1
Host: api.synapsepg.org
Authorization: "s%3A<sig>.<hmac>"
Referer: https://lms.synapsepg.org/notes/{id}/lecture
Agent: browser               ← REQUIRED — see warning below
```

### ⚠ The `Agent: browser` custom header (CRITICAL)

The React frontend sends a **custom `Agent: browser` header on every API request** — this is the server's fingerprint signal that the request came from the actual LMS web app, not a third-party client. Without it:

- Server returns **HTTP 500** (not 401, not 403 — generic server-side error)
- Sometimes returns 200 but with the React app's index.html body instead of JSON

**Every API call must include `Agent: browser`** when invoked from outside the browser. This is easy to miss because:
1. It's not in standard auth docs
2. The error response is a generic 500, not "missing header"
3. Only the `page.on('request')` event listener (with full headers) shows the React app sending it

Captured from browser request headers (2026-06-22):
```
authorization: "s%3A50vR_RgvacMhqqkja5h4KBheSLOonxPZ.avjT9qXYlzq7SIKq58AmuDBTkfvTICwS85TPeX1LKfc"
referer: https://lms.synapsepg.org/
agent: browser                ← THE SIGNAL HEADER
sec-ch-ua: "Chromium";v="148", "HeadlessChrome";v="148", ...
accept: application/json, text/plain, */*
```

**The best way to call the API** is `page.request.get(url, headers={"Agent": "browser"})` — Playwright's request context runs in the same browser context, so it auto-includes the auth header and you only need to add `Agent`. Don't waste time trying curl / Python `requests` from outside the browser — even with the right Authorization + cookies, you'll hit CORS or 500 without that header.

## API endpoints (discovered 2026-06)

| Method | Path | Purpose |
|---|---|---|
| POST | `/api/student/login` | Login (json: `{"username": "...", "password": "..."}`) |
| GET | `/api/student/profile` | Current student info |
| GET | `/api/lecture/{id}` | Single chapter data (videos + files) |
| GET | `/api/course/{course_id}/subject-completion` | Course progress |
| GET | `/api/exam/has-instant-practice` | Exam availability |
| GET | `/api/group/{group_id}` | Group/chat info |

## Lecture API response shape

```json
{
  "status": "200",
  "data": {
    "_id": "6a251ab2585213c2b6778499",
    "name": "Davidson's Notes",
    "videoContents": [],
    "fileContents": [
      {
        "_id": "6a33c313c488c1c2bf67bdae",
        "title": "Gastroenterology Class PDF by Dr. Rafsan",
        "type": "file",
        "key": "directory/775210851440.pdf",
        "isVOD": false,
        "isAvailable": false,
        "isPublished": false,
        "duration": 0,
        "courses": ["69b0f4b98d2df1d11e89f0bf"],
        "lectures": ["6a251ab2585213c2b6778499"],
        "subjects": ["69b13d1d8d2df1d11e89fb47"]
      }
    ]
  }
}
```

## URL patterns

| Page | URL | Content |
|---|---|---|
| Lecture videos | `/videos/{chapter_id}/lecture` | Video tiles (1+ per chapter) |
| Lecture notes | `/notes/{chapter_id}/lecture` | File tiles (DOWNLOAD buttons) |
| Course list | `/courses` | All enrolled courses |
| Exam list | `/exams` | All exams |
| Dashboard | `/` | Course cards |

## React DOM structure (for clicking)

```html
<section class="ant-layout">
  <main class="ant-layout-content custom-container section-padding sec-mh">
    <div class="ant-row" style="...">
      <div class="ant-col ant-col-xs-24 ant-col-md-8">
        <div class="student-video-card-wrap">  <!-- decorative wrapper -->
          <div class="ant-card ant-card-bordered ant-card-hoverable student-video-card">
            <div class="ant-card-body">
              <h5>Video Title Here</h5>
              <p>0%</p>  <!-- progress -->
            </div>
          </div>
        </div>
      </div>
      <!-- ... more cards ... -->
    </div>
  </main>
</section>
```

**Click the `.student-video-card` (inner) — not the wrapper.**

For notes:
```html
<button class="ant-btn ...">DOWNLOAD</button>  <!-- one per file -->
```

## Performance numbers (Synapse, 2h 720p lecture)

| Step | Time |
|---|---|
| Playwright login | ~5s |
| Navigate to lecture, click tile, wait for player | ~10s |
| Fetch m3u8, list segments | <1s |
| Download 1892 segments @ 24 threads | ~30s |
| Decrypt + write 834 MB | ~20s |
| Remux to MP4 | ~3s |
| **Total** | ~70s |

## File size expectations (Synapse, 720p H.264 ~924 kbps)

- 1 hour ≈ 415 MB raw, 400 MB after MP4 remux
- 2 hours ≈ 834 MB raw, 766 MB after remux
- Typical PDF: 1–30 MB (lecture slides with images)
