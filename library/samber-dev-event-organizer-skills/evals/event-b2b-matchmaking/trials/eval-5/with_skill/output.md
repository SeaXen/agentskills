# Foundry Days: booking flow review

**Verdict:** Your hybrid shape is right: quota slots pre-assigned, the rest self-service. One piece must change. Pre-placing meetings on an attendee's agenda and letting them cancel is the one mechanic the skill deletes outright.

## 1. Biggest gap: pre-placed means unaccepted

- ❌ Your plan: team places the meeting, attendee cancels if unwanted. This is opt-out. A meeting on someone's schedule without their acceptance is the "ambushed meeting" failure.
- ❌ It also fails your own goal. A meeting nobody accepted is a no-show already on the schedule, so the count is guaranteed on paper only.
- ✅ Fix: pre-assigned pairs are **proposals**, not bookings.
  1. The team picks matches.
  2. The attendee sees "Sponsor X proposed this meeting" with accept and decline.
  3. A pair reaches any agenda only after the attendee accepts it.
  4. The sponsor side accepts too.
- Gate: every pair on the published schedule was accepted by both sides before publication. Target is zero unconfirmed.
- Expire pending proposals on a stated date, so dead proposals don't hold slots.

## 2. Consent: "opted into the meeting program" is not enough

- ⚠️ Check the exact wording attendees saw. Did it say sponsors may be matched to them, and what is shared with whom? Consent scope is fixed at submission, and retrofitting it is the one error that can't be undone.
- If the wording was vague, don't use it for pairing. Re-collect with explicit wording before any matching.
- The form needs six points:
  1. What is shared.
  2. Who sees it.
  3. What triggers sharing: acceptance, not "organizer judgment".
  4. What they get out of it.
  5. How to withdraw.
  6. When the data is deleted.
- Sponsors get the counterpart's name only after mutual acceptance. No attendee lists.

## 3. "We pick good matches from profiles"

- Write the matching criterion as a sentence first, with the sponsor. Example shape: "An attendee who [self-stated situation] meets a sponsor engineer who [capability], and both accepted."
- Score only on fields attendees typed themselves. Refuse budget or purchase authority, and anything inferred (seniority, company size looked up).
- Use scoring or hand-picking to order candidates, never to create a pair.
- At 400 attendees and 3 quota sponsors, organizer brokering for the quota sponsors is workable. Log a one-line reason per proposal.
- Free-text "what I'm looking for" must be required, or the pool has no intent signal.

## 4. The guarantee is the real risk

"Guarantees the contracted numbers" holds only if attendees accept. Acceptance is the one thing you can't force, and forcing it is what the plan was doing.

- **Quota size vs pool:** propose more candidates per quota than the quota number. Check that opted-in attendees matching each sponsor's criteria actually exist in sufficient numbers. The skill states no ratio: you set it, and you measure it this edition.
- **Criteria:** each of the three sponsors needs a written criteria sheet. It covers who counts, how it is evidenced from a self-entered field, what does not count, and who rules on borderline cases and by when.
- **Counting:** a meeting counts when it is **held** and passes the criteria. Booked doesn't count. Report per sponsor, never averaged.
- **Make-good:** pick it now, before the contracts are final if you still can. Choose one you can fund after the event: fee credit, pro-rata refund, or post-event intros (only to attendees who consented to post-event contact). Never make good with attendee data or program access (talk slot, judging).
- **Contract posture:** if the numbers are already signed, then "guaranteed count with criteria" is the shape, and you need the make-good. If still drafted, consider a best-efforts target. Hand the clause to `event-sponsor-agreement`.
- **Wording to give the three sponsors:** "guaranteed meetings with consenting attendees matching criteria", not "guaranteed meetings".

## 5. Missed meetings (they will happen)

- Cancelling is easy, so it becomes your main no-show source.
- Default: explicit acceptance plus a reminder before the block.
- Add a standby queue if someone is staffed at the meeting area during the block. It is worthless unattended.
- **No overbooking.** You have no measured held-vs-booked count for this program. Don't borrow event-level no-show rates or vendor figures.
- **No penalties or deposits** on attendees for missed meetings.
- Refilled-from-standby meetings are counted separately, so a refill doesn't hide a no-show.

## 6. First-come-first-served remainder

- Fine, since autonomy is preserved. Add these guards:
  - Cap outbound requests per person, or the heaviest requester floods inboxes.
  - Every booking needs the counterpart's acceptance.
  - Expect a few of the 12 sponsors to absorb most requests. Tell the others up front.
- Make sure quota-sponsor capacity (their available slots) can hold both their quota meetings and any self-service load. Otherwise self-service eats the slots your quota needs.

## 7. Schedule and logistics

- The meeting block is a guest inside the published grid. Take its placement as given. Never move a session. If it isn't fixed yet, route that to `event-schedule-design`.
- Equal slots with gaps between them. Check each attendee's meetings against sessions they're speaking at.
- Publish one view per person, not the full pair grid.
- Name one organizer on duty during the block, and put the name on the brief.
- Set two dates: when booking opens, and when the schedule stops moving.

## 8. Handoff and measurement

- Publish one meeting brief, identical for everyone. It covers: criterion, who is eligible, data and sharing, acceptance rule, block location, how to decline, missed-slot rule, organizer on duty.
- Outcome record: one row per pair (both-accepted, held, refilled, criteria checked). Per-sponsor reporting goes to `event-sponsor-fulfillment`.
- Track, all self-set:
  - held vs booked
  - booked vs promised, per sponsor
  - mutual-acceptance rate (a proxy only)
  - empty-slot count
- Gates:
  - unwanted-meeting complaints: zero
  - confirmation completeness: all
- Save these numbers. They are the only ones you may plan against next edition.

## Questions I need answered

1. Are the three quota numbers already signed? What criteria and what make-good, if any?
2. What exact consent wording did attendees see at opt-in?
3. Is the meeting block's place in the grid fixed? Will someone be staffed there?
4. When must booking open, and when must the schedule freeze?

Once I have those, I can write the criteria sheet, consent wording and meeting brief.