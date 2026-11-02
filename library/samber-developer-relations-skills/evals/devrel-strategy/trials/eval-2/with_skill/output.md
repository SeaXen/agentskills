## Bottom line

The split and the hiring plan aren't a strategy — they're a copy of a big vendor's org chart applied to 1.3 FTE. Datadog, Grafana, Honeycomb and New Relic fund all four pillars because each pillar already clears the minimum size to do anything; four pillars at 25% of *your* capacity means every pillar sits below the threshold where devrel work starts to compound. That produces exactly the failure mode you should expect: busy, nothing lands, and in six months the CTO asks why the community has no members and the blog has no readers.

Before touching the hiring plan, name why this is funded and which one or two pillars that reason actually points to. Everything below works that out and gives you a charter you can put in front of the CTO instead of the current split.

## Why the current plan fails, specifically

- **Capacity math doesn't support four pillars.** You have 1 FTE plus a 12h/week engineer — 1.3 FTE total, not "two people." A quarter of that per pillar is roughly 0.33 FTE, which doesn't reach even one archetype's minimum viable bet before task-switching overhead is counted.
- **You're at Seed, not Grow or Scale.** One generalist plus a part-time hat is the textbook Seed stage. The Seed-stage rule is one archetype, one bet, finished before a second starts. A plan with four specialists and a reporting structure is shaped for Scale — several teams past where you actually are.
- **The hires have no trigger.** "Four specialists over 12 months" is a calendar, not a response to a constraint. Nothing in what you've described says *why* month 3 needs a community manager rather than month 9, or at all.
- **No driver is named.** "Look like the big observability vendors" is a shape borrowed from competitors, not a reason a CFO will defend. Every one of your four pillars will score identically against it, so effort will drift toward whoever on the team argues loudest.
- **Context worth having before you argue this internally:** across 310 DevRel practitioners (State of DevRel 2024, DevRel.Agency), 2–5 people is the most common team size (35.2%), 69% of teams are under ten, and solo practitioners are 18.2%. You're not undersized for the category — you're mis-shaped for it.

## What's missing before any pillar mix is legitimate

I don't have your CORE data, real funnel numbers, or the CTO's own words for why this is funded — so I've built the charter below on stated assumptions and flagged the ones that need real answers. Don't let the CTO sign off on the pillar mix until the "Open questions" section is closed.

**Position (assumed, confirm before locking):**
Halvard sells an observability agent — infrastructure a developer installs, not a library they import. At $9M ARR that's very likely a company-adoption motion: an agent that touches production infra almost always needs a security/procurement sign-off above the engineer who tries it. Community: no stated venue of your own — assume support currently lands in tickets or a shared Slack with customers, not a public forum. Organization: two people, no specialization yet, CTO is the sponsor and the one asking for the big-vendor shape. Relationships: you're competing for evaluation attention against vendors (Datadog, Grafana, Honeycomb, New Relic, Elastic) whose devrel machines are 10–50x your headcount — you cannot out-produce them, only out-focus them. Ecosystem: developers likely find you mid-evaluation (comparison searches, an incumbent's pain point) rather than by browsing.

**Driver (guessed, needs the CTO's actual words):**
The stated ask — "look like the big vendors" — is a benchmark, not a driver; it's not on Revell's list of seven funded reasons. My best read of what's actually driving this, given an infra agent at $9M ARR: **sales enablement** (technical evaluators need PoC and security material to move deals) as primary, **developer adoption** (self-serve trial, if one exists) as secondary. Confirm this with the CTO directly — ask what they'd tell a board member this program is *for*, in one sentence. If the honest answer is "so we look credible like Datadog," that's employer brand or optics, and it funds a completely different, much smaller plan than four specialists.

**Goals (hypotheses — no real drop-off data behind these yet):**
- Primary / revenue: evaluations that reach a technical decision (journey step: evaluation) — hypothesis: evaluators today get ad hoc engineer time instead of a repeatable PoC kit, so cycles stall or drag. Needs validating against real deal data.
- Primary / activation: trial or PoC installs that reach a first working signal (journey step: evaluation/commitment boundary).
- Secondary / product: evaluator objections and PoC blockers routed to the roadmap with a named owner — cheap, and it keeps the CTO's "input from the field" instinct served without funding a pillar for it.

**Audience:**
Primary this horizon: the platform/SRE engineer running the evaluation, inside a company-adoption motion where a security or eng-leadership approver ultimately signs. Not served yet: pure individual bottom-up adoption (unless a free tier exists — confirm), and enterprise-grade compliance packages beyond a baseline security/licensing answer set.

## Recommended shape

**Archetype: evaluation-support**, primary — enablement heavy, advocacy medium (pre-sales facing), marketing and community light. This is the archetype built for exactly your funding hypothesis (sales enablement, company adoption) and it fits your real capacity: roughly a quarter of one person's time per bet, artefacts that outlive the program, fully reversible.

**Pillar mix:** enablement 60%, advocacy 25%, marketing 10% (maintenance only — reuse what enablement produces, no new content engine), community 5% (token — answer where developers already are, own no venue). Two pillars funded above token level, which is the ceiling at Seed stage. Marketing and community are the two the CTO wants "properly resourced" first — they're exactly the two with no signal behind them yet.

**Capacity:** commit at most 70% of your 1.3 FTE to these bets (~0.9 FTE). The rest absorbs support requests, the CTO's asks, and the unplanned — a plan that commits 100% breaks the first week something urgent lands.

## Staffing — replace the four-hire calendar with a trigger

Stay Seed. Finish the evaluation-support bets below with current capacity before adding anyone. Point the backend engineer's 12h/week at building and maintaining the PoC kit and integration samples — engineering time, not a fifth pillar.

**Next hire, trigger-based, not calendar-based:** a technical/pre-sales-adjacent content person, when PoC or security-answer requests from sales back up past a two-week turnaround for two consecutive months, or once bets 1–2 below prove the archetype moves the evaluation-completion signal. That's your one hire this horizon — not four in parallel.

Advocacy, marketing and community hires wait until the pillar ahead of them is the actual bottleneck, or until a real signal names the driver for them (e.g., a measured churn-to-competitor pattern would justify promoting community-first later — nothing you've described establishes that yet). Reporting structure for a team that doesn't exist yet is premature; design it once the first hire is validated, not before.

## Build vs buy for the near-term bets

Reference architectures, PoC kits, security/licensing answers, quickstart: build in-house — these are judgment calls about what the agent can and can't do, and a developer discovering they were vendor-written on a security answer would rightly stop trusting the rest. No agency this horizon: the six-month pipeline setup doesn't fit inside a "prove the archetype works" window, and there's no budget line for one described. No community-sourced content: no density to source it from yet.

## Refused this horizon

- No community venue of our own — no retention or churn signal argues for it yet; an empty venue is worse evidence than no venue.
- No conference sponsorship or booth spend — unproven that evaluators discover Halvard that way versus search or sales-led outreach; it costs more than the two enablement bets combined.
- No dedicated developer-marketing hire — no content engine exists to scale yet; hiring for volume before an outline/review loop exists just produces unreviewed output.
- No four parallel pillar hires on a fixed 12-month calendar — hires are trigger-based.
- No attempt to replicate a big observability vendor's devrel shape — their pillar mix presupposes leverage programs and brand recognition you don't have yet. (This is the one the CTO explicitly wanted — name it as refused, don't let it re-enter by default next quarter.)

## Draft charter

```markdown
# DevRel charter: Halvard Systems, next 2 quarters

## Position
Observability agent, ~$9M ARR, company-adoption motion assumed (agent needs
security/procurement sign-off above the engineer who trials it — confirm).
Community: no owned venue; support assumed to run through tickets/shared
Slack with customers. Organization: 1 FTE (you) + 0.3 FTE borrowed backend
engineer, no specialization yet; CTO sponsors and wants big-vendor parity.
Relationships: competing for evaluation attention against Datadog, Grafana,
Honeycomb, New Relic — headcount parity with them is not achievable or
necessary. Ecosystem: developers likely arrive mid-evaluation, not by
browsing. Lifecycle stage: seed.

## Driver
Best-guess primary: sales enablement (technical evaluators need repeatable
PoC/security material). Secondary: developer adoption. Owner: CTO — confirm
in his own words before locking; "look like the big vendors" is a shape, not
a reason he can defend at a board review.

## Goals
Primary: revenue - evaluations reaching a technical decision (journey step:
evaluation). Hypothesis, not yet measured.
Primary: activation - PoC/trial installs reaching a first working signal
(journey step: evaluation/commitment boundary). Hypothesis, not yet measured.
Secondary: product - evaluator objections routed to roadmap with a named
owner.

## Audience
Primary: platform/SRE engineer running the evaluation, inside a
company-adoption motion. Not served this horizon: pure individual bottom-up
trial (unless a free tier exists - confirm), deep enterprise compliance
packages beyond a baseline security/licensing answer set.

## Pillar mix
Enablement 60%, advocacy 25%, marketing 10% (maintenance only), community 5%
(token). Marketing and community are deliberately starved: no signal yet
justifies funding either past token level, however much the CTO wants the
shape to look symmetric.

## Bets
1. PoC kit with a scoped success definition for the top deployment shape.
   Goal: revenue. Owner: you. Signal: evaluations reaching a technical
   decision. Review: week 10.
2. Security/licensing/compliance answer set (agent permissions, data
   handling, deployment footprint), written once. Goal: activation of the
   evaluation stage. Owner: you, engineering reviews. Signal: time from
   first technical contact to signed-off security review. Review: week 8.
3. Ten-minute quickstart plus one tested integration sample for the two
   stacks evaluators actually run. Goal: activation. Owner: backend engineer
   (12h/week), you review. Signal: share of trial installs reaching a first
   data point. Review: week 8.
4. Migration guide from the incumbent named most often in lost or slow
   deals. Goal: revenue. Owner: you, sales gives input. Signal: evaluations
   citing the guide, sales-reported objection reduction. Review: week 12.

## Build vs buy
Bets 1, 2, 4: in-house. Reviewer: you (bet 2 also reviewed by engineering).
Red line - these are judgment calls about what the agent can and can't do.
Bet 3: in-house, engineer builds, you review. No agency or community-sourced
work this horizon - no pipeline budget, no density to source from.

## Staffing
Stage: seed, one generalist plus a 0.3 FTE borrowed engineer. Next hire:
technical/pre-sales content person, triggered when PoC or security-answer
requests back up past two weeks' turnaround for two consecutive months, or
once bets 1-2 move the evaluation-completion signal. Not hiring for
advocacy, marketing or community this horizon - no queue and no signal
names them yet. Reporting structure: not designed until the first hire is
validated.

## Refused
- No community venue of our own this horizon - no retention signal argues
  for it.
- No conference sponsorship or booth spend this horizon - unproven as a
  discovery channel here, and it costs more than bets 1+2 combined.
- No dedicated developer-marketing hire this horizon - no content engine
  exists yet to scale.
- No four parallel pillar hires on a fixed calendar - hires are
  trigger-based.
- No attempt to replicate a large vendor's devrel shape - their mix assumes
  leverage programs and brand we don't have yet. (The CTO wanted this one.)

## Open questions
- What single reason would the CTO name first if asked why this is funded?
  Owner: CTO, before this charter locks - nothing above is safe until this
  is real, not guessed.
- Does Halvard have a self-serve/free trial path, or is every evaluation
  sales-assisted? Owner: you + sales lead, decides the audience path.
- What actually happens today when a prospect evaluates the agent? Owner:
  you, by talking to the last five evaluators directly - decides bet 1's
  real scope.
- Does the $9M ARR run through few large deals or many small ones? Owner:
  you + finance - decides whether named production references are a
  realistic near-term bet.
- Is there a churn signal tied to lack of community, or is that just an
  assumption riding on the CTO's ask? Owner: CTO/CS - the only thing that
  would justify promoting community-first later.
- Who owns the devrel budget number, and does it include salaries? Owner:
  CTO/finance, before the next planning cycle.
- What's the real deadline behind this - a board meeting, a renewal, a
  competitive loss? Owner: CTO - sets whether this is a one-quarter proof
  or a compounding bet.

## Exec narrative
We are funded to make technical evaluations close faster and more of them
reach a decision. Right now evaluators get ad hoc engineer time instead of
a repeatable kit, and we don't yet know where that costs us deals. This
half we build the PoC kit, the security answer set, and the quickstart that
lets an evaluator self-serve the first result. We are not building a
community or a content engine yet, because neither one has a problem behind
it today. By the end of the half you should see more evaluations reaching a
technical decision, and a documented answer to what a fully resourced
devrel team should look like next.

## Review
Re-decision at the end of the half. Early re-decision if the funding driver
turns out to be something other than sales enablement, or if bet 1's signal
doesn't move by week 10.
```

## Quality gate

- Driver: **open** — best guess stated, needs the CTO's own words.
- Goals: **open** — each is pinned to a journey step but rests on hypotheses, not measured drop-off. Close this before treating the charter as final.
- Bets: **pass** structurally (owner, signal, review date on each) — signals need real baselines once open questions close.
- Refused list: **pass** — non-empty, includes the thing the CTO actually wanted.
- Open questions: **pass** — seven listed, none papered over.
- Credibility surfaces: **pass** — nothing on a red-line surface (security claims, technical trade-offs) is outsourced.
- Exec narrative: **pass** — five sentences, no devrel jargon.
- Numeric baselines: two pillars funded above token level, four bets (within the 3–5 range), ~70% capacity committed, three goals (two primary, one secondary) — all applied as stated, none moved without reason.