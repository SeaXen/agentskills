# Cardiology Chapter 16 — Disease-Level Expansion Session Log
**Date:** 2026-06-17 (continued from ch16 session log)
**Scope:** Expanded from 16 broad hubs to 330 disease-level sub-pages under 17 numbered hubs
**Canonical source:** `/root/sea-knowledge-infographics/all_disease_topics.json` (330 topics with parent_slug, hub, topic, slug, idx)
**Local archive:** `/mnt/tb/Sea-knowledge/16. Cardiology/` (17 hub folders, 330 disease folders, 14 extras in `xtra/`)
**Notion hub:** https://app.notion.com/p/cardiology-3825588e846f80cbb9eec8ea437594bc

## Final structure (17 hubs, 330 diseases)

| # | Hub | Disease count |
|---|---|---|
| 16.1 | Acute Coronary Syndromes | 30 |
| 16.2 | Adult Congenital Heart Disease | 14 |
| 16.3 | Arrhythmias | 41 |
| 16.4 | Cardiac Devices and Electrophysiology | 14 |
| 16.5 | Cardiac Disease in Special Populations | 19 |
| 16.6 | Cardiac Emergencies & Critical Care | 21 |
| 16.7 | Cardiac Investigations | 24 |
| 16.8 | Cardiomyopathies | 22 |
| 16.9 | Chronic Coronary Syndromes | 16 |
| 16.10 | Diseases of the Aorta | 5 |
| 16.11 | Heart Failure | 32 |
| 16.12 | Hypertension & CV Risk | 11 |
| 16.13 | Infective Endocarditis | 13 |
| 16.14 | Pericardial Diseases | 16 |
| 16.15 | Pulmonary Hypertension | 9 |
| 16.16 | Systemic Diseases & Cardiac Involvement | 13 |
| 16.17 | Valvular Heart Disease | 30 |

**Total: 330 disease folders across 17 hubs.**

## Per-folder contents

Each `16.N.M. <topic>/` contains:
- `<topic>.md` — markdown source (always present)
- `<topic>.html` — HTML render (present in 328/330)
- `<topic>.png` — A4 portrait infographic (present in 328/330)

## Known gaps

| Folder | Status | Why |
|---|---|---|
| `16.6.4. adhf-management` | md-only | Chromium hangs (Pitfall 43) |
| `16.6.19. cross-link-00-index-medicine-moc-...` | md-only | Chromium hangs (Pitfall 43) |
| `16.8. Cardiomyopathies/` | no hub .md | Source mds not in `/root/sk-content/`; on Notion only |
| `16.12. Hypertension and CV Risk/` | no hub .md | Source mds not in `/root/sk-content/`; on Notion only |
| `16.17. Valvular Heart Disease/` | no hub .md | Source mds not in `/root/sk-content/`; on Notion only |

## Pipeline that worked

```
1. Source: /root/sk-content/<slug>.md  (358 .md files, all 330 canonical slugs present)
2. Map slug prefix → hub root folder (17 hub roots with name-mismatches like
   'cardiac-disease-in-s' → 'special-populations')
3. For each hub (16.1 .. 16.17):
   - mkdir 16.N. <name>
   - Copy hub .md (if present) into hub folder
   - For each disease in this hub:
     - counter 1..N
     - mkdir 16.N.<counter>. <topic>
     - shutil.copy source md → disease folder
     - subprocess.run render_topic.py with --slug sanitized, timeout=120
     - On timeout: log + move md to xtra/, accept md-only
4. Run flatten_renders.py to fix the renderer's nested output
5. Cleanup_16_6.py: remove duplicate leading-hyphen mds, rename nested slug dirs
6. README.md: document the structure + known gaps
```

## Notion publishing

- 3 waves of `notion_upload_diseases.py START END` (0-100, 100-200, 200-330)
- Final wave (`notion_upload_remaining.py`) caught any 429/timeout failures
- ~328 sub-pages published; 2 chromium-hangers skipped
- All 17 hub pages are on the cardiology Notion hub with numbered list of mention-page children

## The `rm -rf` mistake (Pitfall 44 — worth reading)

A restructuring bash script tried to clean up the wrong directory. Shell expansion of `"16. Cardiology "` (with trailing space) produced two tokens — `16.` and `Cardiology` — and the script targeted the populated `16. Cardiology/` directory, deleting all 347 sub-folders.

**Recovery was possible** because:
1. `/root/sk-content/` was the source-of-truth for all 330 markdown files
2. Notion already had 328 sub-pages with the rendered HTML+PNG
3. The renderer was idempotent — re-rendering 328 mds took ~20 minutes

**Without a source-of-truth backup, this would have been a 3-hour loss.** See Pitfall 44 in SKILL.md for the prevention rules.

## Key gotchas (all in SKILL.md)

- **Pitfall 41**: render_topic.py nests output one level too deep — run `flatten_renders.py` after each batch
- **Pitfall 42**: slugs starting with `-` break argparse — sanitize with `lstrip('-').replace('--', '-').rstrip('-')`
- **Pitfall 43**: chromium hangs on `adhf-management` and `cross-link-...` — accept md-only, don't retry
- **Pitfall 44**: never `rm -rf` a path containing a space via shell expansion — use Python
- **Pitfall 45**: orphaned background processes can collide with re-launched scripts — verify exit before relaunch
