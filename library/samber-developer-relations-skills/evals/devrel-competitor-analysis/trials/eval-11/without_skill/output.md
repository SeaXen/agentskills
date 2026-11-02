## Top 3 quick wins this quarter

**Picks, ranked: (a) drop the credit-card gate → (b) fill the SDK-quickstart gap → (g) stand up a community venue.**

These three hit each stage of the funnel — acquisition, activation, retention — and each is scoped to ship inside one quarter with existing headcount. The other five gaps are real but don't clear the bar: either the payoff needs a structural change bigger than a quarter, or the metric can't move without an external trigger (a breaking release, a sponsorship cycle).

### Scoring the full list

| Gap | Impact | Effort (this quarter) | Verdict |
|---|---|---|---|
| (a) CC required before first key | High — kills top-of-funnel before eval starts | Medium — needs abuse guardrails, not new infra | 🎯 Quick win |
| (b) 1/4 languages have quickstarts | High — 3 of 4 dev segments get no onboarding path | Medium — writing + testing, no eng dependency | 🎯 Quick win |
| (g) No community venue, 900 MAU | High — audience exists, zero cost to seed it | Low — platform stand-up is days, not weeks | 🎯 Quick win |
| (d) No changelog | Medium — trust/retention signal | Low | Bundle in if capacity allows |
| (e) No migration-guide practice | Medium — only pays off against an actual breaking change | Low to adopt, but no event to prove it on this quarter | Park — adopt as a template now, measure next breaking release |
| (c) Docs are reference-only | High long-term — but a Diataxis-style rebuild is a multi-quarter content program | High | Roadmap item, not a quick win |
| (f) 3% vs 31% external PRs | High long-term — but moving a contribution culture takes >1 quarter | High | Roadmap item; community venue (g) is the seed |
| (h) 1 vs 14 conference sponsorships | Medium — sponsorships lock months ahead of the event | High (budget cycle, lead time) | Not achievable this quarter |

### 1. Kill the credit-card gate

Every developer-tool free-tier teardown (Stripe, Cloudflare, Supabase, PlanetScale) converges on the same rule: no card for the free tier, full functionality, limits on usage not on evaluation. Requiring a card before the first key is the single highest-friction step in the entire funnel — it filters out exactly the browsing, evaluating, side-project developers who become advocates and later become paying accounts. Neither competitor gates on this, so every side-by-side trial you lose here is a trial they win by default.

- Replace the CC gate with usage-capped keys (rate limit + hard monthly ceiling) plus email/domain verification for fraud control.
- Owner: product + eng (billing/fraud logic), ~1 sprint to design guardrails, rest of quarter to ship and monitor abuse rate.
- Success metric: signup-to-first-call conversion rate, week-over-week, against pre-change baseline.
- ⚠️ Risk: free-tier abuse (crypto miners, scrapers). Mitigate with the same usage caps Stripe/Algolia use — cost stays bounded even if signups spike.

### 2. Ship quickstarts for the other 3 languages

Docs are the actual onboarding UI for an API product. A developer who lands on your docs in their language and finds nothing gives up in under a minute — that's true for 75% of your language surface today, and 0% of Larkspur's or Beacontree's. This is pure content work: no product change, no eng dependency, fully parallelizable across a quarter.

- Scope: one quickstart per missing SDK — install, auth, first call, common error, next steps. Mirror the structure of your one existing quickstart so the four feel like one family, not four different authors.
- Owner: DevRel/docs, can run in parallel with (1) and (3).
- Success metric: activation rate (first successful call within 24h) segmented by language, before/after.

### 3. Stand up one official community venue

You have 900 monthly active developers and nowhere for them to talk to each other or to you. That's a channel sitting unused — support deflection, product feedback, and the seed audience for eventually moving the 3%-external-PR number all come from the same room. Cost to launch is near zero; the audience already exists, which is the hard part most communities have to build from scratch.

1. Pick Discord if the audience skews individual/OSS, Slack if it skews enterprise teams — check which one competitors' communities already use before defaulting.
2. Stand up the minimum structure: #welcome, #help, #announcements, #show-what-you-built, #feedback.
3. Seed it directly — email the 900 MAU with a specific reason to join (office hours, direct line to the team), not a generic "we made a Discord."
4. Route it into (f): tag "good first issue," point new community members at it, and you've started fixing the contribution gap without a separate initiative.
- Owner: DevRel, 1-2 weeks to launch, ongoing light moderation after.
- Success metric: 7-day retention of joiners, and support-ticket deflection rate once #help is active.

### Why not the others, briefly

- **(d) Changelog** — genuinely cheap, ship it opportunistically this quarter if (1)-(3) leave slack, but its impact ceiling is lower than any of the top 3.
- **(e) Migration guides** — adopt the template now so it's ready, but you can't demonstrate a win without a breaking release to point at.
- **(c) Docs restructure, (f) contribution rate, (h) sponsorships** — each real, each needs either a multi-quarter content program, a culture shift, or a booking cycle that doesn't fit "this quarter." Put them on next quarter's roadmap instead of diluting focus now.