# Getting gopherlog.dev posts onto daily.dev

**No, don't suggest your blog as a source.** daily.dev excluded company and personal blogs as sources in 2024. Good RSS doesn't change that, and the request would tie up a review of up to 30 days [platform]. A source also needs 250 reputation and has to be a well-known, multi-author developer publication. Post your articles by hand instead, through **New Post**.

## Assumptions to correct
I made these up to size the plan. Tell me which are wrong, because they change the ranking:
- **Hours:** about 2 hours a week.
- **Comments:** you can answer comments within a day.
- **Reputation:** you're near the starting score of 10.
- **Audience:** no existing audience to invite, such as a newsletter or a large GitHub following.
- **Budget:** organic only.

## Fit verdict: Invest, conditional
- Go-performance readers follow stack tags on daily.dev.
- Two posts a month meets the "technical posts at least monthly" bar.
- The condition is that you answer every comment within a day. If you can't, drop to "syndicate only".

## Entry path
1. **New Post** to your profile ("Everyone"), plus at most 3 Squads in total [platform]. Each post links to its gopherlog.dev URL, with no shortened URLs.
2. **Check the composer for the reputation gate.** The docs disagree on whether New Post needs 250 reputation. If it blocks you, post only inside your own Squad, where admins are never gated.
3. **Optional DEV cross-post.** It may get indexed, and then you can claim authorship. Treat this as a bonus, because daily.dev is currently prioritizing niche sources and DEV content may rank lower [platform]. Add `<meta name="twitter:creator" content="@yourhandle">` to the post `<head>` in Hugo, and put the same X handle under Account details on daily.dev. Claiming gives an author badge and analytics, but it guarantees a feed slot, not traffic.
4. **Skip the Verified Company Squad and Ads plans.** They are sales-assisted, commit you a quarter at a time, and suit a company publishing weekly.

## Setup
- **Profile:** complete it, and follow the tags `go`, `golang`, `performance` and `benchmarking`. Open each tag page and check its top posts before relying on the tag.
- **Account:** one personal account in your own name [platform]. Multiple accounts are banned.
- **Disclosure:** if a post features your own library, open the commentary with "I maintain {project}; this post uses it for {X}."
- **Own Squad:** create one only when you have people to invite. Otherwise it stays a members-only surface for weeks.

## Ranked surfaces for you
1. **Substantive comments on Go and performance posts.** This is the best value per hour. Each comment upvote is worth +50, counted only from voters with 250+ reputation. Five upvotes take you from 10 to 260.
2. **Full post via New Post to your profile plus relevant Squads.** This is your main output.
3. **Own Squad**, once you have an audience.
4. **Curating others' posts into your Squad, with your own commentary.**
5. **DEV cross-post**, for indirect pickup and claiming.
6. **Post Boost.** Use it only if a post earns organic upvotes in its first 24 hours [self-set].

Your hours and audience answers moved the Squad down the list. Under 2 hours a week, keep to comments, claiming and one curated post.

## Per-post targeting
- **Tags:** the stack tags above, never your project name alone.
- **Squads:** pick by topic fit and rules card, not by member count. I can't name specific Squads without checking their gates, so every gate is "check in composer" in your plan.
- **Limit:** one link per Squad, posted once. Don't repost after a decline.
- **Title:** plain and specific. Clickbait gets demoted.

## Eight-week cadence
| Weeks | Action |
| --- | --- |
| 1-3 | Earn reputation. Leave 3-5 substantive comments a week with no links. Reach 250 before your first post [self-set]. |
| 2 | If you have an audience, create the Squad: public, DevTools or closest category, rules, "Require post approval". Seed 5-10 curated posts first. |
| 3-4 | First New Post, with commentary and disclosure. If you're under 250 by week 4, post only in your own Squad. |
| 5-8 | Second post. Your 2-per-month pace is slower than the skill's weekly default, so fill the gaps with curation and comments. Keep to three non-product contributions per product post [self-set]. |
| Monthly | Read post analytics. Drop tags and Squads that drew nothing. |

Hours are about 2 a week, and you are the owner of everything.

## Don'ts
- **Don't ask friends to upvote on cue.** Votes from accounts under 250 reputation do nothing, and coordination reads as manipulation.
- **Don't paste AI-drafted text.** daily.dev screens for AI characteristics. Write the comments and commentary yourself.
- **Don't use affiliate or referral links.**

## Paid decision
Stay organic for now. Consider a Post Boost only on a post that already earned organic upvotes in its first 24 hours. Don't buy a Squad Boost until your Squad has 10+ quality posts.

## Templates
**Earn-first comment** (rewrite in your own voice, with a measured fact and no link):
```text
We hit the same allocation spike after switching to sync.Pool. In our case
it was oversized buffers being returned and never reclaimed, so GC pressure
rose. Capping returned buffer size to 64 KB cut p99 from 410 ms to 120 ms.
Did your pprof heap profile show the same?
```

**New Post commentary:**
```text
Title: {plain, specific title, e.g. "Cutting allocations in {hot path} by 60% in Go"}
Commentary:
I maintain {project}; this post uses it for one step, and the trade-offs
section says where it falls short. The three changes that mattered: {one line
each}. The benchmark is in the repo linked at the end. What allocation
numbers do you see on {Go version}?
Audience: Everyone + {Squad A} + {Squad B} (gates: check in composer)
```

**Reply to a declined Squad post:**
```text
Thanks for the reason - fair, the post read as a launch announcement. I've
rewritten it around the benchmark method and moved the project mention to one
line at the end. Is it OK to resubmit, or is there a better Squad for it?
```

## Metrics
Targets are self-set, because daily.dev publishes no organic benchmark.
- **Reputation:** check weekly until 250.
- **Per post at day 3:** impressions, unique reach, upvotes, comments, clicks. Tag links with UTM parameters (Hugo can add them) to measure gopherlog.dev sessions.
- **Hygiene:** declined posts, removals and reputation drops. The pass threshold is zero.

## Open questions
1. Which assumptions above are wrong?
2. Do you have an audience (newsletter, GitHub following) to invite into a Squad?
3. Does the composer let you use New Post at your current reputation?

I didn't verify any of this against the live daily.dev docs. It comes from the playbook, which warns that the platform changes quickly. Re-check the docs page for any number before relying on it.