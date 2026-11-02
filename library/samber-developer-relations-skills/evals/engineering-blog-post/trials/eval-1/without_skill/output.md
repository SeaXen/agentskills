I only have your summary, not the draft, so I couldn't edit the text directly. Below are replacement passages for each problem. I left bracketed slots wherever the fix needs a fact only your team has, and I didn't invent any numbers or API names. Fill the slots, paste the passages in, and the post is ready for Thursday.

## Before Thursday: facts to get from the author

1. Baseline: which tool and version, and what you compared against.
2. Workload: dataset size, row count, column types and cardinality.
3. Hardware: CPU, cores, RAM, disk, and cloud instance type if applicable.
4. Kestrel version and config used for the benchmark.
5. Absolute times for both sides, and the number of runs, with median and spread.
6. The current name of the method renamed in 2.0, and its signature.
7. A defensible adoption number (see paragraph four) or approval to drop the claim.
8. Cases where the speedup was small, zero, or negative.
9. A link to the benchmark script or repo, if it can be public.

## Replacement passages

### Title and intro

**Title:** How We Cut Our Index Build Time 12x with Kestrel [or: from X min to Y min]

Replace the "fastest columnar index builder available today" sentence with:

> Our nightly index build for [dataset: N rows, M columns] took [X minutes]. After moving to Kestrel [version], it takes [Y minutes], about 12x faster on [hardware]. This post covers what changed, how we measured it, and where it didn't help.

The "fastest available" claim can't be verified and invites a rebuttal. The replacement states what you measured. If marketing insists on a superlative, scope it: "faster than [Tool A vX] and [Tool B vY] on [workload]". Name those tools only if you ran them.

### Results section

Keep the chart and add the context around it:

> **Setup.** [Hardware]. Dataset: [description]. Baseline: [tool, version, config]. Kestrel: [version, config]. Each build ran [N] times; we report the median, with the range in the chart.
>
> | | Baseline | Kestrel [version] |
> |---|---|---|
> | Build time (median) | [X min] | [Y min] |
> | Peak memory | [A GB] | [B GB] |
> | Index size on disk | [C GB] | [D GB] |
>
> The 12x figure is [X ÷ Y] on this workload. Treat it as one data point, not a general guarantee. The benchmark script is [linked here / available on request].

For the chart:
- Label both axes with units.
- Show run-to-run variance.
- Add a caption that states the baseline and the version.
- Add alt text that includes the actual numbers.

### Paragraph four ("thousands of teams")

Pick one:

- **Verifiable number:** "Kestrel is used in production by [N] teams, based on [source, date]."
- **Our own usage:** "We run Kestrel in production for [what], serving [scale], since [date]."
- **No data:** delete the sentence. Nothing else in the post depends on it.

### New section: where this does not help

Place it after Results. The author should supply the real cases. This is the shape:

> ## Where Kestrel did not help
>
> - **[Workload type, e.g. small indexes]:** build time was [unchanged / only Nx faster], because [reason].
> - **[Constraint, e.g. memory]:** Kestrel uses [more/less] memory during builds, so [consequence].
> - **[Operational cost, e.g. migration]:** moving over took [effort], including [specific breaking change].
> - **[Query side]:** this post measures build time only. Query latency was [measured and unchanged / not measured].
>
> If your builds already finish in [threshold] or you're bottlenecked on [I/O / network], expect little gain.

This is the section that makes the 12x believable.

### Code snippet

Make it copy-paste runnable:

```python
import kestrel  # kestrel >= 2.0

# Replace with the 2.0+ method and signature.
index = kestrel.<new_method_name>(
    source="data/events.parquet",   # [real args from the author]
    # ...
)
```

Checklist for the author:
- Add every import, plus a `pip install kestrel==[version]` line above the block.
- Replace `build_index()` with the 2.0 name.
- Run the snippet in a clean virtualenv before publishing.
- Trim it to what a reader needs. If 40 lines is still necessary, link a full runnable file and show the key 10–15 lines inline.
- Add a one-line note: "Using Kestrel 1.x? The method was called `build_index()` before 2.0."

### Closing

Replace "we're thrilled to share this journey with the community" with:

> **Takeaways.**
> - On [workload], Kestrel [version] cut our index build from [X] to [Y].
> - Gains depend on [factor]. Check [specific thing] before migrating.
> - To reproduce: [repo link]. Questions or different results? [issues link / contact].

## Final checks before publishing

- Every number in the post traces back to the benchmark notes.
- The snippet runs on a clean install.
- The version in the text matches the version in the snippet and the chart.
- Get a second pair of eyes from someone outside the author's team. The most common failure is missing context that the author no longer notices.
- Have the author verify the Thursday date against the benchmark rerun. If the numbers can't be reproduced by then, publish without the 12x headline rather than delay with a shaky one.

If you paste the full draft, or just the intro, results and snippet, I'll do a line edit for flow and length in one pass. I'll also check the 2,100 words against the new sections, since adding a limits section and a benchmark setup may push it past 2,300.