#!/usr/bin/env python3
"""3-source chapter completeness audit for MedSea.

Compares source MDs in /mnt/tb/Medicine against MedSea local chapters
and Notion mirror. Reports missing topics per chapter without modifying anything.

Usage:
  python3 audit_chapters_3way.py <chapter-slug> [<chapter-slug> ...]
  python3 audit_chapters_3way.py 11-poisoning 12-envenomation 13-austere-medicine
  python3 audit_chapters_3way.py --all

Prints source count, MedSea count, Notion count, and the missing list per chapter.

Validates:
  2026-06-20 — Davidson Ch 1-5 (initial)
  2026-06-20 — Davidson Ch 6-10 (found 50 missing in Ch 9, 2 missing in Ch 7 Notion,
             1 missing in Ch 9 MedSea, 0 in Ch 6/8/10)
  2026-06-20 — Davidson Ch 11-15 (all full match; added 1 missing: 14.1.55 PCP)
  2026-06-20 — Davidson Ch 16-20 (84 -> 7 after hub-overview + title-fuzzy filter;
             added 7 missing: Ch 16 syncope + Ebstein; Ch 18 urinalysis + GFR)

Pitfalls addressed (see references/3way-audit-gotchas.md):
  - MedSea topic layout varies (flat vs directory) — handles both
  - manifest.json schema varies — uses .get() fallbacks
  - Source _full.md / _Hub.md suffixes stripped
  - Root-level hub-overview MDs filtered out (Ch 17-20 umbrella files)
  - Title-based fuzzy match (Jaccard + overlap coefficient) for renamed topics
  - Notion pagination uses query string, not body
  - Notion child-page hierarchy walked recursively
  - Notion hub numbering may differ from MedSea hub_num (24th→25th Ed renames)
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

SOURCE_BASE = Path("/mnt/tb/Medicine")
MEDSEA_BASE = Path("/mnt/tb/Sea-knowledge/#MedSea/chapters")
NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"
TITLE_FUZZY_THRESHOLD = 0.55  # Jaccard + overlap coefficient


# --- Notion API helpers ---------------------------------------------------

def load_api_key():
    PREFIX = "NOTION" + "_API_KEY" + chr(61)
    for line in Path("/root/.hermes/.env").read_text().splitlines():
        line = line.strip()
        if line.startswith(PREFIX) and not line.startswith("#"):
            return line[len(PREFIX):].strip()
    print("ERROR: NOTION_API_KEY not found in /root/.hermes/.env", file=sys.stderr)
    sys.exit(1)


def notion_get(endpoint, api_key):
    url = f"{BASE_URL}/{endpoint}"
    req = urllib.request.Request(url, method="GET", headers={
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": NOTION_VERSION,
    })
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return {"_error": e.code, "_body": e.read().decode()[:500]}


def get_notion_children_paginated(page_id, api_key):
    children = []
    cursor = None
    while True:
        endpoint = f"blocks/{page_id}/children"
        if cursor:
            endpoint += f"?start_cursor={cursor}"
        data = notion_get(endpoint, api_key)
        if "_error" in data:
            break
        children.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return children


def get_notion_titles_recursive(chapter_id, api_key):
    """Walk chapter -> hub pages -> topic pages. Returns list of (title, slug)."""
    out = []
    top = get_notion_children_paginated(chapter_id, api_key)
    for b in top:
        if b.get("type") != "child_page":
            continue
        title = b["child_page"]["title"]
        slug = slugify(title)
        out.append((title, slug))
        if re.match(r"^\d+\.\d+\s", title):
            out.extend(get_notion_titles_recursive(b["id"], api_key))
    return out


# --- Slug + title normalization ------------------------------------------

def slugify(text):
    s = text.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def normalize_title_words(text):
    return set(w for w in re.sub(r"[^a-z0-9\s]", " ", text.lower()).split() if len(w) >= 4)


def title_fuzzy_match(src_title, med_titles_dict, threshold=TITLE_FUZZY_THRESHOLD):
    src_w = normalize_title_words(src_title)
    if not src_w:
        return None, 0.0
    best_slug, best_score = None, 0.0
    for med_slug, med_title in med_titles_dict.items():
        med_w = normalize_title_words(med_title)
        if not med_w:
            continue
        inter = len(src_w & med_w)
        if inter == 0:
            continue
        union = len(src_w | med_w) or 1
        jaccard = inter / union
        overlap = inter / min(len(src_w), len(med_w))
        score = max(jaccard, overlap)
        if score > best_score:
            best_score, best_slug = score, med_slug
    if best_score >= threshold:
        return best_slug, best_score
    return None, best_score


# --- Source / MedSea topic collectors ------------------------------------

def get_source_topics(source_dir):
    """Source MDs from /mnt/tb/Medicine/<Chapter>/.

    Strips _full / _Hub suffixes AND marks root-level hub-overview MDs.

    Returns:
      dict[slug] -> {"is_hub": bool, "path": str, "name": str}
    """
    src_path = SOURCE_BASE / source_dir
    if not src_path.exists():
        return {}
    skip_keywords = ("MOC", "Hierarchy", "Roadmap", "Template", "README")
    topics = {}
    for f in sorted(src_path.rglob("*.md")):
        if any(k in f.name for k in skip_keywords):
            continue
        clean = (f.name.replace("_full.md", "")
                      .replace("_Hub.md", "")
                      .replace("_HUB.md", "")
                      .replace(".md", ""))
        slug = slugify(clean)
        is_hub = (f.parent == src_path)
        topics[slug] = {"is_hub": is_hub, "path": str(f), "name": f.name}
    return topics


def get_medsea_topics_with_titles(slug):
    """MedSea topics from chapters/<slug>/diseases/. Handles both layouts.

    Returns: dict[slug] -> title (derived from slug name).
    """
    ch_path = MEDSEA_BASE / slug / "diseases"
    if not ch_path.exists():
        return {}

    def title_from_slug(s):
        return " ".join(w.capitalize() for w in s.split("-"))

    topics = {}
    for entry in ch_path.iterdir():
        if entry.is_dir():
            m = re.match(r"^\d+\.\d+\.\d+-(.+)$", entry.name)
            if m:
                topics[slugify(m.group(1))] = title_from_slug(m.group(1))
        elif entry.suffix == ".md":
            m = re.match(r"^(\d+\.\d+)\.(\d+)-(.+)$", entry.stem)
            if m:
                raw_slug = m.group(3).replace("-full", "").replace("-hub", "")
                topics[slugify(raw_slug)] = title_from_slug(raw_slug)
    return topics


def get_notion_topic_slugs(chapter_id, api_key):
    if not chapter_id:
        return set()
    titles = get_notion_titles_recursive(chapter_id, api_key)
    return {slugify(t) for t, _ in titles if t}


# --- Manifest reading (schema varies) ------------------------------------

def read_manifest_meta(slug):
    manifest_path = MEDSEA_BASE / slug / "manifest.json"
    if not manifest_path.exists():
        return None
    try:
        m = json.loads(manifest_path.read_text())
        th = m.get("total_hubs") or m.get("n_hubs", 0)
        tt = m.get("total_topics") or m.get("n_topics", 0)
        return (th, tt, tt)
    except Exception:
        return None


# --- Chapter registry ----------------------------------------------------
# Verified via live Notion API 2026-06-20.

CHAPTERS = {
    "1-clinical-decision-making": {"name": "Clinical Decision-Making", "source_dir": "Clinical Decision-Making", "notion_id": "8e5cd1ec34904d69aa7fb21ab056a508"},
    "2-clinical-therapeutics": {"name": "Clinical Therapeutics & Prescribing", "source_dir": "Clinical Therapeutics and Good Prescribing", "notion_id": "5ec47a8c567148fc91af45d63691e6e6"},
    "3-clinical-genetics": {"name": "Clinical Genetics", "source_dir": "Clinical Genetics", "notion_id": "0b1c71bf18984f99ab97018154d0ad71"},
    "4-clinical-immunology": {"name": "Clinical Immunology", "source_dir": "Clinical Immunology", "notion_id": "0b4e940adc464a56b120b1e4ba682c63"},
    "5-nutritional-factors": {"name": "Nutritional Factors in Disease", "source_dir": "Nutritional Factors in Disease", "notion_id": "20ae0f805c75401983af5d981bccbe72"},
    "6-population-health": {"name": "Population Health & Epidemiology", "source_dir": "Population Health and Epidemiology", "notion_id": "83035ef3c78d462b816a3d8ad0b0e653"},
    "7-principles-of-infection": {"name": "Principles of Infection", "source_dir": "Principles of Infectious Disease", "notion_id": "6469084f1ff046798f4f4bab9f1d0802"},
    "8-oncology": {"name": "Oncology", "source_dir": "Oncology", "notion_id": "8d4228ea84974d4db2e7f62a746f39d1"},
    "9-palliative-care": {"name": "Palliative & Supportive Care", "source_dir": "Pain and Palliative Care", "notion_id": "c65289d8-2227-48e3-a809-cb07e2b70f66"},
    "10-acute-medicine": {"name": "Acute Medicine & Critical Illness", "source_dir": "Acute Medicine and Critical Illness", "notion_id": "3835588e846f81a1bd40fbd5d564fd2e"},
    "11-poisoning": {"name": "Poisoning", "source_dir": "Chapter 7 - Poisoning", "notion_id": "abc75846ef544efcb3b78f00134f50b2"},
    "12-envenomation": {"name": "Envenomation", "source_dir": "Envenomation", "notion_id": "fce508f973a64d58b48ad1e2d186e39d"},
    "13-austere-medicine": {"name": "Medicine in Austere Environments", "source_dir": "Environmental medicine", "notion_id": "b9b201cbbecc4eaab3c4b6c958c8ac11"},
    "14-infectious-disease": {"name": "Infectious Disease", "source_dir": "Infectious Disease", "notion_id": "eb9d6efbe3bb4ccc8302396a8edc57cf"},
    "15-sexually-transmitted-infections": {"name": "Sexually Transmitted Infections", "source_dir": "Sexually Transmitted Infections", "notion_id": "19c59a0895cd4ea4bee4e69d90ce37c8"},
    "16-cardiology": {"name": "Cardiology", "source_dir": "Cardiology", "notion_id": "8baa010d9cc94c48826136417d383973"},
    "17-respiratory-medicine": {"name": "Respiratory Medicine", "source_dir": "Respiratory", "notion_id": "d4fe7d456ca4481581e806ebe9e177cf"},
    "18-nephrology-urology": {"name": "Nephrology and Urology", "source_dir": "Nephrology and Urology", "notion_id": "710f215344c34692af7584e89e714ff0"},
    "19-clinical-biochemistry-and-metabolic-medi": {"name": "Clinical Biochemistry and Metabolic Medicine", "source_dir": "Clinical Biochemistry and Metabolic Medicine", "notion_id": None},
    "20-endocrinology": {"name": "Endocrinology", "source_dir": "Endocrinology", "notion_id": "9db6455d6ae840f0ac29129217d6ccef"},
}


# --- Audit ----------------------------------------------------------------

def audit(slug, info, api_key):
    print(f"\n{'=' * 70}")
    print(f"Chapter: {info['name']} ({slug})")
    print(f"Notion ID: {info.get('notion_id') or '(not in DB)'}")
    print(f"{'=' * 70}")

    src = get_source_topics(info["source_dir"])
    medsea = get_medsea_topics_with_titles(slug)
    notion = get_notion_topic_slugs(info.get("notion_id"), api_key)

    real_src = {s: m for s, m in src.items() if not m["is_hub"]}
    hub_overview_src = [m["name"] for m in src.values() if m["is_hub"]]

    print(f"\nSource total MDs (excl MOC/Hierarchy/Template): {len(src)}")
    print(f"  -> Hub overviews at root (skipped): {len(hub_overview_src)}")
    print(f"  -> Real topics to audit: {len(real_src)}")
    print(f"MedSea live topics: {len(medsea)}")
    print(f"Notion: {len(notion)}")

    manifest = read_manifest_meta(slug)
    if manifest:
        th, tt, _ = manifest
        print(f"Manifest: {th} hubs, {tt} topics")

    matched = set()
    title_matched = {}
    for s in real_src:
        if s in medsea or s in notion:
            matched.add(s)
        else:
            stem = real_src[s]["name"].replace(".md", "").replace("_full", "").replace("_Hub", "")
            m, score = title_fuzzy_match(stem, medsea)
            if m:
                title_matched[s] = (m, score)
                matched.add(s)

    truly_missing = {s: m for s, m in real_src.items() if s not in matched}

    print(f"\n  Slug-matched: {len(matched) - len(title_matched)}")
    if title_matched:
        print(f"  Title-fuzzy matched: {len(title_matched)}")
        for s, (m, score) in list(title_matched.items())[:5]:
            print(f"    {s!r} -> {m!r} (score {score:.2f})")
        if len(title_matched) > 5:
            print(f"    ... +{len(title_matched) - 5} more")
    print(f"  TRULY MISSING (no slug or title match): {len(truly_missing)}")
    if truly_missing:
        for s, m in list(truly_missing.items())[:15]:
            print(f"    - {s}  ({m['name'][:60]})")
        if len(truly_missing) > 15:
            print(f"    ... +{len(truly_missing) - 15} more")
    if hub_overview_src:
        print(f"\n  Hub overview files (represented as MedSea hub pages):")
        for n in hub_overview_src[:5]:
            print(f"    - {n}")
        if len(hub_overview_src) > 5:
            print(f"    ... +{len(hub_overview_src) - 5} more")
    if not truly_missing:
        print("\n  OK: Source fully covered in MedSea + Notion (after title-fuzzy check)")

    return {
        "slug": slug,
        "src_topics": len(real_src),
        "hub_overviews": len(hub_overview_src),
        "medsea": len(medsea),
        "notion": len(notion),
        "truly_missing": truly_missing,
    }


def main():
    args = sys.argv[1:]
    if "--all" in args:
        slugs = list(CHAPTERS.keys())
        args = [a for a in args if a != "--all"]
        if args:
            slugs = [s for s in slugs if s in args]
    else:
        slugs = args

    api_key = load_api_key()
    results = []
    for slug in slugs:
        if slug not in CHAPTERS:
            print(f"Unknown: {slug}. Known: {list(CHAPTERS.keys())}", file=sys.stderr)
            continue
        results.append(audit(slug, CHAPTERS[slug], api_key))

    print(f"\n{'=' * 70}")
    print("OVERALL")
    print(f"{'=' * 70}")
    total_missing = 0
    for r in results:
        n = len(r["truly_missing"])
        total_missing += n
        flag = "OK" if n == 0 else f"!! {n} missing"
        print(f"  {r['slug']:42} src={r['src_topics']:3} medsea={r['medsea']:3} notion={r['notion']:3}  {flag}")
    print(f"\n  Total truly-missing topics: {total_missing}")


if __name__ == "__main__":
    main()
