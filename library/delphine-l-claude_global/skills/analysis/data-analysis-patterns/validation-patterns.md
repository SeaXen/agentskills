# Data Validation Patterns

Patterns for verifying column names, data quality, and data provenance.

## Critical Data Validation: Column Name Verification

### The Problem: Column Names Can Be Misleading

**Column names don't always match their content.** This can happen due to:
- Copy-paste errors during data generation
- Misunderstanding of source code logic
- Legacy naming from previous versions
- Automatic column naming that reverses order

**Real-world example from VGP analysis:**
Dataset columns were named **opposite** of their actual content:
- `telomere_cat0_both_terminal` -> Actually contained "no telomeres" data (cat0)
- `telomere_cat1_one_terminal` -> Actually contained "both terminal" data (cat1)
- `telomere_cat2_no_terminal` -> Actually contained "one terminal" data (cat2)

**Impact**: Would have resulted in completely inverted biological interpretation (showing most chromosomes WITHOUT telomeres when the opposite was true).

### The Solution: Always Verify Against Source Code

**Before using any data column in analysis:**

1. **Find the source script** that generated the data
2. **Read the actual code** that assigns values to columns
3. **Verify column names match the logic**
4. **Add validation checks** comparing to known controls

**Example verification workflow:**
```python
# 1. Find source script (e.g., classify_telomeres.py)

# 2. Check the actual assignment logic in source:
"""
if terminal == 2 and interstitial == 0:
    category = 1  # Both terminal telomeres
elif terminal == 1 and interstitial == 0:
    category = 2  # One terminal telomere
else:
    category = 0  # No telomeres
"""

# 3. Verify column names match this logic
# Expected: cat0 = no telomeres, cat1 = both terminal, cat2 = one terminal

# 4. Check actual data against expectations
print("Cat1 (should be 'both terminal'):")
print(df['telomere_cat1_one_terminal'].describe())

# 5. Add biological plausibility check
# Most chromosomes should have at least some telomeres
pct_with_telomeres = ((df['telomere_cat1'] + df['telomere_cat2']) /
                       df['total_chr_scaffolds']).mean()
assert pct_with_telomeres > 0.5, f"Only {pct_with_telomeres:.1%} with telomeres - check column mapping!"

# 6. Cross-validate with known control samples
# Example: Chr1 of species X is known to have both terminal telomeres
control = df[(df['species'] == 'Homo_sapiens') & (df['chr'] == 'chr1')]
assert control['telomere_cat1_one_terminal'].sum() > 0, "Control chr1 should have cat1"
```

### Prevention Checklist

Before finalizing any analysis using categorical columns:

- [ ] Located source script that generated the data
- [ ] Verified column assignment logic in source code
- [ ] Cross-referenced column names with source logic
- [ ] Added assertions for biological plausibility
- [ ] Tested with known control samples
- [ ] Documented any discrepancies found
- [ ] Updated column names or added mapping if needed

### When This Is Critical

Column verification is **essential** when:
- Processing data from external scripts
- Working with categorical classifications
- Using data with non-obvious column names (cat0, cat1, cat2)
- Column names contain ambiguous terms
- Any time results seem biologically implausible

**Red flags that suggest column verification needed:**
- Results contradict biological expectations
- Percentages don't sum to 100% when they should
- Categories show inverse patterns to literature
- Column names use generic terms (cat0, cat1, cat2)
- Values seem swapped or inverted
- Known controls don't match expected values

### Fixing Column Name Mismatches

**Option 1: Rename columns in code**
```python
# Document the correction
"""
IMPORTANT: Column names are MISLABELED in the dataset!
Actual meanings based on classify_telomeres.py:
  cat0 = 0 terminal (no telomeres) - but column named "both_terminal"
  cat1 = 2 terminal (both terminal) - but column named "one_terminal"
  cat2 = 1 terminal (one terminal) - but column named "no_terminal"
"""

# Correct mapping with clear comments
df['telomere_pct_both_terminal'] = (df['telomere_cat1_one_terminal'] /  # cat1 = both terminal!
                                     df['total_chr_scaffolds'] * 100)
df['telomere_pct_one_terminal'] = (df['telomere_cat2_no_terminal'] /   # cat2 = one terminal!
                                    df['total_chr_scaffolds'] * 100)
df['telomere_pct_no_terminal'] = (df['telomere_cat0_both_terminal'] /   # cat0 = no terminal!
                                   df['total_chr_scaffolds'] * 100)
```

**Option 2: Create corrected dataset**
```python
# Rename columns correctly
df_corrected = df.rename(columns={
    'telomere_cat0_both_terminal': 'telomere_cat0_no_terminal',
    'telomere_cat1_one_terminal': 'telomere_cat1_both_terminal',
    'telomere_cat2_no_terminal': 'telomere_cat2_one_terminal'
})

# Save with clear documentation
df_corrected.to_csv('data_corrected_columns.csv', index=False)

# Document in README
"""
CORRECTED: 2026-02-16
- Column names were mislabeled in original data
- Verified against source code: classify_telomeres.py
- Corrected column names now match actual content
"""
```

### Documentation Template

When you discover and fix column mismatches, document thoroughly:

```markdown
## Data Quality Issue: Column Name Mismatch

**Discovered**: [Date] during [Analysis name]

**Problem**: Column names did not match their content

**Columns affected**:
- `[column_name]` - Named as [X] but actually contains [Y]
- `[column_name]` - Named as [A] but actually contains [B]

**Source of truth**: [script name and line numbers]

**Impact**: [What would have gone wrong without correction]

**Fix**: [How columns were remapped or renamed]

**Validation**: [How correctness was verified]
```

---

## Data Quality Verification During Analysis

### Detecting Implausible Values

When populating analysis files with statistical results, **verify biological plausibility**:

**Red flags for data issues**:
1. **Values outside expected range**:
   - Ratios >1.0 when measuring partial detection (<1.0 expected)
   - Ratios ~2.0 that match patterns from different metrics (e.g., diploid/haploid)
2. **Inconsistency with related metrics**:
   - Figure 5 shows 34.5% telomere detection -> Figure 5b should show ratio ~0.35, NOT 2.0
3. **Biological impossibility**:
   - 200% detection of telomeres (can't detect more than exist)
4. **Pattern matching wrong metric**:
   - Values matching chromosome counts when expecting telomere counts

**Example from Figure 5b issue**:
```markdown
## Statistical Results

### Sample Sizes and Descriptive Statistics

**IMPORTANT DATA ISSUE**: The values obtained appear to represent **chromosome achievement ratios** (similar to Figure 3) rather than **telomere detection ratios**. Expected telomere detection ratios based on Figure 5 results should be ~0.2-0.5, but observed values are ~1.9-2.0, matching chromosome ratio patterns.

| Category | n | Median | Mean +/- SEM | Q1 - Q3 |
|----------|---|--------|------------|---------|
[data table with problematic values]

**Note**: These ratios are consistent with diploid chromosome counts relative to haploid karyotype (expected ~2.0), NOT telomere detection ratios (which should be <1.0 and typically 0.2-0.5 based on Figure 5).
```

**Documentation approach for data issues**:
1. **Flag clearly at the start** of Statistical Results section
2. **Provide evidence** for the mismatch (multiple lines of reasoning)
3. **Explain what data likely represents** instead
4. **Document implications** of missing correct data
5. **Recommend corrective actions** for future analysis
6. **Provide context** from valid related metrics

**Benefits**:
- Prevents propagation of erroneous conclusions
- Creates clear audit trail for data quality issues
- Guides future data collection or correction efforts
- Maintains scientific integrity of analysis documentation

---

## Data Provenance: Verifying Derived vs Source Columns

### The Problem: Derived Columns May Use Inferior Sources

A derived column (e.g., `technology_simplified`) may have been created from an
incomplete external file rather than the richer source column already present in
the dataset. This causes silent data loss.

**Real-world example**: `technology_simplified` was populated from a 316-row
external metadata file, yielding 268 HiFi + 47 CLR. Meanwhile, the `Assembly tech`
column (already in the dataset) contained 536/541 values -> 378 HiFi + 141 CLR.
This meant **225 assemblies (42%) had missing technology** unnecessarily.

### Diagnostic Pattern

```python
# Compare a derived column against its likely source
derived_col = 'technology_simplified'
source_col = 'Assembly tech'

print(f"Derived non-null: {df[derived_col].notna().sum()}/{len(df)}")
print(f"Source non-null:  {df[source_col].notna().sum()}/{len(df)}")

# Cross-tabulate to see mapping
ct = pd.crosstab(
    df[source_col].fillna('MISSING'),
    df[derived_col].fillna('MISSING'),
    margins=True
)
print(ct)
```

### Prevention

1. When a build script merges external metadata, check if the column already exists
2. Document which source file each derived column comes from
3. After building datasets, validate coverage: `df[col].notna().mean()`
4. Prefer reclassifying from rich source columns over merging sparse external files

## Denominator Provenance vs the Temporal Axis

Before reporting a temporal trend in any *derived ratio*, crosstab the denominator's
`*_src` provenance column against the time axis. If source and time are confounded, the
"trend" may be an annotation artifact rather than a change in the thing being measured.

### Diagnostic pattern

```python
# 1. Is the source confounded with time?
print(pd.crosstab(df['year'], df[f'{denominator}_src'], normalize='index').round(2))

# 2. Does the metric differ by source?
print(df.groupby(f'{denominator}_src')[metric].agg(['mean', 'size']))

# 3. Does the trend survive within a single source?
print(df.groupby([f'{denominator}_src', 'year'])[metric].mean())
```

Read it as: **if the within-source trend is flat but the pooled trend is steep, the
pooled trend is the source switch, not the biology.**

### Real case

`num_chromosomes_expected` was 99.7% `original` for 2021-2024, then 65% and 93%
`goat_api+sexchr` for 2025 and 2026. Achievement rate was 87.1% under `original`
(n=318) versus 50.0% under `goat_api+sexchr` (n=184). Within `original` alone the rate
was flat across 2021-2024 (87.5 / 90.3 / 89.7 / 88.0%). The apparent post-2024 decline
in assembly quality was entirely the source switch.

### Always check what else shares the denominator

The confound travels with the denominator, not the metric. In the case above,
`telomere_ratio` divided by the same `num_chromosomes_expected` and inherited the same
spurious decline. When you find one, grep for every other derived column using it.

### Reporting

When release date and annotation source are near-perfectly confounded, no temporal claim
is recoverable for the affected metrics by statistics alone. Either harmonise the
annotation across the dataset or restrict the analysis to a single source — and say
which you did. Absolute rates should carry the source composition alongside them.

> **Look for circularity before concluding "source switch".** In the case above, a large
> part of the apparent 87.1% vs 51.4% split was the older source containing *fallback*
> rows that score 1.0 by construction. Restricting to rows with a genuine denominator, the
> split narrowed to 68.8% vs 48.4%. A provenance difference and a circular fallback look
> identical in a group-by; check `numerator == denominator` to tell them apart.
> See [Circular Derived Metrics](#circular-derived-metrics).

## Verify You're Reading All Available Sources

When a build/combine script exists, **read its output, not its inputs**. A notebook that
loads one upstream file directly will silently miss whatever the combiner merged in, and
the loss is invisible because the file it reads is perfectly valid.

### Coverage check before analysing

```python
cov = set(source['id'].astype(str).str.lower().str.strip())
full['_id'] = full['id'].astype(str).str.lower().str.strip()
full['covered'] = full['_id'].isin(cov)
print(full.groupby('category')['covered']
          .agg(covered='sum', total='size')
          .assign(pct=lambda x: (100 * x['covered'] / x['total']).round(1)))
```

**Uneven coverage across the groups you are comparing is a selection bias, not just a
smaller n** — especially when coverage correlates with time and the groups differ in age.
Each group is then sampled from a different era.

### Rule out a key-matching bug before blaming coverage

Absence and mis-keying look identical in a join result. Distinguish them:

```python
missing = full[~full['covered']]
stem = lambda s: re.sub(r'\d+$', '', s)          # strip specimen number
istem = {stem(x) for x in cov}
print('stem match :', sum(stem(t) in istem for t in missing['_id']), '/', len(missing))
print('name match :', missing['_name'].isin(source_names).sum(), '/', len(missing))
```

If near-zero match either way, the records are genuinely absent and no join fix will
recover them — go to the upstream data instead.

### Real case

A notebook read `summary_pre_vs_post_curation.csv` (one of two pre/post sources) rather
than the combined `scaffold_n50_pre_post_curation.tsv`. The unread AGP-derived source
covered exactly the recent releases where one category lived. That category showed
n=26 pairs / 14 species instead of 137 / 69 — a 5x undercount — and its survivors were
its oldest members, being compared against groups sampled from a different era. Coverage
by category was 8.6% / 85% / 57%; only the 8.6% group was visibly wrong.

## Circular Derived Metrics

A ratio is circular when its denominator falls back to its own numerator. It then returns
**1.0 by construction**, cannot fail, and looks exactly like a saturated-but-real
distribution. Range checks, null checks and type checks all pass.

The usual cause is a well-meant gap-fill: "if the expected value is unknown, use the
observed value."

### Detect it

Compare numerator and denominator directly, grouped by the source of the denominator:

```python
circular = (df[numerator] == df[denominator])
print(df.groupby(df[f'{denominator}_source'].fillna('(none)'))
        .apply(lambda g: pd.Series({
            'n': len(g),
            'num==den': (g[numerator] == g[denominator]).sum(),
            'ratio==1': (g[metric] == 1).sum()})))
```

A source category where `num == den` for ~100% of rows is a fallback, not a measurement.

### Real case

`chr_achievement_ratio = num_chromosomes / num_chromosomes_haploid_adjusted`. Where no
karyotype could be found the pipeline copied the *observed* chromosome count into the
expected field:

| `karyotype_source` | rows | `num == den` | `ratio == 1` |
|---|---:|---:|---:|
| Not_found | 326 | 320 (98%) | 320 (98%) |
| Expected_karyotype.tsv | 22 | 22 (100%) | 22 (100%) |
| GoaT | 250 | 93 (37%) | 121 (48%) |

348 of 835 assemblies were "achieving" their expected chromosome count by dividing a number
by itself. That, not any distributional property, was why 73.5% sat at exactly 1.0.

### Fix

Where the denominator is unknown the metric must be **NA**, never a copy of the numerator.
Assert it: a derived ratio may not be defined where its denominator has no independent
source.

```python
assert not (df[denominator].isna() & df[metric].notna()).any()
```

Expect coverage *and* the headline rate to drop once the fallback is removed. That is the
correct outcome — the previous number was partly arithmetic.

## Read the Formula Before Diagnosing the Metric

Column names imply formulas that are often wrong. Before writing any interpretation of a
derived metric, find its assignment in the build code **and** verify it numerically.

```bash
grep -rn 'df\["metric_name"\]\s*=' scripts/ data-processing/
```

```python
lhs = pd.to_numeric(df[metric], errors='coerce')
rhs = pd.to_numeric(df[a], errors='coerce') / pd.to_numeric(df[b], errors='coerce')
m = lhs.notna() & rhs.notna()
print(f"{np.isclose(lhs[m], rhs[m]).sum()}/{m.sum()} match")   # want 100%
```

### Two real misses, same root cause

1. `chr_achievement_ratio` divides by `num_chromosomes_haploid_adjusted`, not
   `num_chromosomes_expected`. Both exist, both are GoaT-sourced, and they agree in only
   **251 of 833 rows**. A whole written analysis named the wrong column.
2. `gaps` is `total_length - total_contig_length`, not `total_length - ungapped_length`.
   The wrong reading held for 815/815 rows *by coincidence* — the two candidate columns
   are near-duplicates — so a numeric check on the wrong pair still "passed".

**When two candidate columns both fit, the numeric check cannot discriminate.** Go to the
assignment in the source. A formula confirmed against the code costs one grep; a wrong one
propagates into every downstream conclusion.

## Validate a Derived Source Against Ground Truth

When a data source is *derived* (parsed from a structural file, transcribed from a report)
rather than measured, validate it against the primary artifact before trusting it — and
validate **each stage separately**, because where it agrees localises the fault.

### The diagnostic that matters is conservation, not agreement

Aggregate agreement statistics ("89% within 10%") hide systematic incompleteness. Ask
instead whether *totals are conserved*:

```python
# per-item agreement — what a naive check reports
ratio = derived / measured
print(f"within 10%: {(abs(ratio-1) <= 0.10).mean():.0%}")

# conservation — what actually diagnoses the source
combined = df.groupby('item')[['derived_len','measured_len']].sum()
print("combined length ratio:", (combined.derived_len/combined.measured_len).median())
print("derived has FEWER records in:",
      (df.groupby('item').derived_n.sum() < df.groupby('item').measured_n.sum()).sum(),
      "of", df.item.nunique())
```

**Conserved total + fewer records = the source omits a category of item.** That is a
systematic bias, not noise, even when most per-item comparisons look fine.

### Real case

A curated AGP was used as a post-curation N50 source. Per-item agreement looked acceptable
(median ratio 1.0008, 89% within 10%), and its README attributed the 11% tail to "a
different curation round". Conservation checks showed otherwise:

| Check | Result | Reading |
|---|---|---|
| Combined length, both haplotypes | 51/52 within 0.5%, median 1.0000 | Same sequence |
| Record count | **fewer in 52 of 52**, median ratio 0.62 | Omits small unplaced scaffolds |
| Per-haplotype split | complementary errors (x0.892 / x1.113) | Partial misassignment |
| **Pre-curation stage** | **100% within 10%** | **Parser arithmetic is sound** |

Omitting small scaffolds *inflates* N50, so the bias is universal and only visible when the
omitted records are large enough to move the statistic. The source was dropped and the
affected items re-measured from the primary artifact.

### Stage-wise agreement localises the fault

If a derived source is exact at one stage and divergent at another, the parser is fine and
the *input* is incomplete. Testing only the stage you care about would have missed this.

### Rule

Prefer measuring the primary artifact over parsing a derived representation of it, when the
primary is reachable. A derived source that cannot be validated against ground truth should
carry a documented caveat or be excluded — not silently ranked lower.
