# daily.dev plan for Quillstack: tags and posting times

I can't verify daily.dev's current tag list or its audience-activity data from here. The tags below are candidates to check against the picker, and the times are hypotheses for you to test. I've also changed the plan itself, because the current version is likely to backfire.

## Change the plan first

1. **One post a day, all linking to a landing page, looks like spam.** daily.dev ranks posts by community engagement. A daily stream of near-identical LLM-written posts from one corporate account, each ending in a sales link, will probably get downvoted, reported or ignored. That can also hurt the CMO's account.
2. **Don't count on SEO value from the backlink.** Check the link attribute on a live post (view source for `rel="nofollow"` or `ugc`). User-submitted links on large aggregators are often nofollow. They can still bring referral traffic, but they pass little ranking value.
3. **Link to the article, not the landing page.** Publish each piece on your own domain first, with a canonical URL, and share that. Posts that go straight to a sales page get far less engagement. The article carries the CTA to the landing page.
4. **LLM citations come mostly from your own content.** ChatGPT and Perplexity cite pages that answer the query directly, with specific facts, original data, clear structure and schema markup. They cite aggregator posts far less. Put your effort into the pages on your own domain.
5. **Disclose the affiliation.** The CMO should say "I work at Quillstack" in the post or first comment. Undisclosed self-promotion gets accounts banned on developer platforms.
6. **Review the LLM output by hand before it goes out.** Developers spot generic AI text quickly. Cut volume if that's what it takes to keep quality up.

**Recommended cadence:** publish all ~30 articles on your own site. Share the best 8–12 a month to daily.dev, about 2–3 a week, and only the ones with original data, code or a real opinion. Have the CMO also comment on other people's posts, so the account isn't broadcast-only.

## Tags

daily.dev uses a curated tag set, so confirm each one exists in the New Post picker. Use 3–5 per post: one broad tag, two or three specific ones, and one tied to the stack or language in the article. Don't add tags the article doesn't cover. Mismatched tags get posts downvoted and reported.

| Article theme | Candidate tags |
|---|---|
| Code review practice | `code-review`, `pull-requests`, `software-engineering`, `best-practices` |
| AI-assisted review and coding | `ai`, `llm`, `developer-tools`, `ai-coding` |
| Team velocity and quality | `developer-productivity`, `engineering-management`, `devops` |
| Security in review | `security`, `appsec`, `static-analysis` |
| Git workflow and CI | `github`, `git`, `ci-cd`, `testing` |
| Language-specific posts | `typescript`, `python`, `golang`, `java`, `rust` (match the article) |

Rotate the tag sets across posts. Using the identical five tags on every post makes the account look automated.

## Posting times

I have no verified daily.dev engagement data, so treat this as a starting hypothesis. Developer feeds usually peak on weekday mornings in US Eastern time, which overlaps with the European afternoon.

- **Slot A:** Tuesday–Thursday, 13:00–15:00 UTC.
- **Slot B (test arm):** Tuesday–Thursday, 08:00–10:00 UTC, for the European morning.
- Avoid weekends and Mondays before 14:00 UTC for a first test.

**Test for four weeks:**

1. Alternate slots A and B across comparable posts.
2. Record upvotes, comments, views and click-throughs after 48 hours. Add UTM tags, for example `utm_source=dailydev`.
3. Keep the slot with the better median engagement per post. Don't compare means, because one hit will skew them.
4. Check engagement by tag as well. Drop tags that bring downvotes or no clicks.

## Success metrics

- Referral sessions and signups from `dailydev` UTMs.
- Whether Perplexity or ChatGPT cite your own-domain articles. Check monthly with a fixed list of 20 target queries.
- Referring domains from Ahrefs, split by follow and nofollow.
- Share of posts with at least 5 upvotes. If it stays low after a month, reduce the volume.

If you'd like, I can draft the 20-query citation tracking sheet, or a one-page review checklist for the LLM pipeline's output.