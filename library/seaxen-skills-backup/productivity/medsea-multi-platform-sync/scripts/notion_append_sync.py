#!/usr/bin/env python3
"""
Sync MedSea chapter content to Notion - APPEND-only template.

This is the recommended pattern: skips DELETE (avoids 5-10x slowdown and
rate-limit cascades), appends new MedSea content below the existing Notion
content with a clear divider+callout so users can see what's new.

Tested: 139 topics in ~15 minutes (vs 10+ hours for DELETE+APPEND).

Usage:
  1. Set CHAPTER_ROOTS to your chapter's Notion root page ID
  2. Set MEDSEA to your local chapters dir
  3. Run in background via terminal(background=true, notify_on_complete=true)
"""
import json, urllib.request, time, re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# ---- Config: source these from /root/.hermes/.env or hardcode for one-off runs ----
api_key = None
with open("/root/.hermes/.env") as f:
    for line in f:
        if line.startswith("NOTION_API_KEY"):
            api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
            break

# Map: chapter number -> Notion root page ID
CHAPTER_ROOTS = {
    # 11: "abc75846ef544efcb3b78f00134f50b2",
    # 12: "fce508f973a64d58b48ad1e2d186e39d",
}

# Map: chapter number -> MedSea local dir slug
CH_SLUGS = {
    # 11: "11-poisoning",
}

# Map: chapter number -> source dir under /mnt/tb/Medicine
CH_SRC = {
    # 11: "Chapter 7 - Poisoning",
}

# ---- Global rate limiter (3 RPS = 0.36s between calls, safe margin) ----
RATE = 0.36
_last = [0]
_lock = threading.Lock()


def http(method, url, data=None, retries=4):
    """Rate-limited HTTP call. Blocks on _lock until 0.36s since last call."""
    with _lock:
        wait = RATE - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()

    h = {"Authorization": f"Bearer {api_key}", "Notion-Version": "2022-06-28", "Content-Type": "application/json"}
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
                time.sleep(wait)
                continue
            if e.code in (400, 404):
                return {"_error": e.code, "_body": txt[:300]}
            time.sleep(1 + attempt)
            continue
        except (urllib.error.URLError, TimeoutError, OSError):
            time.sleep(1 + attempt)
            continue
    return {"_error": "max_retries"}


def md_to_blocks(md, with_header=True):
    """Convert MD to Notion blocks. Strips Obsidian nav ([[wiki]] links)."""
    blocks = []
    if with_header:
        # Divider + callout so users can see new vs old content
        blocks.append({"object": "block", "type": "divider", "divider": {}})
        blocks.append({"object": "block", "type": "callout", "callout": {
            "rich_text": [{"type": "text", "text": {"content": "📘 MedSea 100% Content — word-for-word match with /mnt/tb/Medicine source."}}],
            "icon": {"type": "emoji", "emoji": "📘"},
            "color": "blue_background"
        }})

    in_code = False
    code_buf = []
    code_lang = "plain text"

    for line in md.split("\n"):
        # Code block toggle
        if line.strip().startswith("```"):
            if in_code:
                content = "\n".join(code_buf)
                if len(content) > 1900:
                    content = content[:1900] + "\n... (truncated)"
                blocks.append({"object": "block", "type": "code",
                    "code": {"rich_text": [{"type": "text", "text": {"content": content}}], "language": code_lang}})
                code_buf = []
                in_code = False
            else:
                in_code = True
                lang = line.strip().lstrip("`").strip()
                code_lang = lang if lang and lang != "```" else "plain text"
            continue
        if in_code:
            code_buf.append(line)
            continue
        if not line.strip():
            continue

        # Skip Obsidian nav: Related: [[...]] and blockquote wikilinks
        if line.strip().startswith("Related:") and "[[" in line:
            continue
        if line.strip().startswith("> [!") and "]]" not in line:
            # Callout → keep as callout
            clean = line.lstrip("> ").strip()
            if clean.startswith("[!"):
                clean = clean.split("]", 1)[1].strip() if "]" in clean else clean
            blocks.append({"object": "block", "type": "callout", "callout": {
                "rich_text": [{"type": "text", "text": {"content": clean}}],
                "icon": {"type": "emoji", "emoji": "💡"},
                "color": "default"
            }})
            continue
        if line.strip().startswith("> ") and "[[" in line:
            continue

        text = line.rstrip()
        if len(text) > 1900:
            text = text[:1900] + "..."

        if text.startswith("### "):
            blocks.append({"object": "block", "type": "heading_3", "heading_3": {"rich_text": [{"type": "text", "text": {"content": text[4:]}}]}})
        elif text.startswith("## "):
            blocks.append({"object": "block", "type": "heading_2", "heading_2": {"rich_text": [{"type": "text", "text": {"content": text[3:]}}]}})
        elif text.startswith("# "):
            blocks.append({"object": "block", "type": "heading_1", "heading_1": {"rich_text": [{"type": "text", "text": {"content": text[2:]}}]}})
        elif text.startswith("- ") or text.startswith("* "):
            blocks.append({"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": text[2:]}}]}})
        elif re.match(r"^\d+\.\s", text):
            content = re.sub(r"^\d+\.\s", "", text)
            blocks.append({"object": "block", "type": "numbered_list_item", "numbered_list_item": {"rich_text": [{"type": "text", "text": {"content": content}}]}})
        else:
            blocks.append({"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": text}}]}})

    return blocks


def get_children(parent_id):
    """Get all non-archived child_page blocks under a Notion page (paged)."""
    children = []
    cursor = None
    while True:
        path = f"/blocks/{parent_id}/children?page_size=100"
        if cursor:
            path += f"&start_cursor={cursor}"
        r = http("GET", f"https://api.notion.com/v1{path}")
        for b in r.get("results", []):
            if b.get("type") == "child_page" and not b.get("archived", False):
                children.append((b["id"], b.get("child_page", {}).get("title", "")))
        if not r.get("has_more"):
            break
        cursor = r.get("next_cursor")
    return children


def process_topic(item):
    """Append MedSea topic.md content to an existing Notion topic page."""
    ch, hub_num, topic_slug, ms_path, page_id = item
    try:
        ms_content = Path(ms_path).read_text()
        ms_blocks = md_to_blocks(ms_content, with_header=True)
        if not ms_blocks:
            return ("skipped", ch, hub_num, topic_slug, "no blocks")
        # PATCH in batches of 100 (Notion's max per call)
        n_appended = 0
        for i in range(0, len(ms_blocks), 100):
            batch = ms_blocks[i:i+100]
            r = http("PATCH", f"https://api.notion.com/v1/blocks/{page_id}/children", {"children": batch})
            if "_error" in r:
                return ("failed", ch, hub_num, topic_slug, f"patch err: {str(r)[:150]}")
            n_appended += len(batch)
        return ("updated", ch, hub_num, topic_slug, f"add={n_appended}")
    except Exception as e:
        return ("failed", ch, hub_num, topic_slug, str(e)[:200])


# ---- Main ----
MEDSEA = Path("/mnt/tb/Sea-knowledge/#MedSea/chapters")

print("=== Indexing Notion hubs and topics ===", flush=True)
hub_map = {}
topic_map = {}
for ch, root_id in CHAPTER_ROOTS.items():
    hub_map[ch] = {}
    for cid, title in get_children(root_id):
        m = re.match(rf"^{ch}\.(\d+)\.?\s*(.*)", title)
        if m:
            hub_map[ch][int(m.group(1))] = cid
    for hub_num, hub_id in hub_map[ch].items():
        topics = {}
        for tid, title in get_children(hub_id):
            cleaned = re.sub(r"^\d+\.\d+(?:\.\d+)?\s+", "", title)
            topics[cleaned.lower()] = tid
        topic_map[(ch, hub_num)] = topics
    n_topics = sum(len(v) for k, v in topic_map.items() if k[0] == ch)
    print(f"  Ch {ch}: {len(hub_map[ch])} hubs, {n_topics} topics", flush=True)

# Build work list from MedSea local
print("\n=== Building work list ===", flush=True)
work = []
not_found = []
for ch in CHAPTER_ROOTS.keys():
    ch_slug = CH_SLUGS[ch]
    medsea_chapter = MEDSEA / ch_slug / "diseases"
    for topic_dir in sorted(medsea_chapter.iterdir()):
        if not topic_dir.is_dir():
            continue
        # Ch 16, 19 use topic.md; Ch 17, 18, 20 use {slug}.md
        md = topic_dir / "topic.md"
        if not md.exists():
            md = topic_dir / f"{topic_dir.name}.md"
        if not md.exists():
            continue

        m = re.match(rf"^{ch}\.(\d+)\.(\d+)-(.+)", topic_dir.name)
        if not m:
            continue
        hub_num = int(m.group(1))
        if hub_num == 0:  # skip MOC/hierarchy
            continue
        topic_slug = m.group(3)

        topics = topic_map.get((ch, hub_num), {})
        title_lc = topic_slug.replace("-", " ").lower()
        slug_lc = topic_slug.lower()
        page_id = topics.get(title_lc) or topics.get(slug_lc)
        if not page_id:
            for t, pid in topics.items():
                if title_lc in t or t in title_lc or slug_lc.replace("-", " ") in t:
                    page_id = pid
                    break
        if not page_id:
            not_found.append(f"{ch}.{hub_num}.{topic_slug}")
            continue
        work.append((ch, hub_num, topic_slug, str(md), page_id))

print(f"\n=== Work: {len(work)} topics, {len(not_found)} not found ===", flush=True)
if not_found:
    print("not_found:", not_found, flush=True)

# Process with 2 workers (rate limiter handles actual pacing)
progress = {"updated": 0, "skipped": 0, "failed": 0, "errors": []}
completed = 0
start = time.time()

with ThreadPoolExecutor(max_workers=2) as ex:
    futures = [ex.submit(process_topic, w) for w in work]
    for fut in as_completed(futures):
        result = fut.result()
        status = result[0]
        progress[status] = progress.get(status, 0) + 1
        if status == "failed":
            progress["errors"].append((result[1], result[2], result[3], str(result[4])[:200]))
        completed += 1
        elapsed = time.time() - start
        rate = completed / elapsed if elapsed > 0 else 0
        eta = (len(work) - completed) / rate if rate > 0 else 0
        print(f"  [{completed}/{len(work)}] {status}={progress['updated']}/{progress['skipped']}/{progress['failed']} | {rate:.2f}/s | ETA {eta:.0f}s | {result[3]} {result[4]}", flush=True)
        # Save progress after each topic
        json.dump(progress, open(f"/tmp/sync_progress.json", "w"))

elapsed = time.time() - start
print(f"\nDONE in {elapsed:.0f}s: upd={progress['updated']} skip={progress['skipped']} fail={progress['failed']}", flush=True)
json.dump(progress, open("/tmp/sync_done.json", "w"))
if progress["errors"][:5]:
    print("First errors:")
    for e in progress["errors"][:5]:
        print(f"  Ch {e[0]}.{e[1]} {e[2]}: {e[3][:150]}")
