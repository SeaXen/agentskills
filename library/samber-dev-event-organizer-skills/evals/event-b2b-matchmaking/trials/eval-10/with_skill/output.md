**Verdict: do not ship auto-scheduling Friday.** Ship scored recommendations plus a two-sided accept step. That cuts the back and forth without placing anyone in a meeting they did not accept.

## Red flags, ranked

### 🔴 1. Auto-placing top-3 matches puts unaccepted meetings on schedules
- The skill deletes this rung outright. No rank, no demotion.
- A meeting nobody accepted is a no-show already on the grid.
- The failure shows up as attendee complaints about unwanted meetings. The target for that metric is zero.
- 500 attendees × 3 is 1500 placed pairings across 40 vendor teams, about 37 per team on average. The average hides worse skew: a score fitted to sparse tags tends to recommend the same few vendors to everyone.
- Check: do 40 teams have capacity for their share? Do the vendors also accept? Nothing in your plan asks them.
- Fix: the score orders a candidate list and never creates a pair. A pair exists only after both sides accept.

### 🔴 2. Consent wording is unchecked, and it cannot be fixed after launch
- Consent scope is fixed by the words people saw when they submitted the form. Your intent does not change it.
- "Opted in" to what? Matching, being shown to vendors, or being auto-booked into a slot?
- If the form did not say "a counterpart sees your profile on mutual acceptance", auto-booking exceeds it.
- Open the live form wording and check the six items: what is shared, who sees it, what triggers sharing, what they get, how to withdraw, when the data is deleted.

### 🔴 3. Firmographic enrichment breaks the "self-entered fields only" rule
- The skill refuses anything the person did not type themselves, such as company size looked up elsewhere.
- Matching on appended data turns a service for attendees into lead qualification done on them.
- People did not consent to it, and it will not show up in the form they saw.
- If any attendees are in the EU or UK, data obtained from a third-party database also carries notice obligations, and the purpose is new. Get legal or your DPO to confirm. I cannot judge that from here.
- Fix: drop the enrichment features from the Friday score. Retrain or reweight on self-entered fields only: role in their words, evaluation-area tags, availability.

### 🟠 4. A 14-feature gradient-boosted model cannot explain itself to a participant
- The skill requires a scoring rule short enough to explain to someone who asks "why was I recommended this vendor?"
- Write the matching criterion as one sentence first. If the model cannot be summarized as that sentence, it is the wrong tool.
- What labels trained it? You have no measured data from this program, so it may be fitted to something unrelated to "both sides would take this meeting again."
- Pre-launch check: read a sample of its own top recommendations before anyone sees them. If it recommends the same ten vendors to everyone, it is fitted to a sparse tag matrix.
- Keep a manual override and log a reason for every override. The log shows what the model misses.

### 🟠 5. The meeting grid has open questions
- Where does the meeting block sit in the published grid? It is a guest in a grid built for sessions, and it loses every conflict.
- Check each person's slots against sessions they speak at or attend. Move the slot, never the session.
- Leave gaps between slots. Publish one view per person, never the whole pair grid, which discloses who meets whom.
- State no slot length or count until you size it from real accepted pairs.

### 🟠 6. No handling for missed meetings
- Default: explicit acceptance at booking plus one reminder before the block.
- Add standby refill only if someone is staffed at the meeting area during the block.
- Do not overbook. You hold no measured booked-versus-held count for this program, and borrowing event-level or vendor-published rates is the mistake to avoid.
- Never penalize the attendee for a missed meeting: no deposit, no forfeited benefit.

### 🟠 7. Vendor contracts may already name a meeting number
- If any signed package says "N meetings", that is a delivery obligation, not a design choice. Then use the hybrid mechanic: contracted quota pairs pre-assigned, each with an acceptance step, and the rest self-service.
- The package needs written criteria for who counts and a make-good you can fund after the event is over.
- Do not make good with attendee data or with program access.
- Track booked against promised per vendor, never averaged.

## What to ship Friday

1. Freeze auto-placement. The score only orders candidate lists.
2. Remove the appended firmographic features. Score on self-entered fields only.
3. Each attendee sees their top candidates. Each vendor sees theirs.
4. A pair exists only after both sides accept. Cap outbound requests per person so no one floods an inbox. Expire pending requests on a stated date.
5. Place accepted pairs into slots. Publish nothing until both sides have confirmed. Target for unconfirmed pairs on the schedule: zero.

This keeps most of the two weeks saved. The back and forth shrinks to one tap each way.

## Answer these before Friday (one at a time works)

1. Paste the exact wording on the opt-in form. I will check it against the six items.
2. Does any vendor package name a meeting number, and what is its remedy for a shortfall?
3. Where does the block sit in the grid, and is anyone staffed at the meeting area during it?
4. Where did the data team's company database come from, and did attendees see notice of it?
5. What labels trained the model?

## After the event: measure these yourself
- Held against booked
- Booked against promised, per vendor
- Mutual-acceptance rate (a relevance proxy, label it as one)
- Empty-slot count
- Unwanted-meeting complaints (target zero)
- Confirmation completeness (gate, must be all)

Next action: open the live opt-in form and paste its consent text here. About 2 minutes.