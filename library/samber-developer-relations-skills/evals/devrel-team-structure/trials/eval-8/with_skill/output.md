# DevRel org design brief — Larkfield Identity, 2026-09-23 (draft for exec review)

**Before you present this:** I built this brief from what you gave me — headcount, the three current homes, and the funded driver — without running the full interview this skill normally requires. Five assumptions stand in for answers I don't have. Confirm or correct them before the exec meeting; each is flagged inline where it drives a decision.

1. Larkfield's self-serve motion means the developer is **both user and buyer** — not just an evaluator who hands off to a procurement-led enterprise deal.
2. No reporting line, manager, or title is politically fixed. If one is (e.g., the platform-engineering headcount can't move), it changes Shape below.
3. You're asking for a **structure recommendation**, not a headcount ask — the two-week deadline reads as "get the shape right," not "get budget for new hires."
4. The 5 people in platform engineering are doing DX-engineering-shaped work (SDKs, samples, integration support), not general product engineering that happens to touch developers.
5. The 2 docs contractors are the only technical-writing coverage — no one else is quietly picking up docs.

---

## Situation

You inherited 11 people doing DevRel work, unmanaged as one function: 4 in product marketing, 5 in platform engineering, 2 contractors on the docs site. This is the norm, not a red flag — 43.6% of surveyed DevRel programs already have more than one team doing this work (*State of Developer Relations 2024*, DevRel.Agency, 310 respondents). The company funds the work to drive self-serve signups: a developer-adoption driver. You have two weeks to bring the exec team a structure.

The tension worth naming up front: the funded driver points to marketing, but the largest existing group (5 of 11) sits in engineering. Any recommendation that moves those 5 people's reporting line is the part of this brief most likely to get contested — plan for that conversation, not just the org chart.

## Candidate structures considered

Per this skill's process, three whole candidates — line, shape, and coverage together — before recommending one.

### Candidate A — Centralized under Marketing (recommended)

All 11 report to you; you report into Marketing (or wherever the self-serve/growth funnel is owned — confirm the exact title). Internally organized by pillar: advocacy/content (ex-product-marketing), DX engineering/SDKs (ex-platform-engineering), docs (contractors).

- **Makes easy:** one voice, one calendar, one place to say no, a direct line to the metric the company is funding this for.
- **Makes hard:** the product/engineering feedback loop, since 5 people move out of engineering's building.
- **Headcount assumed:** 11 (9 FTE + 2 contractors), zero new hires to stand up.
- **Coordination added:** moderate — needs a real, standing interlock with platform engineering to replace the proximity it's giving up.
- **First thing that breaks:** the SDK/DX group's closeness to the eng roadmap, if the interlock isn't funded from day one.
- **Wrong when:** the funded driver is actually product input, not adoption — it isn't, per what you told me.

### Candidate B — Split by focus (Marketing + Platform Engineering)

Advocacy/content (4) stays under Marketing. DX engineering + docs (7) stays under Platform Engineering. Two teams, two managers, a shared-voice owner named between them.

- **Makes easy:** real depth on both awareness and enablement at once; nobody's proximity changes.
- **Makes hard:** one audience, two calendars, two metric sets — the shared-voice problem this skill flags explicitly.
- **Headcount assumed:** 11, split 4/7.
- **Coordination added:** permanent, not setup — split's floor is "roughly eight," and your marketing-side half (4) clears that only if you count generously.
- **First thing that breaks:** duplicated content/docs ownership between the writing contractors and the DX group, since docs sits ambiguously inside the 7.
- **Wrong when:** you have one clear funded driver, not two distinct ones needing separate depth — you have one (self-serve signups), which is the case against this candidate.

### Candidate C — Hub-and-spoke (small hub, spokes near eng and marketing)

A hub of 2–3 (you plus craft leads for content, community, docs) sets standards and calendar; the rest sit as spokes close to platform engineering and to marketing.

- **Makes easy:** consistency with locality — the theoretical best of both other candidates.
- **Makes hard:** everything, on a 2-week clock — this shape's own floor (hub of 2–3 plus 2+ spokes) needs a quarter to stand up and a quarter to unwind if it doesn't work.
- **Headcount assumed:** 11, at the shape's minimum floor with almost no slack.
- **Coordination added:** a full management layer plus a standing forum.
- **First thing that breaks:** the hub turns into an approval queue, because at this size the hub people are also doing their own craft work, not just enabling.
- **Wrong when:** you need a decision in two weeks and an operating structure immediately after — that's you.

**Recommendation: Candidate A.** One funded driver, one team, no new management layer, nothing that needs a quarter to stand up. The real cost — distance from platform engineering — is named and covered below rather than discovered later.

## Reporting line

> DevRel reports to **Marketing** (confirm exact leader/title — whoever owns the self-serve signup funnel metric), because the funded driver is self-serve signups and that leader owns it. This line will starve **the product feedback loop**, concentrated in the 5 people moving out of platform engineering. **A named platform-engineering counterpart** covers that gap via a standing roadmap interlock (below), reviewed at **Q1 close, or immediately if the sponsor changes.**

Source for the line choice: *State of Developer Relations 2024* — marketing 33.1%, product 21.7%, CEO 20.3%, engineering 19.9%, sales 3.2%. No line holds a majority; this is a trade-off, not best practice. Marketing's characteristic failure to watch for: advocates absorbed into pipeline support (webinars, gated assets, lead targets). Counter-move, stated here so it's checkable later: **no DevRel surface carries a lead-gen gate.**

## Shape

Centralized, 11 people (9 FTE + 2 contractors), one manager (you). This skill's baseline is that under roughly ten full-time people, centralized is the only affordable shape — you're just over that line, which is exactly why Candidates B and C looked tempting and exactly why neither clears its own floor comfortably yet. Revisit at ~15–16, where split or hub-and-spoke stop being a stretch.

Rejected: split by focus (shared-voice cost with only one real funded driver to justify it) and hub-and-spoke (needs a quarter to build, you have two weeks and one driver).

## Coverage

| Function | State |
|---|---|
| Advocacy | owned — ex-product-marketing group |
| Community management | **unowned — confirm.** No group among the 11 maps cleanly to this; treat as this brief's primary gap unless you tell me otherwise |
| Technical writing | owned — 2 docs contractors |
| Developer marketing | owned, shared distribution with the broader marketing org |
| Developer education | unowned — recommend **deliberately refusing** this year in writing, not letting it default into someone's spare time |
| Developer-experience engineering | owned — ex-platform-engineering group, SDKs/samples/integration support |

Reality check: the survey shows partial coverage is normal (advocacy 82.2%, community 52.7%, technical writing 42.7%, developer marketing 37.7%, developer education 35.6%, DX engineering 27.4% of teams staffed). An unowned function here isn't a gap in your work — record it as a decision, not an embarrassment.

**Audience note:** self-serve signups implies the developer is both user and buyer (assumption #1 above) — that pulls weight toward advocacy, community, and content over enablement-heavy artefacts. That supports centralizing under Marketing rather than Platform Engineering.

## Roles

Placeholder structure — replace the labels with real names and real hours before you present; I don't have either.

| Person | Surfaces owned | Backup | Capacity assumption |
|---|---|---|---|
| Advocacy/content lead (ex-marketing) | blog, talks, quickstarts | 2nd marketing-group person | 70% of declared capacity |
| 2nd–3rd marketing-group members | developer marketing, campaigns, launch content | rotates within group | 70% |
| DX-engineering lead (ex-platform-eng) | SDK set, samples, roadmap interlock | 2nd DX person | 70% |
| Remaining 4 platform-eng-group members | integration support, sample apps, technical review | pairwise within group | 70% |
| 2 docs contractors | docs site | **none — flagged risk** | not internally controlled |

70% is this skill's chosen planning baseline, not a measured standard — it leaves room for support load, launches and travel. **Bus-factor-one risk: docs.** Contractor coverage with no named internal backup is an outage waiting for a contract non-renewal; fix this in month one, not as an afterthought.

I'm refusing to state an advocate-per-developer or advocate-per-surface ratio — every such number in circulation is a single-company anecdote. Your headcount is what the surface list above says it is, once you fill in the real hours.

## Interlocks

- **Platform Engineering** — facilitation, with a time-boxed collaboration period during the transition quarter — technical review and roadmap visibility in, writing/demo coaching out — arbiter: Head of Platform Engineering. This is the interlock that replaces the proximity you're giving up moving 5 people out; fund it before you announce the move, not after.
- **Product** — collaboration during launches, X-as-a-service otherwise — developer feedback in, launch dates out — arbiter: Head of Product.
- **Support** — X-as-a-service — recurring failure signals in, troubleshooting content out — arbiter: Support lead.
- **Rest of Marketing (brand, paid, campaigns)** — collaboration on campaigns, X-as-a-service on distribution — content in, channels and audience data out — arbiter: your new manager in Marketing.
- **Sales** — X-as-a-service, capped hours/week (set the cap; confirm if sales-assisted deals exist at all given self-serve is the stated driver) — evaluation material out, field objections in — arbiter: your Marketing manager, not Sales. Sales is 3.2% of reporting lines industry-wide for a reason: it buys attribution speed and costs community trust.

One mode per team, by this skill's rule — more than one means nobody can say what the boundary is. Collaboration modes need an end date or they quietly become the operating model.

## Ladder & titles

The ex-marketing 4 likely sit on the marketing ladder (levels on campaign ownership); the ex-engineering 5 likely sit on the engineering ladder. Neither describes DX-engineering-shaped or advocacy-shaped DevRel work well on its own — a borrowed ladder is a slow retention leak, not a loud failure. Recommend adopting the engineering IC ladder's rigor with DevRel-specific criteria, drafted within the first quarter, applied to both groups consistently.

Check any "Head of DevRel"-style title against actual scope before it goes on an org chart — resolve it to a real level (director vs. manager vs. lead) rather than leaving it ambiguous both internally and on the market.

## Budget

**Confirm and record explicitly — I don't have this:** who owns headcount budget for the consolidated 11, and who owns the program budget (events, tooling, docs-site hosting, community platform). In 60% of surveyed programs these are different people; assuming they're the same is how a budget conversation stalls in the exec meeting itself.

## Re-org triggers

- The self-serve-signups driver changes, or its sponsor leaves.
- A second team starts doing DevRel-shaped work (content, community, docs) without a declared interlock.
- Docs stays at bus-factor-one for another quarter without a named internal backup.
- The Platform Engineering interlock stays in collaboration mode past the transition quarter it was scoped for.
- Headcount crosses ~15–16, where split or hub-and-spoke stop needing a stretch to staff.
- Community management stays unowned for two quarters without a written refusal decision.

## Transition

- **Week 1:** publish this brief with real names and hours substituted in; have the reporting-line conversation directly with the current managers of the 5 (platform engineering) and 4 (product marketing) before the exec meeting, not after — this is the part most likely to get renegotiated in the room, better to know that going in.
- **Month 1:** stand up the platform-engineering roadmap interlock; make an explicit, written call on community management (hire, re-scope onto an existing advocate, or formally refuse this quarter — don't let it default silently); confirm budget ownership.
- **Quarter 1:** draft the shared ladder criteria; solve the docs bus-factor risk (internal backup writer, or a plan to convert one contractor to FTE); first check against the re-org triggers above.
- **Unchanged:** the developer-education refusal, docs staying inside DevRel rather than under engineering.

## Quality gate

- Work inventory: **incomplete** — structure is here, real owners/hours are not; flagged, not hidden.
- Reporting line: names driver, leader (title to confirm), starved pillar, named cover, review date. ✅
- Shape: justified by coordination cost against a 2-week deadline and a single funded driver, not by company size; rejected shapes are deleted with reasons, not parked. ✅
- All six coverage functions stated, none blank; two marked as gaps in writing. ✅
- Bus-factor-one flagged on docs. ✅
- Every interlock has exactly one mode and a named arbiter (sales cap still needs your number). ⚠️
- 70% capacity ceiling stated as a chosen baseline, not a benchmark. ✅
- Every number sourced or labeled a baseline; no headcount ratio, no compensation band. ✅
- Re-org triggers are observable, non-empty. ✅

Two things keep this from a clean pass: the work-inventory table needs your real names/hours, and the sales interlock needs an actual hour cap. Fill both before this goes to the exec team.