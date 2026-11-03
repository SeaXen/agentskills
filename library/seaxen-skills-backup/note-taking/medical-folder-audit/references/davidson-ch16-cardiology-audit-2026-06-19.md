# Davidson Ch 16 Cardiology Audit — 2026-06-19

## Context
User asked: *"all of my cardiology topic in there with all information or anything missing, just check and give report"*

User's framing: 3 systems — apps/website (Docker port 8855 + Vercel), Notion, GitHub repo `SeaXen/MedSea`. The user was in `/mnt/tb/Medicine/` context, but the agent initially went to `/mnt/tb/Sea-knowledge/` (the GitHub-mirrored render path). User corrected: *"I mean medicine note from /mnt/tb/medicine"*.

## What the Audit Found
- **Path**: `/mnt/tb/Medicine/Cardiology/` (Davidson 24e Ch 16)
- **Total .md files**: 842
  - 682 `full-fcps-mrcp-note` (real content)
  - 145 `scaffold-hub` (navigation)
  - 11 `starter-note` (empty ~3.7 KB stubs at root — legacy from May 6)
  - 1 `full-note` (legacy `Heart Failure.md`, 42.8 KB)
  - 1 `template`, 1 `disease-level-scaffold` (hierarchy), 1 no-frontmatter
- **Hierarchy target**: 220 disease topics + 16 heading hubs + 85 topic groups
- **Actual in numbered folders**: 570 full notes (259% coverage — every section ≥125%)
- **Word count**: ~962K total in numbered folders, avg 1,687 words/note

## Three Pitfalls Discovered (now in SKILL.md)

### Pitfall #21 — Confirm source-of-truth directory
The `/mnt/tb/Sea-knowledge/` vs `/mnt/tb/Medicine/` naming overlap causes routing confusion. `/mnt/tb/Sea-knowledge/` is the render pipeline (used by website/Vercel/GitHub); `/mnt/tb/Medicine/` is the Obsidian study source. When user mentions "cardiology" without specifying, ask. When user mentions "apps/website + Notion + git", clarify which is the audit target.

### Pitfall #23 — Numbered vs legacy folder duplication
Two parallel folder structures exist:
- `01_Cardiac_Investigations/`, ..., `16_Cardiac_Emergencies/` — 570 full notes (canonical)
- `Clinical Assessment, Hemodynamics, and Cardiac Investigations/`, `Heart Failure and Acute Cardiac Decompensation/`, ... — 111 full notes (legacy, shorter)

Recommendation: delete the legacy long-named folders. Don't auto-delete; flag in report.

### Pitfall #24 — Format compliance is a separate dimension
- Content complete: 100% ✅
- Mermaid diagrams: 10% (74/570) ⚠️
- Markdown tables: 3% (26/570) ⚠️
- Differential dx: 84%
- Mnemonics: 87%

Cardiology has 100% content but only 10% Mermaid/3% tables — pure prose. Hierarchy rules require both. This gap is invisible to "is it complete?" audits but matters for exam-readability.

## Three-Source Sync Status

| Source | Mirrors | Sync mechanism |
|---|---|---|
| `/mnt/tb/Medicine/Cardiology/` (study source) | none — itself | manual editing |
| GitHub `SeaXen/MedSea` | `/mnt/tb/Sea-knowledge/`, NOT `/mnt/tb/Medicine/` | cron runs `scripts/sync.sh` |
| Notion searex share | unclear | none observed |
| Vercel (port 8855) | `/mnt/tb/Sea-knowledge/` site/ | static deploy |

**Conclusion:** `/mnt/tb/Medicine/Cardiology/` is NOT mirrored to GitHub, Notion, or Vercel. Only `/mnt/tb/Sea-knowledge/` has a backup pipeline.

## MOC Lag (Pitfall #25)
- MOC claimed: 570 notes / 549 real / 6 stubs / 115 hubs = 679 total
- Disk reality: 682 full / 11 starter stubs / 145 hubs = 838 total
- MOC last updated: 2026-06-16 (3 days stale)

## Recommendations Issued to User
1. Delete 11 starter-note stubs at root
2. Delete or merge 10 legacy long-named folders
3. Add Mermaid + tables to existing prose notes (biggest upgrade)
4. Refresh `Cardiology MOC.md` progress table
5. Decide if `/mnt/tb/Medicine/Cardiology/` should also mirror to GitHub

## Final Verdict
**Content-wise: 10/10** (220/220 topics, 0 missing, dense medical prose)
**Format-wise: 7.5/10** (low Mermaid/table compliance, 11 dead stubs)

## Detection Snippets That Worked

```python
# Status frontmatter distribution
def count_statuses(base):
    counts = {}
    for md in Path(base).rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="ignore")
        for line in text.split("\n")[:30]:
            if line.startswith("status:"):
                v = line.split(":", 1)[1].strip()
                counts[v] = counts.get(v, 0) + 1
                break
    return counts

# Numbered vs legacy folder classification
def is_numbered(rel_path):
    return bool(re.match(r'^\d{2}_', rel_path.parts[0]))

# Format compliance (mermaid, tables, mnemonics)
def format_score(text):
    return {
        "mermaid": "```mermaid" in text,
        "table": "|---|" in text or "| --- |" in text,
        "mnemonic": "Mnemonic" in text or "mnemonic" in text.lower(),
        "mcq": "MCQ" in text,
        "sba": "SBA" in text,
        "viva": "Viva" in text,
    }

# MOC vs disk delta
def report_moc_lag(moc_path, base):
    moc = open(moc_path).read()
    m = re.search(r"\*\*TOTAL\*\*.*?\*\*(\d+)\*\*", moc)
    claimed = int(m.group(1)) if m else None
    disk = sum(1 for _ in Path(base).rglob("*.md"))
    return claimed, disk, disk - (claimed or 0)
```

## User Feedback After This Audit
User accepted the report. No corrections to style. Session ended cleanly with recommendations offered (delete stubs, add Mermaid, refresh MOC).