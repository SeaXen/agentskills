# Bracknell Data — Community & Content Agency Sourcing Plan

**Context:** Series B, vector database, 4-person DevRel team, 2 advocates paged on-call. Constraint is advocate hours, not budget. Goal: offload Discord L1 moderation + community Q&A, triple blog output via ghostwriting under advocate bylines, and stop paging advocates during outages by having the agency draft status-page updates.

Because hours (not cost) is the binding constraint, this plan optimizes for **fast, low-supervision ramp** over cheapest bid — pay for seniority and technical fluency up front so the team spends onboarding hours once, not every week.

## 1. Scope split — what the agency owns vs. what stays in-house

| Workstream | Agency owns | Stays with advocates |
|---|---|---|
| Discord L1 | First-response, FAQ answers, triage, routine moderation (spam, code of conduct) | Escalated technical questions, roadmap/pricing questions, anything touching an open incident, community strategy |
| Blog ghostwriting | First draft, research, SEO structure, editing passes | Technical accuracy review, final sign-off, voice/POV, any claim about internal architecture or benchmarks |
| Incident status updates | First-draft copy against a pre-approved template, publishing cadence | Root cause framing, ETA numbers, anything requiring engineering judgment — see §4 for the approval gate |

Write this split into the SOW as a RACI, not prose — vendors will quote against ambiguity, and ambiguity is what eats advocate hours later.

## 2. Vendor sourcing approach

Given budget is not a constraint, skip a broad RFP (it burns advocate hours reviewing bids) and go straight to a **targeted shortlist of 4–6 agencies**, sourced from:
- DevRel/community peer referrals (DevRel Collective, CMX, internal network) — ask specifically "who have you outsourced *technical* community moderation or ghostwriting to," not general social agencies.
- Agencies that already publicly list developer-tool or infra clients — a generalist community agency without a technical account team will cost you review hours even if the invoice is cheap.

**Consider splitting into two vendors, not one**, unless a single shop can prove technical fluency in both:
- Community/support agency for Discord L1 (support-ops background, ideally with dev-tool clients).
- Technical content agency for ghostwriting (ex-engineers or specialized dev-content writers, not general marketing copywriters).

Status-page drafting should sit with whichever vendor is faster to reach during an incident — usually the community vendor, since they're already watching the channels where outages surface first. Don't create a third vendor relationship for this alone; it's not enough volume to justify separate onboarding.

**Sourcing timeline (3 weeks to signed pilot):**
- Week 1: shortlist + outreach, send scope doc (§1) and a paid trial task to each (e.g., draft 3 Discord FAQ answers + one blog outline from a real backlog topic).
- Week 2: score trials (§3), reference calls with 2 existing technical clients per finalist — ask specifically about escalation misses and correction rate, not just satisfaction.
- Week 3: contract + onboarding kickoff for the pilot workstream (§6).

## 3. Evaluation scorecard

Score each finalist 1–5 on:

| Criterion | Why it matters here |
|---|---|
| Technical fluency (can they discuss vector search, embeddings, RAG without a script) | L1 answers and blog drafts that misstate the product cost more advocate-repair hours than they save |
| Escalation judgment shown in trial task | The whole point is fewer pages — an agency that escalates everything doesn't reduce hours; one that escalates nothing creates incidents |
| Writing sample matches an advocate's actual voice, not generic B2B copy | Ghostwriting under a real byline fails publicly the moment readers notice the voice shift |
| Incident-comms experience specifically (not just general support) | Status-page work is the highest-risk workstream here — ask for a sample outage postmortem or update they've drafted before |
| Staffing model: dedicated pod vs. shared/rotating agents | Rotating agents relearn your product every time — dedicated pod costs more, saves far more advocate hours over a quarter |
| Turnaround SLA they'll commit to in writing | Not aspirational — contractual |

Weight technical fluency and escalation judgment highest; this is a technical audience, and a generic community-agency playbook (canned responses, high-volume low-context replies) will show within weeks.

## 4. Risk & mitigation by workstream

**Discord L1 + community answers** — lowest risk, most reversible. Main failure mode: agency answers confidently and wrong. Mitigate with a living FAQ/knowledge base the agency drafts *from* and a hard rule — no answer involving roadmap, pricing, security, or "is X a bug" without escalation. Spot-check 5% of resolved threads weekly for the first month.

**Ghostwriting under advocate bylines** — this is standard industry practice (most high-output technical blogs use writer support), but it only holds up if the advocate actually reviews and can defend every claim in a post carrying their name. The risk isn't "ghostwriting is wrong," it's **an advocate's credibility taking a hit for a technical error or a hollow, generic-sounding post published under their name that they didn't meaningfully review.** Mitigate with a non-negotiable gate: advocate does a technical-accuracy + voice pass before publish, even if it's the only hour they spend on that post. If that single review hour isn't protected, you haven't saved advocate time, you've spent it on damage control after the fact, and you've moved the reputational risk onto the advocate personally rather than the agency.

**Status-page updates during outages** — highest risk, least reversible once published, and the reason advocates get paged in the first place is that incident comms need real-time engineering truth (root cause, actual ETA, blast radius). An agency without an engineer in the loop will either stall (defeats the purpose) or publish something wrong (worse than a page). Two viable designs:
- **Pre-approved decision tree**: agency drafts from a fixed template ("we're aware, investigating, next update in X min") that requires zero technical judgment for the first update, with a named on-call *engineering* approver (not necessarily the advocate) required to sign off before any update containing a root cause or ETA. This is what actually removes the advocate from the loop — routing the judgment call to engineering instead of eliminating it.
- **Advocate-authored root cause, agency-published cadence**: advocate drops a one-line technical fact into a shared doc/Slack channel during the incident, agency turns it into public-facing copy and handles the publishing cadence. This still needs a minute of advocate time per incident, but it's a minute, not a page-and-write cycle.
Do not let the agency freelance root-cause or ETA language without one of these gates — that's the one place in this plan where a wrong guess has customer-trust and possibly contractual (SLA) consequences.

## 5. Contract / SOW terms to include

- Named, dedicated staff (not "a team," specific people with technical onboarding logged) — protects against the retraining tax.
- Response-time SLAs per workstream (e.g., Discord first-response <15 min business hours; blog draft turnaround 5 business days; incident update draft <10 min of being briefed).
- Explicit escalation matrix with names/channels on both sides, reviewed and re-signed quarterly.
- IP: Bracknell owns all ghostwritten content outright; no agency portfolio/case-study use without separate written consent (Series B financial details, incident specifics, and unannounced roadmap items should be named explicitly as non-disclosable in the NDA, not left implicit).
- 30-day exit clause with mandatory knowledge-transfer session — don't let institutional knowledge (FAQ macros, incident playbook edits) live only in the agency's head.
- Quarterly QA review built into the contract, not left informal (§8).

## 6. Onboarding & knowledge transfer (minimize advocate hours spent here)

Build once, reuse per vendor:
- **Community FAQ + escalation runbook** — advocates write this once (budget ~4–6 hours total), agency maintains it going forward.
- **Voice/style doc per advocate** — 3–5 past posts annotated for tone, plus a short recorded call, not a live-written brief. One-time cost.
- **Incident comms playbook** — template language, decision tree, and the engineering-approver rotation (§4). This is the highest-leverage document in the whole plan; get it right before go-live, not during the first live outage.

Pilot the Discord workstream first — it's the fastest to validate and lowest-stakes if the agency underperforms — then extend to ghostwriting once the FAQ/voice docs prove out, then incident comms last, only once the engineering-approver rotation is tested on a low-severity incident.

## 7. Governance & success metrics

Track monthly, report to the DevRel lead:
- **Advocate hours reclaimed/week** — the actual KPI here, not cost or output volume.
- Discord first-response time and escalation rate (rising escalation rate = agency losing confidence or scope creeping back).
- Blog cadence (target: 3x current output) and advocate review time per post (should shrink after the first month, not stay flat).
- Incident update turnaround time and count of published updates that required post-hoc correction (target: zero — this is the metric that tells you the approval gate is working).

Re-score the vendor against §3 quarterly, not just at renewal — technical accuracy tends to drift down as staffing rotates unless it's actively checked.