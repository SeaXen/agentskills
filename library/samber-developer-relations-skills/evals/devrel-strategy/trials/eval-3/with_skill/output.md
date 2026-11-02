Using the **devrel-strategy** skill (`samber/developer-relations-skills@devrel-strategy`) to build Quillard's charter. I read the SKILL.md plus its three references (`program-archetypes.md`, `build-vs-buy.md`, `charter-example.md`) in full before writing this.

Since this needs to land as one complete deliverable rather than an interactive interview, I answered the Interview questions myself from what's given and marked every assumption as an **Open question** below rather than asserting it as fact — that's the charter's own honesty rule, not a shortcut I invented.

**The one call that matters most:** the agency-for-15-articles plan doesn't survive contact with your own deadline. The skill's own rule: *"A first result due this quarter deletes agency outright, because six months of pipeline setup does not fit inside that window however much budget it has."* Ten weeks isn't a quarter — it's less. And the funnel problem you described (80% of accounts never run a second build) isn't an awareness problem that more articles fix — it's a leak, and *"reach into a leaking funnel spends audience that does not come back."* Below is the redirected version: same instinct (get technical content out fast, without writing it all yourself), same rough content volume, wrong target abandoned for the one your own numbers point at.

---

```markdown
# DevRel charter: Quillard, Q4 (10-week board-review sprint)

## Position

CORE, written from what's known plus named gaps.
Community: unknown in depth. Signups are healthy, so acquisition isn't the
constraint — but no venue, forum, or channel is described, and no engagement
level is stated. Not assumed either way; see Open questions.
Organization: one person owns DevRel, full stop, reporting close enough to
the CEO that the CEO personally decides its fate at a board meeting — typical
of a company small enough that there's no layer between the program and its
funder. What's been tried before, and why it didn't move the second-build
number, is not stated. That gap matters: repeating a failed play blind burns
the one shot before the board meets.
Relationships: Quillard sits in a technical, infrastructure-adjacent category
(build/CI acceleration) developers evaluate by whether it actually works, not
by marketing volume — competitors and alternatives exist in this space, but
none are named, so none are assumed here.
Ecosystem: developers reach build-cache problems by hitting a slow build or a
cache miss, not by browsing content — the ecosystem note in the archetype
reference ("developers discover by searching an error message") applies
directly, which is part of why Bet 5 below is shaped the way it is.
Lifecycle stage: starting. Not because the product is new, but because this
is the first time the program has been asked to prove itself in a single,
existential window.

## Driver

Primary: developer adoption — proof that healthy signups turn into real,
repeated usage. Owner: CEO, who funds the role and is the one who decides at
the Q4 board meeting whether it continues.
Secondary: developer enablement — the actual work needed to move that number
is removing onboarding and integration friction, not reach.
This pairing is not a guess: the enablement-first archetype is defined for
exactly this situation — "developer enablement, developer adoption after a
signup spike that does not convert."

## Goals

Primary: activation — about 80% of new accounts never run a second build
(journey step: evaluation). This is the one number given, so it's the one
goal built on evidence rather than preference.
Secondary: product — route the root causes found while fixing activation
(likely partly a product/DX gap, not only a documentation gap) into the
backlog with a named engineering owner (journey step: evaluation).
Retention (do activated accounts keep building against the cache in the
following weeks?) is a real next question, but there's no baseline for it
yet — instrumenting one is part of Bet 1, not a goal claimed today without a
number behind it.

## Audience

Primary path: individual-developer adoption. A developer signs up, wires the
cache into their own CI pipeline, and decides alone whether it earns a
second run — nothing in what's given points to a manager or approver in this
loop.
Segment served first: developers who already got through signup and one
build, and stalled before a second — not new-visitor acquisition, and not
yet the enterprise/platform-team evaluation motion.
Not served this horizon: company-adoption buyers (security/procurement
review, reference architectures). No evidence this motion exists yet; worth
a two-week check, not a build.

## Pillar mix

Enablement 70%, advocacy 20%, marketing 10% (token), community 0%.
Enablement is funded because the observed problem is a signup spike that
doesn't convert — the exact fit for enablement-first. Advocacy is the same
person's own diagnostic/troubleshooting-facing work, not a separate hire.
Marketing stays token: the two content bets below (2 and 5) are enablement
content that happens to be public, not an awareness campaign. Community
stays at zero — no evidence of density, and it's a standing job this
10-week, solo-capacity program can't absorb without starving activation.
(Team-size context: solo practitioners are 18.2% of programs surveyed in
*State of Developer Relations 2024*, DevRel.Agency, 310 respondents — a
one-pillar-heavy, mostly-token-elsewhere mix is normal at this size, not a
compromise.)

## Bets

1. Segment the activation funnel — which CI system, language, plan tier, or
   first-error type concentrates the drop-off, instead of treating it as one
   flat number.
   Goal: activation. Owner: DevRel (with eng/data support). Signal: a written
   report naming the top 2-3 concentrated failure points, plus a first
   retention baseline for accounts that do reach a second build.
   Review: week 2.
2. Ship troubleshooting/diagnostic pages for the failure modes Bet 1 finds —
   "why isn't my cache hitting," CI-specific fixes — outlined and reviewed
   by DevRel, drafted with contracted writers.
   Goal: activation. Owner: DevRel, 1-2 contracted technical writers drafting.
   Signal: share of new accounts reaching a second, cache-hitting build
   within 7 days of signup — the direct inverse of the "1 in 5" number.
   Review: week 6, rolled up at week 10.
3. Rebuild CI-specific quickstarts and reference configs for the top 3-4 CI
   systems actually in use among current signups, targeting a first cache
   hit in under a stated number of minutes.
   Goal: activation. Owner: DevRel + one contracted DX engineer.
   Signal: time-to-first-cache-hit for new signups.
   Review: week 8.
4. Route every friction point found in Bets 1-3 into the product backlog
   with a named engineering owner and public follow-through (a changelog
   note when one ships).
   Goal: product (secondary). Owner: DevRel surfaces, a named eng lead
   accepts. Signal: count of shipped fixes traceable to this work.
   Review: week 10.
5. A small set of narrowly-scoped technical pieces addressing the exact
   error-message searches developers already run when a second build fails
   — not broad awareness content, the same audience Bet 2 already targets,
   found through search instead of the product.
   Goal: activation (with incidental awareness inside the same segment).
   Owner: DevRel outlines and reviews, contracted writers draft.
   Signal: organic arrivals on these specific pages, and their downstream
   second-build rate.
   Review: week 8.

Bets 2 and 5 together land somewhere around twelve to sixteen published
pieces this quarter — close to the fifteen originally wanted, just retargeted
from broad awareness to the exact leak the numbers show, and resourced by
contractors instead of an agency retainer.

## Build vs buy

1. instrumentation | in-house (DevRel + eng/data, contract a data contractor
   only if no support exists) | latency: days | setup: none | reviewer: DevRel
   + eng data owner | if it stops: funnel visibility reverts to the flat "1 in
   5," no segmented view to act on.
2. troubleshooting pages | in-house outline, contracted drafting | latency:
   ~1 week/piece | setup: one style brief | reviewer: DevRel (red line:
   technical trade-off calls and "what the product can't do" stay with
   DevRel) | if it stops: pages already published stay useful, nothing decays.
3. CI quickstarts/reference configs | in-house build, one contracted DX
   engineer for breadth across CI systems | latency: 2-3 weeks | setup: test
   environment per CI system | reviewer: DevRel + eng | if it stops: configs
   already shipped keep working until a CI provider changes something.
4. friction routing | in-house only, no vendor | latency: ongoing | setup:
   none | reviewer: named eng lead | if it stops: friction still surfaces,
   just stops reaching product.
5. activation-adjacent articles | in-house outline, contracted drafting |
   latency: ~1 week/piece | setup: shared with bet 2's brief | reviewer:
   DevRel | if it stops: published pieces stay live, nothing decays.

No bet uses an agency. The documented agency pattern (Matt Jarvis, Snyk,
developerrelations.com) — advocate outlines, agency fleshes out, "we needed
to industrialise this process" — is the right shape for volume once a
program has runway to absorb roughly six months of pipeline setup before the
first piece ships. Quillard doesn't have that runway this horizon. Revisit it
next horizon if the program survives the board review.

## Staffing

Stage: seed, one generalist. No hire this horizon — the $60k is program
budget only, and headcount is literally the thing under review; asking for
more of it before proving the case undercuts the case.
Next capability, if the program survives: a technical writer or DX engineer,
triggered when contracted-writer review load exceeds what DevRel can turn
around in a week for two consecutive weeks — the point where this becomes a
standing job instead of a 10-week sprint.

## Illustrative budget split ($60k program budget — self-set, not a rule)

- Bet 1 (instrumentation): $5k
- Bet 2 (troubleshooting pages, contracted writers): $18k
- Bet 3 (CI quickstarts/reference configs, contracted DX engineer): $12k
- Bet 4 (friction routing): $0 — review time only, no direct spend
- Bet 5 (activation-adjacent articles, contracted writers): $12k
- Contingency / unplanned load: $13k (~22%)

The 22% buffer mirrors this skill's own time-capacity baseline ("at most 70%
of declared capacity is committed") applied to budget instead of hours — a
deliberate adaptation, stated as such rather than presented as a sourced rule.

## Refused

- No agency retainer this horizon. This is the thing most wanted going in —
  refused because six months of pipeline setup cannot produce anything
  before the board meets, at any budget.
- No broad top-of-funnel/awareness content program. The audience isn't the
  constraint; the funnel already loses 80% between first and second build.
  More visitors enter the same leak.
- No owned community venue (Discord, forum) this horizon. No evidence of
  conversational density, and it's a standing job a solo, 10-week-constrained
  program can't run alongside the activation work.
- No conference or event spend this horizon. It doesn't move the
  second-build number and draws down budget the enablement bets need.
  (Events have historically dominated DevRel spend — 41.1% in the same
  survey — but that figure comes from 47 respondents whose answers sum to
  104.5%; cited here as history, not as a reason to fund one now.)
- No new headcount request this horizon, even though the instinct under
  pressure is to ask for help. Requesting more headcount while headcount is
  what's being evaluated weakens the exact case being made.

## Open questions

- Is the 80% drop-off concentrated in one CI system, language, or plan tier,
  or spread evenly? Not yet known. Owner: DevRel + eng/data, by week 2 (Bet
  1); it decides which quickstart ships first.
- Does "run a second build" mean a second attempt, or a second build that
  actually hits the cache? The two numbers could differ a lot, and the board
  metric needs the precise definition, not the loose one. Owner: DevRel + eng,
  before instrumentation starts.
- What's been tried before to fix this, and why didn't it work? Not stated.
  Owner: DevRel, by week 1 — repeating a dead approach costs a week this
  program doesn't have.
- Does the $60k program budget already assume any tooling/analytics spend
  committed elsewhere? Not stated. Owner: DevRel, confirm with finance/CEO
  before locking the split above.
- Is there already a hidden company-adoption motion (a platform team
  evaluating Quillard for rollout) inside current signups? Not stated. Owner:
  DevRel, by week 2, from a quick source review of existing accounts.
  (Budget-ownership questions like this one are worth asking even when they
  feel administrative — in the same survey, 33.5% of practitioners couldn't
  state their program's budget at all, and 60% of stated budgets exclude
  salary. Confirming what the $60k actually covers protects the whole plan.)

## Exec narrative

Signups are healthy, but four out of five new accounts never come back for a
second build — we're being tried once, not adopted. This quarter, the DevRel
budget goes into finding exactly where that drop happens and fixing the
specific friction that causes it: clearer setup guides, faster fixes for the
errors that block a second run, and diagnostics that show a developer their
cache is actually working. We are not spending on a content agency or
broad-awareness articles this quarter, because sending more visitors into the
same leak wouldn't raise usage, only the bill. By the board meeting, we'll
show the share of new accounts reaching a second build moving up from its
current one-in-five, plus the specific product and doc fixes that moved it.
If that number isn't moving, we'll know by week 5, not after the quarter closes.

## Review

Checkpoints at weeks 2, 4, 6, and 8, with the board meeting at week 10 as the
hard review. Early re-decision if the funding sponsor (the CEO) changes, or
if the activation signal hasn't moved at all by week 5 — in that case,
collapse remaining budget and effort onto whichever single bet is showing
the clearest early signal, rather than continuing to spread across five.
```

---

## Quality gate

Structural (non-negotiable):

- Driver: one named reason (developer adoption), one named owner (CEO), phrased in the funder's own terms. ✅
- Goals: activation is pinned to a journey step and an observed drop-off (80%, not a preference); product is pinned to the same evidence from a different angle. ✅
- Every bet traces to one primary goal, has one owner, one signal, one review date. ✅
- Refused list is non-empty and includes the thing actually wanted (the agency). ✅
- Open questions are written down, not resolved by assumption — five of them, each with an owner and a date. ✅
- Nothing on a credibility surface is outsourced: every troubleshooting/technical claim is DevRel-outlined and DevRel-reviewed; contractors draft, they don't decide. ✅
- Exec narrative: five sentences, no devrel jargon, repeatable by someone who wasn't in this conversation. ✅

Numeric baselines, self-set by this skill, and where I moved them:

- Bets: 5, at the top of the allowed 3-5 range — justified because the 10-week window needed the instrumentation bet (1) split out from the content bets (2, 5) instead of folded together.
- Pillars funded above token: 2 (enablement, advocacy), inside the "at most two" ceiling.
- Goals: 2 total (1 primary, 1 secondary), under the ceiling of 3 — I chose not to force a second primary goal (retention) without an observed number behind it, which is a deliberate, stated departure toward the gate's own stricter spirit rather than its letter.
- Capacity buffer: applied the 70%-of-capacity rule to budget instead of hours (22% held as contingency) — an adaptation, not the rule as written, flagged as such above.