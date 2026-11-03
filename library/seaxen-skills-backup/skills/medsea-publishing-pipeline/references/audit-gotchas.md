# Audit Gotchas — Specific Failures That Produced False Positives

Lessons from the 2026-06-20 ch 1-15 audit where the user had to flag a wrong "100% complete" claim from a prior session.

## Never trust a prior session's "100% complete" claim

The previous session's commit message said "Ch 1-15: 100% match from /mnt/tb/Medicine source" but the actual state had:
- 26 missing atomic topics (ch 2: 14 missing pharmacology topics; ch 15: 12 missing STI topics)
- 30 missing MOC + Hierarchy overview pages (all ch 1-15)

**Always re-run the audit from scratch against `/mnt/tb/Medicine/` source.** Don't trust commit messages, don't trust pre-computed sync stats, don't trust the website showing HTTP 200 (a chapter can render with an empty topic list and still return 200).

## Slug format variants per chapter

The chapter prefix style differs:
- **ch 1-9**: slug is `N-name` (no leading zero) — `1-clinical-decision-making`, `9-palliative-care`
- **ch 10-32**: slug is `0N-name` (leading zero) — `10-acute-medicine`, `16-cardiology`

The build_site.py `BUILT_CHAPTERS` dict has the canonical slug list. Extract via:
```python
import re
pattern = re.compile(r'"([\w-]+)":\s*\(\s*"[^"]+",\s*"https://medsea\.notion\.site/[^"]*?([a-f0-9]{32})",')
```

## Topic file storage pattern: flat vs subdir

The `diseases/` layout differs per chapter:
- **ch 1-9** (FLAT): `diseases/X.Y.Z-slug.md` (file directly, no subdir)
- **ch 10-15** (mixed): mostly subdir `diseases/X.Y.Z-slug/topic.md` for newer ones, but some flat files exist
- **ch 16-32** (SUBDIR): `diseases/X.Y.Z-slug/topic.md` (folder with topic.md inside)

An audit script that only checks for folders (`if f.is_dir():`) will miss ch 1-9 entirely. Must scan for both `diseases/X.Y.Z-*.md` files AND `diseases/X.Y.Z-*/topic.md`.

## Slug-parse regex bug → orphan "31.31" hub

A previous sync script used `^(\d+)\.(\d+)\.(\d+)-(.+)$` to parse folder names like `31.1.1-foo`. This produced:
- group(1) = "31"
- group(2) = "1"
- group(3) = "1"
- group(4) = "foo"

Wrong. The correct pattern is `^(\d+\.\d+)\.(\d+)-(.+)$`:
- group(1) = "31.1" (hub)
- group(2) = "1" (topic idx)
- group(3) = "foo" (slug)

The wrong regex created orphan `31.31 Hub 31.31` and 49 wrongly-bucketed child topics. Always use the SAME regex as `build_site.py`:
```python
m = re.match(r"^(\d+\.\d+)\.(\d+)-(.+)$", f.name)
hub_num = m.group(1)  # e.g., "31.1"
idx = m.group(2)       # e.g., "1"
slug = m.group(3)      # e.g., "adolescent-development-and-puberty"
```

Test the regex on 2-3 folder names BEFORE running bulk sync.

## Folder name truncation gives false "missing" reports

Some MedSea folder names were truncated during prior sync work:
- `32.6.1-advance-care-planning-and-end-of-life-decision-mak` (missing "ing")
- `32.13.2-hypothermia-hyperthermia-and-age-related-thermal-d` (missing "ysregulation")
- `32.3.1-faecal-incontinence-and-constipation-in-the-elderl` (missing "y")

A slug-name comparison reports these as "missing" — but content is identical to source. **Always verify by content hash** (`hash(open(f).read())`), not by name:
```python
src_hash = hashlib.md5(src_content.encode()).hexdigest()
med_hash = hashlib.md5(med_content.encode()).hexdigest()
if src_hash == med_hash:  # EXACT match despite truncated name
    truly_present.add(src_name)
```

Truncated names are a one-time artifact — leave them alone. Don't rename folders just to satisfy the audit script.

## MOC + Hierarchy overview pages are mandatory for "100% complete"

Every synced chapter since 2026-06-20 should have:
- `diseases/X.0.900-chapter-moc/topic.md` (Map of Content)
- `diseases/X.0.901-chapter-hierarchy/topic.md` (Topic Hierarchy)

If either is missing, the chapter is NOT 100% complete. The atomic topic count alone is not sufficient. Pattern:
```python
moc = (chapters_dir / f"{ch_num}.0.900-chapter-moc/topic.md").exists()
hier = (chapters_dir / f"{ch_num}.0.901-chapter-hierarchy/topic.md").exists()
if not (moc and hier):
    return False, "MOC or Hierarchy overview missing"
```

These are added by `/tmp/gen_overviews_chXX.py` style scripts and copied into `diseases/X.0.900-…/topic.md`. See the main SKILL.md `## Chapter Overview Pages (MOC + Hierarchy)` section.

## Audit report format

```
Ch 21 Diabetes: src=179 medsea=222 missing=0  ✅
Ch 22 Gastroenterology: src=112 medsea=147 missing=0  ✅
...
TOTAL: source=1640 medsea=2058 by-hash=1211 truly-missing=0
VERDICT: ✅ 100% COMPLETE (all 4 targets in sync)
```

The 11-topic "false positive" case in ch 21-32 was solved by hash-verifying; the 26-topic real gap in ch 1-15 was solved by hash-verifying (ch 15: 12 STI topics confirmed missing; ch 2: 14 pharmacology topics confirmed missing).

**Always report:**
1. Source count vs MedSea count per chapter
2. By-name matches vs by-hash matches (difference = name artifacts)
3. Truly missing (source in name AND hash, but not in MedSea)
4. MOC + Hierarchy overview presence per chapter