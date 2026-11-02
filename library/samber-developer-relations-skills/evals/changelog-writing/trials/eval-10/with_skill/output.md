# The business case for a 0.5 FTE release-communication writer

Before the pitch: two corrections to the numbers you're remembering, because a CFO will fact-check anything you cite, and both half-remembered claims point somewhere different than "retention lift."

**There is no published, causal number for retention or upgrade-rate lift from good release notes.** I checked this specifically against the sourcing this skill maintains, because it flags exactly this claim as one to never make: *"a changelog drove adoption, retention, expansion or revenue"* is explicitly listed as unmeasured. Anyone citing a specific percentage lift is citing something unverifiable. Don't build the pitch on that number — build it on the three things that *are* documented below, and propose to measure the rest yourselves.

**The study you're thinking of is Google Play, not the App Store, and it's correlational.** Yang, Hassan, Zou and Hassan, *Empirical Software Engineering* 27:55 (2022) — 69,851 releases, 67.7M reviews, 2,232 top free Google Play apps. Finding: longer release notes and more frequent updates both correlate with higher average ratings. The paper itself flags the confound: release frequency and app maturity move with both variables, so this is not evidence that writing longer notes *causes* better ratings — cite it as "the one published outcome study in this space," not as proof.

**Linear's numbers aren't retention numbers either.** Karri Saarinen (Linear co-founder) has described the payoff as mostly non-user-facing — recruiting, investor confidence, early-adopter trust — and it's a first-party, unquantified claim, not a measured study. Useful as "here's what a company known for this says they got," not as a number you can multiply by anything.

Use both as *documented industry practice*, not as ROI proof. A CFO who catches you overstating a source will discount everything else in the pitch, including the parts that are solid.

---

## What actually supports the ask

Three lines of evidence hold up, and they're enough on their own.

### 1. This is currently an unbudgeted tax on your most expensive people

Drafting one release-note document takes an experienced developer up to 8 hours (Moreno et al., cited in Daneshyan et al., FSE 2025). That's not writing time in the abstract — it's a senior engineer pulled off roadmap work, doing a task they're not trained for and actively dislike. A Microsoft developer advocate's line on this is blunt and representative of the sentiment in the field: *"we hate creating release notes when it's our turn to ship"* (Jasmine Greenaway, opensource.microsoft.com, 2018).

Run your own numbers through this:

| Input | Placeholder — replace with your data | Formula |
|---|---|---|
| Tagged releases per year | 24 (biweekly) | A |
| Hours per release, current ad hoc process | 8 (upper bound, cited above) | B |
| Fully loaded senior-engineer hourly cost | $120/hr (~$250k/yr fully loaded ÷ 2,080 hrs) | C |
| **Annual cost of the status quo** | | **A × B × C = $23,040/yr** |

At most companies this direct wage-cost number alone won't clear the bar for a $45–65k role (illustrative range for 0.5 FTE mid-level technical writer — get your actual band from People/Finance, don't use mine). That's the honest read, and it's worth saying to the CFO up front rather than having them find it: **the case isn't "this one line item pays for itself," it's the portfolio below.** What that $23k figure understates badly is the second-order cost: it's not that the engineer's time is worth $120/hr, it's that it's roadmap time, and roadmap time is the thing the company is actually constrained on. Diverting it to a task a specialist does faster and better is a bad trade twice over.

### 2. Quality on this task compounds with repetition — which a rotating engineer never gets

A Google API technical writer who ran an agent on this exact task tracked review-comment counts per release: 15–20 comments per release fell to 3–5 after roughly a dozen iterations (Tom Johnson, idratherbewriting.com, 2025–2026). That's a convergence curve, not a one-time skill. The same source notes engineers routinely under-report their own changes to whoever's writing this up — the diff catches things self-reports miss.

The structural problem with the current setup: if a different engineer writes release notes every cycle (because it rotates, or because whoever shipped the feature writes their own entry), nobody ever climbs that curve. The org pays the 8-hour tax and the 15-20-comment review overhead *every single release, indefinitely*, because the learning never accumulates in one person. A dedicated 0.5 FTE owner is the only way to actually bank that convergence.

Corroborating data on how bad the current baseline likely is: human-written release notes, on average, cover only about 31% of the commits in a release (vs. 81% for a well-engineered generator+editorial pipeline), and well-formed notes list only 6–26% of the issues a release actually addressed (Abebe, Ali and Hassan; Daneshyan et al., FSE 2025). Some of that gap is deliberate concision. Some of it is silent gaps nobody chose — a breaking change with no entry, discovered in production.

### 3. The downside case is asymmetric and it's the one a CFO should actually weigh

This is the strongest argument and doesn't need a citation — it's your own risk exposure:

- An unannounced breaking change surfaces as a support spike or an outage, not as a line item — it's cheaper to prevent than to triage after the fact.
- If you sell to enterprise, a missed security advisory or unclear upgrade path is a compliance and trust problem, not a documentation nitpick — some of those notes are effectively unretractable once a customer has acted (or failed to act) on them.
- Every release without a dedicated owner is one more release where "does this cost me work?" goes unanswered for someone who then finds out the hard way.

None of this needs to be dressed up as a retention multiplier. "We are currently one missed changelog entry away from a support spike or a compliance conversation, and the person catching that today is whoever happened to ship the feature" is a risk statement a CFO understands natively.

---

## The pitch, assembled

**Ask:** 0.5 FTE technical writer, owning release communication (changelog, release notes, breaking-change and deprecation entries) across [your surfaces].

**Why now, why this shape:**
1. The task currently costs senior engineering time at a rate ([run the formula above with your real numbers]) that's cheap to state and expensive to actually pay in roadmap terms — engineers doing a task they're bad at and dislike, instead of the task they were hired for.
2. Quality on this task only improves with a consistent owner; a rotating cast of engineers resets the learning curve every release, and the industry data on how much ad hoc notes miss (31% commit coverage) says that gap is real, not theoretical.
3. The downside of getting this wrong — an unannounced breaking change, a missed security advisory — costs more than 0.5 FTE, and today nobody owns catching it.
4. This is documented, not speculative, industry practice: companies with strong DevRel/technical-writing reputations for this (Linear, Stripe, Slack) treat it as a standing function, not a per-release scramble — cited here as precedent, not as proof of a specific return.

**What I'm explicitly not claiming:** a retention lift, an upgrade-rate lift, or a revenue number. Nobody in the field has published one, and I'd rather you catch me not making that number up than have a board member catch it later.

**What I will commit to measuring**, starting the quarter this role is funded, so the next budget conversation has real data instead of citations:
- Support/issue volume tagged to each release (cheap — you already triage this; a spike right after ship usually flags an under-communicated change).
- Click-through rate from breaking-change entries to migration guides (an hour to instrument, tells you directly whether the entry did its job).
- Time-to-upgrade: version distribution in use at 7/30/90 days post-release, especially for breaking releases.
- Review-comment count per release, if notes go through review — expect this to fall as the role builds the convergence curve described above.

Two quarters of that data is a stronger renewal case than any number I could hand you today, including the ones you half-remembered.

---

## Sources cited above, for your own fact-check

- Moreno et al., cited in Daneshyan et al., "SmartNote," FSE 2025 (DOI 10.1145/3729345) — 8-hour drafting cost; 31% vs. 81% commit coverage; ~90% of projects have no commit convention.
- Abebe, Ali and Hassan — well-formed release notes cover 6–26% of addressed issues.
- Yang, Hassan, Zou and Hassan, *Empirical Software Engineering* 27:55 (2022) — Google Play ratings correlation, 69,851 releases / 67.7M reviews / 2,232 apps.
- Karri Saarinen (Linear), Medium, 2020 — recruiting/investor/early-adopter framing, first-party and unquantified.
- Jasmine Greenaway (Microsoft), opensource.microsoft.com, 2018-09-06.
- Tom Johnson, idratherbewriting.com, 2025-02-17 and 2026-05-04 — review-comment convergence; engineers under-reporting changes.