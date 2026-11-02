# Segment evaluation: "Air-gapped defence integrators" — decision memo for next quarter's plan

Ran this through `developer-segmentation` step 5 (score, evidence floor) and step 6 (map format). Short version first, then the full writeup.

**Verdict: this does not clear the bar for a funded segment. It's a hypothesis segment — real candidate, wrong evidence, and the SDK spend should wait on a cheap test, not proceed now.** That's not a rejection of the idea; it's what the skill's own evidence floor is for, and it's cheaper to find out now than after four engineer-months.

## Why "put it in the plan as funded" doesn't hold up

**Evidence floor check** (skill step 5.6): a funded segment needs 5-10 independent data points from a consistent group. You have:

| # | Data point | Independent? |
|---|---|---|
| 1 | One lost deal where the prospect mentioned air-gap need | yes |
| 2 | One conference-booth conversation with Ravenhollow Data | yes |

**2 data points.** Below the floor by a factor of 2.5-5x. This is the same shape as the reference case this skill ships with — "regulated platform teams," 3 lost deals, kept as an unfunded hypothesis even at 3. You're starting one point lower than the example the skill uses to illustrate "don't fund this yet."

"Everyone on the team is convinced it's real" is not a data point — it's the exact failure mode the evidence floor exists to catch. Conviction with n=2 is how a segment map fails the gate ("a bare round number," "the pain is assumed rather than quoted") while feeling completely justified in the room.

## Segment-validity check (does this even survive as a segment, evidence aside)

| Criterion | Verdict | Note |
|---|---|---|
| Measurable | **Weak, structurally** | Air-gapped means no telemetry, by definition — this segment can never move past "estimated" or "inferred" confidence. You will never get a "measured" tier here no matter how much evidence you collect. Build the map knowing that ceiling exists. |
| Substantial | **Unknown, flag: single-account risk** | Two data points could mean "a market" or could mean "one company (Ravenhollow) plus one lost deal that happened to share a trait with it." The reference material calls this out by name: "a segment of nine companies" is the standard failure here. You don't yet know if this is a segment or a whale. |
| Accessible | **Plausible, unconfirmed** | A conference booth is one instance of a channel, not a demonstrated venue. Defense-sector/GovCon events likely exist as a real channel — but that's an assumption to confirm, not yet a finding. |
| Differentiable | **Probably yes** | Air-gapped deployment plausibly needs a genuinely different artefact: offline installer, no phone-home telemetry, egress-free update path, on-prem licensing. If confirmed, this is the strongest part of the case. |
| Actionable | **Yes, and that's the risk** | The team already wants to act. Wanting to act is not evidence that acting is warranted — that's precisely the gap this memo exists to close. |

## Scoring against the seven criteria

| Criterion | Score | Basis |
|---|---|---|
| Size | **unscored** | No credible method reaches this niche (SlashData/Stack Overflow/Octoverse-class sources size languages and sectors, not "defense integrators running air-gapped log pipelines" — see `sizing-sources.md`). A rough population figure (e.g., counting defense-industrial-base contractors via SAM.gov or GovWin) is possible later but hasn't been attempted; don't quote a number you can't source. |
| Reachability | **inferred, medium** | One conference booth suggests a channel exists (GovCon/classified-systems events); unconfirmed as a repeatable venue. |
| Fit | **inferred, low confidence** | The pain (air-gap support) is *stated* by one lost prospect and *implied* by one conversation — quoted, not assumed, which is a point in its favor, but n=2. |
| Value | **unscored** | No deal size, no ARR estimate from either data point is mentioned. Can't weight this without it. |
| Effort | **known: ~4 engineer-months** | This is the one number you actually have. It's real and it's not small — roughly a full quarter of one engineer's output, or a meaningful slice of a team's capacity. |
| Competitive position | **unscored** | No stated incumbent, no switching trigger identified. |
| Compounding | **inferred, plausible** | If real, a named air-gapped reference is high-leverage (this exact niche trusts almost nothing except a peer who already runs it) — but "if real" is the open question, not a settled input. |

Five of seven criteria are unscored or low-confidence-inferred. Effort — the one hard number — is real and non-trivial. Ranking by value-per-effort (step 5.3) isn't possible yet because the numerator is missing, not because the denominator is small.

## Where this goes in the quarterly map

```
## Hypotheses
Air-gapped defence integrators (deployment-mode × regulated-sector segment).
2 data points (1 lost deal, 1 conference conversation) — below the 5-10 floor.
Structurally capped at "estimated" confidence: air-gapped means no telemetry,
ever. Single-account risk: unconfirmed whether this is a market or one company
(Ravenhollow Data) plus one deal that happened to share a trait.
Test: see below. Drop the segment if the test comes back as "one account,"
not "a reachable market."

## Anti-segment (until the test resolves it)
Air-gapped defence integrators are NOT funded this horizon. Reason: the
artefact (~4 engineer-months for a new SDK: offline install, no phone-home
telemetry, egress-free updates, likely a security/ATO review path) is a
real quarter of capacity, and the case for it currently rests on 2 data
points. Revisit immediately if the cheap test below returns 5+ more
independent, consistent data points.
```

## The cheap test (days, not a quarter — per `sizing-sources.md`)

Run this before committing engineer-months, not instead of eventually building the SDK:

1. **Pull CRM closed-lost reasons** for the trailing 12-24 months, filtered on keywords: "air-gap," "air gap," "disconnected," "classified network," "no internet access," "SCIF," "IL4/IL5," "offline install." Free, takes an hour, and is the single highest-value step here — it turns "one deal I remember" into an actual count.
2. **Go back to the lost deal and the Ravenhollow contact** and ask directly: how many other integrators do they know who hit the same wall? Referrals from people who already named the pain are the cheapest way to reach 5-10 points fast.
3. **Five structured conversations** with people who match the profile (defense/GovCon systems integrators, air-gapped or disconnected deployments), sourced from #1 and #2. Ask the decision-unit questions from `decision-unit.md`: who blocked the deal, what would have unblocked them, who would have to sign.
4. **One landing page or one-pager** written in the segment's own words ("air-gapped," not "on-prem" — the vocabulary difference is itself a signal of fit), pointed at whatever channel surfaced the conference contact, measured on qualified inbound replies, not traffic.

**Write the failure condition now, before running it** (the skill is explicit that a real test can fail): if these four steps surface fewer than 5 total independent, consistent data points, or if 4 of the 5 conversations turn out to be describing Ravenhollow's own referral network rather than an independent set of companies, this is one account, not a segment — drop it from the plan and treat Ravenhollow as a single named-account deal, not an SDK bet.

## Recommendation

- **Don't put the SDK in next quarter's funded plan.** The evidence doesn't support a 4-engineer-month commitment yet, independent of whether the team's instinct turns out right.
- **Do fund the test above** — it costs a few days of one person's time, not four engineer-months, and directly produces the missing size/value/fit numbers.
- **Set a checkpoint**, not an open-ended "keep watching": revisit funding this segment the moment the test returns 5+ independent data points, or drop it explicitly and say why (so it doesn't quietly get re-proposed next quarter with the same two data points).
- If the funded driver behind this SDK is sales enablement and Ravenhollow is a live, sizable deal on its own — that's a legitimate reason to fund it as a **named-account bet**, not a segment. Say so explicitly in the plan if that's the actual justification; don't dress up a whale as a market, because the artefact list and the review cadence are different for each.

## Quality-gate self-check for this piece of the map

- Evidence floor stated and applied: ✅ (2 of 5-10, hypothesis, not funded)
- Size/method/date/confidence stated where claimed, "unscored" where not: ✅
- Decision unit not yet named — genuinely unconfirmed, flagged as open rather than guessed: this row is **incomplete by design** until the test runs.
- Anti-segment reasoning explicit and reversible (self-host-style trigger: "revisit when test returns 5+ points"): ✅
- No number presented without a stated source, method, or confidence tier: ✅