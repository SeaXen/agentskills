#!/usr/bin/env python3
"""
MedSea chapter build pipeline — TEMPLATE.

Use this as a starting point for building a new Davidson chapter.
Adjust CHAPTERS list, source paths, and slug mapping for your specific chapter.

Validated: Ch 10-15 build 2026-06-19, 182/182 topics.
"""
import os, sys, re, json, shutil, subprocess
from pathlib import Path

# ===== CONFIGURATION =====
REPO = Path("/mnt/tb/Sea-knowledge")
MEDSEA = REPO / "#MedSea"
MEDICINE = Path("/mnt/tb/Medicine")
RENDERER = "/root/sea-knowledge-infographics/render_topic.py"
RENDER_OUT = Path("/tmp/sk_render")
RENDER_OUT.mkdir(exist_ok=True)

# (dav_num_25th_ed, slug, source_subdir_24th_ed, dav_title_25th_ed)
CHAPTERS = [
    # Add your chapter here
    # (10, "acute-medicine", "Acute Medicine and Critical Illness", "Acute medicine and critical illness"),
]


def preprocess_md(md_path):
    """Strip frontmatter, auto-number ## headers, return content + slug."""
    text = md_path.read_text(encoding="utf-8", errors="replace")
    # Strip YAML frontmatter
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:].lstrip()
    # Remove H1 (we'll add later)
    text = re.sub(r"^#\s+.+?\n", "", text, count=1).strip()

    # Auto-number ## sections
    counter = [0]

    def replacer(m):
        counter[0] += 1
        return f"## {counter[0]}. {m.group(1).strip()}"

    text = re.sub(r"^##\s+(?![\d.])(.+)$", replacer, text, flags=re.MULTILINE)

    # Slug
    slug = re.sub(r"[^a-z0-9]+", "-", md_path.stem.lower()).strip("-")
    return text, slug


def discover_chapter(src_dir):
    """Find all MD files in source dir, exclude MOC/Hierarchy."""
    if not src_dir.exists():
        return [], None
    files = sorted([f for f in src_dir.iterdir() if f.suffix == ".md"])
    moc = None
    topics = []
    for f in files:
        if "MOC" in f.name or "moc" in f.name.lower():
            moc = f
            continue
        if any(k in f.name for k in ("Hierarchy", "Roadmap", "Davidson")):
            continue
        if "Chapter" in f.name and "Davidson" in f.name:
            continue
        topics.append(f)
    return topics, moc


def group_into_hubs(topics):
    """Group topics by first number prefix (e.g., 1.1, 2.3 -> hub 1, hub 2)."""
    groups = {}
    for t in topics:
        m = re.match(r"^(\d+)\.\d+\s", t.name)
        if m:
            hub = int(m.group(1))
        else:
            hub = 1
        groups.setdefault(hub, []).append(t)
    return groups


def render_topic(md_text, slug, title, out_path, tag, truncate_to=None):
    """Run render_topic.py with optional truncation."""
    if truncate_to:
        lines = md_text.split("\n")
        if len(lines) > truncate_to:
            md_text = "\n".join(lines[:truncate_to])
            md_text += f"\n\n*...continued (truncated to {truncate_to} lines for renderer)*"
    tmp_md = RENDER_OUT / f"{slug}.md"
    tmp_md.write_text(md_text, encoding="utf-8")
    cmd = [
        "python3", RENDERER,
        "--slug", slug,
        "--title", title,
        "--markdown-file", str(tmp_md),
        "--out-dir", str(out_path.parent),
        "--tag", tag,
    ]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if r.returncode != 0:
            return False, r.stderr[:500]
        return True, "ok"
    except subprocess.TimeoutExpired:
        return False, "timeout"
    except Exception as e:
        return False, str(e)


def flatten_renderer_output(topic_dir, slug):
    """Move files from <topic_dir>/<slug>/ to <topic_dir>/."""
    nested = topic_dir / slug
    if not nested.exists():
        return False
    for src_file in nested.iterdir():
        if src_file.is_file():
            dest = topic_dir / src_file.name
            if src_file.suffix == ".png":
                dest = topic_dir / "topic.png"
            elif src_file.suffix in (".html", ".md"):
                dest = topic_dir / f"topic{src_file.suffix}"
            shutil.move(str(src_file), str(dest))
    shutil.rmtree(nested)
    return True


def build_chapter(dav_num, slug, src_subdir, dav_title):
    """Build one chapter end-to-end."""
    print(f"\n{'='*60}\nCh {dav_num}: {dav_title}\n{'='*60}")
    src_dir = MEDICINE / src_subdir
    topics, moc = discover_chapter(src_dir)
    print(f"  Found {len(topics)} topic MDs")
    if not topics:
        return {"dav_num": dav_num, "slug": slug, "n_topics": 0, "n_ok": 0, "n_failed": 0}

    hubs = group_into_hubs(topics)
    print(f"  Hubs: {len(hubs)}")

    # Output dirs (both local and MedSea)
    chap_local = REPO / f"{dav_num}. {dav_title}"
    chap_medsea = MEDSEA / "chapters" / slug
    for d in [chap_local, chap_medsea]:
        (d / "diseases").mkdir(parents=True, exist_ok=True)

    ok = failed = skipped = 0
    for hub_num, hub_topics in sorted(hubs.items()):
        for idx, topic_path in enumerate(hub_topics, 1):
            local_prefix = f"{dav_num}.{hub_num}.{idx:02d}"
            slug_topic = re.sub(r"[^a-z0-9]+", "-", topic_path.stem.lower()).strip("-")
            topic_dir = chap_medsea / "diseases" / f"{local_prefix}-{slug_topic}"
            topic_dir.mkdir(exist_ok=True)

            # Skip if already rendered
            png = topic_dir / "topic.png"
            if png.exists() and png.stat().st_size > 50000:
                skipped += 1
                continue

            text, _ = preprocess_md(topic_path)
            title = topic_path.stem

            # First attempt
            ok_flag, err = render_topic(text, slug_topic, title, topic_dir, dav_title)
            if not ok_flag and "timeout" in err:
                # Retry with truncation
                ok_flag, err = render_topic(text, slug_topic, title, topic_dir, dav_title, truncate_to=120)

            if ok_flag:
                # Flatten nested output
                flatten_renderer_output(topic_dir, slug_topic)
                # Copy to local
                local_topic_dir = chap_local / "diseases" / f"{local_prefix}-{slug_topic}"
                local_topic_dir.mkdir(parents=True, exist_ok=True)
                for ext in ("png", "html", "md"):
                    src = topic_dir / f"topic.{ext}"
                    if src.exists():
                        shutil.copy2(src, local_topic_dir / f"topic.{ext}")
                ok += 1
                print(f"  OK  {local_prefix}", flush=True)
            else:
                failed += 1
                print(f"  FAIL {local_prefix}: {err[:100]}", flush=True)

    print(f"  Done: ok={ok}, fail={failed}, skip={skipped}")
    return {"dav_num": dav_num, "slug": slug, "n_topics": len(topics), "n_ok": ok, "n_failed": failed, "n_skipped": skipped}


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    results = []
    for dav_num, slug, src_subdir, dav_title in CHAPTERS:
        if only and str(dav_num) != only and slug != only:
            continue
        result = build_chapter(dav_num, slug, src_subdir, dav_title)
        results.append(result)

    print(f"\n{'='*60}\n=== ALL DONE ===\n{'='*60}")
    for r in results:
        print(f"  Ch {r['dav_num']}: {r['n_topics']} total, {r['n_ok']} ok, {r['n_failed']} fail, {r.get('n_skipped', 0)} skip")


if __name__ == "__main__":
    main()
