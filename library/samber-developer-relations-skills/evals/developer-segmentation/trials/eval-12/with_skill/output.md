This document is not something to tidy — it's the exact anti-pattern the skill's own reference file names as a rejected map (three seniority-labelled personas, sizes with no method, no decision unit, no anti-segment, next steps that undercut the stated priority). Polishing the prose would just make a broken segmentation look finished. Below is the rebuild, following the skill's method with the information available, and flagging every place a number is inferred rather than measured.

---

# Developer segment map — Windrose Telemetry, H2 2026

## Why this isn't a tidy-up

- **Seniority is the whole cut.** Junior/mid/staff mixes involvement with authority. A junior and a staff engineer on the same platform team, instrumenting the same services, need the same SDK and the same docs — seniority only matters where it maps to who can approve a tool, which belongs in the decision unit, not as its own axis.
- **No decision unit.** None of the three personas says who evaluates, who approves, who signs. For an infra/telemetry product this is usually not the same person.
- **Sizes with no method.** "Large", "~4 million", "Growing" carry no source, filter, date or confidence tier. The 4 million figure is almost certainly a language-ranking or forge-account count misread as a population.
- **No anti-segment.** Nothing is named out of scope, so effort stays spread across all three by default.
- **Next steps contradict the implied ranking.** A beginner tutorial series funds the persona (Jamie) that was never named primary, while Morgan — the closest thing to a stated priority — gets vague "more content."

## Assumptions this draft runs on

No interview was run to produce this. These are stated defaults, not findings — confirm or correct before funding anything:

- **Funded driver** (interview Q2): assumed developer adoption feeding expansion/usage revenue. If the real driver is contributor community or employer brand, the ranking below changes, particularly for the junior segment.
- **Product shape** (Q1): assumed an SDK/library instrumenting services, with a hosted backend and self-serve pricing plus some enterprise motion — inferred from the company name and the product category, not confirmed.
- **Evidence on hand** (Q5): none reviewed. No signup data, support tickets, sales notes or interviews fed this draft — everything below is public-source or judgement, never first-party.
- **Research ceiling** (Q13): unknown, so both a cheap dimension (decision unit) and a moderate one (workload) are used together; if the real ceiling is hours, drop workload and re-run on decision unit alone.

## Cut

**Dimensions:** workload/operational scale (a handful of services for one small team vs. shared infrastructure across an org) × role in the decision (individual/self-serve adoption vs. company adoption with an approver and a signer).

**Rejected:** seniority — a junior and a staff engineer on the same team need the same SDK and docs; where seniority does matter (a staff engineer approving org-wide tooling) it's already captured inside the decision-unit axis, not as a separate segment.

**Deferred, not rejected:** technographic (language/runtime). Legitimate candidate — SDK and docs work is usually organized per language — but nothing here says which languages Windrose's users actually run. Worth running as a fast follow-up once signups or telemetry carry a language tag.

### Candidates considered

| Candidate cut | What it reveals | Cost to stand up | Verdict |
|---|---|---|---|
| Workload × decision unit (chosen) | which artefact to build (multi-tenant vs. quickstart) and who it must convince | moderate — needs ticket/sales-note coding, not yet done here | recommended |
| Technographic (language × hosted/self-hosted) | SDK and docs priority order | cheap once telemetry is language-tagged; unknown today | fast follow-up |
| Buying-mode alone (individual vs. company) | who signs | cheap — hours of sales-note reading | too coarse alone; doesn't say which artefact, only who pays |

## Segments

| Segment | Definition | Size + confidence | Decision unit | Needs | Where they gather | Evidence |
|---|---|---|---|---|---|---|
| Platform/SRE teams at scale | 4–15+ engineers owning shared observability for 50+ developers across many services | ~1.0M–1.5M developers globally, **estimated** (SlashData/CNCF "State of Cloud Native Development," Q1 2026: 19.9M cloud-native developers, filtered to architect/platform-owning roles using Stack Overflow 2025's 6.1% architect share as a proxy filter; as of 2026-09-19) | User evaluates, platform lead approves, budget owner (VP Eng or eng director) signs | Multi-tenant story, cost-control/cardinality docs, migration guide from an incumbent, named production references | Platform-engineering and SRE-focused communities, infra conferences, incident-management circles — not general dev-content channels | None reviewed — 0 data points, below floor |
| Self-serve small-team app owners | 1–5 engineers instrumenting one or a few services, want it working without an ops project | ~3M–6M developers, **estimated** (residual share of the same 19.9M cloud-native population after the architect/platform-lead slice, cross-checked loosely against SO 2025's combined full-stack + back-end share, 41.2%; as of 2026-09-19) | User = buyer, self-serve/card payment | Fast quickstart, generous free tier, sane defaults, minimal config | Language-ecosystem forums, framework communities, package registry pages | None reviewed — 0 data points, below floor |
| Regulated-industry platform teams | Platform teams above, under data-residency, audit or sector-compliance obligations | ~100k–300k, **inferred** (share of the platform/SRE estimate assumed in regulated verticals, by analogy to general enterprise-software vertical mix — no direct source) | Adds security/legal reviewer and formal procurement | Data-residency answers, audit-log export, self-host parity, signed DPA | Vertical-specific conferences, compliance-focused peer groups | 0 data points — hypothesis |
| Junior/learning developers exploring observability | Bootcamp grads and students in their first year, learning by building | order-of-magnitude "large" only, **inferred** (Stack Overflow 2025: ~11.3% of respondents self-identify as students — directional, not filtered for telemetry relevance; not worth precise sizing given anti-segment status below) | Rarely evaluates or approves tooling at a job; adopts what the team already runs | A working example project, not a dedicated funnel | Bootcamp communities, learn-to-code forums, entry-level dev Discords | 0 data points |

## Scoring (coarse, driver = developer adoption → expansion revenue)

| Segment | Size | Reach | Fit | Value | Effort | Competitive position | Compounding | Value ÷ effort |
|---|---|---|---|---|---|---|---|---|
| Platform/SRE teams | M | H | H | H | M | M | H | **highest** |
| Self-serve small-team owners | H | H | M | L | L | M | M | high, but ceiling capped by low per-seat value |
| Regulated platform teams | L | M | H | H | H | L | M | low — effort dominates |
| Junior/learning developers | H | H | L | L | M | L | L | low — no purchase, no approval authority |

Platform/SRE teams win on value and compounding despite moderate effort; the "hates marketing" trait in the source doc is read here as evidence this segment doesn't respond to generic content, not as evidence it's unreachable — reachability score stays high, but the channel changes to proof-driven material.

## Primary

**Platform/SRE teams at scale.** Highest value-per-effort once the currently-unbuilt multi-tenant/cost-control artefacts are funded; wins the deals self-serve users already convert without help, and each named reference compounds into the next one in the same segment (Moore's beachhead logic).

## Secondary

**Self-serve small-team app owners.** Served only by what the primary segment's docs and SDK investment already funds — quickstart quality, sane defaults, free tier. No dedicated content or channel budget this horizon; this is where "more content for Morgan" from the old doc should land, reframed as product/docs polish rather than blog volume.

## Anti-segment

**Junior/learning developers exploring observability.** The audience the old doc invested most visibly in (the beginner tutorial series), and the one to name explicitly out of scope this horizon: they rarely hold the authority to adopt an observability tool at work, so content aimed at them doesn't move adoption or expansion revenue. Not reachable through the same proof-driven channels platform teams need, and building for them competes directly with the primary segment's budget.

Exception, not a kill: if the real funded driver turns out to include talent brand or "future buyers" (today's bootcamp grad picks the stack at their next job), this segment is legitimate again — but only on that explicit non-revenue justification, stated in writing, not by default.

## Hypotheses

**Regulated-industry platform teams** — 0 data points, below the evidence floor. Cheapest test: pull the last 5–10 lost or stalled deals and read them end to end for a compliance/residency blocker; interview two of the blocking reviewers. Drop the segment if the real blocker turns out to be price or feature-parity rather than compliance.

**Both funded segments above the floor only on judgement, not evidence.** Zero tickets, calls or interviews were reviewed for this draft — treat platform/SRE and self-serve as provisionally funded, and run these before committing real budget:
- Code 10–15 recent support tickets or sales-call notes for team size, role and what blocked or closed the deal.
- Five conversations with recent signups matching each profile.
- One telemetry cut on a trait already collected (team size, deployment mode) checking whether behaviour actually diverges.

## Implications

**Build:** multi-tenant reference architecture, cardinality/cost-control guide, migration guide from the likely incumbent (Datadog/Grafana-stack-class competitor), two named platform-team references.
**Publish:** platform-engineering and SRE communities, infra conferences, incident-management circles — not general content marketing.
**Prove:** benchmarks and comparison material a technical champion can paste into an internal doc, not top-of-funnel blog posts.
**Stop:** the beginner tutorial series. It serves the segment this map just moved to anti-segment, and is the same contradiction the old doc's "next steps" already showed.

## Review

Re-read **2026-12-19** (one quarter out). Early re-read on any of: pricing or packaging change, a new language/runtime SDK target, a competitor winning a platform-team deal on a feature Windrose lacks, or platform/SRE share of new signups crossing a threshold once that split is actually tracked.

## Quality gate

| Check | Status |
|---|---|
| 3–5 segments | Pass — 4 |
| Each segment differs in artefact, channel, proof | Pass |
| Every size has range, method, date, confidence | Pass — all marked estimated/inferred, none claimed as measured |
| Decision unit named per segment | Pass |
| ≥half of funded segments clear the evidence floor | **Fail** — primary and secondary are both funded on judgement, zero first-party data points reviewed. Run the three tests under Hypotheses before locking budget. |
| Anti-segment non-empty, includes an audience the team wanted to keep | Pass — junior/learning developers, the old doc's own investment |
| Segments in members' own language | Pass |
| Fits two pages, names a review date | Pass |

## What would upgrade this from a first pass

- Pull actual signups/telemetry tagged by team size or role — moves platform/SRE and self-serve sizing from estimated to measured.
- Read 10–15 recent tickets and sales-call notes — clears the evidence floor for both funded segments.
- Tag signups by language/runtime — unlocks the deferred technographic cut as a real fast-follow, not a guess.