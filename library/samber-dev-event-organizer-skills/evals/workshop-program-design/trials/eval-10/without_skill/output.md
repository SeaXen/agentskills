# Penhale Conf workshop day: where to start

Start with the facts, and leave the pricing question for last. Four problems arrived at once, but they aren't the same kind of problem. Three are operational failures with fixable causes. The fourth is a strategy question, and a bad day will bias the team's answer to it.

## Step 1: Collect evidence this week (about 2 hours)

Do this before anyone argues about causes. Memory fades fast.

1. Build one shared timeline with these entries:
   - the network drop, at roughly 25 minutes into session 1
   - both camera drops, with times
   - both corridor jams, with times
   - who noticed each problem, when, and what they did
2. Send attendees a 5-question survey while the day is still fresh:
   - Did the network problem stop you from following the workshop?
   - Which session were you in?
   - Was the corridor a problem?
   - Would you pay separately for a workshop day again?
   - What did you pay, and was it worth it?
3. Ask the venue or AV provider for network logs and an incident account.
4. Pull the camera and encoder logs. Check whether the camera fed through the same network or through its own link.
5. List refund requests and complaints received so far.

## Step 2: Find the root cause of each failure

I don't know your setup, so these are questions to answer, not conclusions.

| Problem | Questions to settle | Likely fix direction |
|---|---|---|
| Network died and never recovered | Was it venue Wi-Fi or our own gear? Did the venue size it for the actual device count? Did the workshops need internet, and was there an offline fallback? Was there a named network owner on site? | Contractual: a dedicated, tested, wired-backed network with a capacity commitment and an on-site technician. Content: an offline-capable workshop plan. |
| Video unusable (two camera drops) | Was it the same cause as the network failure, or independent? Was there local recording at the camera, or only a stream? | Record locally to disk, separate from any network. Add a backup audio recorder. Assign an operator who monitors it. |
| Two sessions ending 15 minutes apart jammed the corridor twice | Was the corridor the only route? How many people were in each session? | Schedule fix: align session ends, or stagger them by more than the clearing time. Add a marshal and signage. Consider a break buffer. |
| Team wants to stop charging separately | See Step 3. | See Step 3. |

Notes on the table:
- The network and camera failures may share a cause. Check this first, because it would turn two problems into one.
- The corridor problem is the cheapest to fix. Do it first for an easy win.
- Having no local recording is the real gap behind the video loss. A dropped stream becomes a lost video only when nothing was recording locally.

## Step 3: Treat the pricing question as a separate decision

Don't decide it in the post-mortem meeting. The incidents above were execution failures, and they say nothing about whether the day is priced right. The risk is that a bad day becomes the argument for a structural change.

Gather this first:
- the revenue and cost of the workshop day
- how many attendees bought it, and how many of those were repeat buyers
- the survey answers on willingness to pay
- the refund and complaint count
- what the alternative would look like (bundled into the main ticket, or free)

Then ask which concern is driving the team's view:
- **Refund or reputation pressure.** Attendees paid separately and got a degraded experience. A partial refund or a credit toward next year may settle this without any pricing change.
- **Low value for the price.** Check the survey and the sales data.
- **Friction or complexity of selling it separately.** This is a real argument, but it predates this event.

If the data doesn't support a change, keep the pricing and fix operations. Revisit it after the next event, with a cleaner run to judge by.

## Step 4: Run the meeting

Order the agenda like this:
1. Timeline and facts (15 minutes)
2. Root causes, one failure at a time (30 minutes)
3. Fixes with one named owner and a date each
4. Attendee remediation: who gets a refund or credit, and what you tell everyone
5. Pricing: set the evidence to gather and a decision date, not a decision

## Do first, in this order

1. Decide whether attendees get a message or a refund, since that clock is already running.
2. Start the survey and the log requests (Step 1).
3. Tell the team the pricing decision is deferred until the evidence is in.

## Questions for you

- Did the workshops require internet, or was it only the streaming and recording that broke?
- Did the network belong to the venue, or did you bring your own?
- Have attendees complained or asked for refunds yet?

These answers would change the priority order above, especially the first.