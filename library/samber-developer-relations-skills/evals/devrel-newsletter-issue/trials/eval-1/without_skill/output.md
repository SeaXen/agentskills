# Quillstack digest: Shipped section and subject line

## Subject line

**Streams 2.0 is live: 3x faster ingestion**

Alternates:
- Streams 2.0 is GA today (Team and Enterprise)
- Our biggest release of the year: Streams 2.0

Before you send, confirm the 3x number is measured and that you can state what it was measured against (see the checks below).

## Shipped

### Streams 2.0 is generally available

Streams 2.0 is our biggest release of the year, and it's GA today for **Team and Enterprise** plans.

The headline is ingestion speed: **3x faster** [confirm: vs. Streams 1.x, on what workload?]. Same pipelines, much less waiting.

- **On Team or Enterprise?** Streams 2.0 is available now. [Add upgrade step or link, e.g. "Update to 2.0.0 and you're set."]
- **On Free?** You get Streams 2.0 in Q1 [confirm: calendar Q1 2027?].

[Link: docs or release notes. There's no blog post yet, so link the changelog or docs page rather than a post that doesn't exist.]

### New in the CLI: `qs replay`

The CLI has a new command, `qs replay`. [Add one sentence on what it does and one example invocation. I don't know what it does, so I haven't guessed.]

```bash
qs replay [example flags/args here]
```

## Check before sending

1. **"3x faster."** This is the claim readers will remember, and the changelog is only a version bump. You need a benchmark or an internal measurement, plus its baseline and conditions. If you only have "roughly 3x in our tests," write "up to 3x faster in our benchmarks." If the number is solid, drop the brackets.
2. **"Customers love it."** I left it out. With no quote, metric, or named customer, it reads as filler to 11k developers. If you have one real customer quote, add it as a single line under the headline.
3. **"Total game-changer."** I left it out too. Developers discount that phrase. The 3x figure and "biggest release of the year" carry the excitement better.
4. **`qs replay`.** Get the one-line description from the PM or the CLI help text. A named command with no explanation will get skimmed past.
5. **"Q1."** Is that calendar Q1 2027 or your fiscal Q1? Developers will read it as calendar, so name the year.
6. **Plan tiers.** Check that "Team and Enterprise" matches your pricing page wording exactly, since Free users will be reading closely.

If you can get me the benchmark details and the `qs replay` description, I'll fill the brackets and tighten the copy.