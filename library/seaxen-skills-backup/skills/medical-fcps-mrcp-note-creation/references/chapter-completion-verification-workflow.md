# Chapter Completion Verification Workflow

When user asks "is chapter X fully complete?" or "is it 100% with all information + questions for exam":

## 1. Run Automated Verification First
```bash
python3 scripts/chapter_verify.py "/mnt/tb/Medicine/[Chapter Name]" <expected_leaf_count>
```
- Gets expected leaf count from hierarchy file or user
- Reports: topic files (full), hub files (MOC+hierarchy), scaffolds remaining, no-status files
- Fast sanity check before manual inspection

## 2. Manual File-by-File Inspection (if detail needed)
- Read each topic file to confirm 14-section template completeness
- Check for: mind maps, flowcharts, viva questions, trackers, exam answer modes, revision cards
- **Key distinction**: `status: scaffold` files often contain substantial exam content (MCQs, SBAs, flashcards, must/should/nice tables) but lack the full 14-section template

## 3. Web Verification for Missing Topics
- Search: `Davidson 24th edition Chapter [N] [Chapter Name] contents`
- Cross-reference hierarchy leaf nodes against actual Davidson chapter structure
- Confirm no disease-level topics are missing from the planned file set

## 4. MOC/Hierarchy Status Tags
- MOC and Hierarchy files should have `status: full-fcps-mrcp-hub` (not `scaffold`)
- If missing status tag entirely, add it to frontmatter
- See `references/moc-hierarchy-status-pattern.md` for patch patterns

## 5. Scaffold vs Full Status Criteria

| Status | Criteria |
|--------|----------|
| `full-fcps-mrcp-note` | Complete 14-section template: frontmatter, learning objectives, definitions, etiology, clinical features, differential, investigations, management, complications, high-yield summary, viva questions (10), confusions/mnemonics, mind map, flowchart, recall prompts, trackers, self-test scorecard, exam answer modes (5), MCQs (10), SBAs (5-10), flashcards, revision card |
| `status: scaffold` | Partial content — may have learning objectives, key concepts, MCQs/SBAs/flashcards, must/should/nice table but MISSING ≥3 of: mind map, flowchart, viva questions, spaced repetition trackers, exam answer modes, self-test scorecard, confusions table, one-page revision card |

## Example: Envenomation Chapter (Davidson Ch8) — Session 2026-06-15

**Automated verification result:**
- 13 topic files expected (from hierarchy)
- 9 files: `status: full-fcps-mrcp-note`
- 4 files: `status: scaffold` (General Principles, Spider, Marine, Hymenoptera)
- 2 hub files (MOC, Hierarchy): no status tag (should be `full-fcps-mrcp-hub`)

**Manual finding:** All 4 scaffold files contain high-yield exam content (learning objectives, key concepts, must/should/nice, 10 MCQs, 10 SBAs, flashcards, recall prompts). Missing: mind maps, flowcharts, viva questions (10), spaced repetition trackers, exam answer modes (5), self-test scorecard, confusions/mnemonics table, one-page revision card.

**Web verification:** Davidson 24e Ch8 (J White) has exactly 3 sections (General Principles, Snake Envenomation, Other Envenomation) covering 13 disease-level topics — all present as files.

**Conclusion:** 100% topic coverage, 9/13 at full template standard, 4 need template upgrade, MOC/hierarchy need hub status tag.