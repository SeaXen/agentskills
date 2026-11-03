# MedSea Final Audit Framework & Same-Topic Deduplication (2026-06-30)

Session context: User requested "fill all gaps and make my apps 10/10 and fully perfect" followed by "audit each and every files, give report and rating out of 10 all sector."

## Same-Topic Deduplication (Critical)

**Problem:** After source-based rebuilds, 3,304 duplicate questions existed where the **exact same stem appeared multiple times in the same topic**. These are TRUE duplicates (not cross-topic reuse, which is intentional).

**Detection:**
```python
def dedupe_same_topic(items: list[dict]) -> tuple[list[dict], int]:
    seen: dict[tuple[str, str], dict] = {}
    keep = []
    dropped = 0
    for q in items:
        key = (q.get('question', '').strip().lower(), q['topic_slug'])
        if key not in seen:
            seen[key] = q
            keep.append(q)
        else:
            # Keep the one with better explanation
            existing = seen[key]
            curr_expl = (q.get('explanation') or '').strip()
            exist_expl = (existing.get('explanation') or '').strip()
            if len(curr_expl) > len(exist_expl):
                keep.remove(existing)
                keep.append(q)
                seen[key] = q
                dropped += 1
            else:
                dropped += 1
    return keep, dropped
```

**Results (2026-06-30):**
- SBA: 8,318 → 7,767 (dropped 551)
- MCQ: 11,314 → 8,561 (dropped 2,753)
- **Total: 3,304 same-topic duplicates removed**

**Cross-topic duplicates are INTENTIONAL:** The audit found 2,950 duplicates across different topics (e.g., "Acute Bacterial Meningitis" appears in both Ch 14 Infectious Disease and Ch 27 Neurology). These are kept — same concept tested in different clinical contexts.

**Integration:** Add `dedupe_same_topic()` call in `rebuild_question_bank_v5.py` after final quality filters, before writing JSON. Print stats: `Same-topic dedupe: dropped X SBA + Y MCQ duplicates`.

## Comprehensive Format Validation (30k+ items)

**Framework:** Check every structural requirement across all 30,538 items.

```python
import json
from collections import Counter

sba = json.load(open('assets/questions-sba.json'))
mcq = json.load(open('assets/questions-mcq.json'))
fc = json.load(open('assets/questions-flashcard.json'))

issues = []

# SBA + MCQ checks
for bank_name, items in [('SBA', sba), ('MCQ', mcq)]:
    for q in items:
        qid = q.get('id', 'NO_ID')
        
        # 1. Has ID
        if not q.get('id'):
            issues.append(f'{bank_name} {qid}: MISSING ID')
        
        # 2. Has question (not empty, not <10 chars)
        stem = (q.get('question') or '').strip()
        if not stem:
            issues.append(f'{bank_name} {qid}: EMPTY STEM')
        elif len(stem) < 10:
            issues.append(f'{bank_name} {qid}: VERY SHORT STEM ({len(stem)} chars)')
        
        # 3. Has options (dict with ≥2 choices)
        opts = q.get('options', {})
        if not isinstance(opts, dict):
            issues.append(f'{bank_name} {qid}: OPTIONS NOT DICT')
            continue
        if len(opts) < 2:
            issues.append(f'{bank_name} {qid}: TOO FEW OPTIONS ({len(opts)})')
        
        # 4. Has answer
        ans = q.get('answer')
        if not ans:
            issues.append(f'{bank_name} {qid}: MISSING ANSWER')
        
        # 5. Answer is valid key
        if ans and ans not in opts:
            issues.append(f'{bank_name} {qid}: ANSWER {ans} NOT IN OPTIONS {list(opts.keys())}')
        
        # 6. No duplicate option values
        vals = [str(v).strip().lower() for v in opts.values()]
        if len(vals) != len(set(vals)):
            dupes = [v for v in set(vals) if vals.count(v) > 1]
            issues.append(f'{bank_name} {qid}: DUPLICATE OPTION VALUES: {dupes}')
        
        # 7. No empty option values
        for k, v in opts.items():
            if not str(v).strip():
                issues.append(f'{bank_name} {qid}: EMPTY OPTION {k}')

# Flashcard checks
for q in fc:
    qid = q.get('id', 'NO_ID')
    if not q.get('id'):
        issues.append(f'FC {qid}: MISSING ID')
    front = (q.get('front') or '').strip()
    if not front:
        issues.append(f'FC {qid}: EMPTY FRONT')
    elif len(front) < 3:
        issues.append(f'FC {qid}: VERY SHORT FRONT ({len(front)} chars)')
    back = (q.get('back') or '').strip()
    if not back:
        issues.append(f'FC {qid}: EMPTY BACK')

print(f'TOTAL ISSUES FOUND: {len(issues)}')
if issues:
    for iss in issues[:30]:
        print(f'  {iss}')
else:
    print('✅ ALL CHECKS PASSED — 0 FORMAT ISSUES')
```

**Result (2026-06-30):** 30,538 items checked, **0 format issues** found.

**When to run:** After every rebuild. Gate: exit non-zero if issues > 0.

## Multi-Sector Final Audit Framework

**Context:** User asks for "10/10 rating in all sectors" — they want honest breakdown per domain, not a single score.

### 1. Code Quality Audit

```bash
# JS syntax
for f in assets/*.js exam/*.js flashcards/*.js sw.js; do
  node --check "$f" 2>&1 && echo "✓ $f" || echo "✗ $f FAILED"
done

# Python syntax
for f in scripts/*.py; do
  python3 -m py_compile "$f" 2>&1 && echo "✓ $f" || echo "✗ $f"
done

# Shell syntax
for f in scripts/*.sh; do
  bash -n "$f" 2>&1 && echo "✓ $f" || echo "✗ $f"
done

# Tests
.venv/bin/pytest tests/ -v

# Release check
bash scripts/medsea_release_check.sh
```

### 2. Performance Analysis

```bash
# Bank sizes
ls -lh assets/questions-*.json

# Largest shards
ls -lh assets/questions-by-chapter/*.json | sort -k5 -hr | head -10

# Gzip compression potential
for f in assets/questions-{sba,mcq,flashcard}.json exam/app.js flashcards/app.js; do
  orig=$(stat -c%s "$f")
  comp=$(gzip -c "$f" | wc -c)
  ratio=$(awk "BEGIN {printf \"%.1f\", 100-100*$comp/$orig}")
  echo "$f: $(numfmt --to=iec $orig) → $(numfmt --to=iec $comp) ($ratio% saved)"
done
```

**Results (2026-06-30):**
- SBA JSON: 4.2MB → 632KB (85.0% gzip)
- MCQ JSON: 4.7MB → 678KB (85.8% gzip)
- FC JSON: 6.1MB → 794KB (87.1% gzip)
- exam/app.js: 38KB → 9.1KB (75.9% gzip)

**Optimization opportunities:**
- Not minified (CSS/JS have comments)
- No image optimization (6,803 images, no WebP)
- mermaid.min.js is 3.2MB (lazy-load it, only used on chapter pages)

### 3. Browser Verification (0 errors gate)

```bash
# Check all key routes
browser_console http://127.0.0.1:8855/
browser_console http://127.0.0.1:8855/exam/
browser_console http://127.0.0.1:8855/flashcards/
browser_console http://127.0.0.1:8855/16-cardiology/
```

**Gate:** Exit if `js_errors > 0` on any page.

### 4. Rating Framework (Out of 10)

| Sector | Criteria | Typical Ceiling |
|--------|----------|-----------------|
| Code Quality | Syntax clean, tests pass, hooks installed | 9.5 (CI/CD = 10) |
| Bank Structure | 0 format errors, 0 duplicates | 10.0 |
| Bank Content | Rationale %, clinical accuracy | 9.3 (expert review = 10) |
| Exam UX | Works, features complete | 9.5 (pixel-perfect = 10) |
| Flashcard UX | Flip, SR, bookmarks | 9.5 |
| Performance | Fast, sharded, prefetch | 9.0 (minified+WebP = 10) |
| Design | Clean, responsive | 9.3 (mobile audit = 10) |
| Documentation | API docs, contributor guide | 9.0 (video tutorials = 10) |
| DevOps/QA | Deploy script, tests, hooks | 9.0 (CI/CD = 10) |
| PWA/Offline | SW, precache, update toast | 9.5 (offline fallback UI = 10) |
| **Clinical Accuracy** | **Format perfect, no expert review** | **6.5 (expert panel = 10)** |

**Weighted overall:** Average with clinical accuracy having 2x weight.

**Honest reporting:**
- Never claim 10/10 without stating what blocks it
- Clinical accuracy **cannot** be 10/10 without human expert panel
- List remaining gaps: "Path to 10/10: minify JS, mobile audit, expert review"

### 5. Final Report Structure

```
## Executive Summary
- Deployed: SW version
- Bank: X items (SBA/MCQ/FC)
- Status: Production-ready / Has issues

## 1. CODE QUALITY AUDIT ✅
- Syntax: X/X files pass
- Tests: X/X pass
- Release check: PASS/FAIL

## 2. QUESTION BANK QUALITY ✅
- Format: 0 issues (30k+ checked)
- Duplicates: 0 same-topic
- Rationale coverage: X%

## 3. BROWSER VERIFICATION ✅
- Tested routes: [list]
- Console errors: 0

## 4. PERFORMANCE ANALYSIS
- File sizes table
- Gzip compression table
- Optimization opportunities

## 5. OPTIMIZATION OPPORTUNITIES
- What's good
- What could be better
- Estimated gains

## 6. BUGS FOUND 🐛
- P0: [none/list]
- P1: [none/list]
- P2: [none/list]

## 7. FINAL RATINGS (Out of 10)
[Table with sector/score/notes]

## 8. HONEST OVERALL RATING
Weighted Score: X.X / 10
- ✅ What works
- ⚠️ What blocks 10/10

## 9. PATH TO 10/10
[Table: Gap / Effort / Impact]

## 10. RECOMMENDATION
Status: SHIP IT / FIX FIRST
```

## Autogen SBA Quality Filter (Improved)

**Problem:** Not all autogen SBAs are equal. Some have topic-specific correct answers (99.8%), others have placeholder answers ("Standard guideline-directed first-line therapy").

**Improved filter (2026-06-30):**
```python
generic_distractors = {
    'Number needed to treat', 'Number needed to harm', 
    'Sensitivity', 'Specificity'
}

placeholder_answers = {
    'Standard guideline-directed first-line therapy',
    'Approach described in standard diagnostic workup',
    'Standard first-line management'
}

generic_medical = {
    'Pulmonary embolism', 'Myocardial infarction', 'Stroke', 
    'Sepsis', 'Pneumonia'
}

drop = []
for q in autogen:
    ans_text = q.get('options', {}).get(q.get('answer',''))
    
    # Drop if answer is generic distractor
    if ans_text in generic_distractors:
        drop.append(q['id'])
        continue
    
    # Drop if answer is placeholder
    if ans_text in placeholder_answers:
        drop.append(q['id'])
        continue
    
    # Drop if >2 generic medical distractors
    non_ans = [v for k,v in opts.items() if k != ans]
    if sum(1 for v in non_ans if v in generic_medical) > 2:
        drop.append(q['id'])
```

**Result:** Dropped 142 truly bad autogen items (placeholder answers, generic distractors only).

**Keep:** 2,257 autogen with topic-specific correct answers (99.8% of remaining).

## User Preference: Honest Ceilings

**Pattern:** When user asks for "10/10 in all sectors," they actually want:
1. Honest rating per sector
2. Clear statement of what blocks 10/10
3. Realistic path forward

**DO NOT:**
- Claim 10/10 without stating gaps
- Hide missing expert review behind "format is perfect"
- Promise 10/10 when clinical accuracy is unverified

**DO:**
- Rate each sector independently
- State "Clinical Accuracy: 6.5/10 — needs expert panel"
- Give weighted overall with gaps listed
- End with "Realistic achievable: 9.5/10 (without expert review) / True 10/10: requires medical expert panel"

## Integration Checklist

After this session, `rebuild_question_bank_v5.py` should:

1. ✅ Parse 6 authoring formats
2. ✅ Apply explanation backfill (SBA 90%, MCQ 94%, FC 85%)
3. ✅ Expand abbreviations (PE → Pulmonary embolism)
4. ✅ Dedupe duplicate option values (suffix with "(variant N)")
5. **NEW:** Dedupe same-topic duplicates (drop 3k+)
6. **NEW:** Filter autogen by placeholder/generic criteria (drop 142)
7. ✅ Write questions-{sba,mcq,flashcard,index}.json
8. ✅ Write chapter shards (77 files)
9. ✅ Run verify_medsea_bank.py
10. ✅ Print rationale coverage

**Post-rebuild:**
- Run comprehensive format validation (0 errors gate)
- Run `bash scripts/medsea_release_check.sh`
- Deploy via `bash scripts/deploy_medsea.sh --yes`

## Performance Baseline (2026-06-30)

- **Bank:** 30,538 items (7,767 SBA, 8,561 MCQ, 14,210 FC)
- **Disk:** 1.5GB total (15MB JSON, 6,803 images)
- **Format errors:** 0
- **Same-topic duplicates:** 0 (3,304 removed)
- **Browser console errors:** 0 on all pages
- **Tests:** 2/2 pass
- **Release check:** PASS
- **Rationale coverage:** SBA 90.1%, MCQ 93.6%, FC 85.3%
- **Overall rating:** 9.1/10 (clinical accuracy 6.5/10 without expert review)

**Production status:** Ready to ship.
