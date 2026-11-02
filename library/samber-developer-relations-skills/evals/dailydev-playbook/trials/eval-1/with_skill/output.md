# Tracewell on daily.dev: verdict on your plan, then a replacement plan

## 1. Verdict on your three items

| # | Your item | Verdict | Why |
|---|---|---|---|
| 1 | Suggest blog.tracewell.io as a source | ❌ Drop | Company and personal blogs cannot be sources. Company sources ended in 2024 [platform]. The request would also need 250 reputation and burn a manual review of up to 30 days. |
| 2 | New `tracewell` account, post to the 10 biggest Squads | ❌ Rework | There are three problems, listed below. |
| 3 | 15 engineers sign up and upvote in the first hour | ❌ Drop the coordination | Coordinated voting reads as manipulation, and daily.dev penalizes reputation farming [platform]. Votes from accounts under 250 reputation also add nothing to the author [platform]. |

**Item 2's three problems:**
- **Brand account.** Post from named people's personal accounts instead. The company Squad carries the brand [self-set]. A fresh account starts at 10 reputation, and many Squads gate posting at 250 or 1,000 [platform].
- **Squad cap.** The composer caps one post at 3 Squads, plus your profile [platform]. You cannot post one launch to 10 Squads. Re-posting the same link across Squads or days reads as spam, so post each link once per Squad [self-set].
- **Choosing by size.** Pick Squads by topic fit, rules card and a gate the poster meets, never by member count. Moderators judge a launch announcement against that Squad's rules, and "primarily self-promotion" is rejected [platform].

**Also at risk if the 15 sign up as a group:**
- Fifteen new accounts voting on cue is the exact pattern the platform polices.
- Teammates upvoting each other's comments counts as reputation farming [self-set].
- Penalties run from demotion and removal to reputation loss, submission limits and suspension. Reputation loss also cuts future reach [platform].

## 2. What you're missing

1. **Reputation comes first.** Everyone starts at 10. Posts and comments from high-reputation authors rank higher [platform]. Five comment upvotes from voters with 250+ reputation take an account from 10 to 260.
2. **Launch timing.** Launching next week is inside the 4-week window, and nobody has reputation yet, so this is the launch-first case. daily.dev should be a follow-up channel for the launch, not the main one.
3. **No auto-feed route for a company blog.** The only ways a post reaches the feed are:
   - New Post.
   - Squad posts.
   - A paid Verified Company Squad, which auto-posts your RSS. It is sales-assisted with a quarterly commitment.
   - An indexed publication that runs the piece unpaid.
4. **AI-text screening.** daily.dev screens for AI-generated text and rejects it [platform]. Your engineers must write their own commentary.
5. **Disclosure.** Open every commentary with "I work on Tracewell; …". Affiliate and referral links are banned, and undisclosed promotion posing as a tutorial is banned.
6. **Link hygiene.** English only, no shortened or redirected URLs, and a plain specific title because clickbait is demoted [platform]. Use UTM-tagged full URLs for referral tracking.
7. **Someone must answer comments within 24 hours.** Comment threads feed the Best discussions ranking [platform]. Name the owner before launch.
8. **No published ranking formula.** daily.dev publishes no weights, decay curve or best posting time. Any "first hour" claim is unfounded. The only documented signals are reads, upvotes and freshness on Popular.

## 3. Fit verdict

**Invest, provisionally.** The conditions are:
- Developers read your stack's tags (opentelemetry, observability, nodejs, devops).
- You have 60 technical posts, which suggests at least monthly cadence.
- Someone can answer comments daily.

I'm assuming those three. If nobody can answer comments daily, the verdict drops to **Syndicate only**.

**Open questions that would re-rank the plan:**
1. Which engineers already have daily.dev accounts, and what is each one's reputation?
2. What is the exact v3 launch date? A date inside four weeks keeps the launch-first path.
3. How many hours a week, and who owns replies?
4. Is there a paid budget this quarter, or organic only?

## 4. Entry path

1. **Blog as source:** no, for the reason in section 1.
2. **Already on an indexed publication or DEV?** If Tracewell posts are on DEV, daily.dev may pick them up. Mainstream sources such as DEV may currently rank lower [platform]. If a post gets picked up, claim authorship:
   - Add `<meta name="twitter:creator" content="@handle">` to the post's head.
   - Add the same X handle under Account details on daily.dev.
   - Email support for posts picked up before the claim.
3. **Main route: New Post.** The poster publishes to their profile ("Everyone") plus at most 3 Squads in total, your own Squad included. The docs disagree on whether New Post needs 250 reputation, so check the composer. If it blocks, post inside your own Squad, where admins and moderators are never gated.
4. **Later, if you want RSS auto-post and a verified seal:** a Verified Company Squad. It is paid, so decide after week 8.

## 5. Setup

- **Profiles.** Each poster uses their personal account, one per person:
  - Complete the profile.
  - Verify the company badge with a work email.
  - Follow target tags.
- **Tracewell Squad.** Create it in week 2, public, DevTools category:
  - Image, cover image, description, Stack & Tools and rules.
  - Posting mode "Require post approval".
  - Slack integration on, so comments reach whoever owns replies.
  - Seed 5-10 curated posts with commentary before inviting anyone.
- **Tags.** Use the reader's stack: `opentelemetry`, `observability`, `nodejs`, `distributed-tracing`, `devops`. Check each tag page's top posts. Never use "tracewell" alone.

## 6. Ranked surfaces for Tracewell

Ranked by value per hour. Your launch date promotes New Post and a short Boost.

| Rank | Surface | What moved it |
|---|---|---|
| 1 | Substantive comments in your tags (earn-first) | Cheapest way to reach 250 reputation. |
| 2 | Author claiming | Only applies if posts are already indexed. |
| 3 | Full technical post via New Post, profile + ≤3 Squads | Promoted by your launch date. |
| 4 | Own Squad, seeded | Ranked below New Post, because you have no audience to invite yet. |
| 5 | Curating others' posts into your Squad, with commentary | Builds the Squad's content while reputation grows. |
| 6 | Squad poll | One-shot. Useful in launch week. |
| 7 | Post Boost | Only under the 24-hour rule in section 9. |
| 8 | Verified Company Squad or Ads plan | Defer; decide after week 8. |

## 7. Target Squads for the v3 post

I can't read live Squad rules or gates from here, so every gate is marked "check in composer".

| Squad | Fit | Gate |
|---|---|---|
| Your Tracewell Squad | Always, no gate for admins. | Open. |
| Node.js developers | Good if the v3 post covers Node instrumentation. | Check in composer. |
| An observability or DevOps Squad | Good, rules card decides. | Check in composer. |
| Next.js | Only if v3 has a Next.js-specific angle. | Check in composer. |

**Rules for choosing:**
- Pick your own Squad plus at most 2 others.
- Choose only Squads whose gate the poster already meets.
- Drop any Squad whose rules card or recent posts show no product posts.
- DevOps Daily and the other large Squads are out unless the gate and rules pass.

## 8. Eight-week cadence

Hours are estimates [self-set]. Assign names before week 1.

| Week | Action | Owner | Hours |
|---|---|---|---|
| Pre-launch (next week) | Pick the poster: the named engineer with the highest reputation. Post the v3 post once, via New Post, to their profile + Tracewell Squad + at most 2 Squads they pass. Expect little organic reach. | Poster + comment owner | 3 |
| Pre-launch | Comment owner answers every comment within 24 hours. | Comment owner | 1 per day, 15 min |
| 1-3 | Earn first. Each poster who wants to participate comments substantively on 3-5 posts a week, with no links in comments. | Each engineer who opts in | 1 per person |
| 2 | Build and seed the Squad (section 5). | DevRel | 3 |
| 3 | Share the Squad invitation link to your existing community and newsletter. Never pay for or incentivize joins. | DevRel | 1 |
| 3-8 | One original technical post a week via New Post to profile + Squad + at most 2 more. Pick from your 60 posts or write new ones. Answer every comment within 24 hours. | Rotating named engineers | 2 per week |
| 4+ | Any poster still under 250 reputation posts only in your own Squad. | Poster | n/a |
| 4 | Next launch-scale moment (for example a v3.1 or a benchmark post): one strong post plus a Squad poll. | DevRel | 2 |
| Monthly | Read post and Squad analytics. Drop tags and Squads that drew nothing. | DevRel | 1 |

**Contribution ratio.** Per person, post three non-product contributions (comments, curated shares) for each product post [self-set].

## 9. Paid decision

- **Post Boost:** only if the post earned organic upvotes in its first 24 hours [self-set]. Boosting a weak post buys impressions from readers who downvote. Budget: 5,000-100,000 Cores a day for 1-30 days, stoppable anytime.
- **Squad Boost:** only after the Squad has 10+ quality posts [self-set].
- **Verified Company Squad or Ads plan:** only if you publish weekly and want auto-posting for at least two quarters. It is a quarterly commitment, quoted per company, with no public rate card.
- **Not a fit:** a one-week test.

## 10. Drafts

**Earn-first comment** (weeks 1-3, fill from a real trace you've seen):

```text
We hit the same p99 spike after moving to HTTP/2. In our case it was the
client pool closing idle connections after 60 s, so the first request after
a quiet period paid a new TLS handshake. Pinning keep-alive to 90 s cut it
from 410 ms to 120 ms. Did your trace show handshakes?
```

Replace the numbers with measurements your engineers actually have.

**New Post commentary** (v3 launch, one per poster):

```text
Title: How we cut trace ingestion latency from {X} to {Y} in Tracewell v3
Commentary:
I work on Tracewell; this post covers the v3 ingestion path, and the
trade-offs section says where it falls short. The three changes that
mattered: {one line each}. The benchmark script is in the repo linked at
the end. What ingestion numbers do you see on {runtime}?
Audience: Everyone + Tracewell Squad + {Squad B} (gates checked: {gate B})
```

Do not title it "Tracewell v3 is here". A launch-announcement title gets declined.

**Squad description:**

```text
OpenTelemetry tracing for people building with {stack}. Tutorials, release
notes with migration steps, and questions from the Tracewell team and its
users. No sales posts. Ask anything; a maintainer answers within a day.
```

**Squad rules** (up to 10; a starter six):

```text
1. Technical content only. Why it matters: members joined to learn, not to be sold to.
2. One link per post, with your own summary. Why it matters: a bare link tells nobody why to click.
3. Disclose affiliation. Why it matters: readers trust a post that says who wrote it.
4. No affiliate or referral links. Why it matters: daily.dev bans them platform-wide.
5. English only. Why it matters: daily.dev removes non-English posts.
6. Be kind in comments. Why it matters: questions stop when answers sting.
```

**Invitation message** (existing community or newsletter):

```text
We opened a Tracewell Squad on daily.dev: tutorials and release notes with
the migration steps, in the feed you already read. Join if useful: {invite link}.
```

**If a Squad declines the v3 post:**

```text
Thanks for the reason - fair, the post read as a launch announcement. I've
rewritten it around the benchmark method and moved the product mention to one
line at the end. Is it OK to resubmit, or is there a better Squad for it?
```

Don't repost after a decline. Fix the post and resubmit once. If the platform removes it, contact daily.dev support with the post URL and your fix; reversal is not guaranteed.

**Before sending any draft:** run it through your preferred humanizer skill, then rewrite it in the poster's own voice. daily.dev screens for AI-characteristic text.

## 11. Metrics

Targets are self-set, because daily.dev publishes no organic benchmark.

- **Reputation per poster**, weekly, until 250.
- **Per post at day 3:** impressions, unique reach, upvotes, comments, clicks. Use UTM-tagged links for referral sessions and signups.
- **Squad, monthly:** members, upvote ratio, clicks, new members per Boost.
- **If you buy an Ads plan:** install the daily.dev conversion pixel.
- **Hygiene, pass threshold zero:** declined posts, removals, reputation drops.

## 12. Next actions

1. Answer the four open questions in section 3.
2. Choose the one named poster for next week's post.
3. Name the comment owner.
4. Check each candidate Squad's gate and rules card in the composer.
5. Tell the 15 engineers to read the platform rules and, if they want to take part, start commenting. Give them no upvote instruction and no schedule.