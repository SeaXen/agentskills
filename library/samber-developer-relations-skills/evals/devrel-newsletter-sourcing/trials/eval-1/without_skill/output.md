# Ferrolink developer digest: what makes the cut

**Dates:** I assumed this issue covers 2026-05-01 to about 2026-05-28, since your last issue went out 2026-04-30. The system date is 2026-10-30. If it really ships this Thursday, these items are five months old.

## Running order

| # | Section | Item | Source | External? |
|---|---|---|---|---|
| 1 | Heads-up | Node SDK 6.0.0 removes v1 auth header support (2026-05-14) | #2, our changelog | No |
| 2 | Shipped | Payouts API GA | #4, docs page (2026-05-20) | No |
| 3 | Shipped | Python SDK 3.4.0 adds the async client (2026-05-02) | #9, release notes | No |
| 4 | Learn | "Idempotent refunds with Ferrolink in Go" (2026-05-09) | #6, original dev.to post | Yes |
| 5 | From the community | HN thread on v1 auth headers | #1 | Yes |

**External share:** 2 of 5 is 40%, which clears the one-third floor. Items 1–3 are listed in the order readers need them: breaking change first, then the headline launch, then the smaller release. The order within items 2–3 is my choice.

**The HN slot is forced.** Only #1 and #6 are eligible as external content. The Medium post, the aggregator repost and the forum thread all fail (reasons below). Without #1 the issue is 1 of 4 external (25%) and breaks the charter. If you find another external item, you can drop #1.

## Checks before Thursday

1. **Reconcile #1 and #2.** HN says the API killed v1 auth headers. Our changelog says only that Node SDK 6.0.0 removed support.
   - If the API change is real, the Heads-up must say so, with dates and who is affected.
   - If it's only the SDK, say that plainly. Item 5 then reads as our answer to the thread.
   - Don't run item 5 until the two agree.
2. **Check the tutorial against the auth change.** Item 4 was published five days before the 6.0.0 removal. Confirm its examples don't use v1 auth headers. If they do, it needs a caveat or a swap.
3. **Check the 429s thread (#8).** If the webhook 429s are a real platform issue, it belongs in Heads-up (you have two open slots) with a status link. The thread's 38 replies suggest it is.

## Cuts

- **#3, CEO tweet:** It duplicates #4, which is the canonical, durable source. The screenshot adds nothing.
- **#5, "9x faster" Medium post:** The account is three weeks old, there's no method section, and the claim can't be verified. Don't link it, not even to rebut it. Flag it to whoever owns brand or legal if it's being attributed to us.
- **#7, DailyDevLinks repost:** It's a copy of #6. Link the original author, not the aggregator.
- **#8, forum thread:** It's the month's most active thread, but it's on our forum, so it isn't external and can't fill the community slot. See check 3.
- **#10, Go SDK 2.8.1:** It fixes a typo in an error message. The changelog covers it.

## Spare capacity

Adding #10 as a third Shipped item would bring the issue to 6 items with 2 external. That is exactly 33.3%, with no margin, so I'd leave it out.