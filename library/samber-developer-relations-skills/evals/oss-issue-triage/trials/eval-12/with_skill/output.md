## Retention per day of first response: no

❌ I can't give you a per-day retention cost, or a percentage gain for 5→3 days. No dose-response curve between issue first-response time and contributor retention exists in the literature this skill draws on — inventing one to put in a leadership deck would be a fabricated number wearing a citation.

The strongest real evidence is adjacent, not on-point:

- Hasan et al., "Understanding the Time to First Response In GitHub Pull Requests," MSR 2023 — 111,094 PRs across 10 projects.
- It measures **pull-request** first response, not **issue** triage — different workflow, different population.
- It's a **binary split**: got a human reply within 1 day vs. didn't. Not a continuous curve, so there is no "per additional day" rate to extract.
- The deltas are **descriptive, not significance-tested**.
- Newcomers answered within 1 day were more likely to submit another PR within a year: median **+15.14 pp** (range 2.63–37.44 pp across the 10 projects).
- Existing contributors: a smaller median **+2.25 pp** (range 0.06–9.48 pp).

You can cite that finding honestly — "fast first response to newcomers correlates with a large jump in return-contribution rate, in the closest published study we have" — but not as "our retention" and not scaled to 5-vs-3 days. Going from 5 to 3 days is inside the "later" bucket either way; the study can't tell you what that move is worth.

**What actually justifies a second triager:** capacity arithmetic, not a retention curve. Run `triage-baseline.py` on nordvex's own issue export to get created-vs-closed inflow, then compare against `triagers × sessions/week × minutes/session ÷ minutes/item`. If capacity < inflow, that gap — in items per week your current triager cannot reach — is the number leadership needs. It's project-specific, it's measured not borrowed, and it's harder to argue with than an imported percentage.

If you want a retention number in the deck badly enough to invest in it: pull nordvex's own history, split first-time issue openers by whether they got a human reply within 1 day vs. later, and check whether they opened a second issue within a year. That's the same design Hasan et al. used, run on your own data — a real number instead of a borrowed one.

## 3 minutes per issue: no, that's a placeholder, not a standard

⚠️ Three minutes isn't a measured industry figure — it's this framework's own placeholder for the capacity formula, used only because nothing project-specific exists yet. Don't put it in the deck as a benchmark.

Replace it before the numbers go to leadership:

1. Run one real triage session on nordvex's actual queue, 15–20 items, timed.
2. Divide total minutes by items triaged.
3. Use that figure in the capacity formula going forward — it's nordvex's own number, and it'll be more persuasive to leadership than an unsourced constant anyway.

## Target untriaged percentage: 10%, labeled correctly

ℹ️ Under 10% of open items untriaged is a reasonable starting target — but it's this framework's self-set baseline, not an industry benchmark. Same status for two figures you'll likely want alongside it: published response target met on ≥90% of items, and net inflow at or below zero over a quarter. Put all three in the deck as starting points, not proof points, and say so.

Before leadership treats any of the three as settled:

- Re-run the baseline script monthly for nordvex's first quarter.
- Replace each self-set number with nordvex's own measured distribution once that quarter of data exists.
- If the 10%/90%/zero-inflow targets don't hold with current staffing, that's your headcount evidence — lower the published promise to what the team actually sustains rather than leaving an unmet number in a public policy, and use the shortfall itself as the ask.