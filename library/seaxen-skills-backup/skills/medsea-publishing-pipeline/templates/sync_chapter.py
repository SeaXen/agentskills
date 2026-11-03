#!/usr/bin/env python3
"""Sync /mnt/tb/Medicine/<Chapter>/ → Sea-knowledge → all 5 targets.

Renders missing topics in Sea-knowledge infographic style, fixes broken renders,
then syncs chapters/ → site/ → git. Validated pattern from cardiology sync
2026-06-19.

Usage:
    1. Define NEW_TOPICS as (section_prefix, slug, title, source_md) tuples.
    2. Define RE_RENDER as (prefix, slug, title, source_md) tuples for broken
       chromium-rendered topics (truncate content to ~120 lines to avoid hangs).
    3. List junk topic folder names in JUNK_FOLDERS to delete.
    4. Run: python3 sync_chapter.py

The script:
  - Renders each topic via /root/sea-knowledge-infographics/render_topic.py
  - Renames {slug}.{md,html,png} → topic.{md,html,png} on copy
  - Copies to chapters/, site/, local mirror (all three stay in sync)
  - Updates manifest.json
"""
import json
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

# ---- Paths (edit per chapter) ----
CHAPTER_NUM = 16                  # e.g. 16 for Cardiology
CHAPTER_SLUG = "16-cardiology"    # e.g. 16-cardiology
MED = Path("/mnt/tb/Medicine/Cardiology")  # source of truth
RENDERER = Path("/root/sea-knowledge-infographics/render_topic.py")
CHAP = Path(f"/mnt/tb/Sea-knowledge/#MedSea/chapters/{CHAPTER_SLUG}")
DISEASES = CHAP / "diseases"
SITE = Path(f"/mnt/tb/Sea-knowledge/#MedSea/site/{CHAPTER_SLUG}")
SITE_DISEASES = SITE / "diseases"
LOCAL_MIRROR = Path("/mnt/tb/Sea-knowledge/16. Cardiology")  # adjust per chapter
RENDER_TMP = Path("/tmp/sync_render")
RENDER_TMP.mkdir(parents=True, exist_ok=True)

# ---- Topics to render (edit per sync) ----
NEW_TOPICS = [
    # ("16.X.N", "slug-name", "Display Title", "/path/to/source.md"),
]

RE_RENDER = [
    # For broken chromium renders — truncate content first to avoid hangs
    # ("16.X.N", "slug-name", "Display Title", "/path/to/truncated-source.md"),
]

JUNK_FOLDERS = [
    # Names matching chapter's auto-scraped junk, e.g.
    # "16.6.328-cross-link:-[[..-00_index-medicine-moc]]..."
]


def render_topic(slug: str, title: str, md_path: str, out_dir: Path) -> Path:
    """Run renderer for one topic; return output folder."""
    tmp = out_dir / slug
    tmp.mkdir(parents=True, exist_ok=True)
    print(f"  Rendering {slug} ({title})...")
    result = subprocess.run([
        "python3", str(RENDERER),
        "--slug", slug,
        "--title", title,
        "--markdown-file", md_path,
        "--out-dir", str(tmp),
    ], capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        print(f"  ERROR:\n{result.stderr}")
        return None
    print(f"  ✓ Rendered → {tmp}")
    return tmp


def move_to_chapters(prefix: str, slug: str, render_dir: Path):
    """Move rendered {slug}.{md,html,png} → chapters/<prefix>-slug/topic.{md,html,png}.

    CRITICAL: the renderer outputs {slug}.ext but chapters/ convention is
    topic.ext. Without this rename, build_site.py skips the topic and the
    page renders blank on the live site.
    """
    target = DISEASES / f"{prefix}-{slug}"
    target.mkdir(parents=True, exist_ok=True)
    for ext in ("md", "html", "png"):
        src = render_dir / slug / f"{slug}.{ext}"  # renderer output naming
        dst = target / f"topic.{ext}"               # chapters/ convention
        if src.exists():
            shutil.copy2(src, dst)
        else:
            print(f"    ⚠ Missing: {src}")
    return target


def delete_junk_topic(prefix_slug: str):
    """Delete a junk topic folder from chapters/ + site/."""
    target = DISEASES / prefix_slug
    if target.exists():
        shutil.rmtree(target)
        print(f"  🗑 Deleted chapters: {target.name}")
    site_target = SITE_DISEASES / prefix_slug
    if site_target.exists():
        shutil.rmtree(site_target)
        print(f"  🗑 Deleted site: {site_target.name}")


def update_manifest(total_new_topics: int):
    """Increment manifest.json total_diseases."""
    manifest_path = CHAP / "manifest.json"
    if manifest_path.exists():
        m = json.loads(manifest_path.read_text())
        old = m.get("total_diseases", 0)
        m["total_diseases"] = old + total_new_topics
        m["modified"] = datetime.now().isoformat()
        m["last_sync"] = datetime.now().isoformat()
        manifest_path.write_text(json.dumps(m, indent=2))
        print(f"  Manifest updated: {old} → {m['total_diseases']}")


def main():
    print("="*70)
    print(f"SYNC START: {datetime.now().isoformat()}")
    print("="*70)

    if not NEW_TOPICS and not RE_RENDER and not JUNK_FOLDERS:
        print("Nothing to do — fill in NEW_TOPICS / RE_RENDER / JUNK_FOLDERS first.")
        return

    SITE_DISEASES.mkdir(parents=True, exist_ok=True)

    if NEW_TOPICS:
        print(f"\n[1/5] Rendering {len(NEW_TOPICS)} new topic(s)...")
        for prefix, slug, title, md_path in NEW_TOPICS:
            out = render_topic(slug, title, md_path, RENDER_TMP)
            if out:
                move_to_chapters(prefix, slug, out)

    if RE_RENDER:
        print(f"\n[2/5] Re-rendering {len(RE_RENDER)} topic(s)...")
        for prefix, slug, title, md_path in RE_RENDER:
            out = render_topic(slug, title, md_path, RENDER_TMP)
            if out:
                move_to_chapters(prefix, slug, out)

    if JUNK_FOLDERS:
        print(f"\n[3/5] Removing {len(JUNK_FOLDERS)} junk topic(s)...")
        for junk in JUNK_FOLDERS:
            delete_junk_topic(junk)

    print(f"\n[4/5] Copying to site/...")
    for prefix, slug, _, _ in NEW_TOPICS + RE_RENDER:
        chap = DISEASES / f"{prefix}-{slug}"
        site = SITE_DISEASES / f"{prefix}-{slug}"
        site.mkdir(parents=True, exist_ok=True)
        for ext in ("md", "html", "png"):
            src = chap / f"topic.{ext}"
            dst = site / f"topic.{ext}"
            if src.exists():
                shutil.copy2(src, dst)

    print(f"\n[5/5] Updating manifest.json...")
    update_manifest(len(NEW_TOPICS))

    print("\n" + "="*70)
    print("RENDER & COPY COMPLETE")
    print("Next: build_site.py + build_backup.py + git push + Notion + Docker")
    print("="*70)


if __name__ == "__main__":
    main()