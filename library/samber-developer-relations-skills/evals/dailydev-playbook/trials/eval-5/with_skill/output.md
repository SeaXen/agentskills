# Why Hexmesh's daily.dev posts get no reach, and the 8-week fix

**Next action:** stop posting release links today, and have all three engineers start commenting on posts in your stack's tags. The causes below are mostly rule violations plus a reputation gap, not bad luck.

I followed `dailydev-playbook`. Labels: **[platform]** is daily.dev's own docs, **[practitioner]** is community observation, **[self-set]** is a default from the skill with no platform number behind it. daily.dev publishes no ranking formula and no organic benchmark, so I can't say whether 40 views and 1 upvote is "normal". The causes are still clear from the rules.

## 1. Verdict on each thing you're doing

| What you do | Verdict | Why |
|---|---|---|
| Release link + "check out what's new!" | ❌ Pitch-only post | A bare link tells nobody why to click. Self-promotion as the main purpose is rejected or demoted [platform]. Each downvote lowers the post's ranking [platform]. |
| "You won't believe how fast Hexmesh 2.4 is" | ❌ Clickbait | Clickbait titles get demoted, and Plus readers see them rewritten [platform]. The title also makes a claim the post doesn't back with a method or a number. |
| Three engineers, every release | ⚠️ Likely repeat links | Post each link once per Squad [self-set]. If all three post the same release, that is repeat linking, and it reads as coordination if the teammates upvote each other. I need your answer to question 1 below. |
| Accounts at 10-30 reputation | ❌ Main cause of low reach | High-reputation authors' posts and comments get ranking priority [platform]. Reputation starts at 10, so your accounts have barely moved. Votes from accounts under 250 add nothing to the author [platform]. |
| No affiliation line | ⚠️ Missing | Authors must state their affiliation [platform]. A vendor post with no "I work on Hexmesh" line reads as an undisclosed ad. |
| Posting to the feed with no commentary | ❌ Wasted slot | Commentary on a New Post is where a vendor earns trust. A link with a one-line hype caption gives readers no reason to read. |

## 2. Why reach is bad

1. **Reputation gap [platform].** Ranking favours high-reputation authors, and you are at 10-30. Reaching 250 takes about five comment upvotes from established members (+50 each, counted only from voters with 250+ reputation). Release-link posts don't earn that.
2. **Post type.** A release link is a teaser or pitch. Nothing in it gives a reader a reason to read, upvote or comment, and the ranking rewards early reads and upvotes [platform]. The window length is unpublished.
3. **Title.** A clickbait title is demoted [platform].
4. **Possibly no tag match.** Tags are your targeting: personalized feeds match the tags readers follow [platform]. I don't know which tags you used. Release links are often tagged with the product name alone, which nobody follows yet.
5. **Possible Squad gates.** If the engineers posted into third-party Squads with a reputation gate (commonly 250 or 1,000) or with moderator approval, the posts may have been blocked or declined. Check each post's status. A decline or removal also costs reputation (-100 for a removed post).

## 3. Why DEV-picked articles show no author

This is a known cause, and it is fixable.

- daily.dev picked them up from DEV as an indexed publication, and the author is unclaimed.
- To claim authorship: add `<meta name="twitter:creator" content="@handle">` to the post's head, and add the same X handle under Account details on daily.dev.
- For posts picked up before you claimed, email daily.dev support.
- Once claimed, you get a listing notice, an author badge and analytics [platform].

Two caveats:
- **I can't confirm DEV lets you set that meta tag.** Check each post's head after publishing. If DEV doesn't expose it, the support-email route is the fallback. Verify before promising it to the team.
- **Reach on these posts may stay limited.** daily.dev is temporarily prioritizing niche sources, so content from mainstream sources such as DEV may rank lower [platform]. Being picked guarantees a feed slot, not traffic.

## 4. Fit verdict (provisional)

**Invest, conditional.** That holds if developers read your stack's tags, you publish technical posts at least monthly, and someone answers comments daily. You already have DEV articles, which suggests the backlog exists. If questions 3 and 4 below come back thin, switch to **syndicate only**: claim the DEV posts, one curated post a week, no paid spend.

## 5. Entry path

1. **Claim the indexed DEV articles** (section 3). It costs minutes and keeps paying.
2. **Stop release-link posts.** Company and personal blogs cannot be sources, and company sources ended in 2024. Your release notes reach the feed only through New Post, Squad posts, a Verified Company Squad's RSS auto-post (paid), or an unpaid indexed publication.
3. **New Post for real technical posts only**, to the engineer's profile plus at most 3 Squads in total. The docs disagree on whether New Post needs 250 reputation, so check the composer. If it blocks, post inside your own Squad, where admins and moderators are never gated.
4. **Verified Company Squad:** not now. It is sales-assisted with a quarterly commitment. Revisit when you publish weekly and plan to stay for quarters.

## 6. Setup (week 1, each of the three engineers)

- Complete the profile, verify the company badge with a work email, follow your target tags, claim authorship (section 3).
- Use one named personal account each. A brand account is not the carrier [self-set], and multiple accounts per person are banned [platform].
- **Tags (candidates, verify against each tag page's top posts):** the stack the reader works in. For a service mesh that likely means kubernetes, networking, observability, devops, plus your implementation language. Never use "hexmesh" alone.
- **Squads:** pick by topic fit, rules card and a gate the poster meets, never by member count. Gate unknown means "check in composer".

## 7. Ranked surfaces for Hexmesh

| Rank | Surface | Why for you |
|---|---|---|
| 1 | Substantive comments in your tags, no links | Fastest route to 250. Five comment upvotes take an account from 10 to 260. |
| 2 | Author claiming on the DEV articles | Minutes of work, and it fixes the missing-author problem. |
| 3 | Own public Squad, in DevTools or a topic category | Valuable but needs an audience to invite. Seed it first. |
| 4 | Full technical post via New Post (profile + ≤3 Squads) | Replaces the release-link posts. |
| 5 | Curating others' posts into your Squad, with commentary | Cheap, and it shows the Squad has a voice. |
| 6 | Squad poll | One-shot. Good in launch week. |
| 7 | Cross-post to DEV | Indirect pickup, and it may rank lower [platform]. |
| 8 | Post or Squad Boost | Only after organic traction. |
| 9 | Verified Company Squad / Ads plan / Sponsored Content | Not now. |

What moved: I don't yet know your answers to interview questions 2, 4 and 5. A launch date inside four weeks would promote New Post and a short Boost. Under 2 hours a week per person would cut the plan to comments, claiming and one curated post.

## 8. Eight-week cadence

Hours are my assumption: about 1.5 h/week per engineer [self-set]. Change them if yours differ.

| Weeks | Owner | Work |
|---|---|---|
| 1-3, earn first | Each engineer | Comment substantively on 3-5 posts a week in your tags, with no links. Complete profiles and claim authorship. |
| 1 | Tech lead | Pause release-link posts. Check every past post for declines or removals. |
| 2, build the Squad | One owner (name them) | Public, closest category (DevTools), image, cover, description, Stack & Tools, rules, posting mode "Require post approval", Slack integration on. Seed 5-10 curated posts with commentary before inviting anyone. |
| 3, invite | Community owner | Share the invitation link with your existing community and newsletter. Never pay or incentivize joins. |
| 3-8, publish | Engineer with the most reputation | One original technical post a week via New Post to profile + your Squad + at most 2 more. Answer every comment within 24 hours. |
| By week 4 | Rule | Anyone still under 250 posts only in your own Squad. |
| Week 4+ | Launch owner | Hexmesh 2.5 or the next real launch: one strong post plus a Squad poll. Boost only if the post earned organic upvotes in its first 24 hours [self-set]. |
| Monthly | Tech lead | Read post and Squad analytics. Drop tags and Squads that drew nothing. |

**If a release ships before week 4:** post once, from the engineer with the most reputation, into your own Squad plus at most 2 Squads whose gate that account meets. Expect little organic reach, and skip Boost unless the 24-hour rule holds.

**Default ratio:** three non-product contributions (comments, curated shares) per product post, per person [self-set]. daily.dev publishes no promotion ratio.

**Do not** have teammates upvote each other's comments or posts on cue. It reads as reputation farming [self-set], and farming costs points or the account [platform]. Votes from accounts under 250 move nothing anyway.

## 9. Paid decision

**No paid spend this quarter.** Boosting a weak post buys impressions from readers who downvote it. Revisit when:
- a post has earned organic upvotes in its first 24 hours (then a short Post Boost, 1-30 days, is defensible); or
- the Squad has 10+ quality posts (then Squad Boost); or
- you publish weekly and want auto-posting for at least two quarters (then ask sales about a Verified Company Squad).

daily.dev publishes no rate card, so price anything from a written quote. If you have no technical content and nobody to answer, daily.dev's own advice is to start with one Sponsored Content post.

## 10. Filled templates

All numbers are placeholders. Don't publish figures you haven't measured.

**Retitle and reframe (replaces "You won't believe how fast Hexmesh 2.4 is")**

```text
Title: How we cut sidecar proxy memory from {X} MB to {Y} MB in {version}
Commentary:
I work on Hexmesh; this post uses it for one step, and the trade-offs
section says where it falls short. The three changes that mattered:
{change 1}, {change 2}, {change 3}. The benchmark script is in the repo
linked at the end. What proxy memory numbers do you see on {platform}?
Audience: Everyone + {Squad A} + {Squad B} (gates checked: {gate A}, {gate B})
```

**Earn-first comment (no link, no product pitch)**

```text
We saw the same latency spike after enabling mTLS. In our case it was the
proxy re-establishing connections after cert rotation, so the first request
paid a fresh handshake. Raising the rotation overlap window cut it from
{X} ms to {Y} ms. Did your trace show handshakes at the spike?
```

**Squad description**

```text
Service mesh for people building with {stack}. Tutorials, release notes with
migration steps, and questions from the Hexmesh team and its users.
No sales posts. Ask anything; a maintainer answers within a day.
```

**Squad rules:** use the six from `references/templates.md` (technical content only, one link per post with your own summary, disclose affiliation, no affiliate links, English only, be kind).

**Disclosure first line on every Hexmesh post:** "I work on Hexmesh; {what this post uses it for}."

**If a post was declined:** reply with the decline-reply template, fix the post, and resubmit once. Edits need re-approval, and a repeat after a decline reads as spam.

## 11. Metrics

- Reputation per engineer, weekly, until 250.
- Per post at day 3: impressions, unique reach, upvotes, comments, clicks. Use UTM-tagged links for referral sessions and signups.
- Squad monthly: members, upvote ratio, clicks.
- Hygiene, pass threshold zero: declined posts, removals, reputation drops.
- Targets are self-set. Suggested check at week 8: all three accounts at 250+, authorship claimed on every DEV article, no declined or removed posts. That is a goal I'm proposing, not a platform benchmark.

## 12. Questions I need answered

These would change the plan:

1. Do all three engineers post the same release link, or one each? Do they upvote each other?
2. Is there a launch date inside four weeks (for example Hexmesh 2.5)?
3. How often do you publish technical posts, and where?
4. Who answers comments within a day, and how many hours per week can each engineer give?
5. Do you have a community or newsletter to invite into a Squad, and any budget this quarter?
6. Which tags and Squads did the existing posts use? Were any declined or removed?

## Caveats

- I read the skill and its two reference files. I did not check live daily.dev docs, and the skill says to re-check the docs page before quoting a number to a stakeholder. The skill itself notes that the docs disagree on the New Post reputation gate and on the points per upvote on claimed articles.
- I didn't see your posts or accounts. The causes in section 2 come from what you described plus the platform rules.