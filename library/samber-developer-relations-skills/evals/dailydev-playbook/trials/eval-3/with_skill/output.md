# daily.dev plan for Quillstack: verdict, tags, timing

Don't run this plan as written. Three of its parts get content removed or demoted on daily.dev, and the platform publishes no best posting time. Below are the verdict on each plan item, then the tags and timing you can defend.

Labels: **[platform]** is a daily.dev docs rule. **[self-set]** is a default I propose, with no platform number behind it.

## 1. Verdict on each plan item

| Plan item | Verdict | Why |
|---|---|---|
| Backlinks and ChatGPT/Perplexity citations as the goal | ❌ Rejected | Content made to rank, earn backlinks or get cited by AI tools (SEO, AEO, GEO) is rejected **[platform]**. Links in posts are nofollow, so there is no link equity anyway. |
| ~30 posts from an LLM pipeline | ❌ Rejected | AI-generated text, or text with its characteristics, is rejected, and automated screening looks for it **[platform]**. |
| One post per day | ❌ Fails | Each post links to a landing page, so it reads as self-promotion as the main purpose. Penalties run from demotion to removal, reputation loss, submission restrictions and suspension. A removed post costs -100 reputation. |
| Each post links to a landing page | ⚠️ Risky | One landing-page link per post, in a daily stream of pitches, is the pattern moderators decline. Link the technical artifact (repo, benchmark, write-up) instead. |
| Post from the CMO's account | ⚠️ Change | Post from named engineers' personal accounts, one account each **[self-set]**. A marketing exec posting 30 pitches a month reads as a brand account. The CMO can post, but not the stream. Multiple accounts per person are banned. |
| New Post as the entry path | ✅ Valid, wrong volume | New Post to profile plus at most 3 Squads is a real route. Docs disagree on whether it needs 250 reputation, so check the composer. |

Paid routes for AI visibility exist: Agent Ads, a Verified Company Squad page open to AI crawlers, and Sponsored Content. Organic GEO content stays banned.

## 2. Fit verdict

I'm assuming a technical backlog exists and engineers can answer comments daily. If so, the verdict is **Invest, at a much lower volume**. If nobody can answer comments, it is **Skip organic**. I did not run the interview. These answers would change the plan:

1. Which named engineers will post, and what is each one's current reputation?
2. Is there a launch date inside four weeks?
3. How many hours per week, and who answers comments within 24 hours?
4. Is there a paid budget this quarter?

## 3. Tags

daily.dev publishes no formula, so tags are your targeting: personalized feeds match the tags readers follow **[platform]**. Pick the stack your readers work in, check each tag's top posts, and never use the product name alone.

Candidates for an AI code-review tool. I haven't verified that each tag exists, so confirm each one in the composer:

| Post topic | Tags to try |
|---|---|
| Review process, PR hygiene | `code-review`, `pull-requests`, `github`, `git` |
| Quality, bugs found in review | `testing`, `static-analysis`, `devops`, `ci-cd` |
| How the tool works, with trade-offs | `ai`, `llm`, `developer-tools` |
| Language-specific findings | The customer language or framework: `typescript`, `python`, `go`, `java`, `react` |

Rules:
- Match tags to the post. Don't reuse one tag set across posts.
- Drop tags that draw nothing in the monthly analytics review.

## 4. Posting times

There is no published best posting time **[platform]**. The Popular feed weighs early unique reads, upvotes and freshness, but the window length is unpublished. Anything I gave you as an optimal hour would be invented.

Test in a way you can read **[self-set]**:
1. Post on a weekday morning in your target readers' main time zone, when the poster is online to answer.
2. The slot matters more than the hour: comments must be answered within 24 hours, since commenter reputation and comment freshness drive Best discussions.
3. Alternate two slots across weeks, such as Tuesday morning and Thursday morning.
4. Compare day-3 impressions, unique reach and upvotes, then keep the better slot.

## 5. What to run instead

**Entry path.**
- Publish through New Post to the poster's profile ("Everyone") plus your own Squad and at most 2 more. The cap is 3 Squads, your own included.
- Post only into Squads whose gate the poster meets. If a gate is unknown, mark it "check in composer".
- If New Post blocks the poster, post inside your own Squad until they reach 250 reputation.
- If you want RSS auto-posting, a verified seal and day-one discovery, that is a Verified Company Squad. It is sales-assisted, with a quarterly commitment.

**Setup.**
- Each poster completes their profile, verifies the company badge with a work email, and follows the target tags.
- If posts are already on an indexed publication or on DEV, claim authorship. Add `<meta name="twitter:creator" content="@handle">` to the post head, add the same handle under Account details, and email support for posts picked up earlier.

**Eight-week cadence.** Reputation takes weeks, so this is sized to eight weeks.

| Weeks | Owner | Hours/wk | Action |
|---|---|---|---|
| 1-3 | Each named poster | 2 | Comment substantively on 3-5 posts a week in your tags. No links in comments. Reach 250 reputation. Claim authorship of indexed posts. |
| 2 | Squad owner | 2 | Create a public Squad in the DevTools category. Add image, cover image, description, Stack & Tools and rules. Set posting mode "Require post approval". Turn on the Slack integration. Seed 5-10 curated posts with commentary before inviting anyone. |
| 3 | Community owner | 1 | Invite your existing community and newsletter by link. Never pay or incentivize joins. |
| 3-8 | One engineer per post | 3-4 | One original technical post a week, not a daily post. Post to profile, your Squad and at most 2 more. Answer every comment within 24 hours. A poster still under 250 by week 4 posts only in your Squad. |
| 4+ | Best-reputation engineer | 3 | Launch week: one strong post plus a Squad poll. Boost only if the post earned organic upvotes in its first 24 hours. |
| Monthly | Growth lead | 1 | Read post and Squad analytics. Drop tags and Squads that drew nothing. |

Ratio **[self-set]**: three non-product contributions (comments, curated shares) per product post, per person.

That is about 8 posts in the eight weeks, not 56. Take the best of the ~30 monthly articles, and have an engineer rewrite it from their own experience and numbers.

## 6. Paid decision

- **Post Boost:** only on a post that already has organic upvotes. It runs 5,000-100,000 Cores a day for 1-30 days, self-serve.
- **Squad Boost:** only after the Squad has 10+ quality posts.
- **Verified Company Squad or Ads plan:** only if you will publish weekly for at least two quarters. This is also the only compliant route to what you want. Ask sales about Agent Ads and the AI-crawler-open Squad page, and price from a written quote. daily.dev publishes no rate card.
- **Sponsored Content:** a guaranteed-read test if organic stalls.
- **Not a fit:** a one-week test, or a team with no technical content.

## 7. Filled template: New Post with commentary

```text
Title: How our review bot cut false-positive comments from 31% to 9% on {language} PRs
Commentary:
I work on Quillstack; this post uses it for the measurement step, and the
trade-offs section covers where it still misses. The three changes that
mattered: {one line each}. The benchmark script is in the repo linked at the
end. What false-positive rates do you see from automated reviewers?
Audience: Everyone + {Own Squad} + {Squad B} (gates checked: {gate B})
```

- Replace the figures and placeholders with the engineer's real numbers. The 31% and 9% above are illustrative.
- Use a plain, specific title. Clickbait is demoted and rewritten for Plus readers.
- Link one technical artifact. Use a UTM-tagged link, never a shortened URL.
- Affiliation goes in the first line. Never add an affiliate or referral link.
- Run the draft through a humanizer, then rewrite it in the engineer's own voice.

## 8. Metrics

- **Reputation per poster**, weekly, until 250.
- **Per post at day 3:** impressions, unique reach, upvotes, comments, clicks, and UTM referral sessions and signups.
- **Squad, monthly:** members, upvote ratio, clicks, new members per Boost.
- **Hygiene, pass threshold zero:** declined posts, removals, reputation drops.
- **On an Ads plan:** install the daily.dev conversion pixel.
- All targets are self-set. daily.dev publishes no organic benchmark for vendors.

## 9. Backlinks and AI citations

daily.dev won't deliver these. Use the right channels:
- Publish the articles on Quillstack's own site, with proper schema and `llms.txt`. See the `ai-seo` and `schema` skills.
- Earn links from unpaid indexed publications and community mentions.
- Treat daily.dev as a developer-reach channel, not a link-building one.

## 10. If a post is declined or removed

1. Stop reposting. A repeat after a decline reads as spam.
2. Read the moderator's reason or the Squad rules, fix the post, and resubmit once.
3. For a platform removal or reputation drop, contact daily.dev support with the post URL and the fix. Reversal is not guaranteed.