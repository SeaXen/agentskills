#!/usr/bin/env python3
"""
Restore the full desktop topic-SPA JS block in every chapter HTML.

The mobile-section strip that turns 17MB chapter HTMLs into ~200KB ones can
inadvertently remove the desktop JS that loads topics.json + handles topic
clicks. This script re-injects the full block with per-chapter parameterization
(slug, manifest URL, image path).

Usage:
    1. Save the full template to /tmp/desktop_js_full.html (or any path)
    2. Edit CHAPTER_SLUG_PLACEHOLDER, MANIFEST_URL_PLACEHOLDER, IMG_PATH_PLACEHOLDER
       to match the values used in your template
    3. Update SITE_ROOT below
    4. python3 fix_all_chapter_js.py

The script will:
- Skip chapters that already have the full block
- Replace the truncated block with the full template
- Per-file parameterize slug + paths
- Print byte-delta per file (truncation shows as suspiciously small growth)
- Raise SystemExit before any file write if template sanity check fails
"""
import os
import re
import sys

# 1. Where the full JS template lives on disk
TEMPLATE_PATH = "/tmp/desktop_js_full.html"

# 2. What to find/replace inside the template (the chapter's slug & paths)
CHAPTER_SLUG_PLACEHOLDER = 'CHAPTER_SLUG = "16-cardiology"'
MANIFEST_URL_PLACEHOLDER = '"/16-cardiology/topics.json"'
IMG_PATH_PLACEHOLDER = '"/16-cardiology/${t.png}"'
CRUMB_LINK_PLACEHOLDER = '"/16-cardiology/"'
CHAPTER_NAME_PLACEHOLDER = '<a href="/16-cardiology/">Cardiology</a>'

# 3. Where the chapter pages live
SITE_ROOT = "/mnt/tb/Sea-knowledge/#MedSea/site"

# 4. Regex that captures the slug from a truncated block in any chapter.
#    Matches "<script>\nconst CHAPTER_SLUG = "X-Y"; ... <script src=mermaid
#    non-greedily, so the truncate point doesn't matter.
TRUNCATED_BLOCK_RE = re.compile(
    r'<script>\s*\nconst CHAPTER_SLUG = "([^"]+)";.*?(?=<script src="https://cdn\.jsdelivr\.net)',
    re.DOTALL
)

# 5. The function name that MUST appear at the end of the full template.
#    Used as a sanity check that the template file was not itself truncated.
SANITY_GREP = "function showTopic"


def main():
    if not os.path.exists(TEMPLATE_PATH):
        sys.exit(f"FATAL: template not found at {TEMPLATE_PATH}")

    with open(TEMPLATE_PATH) as f:
        full_template = f.read()

    if SANITY_GREP not in full_template:
        sys.exit(f"FATAL: template at {TEMPLATE_PATH} is missing '{SANITY_GREP}' — refusing to write truncated JS to all chapters")

    if not os.path.isdir(SITE_ROOT):
        sys.exit(f"FATAL: SITE_ROOT not found: {SITE_ROOT}")

    fixed = 0
    skipped = 0
    for d in sorted(os.listdir(SITE_ROOT)):
        p = os.path.join(SITE_ROOT, d, "index.html")
        if not os.path.isfile(p) or d in ("exam", "flashcards"):
            continue

        with open(p) as f:
            html = f.read()

        m = TRUNCATED_BLOCK_RE.search(html)
        if not m:
            skipped += 1
            continue

        chapter_slug = m.group(1)
        chapter_name = chapter_slug.split("-", 1)[1].replace("-", " ").title() if "-" in chapter_slug else chapter_slug

        replacement = (full_template
            .replace(CHAPTER_SLUG_PLACEHOLDER, f'CHAPTER_SLUG = "{chapter_slug}"')
            .replace(MANIFEST_URL_PLACEHOLDER, f'"/{chapter_slug}/topics.json"')
            .replace(IMG_PATH_PLACEHOLDER, f'"/{chapter_slug}/${{t.png}}"')
            .replace(CRUMB_LINK_PLACEHOLDER, f'"/{chapter_slug}/"')
            .replace(CHAPTER_NAME_PLACEHOLDER, f'<a href="/{chapter_slug}/">{chapter_name}</a>'))

        # Re-verify after substitution
        if SANITY_GREP not in replacement:
            sys.exit(f"FATAL: replacement for {chapter_slug} lost '{SANITY_GREP}' — template substitution broke something")

        new_html = html[:m.start()] + replacement + html[m.end():]
        with open(p, "w") as f:
            f.write(new_html)
        fixed += 1
        delta = len(new_html) - len(html)
        print(f"✓ {chapter_slug}: {len(html):>7} → {len(new_html):>7} bytes (+{delta})")

    print(f"\n=== Fixed {fixed} chapter pages, skipped {skipped} (no truncated block found) ===")


if __name__ == "__main__":
    main()
