---
name: davidson-ch22-audit-2026
description: Audit case study of Davidson Ch 22 Nutritional Factors (June 2026) — documents the duplicate-filename pitfall (Zinc scaffold vs completed) and the sub-agent (delegate_task) failure mode for large content. Companion to davidson-ch20-endocrinology-audit-2026.
type: reference
---

# Davidson Chapter 22 Nutritional Factors — Audit Case Study (June 2026)

## Summary
- **Folder**: `/mnt/tb/Medicine/Nutritional Factors in Disease/`
- **Textbook**: Davidson's Principles and Practice of Medicine, 24th Edition, Chapter 22: Nutritional factors in disease
- **Expected topics**: 36 disease-level topics across 7 sections
- **Actual disk files**: 36 disease-level files + 2 hub files (MOC + Hierarchy) = 38 total
- **Completion**: 36/36 (100%) after audit fix

## Key Findings

### Duplicate Filename (Critical Pitfall)
- Original scaffold: `Zinc- Acrodermatitis & Wound Healing.md` (~3KB, 169 lines, status: scaffold)
- Later completed: `Zinc- Acrodermatitis, Wound Healing & Immunity.md` (~31KB, 503 lines, status: full-fcps-mrcp-topic-note)
- Both files coexisted silently; hierarchy referenced the simpler name; scaffold file was a "dead stub"
- **Fix**: `mv scaffold scaffold.tmp && rm scaffold.tmp && mv completed simpler_name`

### Status Value Drift (3 Values Used)
- `full-fcps-mrcp-topic-note` (most files, ~28)
- `complete` (~5 files, written by sub-agents not following convention)
- `full-fcps-mrcp-note` (~3 files, original skill spec)
- **Fix**: `sed` to standardize to `full-fcps-mrcp-topic-note` across the corpus

### Sub-agent (delegate_task) Failure Mode
- Batched 3-4 files per sub-agent → all failed with "Subagent timed out after 600.0s"
- Even 1 file per sub-agent (~30KB) failed in the sub-agent's own write_file call
- **Lesson**: `delegate_task` cannot parallelize 25-36KB Davidson chapter work; direct sequential `write_file` from parent agent is the only reliable path

### MOC Update Pattern
- MOC was updated once at the END (after all 36 files complete), not incrementally
- For 36+ file chapters: write_file (full overwrite) the complete MOC at the end is more efficient than 30+ small patches

## Verification Commands Used
```bash
cd "/mnt/tb/Medicine/Nutritional Factors in Disease/"
for f in *.md; do
  size=$(wc -c < "$f")
  status=$(head -7 "$f" 2>/dev/null | grep "status:" | head -1 | awk '{print $2}')
  echo "$status | $size | $f"
done | sort -t'|' -k2 -n

# Count completion statuses (should be 36/36)
grep -l "full-fcps-mrcp-topic-note\|^status: complete" *.md | wc -l

# Check for duplicate (Zinc)
ls "Zinc"* | sort

# Standardize statuses
for f in *.md; do
  sed -i 's/^status: complete$/status: full-fcps-mrcp-topic-note/' "$f"
  sed -i 's/^status: full-fcps-mrcp-note$/status: full-fcps-mrcp-topic-note/' "$f"
done
```

## Lessons for Future Audits
1. **Always `ls | sort` after creating new files** — check for filename duplicates with "Zinc" or other common topics that may have been created with slightly different names
2. **Status value standards drift across sub-agents and direct writes** — accept ALL completion values in audit scripts, then `sed` to standardize
3. **`delegate_task` sub-agents have same stream timeouts as parent write_file** — for large content (>25KB per file), direct parent write_file is the only reliable method
4. **MOC update as final step** for large chapters: write complete MOC once at the end, not incremental patches

## Cross-References
- See `references/davidson-ch22-nutritional-factors.md` in `medical-fcps-mrcp-exam-notes` skill for the full worked example
- See `references/davidson-ch20-endocrinology-audit-2026.md` for the Endocrinology audit case
- See `references/placeholder-patterns.md` for empty-numbered-block detection
