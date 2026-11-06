---
name: data-analysis-patterns
description: Best practices for data aggregation, recalculation, and category management in scientific analyses. Covers when to recalculate vs reuse aggregated data, handling category changes, and ensuring analytical accuracy.
version: 1.0.0
context: fork
allowed-tools: Read, Grep, Glob, Bash
---

# Data Analysis Patterns

Expert guidance for making critical decisions in data analysis workflows, particularly around aggregation, recalculation, and maintaining analytical integrity.

## When to Use This Skill

- Deciding whether to recalculate from raw data vs reuse aggregated data
- Changing category definitions in existing analyses
- Ensuring accuracy in publication-quality analyses
- Handling conflated features that need separation
- Optimizing analysis pipelines without sacrificing correctness
- Merging multi-source datasets with composite keys
- Handling DataFrame type conversion issues during enrichment

## Core Patterns

### 1. Recalculating vs Reusing Aggregated Data

When you have pre-aggregated data but need different categories or groupings:
- **Recalculate from raw data** when category definitions fundamentally change, previously conflated features need separation, aggregation criteria change, or publication accuracy is critical
- **Approximation may be acceptable** for exploratory analysis, when categories align closely, or when raw data is unavailable
- **Rule**: If you can't confidently map old to new without information loss, recalculate

> For detailed patterns and code examples, see [data-manipulation-recipes.md](data-manipulation-recipes.md)

### 2. Composite Keys for Multi-Source Data Merging

When merging datasets from multiple sources, a single identifier often isn't unique enough:
- Create composite keys by concatenating multiple fields with a delimiter (`|` or `::`)
- Always verify uniqueness after creating the composite key
- Handle duplicates explicitly before merging (latest date, then most complete record)
- Remove composite key before final save (temporary working column)

> For implementation details, see [data-manipulation-recipes.md](data-manipulation-recipes.md#composite-keys-for-multi-source-data-merging)

### 3. Separating Conflated Features

When one metric combines multiple independent features, separate into independent analyses:
- Identify which features are mixed in each category
- Create separate category systems for each independent feature
- Enables clear interpretation and future independent analysis

> For examples, see [data-manipulation-recipes.md](data-manipulation-recipes.md#separating-conflated-features)

### 4. DataFrame Type Conversion During Enrichment

Type mismatches are common when enriching DataFrames from external sources:
- Check target column dtype before assignment
- Convert values to match target dtype (easier than converting whole column)
- Use helper functions to encapsulate type checking logic
- Handle NaN explicitly with `pd.notna()` checks

> For the type-safe assignment pattern and examples, see [data-manipulation-recipes.md](data-manipulation-recipes.md#dataframe-type-conversion-during-enrichment)

### 5. AWS Data Enrichment Patterns

When enriching tabular data from AWS S3 or external repositories:
- Use multi-source path resolution (direct lookup + path inference)
- Auto-detect most complete input file for idempotent re-runs
- Add columns idempotently (check before adding)
- Use TEST_MODE for initial validation before full enrichment

> For implementation patterns, see [enrichment-patterns.md](enrichment-patterns.md)

### 6. Critical Data Validation

Column names don't always match their content. Always verify against source code before using categorical columns:
- Locate source script and verify assignment logic
- Add assertions for biological plausibility
- Test with known control samples
- Document and fix any mismatches found

> For the full verification workflow and prevention checklist, see [validation-patterns.md](validation-patterns.md)

### 7. Data Provenance Verification

Derived columns may use inferior sources, causing silent data loss:
- Compare derived column coverage against likely source columns
- Cross-tabulate to verify mapping consistency
- Prefer reclassifying from rich source columns over merging sparse external files

> For diagnostic patterns, see [validation-patterns.md](validation-patterns.md#data-provenance-verifying-derived-vs-source-columns)

### 8. Organizing Analysis Text for Token Efficiency

Separate computation (notebooks) from interpretation (markdown files):
- Create `analysis_files/` directory with per-figure markdown files
- Keep notebooks for code, analysis files for interpretation
- Token reduction: 98% (1.1M tokens notebook vs 22K tokens analysis files)

> For directory structure and writing guidelines, see [analysis-organization.md](analysis-organization.md)

### 9. Multi-Factor Experimental Design Analysis

When experimental design has multiple factors:
- Use three-category design to isolate individual factor effects
- Compare pairs controlling for one factor at a time
- Identify synergistic, dominant, or antagonistic interactions

> For interpretation framework and examples, see [analysis-interpretation.md](analysis-interpretation.md)

### 10. Interpreting Paradoxical Results

When one category performs better on metric X but worse on related metrics Y and Z:
- Apply the trade-off hypothesis framework
- Document counter-intuitive results transparently
- Explore mechanistic explanations rather than dismissing findings

> For documentation patterns, see [analysis-interpretation.md](analysis-interpretation.md#interpreting-paradoxical-or-contradictory-results)

### 11. Species Name Reconciliation

When external services use different species names than your metadata:
- Classify mismatches into systematic replacements vs name variants
- Use fuzzy matching for variant detection
- Propagate corrections to ALL related files
- Version files to track correction stages

> For reconciliation workflow and code, see [species-reconciliation.md](species-reconciliation.md)

### 12. Phylogenetic Tree Coverage Analysis

Track what percentage of your phylogenetic tree has data available:
- Calculate coverage metric and identify missing species
- Categorize missing as recoverable, phylogenetic context, or unknown
- Recover Time Tree proxy replacements from deprecated datasets
- Document expected vs unexpected missing data

> For coverage analysis workflow, see [species-reconciliation.md](species-reconciliation.md#phylogenetic-tree-coverage-analysis)

### 13. Distinguishing True Variation from Power Limitations

When analyzing multiple groups, determine if lack of effect is real or insufficient power:
- **Power limitation indicators**: Small sample, trend in expected direction, category imbalance, wide CIs
- **True null indicators**: Large sample with narrow CIs, opposite direction from other groups, significant in some metrics but not others
- Report appropriately: "insufficient power" vs "no effect despite adequate power"

> For reporting recommendations and examples, see [analysis-interpretation.md](analysis-interpretation.md#distinguishing-true-variation-from-power-limitations)

### 14. Technology Confounding Analysis

Temporal trends may reflect technology adoption rather than methodology improvements:
- Use three-stage approach: mixed-technology baseline, technology-controlled subset, comparison
- Test orthogonality, persistence, and temporal patterns
- Decision matrix for whether to pool across technologies

> For the systematic testing approach, see [analysis-interpretation.md](analysis-interpretation.md#confounding-analysis-technology-and-temporal-effects)

### 15. Data Consolidation and Enrichment Workflows

When working with multiple intermediate dataset versions:
- Follow Consolidate -> Enrich -> Verify pattern
- Always rebuild filtered subsets from enriched master (don't manually merge)
- Extract accurate dates from repository filenames when release dates are unreliable

> For workflow details, see [enrichment-patterns.md](enrichment-patterns.md#data-consolidation-and-enrichment-workflows)

### 16. Data File Compression Strategies

For large data files, compress instead of delete:
- Decision tree: active (keep) / regenerable (delete) / archive (compress)
- BED/VCF/FASTA compress 70-90% with gzip
- Update scripts to read compressed files directly
- Document compression in READMEs

> For compression benchmarks and workflows, see [compression-strategies.md](compression-strategies.md)

### 17. Verify You're Reading All Available Sources

When a build/combine script exists, **read its output, not its inputs**:
- A notebook reading one upstream file directly silently misses whatever the combiner merged in
- Quantify coverage per group against the full population before analysing
- Uneven coverage across compared groups is a selection bias, not just a smaller n

> For the coverage-check recipe and a worked case, see [validation-patterns.md](validation-patterns.md#verify-youre-reading-all-available-sources)

### 18. Check Denominator Provenance Before Claiming a Trend

A derived ratio can trend purely because its denominator changed annotation source:
- Crosstab the `*_src` column against the time axis before reporting any temporal claim
- Compare the metric within each source, and check whether the trend survives
- The confound travels with the denominator — find every other metric that shares it

> For the diagnostic pattern and a worked case, see [validation-patterns.md](validation-patterns.md#denominator-provenance-vs-the-temporal-axis)

### 19. Check Derived Ratios for Circularity

A ratio whose denominator falls back to its numerator returns 1.0 by construction:
- Detect with `numerator == denominator`, grouped by the denominator's source
- A source where that holds for ~100% of rows is a fallback, not a measurement
- Where the denominator is unknown the metric must be **NA**, never a copy of the numerator
- Expect coverage *and* the headline rate to drop once the fallback is removed

> For the detection recipe and a worked case, see [validation-patterns.md](validation-patterns.md#circular-derived-metrics)

### 20. Encode Source Precedence in Code, Not Convention

When a dataset merges several generations and enrichment passes, write the precedence down
as an ordered list and enforce it with a script:

    1. current freeze   2. previous freeze   3. enrichment on current keys   4. older enrichment

A lower tier may only **fill a gap**, never overwrite a higher tier. Audit by comparing each
tier-1 column against the authoritative file and counting `overrode` versus `gap-filled`.

- Encode documented normalisations (e.g. `?` -> NA) so they are not misread as violations
- Assert no violations remain after repair, and make the script idempotent

> In one project the rule held **by accident** — it was a property of the order enrichment
> happened to run in. The audit script found the only real violation was one introduced
> the same day by a bad repair.

### 21. Read the Formula Before Diagnosing a Metric

Column names imply formulas that are often wrong:
- Find the assignment in the build code (`grep -rn 'df\["metric"\]\s*='`) **and** verify numerically
- When two candidate columns both fit the data, a numeric check cannot discriminate — go to the source
- A wrong formula propagates into every downstream conclusion

> For two worked misses, see [validation-patterns.md](validation-patterns.md#read-the-formula-before-diagnosing-the-metric)

### 22. Validate a Derived Source Against Ground Truth

A source parsed or transcribed from something else can be systematically incomplete while
looking only occasionally divergent:
- Per-item agreement statistics hide it; **conservation checks expose it**
- Conserved total + fewer records = the source omits a category of item
- Validate **each stage separately** — exact at one stage and divergent at another means the
  parser is fine and the input is incomplete
- Prefer measuring the primary artifact when it is reachable

> For the conservation recipe and a worked case, see [validation-patterns.md](validation-patterns.md#validate-a-derived-source-against-ground-truth)

### 23. Never Use Attribute Access for Columns That Shadow DataFrame Methods

`df.colname` silently resolves to the DataFrame *method* when one exists with that name.
No error, no warning — comparisons return False and filters come back empty.

Collisions seen in practice: `pipe`, `pct_change`, `size`, `count`, `min`, `max`, `mean`,
`sum`, `std`, `index`, `shape`, `values`, `rank`, `diff`, `first`, `last`, `name`.

```python
m[m.pipe == "VGP"]        # WRONG — silently always empty, no exception
df.pct_change.dropna()    # WRONG — AttributeError: 'function' has no attribute 'dropna'

m[m["pipe"] == "VGP"]     # RIGHT
df["pct_change"].dropna() # RIGHT
```

**Rule**: bracket access for any column you did not personally name, and for any derived
column. When a groupby or filter returns unexpectedly empty, check this **before**
concluding the data is wrong — the `.pipe` case produces no traceback at all.

### 24. Build Figure Data as a Source Table That Asserts Against the Rendered Figure

When several panels share a dataset, build one table and express each panel's cohort as a
boolean column (`in_fig2a`, `in_fig2b`, ...) rather than filtering separately per panel.
Then hard-code the counts printed on the *rendered* figure and assert them:

```python
EXPECTED = {"fig1a_Mammals": 217, "fig2b_Phased+Dual": 201, ...}
bad = {k: (v, got.get(k)) for k, v in EXPECTED.items() if got.get(k) != v}
if bad:
    raise SystemExit("Table disagrees with the figures; not written.")
```

**Why it pays**: when an upstream refresh moved 149 category values, the build failed
loudly with a per-panel diff instead of quietly emitting a table whose numbers no longer
matched the manuscript. Re-baselining becomes a deliberate, reviewed step.

**Derive the new baseline, don't retype it** — import the builder and recompute, so the
new EXPECTED cannot contain a typo.

**Caveat — row order is part of the output.** Figure scripts that jitter scatter points
with a fixed-seed RNG consume rows in order, so re-sorting the source table changes the
rendered figure cosmetically while every statistic stays identical. Preserve upstream row
order and comment why, or the next person will "tidy" it with a sort.

### 25. Before Reporting a Categorical Difference, Check It Isn't a Batch/Source Effect

A comparison between categories is only about the categories if the categories are not
confounded with where the data came from. Cross-tabulate first:

```python
pd.crosstab(df.category, df.source_institution)
```

Seen in practice: method A was 89% institution X and method B was 91% institution Y, so a
"method" difference (p=3e-3) was substantially an institution difference — it fell to
p=0.83 when repeated **within** the one institution that ran both methods.

**Diagnostics that settle it:**
- Repeat the test **within** each source; report the within-source result as primary
- Test a **negative control** metric the treatment cannot affect (e.g. a value fixed
  upstream of the treatment). If that also differs between sources, the sources differ for
  reasons unrelated to the treatment
- Check whether candidate confounders run the *right way* — two candidates here predicted
  the opposite of the observed effect, which ruled them out rather than explaining it

**Beware n moving the wrong way.** Sample size doubled while significance *fell* — that is
a composition change, not a power change, and is a signal to investigate.

**Three refinements, from a case where the within-source test passed but the analysis was
still wrong:**

**The confound can be larger than the effect you are measuring.** One metric differed ~6x
between the categories of interest and 14-17x between the two institutions that produced
them. When the confound exceeds the signal, pooled summary values are not reportable even
when the within-source *ranking* is intact.

**Surviving the within-source test licenses the ranking, not the values.** The category
ordering held inside each institution, and a phylogenetic-signal statistic held at nearly
full strength inside each (0.82-0.88 against 0.887 pooled). Both were real. The pooled
per-category *medians* were still a blend of biology and institution, and a legend reporting
them as properties of the category would have been wrong.

**Re-test every subgroup claim, not just the headline.** The overall statistic survived and
so did two of four named subgroups — but one fell from 0.50 (p = 6e-5) to 0.00 (p = 1)
within a single institution, because that institution contributed half its output in that
subgroup. A headline that survives says nothing about the per-subgroup claims beneath it.

**Construct the maximally-matched comparison.** The decisive evidence was not a pooled test
but a cell where everything except the suspected confounder matched: same taxonomic order,
same tool, same tool mode, n ~ 10 each — and still 10x apart. One such cell is worth more
than a model with covariates, because nothing has to be assumed away.

### 26. Each Figure Panel Reads the Source Afresh

A panel that reuses a variable another panel already filtered inherits that filter silently.
One panel's category lookup reused a frame filtered to species *with telomere data*, quietly
dropping 6 of 98 pri/alt species. The counts looked plausible; only an assertion against
expected totals caught it.

```python
cat_by_sp = te.set_index("scientific_name").category_combined   # WRONG: te is filtered
cat_by_sp = pd.read_csv(SRC, sep="\t").set_index(...)           # RIGHT
```

Name filtered frames for their filter (`hifi_only`, not `df`) so reuse is obviously wrong.

### 27. Removing a Bad Value: Find Every Consumer First

A single wrong value propagates further than the obvious path. One back-filled category
(*Anomalurus derbianus*, carried as `Phased+Dual` when the authoritative freeze left the
cell blank) was living in four places:

    vgp_assemblies_817.csv              the master, where the back-fill was written
    species_4category_methods_*.csv     a derived file regenerated FROM the master
    itol_4category_colorstrip_*.txt     a config generated from that derived file
    scaffold_n50_pre_post_curation.tsv  reached the figure by a DIFFERENT column

The fourth is the one that caught me out. Figure 2's group assignment came from the pre/post
file's own `curation_method`, not from the category I had just cleared — so clearing the
category changed nothing there, and I reported the figure as unaffected. It wasn't: the
cohort moved 586 -> 584 and a published median moved +0.5% -> +0.4%.

**Enumerate consumers mechanically, don't reason about which ones "should" matter:**

    grep -rl "Anomalurus\|AnoDer" data/ data-processing/ | while read f; do
        printf "%-60s %s\n" "$f" "$(grep -ih "anomalurus" "$f" | head -1 | \
            grep -oiE "Phased\+Dual|Other/Unknown|#[0-9A-Fa-f]{6}" | tr '\n' ',')"
    done

Then check each consumer's *input column*, because a file can carry the same fact under a
different name. Fix at the root — the master — so regenerating downstream files is enough.

### 28. Derive Cohort Flags From One Canonical Field, Never From Membership of a Sibling File

`in_3category_set` was "is this species a row of `vgp_assemblies_3categories.csv`".
`tree_category` was derived from the authoritative freeze. They agreed for months, then
one species was reclassified and the same table carried two answers: the flag said 726,
the category said 725. Nothing broke loudly — the panels that use the flag also require a
technology, which that species lacks — so it would have sat there until someone counted it.

    t["in_3category_set"] = t.scientific_name.isin(set(d3.scientific_name))   # WRONG
    t["in_3category_set"] = t.tree_category.isin(CATS)                        # RIGHT

Keep the sibling file if it is still an input, but **print what it contains that the
canonical field does not** — that difference is a bug report:

    stale = set(d3.scientific_name) - set(t.loc[t.in_3category_set, "scientific_name"])
    if stale:
        print("in the old file but not in the three categories: " + ", ".join(sorted(stale)))

### 29. Prove a Rewritten Pipeline Against Its Predecessor, Column by Column

Rewriting a 500-line builder into a readable derivation is worth doing, and it is also how
silent differences get introduced. "It produces the same figure" is not proof — a figure
hides representation changes and tolerates rounding.

Compare every derived column across every row, and every value of the long-form companion:

    for c in DERIVED_COLUMNS:
        a = new.set_index(KEY)[c]; b = old.set_index(KEY)[c]
        both_na = a.isna() & b.isna()
        assert (both_na | (a.astype(str) == b.astype(str))).all(), c

Two real differences surfaced this way, neither visible in the rendered figure:

- **`None` vs `NaN`.** A function returning Python `None` gives the column dtype `object`;
  the same column read back from CSV is `NaN`. `str()` makes them `"None"` and `"nan"`.
  Normalise before writing, and compare NaN-aware.
- **Key casing.** Two sources spelled one ToLID `fgasAcu3` and `fGasAcu3`. The old code
  matched on a lowercased key and silently absorbed it; the new code joined on the raw key
  and lost two rows. The data was identical — only the join key differed.

### 30. A Suspicious Value Gets Verified Against an Independent Source Before It Gets Explained

When a number looks wrong, the instinct is to explain it. Establish first whether it *is* the
number. Explanation built on an unverified value is wasted, and worse, it is persuasive.

The ladder, cheapest first:

1. **A second computed source.** One often already exists in the project — a collaborator's
   export, an upstream manuscript's supplementary table, an older freeze. Join on the exact
   primary key, not a secondary one: in one case a sample ID matched while the accession did
   not, because the freeze carried a *newer assembly of the same species*. Comparing those
   would have invented a discrepancy.
2. **The primary repository.** `datasets summary genome accession <ACC>` returns canonical
   values, and its submitter field independently confirms the group attribution you are
   about to blame.
3. **Only then interpret.**

Outcome in practice: 508 of 532 values identical to the digit across two independent sources,
none differing by more than 10%, and the repository confirmed every spot check. The anomaly
was real, which redirected the investigation from "our pipeline is wrong" to "these groups
differ" and saved a pointless audit of the extraction code.

**Then rule out the mundane explanations explicitly, and say which you ruled out.** Different
tool, different tool version, different parameters, group size, composition, mislabelling.
Listing the eliminations is what makes the surviving explanation credible — and the one that
survived here (input quality driving read length) could not be tested with the data to hand,
so it had to be reported as an inference rather than a finding.

## Joins on free-text names fail silently

A merge keyed on a species name, a gene symbol, a sample label — any human-entered
string — will not match everything, and the usual idiom throws the misses away without
saying so:

```python
df["cat"] = df.name.map(lookup)      # no match -> NaN
df = df[df.cat.isin(WANTED)]         # NaN is not in WANTED -> row gone
```

No warning, no count, nothing downstream to show a row was ever there. In a figure the
bar just gets shorter. Found in production 2026-10-05: 7 of 188 species silently absent
from a published panel, and *three of them belonged in it*.

**Make the join assert its own coverage.** The filter is what hides the loss, so fail
before it:

```python
df["cat"] = df.name.map(lookup)
lost = sorted(df.loc[df.cat.isna(), "name"])
assert not lost, f"{len(lost)} rows do not join: {lost}. Add them to {CROSSWALK}."
df = df[df.cat.isin(WANTED)]
```

### Name mismatches are rarely typos

Of those seven, only one was an error. The rest were legitimate alternative names, and
each needs a different rule:

| cause | example |
|---|---|
| subspecies trinomial on one side | `Peromyscus maniculatus` vs `P. maniculatus sonoriensis` |
| nominate subspecies | `Melospiza melodia` vs `Melospiza melodia melodia` |
| identifier suffix | `Gorilla gorilla` vs `Gorilla gorilla 9595` |
| taxonomic synonym / renamed genus | `Astur gentilis` vs `Accipiter gentilis` |
| genuine typo | `Monodon monocero` vs `monoceros` |

A **genus rename shares only the epithet**, so no string-distance threshold finds it
without also producing false positives. Record those in an explicit, commented crosswalk
rather than loosening the fuzzy match.

### Fix with a crosswalk, not by editing the source

The source table usually belongs to someone else, and most mismatches are not errors in
it. A `{their_name -> our_name}` TSV carrying the *reason* for each row keeps both tables
intact, makes the mapping reviewable, and leaves the typo visible for its owner to fix.

### Prefer a controlled key wherever one exists

Audit which joins key on free text and which on an identifier. In the project above,
every other join used `tolid` or an underscored tree-leaf name; the PAR table was the
only free-text one, which is exactly why it was the only one that broke.

### Check for duplicates the same way

The mirror failure is a join that *multiplies* rows. `.map()` with a duplicated index
raises, so only `merge`/`join` can do it — check the right-hand key for duplicates
first. To find species entered twice under two spellings, compare on a
spelling-independent key (taxid, accession), then test for **binomial collisions** —
`Genus species` present alongside `Genus species subsp.` — which a normalised-string
comparison will not catch.

## A source table that ships two versions of one measurement

When a delivered table carries `x` and `x_revised` — or `status` and `status_final`, or a
column plus a "corrected" sibling — **quantify the difference before you use either one.**
The revision may be doing more work than your analysis is.

```python
d = pd.read_csv(src)
print(pd.crosstab(d.status, d.status_revised, margins=True))
changed = d[d.status.astype(str) != d.status_revised.astype(str)]
print(f"{len(changed)} of {len(d)} rows changed")
# The question that matters: is the revision SYMMETRIC across your comparison groups?
print(changed.groupby("group").size())
```

Real case (VGP PAR panel, 2026-10-06). The source table shipped `PAR_status` and
`PAR_status_revised`; the figure plotted the revised one. The original had 138 "collapse"
calls, the revised 113 — **25 moved out, none ever moved in**. And the revision was not
symmetric: **22 of the 25 belonged to one arm of the comparison**, with all 15 of the
most consequential reclassifications in that arm without exception.

| | original | revised (plotted) |
|---|---|---|
| treatment arm | 26 of 48 — 54.2% | 36 of 48 — **75.0%** |
| control arm | 1 of 110 — 0.9% | 1 of 110 — 0.9% |
| Fisher | *P* = 4.1 × 10⁻²⁰ | *P* = 2.8 × 10⁻³² |

The control moved by one row. The treatment gained 21 points. **The revision, not the
measurement, was carrying the result.**

There is usually an innocent explanation and it is often correct — here, a collapsed
single-haplotype assembly has nothing a second look could change, while a phased one can be
re-examined and found positive. Asymmetric *re-examination opportunity* produces asymmetric
*revision* with no bias at all. But that argument has to be made in the Methods, not assumed:

- **Report that a revision happened**, with the criteria, in the Methods.
- **Show both numbers** if the delta is larger than the effects you are reporting.
- A reviewer who has the source table will reconstruct this in minutes. Better that you did.

**The general rule:** any filter, revision or re-scoring applied unevenly across comparison
groups is a potential confound, and "it was applied by someone else, upstream" does not
exempt it. Check the symmetry of every *selection* step, not just the measurement.

---

## Before calling another table wrong, date-match it against the truth source

Two tables disagree. The authoritative one wins — that part is easy. But **"the other table
is wrong" and "the other table was built when the truth source said something else" are
different findings with different fixes**, and the second is invisible unless you look at
what the truth source held *on the day the other table was made*.

```bash
git log --diff-filter=A --format='%ad' -- path/to/other_table.csv   # when was it made?
ls archive/freezes/                                                  # what did truth say then?
```

```python
# reconstruct the authoritative category from EACH archived version
for f in sorted(glob.glob("archive/freezes/*.tsv")) + [CURRENT]:
    d = load(f); print(os.path.basename(f), d.loc[SPECIES, "category"].to_dict())
```

Real case (2026-10-06). Four species were labelled `Pri/alt` in a collaborator's table and
`Phased+Dual` in the freeze. Checking the archived freezes split them cleanly:

- **Two were a timing artefact.** They read `Phased + ?` — curation type *undetermined* — in
  the freeze that was current when the collaborator's table was committed. A later drop
  resolved both. The compiler had no value to copy and defaulted.
- **Two were genuine errors.** They were already `Phased+Dual` before that table existed.

Same disagreement, same resolution in the figure — but what you write to the compiler changes
from "four cells are wrong" to "two cells to correct; the other two the freeze has since
resolved, no action needed." The first version is wrong and reads as an accusation.

**Keep superseded versions of the truth source** (`archive/freezes/<name>_superseded_<date>`)
precisely so this check is possible. An undetermined value that was later filled in is the
single most common cause of a stale downstream label.

---

## Name and document derived columns by their provenance

A column named like an authoritative field will be *read* as an authoritative field. If it
is derived, say so in the name or in the shipped documentation — ideally both.

Real case (2026-10-06): a shared table carried `derived_category_combined`, and the reader
still had to ask "is this the category from the freeze?" It half was. The freeze stores two
separate columns, `Assembly type` and `Curation type`; the shipped column was those two passed
through a documented reconstruction rule — **and then a post-hoc transform applied to 34 of
835 rows.** Neither step was visible from the name.

When exporting a joined table for someone else:

1. **Prefix columns by source.** `PAR_*` for one table, unprefixed for the other, and name the
   joined/derived fields explicitly. The reader should never have to guess which file a column
   came from.
2. **Ship the derivation rule verbatim**, not a description of it:
   ```
   curation type == "T2T"        ->  "T2T"       (not "Haploid T2T+T2T")
   assembly or curation missing  ->  "Unknown"
   otherwise                     ->  "<assembly type>+<curation type>"
   ```
3. **Include the raw inputs in the same file** so the reader can verify the rule themselves.
   Costs two columns; removes the question entirely.
4. **Document post-hoc transforms separately from the rule**, with their blast radius:
   *"across the full 835 rows the column is rule-derived AND THEN folded — applying the rule
   to the raw source disagrees for exactly 34 rows, all deliberate. None in this extract."*
5. **Verify the rule reproduces the column** before you claim it does:
   ```python
   assert (df.apply(lambda r: rule(r.a, r.b), axis=1) == df.derived).all()
   ```

A reader asking "where did this column come from?" is a documentation defect, not a reader
defect.

---

### Reproduce a published number with the pipeline's own normalisation

When re-deriving a number a figure already reports, **run it through the same normalisation
the figure uses** — not a fresh one-liner. A shortcut that skips a `.str.strip()` will
"discover" a discrepancy that does not exist, and you will report it before checking.

Real case (2026-10-06): an ad-hoc recount of a figure panel returned 175 species against a
legend claiming 176. One species carried a **trailing space** in the source table. The
pipeline stripped it; the recount did not. The figure was right.

```python
# wrong: fresh join, fresh assumptions
par["cat"] = par["Scientific.Name"].map(lookup)
# right: whatever the figure does, verbatim
par["sp"]  = par["Scientific.Name"].str.strip().replace(CROSSWALK)
par["cat"] = par.sp.map(lookup)
```

Cheapest guard: read the normalisation out of the generating script before recomputing, and
if your number disagrees, **suspect your shortcut before you suspect the figure.**

## Fixing a derived file in place leaves the generator armed to revert

When a value is wrong in a file that a script produces, there are two places to fix it: the
file, and the script that writes it. Fixing only the file leaves a **revert armed** — the next
person to run the generator silently restores the old value, and nothing reports it.

This happened twice in one week on the same project.

- A release-date column was switched to a different source column by rewriting the master CSV
  in place. The two builders that derive that column were left reading the old one. Any rerun
  would have put 91 wrong years back.
- A figure's panels were regenerated correctly, but an **older, unrelated script** also wrote
  the same output filename as a side effect. Running it for its statistics reverted the panels
  to a stale palette and stale counts. Nobody noticed for six days.

**Why in-place fixes are tempting and still wrong.** Rebuilding from scratch can be the worse
option — the derived file may carry manual repairs the generator does not know about. That is a
real reason to patch in place. It is not a reason to skip the generator.

**How to apply**

1. Fix the derived file (in place if it carries repairs a rebuild would discard).
2. **Fix the generator in the same pass.** Not "later", not on the TODO.
3. Ask what else writes this path: `grep -rl "<output filename>" scripts/`. A file can have
   more than one producer, and the stale one wins whenever it runs last.
4. If a script writes an output it is not named for, put a warning at the top of it naming the
   defect and pointing at the right generator. A comment is cheaper than the next six days.

**The tell**: you changed a number in a `data/` or `figures/` file and did not open anything in
`scripts/`. That is the shape of a revert waiting to happen.


## Two R-squared from separate models are not a partition of the variance

Reporting "A explains 94% of the variance, against 8% for B" invites the reader to add them up,
and they do not add up — in the case this is drawn from, to 102%. The two numbers came from two
**single-predictor** models, and the predictors were correlated, so the same variance is counted
twice.

**What to compute instead** is the *incremental* contribution:

```python
r2_a    = fit(y ~ a)          # 94.24%
r2_b    = fit(y ~ b)          #  7.47%
r2_both = fit(y ~ a + b)      # 94.24%   <- b adds +0.01 points over a alone
```

The honest sentence is then: *B accounts for 7% on its own, but adds less than 0.1 percentage
points once A is known, because the two are not independent.* That is both correct and a
**stronger** claim than the original phrasing — it says B contributes nothing, rather than
leaving the reader to infer it from a ratio.

**How to apply**

- Never place two single-predictor R-squared side by side with "against". Either give the
  incremental value, or give one R-squared and a separate test.
- If they sum to more than 100%, that is not a rounding problem — it is the predictors
  overlapping, and the overlap is usually the interesting part.
- Pair it with a residual test (does B explain anything in the residuals of A?) which makes the
  same point without any R-squared at all.


## "Shift of the median" is not "median of the shifts"

These are different statistics and they can differ by an order of magnitude on the same group:

```
shift of the median  = (median(post) - median(pre)) / median(pre)      # +19.1%
median of the shifts = median((post - pre) / pre)  per unit            #  +1.7%
```

Both were printed on one figure panel — the first as bold labels, the second as a footnote —
and the panel read as self-contradictory. The reviewer's reaction was "the numbers seem wrong",
which was the right instinct for the wrong reason: both were correct.

**Prefer the median of the per-unit shifts.** The shift of the median depends on where the
group's median happened to sit, which is a property of **who is in the group** rather than of
whatever treatment is being measured. A group that starts low will show a large shift of the
median from an ordinary per-unit change, and that difference will be read as an effect.

The concrete consequence: a category whose shift-of-median was +19.1% — the largest in the
figure, and quoted in the text as "gained the most" — turned out to be **mid-pack at +1.7%** on
the per-unit measure, below a category the text was contrasting it against.

**How to apply**

- Pick one and say which. "Median change per haplotype", not "change".
- Do not show both on one panel. If both are needed, they belong in different places with
  different labels.
- Before writing "X gained the most", check that the ranking survives the switch between them.


## Normalise missing values before diffing two versions of a table

`.astype(str)` is the obvious way to compare two columns without tripping over dtypes, and it
manufactures differences: it maps `NaN` to the string `"nan"` and an empty cell to `""`. If one
version of a file has blanks where the other has nulls — routine across a CSV/TSV round trip —
every one of those rows reports as changed.

In the case this comes from, that produced a false report of "18-20 changed rows including
assembly type and curation type" for a file that was **byte-identical** across all 41 shared
columns. The wrong conclusion ("this is a new freeze drop, re-derive everything") was acted on
for several minutes before the comparison was redone.

```python
norm = lambda col: col.map(lambda v: "" if pd.isna(v) else str(v).strip())
diffs = {c: int((norm(a[c]) != norm(b[c])).sum()) for c in shared_columns}
```

**How to apply**

- Sort both frames by the key and assert the key columns match before comparing values.
- Check for duplicate keys first — a merge on a duplicated key pairs rows arbitrarily and every
  value then looks different.
- When a diff reports suspiciously many changes in columns nobody edited, suspect the
  comparison before the data.



## Stratify before comparing groups drawn from different measurement sources

When a value can arrive by several routes, **check the provenance mix of the groups before
comparing them**. A difference in how a quantity was measured will masquerade as a difference
in what was measured, and it does so most convincingly when the groups' mixes are opposite.

Worked case. Two pre-curation baselines fed one column. On **known-identical cases** -- the
curated haplotypes alone, where no real difference can exist -- they gave +2.63% vs +0.71%
median change and 13.2% vs 25.1% negative. The two compared groups were 87% one baseline and
57% the other. Unstratified the comparison looked decisive (Fisher P = 0.002); within a single
baseline it was **P = 0.18**. The measurement reproduced nearly the whole apparent effect.

**The diagnostic that sizes the artefact**: run the comparison *within the control group only*,
split by provenance. Any difference there is pure measurement, because the biology is held
constant. If it is the same magnitude as your headline effect, the headline is the artefact.

Then either stratify and report within-stratum results, or restrict to one provenance and say
how many rows that costs. Do not pool and hope.

Related: [Name and document derived columns by their provenance](#name-and-document-derived-columns-by-their-provenance).

## Key Principles

1. **Default to recalculation** when category definitions change, features were conflated, or publication accuracy is needed
2. **Document approximations** when used, and validate against subsets of recalculated data
3. **Separate conflated features** into independent analyses for clarity
4. **Always verify column names** against source code before analysis
5. **Check dtype before assignment** when enriching DataFrames
6. **Rebuild filtered subsets from master** rather than manually merging new columns
7. **Test for technology confounding** before pooling across technology generations
8. **Compress rather than delete** data files that may be needed later
9. **Read a combiner's output, not its inputs** — and check per-group coverage before comparing groups
10. **Check denominator provenance** before reporting a temporal trend in any derived ratio
11. **Test derived ratios for circularity** — a denominator that falls back to the numerator gives 1.0 for free
12. **Confirm a metric's formula from the build code** before interpreting it
13. **Never back-fill a derived value from an older dataset generation** — if it isn't computable now, it's NA
14. **Trace a bad value to every consumer before declaring the blast radius** — including consumers that reach it by a different column
15. **One canonical field per cohort** — never membership of a sibling file
16. **Prove a rewritten pipeline column-by-column against its predecessor**, NaN-aware
17. **Validate derived sources against the primary artifact** — check conservation, not just agreement
17. **When rebuilding an analysis on new data, run three configurations, not one.**
    A = their reference, their cohort (must reproduce the published values — this is the
    proof the rebuild is correct); B = their reference, your data (isolates the data
    update); C = your reference, your data (the result you will publish). Without A you
    cannot tell a real change from a bug; without B you cannot tell a data change from a
    method change. State in the script's header which configuration is the proof, and
    caveat B honestly if it is a reduced cohort rather than a clean swap.

## Best Practices

### Assess Information Loss
Before deciding to reuse aggregated data, check: Can you perfectly reconstruct raw data from aggregates? If NO, recalculate.

### Document Your Decision
```python
"""
Data source: scaffold_telomere_data.csv (n=6,356 scaffolds)
Recalculated: 2026-01-29
Reason: Previous aggregation conflated terminal and interstitial presence
Method: [describe categorization logic]
"""
```

### Validate Against Original if Possible
```python
original_total = df['cat1'] + df['cat2'] + df['cat3'] + df['cat4']
new_total = df['new_cat1'] + df['new_cat2'] + df['new_cat3']
assert (original_total == new_total).all(), "Category totals don't match!"
```

### Time vs Accuracy Trade-off
- **Exploration phase**: Approximations okay, clearly documented
- **Publication phase**: Always recalculate for accuracy
- **Intermediate**: Recalculate once, save results, reuse those

### Performance Considerations
Recalculation is often faster than you think:
```python
# Modern pandas on 10,000+ rows
df['new_cat'] = df.apply(categorize_func, axis=1)
result = df.groupby('species').agg({'new_cat': 'value_counts'})
# Often < 1 second
```

Optimize: use vectorized operations, filter to relevant columns, cache intermediate results.

## Supporting Files

| File | Content |
|------|---------|
| [data-manipulation-recipes.md](data-manipulation-recipes.md) | Recalculation patterns, composite keys, conflated features, type conversion |
| [enrichment-patterns.md](enrichment-patterns.md) | AWS enrichment, data consolidation, date extraction, filtered dataset rebuilding |
| [validation-patterns.md](validation-patterns.md) | Column name verification, data quality checks, data provenance |
| [analysis-interpretation.md](analysis-interpretation.md) | Multi-factor design, paradoxical results, power limitations, technology confounding |
| [species-reconciliation.md](species-reconciliation.md) | Species name reconciliation, phylogenetic tree coverage |
| [analysis-organization.md](analysis-organization.md) | Token-efficient analysis text organization, statistical results population |
| [compression-strategies.md](compression-strategies.md) | File compression decision tree, benchmarks, script updates |

## When groups contribute different numbers of rows per unit, the per-unit summary is not comparable

Aggregating to a common unit ("one value per assembly", "one value per patient") looks like
the conservative move against pseudo-replication. It is not, if the groups contribute
different numbers of rows each.

Real case: diploid-curated assemblies contributed **two** measured haplotypes in 184 of 204
cases; haploid-curated ones contributed **one** in 78 of 87. So "median per assembly" averaged
hap1 with hap2 on one side and used hap1 alone on the other. The second haplotype gained
systematically less (+0.6% against +1.6%, paired P = 0.008), so the asymmetry pulled one arm
down and **widened the very difference the test was measuring**.

**Check before aggregating:**

```python
pd.crosstab(df.group, df.groupby(["unit", "group"]).size().rename("rows_per_unit"))
```

If the distributions differ, the aggregate is not a like-for-like comparison. Options, best
first:

1. **Compare the same sub-unit in both groups** (here, first haplotype against first
   haplotype). No imputation, nothing discarded, one comparable value each.
2. **Restrict one group to complete units** where that is an artefact rather than the finding
   - and state which it is. Here the diploid arm's 20 incomplete units were a data-coverage
   gap, while the haploid arm's incompleteness *was* the result, so only the first was paired.
3. **Keep all rows and model the clustering** - but a cluster permutation is invalid when
   cluster *size* is itself associated with group, which is exactly this situation.

Never impute the missing sub-unit with a neutral value. Filling the absent second haplotype
with "0% change" moved P from 0.09 to 0.71 by asserting something already measured to be
false.

**Watch the P value across corrections.** Here it went 0.0065 (naive pooled) -> 0.050 (per
assembly) -> 0.086 (after an invalid-row exclusion) -> 0.13 (like-for-like). A result that
weakens monotonically as each bias is removed was being carried by those biases, and the
honest claim is the last one.

## A non-significant test is not evidence of no difference - adjust the comparison instead

The tempting write-up is "we tested whether X confounds the result and it did not". It
invites a power objection, and often deserves one.

Before writing that sentence, compute what the test could have detected:

```python
for d in np.arange(0.5, 30, 0.5):               # candidate true shift
    hits = sum(stats.mannwhitneyu(rng.choice(a, len(a)),
                                  rng.choice(b, len(b)) + d)[1] < 0.05
               for _ in range(300))
    if hits / 300 >= 0.80:
        print("detectable from", d); break
```

Real case: three within-category tests gave P = 0.23-0.44, which read as "no confounding".
The minimum detectable shift was 1.5 points in the one well-powered cell but **14 points** and
**8.5 points** in the other two (n = 16 and n = 10). Those P values said nothing.

**The defensible version makes a claim about the comparison of interest, not about the
confounder**: stratify and show the result does not move.

```python
# van Elteren: stratified Wilcoxon rank-sum, weights 1/(n_stratum + 1)
num = den = 0.0
for _, d in df.groupby(stratum):
    x = d.loc[d[g] == g1, val].values; y = d.loc[d[g] == g2, val].values
    n1, n2, n = len(x), len(y), len(x) + len(y)
    if n1 < 2 or n2 < 2: continue
    r = stats.rankdata(np.concatenate([x, y]))
    _, cnt = np.unique(np.concatenate([x, y]), return_counts=True)
    vw = n1 * n2 / 12 * ((n + 1) - (cnt**3 - cnt).sum() / (n * (n - 1)))
    w = 1 / (n + 1)
    num += w * (r[:n1].sum() - n1 * (n + 1) / 2); den += w**2 * vw
z = num / np.sqrt(den); p = 2 * stats.norm.sf(abs(z))
```

"Adjusting for it moved P from 0.16 to 0.17" is evidence. "We failed to reject a difference on
16 observations" is not. Bound the effect too - a Hodges-Lehmann shift with a bootstrap CI
turns "not significant" into "no larger than X".
