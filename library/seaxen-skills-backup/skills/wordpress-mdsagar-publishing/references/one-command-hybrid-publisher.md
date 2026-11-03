# One-command hybrid publisher notes

## Purpose
Use `~/.hermes/scripts/wp_mdsagar_hybrid_publish.py` when converting an existing medical Markdown source note into a WordPress post on `mdsagar.com` in one command.

## Current default behavior
- Hard default style: `exam-hybrid`
- This default exists because the user wants posts that remain professional and public-facing **but closer to the FCPS/MRCP medicine-folder notes** rather than generic blog rewrites.

## What `exam-hybrid` should preserve
Compared with `public-hybrid`, `exam-hybrid` should keep more of the source-note feel, especially for nephrology topics like AKI and CKD:
- Interpretation Frameworks
- Differential Diagnosis
- stronger high-yield clinical framing
- FCPS/MRCP callout boxes such as Exam Pearls, Viva Traps, Red Flags, and Practical Clinical Approach

## When to use which mode
- `exam-hybrid`: default for this user; best for nephrology and other medicine-folder topics where the site post should still feel useful for FCPS/MRCP revision
- `public-hybrid`: only when the user explicitly wants a lighter, more general-reader-facing version

## Example commands
### New CKD post
```bash
python3 ~/.hermes/scripts/wp_mdsagar_hybrid_publish.py \
  --source-note /root/Desktop/tb/Medicine/Nephrology/CKD.md \
  --title 'Chronic Kidney Disease (CKD): Symptoms, Stages, Causes, Diagnosis, and Management' \
  --slug 'chronic-kidney-disease-ckd' \
  --category 'Medicine > Nephrology > CKD' \
  --status publish
```

### Update existing CKD post
```bash
python3 ~/.hermes/scripts/wp_mdsagar_hybrid_publish.py \
  --source-note /root/Desktop/tb/Medicine/Nephrology/CKD.md \
  --post-id 24 \
  --title 'Chronic Kidney Disease (CKD): Symptoms, Stages, Causes, Diagnosis, and Management' \
  --slug 'chronic-kidney-disease-ckd' \
  --category 'Medicine > Nephrology > CKD' \
  --status publish
```

### Dry run without auth
```bash
python3 ~/.hermes/scripts/wp_mdsagar_hybrid_publish.py \
  --source-note /root/Desktop/tb/Medicine/Nephrology/AKI.md \
  --dry-run
```

## Operational pitfall
Gateway interruptions or shell changes may clear `WP_BASE_URL`, `WP_USERNAME`, and `WP_APP_PASSWORD` from the current environment even if earlier live publish commands worked in the same chat session.

Implications:
- dry-run can still be used to generate/verify HTML and excerpt files
- live create/update requires the env vars to be restored first
- when blocked this way, report exactly that the local HTML is ready and specify the generated file paths so work is not lost

## Post-update verification pattern
After using the one-command publisher on `mdsagar.com`, verify in this order:
1. `python3 ~/.hermes/scripts/wp_mdsagar_poster.py get-post <POST_ID>`
2. browser check of the live URL to confirm the rendered headings/TOC
3. raw HTML fetch with a browser-like `User-Agent` to confirm expected strings such as:
   - `Interpretation Frameworks`
   - `Differential Diagnosis`
   - title tag / meta if needed

### Important quirk
`mdsagar.com` may return `403 Forbidden` to plain `urllib` requests without a browser-like `User-Agent`.

Use a check like:
```python
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8','replace')
```

## SEO/title verification pitfall
A browser snapshot title can appear stale even after the post content and heading have updated.

When that happens:
- do not assume the publish failed
- compare the live heading, raw HTML `<title>`, and Rank Math metadata separately
- on `mdsagar.com`, check the cache state header too: `x-litespeed-cache: hit` can mean the base URL is still serving an older cached `<title>`
- retry with a cache-busting query string such as `?cb=<timestamp>`; a `miss` response may already show the corrected title even while the base URL still shows the old one
- if needed, re-send Rank Math metadata through `/wp-json/rankmath/v1/updateMeta`
- if metadata is already correct but the cached base URL remains stale, a practical workaround is to toggle the post status `publish -> draft -> publish` with the same final title/content to invalidate the page cache
- then repeat the browser-like raw HTML check and browser snapshot
