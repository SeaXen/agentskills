## Bottom line

Ship the board evidence from the event you've already paid for, not from the one your CEO wants. Qualify May now, fund it from reserve. Put October's workshop on hold — not killed, gated — because as your CEO has framed it, it can't produce a single data point before 14 March and it can plausibly eat your whole remaining budget in one signature. Here's the plan, in the skill's own shape: one primary objective, three portfolios with one clear winner, a per-event plan for each of your three events, and the artifact you actually put in front of the board.

**Assumption flagged up front:** Marlstone is self-serve, card-payment, $59/month — no enterprise motion mentioned. Everything below treats that as true. If there's also a sales-assisted tier, say so; it shifts Pipeline back onto the table and changes the metric, not the event picks.

---

## 1) Fix the objective

Self-serve, card-paid products behave like consumer marketing (step 1): success is measurable in-product, and the follow-up is a product invitation, not a sales sequence. That leaves two realistic mandates — Awareness or Adoption. Board survival needs a number that reads as revenue-adjacent, not a search-traffic lift nobody in the room can sanity-check.

✅ **Primary objective: Adoption.** Metric: signups on the event's own promo code, cohort still active at 30/60/90 days. Awareness signals (branded search, direct traffic) get captured as supporting evidence, never claimed as the headline.

One objective, one metric, one owner — name that owner today. Two objectives on one budget with one person watching them is how you end up with excuses instead of a number in March.

---

## 2) Three portfolios — pick one

**Portfolio A — CEO's plan, as pitched.** February (sunk) + October flagship tier + workshop add-on, funded by cutting May.
❌ Not recommended. Three problems, all structural, not taste:
- **Timing kills it outright.** October hasn't happened by 14 March. It produces zero data for the one deadline that matters. You'd be walking into the board meeting with exactly the "great buzz, no threshold" failure mode the ROI model warns about — for the *other* event, while the one that could have saved you sits unexecuted.
- **Budget risk.** Published anchors: a DjangoCon-style hands-on workshop add-on runs ~$12k — more than an entire mid tier; a PyCon-style track-lead sponsorship runs $45–75k, more than your whole remaining budget on its own. A "splashy" workshop at a "big" conference is very plausibly a $30–45k combined ask before travel, booth build, or staff time. That's your entire $45k, with nothing left for May and nothing in reserve.
- **Effort ceiling.** A workshop costs a quarter of prep and takes your two best engineers off the floor for its whole slot (step 6). You have two engineers, full stop, and they're already needed for February. Committing them to a quarter of workshop prep on top of a committed event is over capacity before May even enters the conversation.

**Portfolio B — Prove it first.** February (execute + measure) + May (qualify, commit if it clears the bar) + full reserve. October deferred, no decision forced.
Safe, fits the deadline, fits the two-engineer ceiling, fits the budget. Weakness: doesn't answer your CEO at all, and "deferred" with no reopening criteria reads as a stall, not a decision — the skill is explicit that a maybe isn't an acceptable output.

**Portfolio C — Prove it first, with a gate on October.**
✅ **Recommended.** February (execute + measure) + May (qualify and commit) + reserve, *plus* a written, evidence-gated threshold that reopens October once Feb/May data exists — decided in time for October's own contract deadline (large-conference contracts close roughly a quarter out, so you need that call by ~July). This is the only shape that gives the board real numbers on 14 March *and* gives your CEO an actual answer instead of a no.

---

## 3) February — the event that saves the meeting

This is already bought, so step 2's go/no-go doesn't apply — but you still need the audience evidence, because it decides your qualification bar and gives you something better to tell the board than attendance numbers. Send the standard evidence request today if you haven't (role mix, seniority, company size, last edition's post-event report, what contact data the package actually includes). A mid-size platform conference is a good structural signal on its face — platform/SRE audiences are close to feature-flagging's actual ICP, similar to the "strong" worked example in the scorecard (62% engineers, workshop-eligible, third edition).

**Confirm the three prospectus clauses now**, even on a signed contract, because they determine what you can even do on-site:
- What contact data the sponsor tier includes — smallest tier almost never includes badge-scan data, so plan on opt-in capture instead (QR to a landing page, a small giveaway tied to a real conversation, not a scan-for-swag trade).
- Whether a stage slot exists — at the smallest tier, it won't. Workshop is off the table here anyway; don't spend energy negotiating for one.
- Which surfaces are sold separately — check for a cheap, high-traffic add-on (lanyard, coffee break, wi-fi) if anything's still unsold; skip if nothing fits the remaining budget.

**Activation — three options, one clear pick:**

| Option | Fit |
|---|---|
| ✅ Help-desk booth, two engineers, "debug a stranger's pipeline" posture | Matches the smallest tier (no stage/workshop was ever bought), matches the near-deadline default (step 6), matches your 2-person ceiling. |
| Booth + small side dinner | Only worth it if you already have ~20 real names in the CRM from this ecosystem. If you don't, skip — a side event you have to build a guest list for from scratch this week isn't worth the evening it costs. |
| Logo-only, skip activation | Cheapest, but produces no conversations and nothing to show the board. Don't. |

**Feb one-pager (fill in the brackets as you execute):**

```
# [Platform conference] Feb 2026 — sponsorship one-pager

Objective: Adoption · Owner: [you] · Contract: already signed

## Package
Tier: smallest / no stage / no confirmed contact data — confirm via evidence request
Activation: help-desk booth, 2 engineers

## Tracking
Event URL: marlstone.io/[event-slug]  ·  Promo code: [EVENTCODE]
Baseline captured: [branded search / direct signups, 1-4 weeks pre-event]
Qualification bar: has an active flag/release-process pain, can self-serve without
procurement sign-off, agrees to a named next step (e.g. "starting trial this week")

## Threshold
Fully loaded cost: fee (sunk) + travel + booth build + staff time (2 × days × loaded rate)
Target CPQC: derive from current blended CAC ÷ trial-to-paid rate — pull this number
from growth/finance before the event, not after
Minimum conversations: set once fully loaded cost is known

## Result (post-event, within 2 weeks)
Conversations: [ ]  ·  CPQC: [ ]  ·  Early signups on event code: [ ]  ·  7/14-day activation: [ ]
```

Run the post-event review within two weeks of the conference — that lands in late February, ahead of the board date with margin to build the deck. Route conversations: case-study material → marketing, feature feedback → product, bugs → engineering, buyer-side conversations → sales (should be rare at this ICP). Most of what a booth produces for a self-serve product isn't a sales lead — don't force it into a pipeline number that won't hold up.

Realistically, a late-Feb event won't have full 30-day activation data by 14 March — that's fine. CPQC and raw qualified-conversation count *will* exist by then, and that's already a real number, which is more than the board has ever gotten from this budget line before.

---

## 4) May DevOps day — qualify it, then fund it from reserve

Don't commit yet — run the scorecard first (step 2), but the shape is favorable on priors: a regional DevOps audience is close to as good an ICP match as this product gets (feature flags are DevOps/release-engineering tooling, and DevOps practitioners are exactly the people who can self-serve on a card without procurement). Regional spread is cheap per event, low travel overhead, and reaches developers who never fly to the big conference — which is the population your $59/month plan actually converts.

Send the evidence request this week (attendee role/seniority breakdown, prior-edition report, package sheet, contract deadline). If it clears — decent role-mix actuals, no red flags on the walk-away list (no unverifiable demographics, not a first-time organizer overselling sponsor benefits) — commit out of reserve. Activation: booth again, same reasoning as February; a two-engineer team can't staff a workshop at two events in one quarter.

---

## 5) October — the gate, not the kill

Tell your CEO this directly, because "not now" without a reopening condition just sounds like no: **October is not decided, it's gated on data you'll have by early summer.** Concretely:

- Trigger to reopen: February's and May's CPQC and conversation counts, reviewed together once May's data lands.
- What it needs to clear before you sign anything: (a) real audience evidence for *that specific* October conference — role mix, decision access, sponsor density, same request you're sending for May, not the conference's reputation; (b) a workshop curriculum that already exists, because that's what collapses workshop prep from a quarter to a week and is the only condition under which a workshop becomes efficient rather than a staffing sinkhole; (c) budget headroom that isn't already spent on Feb/May overruns.
- Decision deadline: large-conference contracts close roughly a quarter out, so you need a signed yes/no by **~July** for an October event. That gives you Feb's full result and most of May's to decide with, which is the entire point of sequencing it this way.
- If the CEO wants *something* at that October event even if the full workshop doesn't clear the gate: a booth-only presence at a lower tier is a fallback that costs a fraction of the flagship ask and keeps Marlstone visible in that ecosystem without breaking the effort ceiling or the reserve.

Log it now, in writing, as declined-for-this-cycle with the reason — that's what stops it from getting re-bought in July on enthusiasm alone with no more evidence than it has today.

---

## 6) Budget

| Line | Amount | Note |
|---|---|---|
| February incidentals (travel, staff time, booth build, swag) | draws from the $45k | fee already sunk outside this pool — confirm this split with finance |
| May (if scorecard clears) | remaining after Feb, sized to a booth-level tier | anchor from published ladders: booth-inclusive tiers at community/regional events commonly land well under $10k all-in — verify against May's actual prospectus |
| Reserve | 15–25% of $45k = **$6,750–$11,250** | untouched until the October gate resolves, or a better-fit event surfaces mid-year |
| October | $0 committed now | reopens only against the gate in §5 |

---

## 7) What actually goes on the board slide, 14 March

Not "great buzz." This:

1. February: fully loaded cost, qualified-conversation count, CPQC, whatever early signup/activation signal exists at that point — the first real number this budget line has ever produced.
2. May: qualification scorecard result and the commit decision, with the threshold set *before* the event (proves discipline, not just spend).
3. Reserve: the untouched $6,750–$11,250 and the release condition — this is itself evidence the budget isn't being burned reactively.
4. October: the gate, written down — objective criteria and a July decision date, not a maybe.

That's four concrete lines, one of them a real measured result. It's a stronger case for keeping the budget than a workshop that, on 14 March, would still be seven months from happening.