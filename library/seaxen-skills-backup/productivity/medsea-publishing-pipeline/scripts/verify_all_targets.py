#!/usr/bin/env python3
"""
Verify all 5 sync targets for a MedSea chapter.

Use after every pipeline run before claiming "synced". Hit hard on 2026-06-20
when "Notion synced" turned out to mean "36 chapter pages, 0 topic sub-pages".

Usage:
    python3 verify_all_targets.py 16            # verify Ch 16 Cardiology
    python3 verify_all_targets.py 16 18         # verify Ch 16 and 18
    python3 verify_all_targets.py --all         # verify all built chapters
    python3 verify_all_targets.py --all --json  # machine-readable output
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

# Canonical identifiers (kept in sync with SKILL.md)
MEDSEA_DB = "3805588e-846f-808b-a23b-cf63c89f372e"
MEDSEA_REPO = Path("/mnt/tb/Sea-knowledge/#MedSea")
MEDICINE_ROOT = Path("/mnt/tb/Medicine")
SITE_LIVE_BASE = "http://localhost:8855"

# Davidson 25th Ed number → site slug + chapter folder
DAVIDSON_SLUGS = {
    1: "1-clinical-decision-making", 2: "2-clinical-therapeutics",
    3: "3-clinical-genetics", 4: "4-clinical-immunology",
    5: "5-nutritional-factors", 6: "6-population-health",
    7: "7-principles-of-infection", 8: "8-oncology",
    9: "9-palliative-care", 10: "10-acute-medicine",
    11: "11-poisoning", 12: "12-envenomation",
    13: "13-austere-medicine", 14: "14-infectious-disease",
    15: "15-sexually-transmitted-infections", 16: "16-cardiology",
    17: "17-respiratory-medicine", 18: "18-nephrology-urology",
    19: "19-clinical-biochemistry-and-metabolic-medi",
    20: "20-endocrinology", 21: "21-diabetes-mellitus",
    22: "22-gastroenterology", 23: "23-hepatology",
    24: "24-haematology-and-transfusion-medicine",
    25: "25-rheumatology-and-bone-disease",
    26: "26-dermatology", 27: "27-neurology-and-stroke-medicine",
    28: "28-medical-ophthalmology", 29: "29-medical-psychiatry",
    30: "30-maternal-medicine",
    31: "31-adolescence-transition-and-young-adult-m",
    32: "32-older-adult-medicine-and-frailty",
}

CHAPTER_FOLDERS = {  # Davidson source folder name (varies by chapter)
    16: "Cardiology",
}


def load_api_key():
    api_key = os.environ.get("NOTION_API_KEY")
    if api_key:
        return api_key
    env_path = Path("/root/.hermes/.env")
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("NOTION_API_KEY"):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def notion_get(api_key, path):
    req = urllib.request.Request(
        f"https://api.notion.com/v1{path}",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Notion-Version": "2022-06-28",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {"error": str(e), "body": e.read().decode()[:500]}


def count_child_pages(api_key, page_id):
    """Walk blocks/{page_id}/children paginated, count child_page blocks."""
    total = 0
    cursor = None
    pages = 0
    while True:
        pages += 1
        path = f"/blocks/{page_id}/children?page_size=100"
        if cursor:
            path += f"&start_cursor={cursor}"
        r = notion_get(api_key, path)
        if "results" not in r:
            return {"total": -1, "error": r.get("error", "?")}
        results = r["results"]
        total += sum(1 for b in results if b.get("type") == "child_page")
        if not r.get("has_more"):
            break
        cursor = r.get("next_cursor")
        if pages > 100:
            return {"total": total, "warning": "stopped at 100 pages"}
    return {"total": total}


def find_chapter_page(api_key, chapter_num, slug):
    """Find the Notion page ID for 'Chapter N: Title' by DB query."""
    r = notion_get(api_key, f"/databases/{MEDSEA_DB}/query?page_size=100")
    if "results" not in r:
        return None, r.get("error", "query failed")
    for page in r["results"]:
        name = page.get("properties", {}).get("Name", {})
        if name.get("title"):
            t = name["title"][0].get("plain_text", "")
            if t.lower().startswith(f"chapter {chapter_num}:"):
                return page["id"], t
    return None, None


def verify_chapter(chapter_num, api_key=None):
    """Run all 6 verification checks for a single chapter."""
    slug = DAVIDSON_SLUGS.get(chapter_num)
    if not slug:
        return {"chapter": chapter_num, "error": f"unknown chapter {chapter_num}"}

    out = {"chapter": chapter_num, "slug": slug, "checks": {}}

    # 1. Local source
    source_folder = MEDICINE_ROOT / CHAPTER_FOLDERS.get(chapter_num, "")
    if source_folder.exists():
        files = [f for f in source_folder.rglob("*.md")
                 if "status: full-fcps-mrcp-note" in f.read_text(errors="ignore")[:1000]]
        out["checks"]["1_local_source"] = {
            "ok": True,
            "path": str(source_folder),
            "files": len(files),
        }
    else:
        out["checks"]["1_local_source"] = {
            "ok": False,
            "path": str(source_folder),
            "files": 0,
            "note": "source folder not found",
        }

    # 2. Local chapters
    chap_dir = MEDSEA_REPO / "chapters" / slug / "diseases"
    if chap_dir.exists():
        folders = [d for d in chap_dir.iterdir() if d.is_dir()]
        out["checks"]["2_chapters"] = {
            "ok": True,
            "path": str(chap_dir),
            "folders": len(folders),
        }
    else:
        out["checks"]["2_chapters"] = {
            "ok": False,
            "path": str(chap_dir),
            "folders": 0,
            "note": "chapters folder not found — chapter may not be built",
        }

    # 3. Site build (manifest on disk)
    site_manifest = MEDSEA_REPO / "site" / slug / "topics.json"
    if site_manifest.exists():
        try:
            data = json.loads(site_manifest.read_text())
            topics = data.get("topics", [])
            out["checks"]["3_site_build"] = {
                "ok": True,
                "path": str(site_manifest),
                "topics": len(topics),
            }
        except Exception as e:
            out["checks"]["3_site_build"] = {"ok": False, "error": str(e)}
    else:
        out["checks"]["3_site_build"] = {
            "ok": False,
            "path": str(site_manifest),
            "topics": 0,
            "note": "site manifest not built yet",
        }

    # 4. Docker live
    try:
        with urllib.request.urlopen(f"{SITE_LIVE_BASE}/{slug}/topics.json", timeout=10) as r:
            live_data = json.loads(r.read())
            live_topics = live_data.get("topics", [])
            out["checks"]["4_docker_live"] = {
                "ok": True,
                "url": f"{SITE_LIVE_BASE}/{slug}/topics.json",
                "topics": len(live_topics),
            }
    except Exception as e:
        out["checks"]["4_docker_live"] = {
            "ok": False,
            "url": f"{SITE_LIVE_BASE}/{slug}/topics.json",
            "topics": 0,
            "error": str(e)[:100],
        }

    # 5. Notion DB (page exists + has children)
    if api_key:
        page_id, page_title = find_chapter_page(api_key, chapter_num, slug)
        if page_id:
            child_count = count_child_pages(api_key, page_id)
            out["checks"]["5_notion"] = {
                "ok": child_count.get("total", 0) > 0,
                "page_id": page_id,
                "page_title": page_title,
                "child_pages": child_count.get("total", 0),
                "warning": child_count.get("warning") or child_count.get("error"),
            }
        else:
            out["checks"]["5_notion"] = {
                "ok": False,
                "page_id": None,
                "child_pages": 0,
                "note": f"chapter page not found in DB (searched 'Chapter {chapter_num}:')",
            }
    else:
        out["checks"]["5_notion"] = {
            "ok": None,
            "note": "NOTION_API_KEY not set — skipping",
        }

    # 6. GitHub (last commit)
    try:
        r = subprocess.run(
            ["git", "-C", str(MEDSEA_REPO), "log", "--oneline", "-10"],
            capture_output=True, text=True, timeout=10,
        )
        out["checks"]["6_git"] = {
            "ok": r.returncode == 0,
            "last_commits": r.stdout.strip().splitlines()[:3],
        }
    except Exception as e:
        out["checks"]["6_git"] = {"ok": False, "error": str(e)}

    # Compute overall verdict
    chapter_n = out["checks"].get("2_chapters", {}).get("folders", 0)
    site_n = out["checks"].get("3_site_build", {}).get("topics", 0)
    live_n = out["checks"].get("4_docker_live", {}).get("topics", 0)
    notion_n = out["checks"].get("5_notion", {}).get("child_pages", 0)

    if chapter_n == 0:
        out["verdict"] = "NOT_BUILT"
    else:
        parity = (chapter_n == site_n == live_n)
        notion_ok = (notion_n is None or notion_n > 0 or
                     out["checks"].get("5_notion", {}).get("ok") is None)
        out["verdict"] = "OK" if (parity and notion_ok) else "PARTIAL"

    return out


def render_text(results):
    lines = []
    for r in results:
        if "error" in r and "slug" not in r:
            lines.append(f"FAIL Ch {r['chapter']}: {r['error']}")
            continue
        lines.append(f"\n=== Chapter {r['chapter']}: {r['slug']} [{r['verdict']}] ===")
        c = r["checks"]
        lines.append(
            f"  1. local source:       {c.get('1_local_source', {}).get('files', 0)} files"
        )
        lines.append(
            f"  2. chapters/:          {c.get('2_chapters', {}).get('folders', 0)} folders"
        )
        lines.append(
            f"  3. site manifest:      {c.get('3_site_build', {}).get('topics', 0)} topics"
        )
        lines.append(
            f"  4. docker live:        {c.get('4_docker_live', {}).get('topics', 0)} topics"
        )
        notion = c.get("5_notion", {})
        if notion.get("ok") is None:
            lines.append(f"  5. notion DB:          [skipped: {notion.get('note')}]")
        else:
            lines.append(
                f"  5. notion DB:          {notion.get('child_pages', 0)} child pages "
                f"({notion.get('page_title', '?')})"
            )
        git = c.get("6_git", {})
        if git.get("ok"):
            lines.append(f"  6. git:                {git.get('last_commits', ['?'])[0][:60]}")
        else:
            lines.append(f"  6. git:                ERROR {git.get('error', '?')[:60]}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Verify MedSea sync across all targets")
    parser.add_argument("chapters", nargs="*", type=int, help="Chapter numbers to verify")
    parser.add_argument("--all", action="store_true", help="Verify all built chapters")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()

    api_key = load_api_key()

    if args.all:
        chapters = list(DAVIDSON_SLUGS.keys())
    else:
        chapters = args.chapters or [16]

    results = [verify_chapter(n, api_key) for n in chapters]

    if args.json:
        print(json.dumps(results, indent=2, default=str))
    else:
        print(render_text(results))

    # Exit non-zero if any verdict is PARTIAL
    if any(r.get("verdict") == "PARTIAL" for r in results):
        sys.exit(2)


if __name__ == "__main__":
    main()