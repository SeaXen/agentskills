## Show HN, not Launch HN

Launch HN isn't really a menu option you pick because you're funded — it's normally arranged directly with HN (usually via hn@ycombinator.com) and is associated with YC-backed company launches. Even setting that aside, the format test is simple: **is this a thing people can try, or a company announcement?** An open-source columnar cache is squarely "something to try." That's a Show HN by definition, regardless of your funding stage.

Trying to badge it "Launch HN" because you raised $6M would read to HN as company-first framing on a technical audience that explicitly polices that. Keep it Show HN.

## Fix the title — pull the funding and superlative out

Your draft:
> Show HN: Sablefish - the fastest open-source columnar cache, from the team that raised $6M

Two problems:
- "the fastest" is an unsubstantiated superlative — HN titles should be factual, not marketing copy. If you have real benchmarks, put the numbers in the post/first comment, not a bare claim in the title.
- The funding mention is the single closest match to the skill's canonical *bad example*: "Show HN: My startup just raised $5M" — funding isn't something to try, and pairing it with Show HN signals PR, not craft. It will cost you credibility with the exact audience you want reviewing your storage engine.

Rewrite:
> Show HN: Sablefish – an open-source columnar cache

Or, if you have a real, defensible number:
> Show HN: Sablefish – an open-source columnar cache, Nx faster than [specific baseline] on [specific workload]

Put "$6M Series A, small team" in your first comment as backstory, not in the title.

## Timing: 9am ET Tuesday is still right — for the wrong reason if you're optimizing for your own users

9am ET = 6am PT, which sits right at the start of the window that catches US East Coast morning + European afternoon — that's still the standard advice and it holds.

But note what it means for *your* actual users: 9am ET = **3pm CEST** (Germany/Netherlands are UTC+2 through late October). That's mid-afternoon on a workday for them — fine for them to see and organically engage with, not the crack-of-dawn "checking HN with coffee" slot, but not a dead zone either.

The thing to be clear-eyed about: HN's ranking algorithm cares about volume and velocity in the first 1–2 hours, and HN's total traffic is US-dominated regardless of where your specific customers live. So don't re-time the post around Germany/Netherlands work hours hoping your own users carry the launch — optimize for the US window as the skill recommends, and treat your EU user base as a secondary, organic boost that happens to land in a reasonable local time for them. Tuesday 9am ET stays the right call. Keep Wednesday/Thursday 9am ET as your fallback if you need to repost.

One explicit guardrail: it's fine to post the Show HN link where your users will see it (changelog, Twitter, Discord) once it's live — just never phrase it as a call to upvote. That's the line between "awareness" (fine) and "voting ring" (bannable, and detected).

## Your karma is a non-issue

830 karma since 2014 clears the "500+ = posts get more initial trust" threshold in this skill's own table, and account age (2014) reads as a real person, not a launch-day throwaway. You don't need to do anything to "build up" trust before posting — that's already handled.

## What to actually do before posting

- Retitle per above — drop "fastest" and the funding line from the title itself.
- Draft your first comment now, not at post time: who you are, why you built Sablefish, one or two genuinely interesting technical decisions (compression scheme, cache eviction strategy, whatever's actually non-obvious), and *then* — if it feels natural — one line of context ("small team, we're well-funded and building this full-time"). That's where the $6M belongs, framed as "why we can commit to this," not as the headline.
- Block out 2–3 hours after posting to answer every comment yourself, especially critical/skeptical ones about performance claims — those threads are where "fastest" claims get stress-tested in public, so be ready with real numbers if you make any comparative claim at all.
- Confirm Sablefish hasn't been submitted in the last 24 hours (dupe risk) before you post.