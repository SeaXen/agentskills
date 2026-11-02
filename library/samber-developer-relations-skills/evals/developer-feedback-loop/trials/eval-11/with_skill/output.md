# Drafts for #88 and #103: three changes from your request

I changed three things from what you asked for. The rules behind each are in the feedback-loop skill's close-the-loop replies and record references.

| You asked | Drafted instead | Why |
|---|---|---|
| "Your retry request is done" | A "shipped, but not the fix requesters asked for" reply | #88 asked for configurable retry count and backoff. You shipped a replay endpoint. Saying "done" reads as a promise that retries are now configurable, and that is the kind of reply that costs trust. |
| Name Ashgrove Fintech | No company named | Ask before naming a company as a requester in public, even a happy one. The record already names the problem without them. |
| Paste the support ticket with the 212 lost events | Not pasted. The thanks goes to Ashgrove privately, in the support ticket. | Never copy private support text, an account name or a figure from a ticket into a public record. |
| Close #103 as done | Close #103 as a duplicate of #88 | #103 is the same problem. Duplicates close toward the canonical record so the count and the notifications stay in one place. |

## 1. Post on #88 (public)

> Shipped in 4.2 – <changelog link>. This came from this thread, and thank you to everyone who added a use case.
>
> You asked for configurable retry count and backoff. We built an event replay endpoint instead, because <reason product approved>. It solves the problem stated here, events lost while a consumer is down or redeploying, this way: you can re-deliver the missed events after the fact. Docs: <replay endpoint doc link>.
>
> If replay doesn't cover your case, say so in this thread and describe what you're trying to do. That is what would put configurable retries back on the table.

Before you post, fill in or confirm these three points:
- **Reason:** use the one product approved. Don't invent it.
- **Retries:** this draft is silent on whether configurable retries are now off the table. If product decided they are not planned, state that plainly in the thread. The "not planned" template covers it: the reason, the workaround, and what would change the decision.
- **Replay claims:** I have only your word that replay handles lost events. Don't add claims like "works for deploys of any length" unless the docs support them.

## 2. Post on #103 (public), then close as duplicate

> This is the same problem as #88 (9 people). Closing this one so the use cases land in one place.
>
> #88 now has the outcome: an event replay endpoint shipped in 4.2 – <changelog link>. It is not configurable retry count and backoff, and #88 explains why. Please add your use case there if replay doesn't cover it.

The status on #103 is `duplicate`, not `shipped`. Anything that implies #103's own request was fulfilled would be wrong.

## 3. Thank Ashgrove, privately

Post this in their support ticket, not on #88. Tell them where they asked, since tracker notifications reach only subscribers.

> Good news: 4.2 ships an event replay endpoint, <doc link>. Your report of events lost during your deploy window is one of the cases that drove it. Thank you for the detail. It made the problem concrete for product. If you're happy for us to say publicly that Ashgrove helped push for this, let us know. Otherwise we keep it between us.

If Ashgrove agrees to be named, add a line crediting them to #88. Ask the engineer first whether they want to post their own account of the lost events. That is their message to share, not ours.

## 4. Requesters who asked outside the tracker

Anyone on #88 or #103 who asked in Discord, Slack or support also gets a short note in that channel, with the #88 link:

> Update on <problem>: shipped in 4.2 as an event replay endpoint – <link to #88 reply>. Details and caveats are in that thread.

## 5. Record housekeeping (private, no reply needed)

- Set #88 to `shipped` (product sets this status). Set #103 to `duplicate`.
- Link the 4.2 changelog entry from #88.
- Keep Ashgrove's account, the ticket and the 212 figure in the private fields only.
- Check that no stale bot auto-closes #88 or #103 before you do.

## What I need from you

1. The product-approved reason for building replay instead of configurable retries.
2. Whether configurable retries are now "not planned", or still under review.
3. The changelog and replay doc links.