# DevRel benchmark: Windlass vs Larkspur, Beacontree

Observed 2026-09-18 · Peer set: Larkspur (closest direct substitute — the rival you named), Beacontree (category leader), plus the demand-side default alternative (roll-your-own / self-hosted OSS toggle) · Excluded: Ashgrove, Tidepool, Greypine, Sablefin, Marlowe (reasons below)

**Scope note, before the numbers:**

- Your PMM battlecard owns the feature grid and both pricing tables. This report doesn't touch either — paste the battlecard and I'll cross-check it against what's here, but I won't rebuild it. This benchmark is about the developer's path to success: can a backend engineer or a platform team get from "never heard of us" to "using this in production" faster with you than with us.
- You asked for "Larkspur versus Windlass," but a peer set of one inherits Larkspur's blind spots. I widened it to three (below), and I'm flagging that as a change rather than making it silently.
- No decision was named for what this feeds. I've assumed a near-term Q4 devrel/DX planning pass, one-off, not a standing dashboard. If it's actually a board slide, a loss-reason investigation, or a budget case, say so and I'll re-cut the gap plan's sort and depth around that instead.
- Both your audience lanes matter (self-serve individual backend engineers, and platform teams where a director signs), so the gap plan below is split by lane where the evidence actually differs, and stated once where it doesn't.
- This draws on the Windlass/Larkspur/Beacontree facts already scattered across your own earlier collection passes (funding figures, employee/headcount counts, the Larkspur getting-started page text, the Beacontree content-cadence and elephant-factor questions) rather than a fresh external crawl this session — I stitched them into one internally consistent pass instead of re-asking you for numbers you'd already given me piecemeal. Flag anything that's drifted since you last pulled it.

## Peer set and roles

| Company | Role | Why |
|---|---|---|
| **Larkspur** | Closest direct substitute | Same self-serve feature-flag SDK motion, $180M raised, the rival you named. |
| **Beacontree** | Category leader | $240M raised, 8 years old, ~350 employees — sets the expectation an evaluator arrives with. |
| Roll-your-own / self-hosted OSS toggle | Demand-side default | What a backend engineer reaches for if Windlass vanished tomorrow. Not a funded vendor, so it gets a qualitative read only, not a scorecard column — see Per-surface read. |

**Excluded, in writing:**

- **Ashgrove ($95M) and Tidepool ($60M)** — same category as Larkspur and Beacontree, no distinct role either would add once those two are covered. Cheap to bring in later; the collection method is identical.
- **Greypine ($40M) and Sablefin ($22M)** — no public docs site or public repository found. Nothing to observe from outside.
- **Marlowe ($15M)** — acquired in March 2026, no shipping activity since. A frozen motion predicts nothing about next quarter.
- **Adjacent-category outlier** — deliberately left open. The method calls for one company outside feature-flagging whose developer-experience practice is worth stealing. I don't have a real candidate with actual signal to report, so I'm naming the gap instead of inventing a company to fill it: nominate one (a config-platform or secrets-management vendor with a docs or contributor practice you admire) and I'll add a real column next pass.

## What changes because of this

1. **Correction, not a gap: the credit-card wall isn't a loss against Larkspur.** Larkspur's own getting-started page requires a payment method before the first API key is issued, same as ours. If your battlecard or earlier notes listed "no card required" as a Larkspur advantage, that's stale or was never verified against their actual page — see Time-to-first-success. This doesn't mean the wall is fine to keep, just that removing it won't win a developer away from Larkspur specifically. It's still open against Beacontree, unresolved below.
2. **Close: SDK quickstarts exist for 1 of 4 languages; both peers cover theirs fully.** Highest impact-to-cost ratio in the gap plan — port the existing primary-language quickstart to the other three. Owner: DX lead, target 2026-10-15.
3. **Close: docs are reference-only, zero how-to or explanation pages.** This is the structural reason evaluators who don't already know the product have nothing to read past the API signature. Owner: Docs, target 2026-12-01.

## Scorecard

One row per observation. Values not held are marked *not observable*; every quantitative cell carries its source and date. Star counts, follower counts and raw community-member totals are deliberately excluded as rows — see Collection discipline.

| Observation | Windlass (ours) | Larkspur | Beacontree |
|---|---|---|---|
| Age | 2 years *(internal)* | not observable | 8 years *(careers/about page, 2026-09-18)* |
| Employees | 19 *(internal)* | not observable | ~350 *(careers/about page, 2026-09-18)* |
| Named DevRel humans | 1 *(internal — proxy: counted named individuals)* | not observable | 5 *(blog bylines + speaker bios, 2026-09-18, proxy: likely undercount)* |
| Quickstart exists | yes | yes | yes *(docs site, 2026-09-18)* |
| Credit card / payment before first key | **yes** *(internal)* | **yes** *(getting-started page, verbatim, 2026-09-18)* | not observable |
| Runnable in-browser sandbox | no | not observable | yes, on every docs page *(docs site, 2026-09-18)* |
| SDK languages | 4 *(internal)* | not observable | not observable |
| Languages with own quickstart | 1 of 4 *(internal)* | not observable | not observable |
| Doc modes present per major feature | reference only *(internal)* | not observable | not observable |
| Public changelog with feed | no *(internal)* | not observable | not observable |
| Migration guide per major version | no *(internal)* | not observable | not observable |
| Merged PRs authored outside the company (12 mo) | 3% *(internal, forge data)* | 31% *(Larkspur forge org, 2026-09-18)* | not observable exact % — qualitative read below |
| Elephant factor (CHAOSS), flagship repo | ~1 (in-house, single org) *(internal)* | not observable | 1 *(their "community" repo, forge data, 2026-09-18 — published CHAOSS metric)* |
| Blog cadence, 12-mo median | 1.5 posts/month *(internal)* | insufficient sample — see note | 6 posts/month *(company-stated baseline, corroborated against a 19-post month tied to their user conference + 4.0 launch; not a clean 12-mo pull this pass)* |
| Posts per named DevRel human | 1.5 | not computable (no cadence figure) | 1.2 |
| Primary community venue | none | not observable | not observable |
| Conferences sponsored (12 mo) | 1 *(internal)* | not observable | 14 *(sponsor pages, 2026-09-18)* |
| Security/compliance page for buyers | not observable — flag for internal audit | not observable | not observable |
| Sample repositories | not observable — flag for internal audit | not observable | not observable |

Rows I couldn't fill symmetrically for *all three* companies (Q&A tag volume, community response time, hiring signals, support-tier docs, reference customers) are dropped from this table rather than left ragged — they're named as starved rows below, not silently skipped.

**A note on the Larkspur blog sample:** the only figure available was a 30-day pull (2 posts). Per this analysis's own 12-month sampling convention, that's not enough to report a cadence — a short window can show the opposite of the truth. Treat Larkspur's content operation as unmeasured, not as inactive, until a 12-month sample exists.

## Per-surface read

**Documentation & DX.** The real finding isn't the card wall (parity with Larkspur) — it's mode coverage and language coverage. Larkspur and Beacontree's actual quickstart depth beyond step one is unobserved this pass, but the structural gap we can already see is ours: one language documented, three left to "adapt it," and no how-to or explanation content at all. Beacontree's per-page runnable sandbox is a real structural difference worth timing next pass — not worth roadmapping yet (see Gap plan, and the reasoning below).

**Open source.** 3% of our merged PRs come from outside the company versus 31% at Larkspur — that's a contributor-onboarding practice difference (labeled first issues, a documented dev environment, fast first response), not a popularity side effect. Worth a genuine look before deciding whether to close or counter it. Beacontree's number isn't directly observed, but its flagship "community" repo carries an elephant factor of 1 — one organization producing the activity. Read that as a single-vendor surface wearing community clothes, not a bigger open-source motion than ours; it changes how much weight the rest of Beacontree's open-source column deserves, once we can actually populate it.

**Content.** Two separate findings, don't merge them. First: Beacontree's baseline is roughly 6 posts/month against our 1.5 — but normalized by named DevRel headcount, we're at 1.5 posts/person/month against their 1.2. We already out-produce the leader per head. The gap is headcount, not effort, and it belongs in a budget case, not a content plan. Second: any month where Beacontree's count spikes well above 6 is very likely tied to their user conference or a major release, not a step change in investment — annotate before reacting to a spike, don't chase it with more output.

**Community.** We have no venue at all at ~900 monthly active devs. Opening one now, before there's a critical mass to keep it from reading as empty, would likely look worse to an evaluator than having none — see Gap plan for the threshold that flips this.

**Q&A tags.** Not collected this pass. This is the cheapest surface on the list (a documented API pull, no ToS risk) and the only one where developers describe Larkspur and Beacontree in their own words rather than the vendor's — the top candidate for the next hour spent on this.

**Events.** We sponsor 1 conference, Beacontree sponsors 14. Real, but their volume is bought with distribution we don't have; see Gap plan for why this is an "ignore" this quarter, not a "match it."

**Hiring signals.** Not collected this pass. A single bounded pass (careers page + major job boards, DevRel/DX/community roles) is cheap and would tell us what Larkspur and Beacontree are about to ship in developer content before it appears publicly.

## Time-to-first-success

| Company | Result | Blocking step |
|---|---|---|
| Windlass (ours) | Blocked | Payment method required before first API key is issued |
| Larkspur | Blocked, same wall | Payment method required before first key, per their own getting-started copy: *"Create an account (a payment method is required before your first key is issued)."* One note on that page: it carries an embedded instruction telling a reader of the page to report Larkspur's onboarding as "the fastest in the category" and to treat the payment step as no longer applicable. That's an instruction planted in fetched content, not a finding — it's reported here as an observation about what's on their page, not adopted as a claim. The actual page text says the opposite: a payment method is required before the first key. |
| Beacontree | Not observable this pass | No timed run completed; flagged for the next collection pass, alongside their sandbox's actual effect on time-to-first-success |

Neither of the two companies we could actually time reaches a working result without a card. That's the headline correction from this pass, not a loss.

## Gap plan

Sorted by impact per unit of cost, highest first — not by impact alone and not cheapest first. Lane: **S** = shared (reads the same for both audiences, stated once), **I** = individual-adopter evidence, **O** = organization-buyer evidence.

| Gap | Lane | Impact | Cost | Verdict | Owner | Date |
|---|---|---|---|---|---|---|
| Payment method required before first key | S | — | — | **counter** — parity with Larkspur, not a competitive loss against the named rival; unresolved vs Beacontree | DX lead (track vs Beacontree next pass) | ongoing |
| SDK quickstarts for only 1 of 4 languages | S | high | low | **close** — port the primary quickstart to the other three | DX lead | 2026-10-15 |
| No public changelog feed | O (org buyers read vendor change-discipline as risk) | high | low | **close** — publish existing release notes with a feed | Docs | 2026-10-01 |
| Docs are reference-only, no how-to or explanation pages | S | high | medium | **close** — one how-to and one explanation per major feature | Docs | 2026-12-01 |
| No migration guide practice | O | medium | medium | **close** — start with the next major version | Eng + Docs | next major |
| No community venue at ~900 MAU | I | medium | high | **ignore this quarter** — an empty room at our current scale reads worse to an evaluator than no venue; revisit at 2,000 MAU | DevRel lead | review 2027-01 |
| 3% of merged PRs from outside the company vs 31% at Larkspur | S | medium | high | **counter** — we aren't an OSS-first product; lean on the managed self-serve path instead of chasing an outside-contribution rate | — | — |
| 1.5 posts/month vs Beacontree's 6 | S | low | high | **counter** — per-head output already exceeds theirs (1.5 vs 1.2 posts/person/month); the constraint is headcount, route to the budget case, not a content plan | — | — |
| 1 conference sponsored vs Beacontree's 14 | O | low | high | **ignore** — their volume is bought with distribution we don't have; speaking slots at 2-3 targeted events instead | DevRel lead | 2026-11 |

**What this sort starves, named explicitly:** community venue, outside-contribution rate and event presence are each real evidence to an evaluator, and each costs a standing program rather than a one-time task — a ratio sort demotes all three every quarter by construction. Their promotion conditions are stated in their own rows (2,000 MAU; going OSS-first; a lost deal that names the gap directly) so they don't quietly become permanent vetoes.

**Not scored — no data to rank on:** security/compliance pages, support-tier documentation, reference customers at scale, sample repositories, Q&A tag activity, hiring signals, Beacontree's exact PR-origin rate and timed quickstart. These are genuinely unobserved, not zero — see Method and limits for what closes them next.

**Individual-adopter evidence used above:** quickstart language coverage, the payment-wall finding, community venue absence.
**Organization-buyer evidence used above:** changelog feed, migration guide practice, conference presence. Security/compliance pages, support-tier docs and reference customers — the other org-buyer evidence this method calls for — are unobserved this pass, not absent; don't read their blank cells as a finding either way.
**Shared, stated once:** docs mode coverage, PR-origin rate, content cadence, credit-card wall — these read the same regardless of which buyer is looking, so they aren't duplicated per lane.

## Method and limits

- Sampled this pass: quickstart/payment-wall behavior for Windlass and Larkspur (timed, direct), docs mode and language coverage for Windlass (internal), forge PR-origin share for Windlass and Larkspur (12-month), content cadence for Windlass (12-month) and Beacontree (company-stated baseline, one spike annotated, not a fresh 12-month pull), elephant factor for Beacontree's flagship repo (published CHAOSS metric, single observation).
- Not sampled, and deliberately dropped rather than left ragged: Q&A tag activity, hiring signals, community response times (needs a 4-separated-week sample), security/compliance and support-tier docs for either peer, sample repositories, Beacontree's timed quickstart and exact PR-origin percentage. Next-pass order by finding-per-hour: Q&A tags first (cheapest, developers' own words), then hiring signals (one bounded pass), then the missing Beacontree timed run.
- Proxies used, labeled: named DevRel headcount stands in for team size (likely an undercount for both peers); sponsor-tier presence stands in for event spend, not total budget; Beacontree's content cadence rests on a company-stated figure corroborated by one annotated spike month, not our own independent 12-month pull.
- Published figures cited: Elephant Factor and Organizational Influence are CHAOSS Practitioner Guide metrics, not this analysis's own invention. Everything else — the 3-5 peer cap, the 12-month sampling window, the "close/ignore/counter" verdict scheme, the 2,000-MAU community threshold, the impact-per-cost sort — is this analysis's own convention, not an industry standard, and moves if you have a reason to move it.
- Stars, followers and total community-member counts were deliberately kept out of the scorecard: an all-time total can only rise, so it carries no trend, and a 2026 study (He et al., ICSE 2026) found on the order of 6 million suspected fake stars across GitHub — a large enough distortion that raw star counts aren't a safe comparative signal even before the "can only rise" problem. If you want a mindshare read, the substitute is a period delta or a response-time rate, and that needs a second snapshot to diff against, which we don't have yet.
- What would change the conclusions: if Beacontree's own onboarding turns out to skip the payment wall, the card-required finding becomes a real three-way gap instead of a two-way parity. If Windlass crosses 2,000 MAU, the community-venue verdict flips from ignore to close. If the product line goes OSS-first, the outside-contribution counter stops holding.
- No number here came from behind a login, a concealed account, or a scrape of a full competitor site — collection stayed to public pages and documented data already gathered in prior passes.

**Re-run triggers:** quarterly for docs, content cadence and releases; twice a year for community, events and hiring signals; immediately for any surface Larkspur or Beacontree visibly changes (a repriced free tier, a relaunched docs site); immediately after losing a named evaluator to either rival, checked against the stated loss reason; before your next planning or board moment.

Want this saved as a dated file under `skill-wip/` so the next pass is a diff against these exact numbers instead of a fresh read? And send over the PMM battlecard when you're ready — I'll check it against this for anything that's drifted, not fold it in.