Note before the deliverable: WebSearch/WebFetch permission wasn't granted this session, so I couldn't fetch fresh 2026 survey waves. Per the skill's own fallback rule ("if you cannot browse, size from first-party data only, mark every external figure inferred"), everything below is built from what's already sourced in this skill's own reference files plus pre-2026 background knowledge — clearly tiered, with the exact lookups that would upgrade it if you grant browsing.

---

# Segment sizing check — Loomstack (LLM-application evaluation harness)

## Your math, checked

**Verdict: invalid as a population estimate.** All three numbers measure something other than "ML engineers," and none of them can be summed or eyeballed into a headcount.

| Your number | Source class | What it actually measures | Safe to claim | Not safe to claim |
|---|---|---|---|---|
| 2.1M models | artifact hub catalogue (open model hub) | publishing activity — listings, not people | the shape of the niche: formats, base models, task types in play | population; publishing is free and unreviewed |
| 940K datasets | same hub, same class | publishing activity | same as above | same as above |
| 380K downloads/month | package registry, first-party | adoption trend for one library | rough usage trend of your own package | human users — CI runs, container rebuilds and repeat installs inflate registry download counts |

Concrete correction on the model count, from the hub operator's own disclosure (August 2026): **85.6% of published models have fewer than 200 lifetime downloads, and 1.5% of repositories account for 99.2% of all downloads.** Applying that: roughly 300K of your 2.1M models (the ~14.4% above the long tail) show any real usage. That's still a count of *artifacts*, not people — one account can publish or pull hundreds of model variants, and a chunk of that traffic is automated (CI, eval pipelines, mirrors) rather than a human at a keyboard. Treat 2.1M and 940K as evidence of how large and active the hub is, not as a stand-in headcount for anyone using it.

Same logic on your own 380K/month: it's the one number here you actually measured, so it's real evidence your package adopts. It is not 380K distinct ML engineers — repeat installs per pipeline run dominate most registry download graphs, so unique monthly humans behind that figure is very likely a small fraction of 380K. I don't have a verified percentage for your specific package to apply, so I'm not inventing one (see "to upgrade" below).

Net: none of the three numbers are population counts, and stacking them doesn't produce one either. This is the exact move the sizing method refuses by name: *"a hub's catalogue size as a market."*

## Segment size, cross-checked against an independent source class

```
Global professional developer population: ~51M
  method:     derived from SlashData/CNCF "State of Cloud Native Development," Q1 2026
              (19.9M cloud-native developers = 39% of the global developer population → 19.9M ÷ 0.39)
  as of:      Q1 2026
  confidence: estimated (sourced report, re-derived arithmetically; not freshly fetched this session)
```

```
ML/AI developers, global: ~4M–10M
  method:     ~51M global developer population × an AI/ML sector share of 8-20%,
              drawn from pre-2026-wave recollection of SlashData sector sizing and Stack Overflow
              role-category splits — NOT fetched fresh this session
  as of:      waves through ~2025, unverified for 2026
  confidence: inferred — the wide range reflects an unverified multiplier, not the true spread
```

```
Developers actively building or evaluating LLM applications (Loomstack's real target,
narrower than "ML engineers"): no independent population figure found
  confidence: hypothesis segment, below the evidence floor
  cheapest tests: (1) a telemetry cut of your own 380K/month by whatever task/framework signal
                  your install logs already carry; (2) 10 support threads or GitHub issues read
                  end to end, tagged for what the requester was building; (3) one landing page
                  written in this segment's own words (RAG evaluation, agent evaluation, prompt
                  regression testing), measured on qualified signups rather than traffic
```

The addressable segment for Loomstack is that **third row**, not the first two. "ML engineers" is a workload family the product sits inside, but most ML engineers never touch LLM-application evaluation — they're doing classical ML, computer vision, recsys, and so on. Sizing "ML engineers" and calling it your addressable segment overstates the market the same way the hub catalogue numbers do, just one layer up.

## What this number cannot support

- **A precise headcount** — every figure above is order-of-magnitude, and the middle row's multiplier is unverified this session.
- **A claim that it's reachable** — size alone doesn't clear the method's accessibility test. You'd still need to name a venue (which subreddits, which hub collections, which conference) where this specific sub-segment actually gathers.
- **A revenue or funnel number** — none of this says how many would evaluate, let alone buy, Loomstack.
- **"Very large," unqualified** — ~4-10M ML/AI developers is a believable order of magnitude; the LLM-app-evaluation sub-slice inside it could be anywhere from the low hundreds of thousands to a couple million. Right now that's a hypothesis, not a size.

## To upgrade this from inferred to estimated

- Grant WebSearch/WebFetch and pull SlashData's current AI/ML sector sizing report (AI/ML is one of the twelve sectors SlashData tracks — this replaces the 8-20% guess with a sourced percentage) and Stack Overflow's 2025/2026 role breakdown for "data scientist / ML engineer."
- Pull the registry's public download-stats dataset (e.g. the PyPI BigQuery dataset, if that's your registry) filtered by installer/user-agent to separate CI installs from likely-human ones on your own package — turns 380K/month into a real proxy for active users instead of raw installs.
- If Loomstack has any telemetry on what evaluated tasks look like (RAG vs. agents vs. fine-tuning vs. classic ML), that first-party cut would move the third row out of hypothesis status faster than any public source can.