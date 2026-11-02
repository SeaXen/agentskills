Next action: hand the 4,100-response survey spreadsheet (or raw response export) to whoever can recode it by workload category — that single step upgrades most of this map from inferred to measured, for free, since it's already paid for.

Five assumptions below stand in for the interview I couldn't run live. Confirm or correct them; everything else in the map holds either way.

1. Funded driver = developer adoption feeding revenue (PLG infra tool), not pure sales-enablement or employer-brand. Changes scoring weights if wrong.
2. Company shape = developer-first: the engineer usually sits in the buying room, until team size crosses a threshold and platform-lead/security approval appears.
3. No forcing deadline inside the 2-year horizon beyond the horizon itself.
4. Workload taxonomy (DB / streaming / cache-search / ML-infra) is my inference from "stateful workloads," not your survey's actual cluster output.
5. The survey recode above is the highest-leverage single action available — cheaper than every other option below.

---

# Developer segment map — Sablefish, 2026H2–2028H2

## Cut

**Dimensions:** workload domain (what stateful software runs under Sablefish) × decision unit / adoption mode (who evaluates, approves and signs).

**Rejected — ecosystem/technographic.** Sablefish "only runs on Kubernetes — no VM build, no serverless flavour, nothing else planned." One ecosystem, one cell: the cut can't discriminate because there's no second side of the line. K8s distribution or cloud (EKS/GKE/AKS/OpenShift/vanilla) stays a descriptive field per segment — it changes a Helm values file, not who the person is or what they need.

**Rejected — seniority.** A junior SRE and a staff engineer on the same platform team, running the same workload, need the same operator docs and the same failure playbooks. Authority (who can standardize Sablefish across an org) is already carried by the decision-unit axis.

## Candidate cuts considered

| Candidate | Primary axis | Cost to stand up | Why ranked here |
|---|---|---|---|
| **Workload domain** *(chosen)* | what kind of stateful software (DB, streaming, cache, search, ML-infra) | Near-zero — the 4,100-response survey + clustering already exists, unopened, fully paid for | Normally the most expensive cut (weeks of ticket coding); the existing dataset collapses that cost, which is the single fact that reorders the default ranking |
| Ecosystem | cloud/runtime/distro | Near-zero if telemetry captures it | Deleted outright — single dominant cell (K8s-only), fails the discriminate test before cost matters |
| Buying-mode alone | who signs | Hour or two, if sales-notes/CRM data exists — not confirmed for Sablefish | Loses to workload on value (doesn't tell you what to build, only how to sell) and doesn't currently have a confirmed cheap data source either. Kept — but demoted to the second axis, since Step 4 requires naming it per segment regardless |

Default ranking (buying-mode cheapest → ecosystem → workload most expensive) is inverted here specifically because of the pre-paid survey — this is the exact condition the method calls out for promoting the workload cut to first.

## Segments

| Segment | Definition | Size + confidence | Decision unit | Needs | Where they gather | Evidence |
|---|---|---|---|---|---|---|
| **Transactional-DB platform teams** | 4–20-engineer platform/infra teams running Postgres/MySQL-family clusters on K8s for other teams inside the company | Unsized — pending survey recode. Ceiling: 19.9M cloud-native developers globally (CNCF/SlashData *State of Cloud Native Development*, Q1 2026, up from 15.6M Q3 2025); the DB-on-K8s, platform-team-scale slice below that is **inferred**, order-of-magnitude only | User (SRE/DBA) evaluates; platform lead approves; security/compliance signs off on backup+encryption; infra budget owner signs | HA/failover guarantees, PITR & backup automation, replication-topology visibility, migration path off managed DBaaS or bare StatefulSets, multi-tenant RBAC | CNCF/K8s Slack (#sig-storage and DB-operator channels), KubeCon, Postgres/MySQL confs, Platform Engineering Slack / PlatformCon | **Hypothesis** — no independent data points yet; recode survey by workload category to confirm |
| **Streaming/eventing platform teams** | Same team shape, running Kafka/Pulsar/RabbitMQ on K8s | Inferred, smaller than the DB cell | Same shape as above, security sign-off on data-loss/replay guarantees instead of encryption | Zero-data-loss rolling upgrades, partition-rebalancing tooling, throughput SLO visibility, retention storage-tiering | Kafka Summit/Current, CNCF streaming SIGs | **Hypothesis** |
| **ML/AI infra teams** | Platform/MLOps engineers running vector DBs, feature stores or checkpoint stores on K8s | Inferred, smallest and least certain cell — genuinely below the evidence floor | Likely same platform-team shape, plus an ML-platform stakeholder | GPU-aware scheduling integration, large-volume snapshot/restore, storage cost controls | MLOps/vector-DB communities — still fragmented, no single hub | **Hypothesis, thin** — fewer than 5 data points; needs its own test before funding anything |
| **Solo SRE / self-hosters, mixed workloads** | 1–3-person teams or homelab engineers running a mix of DB/cache/queue on one cluster, no formal buying process | Inferred; largest head-count, smallest value per head | User = buyer, or no purchase at all | 10-minute quickstart, safe defaults, small footprint, community support (no paid tier expected) | r/kubernetes, K8s Slack #general, GitHub, homelab communities | **Hypothesis** — justified on non-revenue grounds only (see below) |
| **Regulated/air-gapped enterprise platform teams** *(anti-segment)* | Platform teams under FedRAMP, PCI or data-residency obligations | Inferred, mid-size slice of the DB/streaming cells above | Adds a dedicated security/compliance reviewer and legal | Air-gapped registry mirroring, audit-log export, FIPS-validated crypto, signed DPA, compliance attestation | Vertical/compliance-focused conferences and peer groups | **Hypothesis** |

**Discarded honestly:** every size above is inferred except the one global ceiling figure. That is the map's real state right now — see the Quality Gate below rather than a polished-looking number that hides it.

## Primary

**Transactional-DB platform teams.** Score (driver = developer adoption → revenue): size 3, reachability 3, fit 3, value 3, effort 2, competitive position 1, compounding 3.

Value cluster average (2.6) ÷ effort (2) = **1.3** — highest ratio among the funded candidates, driven by universal fit (data loss and downtime are the most burning pain in any stateful-ops role) and the highest compounding (named production DB references are the highest-leverage proof for every other workload category later). It wins despite the worst competitive-position score in the set (CloudNativePG, CrunchyData and Percona already own default mindshare for Postgres-on-K8s specifically) — because nothing else in the set beats it on fit, value or compounding, and competitive position alone isn't disqualifying, just the thing to design the wedge against (see Implications).

## Secondary

**Solo SRE / self-hosters, mixed workloads.** Ratio (2.0 ÷ 1 = 2.0) beats the primary on paper, and that's the trap the method warns about: highest ratio, thinnest value. No dedicated content or events this horizon — served only by what the primary already funds (quickstart, docs quality, OSS free tier). Justified on non-revenue grounds: **future buyers** (today's homelab engineer picks the stack at tomorrow's platform-team job) and **contributor supply** (OSS issues/PRs), not on this horizon's revenue.

**Not funded, not primary/secondary, kept in the map:**
- *Streaming/eventing platform teams* — ratio 1.0, loses specifically on competitive position (Strimzi is the entrenched open-source default). Revisit if Strimzi's momentum stalls or a Sablefish DB win creates a cheap cross-sell into a streaming workload at the same account.
- *ML/AI infra teams* — ratio 1.0, loses on evidence, not on opportunity. Genuine white space (competitive position 3, least contested cell in the whole map) — worth the cheap test below before writing it off.

## Anti-segment

**Regulated/air-gapped enterprise platform teams.** Reachable and plausibly high-value, but the artefact list — air-gapped registry mirroring, audit-log export, FIPS-validated crypto, formal attestation — is unbuilt and unfunded this horizon. Revisit when/if a compliance pack gets scheduled. Writing this down stops each lost regulated-sector deal from reopening the audience debate on its own.

## Hypotheses

All four non-anti segments sit below the 5–10-data-point evidence floor today. Cheapest tests, cheapest first:

1. **All workload segments** — recode the existing 4,100-response survey's cluster output by "primary workload managed." Days of analyst time, not new research; this alone could move three segments from hypothesis to measured.
2. **ML/AI infra** — read 10 support tickets/community threads end to end tagged for ML/vector-store use, plus 5 conversations with users who match the profile. Write the result that would kill the segment before running the test (e.g., "if fewer than 3 of 10 tickets mention GPU scheduling or checkpoint storage, drop it").
3. **Solo self-hosters** — one telemetry cut on a trait already collected (single-node vs multi-node install), checking whether behavior actually diverges from platform-team installs.

## Implications

- **Build:** HA/PITR reference architecture for the transactional-DB segment; a migration guide off managed DBaaS and off bare StatefulSets; nothing new for streaming, ML/AI or self-hosters beyond what the primary already needs.
- **Publish:** platform-engineering and Postgres/MySQL-specific channels, KubeCon. Not a generic "works for any stateful pod" message — that undersells the DB-specific depth that's the actual wedge against CloudNativePG/CrunchyData.
- **Prove:** 2–3 named production DB references with real numbers (RPO/RTO, uptime) — proof concentrates inside the primary segment per the method, rather than spreading thin across all four.
- **Stop:** don't scope an air-gapped/compliance pack this horizon; don't fund ML/AI-specific work until the hypothesis test above returns a result.

## Review

Re-read at **2027Q1** (2 quarters out — tighter than the 2-year horizon itself, since this map is meant to be re-run, not re-read once). Full re-cut at the 2-year mark regardless.

Early re-read on any of:
- the survey gets recoded by workload category (immediate — every size in this map changes);
- a pricing or packaging change;
- Strimzi or a DB-operator incumbent loses visible momentum, or a new entrant clones their playbook against Sablefish's primary segment;
- the primary segment's share of new signups passes a set threshold;
- Sablefish ever adds a second platform target (would resurrect the ecosystem cut this map just deleted).

## Quality gate

- Three to five segments: **pass** (5, including anti-segment).
- Every segment names a differing artefact/channel/proof: **pass**.
- Every size carries range + method + date + confidence: **pass on format, fail on tier** — everything but the 19.9M ceiling figure is inferred, not measured or estimated. Flagged, not hidden.
- Every segment names its decision unit: **pass**.
- At least half of funded segments clear the evidence floor: **fail, currently** — all four are hypotheses. This is the map's one open item; the survey recode is what closes it.
- Anti-segment is non-empty and names something the team likely wanted to keep: **pass**.
- Plain-language rows: **pass**.
- Fits two pages, names a review date: **pass**.

This map is honest, not finished — it names the right axis and the right shape, but every number in it is a placeholder for what the paid-for survey already knows. Recode it, then re-run this map's sizing section only; nothing else here needs to change.