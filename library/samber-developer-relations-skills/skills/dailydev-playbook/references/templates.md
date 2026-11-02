# daily.dev templates

Adapt each template; never paste one unchanged into two places. Run every draft through your preferred humanizer skill, then rewrite in your own voice: daily.dev screens for text with AI characteristics.

## Earn-first comment

```text
// ✓ Good - adds a measured fact the author and readers can use, no link
We hit the same p99 spike after moving to HTTP/2. In our case it was the
client pool closing idle connections after 60 s, so the first request after
a quiet period paid a new TLS handshake. Pinning keep-alive to 90 s cut it
from 410 ms to 120 ms. Did your trace show handshakes?

// ✗ Bad - praise plus product link, earns downvotes and no reputation
Great article! We built {product} to fix exactly this: {url}
```

## New Post with commentary (your own article)

```text
Title: How we cut cold starts from 900 ms to 120 ms on {runtime}
Commentary:
I work on {product}; this post uses it for one step, and the trade-offs
section says where it falls short. The three changes that mattered: {one
line each}. The benchmark script is in the repo linked at the end. What
cold-start numbers do you see on {runtime}?
Audience: Everyone + {Squad A} + {Squad B} (gates checked: {gate A}, {gate B})
```

## Sharing someone else's post into your Squad

```text
Why this is worth 8 minutes: the section on connection draining matches what
we saw in {incident}. One thing it skips: {gap}. If you run {stack}, check
{setting} before trying the fix.
```

## Squad description (vendor Squad)

```text
{Topic} for people building with {stack}. Tutorials, release notes with
migration steps, and questions from the {product} team and its users.
No sales posts. Ask anything; a maintainer answers within a day.
```

## Squad rules (pick up to 10)

```text
1. Technical content only. Why it matters: members joined to learn, not to be sold to.
2. One link per post, with your own summary. Why it matters: a bare link tells nobody why to click.
3. Disclose affiliation. Why it matters: readers trust a post that says who wrote it.
4. No affiliate or referral links. Why it matters: daily.dev bans them platform-wide.
5. English only. Why it matters: daily.dev removes non-English posts.
6. Be kind in comments. Why it matters: questions stop when answers sting.
```

## Squad poll

```text
Question: How do you run database migrations in CI?
Options: Before deploy, blocking / After deploy, expand-contract / Manually / We don't
Follow-up comment from you: what each answer broke for us, one line each.
```

## Invitation message (existing community or newsletter)

```text
We opened a {product} Squad on daily.dev: tutorials and release notes with
the migration steps, in the feed you already read. Join if useful: {invite link}.
```

## Reply to a declined Squad post

```text
Thanks for the reason - fair, the post read as a launch announcement. I've
rewritten it around the benchmark method and moved the product mention to one
line at the end. Is it OK to resubmit, or is there a better Squad for it?
```

## Reply to a critical thread about your product

```text
I work on {product}. You're right that {fact they got right}. The part about
{claim} changed in {version}: {one-line fact}. Happy to share the benchmark
if useful.
```

No link unless someone asks; never ask teammates to upvote the reply.

## Disclosure lines

- First line of commentary: "I work on {product}; {what this post uses it for}."
- Never add an affiliate or referral link, even disclosed: daily.dev bans them.
