# Northmoor free-tier cost plan — execution playbook

## 0. Fix the plan before executing it

"Halve every limit" breaks on two of your six numbers — fix these before you build anything:

- **Branches: "unlimited" → no number to halve.** This is very likely your real cost driver, not the other five combined. Branches in a copy-on-write Postgres product are cheap to create and expensive to forget — nobody deletes a branch, they just abandon it. Before picking a cap, pull the actual distribution: branch count per free project, storage/compute attributable to branches vs. base project. If you don't have that telemetry yet, that's step 1, not the limit change.
- **Projects: 3 → 1.5.** Round down to 1 if you want the aggressive cost cut (most hobbyist accounts use one project anyway), round up to 2 if you want a softer landing. Pick one and say why in the changelog — don't leave it implicit.

Working table (fill the branch cap once you have the data, everything else halves cleanly):

| Limit | Today | New | Note |
|---|---|---|---|
| Branches | unlimited | **cap, TBD from telemetry** (start at 10 if you have nothing else) | highest-leverage change |
| Storage | 5 GB | 2.5 GB | |
| Compute-hours | 100 | 50 | |
| Projects | 3 | 1 (aggressive) or 2 (soft) | pick one |
| Egress | 10 GB | 5 GB | |
| PITR | 7 days | 3 days | WAL retention is itself a storage cost, don't skip it |

## 1. Instrument before you cut anything

You can't validate the $31k target without a per-project cost baseline. Before shipping any limit change:
- Tag compute-hours, storage, egress, and branch count per free project.
- Segment by activity: last-query timestamp per project.
- Model expected savings separately for (a) dormancy cleanup and (b) limit halving — they're two different levers and you'll want to know which one actually moved the number.

## 2. Sequence: dormancy cleanup first, limit cuts second

Ship in this order, not simultaneously:

1. **Inactivity expiry + deletion** — reclaims abandoned resources, near-zero backlash if done right (nobody defends a 14-month-old forgotten branch).
2. **Halved limits for new signups** — zero backlash, applies only to accounts that never had the old deal.
3. **Halved limits for existing accounts** — highest backlash risk, needs grandfathering (below). Do this last, after the first two have already cut into the $31k.

## 3. Inactivity expiry mechanism

Define dormant precisely: **no compute activity (queries/connections) for 90 days**, checked per-project, not per-account (an account with one dead project and one live one shouldn't lose the live one).

State machine:

```
active → warned (day 60) → warned again (day 75) → 
final notice (day 89) → suspended (day 90, compute blocked, data intact) →
pending-deletion (day 90+14 grace) → deleted
```

Requirements at each step:
- **Day 60/75/89 emails**: state exact deletion date, one-click "keep alive" link that resets the clock without spinning up compute, link to export.
- **Day 90 suspension, not deletion**: block new connections, keep data on disk. This is your safety margin against false positives (billing outage, monitoring bug, user on vacation).
- **14-day final grace with one-click export** (pg_dump or branch export) before hard delete. This single feature is what keeps this from reading as the "silent data loss" anti-pattern — cheap to build, expensive to skip.
- **In-app banner** on the project dashboard from day 60 onward, not just email — email deliverability isn't 100%.

Log every state transition. You will need this the first time someone claims "you deleted my project without warning."

## 4. Grandfathering existing users — this is the part most likely to blow up

Cutting live limits under accounts that already provisioned against the old ones is a rug pull (see: HashiCorp, Redis licensing backlash) even when the business case is sound. Concretely:

- **New limits apply immediately to new signups only.**
- **Existing accounts get a 60-90 day notice window** before new limits are enforced. Email every affected free user individually with *their own numbers*: "you're using 3.2 GB of 5 GB, new limit is 2.5 GB, here's what changes on [date]." Generic blast emails read as corporate deflection; personalized usage emails read as a company that did its homework.
- **Enforce by soft-throttle, not hard deletion**: once the grace period ends, block *new* branch/compute/storage growth above the new cap, but don't force-delete an over-limit project that predates the change. Let it shrink naturally via the dormancy policy instead of a second destructive action stacked on the first.
- Consider a **loyalty carve-out** for accounts active >12 months (your power users are also your loudest public voices — HN/Twitter backlash usually traces back to exactly this cohort feeling blindsided).

## 5. Comms plan

- **Blog post** framed as "keeping the free tier free, permanently" — the honest reason (unsustainable cost) is fine to state plainly, but lead with what stays generous, not with the cuts.
- **FAQ**, minimum: "will my data be deleted," "how do I keep a project alive," "can I export before deletion," "why did limits change," "what if I'm a paid customer — does this affect me" (it shouldn't, say so explicitly).
- **Per-user personalized emails** for the existing-account rollout (see §4) — this is the highest-leverage anti-backlash spend you'll make.
- **In-app banners**, not just email, for both the dormancy countdown and the new-limit notice.

## 6. Legal / ToS

- Update the free-tier terms with an explicit effective date and the inactivity-deletion clause before enforcing it — don't apply the policy retroactively to data already at risk without prior notice.
- State the data-export window explicitly in the ToS, not just in emails — this is your defense if a deletion is disputed later.

## 7. Metrics to watch post-launch

Track weekly for the first two months:
- Free-tier monthly cost (target trajectory toward well under $31k — set a number)
- Free→paid conversion rate (tighter limits should push this up; if it drops, something else broke)
- New signup rate and day-1 activation (should be flat — new limits shouldn't visibly change the hobbyist experience)
- Support ticket volume tagged to this change
- Public sentiment (HN/Twitter/Reddit) — assign someone to watch this the week the blog post goes out, not passively

## 8. Rollout timeline

| Week | Action |
|---|---|
| 1-2 | Ship per-project cost/activity telemetry, pull branch-count distribution |
| 3-4 | Build dormancy state machine + export flow, ship to all free accounts (90-day clock starts now) |
| 5 | New limits live for new signups only |
| 5 | Send personalized notice emails to existing free accounts (grace period starts) |
| 5-13 | Grace period; monitor conversion, sentiment, support load |
| ~14-17 | First dormancy deletions land (90 days from week 3-4 start) |
| ~13-14 | New limits enforced (soft-throttle) on existing accounts |

Re-baseline the $31k number after week 17 — that's your first point with both levers (dormancy + limits) fully live.