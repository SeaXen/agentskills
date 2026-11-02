# Why Basalt's Medium posts stall at about 40 views

**Short version for the VP:** Medium shows a post to a company's followers and to people who search for or browse its topic. It recommends it more widely only if it reads as useful, non-promotional writing from a credible author. Our posts fail on almost every one of those signals, so they reach roughly our 300 followers and stop. The cause is how we use the platform. Medium isn't broken and the product isn't the problem.

I haven't seen your Medium stats dashboard. The mechanics below are from general knowledge of Medium's behavior and policies, which change, so check the "verify" items.

## Causes, ranked by likely impact

| # | Cause | What we do | Why it caps reach |
|---|---|---|---|
| 1 | **Promotional framing** | "Announcing Basalt 2.3", "Why Basalt beats RDS", free-trial link at the end of every post | No one searches for a company's release announcement, so there is no search demand. Medium's rules and curation also treat primarily promotional content as ineligible for broader recommendation. **Verify** against the current Medium Rules and curation guidelines. |
| 2 | **Wrong tags** | Technology, AI, Startup, Productivity, Programming | These are the most crowded tags on Medium, and none describes a Postgres post. Readers browsing "AI" never see a managed-Postgres post. People who want Postgres content browse tags like PostgreSQL, Databases, SQL, and Cloud, and we don't use them. |
| 3 | **Generic AI drafts with a light edit** | ChatGPT drafts, lightly edited | The text reads like every other AI-written post and has no first-hand detail: no benchmark, incident, schema, or query plan. Medium has said it limits distribution of AI-generated writing. **Verify** the current wording. Readers also bounce quickly, which hurts further recommendation. |
| 4 | **Brand account with no audience** | Posting as "Basalt" with 300 followers | A company logo has no personal credibility, and readers follow people more than brands. Followers see the post and stop there. Most likely the 40 views are our existing followers plus some employees and trial users. |
| 5 | **25 @mentions per post** | Tagging about 25 Postgres influencers | This works against us. Mass tagging looks like spam to the recipients and can look like spam to Medium's systems. Influencers don't engage with unsolicited tags from a vendor. It also signals that we are trying to borrow their audience. |
| 6 | **Language split** | Half the posts in Portuguese, on the same account | Medium recommends by language, so Portuguese posts are never shown to our English followers. Brazilian developers are also more active elsewhere (LinkedIn, TabNews, Dev.to, YouTube, local communities). The Portuguese half therefore reaches a small slice of an already small base. **Verify** with the stats split by language. |
| 7 | **Comparison claims with no evidence** | "Why Basalt beats RDS" | Readers distrust a vendor's own comparison, especially one without methodology or numbers. People who open it leave early, and early exits depress recommendation. |

## What to check in our own data (30 minutes)

1. **Traffic source split** in Medium Stats: internal (Medium feed), external, search, and followers. I expect almost all views to come from followers and direct links.
2. **Read ratio and reading time** per post. Low numbers confirm the content isn't holding people.
3. **Compare English and Portuguese posts.** If the Portuguese ones are even lower, cause 6 is real.
4. **Compare one post that has the @mentions with one that doesn't.** I expect no difference.
5. **Check whether any post was ever curated or boosted.** If none was, we are outside Medium's recommendation system.

## Recommended changes, in order of effort

1. **Stop the @mention blast.** Mention at most 1–2 people, and only when we actually cite their work. This costs nothing.
2. **Retag.** Use PostgreSQL, Databases, Cloud Computing, SQL, and DevOps. Keep any two broad tags only where they truly fit.
3. **Change the post types.** Publish posts that solve a problem, such as "How we cut a 40 GB vacuum from 6 hours to 40 minutes" or "Debugging replication lag: a query-plan walkthrough". Mention Basalt briefly where it is relevant, and replace the hard trial CTA with one soft link.
4. **Put real people on the byline.** Use an engineer with their own profile, and have the Basalt publication or account republish it. A named expert beats a logo.
5. **Rewrite AI drafts around original material.** The inputs should be our own benchmarks, incidents, and queries, with ChatGPT used only to tidy the prose. Drop "beats RDS" unless we publish the method and the data.
6. **Decide the Portuguese strategy separately.** Run it as its own account or publication, and cross-post to the channels where Brazilian developers are. Don't count it as part of the Medium effort.
7. **Treat Medium as a secondary channel.** Publish the canonical post on our own blog, which ranks in search and earns links. Cross-post to Medium with the canonical tag set, and add Dev.to, Hacker News when warranted, and the Postgres community channels.

## Suggested success metric

Don't aim for "more views" on this account. Aim for **one post per month that gets to 1,000+ views from non-followers**. That tells us whether the new approach works, and it is a more honest target than total views.

## One-line message for the VP

> Our Medium posts are product announcements with mismatched tags and mass-tagged names, drafted by AI, from a brand account with 300 followers. That combination keeps them out of Medium's recommendations. We'll change the format and the byline, and treat Medium as a distribution channel for content we publish on our own blog.