# DevRel charter: Bracknell Data, next 2 quarters

Next action: confirm funding driver + who signs the contract (open questions below) before this goes to a board.

## Position (CORE)

**Community** — Discord active enough that first-line triage backs onto 2 advocates. 2 known blog authors (the advocates). Champion program: none stated. Engagement level, drop-off point: not given, flagged below.

**Organization** — Team of 4 does advocacy, community, support, and incident comms with no stated role split. No engineering on-call layer mentioned — pages reach advocates directly. That routing is likely the real root cause behind "advocates get paged," not agency capacity.

**Relationships** — Not stated. Vector DB with a status page and outages implies at least some production, company-adoption customers, not just solo devs.

**Ecosystem** — Crowded vector-DB category (Pinecone, Weaviate, Qdrant, Milvus, pgvector class of competitors) where technical differentiation is the whole pitch. Generic ghostwritten content loses fastest exactly here.

**Lifecycle stage**: Grow. Small team, specializing under load, not yet scaling with leverage programs.

## Driver

Not named by a funder in what's given. Working assumption: **developer adoption** (primary), **developer enablement** (secondary — lowering per-developer support cost as production usage grows). Confirm before locking bets below — wrong driver here invalidates the rest. [Open question]

## Goals (AAARRRP)

- Primary 1: **Activation** — developer reaches a working production integration. Journey step: evaluation → commitment.
- Primary 2: **Retention** — production users keep trusting the DB through an incident, don't churn after an outage. Journey step: commitment → standardization.
- Secondary: **Awareness** — blog reaches new developers. Journey step: initial awareness.

No drop-off numbers given for any of these — that's a preference until measured, flagged in Open questions.

## Audience priority

Status page + outages implies both adoption paths exist. Team of 4 can't serve both at full strength this horizon — pick **company adoption** as primary (reference architectures, security answers, named production references), individual-developer path stays served but not the funded focus. Flip this if question 2 (who signs) says bottom-up individuals only. [Open question]

## Pillar mix

Fund two, per Grow-stage cap: **developer enablement** (support discipline, incident trust) and **developer marketing** (blog, advocate-directed). Discord treated as enablement's front door, not a new community-venue build. Advocacy stays in-house — it's the credibility asset the other two pillars are borrowing against.

Starved this horizon: contributor programs, champion program, event sponsorship.

## Bets

1. **Tiered Discord support** — owner: community-owning advocate — signal: % questions resolved off-hours with zero wrong technical answers — review: end of next quarter.
2. **Scaled blog pipeline, outline-and-review pattern** — owner: each advocate, on their own posts — signal: posts/month at unchanged technical-error rate — review: end of next quarter.
3. **Incident comms moved off advocates, kept in-house** — owner: engineering on-call lead — signal: zero advocate pages during a severity incident this horizon — review: after first incident post-launch.

## Build vs buy

| Bet | Source | Latency | Setup cost | Reviewer | If it stops |
|---|---|---|---|---|---|
| Discord tier-one: FAQ, known-issue, "have you tried X" | **Contractor**, not agency — reference table rates agency "no" for developer support and "risky" for moderation; contractor is "workable"/"possible" for both | ~1 week brief, live in 2-3 weeks | Playbook + macro library, one-time | Community-owning advocate, spot-checks | Reverts to advocates day one, no decay |
| Discord escalation, enforcement decisions, any answer needing a technical opinion or a "we don't support X" | In-house. No menu — this is a named red line | — | — | — | — |
| Blog body drafts | Agency, Snyk pattern: advocate writes outline, agency drafts body, advocate reviews before publish | ~6 months to build the pipeline, then 8-9 weeks per piece once running | Outline templates, style guide, byline-disclosure clause in contract | Same advocate whose byline runs, every piece | Series stops cleanly, nothing decays — but don't promise 3x cadence before the pipeline is actually live |
| Ghostwriting with no advocate outline or review, published under the advocate's real name | **Refused** — see below | — | — | — | — |
| Live status-page / outage updates | In-house, engineering on-call. No menu | — | — | — | — |
| Post-incident writeup, after resolution | Advocate-owned; agency can draft a first pass off the closed incident timeline | Days after resolution, never during | Timeline handoff from on-call | Advocate | Reverts to advocate alone |

## Staffing

Grow stage: specialize toward the actual constraint, not a template hire. Next hire, and its trigger: a support/community engineer owning Discord escalation and postmortems — triggered once contractor tier-one volume exceeds what one advocate can spot-check in under an hour a day. Until that trigger fires, extend the contractor, don't add headcount.

Separately, check today whether an SRE/engineering on-call rotation exists at all. If pages only ever reached advocates because no such rotation exists, that's an engineering-org gap. No vendor fixes a missing on-call rotation — it only delays the first bad incident.

## Refused

- **Ghostwriting blog posts under a real advocate byline with no advocate outline or review.** Named failure mode: detected fast, costs more trust than 3x output earns. Developers grant approval to people who visibly did the work (Hawthorn, "DevRel and the approval economy," 2018) — a rented byline breaks exactly that.
- **Agency-authored live status-page or outage updates.** Incident communication is a red line — a promise from a person. During a live incident nobody has time to fact-check a vendor's draft against what engineering actually knows.
- **Agency as final decision-maker on moderation or code-of-conduct enforcement.** Contracted first-line triage is fine. The ban-or-warn call stays in-house.
- **Calling "hand it to the agency" a fix for the paging problem** without first checking whether an on-call rotation exists.

## Open questions

- Real funding driver, in the funder's own words — assumed here, not confirmed.
- Deadline for first visible result, and to whom (board, renewal, budget review).
- One-off win vs compounding asset — changes whether reach or enablement leads.
- Effort ceiling: are all 4 people full-time devrel, or hours on top of another job.
- Company-adoption vs individual-adoption split — who actually signs today.
- Does engineering already run its own on-call, or does every page really only reach advocates.

## Exec narrative

Four people can't triple content, own every Discord answer, and staff incidents at once — something breaks first. This plan rents volume (Discord FAQ answers, blog drafting) and keeps judgment in-house (technical calls, moderation, incident updates), because that judgment is what developers actually trust the company for. It frees advocate hours for outlines, reviews, and escalations instead of first drafts and pages. Blog cadence triples once the agency pipeline is live, in about two quarters, not this week. Incident paging stops hitting advocates only once engineering owns its own on-call rotation — that fix is organizational, not a vendor contract.

## Review

Re-run this charter when the funding sponsor changes, when the agency pipeline misses its 8-9-week per-piece target twice running, or before the next budget review — whichever comes first.

## Quality gate

- Driver named with owner: **FAIL** — assumed, not confirmed. Fix before this goes to a board.
- Each goal ties to a journey step: PASS. Drop-off evidence missing — flagged.
- Every bet has owner, signal, review date: PASS. Owners are role placeholders — name people before finalizing.
- Refused list non-empty, includes something the team wanted: PASS — the ghostwriting and live-incident outsourcing were explicitly proposed and are exactly what's refused.
- Open questions written down, not assumed away: PASS.
- Nothing on a credibility surface outsourced: PASS — byline, moderation calls, incident comms all stay in-house.
- Exec narrative, no jargon: PASS.
- Baselines moved from this skill's defaults: none — capacity 70%, 2 pillars, 3 goals, 3 bets, all held.

Next: confirm the 2 FAIL/open items above (real driver, deadline), then name real owners for the 3 bets.