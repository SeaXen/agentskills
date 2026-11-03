# Notion Special-Case Handlers

When the regular match-and-append loop leaves 1-5 topics unmatched (title mismatches, missing pages), handle them with these patterns.

## Pattern 1: Append to existing page with title mismatch

When the topic EXISTS in Notion but the title doesn't match MedSea's slug. E.g. Ch 14.1.55 source = "Pneumocystis Pneumonia (PCP)" → Notion has "Pneumocystis Pneumonia (PCP / PJP)" with parens breaking the `title_lc in t` check.

```python
# Find the existing page by partial match
pneumocystis_page_id = None
for hub_id, hub_title in hubs:
    topics = get_children(hub_id)
    for tid, ttitle in topics:
        if "pneumocystis" in ttitle.lower():
            pneumocystis_page_id = tid
            break
    if pneumocystis_page_id:
        break

# Append MedSea content (no header — the page title already has it)
content = Path("/mnt/tb/Sea-knowledge/#MedSea/chapters/14-infectious-disease/diseases/14.1.55-pneumocystis-pneumonia-pcp/topic.md").read_text()
blocks = md_to_blocks(content, with_header=True)  # divider + callout marks it as new
for i in range(0, len(blocks), 100):
    r = http("PATCH", f"https://api.notion.com/v1/blocks/{pneumocystis_page_id}/children", {"children": blocks[i:i+100]})
    if "_error" in r: print("Failed:", r); break
```

## Pattern 2: Create new page under a hub (for topics missing from Notion)

When the topic is in MedSea but Notion never had it. Find the hub by listing children, then POST a new page with title and an initial callout.

```python
# Find the hub for Ch 15.3
hubs = get_children("19c59a0895cd4ea4bee4e69d90ce37c8")  # Ch 15 root
hub_15_3 = next(h for hid, h in hubs if "15.3" in h)
# hub_15_3[0] = page_id, hub_15_3[1] = "15.3 Hub 3"

# Create the new page
title = "15.3.06 Syphilis Serology Interpretation (VDRL/RPR, TPHA/FTA-ABS)"
create_r = http("POST", "https://api.notion.com/v1/pages", {
    "parent": {"type": "page_id", "page_id": hub_15_3[0]},
    "properties": {"title": [{"type": "text", "text": {"content": title}}]},
    "children": [
        {"object": "block", "type": "callout", "callout": {
            "rich_text": [{"type": "text", "text": {"content": "📘 MedSea 100% Content — new page created to ensure 100% coverage."}}],
            "icon": {"type": "emoji", "emoji": "📘"},
            "color": "blue_background"
        }}
    ]
})
new_page_id = create_r["id"]

# Append content (with_header=False since the callout is already in the page)
content = Path("/mnt/tb/Sea-knowledge/#MedSea/chapters/15-sexually-transmitted-infections/diseases/15.3.06-syphilis-serology-interpretation/topic.md").read_text()
blocks = md_to_blocks(content, with_header=False)
for i in range(0, len(blocks), 100):
    r = http("PATCH", f"https://api.notion.com/v1/blocks/{new_page_id}/children", {"children": blocks[i:i+100]})
    if "_error" in r: print("Failed:", r); break
```

## How to find a topic's hub ID for creating under it

The MedSea topic dir name like `15.3.06-syphilis-serology-interpretation` tells you:
- Ch 15 (chapter)
- 3 (hub number)  
- 06 (topic number in hub)

The Notion hub for that is the page titled `15.3 Hub 3` under the chapter root. Search by `re.match(rf"^{ch}\.{hub_num}\.?\s*", title)` on the chapter's direct children.

## Pitfall: page title with parens or extra suffixes

Common mismatches that broke the simple `title_lc in t` check:
- `(PCP / PJP)` suffix when source says just `(PCP)`
- Trailing dash characters (`- ` at end of title)
- Em-dash vs hyphen (— vs -)
- Numbered prefixes in source but not Notion

For each unmatched topic, FIRST check if the page exists by searching the hub with looser matching (`any(t in ttitle.lower() or ttitle.lower() in t for t in candidate_slugs)`), THEN fall back to create-new.
