## Don't merge the teams yet — you'd be moving the fight, not ending it

Three months of weekly escalations means the actual failure is **no decision-rights charter**, not the org chart. If you fold docs into devrel without fixing that, the same "who owns this page" argument reopens one layer down, just off your desk — and you'll have traded a governance problem for a new, harder-to-reverse one: accuracy risk on your API reference.

### Why a full merge is riskier than it looks

- **API reference correctness depends on proximity to code**, not proximity to marketing. Someone has to catch every breaking change, every new parameter, every deprecated endpoint — that requires being in engineering's sprint, PR review, and release pipeline. Devrel people are usually good at *explaining* the API; they're rarely the ones who'd notice it silently changed.
- **Devrel and docs optimize for different things.** Devrel is graded on activation, reach, engagement. Docs is graded on completeness and accuracy. Put both under one manager with devrel-style KPIs and the "boring" reference-maintenance work quietly loses priority — you won't see it for a quarter or two, then support tickets spike.
- **Your docs lead will likely read this as a demotion** — moving from an engineering reporting line to a marketing one, even if nothing about their job title changes. That's a retention risk you should surface with them directly before deciding, not after.
- **Engineering will still need to be involved** whether or not the reporting line moves. If you don't get your VP Eng's buy-in on how accuracy gets protected post-move, you've only solved your own problem, not the actual one.

### What's actually broken: ownership was never defined by content type

"API reference" and "tutorials" are not the same kind of content and don't need the same owner:

| Content type | Natural owner | Why |
|---|---|---|
| API reference | Docs, tight to engineering | Must track code changes precisely; source-of-truth accuracy beats reach |
| Tutorials / quickstarts / guides | Devrel | Adoption and activation-focused; devrel knows where new users get stuck |
| Conceptual/architecture docs | Docs | Stability and correctness over time |
| Sample apps, cookbooks, migration guides | Devrel, with docs sign-off | Marketing-adjacent but needs technical review |

Most of the three months of escalation is probably arguments over the middle ground (quickstarts that touch API behavior, reference pages that need better prose) — not a genuine both-teams-want-full-ownership standoff.

### Recommendation, in order

**1. Write a one-page content ownership charter — do this in the next two weeks regardless of what else you decide.**
Get the two devrel people and the docs lead in a room, list every actual page/content type currently disputed, and assign a single named owner per type using the split above. Add one line: "disagreements about content type X go to [charter], not to the CMO." This alone likely kills most of the weekly escalations, because right now there's no artifact either side can point to — it's just two people asserting turf, repeatedly, to you.

**2. Only move docs' reporting line if you can protect API reference accuracy with a real SLA.**
If you do proceed with the merge:
- Get your VP Eng to commit, in writing, that engineering will still review/sign off on any PR touching API reference pages, and that the docs team keeps a seat in relevant sprint planning.
- Talk to the docs lead 1:1 first. Explain the "why" (single accountable owner, not a critique of engineering's stewardship). Listen before you decide it's final.
- Move the budget line and update the reporting chart as one clean event, not a slow drift — ambiguity during the transition will reopen the exact argument you're trying to close.
- Set a 90-day checkpoint with two explicit metrics: time-from-API-change-to-doc-update (accuracy, leading indicator of drift) and tutorial/activation metrics (the thing you're presumably trying to improve by owning devrel content end-to-end). If accuracy lag grows, that's your early warning the SLA isn't holding.
- Stand up a recurring (biweekly is enough) sync between the merged devrel/docs org and engineering so the interface stays healthy without needing another round of escalations to fix it later.

**3. If you don't want to run the SLA negotiation with engineering, don't merge.**
Do step 1 only. A clear charter with named ownership and a stated escalation path solves the pain you're actually describing (constant escalations to you) without taking on accuracy risk you don't yet have a way to catch.

### What I'd avoid

- Don't decide this unilaterally and announce it as a fait accompli — you'll get compliance, not buy-in, and the docs lead in particular will disengage.
- Don't use "who's easier for me to manage" as the deciding factor — pick ownership by where the underlying skill and incentive structure actually lives (accuracy → engineering-adjacent, adoption → devrel-adjacent).
- Don't skip the charter even if you do merge. A merged team with undefined internal ownership just relocates the argument.