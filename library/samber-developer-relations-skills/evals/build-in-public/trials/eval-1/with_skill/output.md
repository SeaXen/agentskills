Using **build-in-public** (`samber/developer-relations-skills`) to design Lumenpath's charter — this is the funded-company trap the skill names directly: *"We're Series A/B, CEO wants to publish revenue like Buffer does."* Below is the complete deliverable: the analysis, the redirect, and the filled charter, ready to bring to your CEO Friday.

---

# The problem with the brief as given

Three of the four things your CEO asked for don't survive contact with reality, and one is closer than it looks. Before building anything, run this past him — it's the whole plan in one paragraph:

**Buffer's model doesn't transfer to Lumenpath.** Buffer is bootstrapped. It owns its revenue and answers to nobody but its customers. Lumenpath is Series B with two institutional leads. Standard investor-rights agreements grant those investors information rights and impose confidentiality on company financials — which makes live ARR and NRR a **legal question before a marketing one**. The one documented venture-backed exception (Gumroad's Sahil Lavingia) followed an explicit strategic pivot away from growth-at-all-costs and a board that signed off on it. That's a precedent to renegotiate toward, not a template to copy.

**Payments infrastructure makes this worse, not neutral.** Your buyer is a B2B evaluator — a CTO, risk officer, or procurement lead deciding whether to route payment flows through you — who needs to convince an internal approver. That buyer wants evidence of release cadence, security handling, incident response, and compliance posture. A small, honest ARR number sitting next to Stripe or Adyen doesn't read as transparency to that buyer — it reads as a vendor-risk flag. You'd be handing procurement a reason to say no, in your own marketing copy. NRR is worse: for a payments company, churn data is a direct signal about platform stability that a banking partner or acquiring bank relationship manager would notice.

**The salary band table is not blocked the same way — it's a different kind of work.** Buffer's model works because it's a *published formula* (level × location × role) applied to roles, not individual comp disclosure. That's legitimately buildable. But it needs People/Comp-team ownership, legal sign-off, and — this is the part that gets missed — enough headcount per level that publishing a band doesn't back out one person's actual salary. Check your levels: if "Staff Engineer" has one person in it today, publishing that band publishes their salary.

So: two of three asks are gated by people who aren't in this conversation yet (General Counsel, your CFO, your board). Don't spend the week building a dashboard. Spend it getting the right no's and yes's on record.

---

# What's actually going on: three practices, one label

Your CEO is asking for "an open page" but the underlying want is almost certainly one of: category credibility, a hiring signal, or investor-facing polish after closing $34M. None of those require live financials. Naming the real goal now saves you from building the wrong artifact and then having to walk it back — which, per the record below, is its own public event, more damaging than never publishing.

---

# What actually happened when funded companies tried this

Relevant precedent, not hypothetical caution:

- **Buffer** — bootstrapped, never raised the kind of round you just closed, still hasn't reversed. The reason the model holds for them is the reason it doesn't transfer to you.
- **Ghost** — publishes a live ARR feed, but frames it as accountability for a **non-profit**. Different governance, different stakeholders, not a comparable structure.
- **Plausible** — the useful counter-example for your CEO specifically: radically transparent about *how the product works* (fully open-source, auditable code), deliberately reticent about *how much it makes* (milestone disclosure only, no live dashboard). Trust built through auditability, not a revenue feed. This is the closer model for a security-sensitive B2B product.
- **The 2022–2024 reversal wave** — Jon Yongfook, Danny Postma, Pieter Levels, Tony Dinh, Damon Chen all built live revenue dashboards and then pulled them, citing stress, competitive exposure, and — for Chen specifically — the exact situation you're in: *"once other people are on the team, it's no longer my personal milestone."* At Series B with a full team, that condition is already true on day one. Silence after disclosure reads as bad news. Reversal is a second public event. Starting narrow avoids ever needing one.

*(Reference positions verified 2026-08-26 in the skill's source material — confirm each is still live before citing externally, since a company that's gone dark on this makes the opposite point.)*

---

# The redirect: what to actually propose

Give your CEO the outcome he wants — category credibility, buyer trust, hiring pull — through the version of transparency Lumenpath can sustain through a bad quarter and never has to retract.

## Recommended rung: 1–3, plus a payments-specific rung 4, explicitly excluding rung 5 financials for now

| Publish | Why it lands for a payments-infra buyer |
|---|---|
| **Release notes / shipping log** | Proof of active development — the first thing a technical evaluator checks. |
| **Architecture & decision posts** | "Why we built X this way" is what convinces a risk-averse buyer's engineering team you understand the problem space. |
| **Postmortems on real incidents** | For payments infra, this is the highest-trust artifact you can publish, full stop — it's literally what procurement asks for in security questionnaires anyway. |
| **Operational metrics**: uptime, incident response time, median support response, compliance status (PCI DSS, SOC 2, relevant licensure) | This *is* the Buffer-style trust signal, correctly aimed at your actual reader. It does the job ARR was supposed to do, without the legal gate. |
| **Culture, hiring, engineering process** | Buffer's open salary/culture content works for employer branding regardless of company stage. This part of the brief is genuinely available to you today. |

## Explicitly excluded for now: live ARR, live NRR

Not "no." Route it through counsel and your board first. If they clear a narrower version — a milestone ("crossed $X in processing volume," announced once, tied to the funding news) rather than a live feed — that's compatible with this charter. A live dashboard is not, for a company with institutional leads on the cap table, without that sign-off existing in writing.

## Salary bands: yes, narrower than "every engineering level," gated on two checks

1. **Legal/People sign-off** on the formula and what it discloses.
2. **Minimum headcount per published band** (recommend: don't publish any band with fewer than 3–4 people in it, to prevent back-calculating an individual's pay). Collapse thin bands into a wider range, or hold them out until headcount grows.

This ships a real, Buffer-style artifact — a leveling framework with banded ranges — without either legal exposure or a colleague finding their own salary reverse-engineered from a table with an `n=1` row.

---

# Stop condition — write this before the first post, not after

Even for the narrowed set (operational metrics, not financials), pre-commit to when it ends:

1. A larger competitor starts using the published numbers to make Lumenpath look small.
2. Publication measurably raises competitive-intelligence or clone risk.
3. The metric stops being informative and starts reading as marketing.
4. Ownership of the practice shifts and it's no longer anyone's personal accountability — the moment metrics become "corporate," they get corporate scrutiny.

What stays published when a metric stops: the changelog and the postmortem archive don't retire. Only the live feed does, announced, not silenced.

---

# Boundaries — Lumenpath-specific

**❌ Never publish:**
- Unpatched vulnerabilities, in any form — coordinated disclosure only; post-fix, say plainly "this release contains a security fix."
- Named customer data, logos, or per-account volume without written consent — payments infra sees more sensitive customer data than most SaaS; treat this as stricter than default, not equal to it.
- Individual employee salaries, performance, or departures.
- Live ARR, NRR, transaction volume, or anything a reasonable reader would treat as material non-public information — route through counsel given the institutional cap table, every time, no exceptions until that changes in writing.
- Anything about a specific banking or processing partner's architecture, terms, or unreleased features.

**⚠️ Grey zone — decide once, record it, don't re-litigate per post:**
- Roadmap dates: direction and sequencing in public, dates only for work already shipping (Osborne effect — a payments company announcing a successor product risks customers deferring integration work on the current one).
- Compliance audit *findings* (as opposed to compliance *status*) — status ("SOC 2 Type II, renewed annually") is a trust signal; findings are not for public consumption.
- Competitive strategy — describe what you built, not why it wins or what's next.

**Four-question pre-publish check**, run on every post including hasty replies: does this expose a security weakness; does it contain third-party data without consent; does it commit Lumenpath to a date or number it doesn't control; would this sentence be a problem quoted alone by a competitor or journalist. Any yes: rewrite or delay.

---

# Cadence, sized to the worst month, not this one

**Release spine** as the backbone — one post per release, material already exists, degrades gracefully when the team is heads-down. Add a **quarterly report** for the rung-4 operational metrics (uptime, response times, compliance status), written from numbers pulled the week before, not the day before.

- Budget: ~90 min per release post, ~3 hours per quarterly report (compliance metrics need sourcing from eng/security, budget accordingly).
- Working baseline: keep total practice under roughly a tenth of your available time. If it creeps past that, cut frequency before cutting depth.
- Pause rule, written now: if two consecutive releases ship without a post, drop to quarterly-only and say so publicly. Announced gaps cost nothing; silent ones read as decline — worse for a payments company, where "are they still maintaining this" is a security question, not just a vibe.

---

# Surfaces

- **Anchor (owned): `lumenpath.com/open`** — but scoped to what's approved: changelog, decisions, postmortems, compliance status, culture/hiring, leveling framework. Not a live financial dashboard, at least not yet.
- **Amplifiers**: LinkedIn (your actual buyer — B2B operators and risk/security evaluators live there, not X/Indie Hackers) for the narrative version of releases and culture posts; a security-focused mailing list or trust-center page if you have compliance-driven prospects; skip X/Twitter-style revenue-flex formats entirely — wrong genre for this audience.
- Repurposing loop: every artifact starts as a repository record (release notes, ADR, postmortem, compliance renewal doc) and gets a short post pointing back to it. One source of truth, corrected in one place.

---

# Downside plan

- **Support load outgrows capacity**: publish scope and response-time targets where readers land (README, `/open` page itself), route feature requests to a public board, not sales DMs.
- **A post lands badly**: answer the strongest objection once, in public, at the same prominence as the original post. Don't relitigate in replies.
- **Bad news** (an incident, a missed compliance renewal): publish it yourselves, first — impact to the reader, then cause, then the systemic fix. For payments infra, a leaked incident you didn't disclose first is categorically worse than the incident itself.

---

# Measurement — tied to your actual goal, not follower count

| Goal | Signal that it's working | Ignore |
|---|---|---|
| Company adoption (your primary reader) | Inbound evaluations, security/compliance questions referencing the page, named deployments citing it in procurement | Reach, impressions |
| Hiring / credibility | Engineering candidates citing specific posts, inbound from the leveling framework | Follower count |

Review quarterly — this compounds too slowly to read week to week. If cadence is met and nothing moves for two straight quarters, change the surface or the rung before posting more. If cadence is missed, fix that first.

---

# What to bring your CEO Friday

Don't bring a rejection. Bring a scoped yes with a faster path than the one he asked for:

1. **What ships by end of Q1, no legal gate required**: shipping log + decisions + postmortems live on `/open`, plus an initial operational-metrics quarterly report (uptime, response times, compliance status) — this is the Buffer-style trust page, correctly aimed at a payments-infra buyer instead of a consumer-SaaS one.
2. **What needs sign-off before it can even be scoped**: live ARR/NRR routed to CFO + General Counsel this week, framed as "confirm what our investor-rights agreements actually allow" — not "should we do this," a factual question with a concrete answer. Salary bands routed to People/Comp lead this week, framed as "which levels have enough headcount to publish a band safely."
3. **The one-line reason for the redirect**, if he pushes back: *"Buffer's model works because Buffer owns its numbers outright. We don't, yet — and our buyer cares more about our uptime and compliance posture than our ARR anyway. This version gets us the credibility by Q1; the financial version needs legal clearance we don't have yet and shouldn't promise before we do."*

---

# Filled charter — Lumenpath

```markdown
# Build-in-public charter - Lumenpath

## Goal
Primary: company-adoption credibility for a payments-infra buyer (security,
compliance, engineering maturity). Secondary: engineering hiring signal.
Explicitly not: consumer attention or founder personal brand.

## Context
Funded (Series B, $34M, two institutional leads). Legal and CFO review
required before any financial disclosure - confidentiality obligations
under investor-rights agreements assumed present until confirmed
otherwise. Marketing owns execution; Legal, CFO and People own sign-off
on anything touching financials or compensation.

## Audience
Company adoption (B2B). Reader is a technical or risk evaluator who must
convince an internal approver. Needs evidence of release cadence,
incident handling, and compliance posture - not raw revenue.

## Rung
Rungs 1-3 (shipping log, decisions, failures) plus a payments-specific
rung 4: uptime, incident response time, support response time,
compliance/certification status (PCI DSS, SOC 2, relevant licensure).
Rung 5 (live ARR, NRR) excluded pending Legal/CFO/board review.
Salary bands: narrowed to a published leveling formula, gated on
minimum headcount per band; excluded for any level with fewer than
3-4 people until headcount grows.

## Stop condition
Stop any published metric if: a competitor uses it to make Lumenpath
look small; it measurably raises competitive-intel risk; it stops
informing and starts reading as marketing; or ownership becomes
diffuse enough that no one person is accountable for it. On stopping:
state the reason once, in full, at the same prominence as the original
disclosure. Archive stays up; only the live feed retires.

## Boundaries
Hard blocks: unpatched vulnerabilities, named customer data, individual
employee data, live ARR/NRR/transaction volume, partner-architecture
detail. Grey zones (decided, recorded): roadmap dates - direction only,
dates on shipped work; compliance status yes, audit findings no;
competitive strategy - what, not why it wins.
Pre-publish check: security exposure? third-party data without consent?
commits to a date/number we don't control? bad if quoted alone?

## Cadence
Release spine (one post per release) + quarterly operational-metrics
report. ~90 min per release post, ~3 h per quarterly report.
Under a tenth of team time. Pause rule: two missed release posts in a
row -> drop to quarterly-only, announced publicly.

## Surfaces
Anchor: lumenpath.com/open (changelog, decisions, postmortems,
compliance status, culture/hiring, leveling framework).
Amplifiers: LinkedIn (primary - matches buyer), security/trust-center
page for compliance-driven prospects. No X/Indie-Hackers-style revenue
content - wrong genre for this audience.

## Support plan
Response-time targets published on /open. Feature requests routed to a
public board, not DMs or sales channels.

## Measurement
Quarterly: inbound evaluations and security/compliance questions
referencing the page, named deployments citing it in procurement,
hiring inbound referencing specific posts. Ignore reach and followers.
Review date: end of each fiscal quarter, alongside the operational
metrics report.

## Pause rule
Two consecutive releases with no post -> quarterly-report-only,
announced. Restart, if needed, with one honest catch-up post covering
the gap, then a lower cadence than the one that broke.
```