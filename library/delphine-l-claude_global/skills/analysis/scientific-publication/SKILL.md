---
name: scientific-publication
description: Best practices for iterative refinement of publication-quality scientific figures. Covers systematic improvement workflows, layout optimization, and ensuring all figure elements are publication-ready.
version: 1.0.0
context: fork
allowed-tools: Read, Grep, Glob, Bash
---

# Scientific Publication Figure Refinement

Expert guidance for systematically improving scientific figures through iterative refinement based on user feedback and publication requirements.

> **Supporting files in this directory:**
> - [publication-standards.md](publication-standards.md) - DPI, file formats, size specs, color accessibility
> - [multi-study-results.md](multi-study-results.md) - Writing integrated results from multi-study analyses and practical recommendations from complex trade-offs
> - [methodological-transparency.md](methodological-transparency.md) - Dual approach pattern for figures vs statistics, outlier handling
> - [overleaf-packages.md](overleaf-packages.md) - Creating production-ready Overleaf packages with templates and checklists

## When to Use This Skill

- Improving figures based on reviewer or collaborator feedback
- Optimizing figure clarity and readability
- Ensuring all figure elements fit within bounds
- Deciding between layout alternatives (horizontal vs vertical panels)
- Preparing figures for high-impact publications

## Iterative Figure Refinement Workflow

### Standard Refinement Sequence

When improving a publication figure, follow this systematic approach:

**1. Identify the Core Issue**
```
Examples:
- "Violin plots look distorted on log scale"
- "P-values are cut off at the top"
- "Too much visual clutter, hard to see the data"
- "Text overlaps with data points"
```

**2. Fix the Visualization Type/Method**
```python
# Example: Replace inappropriate plot type
# Before: Violin plot on log scale (distorted)
ax.violinplot(data)
ax.set_yscale('log')

# After: Boxplot on log scale (accurate)
ax.boxplot(data)
ax.set_yscale('log')
```

**3. Improve Visual Clarity**
Systematically adjust element sizes:

```python
# Point sizes: Reduce for dense data
# Start: s=60 (exploratory)
# End: s=25 (publication)
ax.scatter(..., s=25, alpha=0.5)

# Line widths: Thinner reduces clutter
# Start: linewidth=2.5
# End: linewidth=1.5
ax.plot(..., linewidth=1.5)

# Text sizes: Prevent overlap
# Start: fontsize=10-12
# End: fontsize=8-9
ax.text(..., fontsize=8)

# Error bar caps: Keep readable
ax.errorbar(..., capsize=5)
```

**4. Test Layout Alternatives**
```python
# Option A: Side-by-side panels
fig, axes = plt.subplots(1, 2, figsize=(16, 7))
# Pros: Direct left-right comparison
# Cons: Smaller individual panels

# Option B: Stacked vertically
fig, axes = plt.subplots(2, 1, figsize=(10, 14))
# Pros: Larger individual panels, easier to read details
# Cons: Harder to compare across panels

# Decision: Let user feedback guide choice
# Generate both, ask which is clearer
```

**5. Optimize Element Positioning**
Ensure all annotations fit within plot bounds:

```python
# Calculate safe positioning
y_max = max([d.max() for d in data_list])
y_min = min([d.min() for d in data_list])

# Position annotations WITHIN bounds
y_pos = y_max * 0.92  # 92%, not 105% (which goes outside)

# Set explicit limits with headroom
ax.set_ylim(y_min * 0.95 if y_min > 0 else y_min - 5,
            y_max * 1.05)
```

### Checklist for Publication Figures

Use this checklist before finalizing figures:

- [ ] **Plot type appropriate** for data distribution (no violin on log scale)
- [ ] **All text readable** at publication size (8-10 pt minimum)
- [ ] **Statistical annotations visible** and within plot bounds
- [ ] **Legend clear** and doesn't obscure data
- [ ] **Axis labels** descriptive with units
- [ ] **Color scheme** colorblind-friendly
- [ ] **Line weights balanced** (not too thick or thin)
- [ ] **Point sizes optimized** (visible but not overlapping)
- [ ] **DPI adequate** for publication (300 minimum)
- [ ] **Layout tested** (try both horizontal and vertical if applicable)
- [ ] **File format** publication-ready (PNG, PDF, or SVG)

## Common Refinement Patterns

### Pattern 1: Decluttering Dense Plots

**Problem**: Too many visual elements competing for attention

**Solution sequence**:
1. Reduce point size (60 -> 25)
2. Thin line widths (2.5 -> 1.5)
3. Increase transparency (alpha=0.8 -> 0.5)
4. Reduce font sizes (10 -> 8)
5. Remove grid or make it lighter (alpha=0.3)

**Before/After test**: Generate both versions, compare

### Pattern 2: Fixing Overflow Issues

**Problem**: Annotations, legends, or labels cut off

**Solutions**:
```python
# 1. Adjust annotation positions
y_pos = y_max * 0.92  # Within bounds

# 2. Use bbox_inches='tight' when saving
plt.savefig('figure.png', dpi=300, bbox_inches='tight')

# 3. Explicitly set limits
ax.set_ylim(min_val * 0.95, max_val * 1.05)

# 4. Move legend outside plot area
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# 5. Reduce text size
ax.text(..., fontsize=8)  # Down from 10
```

### Pattern 3: Multi-Panel Layout Optimization

**Try both orientations**:

```python
# Version 1: Horizontal (side-by-side)
fig, axes = plt.subplots(1, 2, figsize=(16, 7))
plt.savefig('fig_horizontal.png', dpi=300, bbox_inches='tight')

# Version 2: Vertical (stacked)
fig, axes = plt.subplots(2, 1, figsize=(10, 14))
plt.savefig('fig_vertical.png', dpi=300, bbox_inches='tight')

# Present both to user, ask which is clearer
```

**Decision criteria**:
- **Horizontal**: Better for direct comparison between panels
- **Vertical**: Better when each panel needs more space
- **User context**: Journal column width, presentation slides, etc.

### Pattern 4: Iterative Statistical Annotation

**Common issue**: P-values positioned outside plot or overlapping with data

**Solution**:
```python
# Calculate data range first
all_data = [data_dual, data_prialt]  # All datasets in plot
y_max = max([d.max() for d in all_data if len(d) > 0])

# Position relative to actual data, not theoretical maximum
for i, (x_pos, comparison) in enumerate(comparisons):
    stat, pval = stats.mannwhitneyu(...)

    # Safe positioning
    y_annotation = y_max * 0.92  # Below the top

    # Format text
    if pval < 0.001:
        text = 'p < 0.001***'
    elif pval < 0.01:
        text = 'p < 0.01**'
    elif pval < 0.05:
        text = 'p < 0.05*'
    else:
        text = f'p = {pval:.3f} ns'

    ax.text(x_pos, y_annotation, text, ha='center', fontsize=9)

# Set explicit limits to ensure annotations fit
ax.set_ylim(0, y_max * 1.05)
```

## Refinement Workflow Example

**Real case: VGP Figure 5 improvement sequence**

1. **Initial version**: 4 categories, violin plots on log scale
   - Issue: Violin distortion, too complex

2. **V1 refinement**: Remove violin plots, keep boxplots
   - Better, but still issues

3. **V2 refinement**: Simplify to 3 categories
   - Clearer interpretation

4. **V3 refinement**: Reduce point sizes (60->25), thin lines (2.5->1.5)
   - Less clutter

5. **V4 refinement**: Test vertical vs horizontal layout
   - Horizontal clearer for this case

6. **V5 refinement**: Fix p-value positioning (105%->92% of y_max)
   - All elements now visible

7. **Final**: Smaller text in statistics box (10->8)
   - Publication ready

**Total iterations**: 7 versions over refinement process
**Result**: Clear, accurate, publication-quality figure

## Verifying Numbers in Legends and Manuscript Text

Every number in a legend, Results paragraph or Methods section must be re-derived from the
data by a script that asserts it — not read off an earlier printout. Four errors caught this
way in one session, none visible on proofreading:

| Written | Actual | Cause |
|---|---|---|
| 9.3% | 9.4% | added two *pre-rounded* percentages instead of computing the combined proportion then rounding |
| P = 0.95 | P = 0.94 | 0.9447 rounded at the wrong step |
| "roughly 88 Mb" | 85.4 Mb | estimated rather than computed |
| n = 377 / 227 | 387 / 232 | correct when written; a later cohort change made them stale |

```python
checks = {
    "panel b 586 total": len(a) == 586,
    "hap1 +1.7 vs +3.2": (round(med(AD, 'hap1'), 1), round(med(AS, 'hap1'), 1)) == (1.7, 3.2),
}
for k, v in checks.items():
    print(("PASS " if v else "FAIL ") + k)
```

**Never add pre-rounded components.** `3.1 + 6.2 = 9.3`, but the combined proportion is 9.4.
Compute the combined value from raw counts, then round once.

**Stale-by-later-edit is the commonest failure.** Numbers written correctly go stale when a
cohort rule changes downstream. Anything hand-written (Methods prose, a change table) needs
its own verification pass after *every* cohort change — unlike figure counts, it is not
auto-asserted.

**Prefer counts to percentages when denominators are small.** "9.4% in 2022" implies
precision; "3 of 32" shows the reader what it rests on.

## A Review Document's Anchors Must Be Machine-Verified

A page-by-page review of a manuscript — "find this text, add this comment" — is only
useful if every anchor actually matches and every page number is right. One wrong anchor
and the reader is hunting; one wrong page number and they are on the wrong page.

Extract the anchors from your own document and check them against the source:

    pdftotext -layout manuscript.pdf full.txt
    for i in $(seq 1 31); do
        pdftotext -layout -f $i -l $i manuscript.pdf pages/p$(printf %02d $i).txt
    done

    full = re.sub(r"\s+", " ", open("full.txt").read())
    anchors = re.findall(r"\*\*Find:\*\*\s*`([^`]+)`", doc)
    bad = [a for a in anchors if re.sub(r"\s+", " ", a).strip() not in full]

Then check each claimed page number against that page's own text, not the whole document.
On the first pass of a 50-anchor document this found **five wrong page numbers**, plus a
heading with no page marker that silently inherited the previous section's — the kind of
error that is invisible on proofreading and obvious to a script.

**Normalise whitespace on both sides.** PDF extraction breaks lines mid-sentence, so an
anchor spanning a line break will not match the raw text even though it is correct.

**Check numbering is monotonic too.** Inserting an item before its neighbour is easy and
leaves the document reading 1.1, 1.2, 1.3, 1.5, 1.4.

**Cross-link items that interact.** Two corrections in that review touched the same number
from different directions — one asked to change 174 to 175, a later one took it back to 174
for an unrelated reason. Applied independently, the second silently undoes the first; each
now warns about the other.

**Against a live document, a whole-sentence find string is a free anchor test.** Putting the
entire old sentence in the Find field and getting `0 of 0` is not a failure — it is the check
firing. Replace cannot run, nothing is touched, and you have learned the live text differs
from your source before you proposed the edit.

Expect this to fire often. A review built from a two-week-old PDF export was carried into the
live document: **twelve of about twenty-five items had already been applied**, several find
strings no longer existed, and one placeholder had been resolved to the *wrong* target. Re-
deriving the list against the live text took one read-through and changed roughly half the
table. Mark the already-done items explicitly in the re-derived list, or the next person
works through the stale one again.

## Reproducing a Collaborator's Statistics: Find Their Cohort File, Not Their Filter

When you rebuild someone else's analysis, the first thing to establish is **which rows they
actually ran it on** — and that is frequently not what their script appears to compute.

A shared script filtered a species table to one sequencing technology, giving 396 species.
The published figure said *n* = 420. The difference was not a bug: an intermediate,
analysis-ready CSV with exactly 420 rows sat in the same data folder, and that was the real
input. Every per-lineage statistic reproduced exactly from the file and none of them from
the filter.

**Before trusting a rebuild, make it reproduce their published numbers.** Build the check in
as a configuration of the script, not as a one-off:

- Search the data folder for a file whose row count equals the published *n*.
- If the stated method and the shipped data disagree, the data wins — then say so in the
  Methods, because the next person will hit the same wall.
- Statistics code is often *not* shared even when plotting code is. Expect to rebuild it from
  the Methods prose, and expect that prose to be an approximation of what ran.

## When the Discussion Overclaims Relative to the Results

A recurring and highly visible failure: careful Results, confident Discussion. One
manuscript's Results said "we find **no evidence** that [treatment] alters [outcome]" while
the Discussion opened "[treatment] demonstrates **clear advantages** ... **at scale**". A
referee comparing the two finds it in the first reading, and it undermines the sections that
*are* well supported.

**Diagnose it mechanically.** Grep the Results for hedges — "no evidence", "did not differ",
"not significant", "do not resolve" — and check whether the Discussion's opening sentences
contradict them. The gap is usually in the first paragraph, because the first paragraph is
written to sell.

**Fix it by explaining the null, not by weakening the claim.** The honest reconciliation is
almost always the more interesting statement:

> The benefit is concentrated in a small fraction of the genome — misphasing, structural
> heterozygosity, the pseudoautosomal region. Genome-wide summary statistics average over
> the whole assembly and are, by construction, insensitive to them. A genome-wide null is
> what one should expect if the benefit is real but local; it is not evidence of absence.

That converts the weakest point into a claim about *where to look*, and it names the measure
that does detect the effect.

**Lead the Discussion with what the method changes, not what it achieves.** A statement about
mechanism is unarguable; a statement about outcome is exactly what the data qualify. Move the
outcome claims to the paragraph that cites the evidence for them.

**Title, Abstract and Discussion stand or fall together.** They typically make the same claim
in three places. Fixing one and leaving the others is a half-measure a referee will notice —
check all three in the same pass.

**Check every Abstract number against the Results.** One Abstract's worked example — a named
species with two specific recovery figures — appeared nowhere else in the manuscript: the
species occurred only in the Abstract, one Discussion sentence and two references. A
different species, with a different result, was the one actually written up. The check is one
grep per claim: take each quantity in the Abstract and find it in the Results. Anything that
does not appear is either missing analysis or a leftover from an earlier draft, and both need
the same action — remove it or write it up.

**Offer a version at the journal's word limit, not just a better version.** An Abstract at
257 words against a 150-word limit will be cut by someone, and it is better that the cut is
yours. Where content genuinely does not fit, produce the tight version and a slightly longer
one, and say explicitly what the extra words buy.



## Do not build a composite by splitting one image at its midpoint

Rendering two panels into one figure and cropping it in half is fragile, and it fails in a
specific, recurring way: **as soon as a panel has ink outside its axes, that ink crosses the
split**. Horizontal bar charts with long category names are the common case -- the tick labels
sit well to the left of the axes and get sliced off, or land in the neighbouring panel.

Export each panel to its own file and have the composer read them:

```python
figb.savefig(OUT_B, dpi=300, bbox_inches="tight")
figc.savefig(OUT_C, dpi=300, bbox_inches="tight")
```

**Draw each panel in its own figure, too, not as two subplots saved twice.** Sharing one figure
means matplotlib decides how much width each panel's label gutter takes from the other, which
creates a feedback loop: raising panel c's type widens its export, the composite scales both to
equal width, and panel c's type comes out *smaller* than before. Separate figures fix each
panel's aspect directly, so one type scale serves both.

If a combined image is wanted for review, paste the two exports together with PIL afterwards
and label it clearly as a review sheet, so nothing downstream reads it by mistake.

## Best Practices

### 1. Version Your Refinements

Keep working versions during major changes:
```bash
scripts/
  plot_figure.py          # Original
  plot_figure_v2.py       # After major change (layout)
  plot_figure_final.py    # Publication version
```

### 2. Generate Alternatives in Parallel

When testing layout options:
```python
# Save both versions
layouts = [
    ((1, 2), (16, 7), 'horizontal'),
    ((2, 1), (10, 14), 'vertical')
]

for (nrows, ncols), figsize, name in layouts:
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    # ... plot data ...
    plt.savefig(f'figure_{name}.png', dpi=300, bbox_inches='tight')
```

### 3. Document Each Refinement

```python
"""
Figure 5 - Terminal Telomere Presence

Version history:
- v1: Initial 4-category version with violin plots
- v2: Removed violin plots (distortion on log scale)
- v3: Simplified to 3 categories (terminal only)
- v4: Reduced point/line sizes for clarity
- v5: Fixed p-value positioning
- final: Publication ready

Changes from v4 -> v5:
- P-value y-position: 1.05 * y_max -> 0.92 * y_max
- Added explicit y-axis limits: (y_min*0.95, y_max*1.05)
- Ensures all annotations visible within plot bounds
"""
```

### 4. Get Feedback at Key Milestones

Don't over-iterate without input:
- After fixing major issues (wrong plot type): **Show user**
- After layout changes (horizontal vs vertical): **Show user**
- After final polish: **Show user**

### 5. Maintain Consistency Across Figure Set

If refining one figure, check if same improvements apply to others:
```python
# Applied violin->boxplot fix to Figures 2, 7, 10, 11
# Applied size reductions consistently across all figures
# Used same color scheme throughout
```

## Summary

**Systematic refinement workflow**:
1. Identify issue -> 2. Fix visualization -> 3. Improve clarity -> 4. Test layouts -> 5. Optimize positioning

**Key principles**:
- Iterate based on user feedback
- Test alternatives (show options)
- Document changes
- Apply lessons across figure set
- Meet publication standards

**Common adjustments**:
- Point sizes: 60 -> 25
- Line widths: 2.5 -> 1.5
- Font sizes: 10 -> 8
- Annotation positions: 105% -> 92% of max
- Always set explicit axis limits

**For additional guidance**, see the supporting files:
- Publication standards (DPI, formats, sizes): [publication-standards.md](publication-standards.md)
- Multi-study result writing: [multi-study-results.md](multi-study-results.md)
- Methodological transparency: [methodological-transparency.md](methodological-transparency.md)
- Overleaf package creation: [overleaf-packages.md](overleaf-packages.md)

## A tick label must carry one kind of fact

Two labels that look parallel assert that the quantities behind them are parallel. If they
are not, the figure makes a claim the data does not support, and it does so in the one place
a reader will not think to question.

Real case: a panel's two second-haplotype groups were labelled `n = 184/184` and `n = 9/73`,
read as "curated of deposited". The second was a genuine finding - under that curation method
the second haplotype is usually not curated. The first was an artefact of **measurement
coverage**: all 204 second haplotypes had been curated, but statistics were published for only
184. Same visual form, two different kinds of fact, and side by side they implied an
equivalence that did not exist.

**Rule: a tick label carries the number plotted.** Anything else - a denominator, a
provenance, a caveat - goes in the legend where it can be named for what it is. The
replacement read `n = 184` and `n = 9`, with the legend giving "all 204 diploid-curated
assemblies curated their second haplotype... of the 87 haploid-curated, 84 deposited one and
9 of those 84 were curated".

**How to catch it:** for every compound label, ask what each number is a count *of*. If the
denominators come from different sources - one from the metadata, one from what happened to be
measured - they do not belong in the same notation.

The same rule covers on-figure subtitles. A line explaining an abbreviation is a sign the
abbreviation is wrong; and a subtitle lifts that panel's title above its neighbour's in the
same row, which reads as a crooked grid. Prefer labels that need no gloss.
