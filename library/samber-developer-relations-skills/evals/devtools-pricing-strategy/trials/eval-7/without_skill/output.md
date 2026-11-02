## Short answer: No — the board is benchmarking against the wrong thing, not looking at a broken number.

The 10-15% figure is almost certainly a **trial-to-paid** conversion benchmark (14/30-day full-access trials, often requiring a credit card up front), or a broad horizontal-SaaS freemium benchmark (Slack/Zoom/Dropbox-style tools with mass consumer-adjacent audiences). Rillwater Migrate is a **CLI-first infrastructure tool with a permanent free tier** — a structurally different funnel, and the two numbers aren't measuring the same thing.

## Why the comparison breaks down

1. **Funnel depth is different.** A free trial only starts once someone has already decided to seriously evaluate you — they've cleared the "is this worth 20 minutes" bar. A permanent free tier is open at the very top of the funnel: curious devs, people testing a one-off migration, CI/script users, students, people bookmarking it for a project six months out. Comparing conversion rates across two different funnel entry points isn't apples to apples — you'd expect the permanent-free-tier number to be lower by design, not by defect.

2. **Category benchmarks differ sharply from "SaaS" in general.** Published PLG conversion data (OpenView, ProfitWell) consistently shows infrastructure/dev-tool categories converting in the **2-5% range**, while horizontal productivity/collaboration SaaS is where the 10-15%+ figures cluster. A CLI database migration tool is about as far into "infra/dev-tool" territory as it gets. 4.2% sits squarely inside the normal range for your actual category — it's not an outlier, and it's not what "broken" looks like.

3. **The denominator is inflated relative to real buying intent.** For a CLI tool, "signup" often just means "ran an install command to try a migration once." Many of those 22,000 were never going to be a paid customer — they're evaluators, one-time script users, or people testing against a side project. Blending them into the same denominator as your genuinely-activated, repeat-usage developers understates the health of the part of the funnel that actually matters.

## The number that actually tells you the business is healthy: 104% NRR

This is the tell the board is missing. A free tier that's failing to convert *and* leaking value would show up as flat or declining NRR — existing paying customers churning or downgrading faster than they expand. 104% NRR says the opposite: once someone converts, they stick and grow. That's the signature of a free tier doing its real job — filtering for the right people and letting them self-select into paid as their usage grows — not a leaky bucket.

Do the arithmetic on what 4.2% actually produced: roughly **924 new paying customers** from that signup cohort, feeding into three tiers starting at $39/mo, compounding at 104% NRR. That's a funnel generating real revenue and durable revenue, not a rounding error to be scared by.

## What cutting the free tier would actually do

Restricting the free tier to "force" payment misdiagnoses the problem as a conversion-rate problem when the evidence points to a top-of-funnel-composition problem. For a CLI-first tool specifically:

- **Adoption and word-of-mouth run through frictionless trial.** Developers install and try tools before they ever consider paying, and they recommend tools they were able to freely test. Tightening the free tier doesn't convert the 95.8% who wouldn't pay — it mostly kills the discovery motion that eventually feeds both direct conversions and indirect ones (recommendations, team adoption after one dev tries it solo).
- **It risks the 104% NRR, not just the 4.2%.** Expansion revenue depends on satisfied users who started on free and grew into it. Squeeze the tier that built that trust and you risk both ends: fewer new conversions *and* worse retention/expansion from people who feel the rug pulled (a well-documented resentment pattern — see HashiCorp/Redis-style backlash when free tiers get retroactively cut).
- **The signups likely aren't the same 22,000 you'd get post-cut.** A more restrictive tier doesn't just convert existing signups at a higher rate — it changes who signs up at all. You'd likely see a smaller, more purely "must-have-it-now" pool, not necessarily a higher-converting one, and you lose the passive top-of-funnel entirely.

## What I'd actually bring to the board instead

1. **Reframe the benchmark.** Show the 2-5% infra/dev-tool PLG conversion range next to the 4.2% and next to 104% NRR. That's the comparison that matters, not the generic 10-15% SaaS figure.
2. **Segment the 4.2%.** Break signups into "activated" (ran a real migration, came back more than once) vs. one-shot evaluators. Report free-to-paid conversion *of activated users* — that number is almost certainly well above 4.2% and is the one that should anchor the board's judgment of funnel health.
3. **If you want to move conversion, don't cut the tier — tighten the right dimension.** Usage-based limits that scale with real project growth (number of concurrent migrations, database size/row count, team seats, migration history/rollback retention) create natural upgrade triggers without blocking evaluation. That's a targeted lever; a blanket cut is a blunt one that trades funnel and NRR risk for a metric that was being measured against the wrong yardstick in the first place.