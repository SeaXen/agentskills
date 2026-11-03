---
name: hub-conversion-pattern
description: Workflow for batch-converting scaffold-hub files to full-fcps-mrcp-hub status programmatically. Distilled from the Diabetes Ch25 session where 53 hub files were upgraded in one session using a single execute_code script.
---

# Hub Conversion Pattern (scaffold-hub → full-fcps-mrcp-hub)

## When to use this pattern
- A chapter folder has hub files (heading hubs + topic-group hubs) at `status: scaffold-hub`
- Disease-level notes are already at `full-fcps-mrcp-note` (200+ files complete)
- The task is to upgrade all hubs to `full-fcps-mrcp-hub` with proper frontmatter, child links, and high-yield tables
- Hubs are small (2-5 KB), don't need MCQs/SBAs/flashcards — perfect for programmatic generation

## The Approach (Single execute_code Script)

**Advantages over subagents:**
- No stream-timeout risk (small files, single write per file)
- Deterministic, no subagent self-report inflation
- Completes 50+ files in ~3 seconds wall time
- Preserves existing high-yield tables from scaffold content

## Script Template

```python
from pathlib import Path
import re
from datetime import date

base = Path("/mnt/tb/Medicine/<CHAPTER>")
today = date.today().isoformat()

def upgrade_hub(hub_path, title, children):
    """Upgrade a scaffold-hub to full-fcps-mrcp-hub"""
    content = hub_path.read_text(errors='replace')
    rel = hub_path.relative_to(base)
    depth = len(rel.parts) - 1
    
    if depth == 0:
        level = "Heading"; hub_type = "heading-hub"
    elif depth == 1:
        level = "Topic-Group"; hub_type = "topic-group-hub"
    else:
        level = "Topic-Group"; hub_type = "topic-group-hub"
    
    # Extract existing high-yield table if present
    high_yield = ""
    table_match = re.search(r'(\| Topic \| Key Facts \|[\s\S]*?)(?:\n---|\n## |\Z)', content)
    if not table_match:
        table_match = re.search(r'(\| Aspect \| Details \|[\s\S]*?)(?:\n---|\n## |\Z)', content)
    if table_match:
        high_yield = table_match.group(1).strip()
    
    # Build children markdown (wikilinks to disease notes)
    children_md = ""
    for child in children:
        child_path = None
        for ff in base.rglob("*.md"):
            if ff.stem == child:
                child_path = ff.relative_to(base)
                break
        if child_path:
            link = f"[[{child_path}|{child}]]"
        else:
            link = f"[[{child}]]"
        children_md += f"- {link}\n"
    
    # Parent links
    parent_links = ""
    if depth == 0:
        parent_links = "- **Parent**: [[Diabetes MOC|Diabetes MOC]]\n"
    elif depth == 1:
        parent_links = f"- **Parent Heading**: [[../{rel.parts[0]}|{rel.parts[0]}]]\n"
    elif depth == 2:
        parent_links = f"- **Parent Heading**: [[../../{rel.parts[0]}|{rel.parts[0]}]]\n"
        parent_links += f"- **Parent Topic-Group**: [[../{rel.parts[1]}|{rel.parts[1]}]]\n"
    
    # New frontmatter
    new_frontmatter = f"""---
tags: [medicine, diabetes, davidson, {hub_type}, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 25: Endocrinology and Diabetes
heading: {heading_val}
topic_group: {topic_group_val}
topic: {topic_val}
status: full-fcps-mrcp-hub
priority: HIGH
cards: {len(children) * 2}
created: {today}
modified: {today}
exam_relevance: "FCPS/MRCP High Yield - {title} core heading; covers {len(children)} disease-level topics; viva questions on classification, diagnosis, management algorithms, complications"
see_also:
  - "[[Diabetes MOC]]"
  - "[[Davidson Chapter 25 - Diabetes Hierarchy|Diabetes Hierarchy]]"
  - "[[../Templates/Diabetes Topic Template|Diabetes Topic Template]]"
---
"""
    
    # Hub content template
    hub_content = f"""# {title}

> [!info]
> {level} hub for **{title}** — covers {len(children)} disease-level topic(s) per Davidson Ch25.
>
> Related: [[Diabetes MOC]] · [[Davidson Chapter 25 - Diabetes Hierarchy|Diabetes Hierarchy]]

## Disease-Level Topics

{children_md}
---

## High-Yield Exam Points (FCPS/MRCP)

{high_yield if high_yield else "| Topic | Key Facts |\n|-------|-----------|\n| *See individual disease-level notes for detailed high-yield facts* | *Each child topic contains comprehensive FCPS/MRCP exam content* |"}

---

## Quick Links

{parent_links}- **Chapter MOC**: [[../../Diabetes MOC|Diabetes MOC]]
- **Chapter Hierarchy**: [[../../Davidson Chapter 25 - Diabetes Hierarchy|Diabetes Hierarchy]]
- **Topic Template**: [[../../Templates/Diabetes Topic Template|Diabetes Topic Template]]
- **Drug Reference**: [[../../Clinical Therapeutics and Good Prescribing|Drugs]]

---

## Tags

#medicine #diabetes #davidson #{hub_type} #fcps #mrcp
"""
    
    # Replace content (preserve nothing from scaffold)
    if content.startswith("---"):
        end_fm = content.find("---", 3)
        if end_fm > 0:
            new_content = new_frontmatter + hub_content
            hub_path.write_text(new_content)
            return True
    return False

# Main loop: find all scaffold-hub files and upgrade
converted = 0
for f in base.rglob("*.md"):
    content = f.read_text(errors='replace')
    if "status: scaffold-hub" in content:
        rel = f.relative_to(base)
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else f.stem
        
        children = re.findall(r'^- \[\[([^\]|]+)(?:\|([^\]]+))?\]\]$', content, re.MULTILINE)
        child_names = [c[1] if c[1] else c[0] for c in children]
        
        if upgrade_hub(f, title, child_names):
            converted += 1
            print(f"  Converted: {rel}")
        else:
            print(f"  Failed: {rel}")

print(f"Total converted: {converted}")
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Single `execute_code` call | Hubs are small (2-5 KB); no timeout risk; deterministic |
| Preserve existing high-yield tables | Scaffolds often have curated exam tables worth keeping |
| Auto-discover child file paths | Avoids hardcoding; works even if folder structure differs |
| Depth-based frontmatter (heading/topic_group/topic) | Enables proper MOC/hierarchy navigation and Dataview queries |
| Cards = children * 2 | Consistent with FCPS/MRCP template convention |
| No subagents | Simpler, faster, no context-inheritance issues |

## Verification After Conversion

```bash
# 1. Confirm all hubs upgraded
grep -r "status: full-fcps-mrcp-hub" /mnt/tb/Medicine/<CHAPTER>/ --include="*.md" | wc -l
# Should equal expected hub count

# 2. Confirm zero scaffolds remain
grep -r "status: scaffold-hub" /mnt/tb/Medicine/<CHAPTER>/ --include="*.md" || echo "None remain"

# 3. Run chapter verification script
python3 ~/.hermes/skills/medical-study/medical-fcps-mrcp-note-creation/scripts/chapter_verify.py /mnt/tb/Medicine/<CHAPTER> <expected_disease_count>
```

## When NOT to use this pattern

- If hubs need substantial new clinical content (not just structure + existing tables) → subagents may be better
- If there are >200 hubs → consider chunking, though single script still handles it
- If chapter topic structure is entirely different from Diabetes → adapt the template strings (heading names, chapter number, etc.)

## Related Patterns

- **Scaffold → Full disease notes**: Use subagents + `references/scaffold-to-full-template-batch-conversion.md`
- **Hub conversion** (this pattern): Use single `execute_code` script
- **MOC upgrade**: Manual `patch` on frontmatter + progress table update
- **Progress tracker update**: Manual `patch` on `00_Index/Davidson Chapter Progress Tracker.md`

## Time/Scale

- Diabetes Ch25: 53 hubs → 3 seconds, 100% success
- Expected for typical chapter (8-15 heading hubs, 20-50 topic-group hubs): <5 seconds
- Zero token cost beyond the execute_code call itself (no LLM calls for generation)