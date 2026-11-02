# Building your first Developer Advocate hire

Scope note: this is the hiring side of DevRel (`devrel-hiring`), not the candidate-coaching skill — the artefacts below are job posting → interview loop → portfolio scoring, in that order, per the skill's own workflow.

## Starting read — veto this before anything else

**Recommended target: Developer Advocate, product-focused, first (founding) hire, reporting into Engineering.** Reasoning: you're an API company and the request originates from VP Engineering rather than Marketing — that combination points at a developer-enablement + product-input driver, not sales enablement. Reporting line matters beyond org-chart trivia: a role reporting into engineering gets measured on signups/API usage; into marketing, on leads/engagement; into sales, on pipeline (Wesley Faulkner's documented mechanism). Confirm you want the engineering-flavored metric set before publishing — moving this role into Marketing later changes what "success" means, not just who signs off on PTO.

Assumptions I made to produce a complete deliverable in one pass, flagged so you can correct any of them:

| Assumption | Why | If wrong |
|---|---|---|
| Company type: growth-stage (not pre-seed team-of-one) | 60 people implies past the earliest stage | Shrinks scorecard to fewer outcomes, raises breadth weighting |
| GTM motion: product-led (self-serve API signup) | "API company" + engineering-sponsored hire | If sales-led, swap the enablement/product-input driver for sales-enablement and add a sales-facing competency |
| Coding-depth bar: high (ships real SDK samples/PRs, not just talks) | Product-focused sub-role, engineering-sponsored | If you actually want an outreach/content generalist, drop the coding take-home and raise the presentation-round weight |
| Compensation: range unpublished pending your input | Never invent a pay figure or a jurisdiction's transparency law | You must fill this in — see Open questions |
| One-off vs. repeatable: treat as the first of a function that will grow | Reusable scorecard costs little extra now, a lot to redo later | If this is truly a single hire with no planned expansion, you can thin the loop |

---

## Artefact 1 — Role scorecard and job posting

### Scorecard

**Mission:** Cut time-to-first-successful-API-call for self-serve developers and turn developer friction into shipped product fixes — funded as a developer-enablement and product-input driver.

**Outcomes** (ranked, quantified — replace the bracketed placeholders with your real baselines before publishing):

1. Publish a friction log of the candidate's own first-30-days integration experience; name the top 3 blockers to self-serve activation.
2. Cut time-to-first-successful-API-call by **[25%]** within two quarters via shipped docs/SDK fixes (baseline: your current activation funnel).
3. Reduce volume on the top 3 recurring onboarding/support tickets by **[25%]** within two quarters via shipped fixes, evidenced by ticket-tag counts before/after.
4. Ship 2 reference integrations covering your platform's two highest-volume use cases within the first quarter.
5. Deliver a quarterly developer-feedback synthesis to Product; get at least one named, dated roadmap decision changed by it per quarter, starting Q2.
6. Publish 6 technical posts and give 2 talks in year one, establishing external credibility.
7. Grow community-sourced integrations/tutorials from zero to 5 pieces by year-end.

**Competencies** (weighted, product-focused/engineering-sponsored profile):

- API design literacy and sample-code craftsmanship — **high**
- Technical writing — **high**
- Developer-empathy interviewing / friction-log discipline — **high**
- Self-direction — building a function with no incumbent team — **high**
- Cross-functional influence without authority (Product, Support, Engineering) — **medium-high**
- Public speaking / developer-facing communication — **medium**
- Community-building instincts — **low** (secondary for this seat; raise later if you hire a #2)

### Job posting (ready to adapt)

> **Developer Advocate — Founding Hire**
>
> **Why this role exists.** You'll be our first Developer Advocate. Your job: make it fast and obvious for developers to succeed with our API, and carry what you learn from them back into the product. This role reports into Engineering.
>
> **What you'll own in year one:**
> - Ship a public friction log from your own first-30-days integration, naming what blocks new developers today.
> - Cut time-to-first-successful-API-call by [25%] via docs and SDK fixes you ship yourself.
> - Build 2 reference integrations for our highest-volume use cases.
> - Run a quarterly developer-feedback synthesis that changes at least one dated, named roadmap decision per quarter.
> - Publish technical content and speak publicly — 6 posts and 2 talks in year one.
>
> **What you bring:**
> - Recent hands-on developer experience — you can read our API docs and immediately spot what's wrong with them.
> - A public track record: code, writing, or talks we can actually look at (links, not a summary of your LinkedIn).
> - Comfort being the only person doing this job — you'll set the bar, not follow one.
>
> **Resourcing, so this isn't a founding-role-in-name-only:** [$X content/travel budget], reporting line to [VP Engineering], a 12-month goal defined above, and a levelling conversation at 6 and 12 months against a written scorecard — not vague "grow into it."
>
> **Compensation:** [published range] — pending confirmation against your hiring jurisdiction's pay-transparency requirement; do not publish "competitive" with no figure.
>
> **How we hire:** portfolio review → conversation with Engineering → paid work sample → DevRel-opinion round. No unpaid content or code asked of you beyond what you've already published.

### Self-audit (must pass before this goes live)

- [x] **Gatekeeper check** — no impossible-person stack. Requirement is "recent dev background + one public track record," not 8 years of engineering plus OSS plus writing plus events all at once.
- [x] **Pit-trap check** — resourcing, reporting line, and a named 12-month goal are stated explicitly in the posting body, not implied.
- [x] **Off-core-skills check** — nothing about specific frameworks or follower counts; the ask is API literacy and communication.
- [x] **Tactics-vs-outcomes check** — every listed activity (friction log, reference integrations, feedback synthesis, content) traces to a numbered outcome above.
- [ ] **Levelling check** — cannot confirm until you fill in the compensation range; verify the number matches "founding, sets the bar" seniority, not junior pay for senior scope.

---

## Artefact 2 — Interview loop and question bank

4-stage loop (matches the product-focused-advocate default), plus an optional founder/exec round given how visible a first DevRel hire is at 60 people.

| Stage | Format | Purpose | Who's in the room | Paid? |
|---|---|---|---|---|
| 0 | Portfolio evaluation (Artefact 3) | Score shipped public work before asking for anything new | You (async) | n/a |
| 1 | Conversational round, 30 min | Technology fluency, working style, logistics | VP Engineering | — |
| 2 | DevRel-opinion + community/technology round, 45–60 min | Their model of the practice; no memorised right answer | VP Engineering + one senior engineer | — |
| 3 | Paid work sample | "Review a real anonymised support thread, propose the SDK/docs fix" | Async submission + 30 min review call | **Yes — pay for this** |
| 4 (optional) | Founder/exec round, 30 min | Commercial context, culture, visibility of this hire | Founder/CEO | — |

Never request unpaid spec content or code from a candidate who already has a public portfolio — score the existing work instead (Artefact 3) and reserve the paid work sample for candidates whose portfolio is genuinely thin.

### Question bank (2–3 per competency, plus a DevRel-opinion question)

**API design literacy / sample-code craftsmanship**
- Describe your experience integrating with an SDK or API you didn't build — where did it fight you?
- How do you evaluate whether documentation is accurate and current?

**Technical writing**
- Walk me through a piece of content you shipped and what it changed.
- How do you keep a tutorial correct after the product changes underneath it?

**Developer-empathy interviewing / friction-log discipline**
- Tell me about developer feedback you carried into a product decision that shipped — name the change.
- How do you tell the difference between a developer's stated complaint and their actual blocker?

**Self-direction (no incumbent team)**
- What is developer relations for, at a company like ours? *(DevRel-opinion — tests whether they can name a funding driver and pillar mix, not recite a definition.)*
- Describe a program you built from nothing, with no playbook to follow.

**Cross-functional influence**
- How do you align DevRel initiatives with the product roadmap when you have no formal authority over it?
- A major product delay threatens developer trust. What do you do in the first week?

**Public speaking / communication**
- How do you prepare a technical talk for an audience with mixed backgrounds?
- How do you handle a live demo failure or a hostile question mid-talk?

### Scoring mechanics

- Every interviewer scores independently, with a written evidence note per competency, **before** any debrief.
- Combine scores mechanically against the weights above — the debrief calibrates interpretation, it never originates a score. This is a general structured-interview finding, not DevRel-specific, but it transfers directly.
- Never let a self-rating questionnaire gate a candidate alone (you're not running one in this loop, but if you add one later, use it only to steer follow-up questions).

---

## Artefact 3 — Portfolio scoring rubric

Score each signal 0–3: **0** absent · **1** claimed but unevidenced · **2** evidenced · **3** evidenced with a stated outcome.

| # | Signal | What a 3 looks like | Weight for this role |
|---|---|---|---|
| 1 | Public writing | Published posts with a link, on a relevant niche, at least one showing a result | Secondary |
| 2 | Public speaking | Two-plus talks with video/slide links; a lightning talk counts | Secondary |
| 3 | Code in public | Repos a stranger can run, matching your API's surface, with a contribution history | **Primary** |
| 4 | Community evidence | A role held (moderating, organising, mentoring) — not membership | Low |
| 5 | Teaching artefact | A tutorial or learner journey with checkpoints | Secondary |
| 6 | Developer-voice artefact | A published friction log, feedback synthesis, or issue thread showing research reaching a product decision | **Primary** |

**Score bands** (this skill's own working baseline — move them for a stated reason, not a published industry standard):
- **Under 6 total:** candidate needs more shipped work before this loop can fairly evaluate them — route to the paid work sample instead of a portfolio-only decision.
- **6–11:** evaluate the weighted signals (3 and 6 above) directly.
- **12+:** the constraint is fit to your specific API/audience, not evidence volume — spend the conversational rounds probing fit, not re-verifying the portfolio.

**Negative signals — name these explicitly when present, don't just list what's missing:**
- Follower count with no substance behind it.
- No shipped code, no public artefacts at all (disqualifying for this product-focused seat specifically).
- Content that centers the candidate rather than the developers they served.
- Ghostwritten or paywalled content they can't defend in conversation.
- Metrics exaggerated, or dismissed entirely when asked.
- Cannot name a specific developer or team they helped.

**Paid work sample for thin portfolios** (score 3–4): *"Review a real, anonymised support thread and propose the SDK or docs fix."* Score on: root-cause read, fix quality, communication to engineering. Freeze this exact rubric for a quarter — every candidate for this seat gets scored against the same bar, not a re-invented one per interview.

---

## Open questions to resolve before you publish

- **Compensation range and jurisdiction** — confirm your hiring location's pay-transparency requirement before publishing; do not ship "competitive" with no figure.
- **Confirm GTM motion** (product-led assumed) — if actually sales-led, the driver and one competency change.
- **Interviewer-hour budget** — if you have fewer hours available than the 4-stage loop above costs, cut to portfolio evaluation + one conversational round + the paid work sample; drop stages, don't reorder them.
- **Deadline** — no date given; a this-quarter deadline would justify reusing this question bank as-is rather than customizing further.

**Review point:** if no candidate scores 6+ on the portfolio rubric within 6 weeks of the posting going live, that signals a sourcing-channel problem, not a bar problem — API companies' Developer Advocate pool skews toward people already visible in your own product's community (Discord/Slack power users), niche DevRel boards (e.g. devreljob.com), and referrals from the DevRel network, over generic job boards.