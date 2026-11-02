# Bluesky templates

Examples for a fictional company, Quillfeather, and its advocate Ines. Adapt every line to the person posting and rewrite it in their own voice; never post these as written.

## Contents

- Profiles and handles
- First posts
- Replies
- Starter pack asks and descriptions
- Feed posts and operator asks
- Bot account
- Disclosure lines
- Cross-post rewrite
- Launch day

## Profiles and handles

```
Handle: ines.quillfeather.dev
Display name: Ines Okafor
Bio: Developer advocate at Quillfeather (log search for Postgres). I write about query plans and bad indexes. Posts are mine.

Handle: quillfeather.dev
Display name: Quillfeather
Bio: Log search for Postgres. Releases, docs, status. People who build it: [starter pack link]. Support: docs.quillfeather.dev/help
```

```
// ✗ Bad - brand handle on the default domain, no person, no disclosure
Handle: quillfeather-official.bsky.social
Bio: 🚀 The #1 AI-powered log platform! Follow for tips!
```

## First posts

```
New here. I spend most days inside Postgres EXPLAIN output and the rest arguing that most slow queries are a missing index. Looking for people who run Postgres in production: who should I follow?
```

```
// ✗ Bad - broadcast, no question, link-first
Quillfeather is now on Bluesky! 🎉 Check out our AI log platform: quillfeather.dev #Postgres #AI #DevOps #Startup #Tech
```

## Replies

```
Seen this exact plan shape. The seq scan is fine until the table passes a few million rows; a partial index on (status) WHERE status = 'pending' fixed ours. Happy to look at the plan if you post it.
```

```
(Disclosure: I work on Quillfeather, which does log search.) For your case pg_stat_statements alone gets you most of the way; you only need a tool once you're correlating across services.
```

## Starter pack asks and descriptions

To a curator, as a public reply first (by default only people a user follows can DM them), one person per ask:

```
Hi Mara, thanks for the Postgres people pack, it's how I found half my timeline. Would Ines (ines.quillfeather.dev) fit? She posts weekly about query plans and answers questions in the Postgres feed. No worries if the pack's scope is different.
```

Your own pack, curating the community:

```
Name: Postgres in production
Description: People who run Postgres for real and post about it: DBAs, maintainers, extension authors. Plus the Postgres feed. Suggestions welcome in replies.
Members: 40 community people, 2 from Quillfeather.
```

Announcing it, once, in a normal post (never by DM):

```
Made a starter pack of people who run Postgres in production and post about it. 40 people, mostly not us. Who's missing?
[pack link]
```

```
// ✗ Bad - a staff directory dressed as a community pack
Name: Quillfeather team
Members: 12 Quillfeather employees + the brand account
```

## Feed posts and operator asks

```
Wrote up why our planner picked a nested loop over a hash join on a 40M-row table, with the EXPLAIN output. #PostgreSQL
[link to the post]
```

To a curated feed's operator:

```
Hi, I run the Postgres pack and post about query plans most weeks. Is your Databases feed open to new accounts? If not, no problem.
```

## Bot account

```
Handle: release-bot.quillfeather.dev
Display name: Quillfeather releases (bot)
Bio: Automated. Posts each Quillfeather release. Replies only if you mention it. Run by @ines.quillfeather.dev.
Settings: bot label on.
```

## Disclosure lines

```
I work at Quillfeather.
Sponsored by Quillfeather; they paid for this post.
Affiliate link: I earn a commission if you sign up.
```

## Cross-post rewrite

```
X original (thread, 4 posts, x.com quote, image without alt text)
Bluesky version: one post, 280 characters, the key finding first, link to the blog post, alt text on the chart, no x.com link, no "1/4".
```

## Launch day

```
Person who built it, own account:
I've spent a year on this: Quillfeather can now search 30 days of Postgres logs in under a second on a laptop. Free tier, no card. What I'd love feedback on: the query syntax. [link] #PostgreSQL

Brand hub: repost Ines, then one release post with the changelog link.
Staff: answer questions in replies with the disclosure line; do not like-bomb the post.
```
