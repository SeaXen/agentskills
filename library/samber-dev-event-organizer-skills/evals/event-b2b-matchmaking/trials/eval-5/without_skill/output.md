# Foundry Days booking flow: gaps in the plan

**Verdict:** the plan doesn't guarantee the contracted numbers, because attendees can cancel. It also carries a consent risk and an unfairness risk. Fix those first.

## 1. Top gaps, in priority order

1. **"Guarantees contracted numbers" is false as written.**
   - Cancellations break it, and so do no-shows.
   - **Action:** check what the contract counts: meetings placed, confirmed, or held.
   - If the contract says "held", you need confirmation, a backfill flow, and check-in tracking.
   - If it says "placed", the plan is fine on this point, but sponsors may not read it that way.

2. **Consent and privacy (GDPR if any EU attendee).**
   - "Opted into the meeting program" may not cover profile-based matching by staff, or sharing the attendee's name, profile, and agenda slot with a sponsor.
   - **Action:** make the opt-in text cover both uses explicitly. Add a way to withdraw, and when someone withdraws, remove their placed meetings and stop sharing their data.
   - Check with your DPO or counsel before launch.

3. **Opt-out default feels like spam.**
   - Putting meetings on a personal agenda that the attendee never asked for will annoy some people.
   - Cancelling also costs them a click and possible social friction.
   - **Alternative:** send a proposal (a pending slot) that auto-confirms after 48h unless declined. You still count it, and the attendee has really been asked.
   - The attendee sees *why* they were matched, e.g. "you work on X, sponsor sells Y".

4. **Fairness across sponsors.**
   - 3 sponsors get guaranteed pre-placement and 9 fight over leftovers.
   - The 9 will see this when slots vanish before self-booking opens.
   - **Action:** decide how much capacity pre-placement may consume, say a cap of 50% of each attendee's meeting slots.
   - Tell the 9 up front, or expect complaints.

5. **Attendee overload and collisions.**
   - One attendee might be a great match for all 3 quota sponsors.
   - **Action:** cap pre-placed meetings per attendee, e.g. 2 total, and at most 1 per sponsor.
   - Place them with buffers around sessions, meals, and room transit.
   - Spread matches so the same 50 attendees aren't picked every time.

6. **Pool size.** Sum the quotas and compare to the opted-in pool. If only 100 of 400 opted in and the quotas total 90+ meetings, you will saturate them or place poor matches. Compute this before you promise anything.

## 2. Cancellation and backfill

- **Cutoff:** set a deadline after which cancelling costs the attendee something, or locks the slot. Otherwise the quota erodes quietly.
- **Backfill:** when someone cancels a quota meeting, the system should offer a replacement. Staff pick a second-best match, or the system auto-proposes one from the waitlist.
- **Reason:** capture a one-click cancel reason ("not relevant", "time conflict"). It tells you which matches fail and gives you sponsor-facing evidence.
- **Sponsor-side cancel or no-show:** define the policy, and notify the attendee.
- **Replaced meetings:** count them once, not twice.

## 3. Self-booking (the FCFS part)

- **Concurrency:** use an atomic reserve (a unique constraint on slot or on attendee+time), not check-then-insert. Otherwise two people get the same slot, or one attendee double-books.
- **Opening rush:** 400 people at one opening time means a spike and a bot or scripted-booking risk. Stagger opening by cohort, or use a short lottery window.
- **Per-attendee caps** keep the FCFS pool from being hoarded by a few.
- **Conflict checks:** against sessions, other meetings, and pre-placed ones.
- **Waitlist** per slot with auto-promotion on cancel.
- **Calendar export** (ICS) and reminders at 24h and 1h.

## 4. Measurement and audit

Track a status per meeting: `proposed → confirmed → cancelled → attended / no-show`. Also record who created it (staff, attendee, sponsor), and when.

- **Attendance proof:** QR scan or sponsor check-in on arrival. Without it you can't prove "held".
- **Sponsor report:** meetings placed, confirmed, held, and cancelled with reasons. Define the contractual unit before the event.
- **Audit log** of staff placements. If a sponsor disputes the numbers, you have the trail.

## 5. Operational and staff load

- Manual match-picking for 3 sponsors across 400 profiles takes real hours. Budget it, or use a scoring shortlist plus human review.
- **Sponsor input:** ask each sponsor for their ICP (role, industry, company size) up front. Otherwise you pick matches the sponsor rejects.
- **Late registrants and walk-ins:** do they get a pre-placement pass, or go straight to FCFS?
- **Day-of changes:** room swaps, sponsor staff illness, schedule slippage. Name an owner and a channel to push updates.
- **Accessibility:** step-free routes between meeting points, and time for longer transits.
- **Test with a dry run:** run the placement algorithm on last year's data or synthetic data and check the distribution before it touches real attendees.

## 6. Suggested revised flow

1. Opt-in captures explicit consent for matching and for data sharing with sponsors.
2. Sponsors supply their ICP.
3. Staff or a scoring tool generate proposals, with caps (2 per attendee, 1 per sponsor).
4. Attendee gets a proposal with the match reason. Auto-confirm at 48h unless declined.
5. Declines trigger a backfill proposal before the cutoff.
6. Self-booking opens for the remaining capacity in staggered cohorts, with atomic reservation.
7. Check-in at the meeting feeds a per-sponsor report with the contractual unit.

## 7. Questions I'd settle with you

1. Does each contract count meetings placed, confirmed, or held?
2. How many of the 400 are likely to opt in, and what do the three quotas sum to?
3. Do attendees see in the opt-in wording that profile data goes to sponsors?
4. What do the other 9 sponsors have in their contracts about access?
5. Is there a remedy clause if a quota is missed (refund, credit, extra slots)?