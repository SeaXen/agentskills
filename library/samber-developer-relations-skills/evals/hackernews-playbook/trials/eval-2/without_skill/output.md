**Don't do a Show HN that points at the waitlist page.** HN's Show HN rules exclude sign-up pages, and a demo video behind a waitlist is a poor fit. Expect it to be flagged or demoted, which means near-zero signups. A day-old account also gets extra scrutiny.

Next step: decide today whether you can ship a no-signup demo by Tuesday night (option A below).

## Options, ranked

**A. Make something tryable, then Show HN (recommended, about 1–3 days of work).**
- Put a public, read-only demo environment on the product, with sample data and no login or email.
- Alternatively, open-source one piece (a CLI, agent, query engine, or sample dataset) that people can run locally.
- The waitlist becomes the next step after the demo, not the gate to it.

**B. Plain submission of an engineering write-up (about 1 day).**
- Write a post on a hard technical problem you solved, with real numbers and trade-offs. Submit it as a normal link, not Show HN.
- Put the waitlist in the footer and in your comment.
- Signups will be fewer, but it is allowed.

**C. Wait for December.** If the product can't be tried until then, a Show HN will work better when it can.

## Draft for option A

**Title** (factual, no superlatives):
`Show HN: Acme – [what it does in one plain sentence] (live demo, no signup)`

**URL:** the demo, not the landing page.

**First comment**, posted within a minute of submitting. Fill the brackets with real details:

> Hi HN, I'm [name], [role] at Acme Observability. We're a team of 9.
>
> We built this because [one concrete problem you hit, with a number or incident].
>
> What's different technically: [2–3 specifics, such as storage format, query model, ingestion cost, or sampling approach]. What it doesn't do yet: [honest limitation].
>
> The demo runs on sample data and needs no signup. The full product is invite-only until December. If you want in earlier, the waitlist is at [link]. Everyone who joins from this thread gets access first.
>
> Happy to answer questions about [specific technical areas].

## Getting the most signups from this

1. Put the demo video on the demo page, not just on the waitlist page.
2. Add a persistent in-demo banner: "Want this on your own data? Join the waitlist." Promise early access only if you will honour it.
3. Tag the link with a `?ref=hn` UTM parameter so you can measure conversion.
4. Answer every comment for the first 2–3 hours, with at least one person on call the whole time. Critical comments get the most careful replies.
5. Use the `acmeobs` name in comments and disclose you work there. Don't hide the affiliation.

## Rules that get you killed

- Don't ask anyone to upvote, in Slack, on X, or by email. Don't have the team vote from one office network. HN detects it and can ban the account.
- Sharing the link with your team "for awareness" is fine. Coordinated voting is not.
- Don't repost within 24 hours if it sinks.
- If it's wrongly killed, email hn@ycombinator.com once.

## Account fix (this week, 15 min a day)

- The account is one day old with no karma. Leave 5–10 useful comments on observability or infra threads before Wednesday.
- Add real technical experience, not links to your product.

## Timing

- Post Tuesday–Thursday, around 8–9 AM Pacific.
- The post is only as good as what people can open, so freeze the demo by Tuesday night.

## What I'm assuming

I don't know what Acme does, so the title, problem line, and technical specifics are placeholders. I also haven't verified that a public demo is feasible for you. If it isn't, option B is the next best.

**Next:** tell me (1) what the product does in one sentence and (2) whether a no-signup demo is possible by Tuesday. I'll then write the final title and first comment.