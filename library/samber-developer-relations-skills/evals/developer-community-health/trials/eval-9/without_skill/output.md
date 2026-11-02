# Fixing the Sablefish community health dashboard

Three separate problems are tangled together here, and they need three separate fixes — don't try to solve them with one dashboard redesign pass.

1. **Thresholds are stale, not wrong.** They were right 14 months ago for whatever traffic/contributor volume Sablefish had then. Nobody re-baselines them, so half the metrics permanently read red against a project that's since grown, shrunk, or seasonally shifted. Static thresholds rot; nobody schedules the re-bake.
2. **No owner means no consequence.** A metric with nobody's name on it can't be acted on, so it gets muted instead of fixed — muting is the rational response to an alert nobody is responsible for resolving.
3. **"Active members" is two different metrics wearing one name.** The community team and data team aren't disagreeing about the number — they're disagreeing about the definition, and the dashboard hides that by giving both a single label.

Below is a complete redesign: new metric governance model, a resolution for the active-members conflict, a threshold-rebaselining method, and a rollout plan. Where I don't have your actual 19 metrics' names/history, I've given you the exact worksheet to fill them into rather than guessing values I can't know.

---

## 1. Kill the "active members" ambiguity — don't average it, split it

Averaging or picking a winner between the two teams' numbers keeps the argument alive forever, because it never resolves *which reality* the number describes. Instead, name them as what they actually are and retire "active members" as a term entirely.

| Old name | New name | Owner | Definition |
|---|---|---|---|
| Active members (data team's number) | **Active Contributors** | Data team | Unique accounts that opened a PR, pushed a commit, or filed an issue in the trailing 28 days |
| Active members (community team's number) | **Active Participants** | Community team | Unique accounts that did any of the above, or commented/reacted on an issue, PR, or discussion, in the trailing 28 days |

This is the standard CHAOSS (Community Health Analytics for Open Source Software) split — "contributors" (people who change the artifact) vs. "community members" (people who engage with it) — and it maps exactly onto why your two teams computed different numbers: they were never measuring the same population.

Rules to make this stick:

- Both metrics live on the dashboard **side by side, permanently**, never merged into one tile. Seeing both kills the "which one is right" framing — they're both right, about different things.
- **Active Contributors ⊆ Active Participants** by construction. If a monthly snapshot ever shows Contributors > Participants, that's a pipeline bug, not a debate — add an automated consistency check that pages the data team (see §3) if this inverts.
- Put the two-line definition table above directly on the dashboard (tooltip or header), so a newcomer to the meeting doesn't re-litigate the split every month.
- One person is the **metrics steward** for this pair — not for computing them, but for owning the definition text itself, so a future edge case (bot accounts, co-authored commits, staff reactions) gets decided once and written down, not re-argued live.

---

## 2. Replace static thresholds with a rebaselined, tiered system

A threshold set once 14 months ago and never revisited is a guess that's had 14 months to go stale. Replace "is the number above/below X" with "is the number outside its own recent normal range," recomputed on a schedule.

**Per metric, define three things instead of one:**

| Field | Meaning |
|---|---|
| **Baseline window** | Trailing 6 months of actual data for this metric (excludes the current month) |
| **Band** | Green = within 1 std-dev (or ±20% if the series is too short/noisy for std-dev) of the baseline mean. Yellow = 1–2 std-dev. Red = beyond 2 std-dev, **or** breaches a hard floor tied to an actual business consequence (e.g., "median issue response time > 14 days" — a number chosen because it's the point where contributors churn, not an arbitrary round figure) |
| **Recalibration cadence** | Baseline window rolls forward automatically every month. A human only re-examines the *hard floor* (not the statistical band) once a quarter |

Why this fixes "half go red every month": a fixed threshold can't tell the difference between "this metric is actually broken" and "this metric has permanently moved because the project is 3x bigger than when the number was chosen." A rolling baseline absorbs organic growth/decline automatically and only fires when something moves *relative to its own recent self* — which is what "worth discussing in the monthly meeting" should mean.

For the few metrics where a hard floor genuinely matters regardless of trend (e.g., security-patch response time, license-compliance checks), keep a hard red line — but require it to be justified in one sentence in the metric's definition doc ("red below X because Y"), not just inherited from whoever set it up originally. If nobody can write that sentence today, that's your signal the threshold was arbitrary and should convert to the rolling-band model.

---

## 3. Assign a named owner to every metric — no exceptions

Nobody being named against any metric is why muting is the equilibrium. Fix with a one-time pass, then enforce it as a gate on the dashboard itself.

For each of the 19 metrics, fill in:

| Metric | Definition owner (decides what it means) | Response owner (acts when it's red) | Runbook link | Review cadence |
|---|---|---|---|---|
| *(19 rows — see worksheet below)* | | | | |

Rules:

- **A metric with no Response owner gets auto-muted from the "requires action" view** and moves to an "informational only" section of the dashboard — this makes the current de facto muting *visible and intentional* instead of silent and universal. Right now everyone mutes everything ad hoc; make the dashboard do it explicitly for genuinely ownerless metrics, and force a decision (assign an owner or retire the metric) before it can come back.
- Definition owner and Response owner can be the same person but don't have to be — e.g., data team defines "Active Contributors," but the response owner when it drops might be devrel.
- Every red metric must link to a one-paragraph runbook: what to check, who to loop in, what "fixed" looks like. If you can't write the runbook, you likely can't act on the metric either — that's a sign it's a "watch" metric, not an "act" metric (see §4).
- Put owners' names/handles directly on the dashboard tile, not in a separate doc. Visibility is the enforcement mechanism.

---

## 4. Split the dashboard into two tiers: Act vs. Watch

Not all 19 metrics deserve the same visual weight or the same monthly-meeting airtime. Force a one-time classification:

- **Act tier** (page/discuss when red): metrics with a Response owner, a runbook, and a real consequence if ignored. Expect this to be a *small* subset — 5-8 metrics, not 19. This is what the monthly meeting actually reviews.
- **Watch tier** (context, not alarm): metrics worth tracking for trend but with no single actionable response — vanity/health-context numbers like total star count or forum post volume. These render in a muted, non-red-capable style (grey trend arrows, not stoplight colors) so they stop competing visually with metrics that actually need a decision.

This single change — removing the *ability* of Watch-tier metrics to render red — eliminates most of "half the board is red every month" without touching a single threshold, because most of what's going red is probably Watch-tier noise that was never actionable in the first place.

---

## Rollout plan

| Week | Action |
|---|---|
| 1 | Run the ownership + tier worksheet (below) against all 19 metrics with both teams in the room. Resolve Active Contributors/Participants split as the first agenda item — it'll unblock the rest since it's the most contentious. |
| 2 | For every Act-tier metric, pull 6 months of history, compute the rolling baseline band, and get the Response owner to sign off on the hard-floor sentence (or confirm there isn't one). |
| 3 | Rebuild the dashboard: two-tier layout, owner names on tiles, Active Contributors/Participants side by side with the definition tooltip, ownerless metrics demoted to informational. |
| 4 | Run one full monthly cycle live, alongside the old dashboard, and compare which metrics actually got discussed vs. ignored. Retire the old dashboard once the new one's Act tier proves itself. |

## Ongoing governance

- **Quarterly threshold review**: 30 minutes, only for hard floors (the statistical bands self-adjust). Agenda: "did any hard floor's justification sentence stop being true?"
- **New metric gate**: nobody adds metric #20 without filling in Definition owner, Response owner, tier, and threshold method on day one. This is the actual root-cause fix — the current 19 accumulated ownerless and undefined because there was never a gate, not because anyone was careless.
- **Annual metric cull**: any Watch-tier metric nobody has referenced in a meeting in 12 months gets removed, not archived-and-ignored. A dashboard that only shows things people use stays trusted; one that accumulates zombie tiles is what got you here.

---

### Worksheet to fill in your real 19

Copy this row for each metric you currently track:

```
Metric name: 
Current definition (exact formula): 
Tier: Act / Watch
Definition owner: 
Response owner (blank if none — this is your muted-metric signal): 
Baseline: rolling 6-mo band / hard floor + justification sentence
Runbook (Act tier only): 
Last time this metric changed a decision: 
```

Run this once, live, with both teams — the act of filling in "last time this metric changed a decision" is usually enough on its own to reveal which of your 19 are actually Watch-tier pretending to be Act-tier, which is most of what's driving the monthly-red fatigue.