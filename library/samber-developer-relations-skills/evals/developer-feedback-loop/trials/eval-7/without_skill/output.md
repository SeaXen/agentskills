**Not OK to send as drafted.** Two of the three drafts say something other than what the review decided, and one skips the post it most needs. Revised versions are below.

## What to change

| # | Your draft | Problem |
|---|---|---|
| 1 | "Great idea, on our radar!" | Reads as a maybe, but the decision is no. People will wait, then feel misled. |
| 2 | "Coming in Q2!" | The PM said "probably Q2". Your post turns that into a commitment, and a miss will read as a broken promise. |
| 3 | Close the thread quietly | You promised this publicly in January. A silent close looks like a retreat. A short, direct post costs less than the rumor that follows. |

Posting on the request board only is also too narrow. Most of the original asks came from Discord and support tickets, and those people never read the board.

## Revised drafts

**1. Webhook retry counts (declined)**

> We're not going to add configurable retry counts to webhooks. We'd rather build a replay endpoint, so you can re-deliver failed events yourself instead of tuning retries. It isn't scheduled yet, and we'll share a date once we have one. If you have a concrete case where retries aren't enough, reply here. It will shape the replay design.

**2. SSO for self-hosted (approved, not committed)**

> SSO for self-hosted is approved, and we're aiming for Q2 2027. That's a target, not a commitment. We'll confirm the date once scoping is done.

**3. Bulk log export (dropped)**

> In January we said bulk log export was coming. We've decided not to build it and to put that time into the connector work. We should have told you sooner. If you depend on bulk export, reply with your use case. We'd like to know whether the connectors cover it.

Don't call the connector work a replacement unless it covers the export use case. Check that before you post.

## Where to post

- **Request board:** post all three, since that is where the records live.
- **Discord:** post a short version with a link to the board, in the channels where people asked.
- **Support tickets:** reply to the linked tickets for each request. Ticket requesters won't see Discord or the board.
- **Bulk export:** post it where the January promise was made, and lead the Discord post with it.

## Questions before you send

1. Is Q2 2027 correct? Today is 2026-10-30, so I assumed next year.
2. Where did you make the January promise? That is the place the bulk-export post must go.
3. Is the replay endpoint approved internally, or only an aspiration? If it's only an aspiration, change the wording to "we're exploring".
4. Do the connectors really cover bulk-export needs? If they don't, say so plainly in post 3.
5. Does your team approve naming the "connector work" publicly? If not, replace it with "other priorities".

Once you answer 1–3, I can finalize the exact text for each channel.