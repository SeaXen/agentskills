---
name: drbeen-lecture-download
description: Download drbeen.com course lectures (Vimeo embed-only) for paid accounts. Covers login (connect.sid), catalog scrape from /courses, lecture URLs under /learn/{slug}/{id}, yt-dlp with embedding page URL + cookies, 1080p MP4 to /mnt/tb/drbeen/{course-slug}/, resume + thermal pacing. Never store passwords in skills or memory — use accounts/*.creds. Use when user asks to download DrBeen videos offline.
version: 1.0.0
metadata:
  hermes:
    tags: [drbeen, vimeo, medical, download, lms, yt-dlp]
---

# DrBeen lecture download

Offline download for **https://www.drbeen.com/** (Heroku/Express, session cookie `connect.sid`, video host **Vimeo**).

## When to use

- User has a **paid** DrBeen account and wants course videos under `/mnt/tb/drbeen/` (or custom base).
- User mentions drbeen.com, DrBeen courses, or continuing a pilot (e.g. Pain Management).

**Not Synapse:** Synapse is `lms.synapsepg.org` + Vidinfra HLS → skill `synapse-lms-download`.

## Architecture (verified 2026-06)

| Piece | Detail |
|-------|--------|
| Login page | `GET https://www.drbeen.com/signin` |
| Login POST | `POST https://www.drbeen.com/login` body: `username` (email), `password` |
| Session | Cookie `connect.sid` (domain `.drbeen.com` or `www.drbeen.com`) |
| Catalog (auth) | `GET https://www.drbeen.com/courses` — HTML lists `/courses/{slug}/{courseId}` |
| Course page | `GET https://www.drbeen.com/courses/{slug}/{courseId}` — links to lectures |
| Lecture page | `GET https://www.drbeen.com/learn/{lecture-slug}/{lectureId}?topic=...` |
| Player | iframe `https://player.vimeo.com/video/{numericId}` (also in HTML) |
| Paid flag | Inline `dataLayer`: `loggedIn: true`, `paid: true` when entitled |

## Critical download rule (Vimeo)

Vimeo on DrBeen is **embed-only**. **Do not** pass `https://player.vimeo.com/video/ID` to yt-dlp.

**Pass the lecture page URL:**

```text
https://www.drbeen.com/learn/{slug}/{lectureId}
```

yt-dlp discovers Vimeo from the page. Add:

- `--cookies` Netscape cookie file (must start with `# Netscape HTTP Cookie File`)
- `--referer https://www.drbeen.com/`

Quality: `-S res:1080,ext:mp4:m4a` `--merge-output-format mp4`

## Credentials (never in SKILL, memory, or chat logs)

```bash
mkdir -p ~/.hermes/secrets/drbeen-accounts
printf '%s' 'PASSWORD_ONLY' > ~/.hermes/secrets/drbeen-accounts/default.creds
chmod 600 ~/.hermes/secrets/drbeen-accounts/default.creds
# Email/username: pass as env DRBEEN_EMAIL or first line of accounts/default.json
```

Scripts read `DRBEEN_EMAIL` + password from `DRBEEN_PASSWORD` or `~/.hermes/secrets/drbeen-accounts/<account>.creds`.

**Rotate** any password ever pasted in Discord/Telegram.

## Output layout

```text
/mnt/tb/drbeen/
  pain-management/
    01 - Lecture Title.mp4
    ...
    _lectures.json    # cached paths, vimeo_id, titles
  cardiovascular-system/
    ...
```

Folder name = course **slug** from URL (e.g. `pain-management`).

## Scripts (this skill)

```bash
/root/.hermes/skills/devops/drbeen-lecture-download/scripts/setup.sh   # once: ensure yt-dlp, ffmpeg
/root/.hermes/skills/devops/drbeen-lecture-download/scripts/auth.py <account>
/root/.hermes/skills/devops/drbeen-lecture-download/scripts/download_course.py <account> <course_slug> <course_id>
```

Env pacing (laptop thermals):

- `SLEEP=45` — seconds between lectures
- `COOLDOWN_EVERY=4` — long pause every N lectures
- `LONG_COOLDOWN=120`

## Workflow summary

1. **Auth** → write `/tmp/drbeen_cookies.txt` (Netscape) or account-specific path under secrets dir.
2. **List courses** — parse `/courses` HTML for `href="/courses/{slug}/{id}"`.
3. **Per course** — parse `/learn/...` links from course HTML.
4. **Per lecture** — optional: fetch page once, regex `player\.vimeo\.com/video/(\d+)`, save `_lectures.json`.
5. **Download** — yt-dlp with **lecture URL**, skip if `.mp4` exists and size > 1MB.
6. **Verify** — `ffprobe` → `h264`, `1920x1080`, `format_name` contains `mp4`.

## Pitfalls

1. **Cookie file without Netscape header** → yt-dlp auth fails; first line must be `# Netscape HTTP Cookie File`.
2. **Direct Vimeo URL** → `Cannot download embed-only video without embedding URL`.
3. **`/tmp` scripts vanish** on reboot/tmpfs cleanup — use skill `scripts/` under `/root/.hermes/skills/...`.
4. **Session expiry** — refresh via `auth.py` mid-batch (pilot recovered lecture 15 after refresh).
5. **Filename length** — very long titles can hit 255-byte limits; truncate sanitize to ~180 chars.
6. **Scope** — ~30 enrolled courses, ~1279 lectures, ~350 GB @ 1080p; batch takes days with thermal sleeps.

## Worked example (pilot)

- Course: Pain Management — slug `pain-management`, id `rJbH_8FNp`
- 17 lectures, 4.7 GB, all 1080p h264+aac MP4
- Path: `/mnt/tb/drbeen/pain-management/`

## Related

- `synapse-lms-download` — different site, HLS/AES, no Vimeo.