# Customer summit: sign-offs and order

**Next action today:** send the 6 federal and bank guests' hospitality question to your compliance owner. Nothing else on this list can wait as long as that one can't.

Dates assume the summit is about Dec 2 and registration opens about Nov 4. Please correct me if those are off.

## Short answer to legal

No, you have no terms. The summit needs three things before the registration form goes live:
- published terms of attendance
- a code of conduct that binds your own staff as well as guests, with an enforcement path for when the person reported is an employee
- event insurance

Those are one review, covered in step 4 below. Two other reviews sit alongside it, and they are the ones that can hurt you.

## Why this order

Each sign-off is ordered by what can't be undone:
- **Accepted hospitality:** an invitation accepted under a rule it breaks is unrecoverable, and the cost lands on the guest as well as on you. A withdrawn invitation is recoverable.
- **Collected registration data:** a list collected under the wrong notice can't be un-collected, and the fix usually means not using it. A wrong notice can be corrected going forward.
- **Published terms:** these can be revised for the next edition. An incident at this edition can't be revised at all.

## Sign-offs in order

| # | Sign-off | Who signs | Done by | Blocks |
|---|---|---|---|---|
| 1 | Hospitality clearance for VIP guests | Your compliance/legal owner, plus each guest's own employer | Start today. Written clearance before any flight is booked. | Invitations, flights, hotels |
| 2 | Goal, funding owner and measurement commitment | Budget owner, plus RevOps/sales if they co-fund | ~Oct 21 | Step 3, and what the Salesforce feed is allowed to do |
| 3 | Attendee data into Salesforce | Whoever holds the company's privacy obligations (DPO or privacy counsel) | ~Oct 28 | Registration form and its notice |
| 4 | Terms of attendance, code of conduct, insurance | Legal, plus your insurer or broker | ~Oct 28 to Nov 1 | Registration going live |
| 5 | Go-live check | You | ~Nov 3 | Registration opening |

### 1. Hospitality for the 35 VIP guests (now)

- **Two policies apply, not one.** There is your company's anti-bribery and gifting policy. There is also each guest's employer's policy, which is often stricter and is not yours to waive.
- **The 4 federal guests and 2 bank guests are the high-risk cases.** For public-sector and regulated-industry guests, an ordinary flight-plus-two-nights package may not be permitted at all.
- **Ask your counsel to answer these:**
  - Does our policy permit flights and two hotel nights for customers?
  - Does it need pre-approval, a value cap or a register entry?
  - Should we pay vendors directly or reimburse?
- **Ask the six guests to check with their own ethics or compliance office.** Their written answer is your evidence.
- **Do not book anything until clearance is in hand.** Federal and bank clearances can take weeks, so start them now.
- **Prepare a fallback for anyone who can't accept.** Options are attending without hosted travel, paying their own way, or joining remotely. An invitation withdrawn early costs a conversation. One accepted and then breached costs the relationship.
- **Check the other 29 guests too.** Many employers have rules even where yours doesn't.
- **Keep the VIP logistics data (passport details, dietary needs) out of Salesforce.** Hold it in a separate, minimal travel list. Your privacy owner should confirm this in step 3.

### 2. Goal, funding owner and measurement (~Oct 21)

RevOps asking for the feed is a goal and a funding question as well as a data question. The skill requires a named line owner and a goal with a measurement commitment before registration opens. Without them, the feed has no purpose to be reviewed against.

I don't yet know four things, and the answers change the recommendation. I'd settle them with you in this order:
1. **Does the engineer who attends also sign, or does someone else?** Your VIPs are engineering leaders, so I suspect the buyer is separate. If so, any pipeline number is *influence*, not attribution. Say that in the brief.
2. **Who owns the budget line today?** If nobody does, that is the first finding.
3. **Is this a one-off, or the first of an annual program?**
4. **Does a working join between the attendee list and Salesforce exist today, or would it have to be built?**

**My default recommendation: adoption-first.**
- The 35 VIPs are existing customers, so adoption and retention is the goal your invite list can actually support.
- Pipeline-first needs three things at once: a hard reporting date, a room that is mostly people who have never bought, and a join that already exists. Your VIP room fails the second.
- Promote to a blend of adoption and pipeline only if:
  - the summit is a compounding annual program
  - both joins can be built
  - someone will hold the measurement job through the quarter after the event
- Co-funding with sales only makes sense once the join exists. Sales won't keep funding a number it can't see.
- Delete "attendance count" as a goal. Delete "ecosystem goodwill only" if any co-funder is named.

**Four fields per goal, written before registration opens.** Placeholders in brackets are yours to fill:
- **Adoption:**
  - Metric: share of attending accounts that activate at least one capability they hadn't used, compared with a matched set of non-attending accounts.
  - Owner: [named person in the product org].
  - Source: [product telemetry that identifies accounts].
  - Read date: [a date before the planning cycle that renews the line].
- **Pipeline (only if chosen):**
  - Metric: opportunities created in an agreed window, on accounts with at least one attendee, under an attribution rule agreed now.
  - Owner: [named person in RevOps].
  - Source: Salesforce.
  - Read date: [a date].

A goal missing any of the four is an intention. These thresholds are self-set, because no industry figure transfers between companies.

### 3. Attendee data into Salesforce (~Oct 28)

This is a personal-data decision, not a reporting one. Your privacy owner reviews it before the form is built, because the notice must be right at the moment of collection. Four things need a decision:
- **Lawful basis** for passing registrations to sales.
- **The notice** shown at registration. It must say the data goes to sales, if it does.
- **The retention rule.**
- **Limits on internal reuse.** This is where the AE question lives.

Your counsel decides the actual rules and jurisdictions. I name none here. Questions to bring them:
- **Does the feed need to be live, or is a post-event import enough?** "Piped straight in" is the riskiest design. A post-event import with a clean notice is much easier to defend.
- **May AEs work the list during the event?** I'd suggest excluding the hosted VIPs from outreach. They are guests of the company, and the federal and bank guests may be restricted in what they can accept. Limit AE use to approved account conversations.
- **Should sales get all registrants, or only those with a stated opt-in?**

Even if the feed ships later, the notice must anticipate it. If the notice is wrong at collection, the usual fix is not using the data.

### 4. Terms, conduct and insurance (~Oct 28 to Nov 1)

This answers legal's question. Hand legal this scope:
- Terms of attendance, covering photography, liability, refusal of entry and cancellation.
- A code of conduct that binds employees and states who enforces it when the reported person is staff. The policy itself belongs in `event-code-of-conduct`, and the risk register in `event-risk-management`.
- Insurance for the event itself. Lead times vary, so ask your broker this week.

Keep the privacy notice from step 3 separate from the terms. Terms can be revised next year. An incident this year can't.

### 5. Go-live check (~Nov 3)

Do not open registration until all of these are true:
- Step 1 clearances are in hand, and no unresolved guest is on the booking list.
- Step 2's four fields are written and the funders have seen the same numbers.
- Step 3's notice is live on the form and the feed design is approved.
- Step 4's terms and conduct policy are published and insurance is bound.

## Candidate goal mixes (if funders disagree)

1. **Adoption-first**, with sales as a reader but not a co-funder. Lowest effort, and it fits your invite list. Slower to read.
2. **Adoption-first now, blend next year.** Build the Salesforce join this year, but make pipeline a watched number rather than the goal. This is my recommendation if RevOps insists.
3. **Pipeline-first.** Only if the three promotion conditions above hold. I don't expect them to.

## Re-run this brief if

- the goal changes
- a funder joins or leaves
- the buyer-and-user answer changes
- the invite list stops matching the goal

## What I did not check

I read only the `corporate-event-strategy` skill and its two reference files. I did not review your actual policies, contracts or any counsel advice. Nothing here is legal advice. All rules, thresholds and jurisdictions come from your own counsel.

## Questions for you

1. When exactly is the summit, and when does registration open? I assumed Dec 2 and Nov 4.
2. Do the engineering leaders also sign, or does someone else?
3. Who owns the budget line today?
4. Does an attendee-to-Salesforce join exist today, or would it be built from scratch?