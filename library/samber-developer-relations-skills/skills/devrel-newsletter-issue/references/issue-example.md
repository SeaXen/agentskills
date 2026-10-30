# Worked issue and a negative example

Illustrative scenario, not a real company. It shows the shape, not a house style to copy.

## Scenario

A queue-service vendor sends a monthly own-surface digest with one ecosystem section to 6,000 developers. The charter template: Lead, Shipped (releases and the team's own posts), From the ecosystem, Built by the community, One thing to try, footer. This month: release 3.4 (dead-letter queues GA, a Go SDK beta), one blog post, two ecosystem links, nothing from the community. A monitoring vendor bought the one sponsor slot. The ask: reply with the queue pattern you want covered next.

## Running order presented for approval

1. Lead: dead-letter queues GA
2. Sponsor slot (charter: after the lead)
3. Shipped: Go SDK beta, retry-policy post
4. From the ecosystem: 2 items
5. Built by the community: empty, section dropped this issue
6. One thing to try: evergreen slot from the docs backlog
7. Ask, footer

Subject options:

- "Dead-letter queues are GA in 3.4" (32 characters) - names the lead, safest.
- "3.4: dead-letter queues, Go SDK beta" (36) - two items, weaker lead.
- "Stop losing poison messages" (27) - benefit-led, but names no version and reads closer to marketing.

## The issue (excerpt)

**Subject:** Dead-letter queues are GA in 3.4
**Preview:** Failed messages now park instead of vanishing. Plus: a Go SDK beta and what retry storms cost a payments team.

**Lead**

**[Dead-letter queues are generally available](https://example.com/changelog/3-4)**
You can now route messages that fail every retry to a dead-letter queue instead of dropping them. Available on every plan from 3.4. Set `dead_letter: true` on the queue to turn it on.

**Sponsor**

**[Trace one message across five services](https://example.org/sponsor-link)**
A short guide to following a message ID through producers, brokers and consumers.

**Shipped**

- **[Go SDK beta](https://example.com/go-sdk)** - publish and consume from Go 1.22+; the API may change before 1.0.
- **[Choosing a retry policy](https://example.com/blog/retry-policy)** - when exponential backoff beats a fixed delay, with the numbers from our own load test.

**From the ecosystem**

**[What a retry storm cost us](https://example.net/retry-storm)**
A payments team describes how synchronised retries took their queue down for 40 minutes, and the jitter change that fixed it. Useful if your consumers retry on a fixed schedule.
R. Okafor (Example Payments)

**One thing to try**

Inspect a stuck message without consuming it:

```
qctl peek orders --count 1
```

**Reply to this email** with the queue pattern you want covered next month.

**Footer:** Submit an item: reply or open an issue in the newsletter repository. Spotted an error? Reply and we will fix the archive. Archive · Unsubscribe · sender address.

## Why each choice

- The lead release follows capability, availability, first step. No "excited", no benchmark.
- The opener is absent: nothing changed in schedule or format.
- The empty community section is dropped, not padded with a forum post nobody would forward.
- The retry-storm item states the source's own figure (40 minutes) and attributes it.
- The sponsor sits in its fixed slot with one link and the house label.
- The code is one line of live text.

## Negative example

```
Subject: 🚀 October Newsletter - Big News Inside!
Preview: View this email in your browser

Hi there! Welcome to the October edition of our newsletter! It's been an
incredibly exciting month here and we can't wait to share everything with you.

We're thrilled to announce our game-changing Dead-Letter Queues, which make
message handling seamless and up to 10x more reliable! Read more >>

[image: screenshot of a 25-line config file, alt="code"]

Also check out the Go SDK! Click here. Star us on GitHub! Join our Discord!
Follow us on X! Register for our webinar!

Featured: Trace any message, instantly, with the industry's best observability.
```

What fails:

- The subject names no item; the preview falls back to "View this email in your browser".
- The opener spends 26 words, past the 25-word ceiling, saying nothing changed.
- Hype words, an unsourced "10x more reliable", and no availability or first step.
- "Read more" and "Click here" as link text.
- Code as an image with useless alt text, too long for the issue anyway.
- Five competing asks.
- The sponsor copy carries no label and reads as editorial.
