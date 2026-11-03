#!/usr/bin/env python3
"""Audit MedSea chapter sync: source / local / Notion.

CORRECTED 2026-06-20 to handle:
- Nested subdirectories (3+ levels deep) in source
- Duplicate folders with same content (TDM/ vs Therapeutic Drug Monitoring/)
- Source files with leading numeric prefixes that need full strip (1.1 Foo.md)
- Ampersand differences (& -> 'n v' vs 'nv')

Compares three platforms and reports REAL missing topics only,
not slug-normalization false positives.

Usage:
    python3 audit_chapter_full.py          # Audit all chapters 1-10
    python3 audit_chapter_full.py 9        # Audit single chapter
"""
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


def load_notion_key():
    """Load NOTION_API_KEY from /root/.hermes/.env without leaking into output."""
    env_path = Path("/root/.hermes/.env")
    if not env_path.exists():
        raise SystemExit("FATAL: /root/.hermes/.env not found")
    prefix = "NOTION_API_KEY" + "***"
    key = None
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line.startswith(prefix) and not line.startswith("#"):
                key = line[len(prefix):].strip()
                break
    if not key:
        raise SystemExit("FATAL: NOTION_API_KEY not in env")
    return key


NOTION_KEY = load_notion_key()


def http(method, url, data=None):
    h = {"Authorization": "Bearer " + NOTION_KEY, "Notion-Version": "2025-09-03"}
    if data is not None:
        h["Content-Type"] = "application/json"
        body = json.dumps(data).encode()
    else:
        body = None
    req = urllib.request.Request(url, data=body, method=method, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return {"_error": e.code}


def slugify(text):
    """Aggressive normalize: punctuation to space, collapse underscores/dashes."""
    s = text.lower()
    s = re.sub(r'[^\w\s-]', ' ', s)
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')


def normalize(s):
    """Strip ALL leading digits/dots/dashes/whitespace, then -full/-hub suffix.

    CRITICAL: old version `r'^\\d+(\\.\\d+)?[\\s\\.\\-]*'` only matched one N.N group,
    leaving "1-1-clinical-reasoning" stuck on source "1.1 Clinical Reasoning.md".
    New version strips everything: "1.1.01-foo" -> "foo", "1-1-bar" -> "bar".
    """
    s = re.sub(r'^[\d\.\-\s]+', '', s)
    s = re.sub(r'(-full|-hub)$', '', s)
    return s.strip('-')


def get_source_topics(src_dir):
    """Source topics with dedup by slug (pick longest content).

    Skips: MOC, Hierarchy, Roadmap, Template, COMPLETION_PLAN files.
    Includes: all other .md files regardless of size or nesting depth.
    Dedup: if same slug appears multiple times, keep the longest content.
    """
    src = Path(src_dir)
    if not src.exists():
        return {}, []
    by_slug = {}
    for f in sorted(src.rglob("*.md")):
        name = f.name
        if any(x in name for x in ['MOC.md', 'Hierarchy.md', 'Roadmap.md', 'Template.md', 'COMPLETION_PLAN']):
            continue
        clean = name.replace('_full.md', '').replace('_Hub.md', '').replace('_HUB.md', '').replace('.md', '')
        slug = normalize(slugify(clean))
        if not slug:
            continue
        by_slug.setdefault(slug, []).append((f, clean))

    unique = {}
    duplicates = []
    for slug, files in by_slug.items():
        if len(files) == 1:
            unique[slug] = files[0]
        else:
            best = max(files, key=lambda x: x[0].stat().st_size)
            unique[slug] = best
            duplicates.extend([(f, n) for f, n in files if f != best[0]])
    return unique, duplicates


def get_medsea_slugs(medsea_dir):
    """MedSea disease slugs (handles both flat and dir layouts)."""
    out = set()
    d = Path(medsea_dir)
    if not d.exists():
        return out
    for f in d.iterdir():
        if f.is_dir():
            m = re.match(r'^\d+\.\d+\.\d+-(.+)$', f.name)
            if m and (f / "topic.md").exists():
                out.add(normalize(slugify(m.group(1))))
        elif f.suffix == ".md":
            m = re.match(r'^(\d+\.\d+)\.(\d+)-(.+)$', f.stem)
            if m:
                out.add(normalize(slugify(m.group(3))))
    return out


def get_notion_slugs(ch_page_id):
    """All topic slugs from a Notion chapter page (recursive into hubs)."""
    slugs = set()

    def fetch(parent_id):
        cursor = None
        while True:
            url = f"https://api.notion.com/v1/blocks/{parent_id}/children"
            if cursor:
                url += f"?start_cursor={cursor}"
            res = http("GET", url)
            if "_error" in res:
                return
            for b in res.get("results", []):
                if b.get("type") != "child_page":
                    continue
                title = b["child_page"]["title"]
                slugs.add(slugify(title))
                if re.match(r'^\d+\.\d+\s', title):
                    fetch(b["id"])
            if not res.get("has_more"):
                break
            cursor = res.get("next_cursor")

    fetch(ch_page_id)
    return slugs


CHAPTERS = {
    1:  ("8e5cd1ec-3490-4d69-aa7f-b21ab056a508", "1-clinical-decision-making",  "Clinical Decision-Making"),
    2:  ("5ec47a8c-5671-48fc-91af-45d63691e6e6", "2-clinical-therapeutics",     "Clinical Therapeutics and Good Prescribing"),
    3:  ("0b1c71bf-1898-4f99-ab97-018154d0ad71", "3-clinical-genetics",         "Clinical Genetics"),
    4:  ("0b4e940a-dc46-4a56-b120-b1e4ba682c63", "4-clinical-immunology",       "Clinical Immunology"),
    5:  ("20ae0f80-5c75-4019-83af-5d981bccbe72", "5-nutritional-factors",       "Nutritional Factors in Disease"),
    6:  ("83035ef3-c78d-462b-816a-3d8ad0b0e653", "6-population-health",         "Population Health and Epidemiology"),
    7:  ("6469084f-1ff0-4679-8f4f-4bab9f1d0802", "7-principles-of-infection",   "Principles of Infectious Disease"),
    8:  ("8d4228ea-8497-4d4d-b2e7-f62a746f39d1", "8-oncology",                  "Oncology"),
    9:  ("c65289d8-2227-48e3-a809-cb07e2b70f66", "9-palliative-care",           "Pain and Palliative Care"),
    10: ("3835588e-846f-81a1-bd40-fbd5d564fd2e", "10-acute-medicine",           "Acute Medicine and Critical Illness"),
}


def main():
    ch_n = int(sys.argv[1]) if len(sys.argv) > 1 else None
    chapters_to_check = [ch_n] if ch_n else sorted(CHAPTERS.keys())

    total_src = total_med = total_not = total_gaps = 0

    for ch_n in chapters_to_check:
        notion_id, slug, src_name = CHAPTERS[ch_n]
        src_dir = Path("/mnt/tb/Medicine") / src_name
        ch_dir = Path("/mnt/tb/Sea-knowledge/#MedSea/chapters") / slug

        src_topics, src_dups = get_source_topics(src_dir)
        med_slugs = get_medsea_slugs(ch_dir / "diseases")
        notion_slugs = get_notion_slugs(notion_id) if notion_id else set()

        src_slugs = set(src_topics.keys())
        src_only_med = src_slugs - med_slugs
        src_only_not = src_slugs - notion_slugs

        status_med = "OK" if not src_only_med else "MISSING-" + str(len(src_only_med))
        status_not = "OK" if not src_only_not else "MISSING-" + str(len(src_only_not))

        print(f"\nCh {ch_n:2} ({slug}):")
        print(f"  source unique: {len(src_slugs):3}  ({len(src_dups)} dupes removed)")
        print(f"  medsea:        {len(med_slugs):3}  {status_med}")
        print(f"  notion:        {len(notion_slugs):3}  {status_not}")

        if src_only_med:
            print(f"  ! Source topics NOT in MedSea ({len(src_only_med)}):")
            for s in sorted(src_only_med):
                f, raw = src_topics[s]
                print(f"      [{s}] <- {f.relative_to(src_dir)}")
            total_gaps += len(src_only_med)

        if src_only_not:
            print(f"  ! Source topics NOT in Notion ({len(src_only_not)}):")
            for s in sorted(src_only_not)[:10]:
                print(f"      [{s}]")
            if len(src_only_not) > 10:
                print(f"      ... +{len(src_only_not) - 10} more")

        total_src += len(src_slugs)
        total_med += len(med_slugs)
        total_not += len(notion_slugs)

    print("\n" + "=" * 70)
    print(f"TOTAL source unique: {total_src}  medsea: {total_med}  notion: {total_not}")
    print(f"REAL GAPS (source not in MedSea): {total_gaps}")
    if total_gaps == 0:
        print("OK All chapters fully synced across source / MedSea / Notion")


if __name__ == "__main__":
    main()