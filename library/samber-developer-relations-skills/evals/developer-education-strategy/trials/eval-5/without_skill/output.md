# Halcyon Learn — Measurement Plan for Q[next]

## The real problem isn't measurement. It's that no metric ties to money.

640 enrolled, 4.6/5, 82% pass rate — these are **quality-of-content** signals, not **business-impact** signals. They tell you people liked it. They tell the CFO nothing about revenue, cost, or retention. Anonymous access was the right call to protect signups — but it means today you have zero way to join a learner to anything downstream. Fix the join, not the vanity metrics.

---

## Step 1 — Pick ONE primary business metric before touching any tooling

Chasing every possible benefit proves none of them convincingly. Force a choice. Pick the hypothesis the CFO actually cares about, plus at most two secondary ones.

| Hypothesis: Halcyon Learn exists to... | Primary lagging KPI | Who it applies to |
|---|---|---|
| Generate top-of-funnel pipeline | Marketing-sourced pipeline $, learner→opportunity conversion rate | Prospects |
| Speed up onboarding / time-to-value | Time to first key product action, feature adoption depth at 90 days | New customers |
| Drive expansion / upsell | Upsell attach rate, expansion ARR among learners vs non-learners | Existing customers |
| Reduce churn | Churn rate, learners vs matched non-learners | Existing customers |
| Deflect support cost | Ticket volume/cost for topics the course covers | Existing customers |

🎯 **Pick one now.** Everything below assumes you have.

---

## Step 2 — Name the root cause, out loud, to the CFO

"We removed login to protect signups. That decision also removed our ability to attribute business outcomes to this program — those two things are the same tradeoff, not two separate problems." This reframes the QBR miss as a known, fixable architecture gap, not a failure of the program itself.

---

## Step 3 — Fix instrumentation without adding a login wall

Keep enrollment fully open. Add tracking in three layers, each one preserving the current friction-free entry:

**Layer 1 — Anonymous product analytics (no identity, ship this immediately)**

| Event | Properties | Trigger |
|---|---|---|
| `course_enrolled` | referrer, utm_source/medium/campaign, anon_id | Enrollment |
| `module_started` / `module_completed` | module_number, module_name, anon_id | Per module |
| `quiz_attempted` / `quiz_passed` | module_number, score, attempt_number | Quiz submit |
| `course_completed` | total_time, modules_completed | Final module done |

This alone gives you a real completion funnel and drop-off points per module — useful, but still not tied to a dollar.

**Layer 2 — One optional, incentivized identity ask, placed AFTER value is delivered**

Don't gate entry. Gate the certificate/badge instead: "Get your completion certificate" → email required only at that step, only for people who already finished. This is the `identify()` call — it merges the anonymous journey (Layer 1) into a known person, for exactly your highest-intent segment, with zero cost to top-of-funnel enrollment.

At that same moment, ask two self-reported questions inline:
- "Are you a current customer, prospect, partner, or other?"
- "What will you do differently on [platform] because of this course?" (free text)

This is deliberate self-reported attribution — it catches intent before any behavioral data exists, and it's the only channel that will ever see word-of-mouth or internal-champion effects.

**Layer 3 — Join identified learners to systems of record**

Match captured emails against CRM and product DB (exact match, or domain match for B2B accounts). Tag each identified learner: existing customer + account/ARR tier, or open pipeline contact, or neither. Route them into the KPI from Step 1.

⚠️ Anonymity guardrail: never smuggle an identified email back into anonymous analytics events, and never force-match on partial/fuzzy identity. If a match is ambiguous, leave it unmatched — a smaller clean sample beats a larger corrupted one.

---

## Step 4 — Measure the identified segment (starts next cohort, imperfect but real)

For learners who completed the certificate flow:
- Customers: compare product usage (feature adoption depth, key-action frequency), support ticket volume, and renewal/expansion events in the 90 days after completion vs. the 90 days before.
- Prospects: compare CRM stage movement, deal velocity, and win rate against a matched cohort of similar accounts that didn't take the course.

⚠️ Say this explicitly in the readout: certificate-completers are a self-selected, most-engaged slice of the 640, not a random sample. Report results as "lift among engaged completers," never as "proven program-wide ROI."

---

## Step 5 — Build one real causal test (this is what makes the CFO conversation defensible)

The course itself may be anonymous, but the **promotion channel isn't** — you already know who you emailed, which accounts saw the in-app banner, which docs page linked to it. Use that.

For the next module launch or next promotional push: split your target accounts/segment into an **invited-now** group and an **invited-next-month** group (staggered rollout, nobody permanently excluded). Track the Step 1 KPI in both groups over the same window.

- This is an incrementality/holdout test — the gold standard for "did this cause the lift," independent of whether any individual logs in.
- Expect product-usage or ticket-volume signals to reach significance in weeks; expansion revenue or churn will likely need 1–2 quarters at your current volume. Use the faster-moving metrics as leading proxies for the slower revenue metric in interim reporting.

---

## Step 6 — Salvage a first-pass read on the existing 640, this quarter

You can't retrofit identity onto data that was never captured, but you have two cheap options:

1. **Retroactive self-reported pass**: send a short optional survey to whatever list you used to promote the course (email blast, community post, docs banner clicks) — "Did you complete Halcyon Learn? Has it changed how you use [platform]? Are you a customer?" Low response rate, but the only signal available for this cohort.
2. **Directional cohort correlation**: overlay the 6-month enrollment/module-launch curve against aggregate account-level usage or pipeline curves for the promoted segment vs. an unpromoted comparable segment. Present as directional only — correlational, not causal — and say so plainly.

Frame this to the CFO as: "Here's the best retroactive read we can get on the first 640 — treat it as a hint, not a verdict. Here's the test already running that will give you a real number next quarter."

---

## Step 7 — Reporting cadence

- **Monthly** — leading indicators: enrollment, completion rate, quiz pass rate, satisfaction. Cheap health check, not a business case.
- **Quarterly** — business-impact readout:

```
# Halcyon Learn — Attribution Readout, Q[x]

## The question
Did Halcyon Learn move [primary KPI from Step 1]?

## Source of truth
[CRM pipeline data / product usage DB — whichever defines the KPI]

## What we can see
| Segment | Sample | Method | Result | Confidence |
|---|---|---|---|---|
| Certificate-completers (identified) | ~N | Matched-cohort comparison | ... | Low–medium (self-selected) |
| Invited vs. held-out (new cohort) | ~N | Staggered-rollout test | ... | Medium–high |
| Original 640 (retroactive) | ~N | Self-reported survey + cohort correlation | ... | Low |

## Gaps
[What we still can't see, and why]

## Recommendation
[Allocation/continuation call, with confidence level attached — never a bare ROI number]
```

---

## One line for the CFO right now

"We optimized for reach and got real proof the content works — 640 enrolled, 4.6/5, 82% pass. We didn't instrument it to prove business return, and that's the gap. Fix ships this quarter: an optional certificate-based identity capture that doesn't touch signup friction, plus a staggered-rollout test on the next module launch that will give you a defensible lift number by [date]."