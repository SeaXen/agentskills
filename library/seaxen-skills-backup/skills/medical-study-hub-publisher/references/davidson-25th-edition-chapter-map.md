# Davidson 25th Edition Chapter Map (2026-06-19)

When the user asks to **adopt Davidson 25th Edition chapter numbering** for a content tree originally organized by 24th Edition (e.g. `/mnt/tb/Medicine/`), this file is the source of truth for the renames.

## Affected renames (24th → 25th)

| 24th Ed folder name                | 24th Ed # | 25th Ed # | 25th Ed title                  | Notes                                |
|------------------------------------|-----------|-----------|----------------------------------|--------------------------------------|
| Cardiology                         | 16        | **16**    | Cardiology                       | Number unchanged                     |
| Respiratory                        | 17        | **17**    | Respiratory medicine             | Number unchanged, title refines      |
| Nephrology and Urology              | 15        | **18**    | Nephrology and urology           | Renumbered up                        |
| Endocrinology                      | 18        | **20**    | Endocrinology                    | Renumbered up                        |
| Gastroenterology                   | 21        | **22**    | Gastroenterology                 | Renumbered up                        |

## Full 32-chapter canonical list (Davidson 25th Ed)

Use this in the `DAVIDSON_25TH` table of `build_site.py` for the chapter dropdown. The display number (1-32) is the 25th Ed number; the slug is the on-disk folder name (must match the chapter folder exactly).

```python
DAVIDSON_25TH = [
    (1,  "Clinical decision-making",                       "1-clinical-decision-making"),
    (2,  "Clinical therapeutics and good prescribing",     "2-clinical-therapeutics"),
    (3,  "Clinical genetics",                              "3-clinical-genetics"),
    (4,  "Clinical immunology",                            "4-clinical-immunology"),
    (5,  "Nutritional factors in disease",                 "5-nutritional-factors"),
    (6,  "Population health and epidemiology",             "6-population-health"),
    (7,  "Principles of infection",                        "7-principles-of-infection"),
    (8,  "Oncology",                                       "8-oncology"),
    (9,  "Palliative and supportive care",                 "9-palliative-care"),
    (10, "Acute medicine and critical illness",            "10-acute-medicine"),
    (11, "Poisoning",                                      "11-poisoning"),
    (12, "Envenomation",                                   "12-envenomation"),
    (13, "Medicine in austere environments",               "13-austere-medicine"),
    (14, "Infectious disease",                             "14-infectious-disease"),
    (15, "Sexually transmitted infections",                "15-sexually-transmitted-infections"),
    (16, "Cardiology",                                     "16-cardiology"),
    (17, "Respiratory medicine",                           "17-respiratory-medicine"),
    (18, "Nephrology and urology",                         "18-nephrology-urology"),
    (19, "Clinical biochemistry and metabolic medicine",   None),
    (20, "Endocrinology",                                  "20-endocrinology"),
    (21, "Diabetes mellitus",                              None),
    (22, "Gastroenterology",                               "22-gastroenterology"),
    (23, "Hepatology",                                     None),
    (24, "Haematology and transfusion medicine",           None),
    (25, "Rheumatology and bone disease",                  None),
    (26, "Dermatology",                                    None),
    (27, "Neurology and stroke medicine",                  None),
    (28, "Medical ophthalmology",                          None),
    (29, "Medical psychiatry",                             None),
    (30, "Maternal medicine",                              None),
    (31, "Adolescence, transition and young adult medicine", None),
    (32, "Older adult medicine and frailty",               None),
]
```

## Rename batch (do all 4 in one go)

```bash
# 1. Local chapter folders under /mnt/tb/Sea-knowledge/
cd /mnt/tb/Sea-knowledge
mv "15. Nephrology and Urology" "18. Nephrology and Urology"
mv "17. Respiratory" "17. Respiratory Medicine"
mv "18. Endocrinology" "20. Endocrinology"
mv "21. Gastroenterology" "22. Gastroenterology"

# 2. MedSea backup repo (chapters/ + site/ trees, use git mv for tracked files)
cd /mnt/tb/Sea-knowledge/#MedSea
git mv chapters/15-nephrology-urology      chapters/18-nephrology-urology
git mv chapters/18-endocrinology          chapters/20-endocrinology
git mv chapters/21-gastroenterology       chapters/22-gastroenterology
git mv site/15-nephrology-urology         site/18-nephrology-urology
git mv site/18-endocrinology              site/20-endocrinology
git mv site/21-gastroenterology           site/22-gastroenterology
```

## After the renames — sync these files

1. **`scripts/site/build_site.py`** — update both `DAVIDSON_25TH` and `BUILT_CHAPTERS`:
   - Change the slugs in `BUILT_CHAPTERS` keys: `"15-nephrology-urology"` → `"18-nephrology-urology"`, etc.
   - Change the Notion URLs in `BUILT_CHAPTERS` values to the new chapter root page IDs (only if the user has created the new Notion root pages).
   - Update the `display_num` for built chapters: the chapter number in the `BUILT_CHAPTERS` dict is derived from the slug prefix (`ch_slug.split("-")[0]`), so renaming the folder is enough for the site to show the new number in cards — no code change needed for that part.

2. **Notion** — the user has new root pages for the renumbered chapters. Update the `BUILT_CHAPTERS` Notion URLs to point to the new page IDs. For chapters whose number didn't change (Cardiology 16, Respiratory 17), the user may have a NEW chapter-specific root page they want to use instead of the old topic-tree root.

3. **GitHub** — commit the renamed folders + the updated `build_site.py` + the site rebuild, then push.

## Verification (mandatory after renames)

```bash
# All chapter folders should match the new naming
ls /mnt/tb/Sea-knowledge/ | sort   # should show 18, 20, 22 — NOT 15, 18, 21
ls /mnt/tb/Sea-knowledge/'#MedSea'/chapters/ | sort   # same

# Site should rebuild with 14+ chapters, all PNGs present
cd /mnt/tb/Sea-knowledge/#MedSea && python3 scripts/site/build_site.py
# Look for: "Wrote index.html (N topics across M chapters)" — N should match
# the total across all built chapters (1287+ for Ch 1-9 + 15-18 + 20-22)

# Docker image should rebuild and restart
docker build -t medsea-site:latest .
docker stop medsea && docker rm medsea
docker run -d --name medsea --restart unless-stopped -p 8855:8855 medsea-site:latest

# Browser sanity check
curl -s http://localhost:8855/ | grep -oE 'Ch [0-9]+' | sort -u
# Should show: 1, 2, 3, 4, 5, 6, 7, 8, 9, 16, 17, 18, 20, 22 (only the built ones)
```

## Notion move caveat (Pitfall 76)

For chapters whose **number didn't change** but whose user-facing URL did (Cardiology 16, Respiratory 17), the user may want the topics physically moved from the old root page to a new "Chapter 16: Cardiology" root page. The Notion API cannot do this via `PATCH /v1/pages/{id}` for `child_page` blocks (Pitfall 76) — the move is silently ignored. Add a redirect callout to the old page OR re-upload the topics to the new root.

## Source-of-truth priority

When there's a conflict between chapter numbers in different sources, use this order:

1. **Davidson 25th Ed canonical list** (this file) — most authoritative
2. **User's explicit instruction** — overrides the canonical list if they say so
3. **Existing Notion root page IDs** — what the user has actually published
4. **Local chapter folder name** — derived from the canonical number, may be out of date

If a chapter number is in the source MDs (24th Ed) but the user wants 25th Ed, the canonical list wins. The local folder rename + `git mv` + `build_site.py` update + new Notion root are all required to make the change end-to-end consistent.

## Source: New lessons from 2026-06-19 session

The following additional pitfalls were identified while building Ch 10-15:

- **Pitfall 76**: Notion `PATCH /v1/pages/{id}` parent change is silently ignored for `child_page` blocks
- **Pitfall 78**: Renderer infinite loop on unnumbered `## 24-Hour Recall Prompts` headers
- **Pitfall 79**: Mermaid `mindmap` and `flowchart` blocks need custom rendering
- **Pitfall 80**: Renderer output is `out_dir/slug/slug.{png,md,html}` — TWO levels deep
