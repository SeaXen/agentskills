# Why Hexmesh's daily.dev reach is so low

I couldn't run web searches here (permission denied), so the daily.dev specifics below come from memory. Check the ones marked **verify** against current daily.dev docs and your own account settings before you change anything.

## Short answer

Reach is low because the posts ask the feed to do the work the post should do. The release link, the "check out what's new!" caption and the clickbait title give readers nothing to judge. Low-reputation accounts then get little boost. The missing author on picked-up articles is a separate, fixable attribution problem.

## Cause 1: the posts are changelog links with ad copy (biggest factor)

- **A release link is not an article.** The daily.dev audience is developers browsing a feed. A GitHub release page or changelog has no hook, no narrative and no reason to care. It reads as an announcement.
- **"Check out what's new!" says nothing.** It names no problem solved, no number and no reader outcome.
- **"You won't believe how fast Hexmesh 2.4 is" is clickbait with no proof.** Developers distrust this pattern, and the claim has no number. "Fast" compared to what, measured how? In a service-mesh category full of benchmark wars, an unsupported speed claim reads as marketing. It gets scrolled past or downvoted.
- **Three coworkers posting every release is a promo pattern.** Repeated, same-source, same-format posts from related accounts look like self-promotion, to readers and likely to the feed's quality signals. It also tells readers "vendor, not peer".
- **Hexmesh 2.4 means nothing to someone who has never used Hexmesh.** Most feed readers aren't existing users. A point release gives them no entry point.

## Cause 2: account standing

- **At 10–30 reputation, the accounts have no track record.** daily.dev ties reputation to community response such as upvotes and engagement on your content, and gates some privileges on it **(verify the exact thresholds)**.
- **There is a loop.** Posts that nobody upvotes can't build reputation, so the next post starts from the same position. Forty views and one upvote after two months says the audience never engaged.
- **Three accounts don't pool.** Each starts from zero, and each posts the same kind of content.

## Cause 3: ranking and distribution (my understanding, not verified)

- **The feed favors early engagement, topic tags and source quality.** A post with no early upvotes, comments or bookmarks stops being shown. A bare link with a thin title and no useful tags gives the ranker nothing.
- **Posts that duplicate your own source may be deduplicated or deprioritized.** If the link already appears as a picked-up article from your blog or DEV, a manual post of the same content adds nothing.
- **Service mesh is a narrow topic.** Reach scales with how many people follow the matching tags, and a point release of one tool is a small slice of that.

## Cause 4: the missing author on picked-up DEV articles

daily.dev ingests content from RSS feeds and publication sources. If it shows no author, the likely causes, in order, are:

1. **Your DEV feed or the article metadata has no author field that daily.dev can parse.** Check how the DEV posts appear in the RSS and in the page's `author` meta, JSON-LD `Article.author`, or `rel=author`.
2. **The article was ingested under a publication or organization source** (for example a Hexmesh DEV organization) rather than a person, so no profile is attached.
3. **Nobody has claimed the posts on daily.dev.** Authors can usually claim authorship or link their profile **(verify the current flow)**. An unclaimed article stays anonymous, and a claimed one carries your name, reputation and followers.

Missing authorship hurts twice: readers can't follow or trust a person, and the writers earn no reputation from their best-performing content.

## What to do

1. **Stop posting every release as a bare link, starting today.** Keep release announcements in your changelog, GitHub and your newsletter.
2. **Post only content that stands on its own.** A good fit is a short engineering article about a problem, a measurement or a design decision. For example, "How we cut sidecar latency by X% (and what it cost)", with the benchmark method and numbers in the post.
3. **Use honest, specific titles.** Say what happened and give a figure with its test conditions. Drop "You won't believe".
4. **Let one or two engineers with a real voice post, not all three on every release.** Reputation builds faster when one person earns it with useful content.
5. **Fix attribution.** Check the author metadata and RSS on DEV, add a proper author field, then claim the articles under each engineer's daily.dev profile.
6. **Engage as a reader first.** Upvote, comment helpfully and bookmark service-mesh, Kubernetes and networking content. Reputation comes from useful participation, and genuine comments earn it faster than link posts.
7. **Do not ask colleagues to upvote.** Coordinated voting is detectable and gets content penalized.
8. **Measure differently.** Judge by clicks to the article or repo, and by stars, installs and doc traffic from daily.dev referrals, not only views and upvotes.

## What I could not confirm

- The exact reputation thresholds and which privileges they gate.
- How daily.dev ranks and deduplicates posts today.
- The current author-claim flow.

If you share one example of a good-performing article and one failing post, I can compare them. Your analytics referral data would also show whether daily.dev traffic converts at all.