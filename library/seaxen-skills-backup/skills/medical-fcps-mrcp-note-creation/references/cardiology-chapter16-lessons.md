# Cardiology Chapter 16 - Lessons Learned (June 2026)

## Context
Generated 570 full FCPS/MRCP notes for Davidson 24th Edition Chapter 16: Cardiology.
Initial attempt produced 549 template placeholders (2.7% real content).
Remediation: built topic-specific content database → 98.9% real content.

---

## Critical Pitfalls Discovered

### 1. Template Placeholder Syndrome
**Problem**: Auto-generation produces correct STRUCTURE but generic filler text.
- "Underlying mechanism involves multifactorial pathophysiology"
- "Option A / Option B" MCQs without real distractors
- "Comprehensive overview of [topic]"

**Detection**: Scan for these template phrases:
- "Most common causes | Direct injury"
- "Comprehensive overview of"
- "multifactorial pathophysiology"

**Fix**: Topic-specific content databases with pattern-matched routing.

### 2. False "100% Complete" Claims
**Problem**: Declaration based on file count, not content quality.

**Fix**: Mandatory verification protocol:
- Sample 5-10 notes for real medical indicators (GRACE, TIMI, PARADIGM-HF, ESC 202x, drug doses, trial names, scoring systems)
- Target: ≥95% notes with ≥3 real indicators
- Calculate: real_content = files with real indicators / total full notes

### 3. Hierarchy Coverage Gaps
**Problem**: Notes exist but don't map to Davidson hierarchy topics.

**Fix**: Hierarchy-driven verification:
- Parse hierarchy for 220 disease-level topics
- Map notes to sections
- Report exact matches, gaps, extras
- Generate missing before claiming complete

### 4. Duplicate File Naming
**Problem**: Same topic → two files ("Atrial Fibrillation.md" + "Atrial_Fibrillation.md")

**Fix**: Enforce consistent naming (underscores), deduplicate content mapping.

### 5. Generic Category Fallbacks
**Problem**: Category-aware fallbacks still semi-generic.

**Fix**: Expand specific content functions. Target: ≥50 functions for Tier 1/2 topics.

---

## Verification Protocol (Mandatory)

```bash
# 1. Count full notes
search_files pattern="status: full-fcps-mrcp-note" path="/mnt/tb/Medicine/ChapterName"

# 2. Real content verification
python3 -c "
import re, glob
real_indicators = ['GRACE','TIMI','PARADIGM-HF','DAPA-HF','EMPEROR','ESC 202','ACC/AHA','NICE','LVEF','BNP','troponin','CHA2DS2','HAS-BLED','SCD','ICD','PCI','CABG']
template_phrases = ['Most common causes','Comprehensive overview','multifactorial pathophysiology']
for f in glob.glob('/mnt/tb/Medicine/ChapterName/**/*.md', recursive=True):
    content = open(f).read()
    if 'full-fcps-mrcp-note' in content:
        has_real = sum(1 for i in real_indicators if i in content) >= 3
        is_template = any(p in content for p in template_phrases)
        print(f, 'REAL' if has_real else 'TEMPLATE')
"
# Target: >95% REAL
```

---

## Technique: Topic-Specific Content Database

```python
# specific_functions = {
#   "acs classification": acs_classification_content,
#   "atrial fibrillation": af_content,
#   "aortic stenosis": aortic_stenosis_content,
#   "hfref": hfref_content,
#   # ... 50+ functions for Tier 1/2 topics
# }

# Route: topic_clean lowercased → pattern match → specific function
# Fallback: category-aware generator (arrhythmia, valve, HF, CM, PH, etc.)
```

Each function returns 12-section dict with:
- Real drug doses, trial names (PARADIGM-HF, DAPA-HF, EMPEROR, ISCHEMIA, COMPLETE, etc.)
- Current guidelines (ESC/ACC/AHA/NICE 2021-2024)
- Scoring systems (GRACE, TIMI, CHA2DS2-VASc, HAS-BLED, HCM Risk-SCD)
- Topic-specific pathophysiology, clinical features, diagnostics, management

**Result**: 98.9% real content for 570 Cardiology notes.

---

## Category-Aware Fallback Pattern

```python
def category_aware_content(topic, topic_clean, section):
    if is_arrhythmia(topic_clean): return arrhythmia_content(topic)
    if is_valve(topic_clean): return valve_content(topic)
    if is_hf(topic_clean): return hf_content(topic)
    if is_cm(topic_clean): return cm_content(topic)
    # ... 15 categories
    return generic_topic_content(topic, topic_clean, section)
```

Detect category from keywords in topic name, route to category generator that knows the domain.

---

## Results Summary

| Metric | Initial (Failed) | After Remediation |
|--------|------------------|-------------------|
| Full notes | 549 | 570 |
| Real content | 2.7% | 98.9% |
| Template stubs | 549 | 0 |
| Scaffolds | 220 | 0 |
| Hub files | 115 | 115 |
| Hierarchy coverage | ~60% | 264/309 exact matches |

---

## Key Takeaway for Future Chapters

**Never generate 500+ notes in one pass without:**
1. Building specific content for top 50 high-yield topics first
2. Running verification protocol on sample
3. Confirming ≥95% real content
4. Hierarchy mapping validation

The "generate all then fix" approach is fundamentally broken for medical content.