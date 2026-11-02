Two of your six numbers don't hold up under this skill's own rules, so I adjusted them rather than force a blank shut with an invented figure. Specifically: **Evaluate** and **Contribute** genuinely have zero data anywhere in what you gave me — inventing a number there would be exactly the failure mode this skill exists to prevent ("an honest map with holes beats a complete map with invented numbers"), so they stay `not instrumented` and move to Gaps. And I didn't compute the 4/112 = 3.6% advocate rate: at n=4 it's far below this skill's 30-event floor (publish the raw list, not a rate), and it silently divides an Advocate-stage count by an Adopt-stage population that was never shown to overlap with it. Instead, I moved your "112 production accounts" figure to where it actually belongs — it's the Adopt stage's own signal, not an Advocate denominator — which fixes a second blank with a real number instead of a fabricated one. Full map below.

---

# Developer journey map — Frontend engineers at product companies, 2026-09-19

## Scope

- **Product:** embeddable charting SDK.
- **Segment:** frontend engineers at product companies.
- **End state:** production usage.
- **Stage model:** the six stages you supplied (Discover → Evaluate → Try → Adopt → Contribute → Advocate). This is this skill's *unsourced default spine* (Discover → Try → Adopt → Contribute → Advocate) with Evaluate split out — a legitimate split, since evaluation (reading docs, comparing alternatives) and trying (hands-on signup) have different owners. Flagging its provenance rather than silently citing it as a published framework: it buys no comparability with Revell/AAARRRP/the API arc, only with your own next re-read.
- **Buyer lane:** not determined — see below.
- **This half's OKR: signups (Try stage), currently 22,900 cumulative.** Watch the Leak section — there's a real risk this metric can climb while the thing it's supposed to be a proxy for (production usage) doesn't move.

## Journey

| Stage | Developer's job | Entry trigger | Exit event | Touchpoints | Owner | Friction evidence | Signal |
|---|---|---|---|---|---|---|---|
| Discover | "Find a charting library I don't have to hand-roll on canvas/SVG." | Sees it via search, GitHub, a "best chart libraries" roundup, or a colleague's mention | Opens the docs or the repo | Search results, GitHub repo, comparison posts, community mentions | Marketing / DevRel | No evidence yet | 11,400 cumulative GitHub stars — `inferred`. Flagged: a monotonic total (can't fall when discovery breaks), and Borges & Valente (2018) found ~37% of stargazers star only *after* they're already using the repo, so this also counts post-adoption behavior, not pure discovery. |
| Evaluate | "Decide if this is production-grade enough to replace building charts ourselves or picking a competitor." | Reads docs, compares against alternatives (D3/Recharts/build-it-yourself, other embeddable SDKs) | Creates an API key / starts a sandbox | Docs, pricing page, comparison content, community threads | Docs owner / product marketing | No evidence yet | `not instrumented` |
| Try | "Get a real chart rendering with our own data in under an hour." | Signs up / creates an API key | First chart rendered with real (non-sample) data — **not yet instrumented**; signup date is currently the only proxy, but that marks *entry into* Try, not completion of it | Signup flow, quickstart docs, package install | Developer experience / docs | No evidence yet | 22,900 cumulative signups — **OKR metric**. Flagged: this is, almost verbatim, this skill's own textbook weak signal ("total signups… monotonic, cannot fall when the stage breaks, and covers multiple stages at once"). |
| Adopt | "Ship this in a real feature that goes to production, not a spike branch." | First chart rendered with real data | SDK actively, sustainedly serving charts from a production environment | Production deploy, plan/billing upgrade, support, status page | Product | No evidence yet | 112 active production accounts → **0.49% of cumulative signups** (112 / 22,900). Reallocated here from the figure originally attached to Advocate — production accounts is literally this map's end state, so it's Adopt's signal, not Advocate's denominator. Caveat: valid only if "signup" and "production account" key off the same account object — confirm before trusting the ratio. |
| Contribute | "Fix or extend the SDK ourselves since we're now relying on it in production." | Hits a bug or missing feature while running in production | First pull request merged | GitHub repo, issue tracker, contribution guide | Maintainers | No evidence yet | `not instrumented` |
| Advocate | "Tell other frontend engineers this saved us from building charts by hand." | Sustained production usage over time (contributing is not a prerequisite) | Gives a talk, writes a post, or makes an unprompted recommendation | Conference CFPs, blog/social, community channels | Community / DevRel | No evidence yet | 4 conference talks by non-employees, Q2 2026 — raw dated list. Below the 30-event floor, so it's published as a count, not a rate, and it is *not* expressed as a share of the 112 production accounts (see Leak). |

## Buyer lane

Not established. I don't have an answer to whether the frontend engineer is the buyer, an influencer, or whether "product companies" means procurement/security review sits between Adopt and Advocate. The fact the data already talks in "accounts" rather than raw users hints that account-level rollup may already be informally happening — worth confirming rather than defaulting this to "none, self-serve." Treated as a gap, not a decision, so it isn't silently assumed either way.

## Moments

- **First success**: chart rendered with the developer's own data for the first time. Time-to-first-success is not instrumented — Try currently only counts signups, which happen *before* success, not at it.
- **Moment of truth**: swapping a prototype/spike implementation for the SDK in the PR that actually ships to production — this is the Try→Adopt boundary, and it's the only boundary on this map with a real number attached (0.49%).
- **Abandonment point**: not determined. No friction log, ticket mining, or exit interviews exist yet for any stage (every row above reads "no evidence yet"). The raw counts hint most people stop somewhere between Evaluate and Adopt, but Evaluate is completely dark, so that's a hypothesis, not a finding.

## Leak

**Adopt.** Not chosen by beating out other measured candidates — it's the *only* stage on this map with a real, computable conversion rate. Discover's number can't feed conversion math (it isn't even the same population as Try: 11,400 stars is smaller than 22,900 signups, which alone proves stars aren't an upstream superset here). Evaluate and Contribute have zero data. Advocate's n=4 is below the statistical floor for a rate. So Adopt wins by elimination, and 0.49% of cumulative signups ever reaching a sustained production account is worth treating as a real problem regardless.

That said: nominating Adopt is also a statement about the map, not just the product. Five of six stages currently cannot support a leak diagnosis at all. Instrumenting Evaluate — the stage sitting on top of the largest currently-invisible population — is arguably more urgent than fixing Adopt itself, even though the ranking rules (earliest-measured, owned) don't let it win this cycle.

**Why it leaks (hypothesis, not yet evidenced — no friction log or exit interviews have run on Adopt):** most likely Ability, not Motivation. Going from "chart renders in a demo" to "shipped in a real feature" typically costs time and mental effort — clearing an internal review, migrating off a spike branch, handling edge cases the trial never surfaced — which is the default answer for a developer audience anyway (Fogg: "motivation is unreliable... ability is not"). Confirm with a friction log walking one real Try→Adopt integration, plus 3 exit interviews with signups who never reached production, before committing budget to a fix.

## Handoff

- **Owner:** Product.
- **Signal to watch:** share of cumulative signups with an active production account (currently 0.49%, 112/22,900).
- **Re-read date:** 2026-12-18 (90 days), or sooner if the quickstart, pricing, or docs change before then.

## Gaps

- **Evaluate** — `not instrumented`. Cheapest fix: count docs sessions reaching a pricing/decision page, or sandbox/API-key creations, owned by docs or product marketing.
- **Contribute** — `not instrumented`. Cheapest fix: first-time contributors per quarter from repo data, owned by maintainers.
- **Discover** — stars flagged as a monotonic, contaminated proxy (Borges & Valente: ~37% star post-adoption). Replace with new-stars-per-month or a self-reported "how did you hear about us" field.
- **Try** — signups flagged as a monotonic total covering more than one stage's worth of behavior. Replace with signups-this-quarter (keeps your OKR trackable as a period metric instead of an ever-climbing total) paired with a quality counter-metric (e.g., 30-day-active rate) so the OKR can't be gamed by throwaway signups — and separately instrument first-real-chart-rendered as Try's actual exit event.
- **Advocate** — n=4, below the 30-event floor. Keep it a dated raw list (add speaker/venue/date per talk) until volume justifies a rate; do not divide it by the 112 production accounts, since nothing here shows those 4 speakers are drawn from that set.
- **Buyer lane** — undetermined; needs an answer to "is the frontend engineer the buyer, an influencer, or neither, and does 'product company' imply a procurement/security step?"
- **Every friction column** — currently "no evidence yet" across all six rows. No friction log, ticket mining, or exit interviews have been run; that's the single biggest gap underneath all the above.

## Quality gate check

- One exit event per stage, phrased as an observable event: ✅
- One owner per stage, at least one outside DevRel: ✅ (docs, developer experience, product, maintainers all appear)
- ≥60% of stages carry a signal with a real current value: ✅ 4/6 (Discover, Try, Adopt, Advocate) = 66.7%; Evaluate and Contribute correctly fall to Gaps instead
- Every friction claim cited, no hypothesis dressed as evidence: ✅ ("no evidence yet" throughout, not invented)
- Exactly one leak, named owner, re-read date: ✅ (Adopt / Product / 2026-12-18)
- Inferred/uninstrumented stages labelled everywhere they appear: ✅
- Fits on one page: ✅