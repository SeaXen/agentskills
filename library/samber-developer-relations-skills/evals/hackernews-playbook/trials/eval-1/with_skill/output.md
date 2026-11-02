# Shiftlog Show HN: what I can't do, what's wrong, and what to do next

## Next action

1. Cancel the 9am upvote plan today. Send the staff note at the bottom.
2. Rewrite the title, body and first comment yourself, from scratch. Use the shape below.

## Refusals triggered

- ❌ **I won't polish or write your title, body or first comment.** HN bans generated and AI-edited text in posts and comments. Moderators ask for "not even a tiny bit" [HN]. I'm naming the problems and giving you the shape instead. A human proofreader is fine.
- ❌ **Don't tell the 6 teammates to upvote at 9am.** Solicited votes penalize or ban submissions, accounts and whole sites [HN]. Voting rings are detected [HN]. A coordinated burst from one team is the pattern HN looks for. Booster comments are "the worst mistake you can make" [HN].
- ❌ **Don't ask them to comment either.** Same rule.

## Problems in your draft

| Where | Problem | Rule |
|---|---|---|
| Title: "the fastest" | A superlative, and unprovable. | Marketing words and superlatives sink or get edited [HN]. |
| Title: "smartest" | An adjective that says nothing. | Same. |
| Title: "never write a migration again" | A tagline. It doesn't say what the tool does. It also invites the top comment, "what about renames and data migrations?" | Titles are neutral and factual. Moderators restore the original or a neutral phrase [HN]. |
| Title shape | No plain statement of the thing: a CLI that diffs Postgres schemas and generates migrations. | Shape is `Show HN: <Name> – <what it does, in plain words>`, under 80 characters. |
| Body: "landing page copy" | HN readers read it as promotion. | Marketing words are penalized [HN]. |
| Body: the feature list | A feature list is what HN dislikes most in a Show HN text. | Feature lists are in the do-less list [HN]. |
| Body: no author voice | Nobody says who they are, where they hit the problem, or how it works. | Required paragraph shape, below. |
| Body: no limits | No mention of what it doesn't do. | An honest "doesn't do yet" earns trust. |
| Body: no comparison | Readers know existing Postgres diff and migration tools. Silence reads as hiding. | Name the alternatives honestly. |

## Example to rewrite, not paste

This is for a fictional product, not Shiftlog. It shows the shape only.

```
// ✓ Good - names the thing and what it does, no adjectives
Show HN: Litequeue – a job queue that runs inside SQLite

// ✗ Bad - superlative, hype, version bump, site name
Show HN: The fastest job queue ever! v2.1.3 is out | litequeue.dev
```

**Shape for the text field**

Write one paragraph for each item. No bullets, no feature list.

1. Who you are.
2. What it does, said differently from the title.
3. The problem, and where you hit it.
4. How it works technically.
5. What's different from the tools readers already use, named honestly.
6. What it doesn't do yet.
7. How to try it without signup, linking the repo or a binary.
8. License and how you make money. Yours is MIT, so say so plainly.
9. Earlier HN threads, if any.
10. One real open question for readers.

The full fictional example is in `references/templates.md`. Read it, then close it and write your own.

## The first comment

- Put your text in the **text field**.
- Post a first comment only if the text field doesn't show [HN].
- Don't paste the same text twice.
- Don't use the first comment to add the landing-page pitch you cut from the body.

## Account readiness: unknown

- ⚠️ **Who submits?** It must be a person's account, not a company-named one [HN].
- ⚠️ **How old is it, and what comment history does it have?** New accounts are blocked from Show HN, with no published threshold [HN].
- I'm assuming it's a personal account and it's fine. Check it before tomorrow. If it's new, no wording fixes that.

## Timing: your premises don't hold

- ⚠️ **Date mismatch.** You said "tomorrow" and "Tuesday". Today is Friday 2026-10-30, so tomorrow is Saturday 2026-10-31. Which date is it?
- **"9am PT Tuesday is the best time" is not an HN rule.** It's [practitioner] data, and it conflicts with itself:
  - One dataset finds the best odds near 00:00 UTC and on weekends.
  - The best mean scores come at 12:00-15:00 UTC on weekdays. 9am PT is 16:00 UTC, just after that window.
  - Best and worst slots differ about fourfold. About nine in ten posts even at the best slot stay under 50 points.
  - dang calls `/newest` a lottery [HN].
- **Pick the slot when the author can stay six hours.** Answer the top-ranked questions first, in page order.

## What the ranking rewards

- Early votes from readers who found it themselves [HN].
- A no-signup path that survives load: a binary or a `go install` line works. Pricing is moot, since it's MIT.
- Calm replies. Overheated threads are demoted [HN].

## Cadence

1. **Before posting:**
   - Confirm the account.
   - Make sure the README quickstart runs in about two minutes, cold, on a clean machine.
   - Note baselines for stars, installs and referrals.
2. **Launch day:**
   - Submit when the author can stay six hours.
   - Reply to critics as in the example below, one person per thread.
3. **Days 1-2:** capture stars and emails now. Most front-page stars arrive within 48 hours [practitioner].
4. **If it flops:**
   - Don't delete and resubmit [HN].
   - A small number of reposts is fine if it got no significant attention, about a week apart [practitioner].
   - Or email hn@ycombinator.com once for the second-chance pool.

## Limits that bind you

| Limit | Kind |
|---|---|
| Show HN needs something tryable. A landing page isn't enough. | enforced [HN] |
| Title must start with "Show HN" or it never reaches `/show`. | enforced [HN] |
| No AI-edited text anywhere in posts or comments. | enforced [HN] |
| Don't comment about votes or flags in the thread. | enforced [HN] |
| One person answers per question. Colleagues don't pile in. | [HN] |
| Edit window on comments is about 2 hours. | enforced, number [practitioner] |

## Replying to critics: example to rewrite

```
// ✓ Good - agrees first, answers with a fact, says what changes
You're right that the README oversells the throughput. The 2,000 jobs/s figure
is from a VPS with a local NVMe disk; on network storage I measured about 300.
I'll put both numbers in the README today.

// ✗ Bad - defends, addresses the user, insinuates
@foo123 you clearly didn't read the docs. Are you from <Competitor>?
```

Shape: what's right in the criticism, then the fact that answers it, then what you'll change or why you won't. Never call critics shills.

## Metrics

- Points and comments at 1 h and 6 h. The median Show HN gets 2 points, and 50+ is the top 6% [practitioner].
- Stars, installs and referrals per day for 7 days, against your baseline.
- Comments on others' threads should stay the majority of the account's activity.

## Internal staff note (finished text, send as is)

> We're posting a Show HN today. Please don't upvote it, don't post the link in team, community or social channels, and don't comment to praise it. HN detects this and can penalize the post, our accounts and our domain. <Author> answers the thread; send technical points to them instead of commenting. If someone is rude, don't reply; tell <Author>.

## Questions I need answered

1. Which date is the launch, Saturday 2026-10-31 or Tuesday 2026-11-03?
2. Who posts, and how old is that account? What is its comment history?
3. Who stays in the thread for six hours, and in which time zone?

I did not re-read `newsguidelines.html`, `showhn.html` or `showlim` this session. Rules move, so skim them before you post.