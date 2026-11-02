# DevRel benchmark setup: Windlass vs. feature-flag category — Q4 2026

**Status:** peer set framed, scorecard frozen, collection plan sequenced. No live collection has run yet — steps below are ready to execute this week. Observed date: 2026-09-20.

## Before the scorecard: the VP's list needs re-cutting

Ranking by last raise and handing over all seven is the exact anti-pattern this method warns against, for three compounding reasons:

1. **Funding rank measures distribution, not developer experience.** Beacontree at $240M and Larkspur at $180M can fund docs teams, twelve-language SDK coverage, and a conference circuit that a 900-MAU self-serve product has no budget to match. If the Q4 plan ends up being "publish and sponsor as much as Beacontree," that's the volume-matching failure this method flags by name — their output level is funded by scale Windlass doesn't have; only their *choices* (which artefact types they bother to build at all) transfer.
2. **Three of the seven have no developer surface to observe.** You already found this: Greypine and Sablefin have no public docs or repos, and Marlowe's motion froze after its March acquisition. That's not a data gap to paper over — a benchmark row that can't reach symmetry across the set gets deleted, not left ragged. All three are **excluded**, same as the worked example's "one acquired last year whose motion is frozen and will not predict anything."
3. **Seven exceeds this method's own peer cap (3–5, set by this analysis, not an industry rule).** Past five, each added column dilutes the others and the analysis stops converging on a plan anyone can act on this quarter.

That leaves four vendors with a real public developer surface — Beacontree, Larkspur, Ashgrove, Tidepool — plus a fifth slot the funding-ranked list never asks about at all: what would a Windlass developer actually reach for if Windlass vanished tomorrow? For a self-serve backend SDK, that's very likely a config-toggle rolled by hand, or the open-source path (OpenFeature's vendor-neutral spec paired with an OSS flag backend). That's the demand-side peer the funding list structurally can't surface, and it's frequently the most instructive column in the table.

**Peer set (5, at cap):**

| Peer | Role | Why |
|---|---|---|
| Beacontree ($240M) | Category leader | Largest round in the set — sets the DX expectation an evaluator arrives with, whether or not Windlass competes with them for the same deal |
| Larkspur ($180M) | Second enterprise-scale data point | Same funding tier as Beacontree; likely also sales-led at this scale — confirm GTM motion before treating it as a second "leader" read vs. a genuine substitute |
| Ashgrove ($95M) *or* Tidepool ($60M) | Closest direct substitute — **pick one, provisional** | Smaller rounds in this category more often mean the company is still running a self-serve/PLG motion closer to Windlass's own stage. Unconfirmed from funding alone — first thing to check when collection starts (rung 1, the quickstart itself, answers this in an hour: does it ask for a credit card or a sales call, same as Windlass) |
| Tidepool ($60M) *or* Ashgrove | Second substitute / stage check | Keeps both smaller-round vendors in frame until the quickstart run tells you which one is the real self-serve peer |
| Demand-side: config-toggle / OpenFeature + OSS backend | Adjacent-category outlier, stand-in | What a developer builds or adopts for free instead of buying anyone on this list. No funding, no vendor — that's the point |

**Excluded, and why:**

- **Greypine** — no public docs or repository found; nothing to observe. Not observable from outside, deleted rather than left blank.
- **Sablefin** — same as Greypine.
- **Marlowe** — acquired March 2026, no shipping activity since; a frozen motion predicts nothing about Q4. Worth one separate note to DevRel/community, not a scorecard column: if Marlowe had any public community or forum, its members are an orphaned audience — a possible outreach target, but that's a community-capture tactic, not a devrel-DX comparison, and doesn't belong in this table.

**Gap this leaves, flagged rather than silently accepted:** the method calls for a third role — an outlier *outside* the feature-flag category whose practice is worth stealing (the worked example uses a database company's contributor-onboarding practice). None of the VP's seven sit outside the category, so this peer set has zero cross-category idea import. Recommend either swapping the weaker of Ashgrove/Tidepool for a named outlier (an API-first company with unusually good DX — Stripe- or Twilio-shaped, not feature-flag-shaped) once the substitute role is confirmed, or accepting the gap this quarter and saying so in the final report. Your call — flagging it rather than deciding it for you.

## Audience lane

Windlass sells self-serve to backend teams at ~900 MAU — read as **individual-developer-adopter led**. Weight collection toward quickstart time, free-tier reach, sample repos, and community/Q&A answer speed over security/compliance pages and enterprise support-tier docs. If any of the four vendors turn out to be enterprise-gated (credit card or sales call before first result), that split itself is the finding — Windlass's whole motion depends on not having that wall.

## Frozen scorecard (fields locked, values pending collection)

Same fields for all five columns, Windlass included. Every cell will carry a value, "not observable from outside," or "proxy: \<what stands in\>" plus a source URL and observation date — no cell ships blank or guessed.

**Documentation & DX**
- Quickstart exists; steps to first working result
- Timed first success (minutes); blocking step; credit card / approval / sales call required
- Doc modes present per major feature: tutorial / how-to / reference / explanation
- SDK languages, and which have their own quickstart vs. a shared generic one
- Runnable surfaces: sandbox, playground, seeded demo, one-command local setup
- Machine-readable artefacts: OpenAPI/schema file, `llms.txt`, `AGENTS.md`
- Versioning: versioned docs, migration guide per major version, deprecation timeline, changelog with a feed
- Error-string searchability: does a real error from their SDK land on their own page

**Open source**
- Release frequency (12 mo), point releases included
- Median time to first human response on issues/PRs (bots excluded)
- Change-request closure ratio
- Elephant Factor (CHAOSS): fewest orgs producing 50% of activity — flags a single-vendor repo wearing community clothes
- Share of merged PRs from outside the company
- Community health files present (CONTRIBUTING, CoC, templates, security policy)

**Content** (12-month window, plotted, launch/conference months annotated)
- Posts/month, format mix, author mix (named engineers vs. DevRel vs. marketing vs. guest)
- Evergreen vs. release-bound share
- Posts per named DevRel human (the divisor that keeps this honest against Beacontree's team size)

**Community**
- Which venue is the real one (most list three, staff one)
- Median time to first reply; share of unanswered questions; staff share of replies
- Programs on top of the venue (office hours, champions, public roadmap)

**Q&A tags** (12-month window)
- Question volume and direction per vendor tag
- Median time to accepted answer; share unanswered
- Word frequency across questions — this is the one where developers describe each vendor in their own words, and it's the cheapest surface on the list

**Hiring signals** (one pass, capped)
- Open DX/DevRel/community roles, time open, named ecosystems in requirements

**Events** — only promoted if a sponsorship decision is the actual Q4 deliverable; otherwise stays at the bottom.

## Collection plan, sequenced

Ranked by finding per analyst hour, not by what's quickest to open — a pass cut short at any point still ships something usable:

| Order | Surface | Effort | Why this position |
|---|---|---|---|
| 1 | Timed quickstart, all 5 columns | ~1 hr/peer, ~5 hrs total | The finding evaluators feel most directly; stops at the first paid wall or sales call, which is itself the result |
| 2 | Doc mode coverage | 1–2 hrs/peer | Categorical, transfers regardless of company size — most likely source of "why evaluators pick them" |
| 3 | Forge release & response metrics | 1 API pull/repo | Only clean collection route under GitHub's acceptable-use terms is the API, not scraping — use it, respect rate limits |
| 4 | Q&A tags | cheapest surface on the list | Developers' own words, not the vendor's |
| 5 | Content cadence | 1 day, full 12-month sample — no 30-day shortcut, it reports the opposite of the truth | Needed to tell a launch burst from a trend |
| 6 | Community | 1 day + 4 sampled weeks | Answers retention/ecosystem questions nothing above reaches; heaviest compliance-review surface, stay logged-out, no account, no export |
| 7 | Hiring | 1 hr, capped at one pass | Leading indicator, high false-positive rate |
| 8 | Events | 1 day | Only worth it if sponsorship is the actual decision this quarter |

Given a Q4-planning-cycle deadline (weeks, not days), the full pass fits — this isn't a same-week crunch that would force stopping at rung 3. Recommend running 1–5 this week (roughly 2 analyst-days across 5 columns) and 6–8 the following week.

## Time-to-first-success protocol

One person, one machine, a timer, no prior familiarity with the product where possible. Record: minutes to first working result, the exact step that blocked (paid wall / sales contact / missing docs / broken sample), and whether Windlass's own onboarding was re-run the same week for a fair comparison — not carried over from an old number.

## Gap plan (template — verdict required on every row once populated)

| Gap | Impact | Cost | Verdict | Owner | Date |
|---|---|---|---|---|---|
| *(populated after collection)* | | | close / ignore / counter | | |

Sort by impact per unit of cost, highest first, once real rows exist — state that sort in the final report. Every row gets a verdict; a gap without one is trivia, and the recorded *ignores* are what stop the same gap being rediscovered next quarter. Where cost genuinely can't be sized from outside, say so in the cell and rank on impact alone.

## Method and limits

- **Set by this analysis, not industry standard:** the 3–5 peer cap (landed at 5), the 12-month sampling window, the 4-week community sample, 100% symmetry/traceability/verdict targets.
- **Observed by you already, carried in as given:** Greypine and Sablefin have no public developer surface; Marlowe's motion froze at its March 2026 acquisition. Not independently re-verified — worth a 5-minute recheck before the report ships, since "no public surface" can change between now and collection.
- **Not yet observed:** every scorecard cell above. This document sets up the analysis; it does not yet contain a single live measurement.
- **Open judgment call, needs your sign-off:** which of Ashgrove/Tidepool is the closer substitute, and whether to swap one for a true cross-category outlier.
- **What would change the conclusions:** either substitute shipping a free tier that removes Windlass's main quickstart advantage, or Beacontree's motion turning out to be sales-led rather than self-serve, which would make it a weaker "category leader" read for an individual-adopter audience.

## Re-run triggers

| Trigger | Scope |
|---|---|
| Before the Q4 plan lands | Whatever the argument rests on — run this now |
| A named peer ships a major launch or reprices | That peer's affected surfaces, immediately |
| Quarterly | Docs, content cadence, releases |
| Twice yearly | Community, events, hiring |

## Persisting this

Save the peer set with roles, the frozen field list above, and the collection plan as the dated baseline — the next run becomes a diff against these five columns instead of a fresh opinion. If this session's memory isn't retained for the Windlass project, put this document in the team's workspace under a dated filename (e.g. `2026-09-20-devrel-benchmark-setup.md`) before collection starts, so the frozen scorecard and the recorded exclusions don't have to be re-argued next quarter.