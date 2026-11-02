# TapStack Conf: attendee directory and meeting request flow

## Verdict

**Don't build the directory from the registration data.** Your plan is the one pairing the skill deletes outright: only the sponsor chooses, and the attendee's data was collected for a different purpose. Attendees declining a request doesn't fix this. A request that reaches an attendee who never agreed to be listed is already the ambush, and the consent problem happened when the data was reused.

Three sponsors and 800 attendees don't need a directory. They need a small opt-in program, or possibly none.

## Why the plan fails

1. **Ticket purchase is not consent to be contacted.** Consent is fixed by the wording attendees saw when they submitted. Unless your checkout said "we may share your title, company and interests with sponsors who can contact you", you can't retrofit that. Sponsors at community events get aggregate demographics, never names.
2. **A browsable directory is the hardest rung to undo.** A copied directory can't be unpublished. It also gives the widest disclosure and the weakest matching, since only the requester chose.
3. **Declining is not a safeguard.** The attendee gets contacted before they decide anything. Some will treat that as misuse of their ticket data.
4. **Developers come to learn.** An unsolicited vendor meeting reads as an interruption.

⚠️ **One check before anything else:** reread the exact wording on your ticket checkout and privacy notice. If it says nothing about sharing with sponsors, the registration data is off the table for this purpose, even for an internal "sorted" list. Also check what the GDPR notice says about purposes. This is a legal question for your counsel, not something I can settle.

## What to do instead

### Step 1: Decide whether to run the program

I need two answers from you first:
- **Do the sponsor contracts name a number of meetings?** If not, there is no signed obligation, and the default is no program or a very light one.
- **Are attendees and sponsors two separately invited populations?** In your case they are one audience with sponsors standing in it.

On your facts so far, the right default is **no booked-meeting program**. Handle the three sponsor requests as brokering (below). If a contract does name a number, the program becomes a delivery obligation. Use the opt-in version below.

### Step 2: Matching mechanism

With three sponsors, the pair count is small enough for one person to hold in their head. That makes **organizer brokering** the best fit. If you want attendee-initiated discovery as well, add **mutual opt-in**.

**Matching criterion** (agree this with each sponsor before building anything):
> A meeting is a good match when an attendee who [situation they state, e.g. runs payment-rail integrations and is evaluating a change there] meets a sponsor engineer who works on that area, and both accepted the pairing.

**Brokering run sheet:**
1. Each sponsor gives you their criterion in one sentence.
2. Announce an open invitation from the stage, in the attendee app and in the pre-event email: "Sponsor X would like to talk with people working on Y. Raise a hand here if you'd like an intro."
3. A named organizer reads all responses in one sitting, then pairs on paper with a one-line reason per pair.
4. Send both sides the same introduction: counterpart, reason, how to decline without explaining.
5. Nothing is published. Nothing about who was asked is shared.

**Mutual opt-in (optional extension)** if you want volume beyond hand-brokering:
1. Send a **new** opt-in form to attendees. Don't reuse the registration data.
2. Keep the form to the fields the criterion uses (see "What the profile shows").
3. A pair exists only after both sides accept. Cap outbound requests per sponsor, and expire pending requests on a stated date.

### Step 3: Consent wording

Put this in the attendee's line of sight at submit, before any collection. It must state:
1. **What is shared:** the fields a sponsor sees.
2. **Who sees it:** only a sponsor the attendee has accepted, not the whole directory.
3. **What triggers sharing:** the attendee's own acceptance of a specific request.
4. **What they get:** meetings with vendors on topics they chose.
5. **How to stop:** withdraw anytime, and what happens to accepted pairings.
6. **When it ends:** the pool is deleted by a stated date after the event.

Read points 1–3 aloud and ask whether anyone would be surprised on the day. If yes, rewrite.

## What the profile shows

This is the answer to "what should the directory show". Collect the smallest set the criterion consumes, all entered by the attendee. The sponsor sees this only for attendees who have opted in and only once the attendee accepts.

| Field | Why |
|---|---|
| Role or function, in their own words | Carries the "situation" half of the criterion. A job-title dropdown flattens it. |
| What they're looking for, one line, required | The only field that establishes intent. Optional makes the pool a list of people who asked for nothing. |
| Topic tags from a short fixed list | Makes the pool sortable. A long list gets no selections. |
| Availability windows within the block | Needed only if you book slots (Step 4). Collect it after the block is placed, not before. |

**Refuse these:**
- Budget or purchase authority. It turns the profile into a qualification record the organizer holds, i.e. lead scoring performed on attendees.
- Anything inferred or looked up elsewhere, such as seniority or company size.
- Anything pulled from the registration data.

**Hide until accepted:** the attendee's name and company. Before acceptance, a sponsor sees only the role description and the "looking for" line. Nobody sees who was requested by whom.

## The request flow

1. **Attendee opts in** on the new form, with the consent wording above. Not opting in is the default and has no consequence.
2. **Request.** Either you broker an intro, or a sponsor (within a request cap) sends one request to a specific opted-in attendee. The request carries the sponsor's one-line reason, in plain text.
3. **Attendee responds.** Accept, decline, or ignore. Decline needs no explanation. The sponsor sees only "not available", with no distinction between decline and silence.
4. **Pair exists only on acceptance.** Nothing else creates a pair, and nothing is ever placed on an attendee's schedule without it.
5. **Reconfirm.** An explicit acceptance at booking time, plus a reminder before the block.
6. **Pending requests expire** on a stated date.
7. **Decline tracking.** Count declines per attendee. Repeated declines from the same person means your read of their entry was wrong, so stop sending them requests. That threshold is a judgment call, not a measured one.

## Scheduling

- **Default: self-service booking** against published availability, or **no booked slots** if you only want introductions and let people use the hallway track. The latter needs no timetable at all.
- If a contract names a meeting number, use a **hybrid**: contracted slots pre-assigned, each with an acceptance step before it appears on any schedule. Remaining capacity is self-service.
- **Placement:** put the meeting block inside the grid you already have, and never move a session. Take its boundaries as given from whoever owns the schedule.
- **Slot construction:** equal slots, with gaps between them, and no conflicts with sessions someone is speaking at or attending. Choose the slot length from your block and your real accepted-pair count. I'm not stating a number.
- **Publish one view per person.** A full pair grid reveals who is meeting whom.
- **Name one organizer on duty** for the block and put their name on the brief.

## What you may promise sponsors

- **No contract number:** *"The package includes access to the meeting program on the same terms as everyone else. No number of meetings is promised."* This is the safest choice.
- **If they want a number:** a **best-efforts target** with the criteria written down, framed as an intention with no remedy attached.
- **Guaranteed count with criteria** only if the contract already names a number and the opt-in data lets you verify the criteria. It needs a defined make-good you can fund after the event. Hand the shape to whoever drafts the clause.
- **Never** print a bare meeting number with no criteria and no make-good.
- **Never** settle a shortfall with attendee data or program access (speaking slot, judging seat).
- Sponsorship buys access, not influence over the program.

⚠️ I'm not quoting typical acceptance rates, no-show percentages or slot counts. Any figure in circulation is vendor marketing, and the only numbers you may plan against are ones you measure on this program.

## Missed bookings

- **Default:** reconfirm and remind.
- **Standby queue** only if someone is staffed at the meeting area during the block.
- **No overbooking** in a first edition, because you hold no measured booked-versus-held count.
- **No deposits or penalties** on the attendee side.

## The meeting brief

One document, identical for everyone, published before booking opens. It contains:
1. The matching criterion sentence.
2. Who can join on each side and how.
3. What data is collected, what is shared, with whom, on what trigger, and when it is deleted.
4. That both sides must accept every pairing.
5. Where the block sits, where meetings happen, and the slot length.
6. How to decline, cancel or withdraw.
7. What happens to a missed slot.
8. The named organizer on duty and how to reach them.

## What to record afterwards

One row per pairing: the two sides, whether both accepted, whether the meeting was held, whether it was refilled from standby, and which criteria it was checked against. Nothing about what was said. Hand this record to whoever runs sponsor reporting, and don't build per-sponsor tracking here.

Measures (all self-set, comparable only to your own future editions):
- **Held against booked**, the number to plan against next time.
- **Booked against promised**, per sponsor, never averaged.
- **Mutual-acceptance rate**, labelled as a proxy.
- **Empty-slot count**, as an absolute number.
- **Unwanted-meeting complaints:** target zero. Any non-zero count is a defect in your process, not attendee behaviour.
- **Confirmation completeness:** every pair on the schedule was accepted by both sides before publication.

## Questions I still need answered

1. Does any signed or drafted sponsor package name a meeting number?
2. What exact wording did attendees see at checkout about sharing their data?
3. Where does the meeting block sit in the grid, and is it fixed?
4. Will anyone be staffed at the meeting area during the block?
5. By what date must booking open, and when must the schedule stop moving?
6. Is this a one-off, or will you run it again and want to learn from it?
7. How many organizer hours can you spend during booking and on the day, and how comfortable are you telling a paying sponsor their meetings aren't available?

I haven't seen these answers, so everything above is the default for your stated facts. The answers to 1 and 2 could change the recommendation most.