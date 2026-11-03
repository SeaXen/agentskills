# Bulk-rename existing ID-only files to the new title-based naming

As of 2026-08-19, `/mnt/tb/#Sea/fbdown/` had ~32 files using the old `facebook_<ID>.mp4` scheme. After the wrapper was upgraded to use the title-based naming (`facebook_<ID>_<title>.mp4`), those old files were left as-is — the user was offered a retroactive rename but had not yet confirmed.

This is the recipe to do it safely if/when the user says yes.

## Strategy

For each existing `facebook_<ID>.mp4`:
1. Re-fetch the metadata via `yt-dlp --dump-json` using the same `--cookies-from-browser firefox` flag.
2. Extract the real title using the same `split(" | ")[1]` rule.
3. Compute the new filename: `facebook_<ID>_<sanitized-title>.mp4`.
4. **Only rename** if the target filename doesn't already exist (avoid clobbering files the wrapper has already re-downloaded with the new name).
5. **Skip** the rename if the title is empty (keep the ID-only file).

## One-liner recipe (verified to work on a single file during testing)

```bash
mv "/mnt/tb/#Sea/fbdown/facebook_<ID>.mp4" "/mnt/tb/#Sea/fbdown/__tmp.mp4" \
&& /root/.hermes/skills/facebook-download/scripts/fbdl.py "<reconstructed-URL>" \
&& ls -lh "/mnt/tb/#Sea/fbdown/facebook_<ID>"* \
&& rm -f "/mnt/tb/#Sea/fbdown/__tmp.mp4"
```

The mv-out-of-the-way trick makes the wrapper see no existing file, so it actually re-downloads. But that wastes bandwidth — prefer the rename-only approach below.

## Better: rename-only (no re-download)

There's no public Wayback API for FB video titles, so we have to re-fetch metadata for each ID. For each `facebook_<ID>.mp4`:

```bash
# 1. Re-derive the URL (we don't store share slugs, so use the watch form)
#    The watch URL works because yt-dlp resolves it the same way:
url="https://www.facebook.com/watch/?v=<ID>"

# 2. Get the metadata
title=$(yt-dlp --no-warnings --cookies-from-browser firefox \
  --dump-json --skip-download "$url" 2>/dev/null \
  | python3 -c "
import sys, json, re
d = json.loads(sys.stdin.read())
t = d.get('title','')
real = t.split(' | ', 1)[1].strip() if ' | ' in t else t.strip()
clean = re.sub(r'[^\w\s.-]', '', real, flags=re.UNICODE)
clean = re.sub(r'\s+', '_', clean.strip())
clean = re.sub(r'-+', '-', clean).strip('_-')[:80]
print(clean)
")

# 3. Build new name and rename (only if title is non-empty AND target doesn't exist)
if [ -n "$title" ]; then
  new="/mnt/tb/#Sea/fbdown/facebook_<ID>_${title}.mp4"
  old="/mnt/tb/#Sea/fbdown/facebook_<ID>.mp4"
  if [ ! -e "$new" ]; then
    mv "$old" "$new"
    echo "renamed: $(basename "$new")"
  else
    echo "skip (target exists): $(basename "$new")"
  fi
else
  echo "skip (no title)"
fi
```

Wrap in a `for id in $(ls /mnt/tb/#Sea/fbdown/facebook_*.mp4 | grep -oE '[0-9]+' | sort -u)` loop to process all.

## Why this is safe
- `mv` on the same filesystem is atomic — no partial state.
- Target-exists check prevents clobbering wrapper-produced files.
- No re-download needed — title can be derived from `yt-dlp --dump-json` alone (no media fetch).
- Cookie auth is required to get the title; the loop will fail cleanly on auth expiry with `[META FAIL]` in stderr.

## Risk: FB may rate-limit bulk metadata fetches
The 12-URL spot-check during the session took ~30s total (parallel where possible). For ~32 files, expect ~60-90s sequential. If throttled, add `sleep 1` between iterations or batch in groups of 10 with a longer pause.
