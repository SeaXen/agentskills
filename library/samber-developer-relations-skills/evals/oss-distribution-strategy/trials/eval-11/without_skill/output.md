## 1. Why cloudferry isn't showing up

⚠️ I couldn't pull live pages this session (WebSearch/WebFetch/`gh api` were all blocked by permissions that didn't get granted), so treat the diagnostics below as things to confirm on your end, not confirmed facts about your repo's current state.

The core issue: you're treating "topics" and "collections" as one discovery system. They're two unrelated systems on GitHub, with different mechanics.

**Topic pages** (`github.com/topics/kubernetes`, `github.com/topics/gitops`) are automatic. Any repo with that string in its actual **Topics** field gets indexed there — no human review. If cloudferry has the topics set and still isn't visible, the cause is one of these, roughly in order of likelihood:

- **Topics were typed into the description, not the Topics field.** The Topics field is the separate chip-list set via the gear icon next to "About" on the repo homepage — not prose in the description. This is the single most common reason people think they "added a topic" and it did nothing.
- **String mismatch.** `k8s` ≠ `kubernetes`; a typo or non-canonical slug silently creates a topic page with near-zero traffic instead of tagging into the real one.
- **Indexing lag.** Topic-page indexing isn't instant; it can take hours to reflect a new tag.
- **cloudferry is a fork.** Topic pages default to excluding forks unless a viewer explicitly includes them.
- **You're present but buried.** Default sort on a topic page is relevance/best-match, not stars. With thousands of repos tagged `kubernetes`, 1,900 stars can land you many pages deep — that reads as "invisible" even though you're technically indexed. Sort the topic page by "Recently updated" (not stars) — that will surface a legitimately-tagged repo near the top regardless of star count, and tells you definitively whether you're indexed at all versus just outranked.

**Action:** go to the repo → gear icon next to "About" → verify `kubernetes` and `gitops` sit in the actual Topics chip field. Then open both topic pages yourself and switch sort to "Recently updated" to confirm indexing. If you don't show up even there, it's a tagging/indexing bug worth a GitHub support ticket. If you do show up but only on page 40 under default sort, that's not a bug to fix — that's a stars/relevance problem, not a tagging problem.

**Collections** (`github.com/collections/devops-tools` or similar) are a completely different, editorially-curated surface — historically maintained through the open-source repo `github/explore`, where a repo gets added to a collection via a pull request that GitHub's own curators review and merge (or reject) at their discretion. Adding topics to your repo has **zero effect** on collections. There's no auto-qualification threshold, no self-serve submit button on your side — you (or a community member) have to go open a PR against `github/explore` proposing cloudferry for the DevOps collection, write the blurb, and wait on human review. Expect this to be a judgment call, not a formality, and expect it to take real calendar time.

**Bottom line on part 1:** stop expecting topics to produce a collections listing — go file a PR against `github/explore` for that. Separately, verify your topics are in the actual Topics field (not description text) and check indexing via the "Recently updated" sort before assuming there's a platform bug.

## 2. Star velocity for a repeat trending hit

There is no official published threshold — GitHub has never disclosed the trending formula. What's understood from years of community reverse-engineering: trending is driven by stars gained inside the selected window (WatchEvents in that period), ranked **relative to other repos in the same language filter on the same day** — not against an absolute bar. That last point matters for you: Go's daily trending pool is much shallower than JavaScript's or Python's, so the velocity needed to place in Go trending is meaningfully lower than what people usually cite for "GitHub trending" in general (which is contaminated by JS/Python numbers).

Commonly cited (not official) ranges for a lower-volume language's daily trending page: roughly **30–100 stars within 24h**. That's the ballpark to plan around, but it's secondhand — don't treat it as precise.

The number you actually have and I don't: **your own June trending day.** That's a real, empirical data point — proof of a velocity sufficient to trend, for your exact language and repo quality bar, not an industry average. Pull it from star-history.com (plot cloudferry, zoom to that week) or a GH Archive query on WatchEvents for that day, and that figure becomes your real target — treat it as a floor, not a ceiling, since trending is relative to that day's competition and you don't control what else was trending.

One structural point worth acting on: your best clone week was *caused by* trending, not the other way around — trending drives the traffic that produces clones, so the lever to pull is the 24h star spike itself, not clone-optimization. To engineer that spike, concentrate every promotion channel into the same tight window instead of spreading a launch over a week: line up HN, relevant subreddits, X/Twitter, a newsletter mention, and any Slack/Discord communities to fire within a few hours of each other on the same day, so the WatchEvents cluster inside one 24h window rather than diffusing across several below-threshold days.

**To get an exact number instead of a range:** tell me the star count cloudferry gained on that June trending day (or the date, so I can look it up once I have working web access again) and I'll turn this from a range into your actual target.