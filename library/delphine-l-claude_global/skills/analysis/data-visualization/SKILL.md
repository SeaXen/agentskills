---
name: data-visualization
description: Best practices for creating clear, accurate scientific visualizations with matplotlib, seaborn, and other Python plotting libraries. Covers common pitfalls, optimization techniques, publication-quality figure generation, and Claude API image size constraints.
version: 1.2.0
context: fork
allowed-tools: Read, Grep, Glob, Bash
---

# Data Visualization Best Practices

Expert guidance for creating publication-quality scientific visualizations, avoiding common pitfalls, and optimizing figure clarity.

## When to Use This Skill

- Creating figures for scientific publications
- Debugging misleading or distorted visualizations
- Optimizing figure layouts and element sizes
- Choosing appropriate plot types for data characteristics
- Ensuring statistical annotations fit properly
- Generating images for sharing with Claude or other AI tools

## Supporting Files

This skill is organized into focused reference files. Load them as needed:

- **[pitfalls-and-troubleshooting.md](pitfalls-and-troubleshooting.md)** - Log-scale distortion, coordinate transform bugs, outlier handling philosophy, axis range optimization, float year labels
- **[chart-recipes.md](chart-recipes.md)** - Code recipes for temporal trends, boxplots, scatter plots, category proportions, stacked area charts, sample size legends, the dual-approach for outlier handling in publication figures
- **[color-palettes.md](color-palettes.md)** - Okabe-Ito palette, Paul Tol palette, sequential/diverging schemes, colorblind-safe implementation in matplotlib/seaborn
- **[claude-image-constraints.md](claude-image-constraints.md)** - Claude API 8000px limit, safe figure size presets, resize helpers, Jupyter notebook oversized image fixes
- **[figure-descriptions.md](figure-descriptions.md)** - Templates for writing publication-quality figure descriptions with proper statistical reporting
- **[itol-reference.md](itol-reference.md)** - iTOL dataset formats (DATASET_STYLE, DATASET_BINARY, DATASET_COLORSTRIP), species name synchronization, troubleshooting
- **[journal-requirements.md](journal-requirements.md)** - Journal-specific figure specs (Nature, Science, Cell, PLOS, ACS, IEEE, Elsevier, BMC): dimensions, DPI, formats, panel labeling, file naming

## Assets (importable in notebooks/scripts)

- **`assets/publication.mplstyle`** - General publication style: `plt.style.use('path/to/publication.mplstyle')`
- **`assets/nature.mplstyle`** - Nature journal style (89mm single column, 7pt fonts, 600 DPI)
- **`assets/presentation.mplstyle`** - Larger fonts/lines for posters and slides
- **`assets/color_palettes.py`** - Importable palette definitions (Okabe-Ito, Wong, Paul Tol), `apply_palette()` helper, DNA base colors

## Scripts (helper utilities)

- **`scripts/figure_export.py`** - `save_publication_figure()`, `save_for_journal()`, `check_figure_size()` - export in multiple formats with journal-specific DPI/format settings
- **`scripts/style_presets.py`** - `apply_publication_style()`, `configure_for_journal()`, `set_color_palette()` - one-command journal configuration

## Core Principles

### 1. Always Check Log-Scale Plots

KDE-based plots (violin, ridge) on log axes produce distorted shapes. Use boxplots or log-transform data first, then plot on linear axes. See [pitfalls-and-troubleshooting.md](pitfalls-and-troubleshooting.md) for details.

### 2. Show All Data First, Filter Later

Default to showing ALL data points in initial visualizations (`showfliers=True`). Outliers may be biologically meaningful. Only filter after review with domain expert, and always document exclusions.

### 3. Use Colorblind-Safe Palettes

Use Okabe-Ito palette (recommended by Nature) for categorical data. Combine color with marker shapes for redundancy. Never use red-green combinations. See [color-palettes.md](color-palettes.md) for hex codes and implementation.

### 4. Respect Claude's Image Size Limit

Images shared with Claude must not exceed **8000 pixels** in either dimension. Use safe figure size presets and the `save_figure()` helper. See [claude-image-constraints.md](claude-image-constraints.md).

### 5. Check for Saturated Metrics Before Boxplotting

If most values of a bounded metric are identical, IQR = 0 and every box renders as a flat line — the panel looks like missing data when coverage is complete. Guard with `modal_frac > 0.5 or iqr == 0`, then plot the per-group proportion as bars instead. See [pitfalls-and-troubleshooting.md](pitfalls-and-troubleshooting.md).

### 6. Position Annotations Carefully

Use pure data coordinates or `ax.transAxes` (0-1 range) for text positioning. Never mix coordinate systems (e.g., `ax.get_xaxis_transform()` with data-scale y-values). See [pitfalls-and-troubleshooting.md](pitfalls-and-troubleshooting.md).

## Chart Selection Quick Guide

| Data Type | Recommended Chart | When to Use |
|-----------|------------------|-------------|
| Distribution comparison | Boxplot | Large datasets, log scales, multiple groups |
| Distribution shape | Histogram | Always works on log scales, shows true frequency |
| Temporal trends (few points) | Scatter + regression | < 50 points per timepoint, continuous time |
| Temporal trends (many points) | Boxplots by year | Overlapping points, discrete timepoints |
| Category proportions over time | Stacked area + stacked bar (dual panel) | Showing both relative and absolute trends |
| Categorical comparison | Bar chart, violin (linear scale only) | Group means or distributions |
| Phylogenetic annotation | iTOL datasets | Tree visualization with metadata |

## Publication Figure Checklist

### Before Creating

- [ ] Choose colorblind-safe palette (Okabe-Ito recommended)
- [ ] Plan figure dimensions within Claude's 8000px limit
- [ ] Decide on panel layout (side-by-side vs stacked)

### During Creation

- [ ] Include sample sizes in legends: `Category (n=123)`
- [ ] Use integer year labels: `ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))`
- [ ] Set explicit axis limits when adding annotations
- [ ] Reduce element sizes for dense data (s=25, alpha=0.5)
- [ ] Use `bbox_inches='tight'` for **drafts only** — never for final assets with an exact width requirement (see "Hitting an Exact Journal Width")

### After Creation

- [ ] Verify image dimensions (max 7999x7999 for Claude)
- [ ] Check annotations are within plot bounds
- [ ] Test colorblind accessibility
- [ ] Save at 300 DPI minimum for publication

### For Temporal Analyses

- [ ] Create both all-data and cleaned versions
- [ ] Calculate statistics on FULL dataset (not cleaned)
- [ ] Document outlier removal method and retention rate
- [ ] Use clear file naming: `figure.png` vs `figure_clean.png`

## Quick Reference: Safe Figure Sizes (300 DPI)

```python
FIG_SIZES = {
    'single_column': (3.5, 4),      # 1050x1200 px
    'double_column': (7, 5),        # 2100x1500 px
    'full_page': (7, 9),            # 2100x2700 px
    'poster': (20, 15),             # 6000x4500 px
    'max_claude': (26, 26),         # 7800x7800 px
}
```


### Hitting an Exact Journal Width

Two traps when the target is a precise width (e.g. Nature Methods 180 mm at 300 DPI):

**1. matplotlib truncates `figsize * dpi`.**
`180/25.4 = 7.086614 in`, `x 300 = 2125.98 px` -> renders **2125 px**, one short.
Derive the figure size from the target *pixel count* instead:

```python
TARGET_W_PX = 2126                      # 180 mm at 300 dpi
fig, axes = plt.subplots(2, 2, figsize=(TARGET_W_PX / 300, h_in))
```

**2. `bbox_inches='tight'` breaks exact sizing — do not use it for final assets.**
It recomputes the bounding box from the drawn artists, so the saved width changes whenever
a label changes length. Worse, it silently *expands* the canvas to fit artists drawn
outside the axes, which hides real layout bugs: panel letters at negative axes coordinates
and over-wide footnotes were both being absorbed, and only surfaced as clipping once the
tight bbox was removed.

```python
# deterministic: explicit margins, no bbox_inches
fig.subplots_adjust(left=0.115, right=0.978, top=0.95, bottom=0.125,
                    wspace=0.30, hspace=0.72)
fig.savefig(out, dpi=300, facecolor="white")
```

`tight_layout()` does not account for text placed in axes coordinates below the axis
(footnotes) either — reserve that space in `bottom`/`hspace` manually.

**Verify, don't eyeball** — scan for ink at the canvas border:

```python
a = np.array(Image.open(path).convert("RGB"))
nw = (a < 250).any(axis=2)
rows, cols = np.where(nw.any(axis=1))[0], np.where(nw.any(axis=0))[0]
assert cols.min() > 0 and cols.max() < a.shape[1] - 1   # nothing clipped L/R
assert rows.min() > 0 and rows.max() < a.shape[0] - 1   # nothing clipped T/B
```

### Axes-coordinate annotations break when panel geometry changes

Text placed at negative axes coordinates — panel letters, footnotes — scales with the
*panel*, not the figure. Changing the layout silently moves it off-canvas:

- A `-0.215` letter offset works for a half-width panel but lands outside the figure on a
  full-width one. Use a per-axis offset.
- A legend at `bbox_to_anchor=(1.01, 0.5)` is fine while the panel sits in the left column;
  move that panel to the right column and the legend leaves the canvas.
- Adding a group to a panel makes tick labels taller, so a footnote offset that cleared them
  before now overlaps.

**Re-verify after every layout change** with the border-ink scan above, and look at the
render. Three label formats were tried before one fit five groups in a half-width panel;
only the rendered image showed which.

## Quick Reference: Okabe-Ito Colors (3 Categories)

```python
colors = {
    'Category_A': '#0072B2',    # Blue
    'Category_B': '#E69F00',    # Orange
    'Category_C': '#CC79A7'     # Reddish Purple
}
```

## Verify a hand-made asset by its content, not its filename

Some figure panels cannot be scripted — a tree exported from iTOL, a cartoon drawn in
Illustrator, a screenshot. They arrive as files, and a filename is not evidence that the
file is the version you think it is.

**Check something measurable that the regeneration should have changed.** For a
categorical colour annotation, count palette pixels and compare the shares against the
counts the data says it should show:

```python
from PIL import Image
import numpy as np
a = np.array(Image.open(f).convert("RGB")).reshape(-1, 3).astype(int)
for name, (r, g, b) in PALETTE.items():
    hits = ((np.abs(a[:,0]-r) < 6) & (np.abs(a[:,1]-g) < 6) & (np.abs(a[:,2]-b) < 6)).sum()
    print(f"{name:16s} {100*hits/total:5.1f}%")
```

Used 2026-10-05 to confirm a new tree export carried a category merge before building on
it: one colour went 46.0% -> 50.5% and another 11.2% -> 6.8%, against the expected
426/835 and 54/835. The tolerance absorbs anti-aliasing; the shares will not match
exactly, because legend swatches and other elements use the same colours — the
**direction and magnitude** of the shift is the signal.

Other cheap content checks: image dimensions (a re-export usually changes them), the
rendered key or legend text if it bakes in counts, and file mtime against the data it
should have come from.

### Composite figures: localise a difference before explaining it

When a composite built from scripted and hand-made panels does not match a reference,
find out *which rows* differ before concluding anything:

```python
diff = (np.abs(a[:h] - b[:h]).sum(axis=2) > 0)
rows = np.where(diff.any(axis=1))[0]
print(rows.min(), rows.max())
```

In that project the composite differed by one pixel of height between two repositories.
Localising showed **zero** differing pixels in the hand-made panel — both composited the
same export — and all divergence in the scripted panels, whose `bbox_inches="tight"`
crop depends on font metrics. "Not byte-identical" on its own would have invited the
wrong conclusion.

## A legend is an output of the figure, not a note beside it

A hand-maintained legend drifts from its figure silently. The image is regenerated, the prose
is not, and the stale numbers survive into the manuscript — where they contradict the panel
they describe.

**Cheapest possible check, before trusting any legend:**

```bash
ls -la figures/composite/Figure1_phylo_overview.png figures/composite/Figure1_legend.txt
# legend OLDER than the figure -> assume stale until proven otherwise
```

Real case (2026-10-06). A tree figure was re-exported after a category change; its legend was
not touched. **Ten values were wrong** — three category counts, two panel *n*s, a CLR
denominator, and four percentages — plus one claim the change had made outright false
("fell to three or four per year" when the new data said 3, 6, 4, 10, 6). The sibling figure's
legend was fine, because it was regenerated in the same pass as its own figure.

What to do, in order of preference:

1. **Emit the legend from the plotting script**, with the numbers interpolated from the same
   variables the panels use. It cannot drift.
2. **Assert the legend's values** from the source-data builder — read the counts out of the
   legend text and fail the build on a mismatch. (Pattern: a builder that refuses to write
   when its `EXPECTED` dict disagrees with the rendered legends.)
3. **At minimum, compare mtimes** and re-read the legend whenever the figure is rebuilt.

**Check prose claims, not only numbers.** A legend sentence like "fell to three or four per
year" or "the remaining five are murid rodents" is as falsifiable as an *n*, and nothing in a
numeric assertion will catch it. In the same session a legend asserted a taxonomic **family**
for five species when the dataset carried only **order** — the claim had been copied from an
annotator's free-text comment and was wrong for three of the five, including one species in a
different suborder entirely. **If a legend states something at a finer resolution than the
data carries, that claim came from somewhere else — find out where.**

---

## Before writing a generator, find the one that made the figure

A published figure's style lives in the script that produced it, not in its legend. If you
rebuild the panel from the legend you will get the numbers right and the style wrong, and the
difference is immediately visible to whoever has been looking at that figure for months.

One command usually finds it:

```bash
grep -rl "<an exact title string from the figure>" . --exclude-dir=.git
```

Titles, axis labels and legend entries are all good search keys because they are literal strings
in the plotting code.

In the case this is drawn from, a replacement generator was written from scratch for two panels.
The existing script already had the correct palette, the correct hatching, the value labels, the
framed legends and the established titles — **its only defect was that it read a retired input
file.** The fix was two lines. The rewrite was a hundred, and it looked wrong.

**How to apply**

- Search before writing. Check `scripts/`, any `*_share/` or `figure_*/` folders, and archived
  directories, because the live generator is not always the newest file.
- When you find it, ask what is actually broken. A stale *input path* is not a reason to replace
  a script.
- If several scripts write the same output path, the one that runs last wins. `grep -rl
  "<output filename>"` tells you how many producers a figure has.
- Delete your own replacement once the original is fixed. Two generators for one figure is the
  condition that caused the problem in the first place.


## A validator must count the cohort the panel draws, not the whole table

Assertion blocks that check "the figure reproduces the numbers in its legend" are worth having,
and they go quietly wrong when they count the wrong rows.

A validator computed per-lineage and per-category totals across the **entire** source table
while the panel drew only the rows flagged as being on the tree. Those were the same number for
months, so the bug was invisible. The day a filter was added — restricting the panel to species
carrying an assembly accession — the two diverged by 18 species and seven assertions failed at
once, which at least surfaced it. Had the filter been subtler it would have passed and the
legend would have been wrong.

```python
# wrong: counts everything the table holds
for c, n in t.clade.value_counts().items(): ...

# right: counts what the panel draws
panel = t[t.in_fig1a_tree]
for c, n in panel.clade.value_counts().items(): ...
```

**How to apply**

- Derive every asserted count from the same filtered frame the plotting code uses. If the panel
  uses `df[df.flag]`, so must the check.
- Write the filter once into a variable and use it for both. Two expressions that *mean* the
  same cohort will eventually stop being the same cohort.
- When adding a filter to a panel, grep the validator for the columns it touches before
  assuming the assertions still mean what they say.


## Place panel letters in points, not axes fraction

`ax.text(x, 1.10, "a", transform=ax.transAxes)` puts the letter at a fixed **fraction** of the
panel's height above it. In a grid with uneven row heights — `height_ratios=[1.35, 1, 1]`, or any
layout where one row is taller — the same fraction is a different physical distance in each row,
so the letters land at different heights and none of them lines up with its title.

Use an offset in points instead, which is constant regardless of panel size:

```python
ax.annotate(letter, xy=(xoff, 1.0), xycoords="axes fraction",
            xytext=(0, 9), textcoords="offset points",
            va="bottom", ha="left", fontsize=11, fontweight="bold",
            annotation_clip=False)
```

9 pt with `va="bottom"` puts an 11 pt bold letter's cap height level with a 9 pt title set at
`pad=8`. Adjust together if either font size changes.

The same reasoning applies to anything else positioned relative to a panel edge in a mixed-height
grid: footnotes, significance brackets, and text placed below tick labels. Axes fractions are
right for things that should scale with the panel, points for things that should not.



## Three matplotlib traps that silently ruin a panel

**`twinx` paints over its partner wholesale.** A zorder set on the first axes cannot lift an
artist above anything drawn on the twin -- axes are composited in creation order, and zorder
only orders artists *within* one axes. Text placed on the first axes will be crossed by lines
on the twin no matter what zorder or `bbox` it carries. Draw the text on the **twin** and
position it in the partner's units:

```python
axb2.text(x, y, label, transform=axb.transData, zorder=10, clip_on=False,
          bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"))
```

**Hatch is drawn in the edge colour.** `hatch="//"` with the default black edge is invisible on
a dark fill. Give hatched artists a white edge (`edgecolor="white"`) and keep black edges on the
unhatched ones -- the outline change is a small price for the texture being visible at all.

**A KDE evaluated over the full data range gets clipped into a vertical bar at the frame.** If
the axis is limited to the whiskers (as it should be when outliers would flatten the boxes),
evaluate the density over the **visible band**, not over `v.min()` to `v.max()`:

```python
ys = np.linspace(bot, top, 200)          # the plotted range, not the data range
xs = kde(ys); xs = xs / xs.max() * 0.34
```
The density is still computed from all the data -- only the drawn interval changes.

## Desaturating for print: bake the tint, do not pass `alpha`

To make fills less saturated for print, composite the colour over white and emit **opaque
hex**. A real `alpha=` also washes out the black outlines and any hatching, and composites
unpredictably in PDF where shapes overlap.

```python
def tint(hex_colour, a=0.80):
    rgb = [int(hex_colour[i:i+2], 16) for i in (1, 3, 5)]
    return "#%02X%02X%02X" % tuple(round(v * a + 255 * (1 - a)) for v in rgb)
```

**Choose the tint level by measurement, not by eye.** Lightening costs colour-vision
separation, and the cost is not linear. Compute worst-pair CIE Lab dE across normal vision,
deuteranopia, protanopia and tritanopia at several levels and stop at the end of the flat part
of the curve. On one real palette, 0.80 cost the technology ramp 20.0 -> 16.1 while *improving*
the method palette 15.4 -> 16.2 (lightening a dark red and an olive increased their deutan
separation); below 0.75 the two mid blues fell to 12.8.

Record the measured numbers next to the constant. The next person will otherwise nudge it.

## Best Practices Summary

**Declare a logarithmic axis in the legend.** A linear axis is the reader's default
assumption, so a log axis that goes unstated is a reporting defect — and it is easy to miss,
because the axis label usually carries the unit, not the scale. Two figures in one manuscript
were logarithmic and neither legend said so.

**Choosing the scale: ask where the story is.**

| Situation | Scale |
|---|---|
| Range spans > 2 decades **and** the finding is in the bottom decade | log — linear collapses it onto the baseline |
| Range spans ~1 decade | linear — log buys nothing and distorts arrow/bracket geometry |
| One series spikes far above the others **and the spike is the point** | linear — log flattens exactly what you are showing |

A measure plotted on different scales in two figures of the same paper is acceptable when
each is justified, but **each legend must then state its own scale and point at the other**,
or a reader comparing them will misread one.

**Derive axis limits from the same rule the marks use.** A boxplot drawn with
`showfliers=False` whiskers to 1.5 x IQR; setting the axis to the data max then leaves a
large empty band above the whiskers. Compute the top from the same rule:

```python
q1, q3 = np.percentile(v, [25, 75])
top = min(v.max(), q3 + 1.5 * (q3 - q1))
ax.set_ylim(0, top * 1.5)      # headroom for brackets/labels
```

Then position significance brackets and in-panel labels **from that computed top**, not from
constants — constants tuned for a log axis are meaningless on a linear one.

**Offer a scale change as a variant, never as an overwrite.** Add a flag that writes to a
separate filename, show both, and flip the default only once the choice is made. The old
figure stays reproducible either way.


**Never hard-code a below-axis offset in axes fractions.** A footnote placed at `y = -0.44`
cleared its tick labels perfectly in a 3x2 figure and landed on top of them the moment a
fourth row made the panels shorter. The same constant then needed retuning for every
subsequent layout edit. Measure the drawn artists instead:

```python
def below_axes(ax, gap_pt=7):
    """Axes-fraction y just under the x tick labels, for text with va='top'."""
    fig = ax.figure
    fig.canvas.draw()
    boxes = [t.get_window_extent() for t in ax.get_xticklabels() if t.get_text()]
    if not boxes:
        return -0.15
    ax_bb = ax.get_window_extent()
    return (min(b.y0 for b in boxes) - gap_pt * fig.dpi / 72) / ax_bb.height
```

This accounts for tick length, tick padding and the renderer's own line spacing, none of
which a font-size estimate captures. It requires a draw, so **place everything that sits
below an axis last**, after `subplots_adjust` and after every panel has its final labels.

Panel letters have the same problem in reverse: offset them in **points**
(`ax.annotate(..., xytext=(-80, 8), textcoords="offset points")`), not axes fractions, or
panels of different heights will carry their letters at different distances.

Related: when rows differ in what hangs below them, uniform `hspace` cannot serve both. Size
it for the row with the footnote, then give the surplus to the row without one via
`height_ratios` rather than leaving an obviously empty band.


1. **Always check log-scale plots** - Verify KDE-based plots against histograms
2. **Test element sizes** - Regenerate with different sizes for optimal clarity
3. **Explicit axis limits** - Don't rely on auto-limits when annotations are added
4. **Consistent styling** - Use seaborn context and style for publication consistency
5. **High DPI** - Save at 300 DPI minimum. Use `bbox_inches='tight'` for drafts; for final assets set explicit margins instead so the output size is deterministic
6. **Optimize axis ranges** - Zoom to data range when distributions are compressed
7. **Check image dimensions** - Verify size before sharing with Claude (max 7999x7999)
8. **Set size constraints** - Use safe figure sizes when generating images programmatically
9. **Temporal trends with outliers** - Create both cleaned (publication) and full (verification) versions
10. **Include sample sizes** - Always show n= in legends for comparative figures

## References

- Matplotlib documentation: https://matplotlib.org/
- Seaborn visualization: https://seaborn.pydata.org/
- iTOL documentation: https://itol.embl.de/help.cgi
- Okabe-Ito palette: https://jfly.uni-koeln.de/color/
- ColorBrewer: https://colorbrewer2.org

## Verify a density estimate against the points it sits beside

A violin or half-violin is an *estimate*, and `scipy.stats.gaussian_kde` with its default
bandwidth can be badly wrong without looking wrong. Before trusting one, compare its CDF to
the empirical CDF of the points drawn next to it:

```python
ys = np.linspace(lo, hi, 2000)
cdf = np.cumsum(kde(ys)); cdf /= cdf[-1]
vis = np.sort(v[(v >= lo) & (v <= hi)])
ecdf = np.searchsorted(vis, ys, side="right") / len(vis)
print("KS:", np.abs(cdf - ecdf).max())          # < 0.08 fine, > 0.15 suspect
```

**Why it goes wrong.** Scott's and Silverman's rules set the bandwidth from the *standard
deviation*. Any measure with a tight core and fat tails has SD far larger than its
interquartile range, so the kernel ends up wider than the middle half of the data. The
symptom is diagnostic and easy to miss: **every group looks like the same smooth teardrop**,
and the curve carries visible mass where the point cloud is nearly empty.

Real case (VGP curation paper, 2026-11-05, caught by the user, not by me): percentage change
in scaffold N50, values packed near zero with outliers from -57% to +133%. SD 18-26 against an
IQR of 6-13, so Scott's bandwidth was **7.5-9.8 units - wider than the IQR of every group**.
KS was 0.20-0.29; one bin held 17% of the data and 0% of the curve. In a second panel of the
same figure, whose data were genuinely broad, bandwidth was 0.19-0.25 x IQR and KS 0.03-0.08.
Same code, same call, one panel right and one wrong.

**The fix** - trim to the band you draw, and use a robust scale:

```python
def half_violin_density(v, lo, hi, n_grid=200):
    v = pd.Series(v).dropna()
    v = v[(v >= lo) & (v <= hi)]          # describe the points you actually plot
    if len(v) < 3 or v.nunique() < 2:
        return None, None
    sd = v.std(ddof=1)
    iqr = np.subtract(*np.percentile(v, [75, 25]))
    sigma = min(sd, iqr / 1.349) if iqr > 0 else sd
    kde = stats.gaussian_kde(v, bw_method=len(v) ** (-1 / 5) * sigma / sd)
    ys = np.linspace(lo, hi, n_grid)
    dens = kde(ys)
    return ys, dens / dens.max()
```

`bw_method` is a multiplier on the data's own SD, so `n**(-1/5) * sigma/sd` is Scott's rule
recomputed on the robust scale. This is a **no-op on well-behaved data** - it only bites when
SD exceeds IQR/1.349 - so it is safe to apply everywhere rather than per panel.

**What no bandwidth can fix: a point mass.** If 17% of values are *exactly* zero, a Gaussian
kernel spreads them symmetrically and the curve will always claim mass just below zero that
does not exist. Say so in the legend ("the spike is real, the shoulder under it is the
kernel"), or use a horizontal histogram with a bin centred on the spike, which represents it
exactly at the cost of a noisier outline.

## A small group should neither get a density nor set the axis limits

Two separate rules, both triggered by the same group:

- **No KDE below ~20 points.** A Gaussian KDE on nine values describes the bandwidth, not the
  data, and renders as a slab wide enough to dominate the panel. Draw the points and the box;
  that is all nine values support.
- **Let it show its box, not its whisker.** Taking the axis limit from `q3 + 1.5*IQR` of a
  nine-point group with a huge spread pushed a percentage axis past 100 and pressed every
  other box flat. Take the limit from `q3` for small groups and from the whisker for the
  rest: nothing is hidden, only the whisker is cropped, and the group's *n* on its tick says
  why it is wide.

```python
for v in groups:
    q1, q3 = np.percentile(v, [25, 75]); iqr = q3 - q1
    if len(v) >= MIN_N_SETS_LIMIT:
        hi.append(min(v.max(), q3 + 1.5 * iqr))
    else:
        hi.append(q3)
```
