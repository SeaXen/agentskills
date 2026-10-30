# Hacker News templates

Every HN-facing template below is a full **example** for a fictional product. It shows shape and tone only. HN bans generated and AI-edited text, so the human rewrites it from scratch, in their own words, about their own work before posting. Never fill these with the user's product details: hand over the example and the shape, never a draft to paste. Only the internal staff note is finished text, because it never reaches HN.

## Show HN title

> Example - rewrite in your own words before posting.

```
// ✓ Good - names the thing and what it does, no adjectives
Show HN: Litequeue – a job queue that runs inside SQLite

// ✗ Bad - superlative, hype, version bump, site name
Show HN: The fastest job queue ever! v2.1.3 is out | litequeue.dev
```

Shape: `Show HN: <Name> – <what it does, in plain words>`. Keep it under 80 characters. Start with "Show HN", or the post never appears on `/show`.

## Show HN text field (post it as the first comment only if it does not show)

> Example - rewrite in your own words before posting.

> I'm Maya, and I maintain Litequeue, a background job queue that stores jobs in the SQLite file your app already uses.
>
> I run a few small web apps on single servers. Each one needed background jobs, and each time the choice was a Redis instance I had to babysit or a cron script that lost jobs on deploy. I wanted jobs to live in the same file as the data, so a backup is one copy and a transaction can enqueue a job atomically with the row that triggered it.
>
> Workers claim jobs with a single UPDATE ... RETURNING inside a short write transaction, so two workers never grab the same job. WAL mode lets readers keep going while a worker writes. On a cheap VPS it sustains about 2,000 jobs per second, measured with the benchmark script in the repo; a dedicated broker will do far more.
>
> What it doesn't do: no multi-machine workers, since SQLite is one file on one disk, and no priorities yet. If you need either today, a broker is the better tool.
>
> The repo has a two-minute quickstart, no signup: github.com/example/litequeue. It's MIT-licensed, and I don't plan to sell anything around it.
>
> I'd like to hear from people running jobs on SQLite in production: what broke first?

Shape, one paragraph each, no feature list: who you are; what it does, said differently from the title; the problem and where you hit it; how it works technically; what's different from tools readers use, named honestly; what it doesn't do yet; how to try it without signup, linking the repo or demo itself; license and how you make money; earlier HN threads, if any; an open question.

## Reply to a critic

> Example - rewrite in your own words before posting.

```
// ✓ Good - agrees first, answers with a fact, says what changes
You're right that the README oversells the throughput. The 2,000 jobs/s figure
is from a VPS with a local NVMe disk; on network storage I measured about 300.
I'll put both numbers in the README today.

// ✗ Bad - defends, addresses the user, insinuates
@foo123 you clearly didn't read the docs. Are you from <Competitor>?
```

Shape: what's right in the criticism, or the good intent behind it; the fact, measurement or trade-off that answers it; what you'll change, or why you won't.

## Disclosure in a thread about your product or a competitor

> Example - rewrite in your own words before posting.

```
Disclosure: I work on Litequeue. For the dead-job problem you describe, we
lease jobs with a timeout and requeue them on expiry; the trade-off is a
duplicate run if a slow job outlives its lease, so jobs need to be idempotent.
```

One mention, only when it answers the question. Never in a competitor's Show HN unless asked directly.

## Who is hiring post

> Example - rewrite in your own words before posting. Job posts fall under the same AI-text ban.

```
Fernwood Labs | Backend engineers (Go), SRE | Lyon, France | REMOTE (EU) | Full-time | €70k-95k
We build a feature-flag service used by about 400 engineering teams; flags
are evaluated in the customer's own process via SDKs, so latency budgets are
in microseconds.
Backend: the flag evaluation engine and its sync protocol. SRE: our
multi-region Postgres setup and the on-call we're making quieter.
Apply: jobs@fernwood.example - a human reads every email, and we reply within
a week either way.
```

Shape: company, roles, location, `REMOTE` / `REMOTE (region)` / `ONSITE`, contract, salary range if you publish one; what the company does; what the roles work on; how to apply and a reply promise you'll keep. One post per company per month, written by someone at the company, only while the roles are open.

## Launch HN (YC companies only)

> Example - rewrite in your own words before posting.

```
Launch HN: Fernwood (YC W26) - Feature flags evaluated inside your process
```

Under 80 characters, neutral and factual tagline. Fill HN's form first; staff decide, and each startup gets one Launch HN. The text follows the Show HN example's shape, plus how you make money. Don't time it with press. It makes your YC funding public.

## Second-chance pool request (email to hn@ycombinator.com)

> Example - rewrite in your own words before sending.

```
Subject: Second-chance pool: https://news.ycombinator.com/item?id=<id>

This Show HN covers enqueueing jobs atomically with the rows that trigger
them in SQLite, which I think HN readers who run small servers would find
useful. Disclosure: it's my own project. Thanks for considering it.
```

Send once. Moderators act on pool requests but may not reply.

## Internal staff note (finished text, never posted on HN)

> We're posting a Show HN today. Please don't upvote it, don't post the link in team, community or social channels, and don't comment to praise it. HN detects this and can penalize the post, our accounts and our domain. <Author> answers the thread; send technical points to them instead of commenting. If someone is rude, don't reply; tell <Author>.
