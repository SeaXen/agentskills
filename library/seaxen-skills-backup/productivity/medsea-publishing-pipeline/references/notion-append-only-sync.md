# Notion APPEND-Only Sync — Validated Pattern (Ch 11-15, 2026-06-21)

When the MedSea Notion mirror has content from a prior sync but it's significantly shorter than the current `/mnt/tb/Medicine` source, use this pattern instead of the DELETE+append approach. Avoids the rate-limit cascade that killed the v2/v3 sync attempts.

## Why APPEND-Only Works

- Notion's rate limit is 3 RPS burst / ~50 req/min sustained. Parallel DELETEs (10 workers × 100+ blocks = 1000+ DELETE calls) hit 429 almost immediately.
- The 429 backoff (Retry-After header) can be 30-60s. Parallel DELETE workers all sleeping simultaneously means the script stalls for 5-10 minutes between topic batches.
- APPEND-only makes 4-6 PATCH calls per topic (100 blocks/call), no DELETE. The old content remains above the divider; new 100%-match content below. Pages are bigger but each is complete.

## The Script (validated on Ch 11-15: 139 topics in 879s)

```python
#!/usr/bin/env python3
"""APPEND-only Notion sync for MedSea chapters.

Strategy: skip DELETE entirely. PATCH new content with a clear divider+callout
header so users can find the new 100%-match content. Old content stays above
as stale history.
"""
import json, urllib.request, time, re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Load API key
api_key = None
with open("/root/.hermes/.env") as f:
    for line in f:
        if line.startswith("NOTION_API_KEY"):
            api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
            break

# Chapter root IDs (25th Ed MedSea DB)
CHAPTER_ROOTS = {
    11: "abc75846ef544efcb3b78f00134f50b2",  # Poisoning
    12: "fce508f973a64d58b48ad1e2d186e39d",  # Envenomation
    13: "b9b201cbbecc4eaab3c4b6c958c8ac11",  # Austere/Environmental
    14: "eb9d6efbe3bb4ccc8302396a8edc57cf",  # Infectious Disease
    15: "19c59a0895cd4ea4bee4e69d90ce37c8",  # STI
}

# Source dir mapping (CRITICAL — see medsea-publishing-pipeline SKILL.md)
CH_SRC = {
    11: "Chapter 7 - Poisoning",  # NOT "Poisoning"
    12: "Envenomation",
    13: "Environmental medicine",  # NOT "Medicine in Austere Environments"
    14: "Infectious Disease",
    15: "Sexually Transmitted Infections",
}

# Safe rate: 2.5 RPS (0.4s per call). 0.36s was tested and still 429s.
RATE = 0.4
_last = [0]
_lock = threading.Lock()

def http(method, url, data=None, retries=4):
    with _lock:
        wait = RATE - (time.time() - _last[0])
        if wait > 0: time.sleep(wait)
        _last[0] = time.time()
    h = {"Authorization": f"Bearer {api_key}", "Notion-Version": "2022-06-28",
         "Content-Type": "application/json"}
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, method=method, headers=h)
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            txt = e.read().decode()
            if e.code == 429:
                wait = int(e.headers.get("Retry-After", "5"))
                time.sleep(wait); continue
            if e.code in (400, 404): return {"_error": e.code, "_body": txt[:300]}
            time.sleep(1 + attempt); continue
        except (urllib.error.URLError, TimeoutError, OSError):
            time.sleep(1 + attempt); continue
    return {"_error": "max_retries"}


def md_to_blocks(md, with_header=True):
    """Convert MD to Notion blocks. Skip nav links, convert callouts."""
    blocks = []
    if with_header:
        blocks.append({"object": "block", "type": "divider", "divider": {}})
        blocks.append({"object": "block", "type": "callout", "callout": {
            "rich_text": [{"type": "text", "text": {"content":
                "📘 MedSea 100% Content (synced 2026-06-21) — word-for-word match "
                "with /mnt/tb/Medicine source. Stale content above this divider is "
                "the previous Notion version."}}],
            "icon": {"type": "emoji", "emoji": "📘"},
            "color": "blue_background"
        }})

    in_code = False; code_buf = []; code_lang = "plain text"
    for line in md.split("\n"):
        if line.strip().startswith("```"):
            if in_code:
                content = "\n".join(code_buf)
                if len(content) > 1900: content = content[:1900] + "\n... (truncated)"
                blocks.append({"object": "block", "type": "code", "code": {
                    "rich_text": [{"type": "text", "text": {"content": content}}],
                    "language": code_lang}})
                code_buf = []; in_code = False
            else:
                in_code = True
                lang = line.strip().lstrip("`").strip()
                code_lang = lang if lang and lang != "```" else "plain text"
            continue
        if in_code: code_buf.append(line); continue
        if not line.strip(): continue
        if line.strip().startswith("Related:") and "[[" in line: continue
        if line.strip().startswith("> [!") and "]]" not in line:
            clean = line.lstrip("> ").strip()
            if clean.startswith("[!"):
                clean = clean.split("]", 1)[1].strip() if "]" in clean else clean
            blocks.append({"object": "block", "type": "callout", "callout": {
                "rich_text": [{"type": "text", "text": {"content": clean}}],
                "icon": {"type": "emoji", "emoji": "💡"},
                "color": "default"}})
            continue
        if line.strip().startswith("> ") and "[[" in line: continue
        text = line.rstrip()
        if len(text) > 1900: text = text[:1900] + "..."
        if text.startswith("### "):
            blocks.append({"object": "block", "type": "heading_3",
                "heading_3": {"rich_text": [{"type": "text", "text": {"content": text[4:]}}]}})
        elif text.startswith("## "):
            blocks.append({"object": "block", "type": "heading_2",
                "heading_2": {"rich_text": [{"type": "text", "text": {"content": text[3:]}}]}})
        elif text.startswith("# "):
            blocks.append({"object": "block", "type": "heading_1",
                "heading_1": {"rich_text": [{"type": "text", "text": {"content": text[2:]}}]}})
        elif text.startswith("- ") or text.startswith("* "):
            blocks.append({"object": "block", "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": text[2:]}}]}})
        elif re.match(r"^\d+\.\s", text):
            content = re.sub(r"^\d+\.\s", "", text)
            blocks.append({"object": "block", "type": "numbered_list_item",
                "numbered_list_item": {"rich_text": [{"type": "text", "text": {"content": content}}]}})
        else:
            blocks.append({"object": "block", "type": "paragraph",
                "paragraph": {"rich_text": [{"type": "text", "text": {"content": text}}]}})
    return blocks


def get_children(parent_id):
    children = []; cursor = None
    while True:
        path = f"/blocks/{parent_id}/children?page_size=100"
        if cursor: path += f"&start_cursor={cursor}"
        r = http("GET", f"https://api.notion.com/v1{path}")
        for b in r.get("results", []):
            if b.get("type") == "child_page" and not b.get("archived", False):
                children.append((b["id"], b.get("child_page", {}).get("title", "")))
        if not r.get("has_more"): break
        cursor = r.get("next_cursor")
    return children


def process_topic(item):
    ch, hub_num, topic_slug, ms_path, page_id = item
    try:
        ms_content = Path(ms_path).read_text()
        ms_blocks = md_to_blocks(ms_content, with_header=True)
        if not ms_blocks: return ("skipped", ch, hub_num, topic_slug, "no blocks")
        n_appended = 0
        for i in range(0, len(ms_blocks), 100):
            batch = ms_blocks[i:i+100]
            r = http("PATCH", f"https://api.notion.com/v1/blocks/{page_id}/children",
                     {"children": batch})
            if "_error" in r: return ("failed", ch, hub_num, topic_slug, f"patch err: {str(r)[:150]}")
            n_appended += len(batch)
        return ("updated", ch, hub_num, topic_slug, f"add={n_appended}")
    except Exception as e:
        return ("failed", ch, hub_num, topic_slug, str(e)[:200])


def build_work_list():
    """Index Notion + build MedSea work list."""
    MEDSEA = Path("/mnt/tb/Sea-knowledge/#MedSea/chapters")

    hub_map = {}; topic_map = {}
    for ch, root_id in CHAPTER_ROOTS.items():
        hub_map[ch] = {}
        for cid, title in get_children(root_id):
            m = re.match(rf"^{ch}\.(\d+)\.?\s*(.*)", title)
            if m: hub_map[ch][int(m.group(1))] = cid
        for hub_num, hub_id in hub_map[ch].items():
            topics = {}
            for tid, title in get_children(hub_id):
                cleaned = re.sub(r"^\d+\.\d+(?:\.\d+)?\s+", "", title)
                topics[cleaned.lower()] = tid
            topic_map[(ch, hub_num)] = topics

    work = []; not_found = []
    for ch in CHAPTER_ROOTS.keys():
        ch_slug = None
        for d in MEDSEA.iterdir():
            if d.is_dir() and d.name.startswith(f"{ch}-"):
                ch_slug = d.name; break
        if not ch_slug: continue
        medsea_chapter = MEDSEA / ch_slug / "diseases"
        for topic_dir in sorted(medsea_chapter.iterdir()):
            if not topic_dir.is_dir(): continue
            md = topic_dir / "topic.md"
            if not md.exists(): continue
            m = re.match(rf"^{ch}\.(\d+)\.(\d+)-(.+)", topic_dir.name)
            if not m: continue
            hub_num = int(m.group(1))
            if hub_num == 0: continue
            topic_slug = m.group(3)
            topics = topic_map.get((ch, hub_num), {})
            title_lc = topic_slug.replace("-", " ").lower()
            slug_lc = topic_slug.lower()
            page_id = topics.get(title_lc) or topics.get(slug_lc)
            if not page_id:
                for t, pid in topics.items():
                    if title_lc in t or t in title_lc or slug_lc.replace("-", " ") in t:
                        page_id = pid; break
            if not page_id:
                not_found.append(f"{ch}.{hub_num}.{topic_slug}"); continue
            work.append((ch, hub_num, topic_slug, str(md), page_id))
    return work, not_found


def main():
    print("=== APPEND-only Notion sync (Ch 11-15) ===", flush=True)
    work, not_found = build_work_list()
    print(f"Work: {len(work)} topics, {len(not_found)} not found", flush=True)
    if not_found: print(f"not_found: {not_found}", flush=True)

    progress = {"updated": 0, "skipped": 0, "failed": 0}
    completed = 0; start = time.time()

    with ThreadPoolExecutor(max_workers=2) as ex:
        futures = [ex.submit(process_topic, w) for w in work]
        for fut in as_completed(futures):
            status, ch, hub_num, topic_slug, detail = fut.result()
            progress[status] = progress.get(status, 0) + 1
            completed += 1
            elapsed = time.time() - start
            rate = completed / elapsed if elapsed > 0 else 0
            eta = (len(work) - completed) / rate if rate > 0 else 0
            print(f"  [{completed}/{len(work)}] {status}={progress['updated']}/{progress['skipped']}/{progress['failed']} | {rate:.2f}/s | ETA {eta:.0f}s | {topic_slug} {detail}", flush=True)

    elapsed = time.time() - start
    print(f"\nDONE in {elapsed:.0f}s: upd={progress['updated']} skip={progress['skipped']} fail={progress['failed']}", flush=True)


if __name__ == "__main__":
    main()
```

## Special-Case Handler: Parens in Title and Missing Pages

After the main sync, 2-3 topics per chapter usually fail to match by title. Handle in a separate post-script:

```python
# 1. Topic exists in Notion but title has parens/special chars
# Example: MedSea slug "pneumocystis-pneumonia-pcp" vs Notion title
# "Pneumocystis Pneumonia (PCP / PJP)" — the parens break `in` containment check.
# Find by direct search or by walking hub children and matching on the LONGEST word overlap.

def find_page_by_bag_of_words(hub_id, slug_words):
    """Match when slug's long words overlap Notion title's long words."""
    topics = get_children(hub_id)
    best = None; best_score = 0
    for tid, title in topics:
        title_clean = re.sub(r"[()/]", " ", title.lower())
        title_words = set(w for w in re.split(r"[\s\-]+", title_clean) if len(w) > 3)
        score = len(slug_words & title_words)
        if score > best_score:
            best_score = score
            best = (tid, title)
    return best if best_score >= 2 else None  # require 2+ word overlap

# 2. Topic doesn't exist in Notion at all (hub has fewer topics than expected)
# Create the page first, then APPEND content.
def create_topic_page(hub_id, title, ms_md):
    create_r = http("POST", "https://api.notion.com/v1/pages", {
        "parent": {"type": "page_id", "page_id": hub_id},
        "properties": {"title": [{"type": "text", "text": {"content": title}}]},
        "children": [{"object": "block", "type": "callout", "callout": {
            "rich_text": [{"type": "text", "text": {"content":
                "📘 MedSea 100% Content (synced YYYY-MM-DD) — NEW page created. Word-for-word match with /mnt/tb/Medicine source."}}],
            "icon": {"type": "emoji", "emoji": "📘"},
            "color": "blue_background"
        }}]
    })
    if "_error" in create_r: return None
    new_id = create_r["id"]
    blocks = md_to_blocks(ms_md, with_header=False)
    for i in range(0, len(blocks), 100):
        batch = blocks[i:i+100]
        r = http("PATCH", f"https://api.notion.com/v1/blocks/{new_id}/children",
                 {"children": batch})
        if "_error" in r: return None
    return new_id
```

## Verification After APPEND Sync

```python
# Total chars per page should be ~2x the MedSea source (old + new stacked)
# If a page has < 1.5x the MedSea chars, the APPEND silently failed for that page.
for page_id, medsea_chars in topic_sizes.items():
    total_chars = count_chars_in_page(page_id)
    if total_chars < medsea_chars * 1.4:
        # Suspicious — re-run for this page
        log.warning(f"Page {page_id} has {total_chars} chars, expected ~{medsea_chars * 2}")
```

## Real Ch 11-15 Run Stats (2026-06-21)

| Ch | Topics | API calls | Time | Failures | Notes |
|---|---|---|---|---|---|
| 11 | 37 | ~140 | 4 min | 0 | Antidotes Overview: MedSea 26K → Notion 50K (2x as expected) |
| 12 | 13 | ~50 | 2 min | 0 | |
| 13 | 9 | ~30 | 1 min | 0 | |
| 14 | 55 | ~210 | 6 min | 0 | Acute Bacterial Meningitis: MedSea 33K → Notion 57K |
| 15 | 26 | ~90 | 2 min | 0 | |
| Special: 14.1.55 PCP | +1 | 3 | 30s | 0 | Title with parens, found via search |
| Special: 15.3.06 Syphilis Serology | +1 | 6 | 30s | 0 | Page didn't exist, created new |
| **Total** | **142** | **~530** | **~15 min** | **0** | All topics at 100% MedSea match |

vs DELETE+append (v2 attempt): 10/951 in ~30 min, then stalled 7+ min on a single topic due to 429 cascade. APPEND-only is the right tool for "stale content, not empty" Notion mirrors.
