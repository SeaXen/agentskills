## Verdict

No. The plan measures whether people *liked* the page, not whether the tutorial did its job or whether it justifies two headcount. All three legs sit at Kirkpatrick Level 1 (reaction). Nothing measures learning (Level 2) or behavior change (Level 3) — and Level 3 is the only thing that answers a board's question.

## Leg by leg

**Completion rate, 40% target.** Drop the target, keep the metric.

- No published completion-rate benchmark exists for developer tutorials. The 40% figure you keep seeing is almost certainly a self-reported activation/signup-funnel number from marketing material — a different population (people finishing a signup flow) doing a different thing (not learning a skill). Importing it as your target is comparing tutorials to funnels.
- The only defensible comparison is this tutorial against its own next revision. You shipped last month, so you have no prior baseline yet — this cohort *becomes* the baseline. Report the raw number to the VP as "our first measured baseline," not "we hit/missed the industry bar."
- Presenting a borrowed number as an external standard is the exact risk this doc-measurement space calls out: it looks authoritative until someone at the board table asks for the source, and then it actively damages the team's credibility at the worst possible moment.
- Free upgrade, same wiring cost: instrument a drop-off event per checkpoint, not just a single completion event. Completion rate alone tells you *whether* people quit; per-checkpoint events tell you *where*. Same instrumentation bill, far more useful output — one dominant abandonment step points at a specific broken step you can fix before the board meeting, not a vague number you can't act on.
- Also free at that point: median completion time vs. your stated estimate. If it's off, that's a second, concrete "we found and fixed this" story for the board deck.

**Thumbs-up/down widget.** Weak, keep only if it's basically free.

- It only hears from people who scrolled to the bottom — exactly the population that already succeeded. It says nothing about the people who bounced, who are the ones costing you completion.
- It doesn't localize to a step, so a bad score gives you no fix to make.
- Per-checkpoint drop-off (above) is a strictly better read for the same order of effort. Don't feature the thumbs widget in the board narrative; a happy-thumbs ratio proves people enjoyed reading, not that the SDK tutorial works.

**Quarterly NPS on docs.** Cut it from this plan entirely.

- It's docs-wide, not tutorial-specific — you can't attribute a docs-wide NPS number to this one page.
- Quarterly cadence means it won't move, or even fire, inside your six-week window.
- Keep it for general docs-health tracking if you already run it, but it answers a different question than the one the VP is asking.

## The actual problem: none of this proves headcount value

Your VP's ask — justify two headcount at a board review — is the specific trigger for promoting one metric above everything else: **share of tutorial-completers who perform the same task in the product within a week.** It's the only line on the board that shows the *product* changed, not just the *page*. A strong completion rate with no downstream usage means the tutorial taught the tutorial, not the SDK — that's a real trap, teams that stop at completion-rate-and-satisfaction can look successful for years while producing zero behavior change.

Two catches, both real for your timeline:

- It requires the tutorial's completion event and your product's usage telemetry to share an identity (same user/account ID on both sides). That plumbing has to exist *before* you can attribute anything, and nothing in your current plan builds it.
- If that join doesn't already exist, wiring it is most of your few-days budget by itself — it's the one line item on this whole list explicitly flagged as "a standing job," not a quick add. Scope it to whatever identifier docs and product already share (an API key, account ID, logged-in session) rather than building new identity resolution from scratch.

Also add, because it's nearly free and it's the only in-tutorial evidence a skill actually formed: run one cold run of the tutorial against its pass criteria (a learner at your declared audience level, no help, on a clean machine) and record whether they can repeat the task unaided on a variation you didn't walk them through. That single pass/fail is cheap — you should be running it anyway to know the tutorial itself is sound — and it's a concrete "we verified people can actually do this" line for the board that a completion percentage can't give you.

## What to ship with a few engineer-days, in priority order

1. Per-checkpoint drop-off events (reuses the completion event you were already going to build; ~an hour once checkpoints are defined).
2. Completion rate + median time vs. stated estimate — free once the above exists. Report as baseline, no external target attached.
3. One cold run against the pass criteria, transfer-test result recorded — near-zero engineering cost, mostly a person's time.
4. Whatever slice of the completion→in-product-usage join is achievable in the remaining budget. Even a rough version (e.g., "completers with a matched API key who called the SDK within 7 days") beats nothing — this is the number that actually speaks to headcount.
5. Thumbs widget only if it falls out of the checkpoint instrumentation for free. Quarterly NPS: leave it running if it already exists, exclude it from the board story.

If the identity join genuinely can't land before the board date, say that to the VP now: completion rate, thumbs, and NPS are reaction-level proxies, they won't hold up as ROI evidence on their own, and the number that would hold up needs the plumbing funded first.