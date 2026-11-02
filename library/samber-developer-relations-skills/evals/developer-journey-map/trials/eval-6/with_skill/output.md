# Developer journey map — Quillbore, backend engineers at scale-ups, 2026-09-19

## Scope

- **Segment:** backend engineers at scale-ups (one segment, one map).
- **End state named:** production usage.
- **Stage model:** API and platform five-stage arc — awareness → onboarding → integration → production → advocacy. Carried by the `gtm-developer-ecosystem` skill (beingsmit/technical-product-gtm); its published numbers are one company's anecdotes, never benchmarks. Chosen because its boundaries (first success, first service-repo call, sustained traffic) already sit in your numbers, and its documented terminal stage is *production* — which matches the end state you named.
- **Note on the fifth stage:** the model's own terminal stage is production, not advocacy. Your table carries advocacy past that terminal stage, which the model's own documentation treats as an optional branch off the main line, not a competing priority. That's fine — you own it and want it tracked — but it means advocacy isn't the funded end state of this map, which matters for the leak diagnosis below.
- **Assumptions made to finish this in one pass** (flag if wrong): no procurement/security-review process exists for scale-up accounts, so no buyer lane is modeled; the four percentages you gave are treated as this quarter's real signal values, source unstated.

## Journey

| Stage | Developer's job | Entry trigger | Exit event | Touchpoints | Owner | Friction evidence | Signal |
|---|---|---|---|---|---|---|---|
| Awareness | find something better than the GraphQL stitching we've hand-rolled | search, peer mention, blog/conference reference | opens the quickstart | search results, comparison posts, community threads, repo | *none named* | no evidence yet | not instrumented |
| Onboarding | prove Quillbore can front our schemas from my laptop before I bring it to the team | opens the quickstart | first query served through Quillbore | quickstart, config/schema setup, docs, CLI | docs team | no evidence yet | 47% of quickstart starters reach first success |
| Integration | wire it into a real service, not just a demo | first success reached | gateway called from a service repo within 30 days | SDK/reference docs, service repo, CI, support | product | no evidence yet | 61% of first-success users call from a service repo within 30 days |
| Production | run this in front of real traffic and trust it on call | integrated into a service repo | 14 days of sustained production traffic | dashboards, alerting, runbooks, support | product | no evidence yet | 58% of integrating accounts reach 14-day sustained traffic |
| Advocacy | tell other engineers it was worth switching | sustained production usage reached | a public mention attributable to a production account — *unbounded window, see Gaps* | community, conference CFPs, changelog, social | DevRel (you) | no evidence yet | 3% of production accounts ever mention us publicly |

## Buyer lane

None modeled. No security-review, procurement or licensing-blocker data was given, and "end state = production usage" reads as developer-led rather than committee-approved. State this explicitly rather than leaving it blank: if scale-up deals actually route through a security questionnaire or a budget owner, that's a second lane you're currently not seeing, and accounts could be stalling there invisibly before ever showing up as a Production-stage number.

## Moments

- **First success** — first query served through Quillbore (onboarding's exit). No time-to-complete data was given, so I can't cite a duration; that's a gap worth closing, since "47% get there" and "it takes 40 minutes to get there" are different problems with different fixes.
- **Moment of truth** — the decision to call Quillbore from a real service repo instead of a demo (integration's exit). This is where a team stops evaluating and starts depending on it.
- **Abandonment point** — onboarding, inferred from the largest percentage-point drop on the map (53 points, versus 39 at integration and 42 at production). This is inferred from rates, not from exit interviews — nobody has asked the 53% who leave why yet, so treat this as the leading candidate, not a confirmed finding.

## Leak

**Onboarding.** 47% of quickstart starters reach first success — the worst conversion among the stages that are both instrumented and owned, and the earliest one.

Why not the alternatives:

- **Awareness** is earlier, but it has no owner and isn't instrumented. "Earliest wins" only applies among stages someone can actually move — an unowned recommendation is a wish, not a fix. It's still worth naming as a finding (see Gaps), just not as this quarter's leak.
- **Advocacy**, at 3%, is the worst raw number on the whole map, and I want to be direct about why it's still not the nomination:
  1. It's the latest stage. A late stage only outranks an early owned one when the early stage is unowned, already being fixed, or is itself the funded end state — none of those hold here. Onboarding is owned, not (as far as I know) already in flight, and you named production, not advocacy, as the end state.
  2. Per the stage model's own definition, production is this map's terminal/funded stage. Advocacy sits past it as an optional branch, not the priority line.
  3. Its exit event has no time bound — "ever mentions us," measured against three other stages that all use fixed windows (30 days, 14 days). A lifetime rate compared against period rates will structurally look worst regardless of whether it's actually the leakiest stage. That's a measurement artifact, not yet evidence of a real problem.

## Handoff

- Owner: docs team (owns the quickstart and first-success path).
- Signal to watch: share of quickstart starters reaching first success.
- Re-read date: 2026-12-18 (90 days), and immediately again after any quickstart or docs rewrite.

## Gaps

- **Awareness** has no owner and no signal. This is likely your single biggest unknown, sitting upstream of everything else on the map — cheap to close with a self-reported "how did you hear about us" field or referrer tagging on the docs entry point.
- **Every friction-evidence cell is empty.** No friction log or exit interview has been run. Every "why" in this document — including the abandonment point above and the advocacy read below — is currently a hypothesis wearing the shape of a finding, not evidence.
- **Signal sources are unstated.** Confirm where the four percentages come from and snapshot them into your own store now — none of the systems these numbers typically come from (product analytics, repo traffic endpoints) retain data indefinitely, so backfilling won't be possible later.
- **Advocacy's exit event needs a bound.** Redefine "ever mentions us" to a period rate — e.g., "within 90 days of reaching production" — before the next re-read, or the 3% will keep sinking every quarter purely because the denominator (all-time production accounts) grows faster than the numerator, independent of whether advocacy is actually getting better or worse.
- **Buyer lane unmodeled** — confirm whether scale-up deals ever hit procurement or security review; if so, add the lane before trusting the production number as final.

**Quality gate check:** one exit event per stage (pass) · every stage owned, ≥1 owner outside DevRel (pass — docs, product×2; awareness's missing owner is itself flagged rather than hidden) · signal coverage 4/5 = 80% ≥ 60% (pass) · no friction claim dressed as evidence (pass — all honestly "no evidence yet") · exactly one leak, with owner and re-read date (pass) · inferred/unmeasured stages labelled everywhere they appear (pass) · fits on one page (pass). The map is structurally sound but evidence-thin — treat every non-rate claim in it as provisional until a friction log exists.

---

## Top three things to fix next quarter

The method only lets me nominate one leak — three priorities is none, and nominating three here would repeat the exact mistake the map exists to prevent. So: one fix, plus two structural repairs that don't compete with it for priority but would otherwise waste next quarter's effort.

1. **Run a friction log and 3 abandonment interviews on the onboarding quickstart** (docs team). This *is* the nominated leak. Right now nobody knows which of the 53 points lost are a missing prerequisite, a confusing config step, or something else — without that, any fix is a guess.
2. **Give Awareness an owner and one signal.** It's unowned and unmeasured, directly upstream of the stage you're about to fix. A referrer tag or a "how did you hear about us" field is a day of work and turns your biggest blind spot into next quarter's actual finding instead of a permanent unknown.
3. **Rebound Advocacy's exit event to a fixed window** before spending budget on it. This doesn't fix advocacy — it makes it measurable, which has to happen before any intervention there can be judged to have worked.

## On the advocacy motivation/incentive read

Worth saying plainly before I hand you a plan: reaching for a motivation story here is the specific trap this method warns about — B=MAP only earns trust once a stage has actually cleared the leak diagnosis, and advocacy hasn't, for the three reasons above. I'd also flag that "3% ever mention us publicly" quietly excludes internal Slack shoutouts, hallway mentions at a conference, and anything said before you had a way to see it — that's a visibility gap, not proof people aren't proud to run Quillbore.

If you still want to move on advocacy this quarter — reasonable, since you own the stage and it's demoted rather than deleted — Fogg's own model argues against leading with incentives: *"motivation is unreliable. Luckily, ability is not."* Two cheaper, likelier levers to test before an incentive program:

- **Prompt.** Nothing currently asks a production user to share anything, at the one moment they're most likely to say yes — 14 days of sustained traffic, the same event that already closes the Production stage. Add one nudge there.
- **Ability.** Lower the cost of the act itself: a one-click "built with Quillbore" badge, a case study your team drafts and they approve rather than write from scratch, a pre-written post they can edit.
- **Motivation/incentive** (what you asked for) — the weakest of the three levers per Fogg, so treat it as a third pass, not the opener: public recognition (a "who's running Quillbore in production" page) rather than swag or cash, since this audience already chose to run it in prod — they're not being courted, they're being under-asked.

Run these as hypotheses against 3–5 short interviews with production accounts who've never mentioned you (protocol in the skill's evidence reference) before committing budget to any of them.