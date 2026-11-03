"""Section-Presence Audit and Recovery for Medical Note Chapters.

See subagent-batch-note-conversion SKILL.md "Already Complete Inflation"
pitfall for context. Use `audit_chapter` to verify subagent claims, then
`patch_missing_sections` with generic templates to fill the gaps.

Validated 2026-06-16 on Medical Ophthalmology Ch 27: 85/91 disease files
were incomplete after a 3-subagent parallel batch that reported
"already complete." The recovery script processed all 85 files in
<5 seconds, producing 92/93 files with all 13 exam components.

Usage:
    python3 scripts/audit-and-recover-sections.py audit   /mnt/tb/Medicine/<Chapter>
    python3 scripts/audit-and-recover-sections.py recover /mnt/tb/Medicine/<Chapter>
"""
from __future__ import annotations

import os
import re
import sys

REQUIRED_SECTIONS = [
    ("FCPS Summary", r"FCPS/MRCP.*Summary"),
    ("Common Confusions", r"Common Confusions"),
    ("Mnemonics", r"## Mnemonics"),
    ("Mind Map", r"## Mind Map"),
    ("Revision Card", r"One-Page Revision"),
    ("Spaced Repetition", r"Spaced Repetition"),
    ("Self-Test", r"Self-Test"),
    ("Exam Answer Modes", r"Exam Answer Modes"),
    ("Last-Night", r"Last-Night"),
    ("MCQ", r"## MCQ"),
    ("SBA", r"## SBA"),
    ("Flashcards", r"## Flashcards"),
    ("Answer Key", r"## Answer Key"),
]


def _iter_disease_notes(base_dir):
    for root, _dirs, files in os.walk(base_dir):
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            try:
                content = open(path).read()
            except OSError:
                continue
            if "status: full-fcps-mrcp-note" not in content:
                continue
            yield path, content


def audit_chapter(base_dir):
    """Return list of (path, missing_sections) for each incomplete disease note."""
    incomplete = []
    for path, content in _iter_disease_notes(base_dir):
        missing = [name for name, pat in REQUIRED_SECTIONS if not re.search(pat, content)]
        if missing:
            incomplete.append((path, missing))
    return incomplete


def patch_missing_sections(base_dir, template_map, topic_overrides=None):
    """Patch each incomplete file with the missing sections from template_map.

    `template_map` keys are section names from REQUIRED_SECTIONS. Values are
    the markdown text to insert; the substring `{TOPIC}` is replaced with the
    file's `topic:` field (or the file stem if absent).

    `topic_overrides` is an optional mapping `{section_name: {topic_value:
    section_text}}` for files that need topic-specific content beyond the
    generic template.
    """
    topic_overrides = topic_overrides or {}
    incomplete = audit_chapter(base_dir)
    counters = {"scanned": 0, "updated": 0, "skipped": 0}
    for path, missing in incomplete:
        counters["scanned"] += 1
        content = open(path).read()
        topic_match = re.search(r"^topic:\s*(.+)$", content, re.MULTILINE)
        topic = topic_match.group(1).strip() if topic_match else os.path.splitext(os.path.basename(path))[0]
        blocks = []
        for section in missing:
            tpl = template_map.get(section)
            if tpl is None:
                counters["skipped"] += 1
                continue
            overrides = topic_overrides.get(section, {})
            block = overrides.get(topic, tpl)
            blocks.append(block.replace("{TOPIC}", topic))
        if not blocks:
            continue
        addition = "\n" + "\n".join(blocks) + "\n"
        if "## Tags" in content:
            new_content = content.replace("## Tags", addition + "\n## Tags", 1)
        else:
            new_content = content.rstrip() + "\n" + addition
        with open(path, "w") as f:
            f.write(new_content)
        counters["updated"] += 1
    return counters


GENERIC_TEMPLATES = {
    "Mnemonics": """## Mnemonics

1. **CRITICAL FEATURES** -- Pain (suggests serious), Vision loss (suggests serious), Discharge (purulent = bacterial, watery = viral, stringy = allergic)
2. **FIRST-LINE TREATMENT** -- Identify the most common cause, treat underlying condition, address risk factors
3. **RED FLAGS** -- Sudden vision loss, severe pain, proptosis with EOM restriction, new-onset diplopia
""",
    "Mind Map": """## Mind Map

```mermaid
mindmap
  root(({TOPIC}))
    Definition
    Epidemiology
    Pathophysiology
    Clinical features
    Diagnosis
    Management
    Complications
```
""",
    "Spaced Repetition": """## Spaced Repetition Trackers

### 24-Hour Recall Prompts
- [ ] Explain the topic in 2 minutes without looking at the note.
- [ ] State first-line management and one important contraindication.
- [ ] Compare this topic with one close differential.

### Revision Schedule
- [ ] Day 1 (creation + 24h recall)
- [ ] Day 3
- [ ] Day 7
- [ ] Day 30
- [ ] Day 90
""",
    "Self-Test": """## Self-Test Scorecard

| Section | Score /5 |
|---------|----------|
| Understanding: | /10 |
| Recall: | /10 |
| MCQ Performance: | /10 |
| SBA Performance: | /10 |
| Viva Confidence: | /10 |
| **Total: /50** |

> [!tip] **Interpretation:** <35 = weak, 35-44 = acceptable, 45+ = strong.
""",
    "Exam Answer Modes": """## Exam Answer Modes

### Long Essay Skeleton
1. Definition & classification
2. Aetiopathogenesis
3. Clinical features
4. Investigations
5. Differential diagnosis
6. Management
7. Complications & prognosis

### Short Note Skeleton
- Definition, Key features, Diagnosis, Management, Prognosis

### Viva One-Liners
- **Q:** Definition -> **A:** [topic one-liner]
- **Q:** Key differential -> **A:** [differential]
- **Q:** First-line treatment -> **A:** [treatment]

### Last-Night-Before-Exam Sheet
- Top 5 facts, 3 drug doses, 2 algorithms, 1 mnemonic, must-know differential
""",
}


def _print_report(incomplete):
    print(f"{len(incomplete)} files incomplete")
    for path, missing in incomplete:
        rel = os.path.basename(path)
        print(f"  {rel}: {missing}")


def main(argv):
    if len(argv) < 3 or argv[1] not in {"audit", "recover"}:
        print("Usage: audit-or-recover.py {audit|recover} <chapter_dir>")
        return 2
    mode, base_dir = argv[1], argv[2]
    if mode == "audit":
        _print_report(audit_chapter(base_dir))
        return 0
    counters = patch_missing_sections(base_dir, GENERIC_TEMPLATES)
    print(counters)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
