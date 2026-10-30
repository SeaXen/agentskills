# Candidate sheet example

A worked sheet for a fictional monthly vendor digest, then the padded version an unguided run produces.

## Input

- Product: Quarrystack, a hosted queue with SDKs in three languages. Monthly digest, primary reader: developers already running it.
- Charter sections: Shipped (2-5 items), Heads-up (0-3, action required), Learn (1-3), From the community (1-3, external), Events (0-3). Empty-section rule: drop the section. House share: at least one third external.
- Last issue: sourcing closed 2026-02-04 12:00 UTC. This issue closes 2026-03-04 12:00 UTC and sends 2026-03-06.
- Channels read: release feed, labelled merged-PR query, submissions inbox (9 links), the advisory feed for the three SDK runtimes, docs zero-result searches, community forum.

## Worked sheet

**Window:** 2026-02-04 12:00 UTC to 2026-03-04 12:00 UTC. **Channels:** release feed 3, merged-PR query 5 (2 unreleased), unlabelled sweep 1, submissions 9, advisory feed 1, docs searches 1 cluster, forum 4, calendar 0. **Found:** 24. **Kept:** 9. **Held:** 4. **Cut:** 11. **Own vs external:** 5 own, 4 external (44%, share met). **Thin-issue call:** full issue; no call needed.

| # | Item (page title) | Primary link | Channel | Date | Rung | Section | Verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| 1 | SDK for Python 4.0.0 release notes | releases page | unlabelled sweep | 2026-02-19 | 1 | Heads-up | keep | drops the deprecated `ack_all()`; merged without a breaking label |
| 2 | Security advisory for the Node runtime HTTP parser | advisory page | advisory feed | 2026-02-27 | 1 | Heads-up | keep | high severity; affects the Node SDK's default transport |
| 3 | Dead-letter queues are generally available | changelog entry | own feed | 2026-02-11 | 2 | Shipped | keep | |
| 4 | Batch publish API | changelog entry | own feed | 2026-02-25 | 2 | Shipped | keep | |
| 5 | Retry backoff in the Go SDK | merged PR #812 | merged-PR query | 2026-03-01 | - | - | hold | merged, release due 2026-03-10; expires 2026-04-04 |
| 6 | "Quarrystack 4.0 is a mess" thread | forum thread | forum | 2026-02-20 | - | - | cut | commentary on item 1; linked the release notes instead |
| 7 | Handling poison messages with dead-letter queues | author's blog | submissions | 2026-02-14 | 3 | From the community | keep | external walkthrough, author's own post |
| 8 | "10x faster than every queue" benchmark | unknown author's post | submissions | 2026-02-28 | - | - | hold | authenticity: no method, account two weeks old |
| 9 | Idempotent consumers guide | docs page | docs searches | 2023-06-02 | 3 | Learn | keep | trigger: 14 zero-result searches for "exactly once" after item 4 shipped |
| 10 | Batch publish tutorial reposted by an aggregator | aggregator entry | submissions | 2026-02-26 | - | - | cut | duplicate of item 4's source |

Remaining rows elided. Hold list: items 5, 8 and two others, each with its expiry. Intake gaps: event calendar returned 0; confirm there is no community calendar before dropping the Events section for good.

## Negative example: the padded sheet

```
// ✗ Bad - five sections filled at any cost
Shipped: Dead-letter queues GA; Batch publish API; "Recap: last month's v3.9 release"
Heads-up: (moved the Python 4.0 change to Shipped because Heads-up "looked alarming")
Learn: three posts from an aggregator's "top queue articles" list, none opened
From the community: forum thread "Quarrystack 4.0 is a mess" (most upvoted)
Events: a conference from last year's calendar, "probably running again"
```

What went wrong, gate by gate:

- The v3.9 recap is last issue's item: duplicate gate.
- Moving the breaking change out of Heads-up hides the one item readers must act on: consequence ladder.
- Unopened aggregator links: primary-source gate, and they stay unverified.
- The most upvoted thread is commentary; popularity never moves an item up a rung.
- The "probably running" conference has no confirmed date: window gate, events rule: no confirmed date on the event's own page.

```
// ✓ Good - same inputs, gated
Heads-up: Python SDK 4.0.0 (breaking), Node runtime advisory
Shipped: Dead-letter queues GA, Batch publish API
Learn: Idempotent consumers guide (evergreen, trigger stated)
From the community: one external walkthrough
Events: dropped, calendar returned nothing
```
