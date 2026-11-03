# Cardiology Chapter 16 — Study Hub Publisher Session Log
**Date:** 2026-06-17
**Chapter:** Davidson Chapter 16 — Cardiology
**Notion hub:** https://app.notion.com/p/cardiology-3825588e846f80cbb9eec8ea437594bc
**Local archive:** /mnt/tb/Sea-knowledge/ (16 topic folders, 7.4 MB total)
**Source:** /mnt/tb/Medicine/Cardiology/ (16 numbered sub-folders + top-level .md files)

## Topic list (Davidson Chapter 16, 16 major sections)

| # | Slug | Title | Source folder |
|---|---|---|---|
| 1 | cardiac-investigations | Cardiac Investigations | 01_Cardiac_Investigations/ |
| 2 | acute-coronary-syndromes | Acute Coronary Syndromes | 02_Acute_Coronary_Syndromes/ |
| 3 | chronic-coronary-syndromes | Chronic Coronary Syndromes | 03_Chronic_Coronary_Syndromes/ |
| 4 | heart-failure | Heart Failure | 04_Heart_Failure/ |
| 5 | valvular-heart-disease | Valvular Heart Disease | 05_Valvular_Heart_Disease/ |
| 6 | infective-endocarditis | Infective Endocarditis | 06_Infective_Endocarditis/ |
| 7 | pericardial-diseases | Pericardial Diseases | 07_Pericardial_Diseases/ |
| 8 | arrhythmias | Arrhythmias | 08_Arrhythmias/ |
| 9 | cardiac-devices-ep | Cardiac Devices & Electrophysiology | 08_Cardiac_Devices_EP/ |
| 10 | adult-congenital-heart-disease | Adult Congenital Heart Disease | 10_Adult_Congenital_Heart_Disease/ |
| 11 | pulmonary-hypertension | Pulmonary Hypertension | 11_Pulmonary_Hypertension/ |
| 12 | aortic-diseases | Diseases of the Aorta | 12_Aortic_Diseases/ |
| 13 | systemic-cardiac | Systemic Diseases & Cardiac Involvement | 13_Systemic_Cardiac/ |
| 14 | hypertension-cv-risk | Hypertension & Cardiovascular Risk | 14_Hypertension_CV_Risk/ |
| 15 | special-populations | Cardiac Disease in Special Populations | 15_Special_Populations/ |
| 16 | cardiac-emergencies | Cardiac Emergencies & Critical Care | 16_Cardiac_Emergencies/ |

## File sizes (md / html / png per topic)

| Topic | MD | PNG | PNG dims |
|---|---|---|---|
| acute-coronary-syndromes | 9,015 | 430,400 | 794x2042 |
| adult-congenital-heart-disease | 10,260 | 435,136 | 794x1712 |
| aortic-diseases | 9,399 | 436,618 | 794x2097 |
| arrhythmias | 8,824 | 384,856 | 794x1590 |
| cardiac-devices-ep | 9,433 | 409,204 | 794x1568 |
| cardiac-emergencies | 12,519 | 548,866 | 794x2577 |
| cardiac-investigations | 8,379 | 401,054 | 794x1942 |
| chronic-coronary-syndromes | 8,523 | 392,179 | 794x1988 |
| heart-failure | 9,216 | 424,611 | 794x2220 |
| hypertension-cv-risk | 10,911 | 513,488 | 794x2471 |
| infective-endocarditis | 10,703 | 467,690 | 794x2427 |
| pericardial-diseases | 9,987 | 416,718 | 794x1772 |
| pulmonary-hypertension | 9,940 | 434,983 | 794x1672 |
| special-populations | 13,102 | 563,393 | 794x2574 |
| systemic-cardiac | 11,664 | 524,656 | 794x2382 |
| valvular-heart-disease | 9,971 | 458,391 | 794x2152 |

For reference: the IHD prototype at /root/sea-knowledge-infographics/ischemic-heart-disease.html was 7,921 chars and fit one A4 page at 794x1123.

## Timing

- Phase 1 (topic identification): ~1 min
- Phase 2 (3 parallel subagents, 5-6 topics each): ~10 min
- Phase 3 (rendering 16 PNGs via Chromium): ~1 min
- Phase 4 (Notion upload, 3 API calls per topic): ~5 min
- Phase 5 (build numbered index, delete child_page blocks): < 1 min
- **Total: ~17 minutes for 16 sub-pages + hub with numbered index**

## Verification result

```
$ python3 verify.py  # reads /pages/{id}/markdown for each
16/16 pages OK
  - All have 10 H2 sections
  - All have image embedded (X-Amz-Signature in markdown)
  - All have 3-4 callouts
  - Hub has 16 numbered_list_item blocks with mention-page
```

## Key gotchas hit (and now in the skill)

1. The 3-step Notion file upload requires `multipart/form-data` with field name `file` and the `Notion-Version` header on the upload URL. The `notion_upload.py` helper handles this.
2. Color values in the JSON blocks API need the full `_background` suffix (e.g. `pink_background`, not `pink_bg`). The Markdown `/markdown` field accepts the short form, but JSON blocks do not.
3. Creating a sub-page via `POST /v1/pages` with `parent: {page_id: HUB}` auto-adds a `child_page` block on the hub. If you also add a manual `link_to_page`, you get duplicates. Solution: delete the auto child_page blocks, then add the numbered index.
4. `PATCH /v1/blocks/{id}/children` is append-only. New blocks always go to the end. The hub's structure ended up as: [numbered index, divider, footer callout, header callout, divider, h2 heading] because the header was added last.
5. `GET /v1/blocks/{page_id}/children` may return 404 for fresh pages created via the `markdown` field. Use `GET /v1/pages/{page_id}/markdown` for verification — it's reliable.
6. The Sea Knowledge style requires 10 sections in a specific order. Deviating breaks the visual rhythm.

## Outputs

- **Notion:** 16 sub-pages under https://app.notion.com/p/cardiology-3825588e846f80cbb9eec8ea437594bc
- **Local archive:** /mnt/tb/Sea-knowledge/ (16 folders × {md, html, png} = 48 files, 7.4 MB)
- **Scripts (in /root/sea-knowledge-infographics/):**
  - `render_topic.py` — markdown → HTML → PNG
  - `topics.py` — the topic list with slugs and source paths
  - `notion_upload.py` — 3-step upload + page creation
  - `batch_render.sh` — shell loop to render all topics
  - `notion_results.json` — page IDs and URLs for verification
