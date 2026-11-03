# MOC & Hierarchy File Status Tag Pattern

**Problem**: When auditing chapter completion, the verification grep for `status: full-fcps-mrcp-note` matches topic notes but not the MOC/hierarchy files. If MOC/hierarchy stay as `status: scaffold`, they show up as "incomplete" in audits even when the chapter is 100% done.

**Solution**: Use a third status tag `status: full-fcps-mrcp-hub` for chapter infrastructure files (MOC, hierarchy, theme-group hubs).

## The Three Status Tags

| Status Tag | Use For | Audit |
|------------|---------|-------|
| `status: scaffold` | Initial stubs (during chapter setup) | Should be 0 once chapter is complete |
| `status: full-fcps-mrcp-note` | Disease-level topic notes (14-section template) | Matches expected leaf count from hierarchy |
| `status: full-fcps-mrcp-hub` | MOC files, hierarchy files, theme-group hub files | ≥2 (MOC + hierarchy) + theme-hubs |

## When to Apply This Fix

When user asks "is chapter X fully complete?" or "is it 100% complete with all information?":

1. Run the chapter completion verification (see SKILL.md "Chapter Completion Verification" section)
2. If MOC/hierarchy still show `status: scaffold`, patch them to `full-fcps-mrcp-hub`
3. If MOC doesn't have a `status:` line at all, add one

## Patch Patterns

### Pattern 1: Replace `status: scaffold` in MOC/hierarchy only
```python
import os
chapter_dir = "/mnt/tb/Medicine/[Chapter Name]"
for filename in ["[Chapter Name] MOC.md", "Davidson Chapter XX - [Chapter Name] Hierarchy.md"]:
    path = os.path.join(chapter_dir, filename)
    if os.path.exists(path):
        with open(path) as f: content = f.read()
        new_content = content.replace("status: scaffold", "status: full-fcps-mrcp-hub")
        with open(path, 'w') as f: f.write(new_content)
        print(f"✓ {filename}: scaffold → full-fcps-mrcp-hub")
```

### Pattern 2: Add `status:` line if MOC frontmatter lacks it
```python
import os
moc_path = "/mnt/tb/Medicine/[Chapter Name]/[Chapter Name] MOC.md"
with open(moc_path) as f: content = f.read()
if "status:" not in content[:300]:
    new_content = content.replace(
        "davidson_chapter: Chapter XX: [Name]\n---",
        "davidson_chapter: Chapter XX: [Name]\nstatus: full-fcps-mrcp-hub\n---"
    )
    with open(moc_path, 'w') as f: f.write(new_content)
    print("✓ Added status: full-fcps-mrcp-hub to MOC")
```

## Verification (After Patch)

```bash
# Topic notes count
grep -l "status: full-fcps-mrcp-note" /mnt/tb/Medicine/[Chapter]/*.md | wc -l

# Hub files count (MOC + hierarchy + any theme-hubs)
grep -l "status: full-fcps-mrcp-hub" /mnt/tb/Medicine/[Chapter]/*.md | wc -l

# Remaining scaffolds (should be 0)
grep -l "status: scaffold" /mnt/tb/Medicine/[Chapter]/*.md | wc -l
```

## Pitfall: Don't Bulk-Flip All Scaffolds

Some files legitimately use `status: scaffold` (e.g., partial sub-section hubs, placeholder files for "see X" cross-references). Before bulk-flipping:
- Verify the file actually contains complete content (frontmatter + 14 sections)
- Do NOT use `sed -i 's/status: scaffold$/status: full-fcps-mrcp-note/'` blindly
- Audit each file individually if uncertain

## Example: Pop Health & Epidemiology Fix (Session 2026-06-15)

**Before**:
- 27 topic files: `status: full-fcps-mrcp-note` ✓
- 2 hub files (MOC, hierarchy): `status: scaffold` ✗ (audit said 1 scaffold remaining)

**After**:
- 27 topic files: `status: full-fcps-mrcp-note` ✓
- 1 hierarchy file: `status: full-fcps-mrcp-hub` ✓
- 1 MOC file: `status: full-fcps-mrcp-hub` (added line) ✓
- 0 scaffolds remaining → chapter 100% complete

## Reference
This pattern was discovered when completing the Population Health & Epidemiology chapter (Davidson Ch5, session 2026-06-15). All other completed chapters (Diabetes, Endocrinology, Clinical Biochemistry) may benefit from the same audit + patch.
