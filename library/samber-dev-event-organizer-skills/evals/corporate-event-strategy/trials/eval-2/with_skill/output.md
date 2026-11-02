# Meridock roadshow: what to tell the CFO, and how to avoid a repeat

I followed the `corporate-event-strategy` skill and its two reference files. The skill is built as a one-question-at-a-time interview, and you asked for the finished answer, so I filled the gaps with labeled assumptions. Correct any that are wrong. Sections 3 and 4 depend on them most.

## 1. The honest position

- ℹ️ **Buyer and user are separated.** Engineers evaluate, and a CISO or procurement signs 6 to 9 months later. Any join between "someone attended" and "an opportunity exists" links two different people. It measures **influence, not attribution**. Use the word "influence" in front of the CFO.
- ⚠️ **No goal was written before the roadshow.** "Be visible to the dev community" is an ecosystem-goodwill goal with no number attached. The skill calls a goal set after the fact "a description of what happened." You can report what happened, but you can't say the roadshow met a target, because it had none.
- ⚠️ **The 14 opportunities and $2.1M are touched-account pipeline.** They are not sourced pipeline and not revenue.
- ⏳ **The cycle isn't finished.** Spring events plus 6 to 9 months puts the first real read between now (2026-10-10) and roughly spring 2027.

## 2. What you can tell the CFO

**Facts (safe to state)**

| Item | Value |
|---|---|
| All-in cost | $410k |
| Cities | 5 |
| Attendees | ~1,100 |
| Cost per attendee | ~$373 |
| Opportunities on accounts with someone at a stop | 14 |
| Pipeline value of those opportunities | $2.1M |
| Cost per touched opportunity | ~$29k |

**The break-even number.** $410k divided by $2.1M is 19.5%. For the roadshow to cover its cost in revenue, about one in five dollars of that pipeline would have to close, and only if all of it counts as event-influenced. That is a bar the CFO can judge. The skill says all thresholds here are self-set, because no industry figure transfers between companies. Compare it with Meridock's own enterprise win rate, which you have and I don't.

**Suggested script**

> "We didn't set a goal beforehand, so I can't tell you it hit one. Here's what's measured: $410k, 1,100 engineers, 5 cities. 14 open opportunities worth $2.1M are on accounts that had someone at a stop. That is influence, not sourced pipeline, because engineers evaluate and a CISO signs 6 to 9 months later. I'm splitting the 14 by whether they were created before or after the stop, and I'm comparing them with similar accounts that sent nobody. I'll report that by [date]. Closed revenue can't be read until [Q1–Q2 2027]. For next year the goal, owner, source system and read date are written down before registration opens."

**Do not say:**
- "ROI" or "returned $2.1M".
- That the roadshow "sourced" the pipeline.
- Any attendee-count claim as an outcome. The skill deletes attendance from the goal menu.
- Any figure on visibility or brand lift. Nothing was measured.

## 3. Retrofit this week (cheap, and it makes the answer defensible)

Run these on the existing 14 opportunities. Fix the rules before anyone looks at the results, because a rule chosen after the numbers are visible is a negotiation.

1. **Created before or after the stop.** Split the 14 into: opportunity already open before the account attended, and opportunity created after. Only the second group is plausibly new pipeline. The first group is at most acceleration.
2. **Who attended.** Was the person an engineer, a security lead, or someone in a buying role? One engineer at an account tells you less than a security lead plus an engineer.
3. **Comparison set.** Pick similar accounts (size, segment, region) that had no attendee. Compare opportunity creation rates over the same window.
4. **Interim read now, final read at closing.** Report stage movement on the 14 now. Report closed-won once the cycle has run.

In the brief, state which counterfactual case applies:
- **Comparison set used.** It still isn't proof.
- **Before-and-after only.** The roadshow is one of several plausible causes.
- **Influence, not attribution.** This applies in either case, because buyer and user are separated.

⚠️ **One check before sales uses attendee lists further.** Sales already matched attendees to accounts, so the list sits in sales systems. Confirm with whoever holds privacy obligations that the registration notice covered that use. A list collected under the wrong notice can't be un-collected, and the fix is usually to stop using it.

## 4. Next year: goal, funding, measurement

### Assumptions to confirm

| Assumption | Why it matters |
|---|---|
| The roadshow becomes an annual program (Q7: compounding). | It promotes the durable, blended goals. |
| Sales has some account-level match to attendees, since it found the 14. | A pipeline goal is available. |
| The room is mostly engineers at accounts that haven't bought. | This supports pipeline over adoption alone. |
| The CFO review is a hard date. | It favors goals readable inside the cycle. |
| Someone can hold a standing measurement job through the quarter after each event. | The blend needs a reconciliation owner. |

If the last assumption fails, drop to Candidate B.

### Candidate goal mixes

- **A. Blended influence-and-evaluation (recommended).**
  - **Pipeline influence:** opportunities created after the stop, on accounts with an attendee in the agreed role.
  - **Evaluation activity:** attending accounts that start a trial or proof of concept, against a matched non-attending set.
  - **Why:** a 6 to 9 month cycle means pipeline alone can't be read inside one fiscal year. Evaluation activity is the leading indicator that the engineer-evaluates, CISO-signs path is working, and it gives you a second story if a quarter produces no opportunities.
  - **Cost:** the slowest read, and a reconciliation owner.
- **B. Pipeline-first, stated as influence.**
  - Cheaper to instrument and fastest to read, but it is the first goal to fail in a weak quarter. If the cycle is 6 to 9 months, the first read lands after the CFO's next review.
  - Use it only if the answer to the standing-owner assumption is no.

**Rejected rungs, so the goal doesn't widen later:**
- **Ecosystem-goodwill only.** Deleted, not demoted. Once sales is a funder, a goal with no number is the retreat the team takes when instrumentation runs late.
- **Attendance as a goal.** Deleted. It is the number reached for when the real one is late.
- **Adoption-first on its own.** For a room of people who haven't bought, the metric would mostly measure existing users.

### Budget ownership

- **Recommended:** marketing and sales co-funded, but only once the attendance-to-opportunity join demonstrably exists. Sales won't keep funding a number it can't see.
- **Coupling check:** sales is buying the pipeline half. It gets a say on guest-list weighting and no say on content. The skill warns that weighting toward accounts in an active cycle changes what the room is and what you can honestly claim.
- **Alternative:** a multi-function committee (marketing, sales, product) with a named executive sponsor, if product also wants the evaluation data. It is more durable and costs more effort. A committee without a sponsor has every veto and none of the protection.
- **Not acceptable:** funding from whichever pot has room. Name one line owner today.

### Measurement commitment (write before registration opens)

All thresholds and windows are self-set. None comes from an industry benchmark.

| | Pipeline influence | Evaluation activity |
|---|---|---|
| **Metric** | Opportunities created within [N] days after the stop, on accounts with at least one attendee in [agreed roles], under a rule fixed in advance | Share of attending accounts that start a trial or proof of concept within [window], against the matched non-attending set |
| **Owner** | Named person in sales ops | Named person in product or developer relations |
| **Source system** | CRM, with an attendance-to-account join confirmed to exist | Product telemetry that identifies accounts |
| **Read date** | Interim at +90 days, final at +9 months, both before the planning cycle that renews the line | Interim at +90 days |

The skill treats a goal missing any of the four fields as an intention, not a goal. If "source system" is "a spreadsheet someone will build," that goal isn't available yet.

Also name one **reconciliation owner**. Without one, the blend produces two numbers that disagree and an argument nobody wins.

Pick two or three observables and write down what each would change:
- **Goal-to-number latency:** the gap between the event and when the number is readable. If it is longer than the funding cycle, the goal can't defend its line.
- **Funder attrition:** how many of the functions that signed the line still fund it next cycle.
- **Goal drift:** whether the debrief scores the edition against the goal set here.

## 5. Reviews to send out before the invitation goes live

| Review | Owner | Status |
|---|---|---|
| Company name on a room it doesn't fully control (terms, how the code of conduct binds staff, insurance) | Legal | ⏳ To send |
| Attendee list moving into sales systems (lawful basis, registration notice, retention, reuse limits) | Whoever holds privacy obligations | ⚠️ Check for spring now, fix before next registration |
| Customers and prospects hosted as guests (your anti-bribery and gifting rules, and the guest's employer's, which are often stricter; public-sector and regulated guests are the common case) | Compliance | ⏳ To send. Ask before inviting target accounts that may not be allowed to accept |

Legal and privacy specifics come from your own counsel. The skill names no jurisdiction or retention period.

## 6. Re-run this strategy when

- The goal changes.
- A funder joins or leaves.
- The product changes so that the developer who evaluates now also signs.
- The invite list stops matching the goal.

## 7. Open questions

1. Is the roadshow an annual program, and is there a hard date for the CFO's next review?
2. What does the attendance-to-CRM match actually cover: account only, or person and role?
3. Of the 14 opportunities, how many were open before the stop?
4. Who in sales or marketing could hold the standing measurement job?

Answers to 1 and 4 decide between Candidates A and B.