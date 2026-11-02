# Drafts for #88 and #103

I changed three things from your request. I did not draft them as written, because publishing them could cause harm.

| Your ask | What I drafted instead | Why |
|---|---|---|
| "Shipped! Your retry request is done" on #88 | The post says replay shipped and that retry count and backoff configuration did not | #88 asks for configurable retry count and backoff. Replay is a different feature: it fixes recovery after failure, not retry behavior. Nine people will read "done" and find no retry setting. |
| Name Ashgrove Fintech | Not named | A named customer on a public thread is their disclosure to make. Ask them first. |
| Paste the support ticket with the 212 lost events | Not pasted | Support tickets are private. The ticket exposes Ashgrove's incident and event volume, and it may carry their engineer's name and internal details. A partial-credit option is below. |
| Close #103 as done | Comment, and leave it open | #103 has the same gap as #88. Close it as a duplicate of #88 only if you are happy to track both there. |

⚠️ Check one thing before posting. If 4.2 also shipped configurable retry or backoff, say so and I'll redo these as the full "shipped" version. I only know about replay.

## Draft 1: comment on #88 (public)

> Update: **event replay shipped in 4.2.**
>
> You can now re-deliver events that failed or were missed, from the endpoint or the API. This came directly from the discussion here. Many of you described losing events after retries ran out, and replay is how you recover them.
>
> **What this does not change:** retry count and backoff are still not configurable. That is the core of this request, and it stays open here.
>
> What replay gives you today:
> - Re-send any event within the retention window, individually or in bulk
> - Recover from a long endpoint outage without waiting on retry schedules
>
> Docs: `<link to replay docs>`
> Release notes: `<link to 4.2 notes>`
>
> If replay covers your case, tell us. If you still need configurable retries, say what values you'd set and why. That will shape the design.
>
> Thanks to everyone who weighed in.

## Draft 2: comment on #103 (public)

> Replay shipped in 4.2 (details in #88). It helps with recovering events that failed delivery.
>
> It does not make retry count and backoff configurable. I'm keeping this open for now so you get notified when that moves. If you'd rather follow one thread, I can close this as a duplicate of #88. Say so below.

If you prefer to merge now, swap the last two sentences for: "Closing as a duplicate of #88, where this is tracked. Subscribe there for updates."

## Draft 3: private note to Ashgrove (support ticket or account manager)

> Replay shipped in 4.2, and the lost-events scenario you described in your ticket was one of the cases that pushed us to build it. Thank you for the detailed report. It made the case clearly.
>
> Retry count and backoff configuration are still on the roadmap, not shipped.
>
> We'd like to mention on the public #88 thread that a customer's report helped drive this. We can keep you unnamed, name Ashgrove, or share nothing. Which do you prefer? We would not include any ticket content or event counts without your approval.

If they agree to be named, add this to Draft 1 after the first paragraph:

> Thanks in particular to Ashgrove Fintech for a detailed report of the impact.

If they also approve a number, use their own wording. Do not paste the ticket.

## Anonymized proof you can use now

If you still want to show that you listened, without Ashgrove's approval:

> One customer reported losing hundreds of events during an endpoint outage once retries were exhausted. That report moved replay up our list.

Only keep "hundreds" if it cannot identify them. The exact figure of 212 is more traceable, so leave it out.

## Decisions for you

1. Did 4.2 include any retry or backoff configuration? If yes, I'll rewrite Draft 1 as the full "shipped" post.
2. For #103, do you want to leave it open, or close it as a duplicate of #88?
3. Do you want me to send Draft 3 to Ashgrove first, and hold the public post until they reply?