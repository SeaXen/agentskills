Web verification tools were blocked in this session (WebSearch/WebFetch denied, MCP reader erroring), so this is from my knowledge of CHAOSS's metrics work — the core claims below are stable and checkable against `chaoss.community/kb/`.

## Is the 24-hour figure right?

No — it's a misattribution on two counts:

- **CHAOSS defines the metric, not a standard.** The CHAOSS metrics dictionary defines *Time to First Response* (elapsed time from an issue/PR being opened to the first response from anyone other than the original author). It publishes no target value for it. CHAOSS's explicit position is that thresholds are project-specific — you benchmark against your own history, not an external number.
- **The 24h figure is SLA thinking imported from staffed/corporate open source programs.** For an all-volunteer project with no on-call and global timezone spread, a 24h first-response target is a burnout generator, and a quarterly report measured against it will read permanently red — which trains your steering committee to ignore the report.

What research does support: responsiveness is among the strongest predictors of whether a first-time contributor ever comes back (Zhou & Mockus on newcomer retention; Steinmacher's newcomer-barrier surveys). But the effective window in that literature is days, not hours, and a useful human reply beats an instant dismissive one.

Recommendation: **keep the metric, drop the imported threshold.** Measure your current distribution this quarter as the baseline, then set your own target. For a project of your shape, something like *median ≤ 48h, p90 ≤ 7 days, zero items with no human response older than 14 days* is defensible and humane — adjust from what your baseline actually shows.

## What to measure quarterly

**Responsiveness (are people heard)**
1. Time to first response — issues and PRs reported separately; median + p90, bot-filtered, self-responses excluded.
2. Issue resolution duration — median, plus the age distribution of still-open issues.
3. PR review duration / time-to-merge — reviewers are your scarcest resource; this is your burnout early-warning.
4. Stale backlog — count of open issues/PRs with no human response in >30 days. More actionable than any average; this is where "we're ignoring people" actually shows up.

**Community structure (is it durable)**
5. Bus factor — smallest set of people producing >50% of changes. With ~30 recurring contributors, if 3 of them carry 60% of commits, that's your continuity risk, committee-worthy or not.
6. New contributor retention — % of quarter's first-time contributors who contribute again within 90 days. Your leaky-bucket metric; matters more than raw inflow.
7. Organizational spread (CHAOSS *Elephant Factor*) — if contributors are mostly unaffiliated individuals, report "no dominant employer," which is itself a health fact. Concentration matters even without a company behind you.

**Activity (is it alive)**
8. Active contributors in 90 days, split new vs recurring.
9. Merged PRs, closed issues, releases shipped on usual cadence.

**Context (adoption, not health — footer only)**
10. Downloads / package installs, fork count, star delta. Stars are a lagging popularity signal; keep them off the decision axis.

## Measurement practice that keeps the numbers honest

- **Medians and percentiles, never means** — one abandoned 6-month-old issue wrecks a mean.
- **Filter bots and auto-labels**, or the metric reads "3 minutes" and means nothing. If you use triage bots, track *time to first human response* explicitly.
- **Trend beats absolute** — report each metric against the previous 2–3 quarters. The committee should act on direction and on the tail (p90, stale count), not on single values.
- **Collection**: for a quarterly one-pager, a small script over the GitHub API (paginated issues/comments/PR pulls) is enough. CHAOSS's own tooling (GrimoireLab, Augur) exists but is heavy for your cadence.

## Suggested report shape

One page: the 4 responsiveness numbers with quarter-over-quarter deltas, the 3 structural metrics under a "risks" heading, activity as a two-line summary, adoption in the footer. If everything needs a red/green call, restrict it to stale backlog, retention, and bus factor — the three that say "act now" rather than "feel good."

Given there's no company and nothing to sell, skip CHAOSS's DEI-event and marketing-adjacent families entirely — the Response, Evolution, and Risk metric slices above are the right fit for a community-governed toolchain.