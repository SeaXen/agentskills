# Davidson 24th → 25th Edition Chapter Mapping

The source at `/mnt/tb/Medicine/` is **Davidson 24th Edition** (folder names match).
The target structure (local, Notion, site, git) uses **Davidson 25th Edition** numbers.
The chapter NUMBERS change between editions even though most topic content is similar.

## Chapter Number Mapping (24th → 25th Ed)

| 24th Ed | 25th Ed | Title (25th Ed) | Slug |
|---------|---------|-----------------|------|
| 1 | 1 | Clinical decision-making | 1-clinical-decision-making |
| 2 | 2 | Clinical therapeutics and good prescribing | 2-clinical-therapeutics |
| 3 | 3 | Clinical genetics | 3-clinical-genetics |
| 4 | 4 | Clinical immunology | 4-clinical-immunology |
| 5 | 5 | Nutritional factors in disease | 5-nutritional-factors |
| 6 | 6 | Population health and epidemiology | 6-population-health |
| 7 | 7 | Principles of infection | 7-principles-of-infection |
| 8 | 8 | Oncology | 8-oncology |
| 9 | 9 | Palliative and supportive care | 9-palliative-care |
| 10 (24th) | 10 | Acute medicine and critical illness | 10-acute-medicine |
| 7 (24th) | 11 | Poisoning | 11-poisoning |
| (24th Envenomation) | 12 | Envenomation | 12-envenomation |
| (24th Environmental) | 13 | Medicine in austere environments | 13-austere-medicine |
| (24th Infectious) | 14 | Infectious disease | 14-infectious-disease |
| (24th STI) | 15 | Sexually transmitted infections | 15-sexually-transmitted-infections |
| 17 (24th) | 16 | Cardiology | 16-cardiology |
| 18 (24th) | 17 | Respiratory medicine | 17-respiratory-medicine |
| 15 (24th) | 18 | Nephrology and urology | 18-nephrology-urology |
| (24th Biochemistry) | 19 | Clinical biochemistry and metabolic medicine | 19-... (not yet built) |
| 18 (24th Endo) | 20 | Endocrinology | 20-endocrinology |
| (24th Diabetes) | 21 | Diabetes mellitus | 21-... (not yet built) |
| 21 (24th) | 22 | Gastroenterology | 22-gastroenterology |
| (24th Hepatology) | 23 | Hepatology | 23-... (not yet built) |
| (24th Haematology) | 24 | Haematology and transfusion medicine | 24-... (not yet built) |
| (24th Rheumatology) | 25 | Rheumatology and bone disease | 25-... (not yet built) |
| (24th Dermatology) | 26 | Dermatology | 26-... (not yet built) |
| (24th Neurology) | 27 | Neurology and stroke medicine | 27-... (not yet built) |
| (24th Ophthalmology) | 28 | Medical ophthalmology | 28-... (not yet built) |
| (24th Psychiatry) | 29 | Medical psychiatry | 29-... (not yet built) |
| (24th Obstetric) | 30 | Maternal medicine | 30-... (not yet built) |
| (24th Adolescent) | 31 | Adolescence, transition and young adult medicine | 31-... (not yet built) |
| (24th Geriatric) | 32 | Older adult medicine and frailty | 32-... (not yet built) |
| (n/a) | 33 | Laboratory reference ranges | (appendix) |

## Source Folder Names in /mnt/tb/Medicine/

The 24th Ed source uses different folder names than the chapter number. Examples:

| 25th Ed Ch | 25th Ed Title | Source folder in /mnt/tb/Medicine/ |
|---|---|---|
| 10 | Acute medicine and critical illness | `Acute Medicine and Critical Illness/` |
| 11 | Poisoning | `Chapter 7 - Poisoning/` |
| 12 | Envenomation | `Envenomation/` |
| 13 | Medicine in austere environments | `Environmental medicine/` |
| 14 | Infectious disease | `Infectious Disease/` |
| 15 | Sexually transmitted infections | `Sexually Transmitted Infections/` |
| 16 | Cardiology | `Cardiology/` |
| 17 | Respiratory medicine | `Respiratory Medicine/` |
| 18 | Nephrology and urology | `Nephrology and Urology/` |
| 20 | Endocrinology | `Endocrinology/` |
| 22 | Gastroenterology | `Gastroenterology/` |

**When building a chapter, the `src_subdir` in `build_chapter.py` must use the 24th Ed source folder name, NOT the 25th Ed chapter number.**

## Renaming Pattern

When the 25th Ed renumbering changes a chapter number from 24th to 25th:

1. **Local folder rename**: `git mv` (or filesystem rename) — but be careful, the OLD folder may be left empty by git as a "ghost directory"
2. **MedSea folder rename**: same as local
3. **DAVIDSON_25TH list** in `build_site.py` — update slug
4. **BUILT_CHAPTERS dict** in `build_site.py` — update key, Notion URL
5. **Notion page** — Notion API CANNOT reparent child_page blocks. The old chapter page keeps its sub-pages. Workaround: add a redirect notice to the OLD page pointing to the NEW page.

## Ghost Directory Cleanup

After `git mv` rename, the old directory may persist as empty subdirs. Clean up with `rmdir` (NOT `rm -rf` — that's destructive and will be blocked by safety):

```bash
cd /mnt/tb/Sea-knowledge/#MedSea/chapters
# Verify empty first
ls -la 15-nephrology-urology/
# If all subdirs are empty:
rmdir 15-nephrology-urology/diseases/15.1.1-.../  # remove deepest first
rmdir 15-nephrology-urology/diseases
rmdir 15-nephrology-urology/hubs
rmdir 15-nephrology-urology/source
rmdir 15-nephrology-urology
```

## Notion Cardiology Move (25th Ed Case Study)

Ch 17 (24th Ed Cardiology) → Ch 16 (25th Ed Cardiology). The MedSea page IDs:

- OLD: `3825588e-846f-80cb-b9ee-c8ea437594bc` (page slug `cardiology-...`)
- NEW: `8baa010d-9cc9-4c48-8261-36417d383973` (page slug `Chapter-16-Cardiology-...`)

The Notion API allowed creating a NEW page in the MedSea DB with the new title. It did NOT allow reparenting the OLD page's child_page blocks (hubs, topics) to the NEW page. **Final state**: NEW page is empty with a redirect callout at top, OLD page retains all sub-pages.

**User-visible result**: clicking the Notion link for "Chapter 16: Cardiology" goes to a page that has the content; clicking the 25th Ed Davidson reference goes to an empty page with a redirect.

## Color Coding per Chapter (in BUILT_CHAPTERS)

```python
"1-clinical-decision-making": (... "#64748b"),  # slate
"2-clinical-therapeutics":    (... "#0ea5e9"),  # sky
"3-clinical-genetics":        (... "#84cc16"),  # lime
"4-clinical-immunology":      (... "#f97316"),  # orange
"5-nutritional-factors":      (... "#eab308"),  # yellow
"6-population-health":        (... "#14b8a6"),  # teal
"7-principles-of-infection":  (... "#dc2626"),  # red
"8-oncology":                 (... "#7c3aed"),  # violet
"9-palliative-care":          (... "#be185d"),  # pink
"10-acute-medicine":          (... "#f43f5e"),  # rose
"11-poisoning":               (... "#84cc16"),  # lime
"12-envenomation":            (... "#22c55e"),  # green
"13-austere-medicine":        (... "#0d9488"),  # dark teal
"14-infectious-disease":      (... "#0891b2"),  # cyan
"15-sexually-transmitted-infections": (... "#7c3aed"),  # violet
"16-cardiology":              (... "#ef4444"),  # red
"17-respiratory-medicine":    (... "#10b981"),  # emerald
"18-nephrology-urology":      (... "#06b6d4"),  # cyan
"20-endocrinology":           (... "#a855f7"),  # purple
"22-gastroenterology":        (... "#f59e0b"),  # amber
```
