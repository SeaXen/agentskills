# Medium templates

Fictional examples. Adapt every line to the real story; run drafts through a humanizer pass.

## Disclosure lines

- Affiliation, first paragraph: "I work on Tidepool, the queue this post uses; the limits section covers where it falls short."
- AI assistance, within the first two paragraphs: "This story was written with the assistance of an AI writing program; the benchmarks were run and checked by me."
- AI image caption: "This image was created using an AI image creation program."
- Offsite link, right next to it: "Subscribe to our engineering newsletter (this link leaves Medium)."
- Value received, first paragraph: "Tidepool gave me free credits to run these benchmarks."
- Affiliate link, footer: "This post includes affiliate links; I may earn a commission if you buy through them."

## Earn-first response

```text
// ✓ Good - adds a fact the author can use, no link
We hit the same lock contention with SKIP LOCKED once workers passed 40:
the fix was batching claims 50 at a time, which cut p99 from 900 ms to
120 ms. Did you try batch sizes, or did partitioning come first?

// ✗ Bad - praise plus product link, reads as promotion through responses
Great article! Tidepool solves exactly this, check it out: tidepool.dev
```

## Story skeleton (Boost candidate)

1. The incident or decision, in the first paragraph, with one number.
2. What you tried first and why it failed.
3. What you changed, with code blocks and a diagram you made.
4. Results, measured, and what still does not work.
5. One call to action at the end: the repo, the docs page, or the free tier.

Title: what happened and to what. Subtitle: the result. Cover: your own diagram or none.

```text
// ✓ Good
How we cut Postgres queue latency from 900 ms to 120 ms
Batching claims, partial indexes, and the one change that made it worse

// ✗ Bad - generic, product-first
Introducing Tidepool 3.0: The Ultimate Queue for Modern Teams
```

## Pitch to a publication editor

Use the publication's own channel (its form, email or submission queue).

```text
Subject: Submission - "How we cut Postgres queue latency from 900 ms to 120 ms"

Hi {editor name},

I'm an engineer at Tidepool. This draft covers a production incident:
lock contention at 40 workers, three fixes, benchmarks and one that
backfired. About 1,800 words, 3 diagrams, original to your publication.

It names our product once, in the closing paragraph, with a link to the
open-source repo. Happy to drop that line if it breaks your guidelines.

Draft: {Medium draft link}
{name}
```

## Company publication guidelines page

```text
Write for {Company} Engineering

Who: {Company} engineers and invited partners. Partners keep all
rights to their stories; submitting grants us nothing extra.
What: incidents, migrations, benchmarks, architecture decisions,
told by the person who did the work.
Not: product announcements (they go on {brand account}), sponsored
content, AI-written drafts.
How: publish on your own account, canonical link to
{company blog URL} if it ran there first, then Submit to publication.
Paywall: off.
Topics: up to 5, each one the story is about.
AI: no AI-generated drafts; label AI assistance within the first
two paragraphs.
```

## Canonical check before publishing

1. Story settings > More settings > Advanced settings shows the original URL.
2. Published page source contains `rel="canonical"` pointing at the company domain.
3. Paywall toggle off; topics chosen; AI label present when needed.
4. Submitted to the company publication; featured if it is the week's best.
