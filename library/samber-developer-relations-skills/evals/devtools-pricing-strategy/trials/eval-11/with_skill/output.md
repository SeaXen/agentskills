# Northmoor Free Tier — Pricing Memo & Execution Plan

## Verdict before the memo

Two of the three moves in the plan as written break this market's own free-limit rules, and will cost you more in backlash than the $31k/month they're meant to save. One is a plan you should keep, tightened.

| Plan item | Verdict | Why |
|---|---|---|
| Halve every limit | ⚠️ Partially keep — not as a blanket rule | "Halve" doesn't apply to **unlimited branches** — half of infinity is still infinity. That's very likely where the real leak is, not in the bounded numbers. |
| 90-day inactivity **expiry** | ❌ Reject as written | The skill's own free-limit checklist names this exact pattern as the thing not to do: *"No time bomb: no expiry, no 'free tier ends after 90 days of inactivity'... Never delete data as enforcement."* A silent timer with no warning is the single most avoidable trust break in this design. |
| Delete data on dormant projects | ❌ Reject as immediate/silent | Same rule. Deleting user data with no warning and no export path is worse than a price increase — it's the failure mode "retroactive gating" describes, one tier more severe. |

The fix below keeps the cost outcome you want and drops only the mechanism, not the goal.

---

## Inputs

- **Model**: hosted managed Postgres with branching, self-serve. Buyer: individual developer, personal card, no procurement.
- **Value metric already chosen, and it's the right one**: compute-hours, consumption family, already billed on the paid side ($29 entry, metered on compute-hours). This is a hybrid already — capacity/entitlement free allowance (compute-hours, storage, branches, projects, egress, PITR days) sitting on top of the same axis the paid tier meters. Don't touch the metric. The problem is the free-side numbers and their enforcement, not the unit.
- **Cost per unit**: not given beyond the $31k/month aggregate. This memo needs it split by resource (compute, storage, egress, WAL/PITR retention) and by cohort (active last 30 days vs. dormant) before any number below is final — see Phase 0 of the execution plan. Everything below is directionally sound; the exact digits are placeholders for your real metering breakdown.
- **Free alternative's true cost**: self-hosting Postgres with branching-equivalent tooling (manual snapshot/restore scripting, or an OSS branching layer) costs a developer real setup and operator time — this bounds how low you can push the free tier before "just self-host it" beats you outright. Don't need to solve for this now; it's slack, not the constraint.

## Value metric — no change

Compute-hours passes all five tests: moves with value, already counted by every cloud-DB user, forecastable from live usage, hard to game, and correlates with your actual infra cost. Keep it as both the free-tier headline and the paid meter. The redesign below is about which numbers gate and how gating behaves, not about switching units.

## Ladder — free surface only, rest unchanged

The free surface's job stays the same: a real side project, permanently, no card. It just needs fewer numbers a user actually has to think about, and one number (branches) that was never actually bounded.

### New limits

| Limit | Today | "Halve everything" gives | Recommended | Why |
|---|---|---|---|---|
| **Compute-hours/mo** (headline #1, same axis as paid) | 100 | 50 | **50** | Correct to halve — it's the unit paid customers already pay on, so hitting it *is* the upgrade moment. |
| **Storage** (headline #2) | 5 GB | 2.5 GB | **2 GB** | Still fits a real side project; below this, most people are outgrowing free tier anyway. |
| **Branches** | unlimited | unlimited (halving fails) | **10 per project** | The actual fix. Uncapped branches against a multi-day PITR/WAL retention window is an unbounded storage multiplier that a 5→2.5 GB storage cut doesn't touch if branch WAL is metered separately, and does touch invisibly if it isn't. Cap it outright. |
| **PITR window** | 7 days | 3.5 days | **3 days** | Halves WAL retention cost per branch directly — compounds with the branch cap above, since it's retention-days × branch-count that was driving cost, not either number alone. |
| **Projects** | 3 | 1.5 (undefined) | **2** | Don't mechanically halve a headcount-like limit below 2 — it gates the completely normal "main + staging" pattern for an individual. Keep as a light backstop, not a lever. |
| **Egress** | 10 GB | 5 GB | **5 GB** | Fine as proposed. Backstop, not headline. |

Only compute-hours and storage should appear on the pricing page and in the dashboard's live-usage widget — that satisfies "one or two headline numbers" even though six caps technically exist. The rest are set generously enough that a real side project rarely touches them; they exist to stop abuse, not to be a second thing a user has to track.

**Before shipping these exact numbers**: run the cost-by-resource, cost-by-cohort query described in Phase 0 below. If it turns out branches × PITR-days is 70% of the $31k, the branch cap and PITR cut alone may get you most of the way there and you can be less aggressive on compute-hours/storage — don't cut all six on faith when the data will tell you which two matter.

## Free surface — enforcement, not deletion

Checklist requirement: warnings at 70/85/95%, then throttle/queue/pause/bill overage — never delete as enforcement.

**For live, active accounts hitting a cap:**
- 70% of compute-hours: in-app + email warning, live usage graph, upgrade CTA.
- 85%: second warning, projected overage date.
- 95%: final warning.
- 100%: **hard cap** — new queries pause until next billing cycle or upgrade. Hard cap is the correct default for a free/hobby tier per step 5. Data is never touched; upgrading mid-cycle un-pauses immediately.
- Branch/storage/egress caps: reaching them blocks new writes or new branch creation, never deletes what already exists.

**For genuinely dormant projects (the actual target of the $31k, reframed):**

This is not "enforcing a limit" — it's abandoned-resource reclamation, a different and legitimate category, the same thing AWS and every major cloud does with unused free-tier resources. The rule against silent deletion is about punishing usage; a published, warned, exportable reclamation policy is standard hygiene. Keep the 90-day instinct, but move it to the *end* of a due-process sequence instead of being the whole sequence:

| Day (of zero compute-hours) | Action |
|---|---|
| 60 | **Send email #1**: "this project has been idle 60 days, here's what happens next," with dates. |
| 80 | **Send email #2** + in-app banner. |
| 88 | **Send email #3** (final notice) with a one-click **export/download** link and a one-click **"I'm still using this"** keep-alive button. |
| 90 | **Pause compute** (near-zero marginal cost already, since it's idle) and **drop PITR retention to 0** on that project — this is where the real WAL-storage saving lands. Base data snapshot stays intact. |
| 90–150 (published window) | Project sits **archived**: reachable, exportable, reactivatable by resuming or upgrading. Not deleted. |
| 150 | **Send final email**, 7-day hard deadline, then **delete**. |

This keeps your 90-day number, gives real notice, never touches data without a warned, exportable off-ramp, and still stops paying for WAL retention on data nobody has looked at in three months — which is very likely the larger cost saving anyway, since a project that's already at zero compute-hours contributes nothing to the compute-hours side of the $31k; its cost is almost entirely storage and PITR sitting idle.

**Before turning this on for existing dormant projects**: the 60-day clock starts from the *policy's announcement date*, not from whenever each project actually went quiet. A project dormant since last year does not wake up at "day 400" the moment you ship this — it gets the same 60/80/88/90 sequence as everyone else, starting from announcement day. Anything else is the silent-timer problem again, just backdated.

## Predictability

- Live compute-hours and storage usage in-dashboard, with a projection to period end — you likely already have this for the paid meter; extend it to free.
- The three-email dormancy ramp above doubles as the "written policy on what happens at the limit."
- Pre-approve one concession, per the Netlify precedent: reinstate from the archive at no charge, no questions, if a user disputes the dormancy flag within the archive window. The credit is always cheaper than the "Northmoor deleted my database" thread.

## Change plan — cohorts

| Cohort | What changes | Notice |
|---|---|---|
| New free signups | New limits from day one. | Immediate — this is just the new price list. |
| Existing free accounts, currently within new limits | Nothing changes today; new limits apply automatically once the grace period ends. | 30–45 days from announcement. |
| Existing free accounts, currently *over* new limits (e.g. >10 branches, >2 GB storage) | Grandfathered at current usage — cannot grow further, not clawed back immediately. New caps bind at the same grace-period date; give a specific "what to trim" list per account if possible. | 30–45 days, same date as above, named explicitly in the email to this cohort. |
| Already-dormant free projects | Enter the 60/80/88/90/archive/delete sequence starting from announcement date. | Per the table above, starting day 0 = announcement. |
| Paying customers | Unaffected. Announce anyway — silence here reads worse than the change itself once the free-tier post goes out. | Same announcement, different framing: "here's what's changing on free; nothing changes for you." |

Rules that apply regardless of cohort:
- Apply the shrink to **new accounts immediately**, say so explicitly.
- Never claw back what an *active* account already has without a stated, dated grace period — that's the retroactive-gating failure mode, and it's the one that produces forks and front-page threads, not the number itself.
- Pair the cost-driven cut with something delivered, even something small — e.g. "free tier usage is now visible live with a projection, and export is one click, always" — so the announcement doesn't read as pure extraction. Cost-only justifications invite the reader to compute your margin, and they will.
- Name one owner for the public thread before it ships, with the reinstatement concession pre-approved.

---

## Execution plan

**Phase 0 — before any code ships (this week).**
Run a cost breakdown by resource (compute, storage, egress, WAL/PITR bytes) crossed with cohort (active in last 30 days vs. dormant). This confirms whether branches × PITR-days or raw compute-hours is the real driver of the $31k, and sizes the expected saving from each lever before committing engineering time to all of them equally. This is the mandatory first step the skill calls out — don't skip it in favor of "halve everything and see."

**Phase 1 — engineering (weeks 1–3).**
- Confirm per-project metering granularity exists for compute-hours, storage, egress, WAL bytes, branch count. Reuse whatever already bills the paid tier on compute-hours.
- **Add a hard branch cap (10/project)** at the control-plane API — reject branch creation past the cap with an upgrade CTA in the error.
- Build the 70/85/95/100% warning + hard-pause path for compute-hours if it doesn't already exist for free accounts.
- Build the dormancy detector (0 compute-hours in 60 days) and the notification pipeline: 3 emails, in-app banner, one-click export, one-click keep-alive.
- Build the pause → archive → delete state machine, each transition logged, each stage reversible until the final one.
- **Do not wire the delete stage live** until the full sequence has run once end-to-end against a staging cohort and the emails/exports have been manually verified.

**Phase 2 — announce (30 days before existing-account enforcement).**
- Publish the changelog/blog post: new limits, why, who's affected, exact dates, FAQ. Pair with the "usage now visible live" framing.
- Email every free-tier account directly — a blog post alone doesn't count as notice for this cohort.
- Publish the dormancy sequence dates alongside it, stated as a separate policy from the limit shrink.

**Phase 3 — roll out.**
- New signups get new limits immediately.
- Grace-period clock starts for existing accounts at announcement.
- Dormancy pipeline starts in **detect + notify only** mode immediately — no harm in warning early. Hold pause/archive/delete stages until at least one full cohort has cleared the sequence as a dry run and support volume from it looks sane.
- At grace-period end, new limits bind for everyone.

**Phase 4 — measure, from launch.**
- Weekly: free-tier COGS trend, target expressed as a share of paid gross profit (needs your paid gross-profit number — set the ceiling once you have it, rather than eyeballing "halved" as the target).
- Free-to-paid conversion, watched against the 3–8% self-serve developer band (Lenny's Newsletter corpus) — a drop below it means the cuts went too far, not that marketing needs to work harder.
- Support tickets mentioning lost data or surprise archival — any spike is a stop-and-fix signal on the notice sequence, not a support-team problem to absorb.
- Reactivation rate on paused/archived projects — tells you whether 60/90 days is well-calibrated or catching legitimate low-frequency users.
- **Revisit trigger**: if COGS/gross-profit is still too high after this ships, the next lever is metering PITR/WAL storage as its own explicit line or moving PITR beyond a short window behind the paid rung entirely — not a second round of "halve everything again."