---
type: llm
weight: 2
focus: {source: file, path: "deck.html"}
---

PASS only if all of these hold in the filled HTML deck:
- The provided numbers survive unchanged: 400 services/repos, 37 CI configs, 6 weeks, 5 waves, 11 months, 3 days, 41%, 88%, 23 to 9 minutes, 2 days, 12 legacy repos, Q1.
- Most content slide titles are assertions (a full claim such as "Remote caching doubled our hit rate") rather than topic labels ("Results").
- No invented metrics, quotes, or team names.
FAIL if numbers are altered or invented, or if most titles are bare topic labels.

The brief the author worked from follows. Everything it states is supplied, not invented, so judge invention only against it, and do not fail a fact because the list above omits it:

> Turn this talk outline into a slide deck PDF (about 8 to 10 slides) and save it in the current directory. Don't ask me anything, just build it. Name the source file deck.html and the PDF deck.pdf.
>
> Talk: "What we learned moving 400 services to a monorepo" for an internal engineering all-hands, 20 minutes.
> 1. Why: 400 repos, 37 different CI configs, dependency upgrades took 6 weeks on average.
> 2. The plan: one Bazel workspace, migrated in 5 waves over 11 months.
> 3. What went wrong: wave 2 broke release tooling for 3 days; build cache hit rate was only 41% at first.
> 4. Fixes: remote cache plus build-without-the-bytes took cache hit rate to 88%.
> 5. Results: median CI time from 23 minutes to 9 minutes; a cross-cutting dependency upgrade now takes 2 days.
> 6. What we'd do differently: migrate tooling before services; staff a dedicated build team from day one.
> 7. Next: test impact analysis, and retiring the last 12 legacy repos by Q1.
