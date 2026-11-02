# Sablefish audience segmentation — recommendation

## Cut it three ways, not one: role × workload × platform maturity

Stop looking for a single "type of customer." For an infra tool that only runs on Kubernetes, one axis will always underfit. Use a small, fixed set of orthogonal axes and cross them into a matrix. That's what makes the document durable — you update the *values* in each axis over time without ever re-deriving the *structure*.

**Axis 1 — Role in the adoption path** (who, and what they need from you)
- **Operator/Champion** — Platform engineer, SRE, or DBRE who runs Sablefish day to day. Cares about toil reduction, failure modes, upgrade safety, debuggability.
- **Economic buyer** — Head of Platform / Infra Director / VP Eng. Cares about headcount leverage, incident cost, vendor risk, licensing cost vs. managed cloud alternatives.
- **Adjacent stakeholder** — App team lead or data engineer who owns the workload Sablefish manages but doesn't run K8s themselves. Cares about latency/availability SLAs and not getting paged.

**Axis 2 — Workload class** (what stateful system they're actually running)
- Relational (Postgres/MySQL), streaming (Kafka/Pulsar), cache (Redis), search (Elasticsearch/OpenSearch), vector/AI stores, other (queues, custom).
- This matters because Sablefish's value prop is fundamentally different per workload — backup/restore semantics, failover behavior, scaling levers, and upgrade risk are not interchangeable across these. A persona that averages across workload classes will produce roadmap decisions and messaging that fit none of them well.

**Axis 3 — Platform maturity** (how far along their Kubernetes journey they are)
- Exploring (evaluating K8s for stateful workloads at all), Migrating (moving existing stateful services off VMs/managed cloud), Scaling (multiple clusters, established platform team), Mature (K8s is default, optimizing cost/reliability at fleet scale).
- This is the axis that changes your GTM motion — an "Exploring" org needs education and risk reduction; a "Mature" org needs fleet-level features and integration depth.

Build the document as a **role × workload matrix**, with maturity as a **filter/overlay** rather than a fourth grid dimension (3D matrices don't get re-read). Not every cell needs a persona — populate only where you have real signal, leave the rest blank and marked "unvalidated."

## Why the agency's clustering is dead in a drawer

Almost certainly it clustered on **statistical similarity across survey responses** (e.g., k-means over satisfaction/NPS-style items, feature-usage frequency, firmographic fields) rather than on a **decision-relevant variable**. That produces clusters with names like "the enthusiasts" or "the cost-conscious" — internally coherent, externally useless, because no one in product or marketing can look at a cluster and know what to *build* or *say* differently. A segmentation only earns its keep if a stranger on the team can read a cluster label and immediately derive a roadmap decision or a headline. Attitudinal/firmographic clusters rarely clear that bar for a technical infra buyer, where the actual driver of adoption is "which stateful system, run by whom, at what stage of K8s maturity" — not sentiment.

This is also why it never got re-opened: nobody could act on it, so nobody had a reason to return to it. Design against that failure mode explicitly — every cell in the new matrix must map to at least one concrete "so we should..." for either the roadmap or the messaging.

## Salvage the 4,100 responses — don't trust the delivered clusters, re-cut the raw data

The clustering output is disposable; the underlying response-level data almost certainly isn't. Before running anything new:
1. Get the raw, respondent-level export from the agency (not just the cluster summary) — check the contract/SOW for data ownership if this isn't already in hand.
2. Check whether the survey instrument captured role, workload type, and any K8s-maturity proxy (cluster count, managed vs. self-hosted, years running K8s in prod). If those fields exist, you can re-cut the existing 4,100 responses against the new matrix in an afternoon — no new fieldwork needed for a first pass.
3. If those fields are missing or too coarse, that's your primary gap to fill with new research (see below), not a reason to discard the dataset — free-text/open-ended answers can often be hand-coded into workload class and maturity retroactively.
4. Flag confidence per cell: a cell backed by re-cut survey data is **High**; a cell you're populating from your own team's intuition or sales anecdotes is **Low** until validated.

## What goes in a populated cell (persona-lite, not a full dossier)

For each priority cell, capture only what changes a decision:
- **Primary job to be done** (one sentence)
- **Top 2-3 pains**, in their words if the survey free-text has quotes
- **Trigger event** that made them look for something like Sablefish
- **Objection/fear** that stalls adoption
- **What "success" looks like to them**, concretely

Skip demographic filler (age, generic "tech-savviness") — it doesn't drive a K8s tooling decision. Skip naming them cutely; this audience will read the document literally, and cute names age worse than technical ones do.

Example — one high-confidence cell to seed the matrix (adjust once you re-cut the survey):

> **Operator × Relational databases × Scaling maturity**
> Job: keep Postgres/MySQL highly available across multiple clusters without a dedicated DBA team.
> Pains: manual failover runbooks, upgrade anxiety (data loss risk), alert fatigue from a home-grown operator.
> Trigger: an outage or a failed manual failover that got escalated to leadership.
> Objection: "operators are a black box — what happens when it does the wrong thing at 3am?"
> Success: zero-touch failover, verified restore drills, upgrades that don't require a maintenance window.

Leave every other cell as a stub (`role × workload — unvalidated, no data yet`) rather than inventing content — a visibly incomplete matrix is more trustworthy, and more likely to get filled in by whoever reads it next, than one that fakes completeness.

## Keeping it alive for two years

A document only stays "re-read and updated" if updating it is cheaper than re-deriving it from scratch. Structure for that:
- **One matrix, versioned** (a single source file, not a slide deck) — role rows, workload columns, maturity as a tag on each cell, confidence level on each cell.
- **Quarterly light touch**: sales/CS/support tag new signal (a lost deal, a churn reason, a support escalation) directly against a matrix cell as it happens, instead of batching it into an annual project. This is the mechanism that killed the last one — nothing fed it between the survey and now.
- **Annual heavy touch**: re-survey or re-mine (support tickets, community forum, sales call notes) specifically to update maturity distribution and surface new workload classes (e.g., vector stores didn't matter two years ago and might dominate next year) — expect the axes themselves to need revisiting at this cadence, not the cells.
- **One owner**, named, whose job includes noticing when a cell's confidence is stale (12+ months since last real evidence) and either refreshing it or explicitly marking it deprecated.
- **A standing "so what" column** next to every cell — the roadmap or messaging implication. If a cell can't produce one, it's not worth maintaining; merge it into a neighboring cell instead of preserving it out of completeness.

## What not to do

- Don't cut by company size or industry as the primary axis — for a K8s-only operator, firmographics are a weak proxy for the workload/maturity reality that actually drives fit.
- Don't keep the agency's attitudinal clusters as a parallel "for reference" artifact — a second, un-actionable taxonomy sitting next to the good one just recreates the confusion that shelved it the first time. Retire it explicitly.
- Don't wait for a full new survey before shipping v1 of the matrix — populate what the re-cut 4,100 responses support now, mark the rest unvalidated, and let the quarterly cadence fill gaps.