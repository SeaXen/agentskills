**I can't fix the grammar of your text.** HN bans generated and AI-edited text in posts, and moderators ask for "not even a tiny bit" [HN]. Fixing grammar and rewriting wording are the same act under that rule. I also can't machine-translate it. Imperfect English reads better on HN than polished LLM text. A human proofreader is fine, for example a colleague or a friend.

## 1. Should you post at all? Read this first

Assumptions, since I did not ask: your account is old enough to post Show HN, and you can stay in the thread for six hours.

- **Eligibility is doubtful.** HN's Show HN page excludes "minor releases" [HN]. A new version qualifies only if it is significantly different, at most once or twice a year, and you link the old thread [HN]. Moderators decide, and I can't predict their call. "Faster encoder, new hooks, bug fixes" reads like a minor release.
- **A flop here costs you.** Reposts are only for stories that got no attention [HN]. A weak v1.4 post could hurt later launches.
- **Better option:** submit a regular post about *how* you made the encoder 2x faster, if it teaches something. Your own submissions should stay "part of the time" [HN].

## 2. Problems in your text (named, not rewritten)

| Problem | Rule |
|---|---|
| "most fast" is a superlative. HN readers distrust it. | Superlatives and marketing words [HN] |
| "very happy to present" is promotional filler. | Marketing words [HN] |
| "New: encoder 2x faster, new hooks, bug fixes" is a bare feature list, with no explanation. | Feature lists [HN] |
| "2x faster" has no benchmark, hardware or comparison, so nobody can check it. | Readers want facts they can verify [practitioner] |
| "Try it!" gives no link and no path to try it without signup. | A tryable link is required [HN] |
| It lacks who you are, the problem, how it works, what it does not do, the license, and an open question. | Templates shape |
| "We" reads as a company voice. | Post from your own personal account [HN] |

**Title:** it must start with `Show HN:` or the post never reaches `/show` [HN]. Use this shape: `Show HN: <Name> – <what it does, plain words>`. Keep it under 80 characters, with no version number, no site name and no adjectives. Compare the fictional example from `references/templates.md`:

```
// ✓ Good - names the thing and what it does, no adjectives
Show HN: Litequeue – a job queue that runs inside SQLite

// ✗ Bad - superlative, hype, version bump, site name
Show HN: The fastest job queue ever! v2.1.3 is out | litequeue.dev
```

For the body, the template's shape is one short paragraph for each of these:
1. Who you are.
2. What the project does.
3. The problem and where you hit it.
4. How it works technically.
5. What is different from other tools, named honestly.
6. What it does not do yet.
7. How to try it, linking the repo or demo itself.
8. License and how you make money.
9. The earlier HN thread (link your v1 thread, as the rule requires).
10. One open question.

Write it yourself, in your own English.

## 3. Do not do these

- Do not ask the team, Discord, GitHub or a newsletter to upvote or comment. This penalizes or bans posts, accounts and domains [HN]. Booster comments are "the worst mistake you can make" [HN].
- Do not delete and resubmit if it sinks [HN].
- Do not call critics shills or brigaders [HN].

Send this internal note to your team. It is finished text and never goes on HN:

> We're posting a Show HN today. Please don't upvote it, don't post the link in team, community or social channels, and don't comment to praise it. HN detects this and can penalize the post, our accounts and our domain. <Author> answers the thread; send technical points to them instead of commenting. If someone is rude, don't reply; tell <Author>.

## 4. Timing

Tomorrow is Saturday, 31 Oct 2026. One dataset finds the best odds near 00:00 UTC and on weekends [practitioner]. About nine in ten posts at the best slot still stay under 50 points [practitioner]. dang calls `/newest` a lottery [HN]. Post only if you can stay in the thread for six hours, answering the top-ranked questions first.

## 5. Limits that bind

- **Show HN:** the product must be tryable and your own work, and minor releases are excluded. [HN, enforced]
- **Show HN:** a new version is allowed once or twice a year, linking the old thread. [HN, policed]
- **All posts:** no AI-edited text. [HN, enforced]
- **Reposts:** only if the story got no significant attention. [HN]

## 6. After posting

- If it sinks, check it logged out with `showdead` on. Then email hn@ycombinator.com once. Moderators may offer the second-chance pool.
- Never comment about votes or flags in the thread [HN].
- Collect stars and emails in the first 48 hours [practitioner].
- Track points and comments at 1 h and 6 h. The median Show HN gets 2 points, and 50+ is the top 6% [practitioner].

## 7. What I need from you

1. Is the v1.4 encoder rewrite a significant change, or an optimization pass?
2. Can you publish a benchmark (hardware, method, before and after)?
3. Do you prefer a regular post about the encoder work, or a Show HN?