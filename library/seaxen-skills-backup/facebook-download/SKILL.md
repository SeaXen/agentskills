---
name: facebook-download
description: Use when the user pastes a Facebook link (video reel/watch/permalink/share/fb.watch) — download it and save into /mnt/tb/#Sea/fbdown with a clean, human-readable filename derived from the real post title. Videos work via the wrapper script + yt-dlp + Firefox cookies; photos are a known limitation of this toolchain.
---

# Facebook Download → /mnt/tb/#Sea/fbdown

## Trigger
User gives any URL containing one of:
`/share/v/`, `/share/r/`, `/reel/`, `/watch/`, `/video/`, `/permalink/`, `fb.watch`, `facebook.com`

## Destination
Always use the directory (quote it — `#` is a shell comment char):
`"/mnt/tb/#Sea/fbdown"`

## Method: use the wrapper script (PREFERRED)

The wrapper at `/root/.hermes/scripts/fb-dl.py` handles title extraction + sanitization + dedupe + auth + optional Telegram send. **Always prefer the wrapper over raw `yt-dlp`** for video downloads.

```bash
/root/.hermes/scripts/fb-dl.py "<URL>"               # single URL
/root/.hermes/scripts/fb-dl.py URL1 URL2 URL3        # batch
/root/.hermes/scripts/fb-dl.py --send "<URL>"        # download + Telegram send if ≤20MB
/root/.hermes/scripts/fb-dl.py --no-download "<URL>" # preview planned filename only
```

### Naming pattern (since 2026-08-19)

**Format:** `<clean readable title>.mp4` — no `facebook_` prefix, no ID in filename, no underscores in the title.

Example: `The Sugar Doctor's WARNING The ''Healthy'' Foods Quietly Destroying Your Body! - Dr David Unwin.mp4`

The wrapper:
1. Calls `yt-dlp --dump-json` (cookie-auth) to grab metadata.
2. Strips the engagement prefix from the title (`"78K views · 2K reactions | Real Title Here"` → `"Real Title Here"`).
3. Transliterates Bengali / Devanagari → Latin (diacritics stripped), so `কেন পড়তে ভালো লাগেনা` → `kena padate bhalo lagena`.
4. Replaces underscores with spaces.
5. Keeps only: letters, digits, spaces, `. , - ' " ! ?` — drops colons, slashes, brackets, emojis, URLs.
6. Collapses whitespace, caps at 120 chars at last word boundary.
7. Dedupes: if the target filename already exists, appends `-2`, `-3`, … ; if it already exists with same name and same size, `[SKIP-EXISTS]`.

### Photo (try yt-dlp first):
```bash
yt-dlp --no-warnings "<URL>" -o "/mnt/tb/#Sea/fbdown/facebook_<ID>.%(ext)s"
```
If yt-dlp fails, fall back to `web_extract` + `curl` to inspect page HTML for any direct `fbcdn.net`/`scontent` image URL. If nothing exposed, declare photo unsupported (see below).

## Steps (raw yt-dlp fallback, used inside the wrapper)

### 1. Resolve the real post ID
```bash
yt-dlp --no-warnings --simulate "<URL>" 2>&1 | head -20
```
Share-slug URLs (`/share/r/...`, `/share/v/...`) resolve to numeric IDs.

### 2. Download with cookie auth (Firefox profile `646ifort.default-esr`)
```bash
yt-dlp --no-warnings --cookies-from-browser firefox "<URL>" -o "<DEST_TEMPLATE>"
```
Public (no-cookie) downloads often fail with "Cannot parse data". **Always use cookies for FB.**

Chrome is NOT installed on this host — `firefox` is the only working browser for cookie auth.

## Photos are UNSUPPORTED here
yt-dlp returns `ERROR: Unsupported URL` for `/photo/` links (even with cookies).
`web_extract` returns empty. Raw HTML only contains JS bundles.
The `/photos/download/?fbid=` endpoint returns 9-byte junk.
=> Tell the user: photos require Graph API + access token, or save manually in a browser.

## Pitfalls (LESSONS FROM THIS SESSION)
- **User wants READABLE filenames, not technical-looking ones.** First version used `facebook_<ID>_<slugified_title>.mp4`; user rejected it. Second version dropped the prefix and replaced underscores with spaces — accepted. When in doubt, ask. Don't engineer cleverness the user doesn't want.
- **Probe before ruling out.** When the user asks "is X possible?" — run a real probe (~30s `yt-dlp --dump-json`, small test call, etc.) BEFORE saying "no". I told the user "FB doesn't expose titles" without testing; user pushed; `--dump-json` showed titles ARE available. Cost of probe << cost of confidently wrong answer. Trust the test, not the assumption.
- **Bengali sanitization gotcha.** Python `re` `\w` does NOT match Bengali vowel signs (া, ি, ী, …), so a naive `re.sub(r"[^\w]", "", title)` returns gibberish like `কন পডত ভল লগন`. Use `indic-transliteration` (`sanscript.transliterate(text, BENGALI, ISO)`) and then strip diacritics with `unicodedata.normalize("NFD", ...)` + `category(c) != "Mn"` filter.
- **Quote every path** containing `#Sea` — unquoted `#` breaks the command.
- **Cookie dependency:** All video downloads rely on Firefox cookie store. If user logs out of Facebook in Firefox or the profile rotates, downloads break. Note this when reporting failures.
- **Photos are unsupported** here — don't waste iterations trying the same dead-end approaches.
- **Don't trust prior-session file IDs** — resolve the real ID from the current URL (`--simulate` step) before checking/downloading. Context compaction can leave stale IDs in memory.
- **Telegram 20 MB ceiling** is for inline display only. Files >20 MB save to HDD fine; `MEDIA:` return of a 30 MB mp4 works. For genuine oversize files (>~50 MB), tell the user to share via cloud (Drive/Dropbox/WeTransfer).
- **yt-dlp path is `/usr/local/bin/yt-dlp`, not `/usr/bin/yt-dlp`.** The wrapper pins the absolute path to avoid PATH surprises.

## Reference files
- `references/fb-title-format.md` — what FB metadata actually looks like (engagement prefix, real title separator, sample dump from real URLs).
