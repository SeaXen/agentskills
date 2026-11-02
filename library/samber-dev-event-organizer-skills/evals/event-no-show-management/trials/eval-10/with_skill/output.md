# No, the plan doesn't hold up

Planning 60 meals and holding 60 seats rests on an assumption nobody has measured. Plan on about half of the 60 showing up.

## Why the assumption fails

- **Speakers aren't a comparison group.** Paid speakers have a role, a slot on the program, and money at stake. Scholarship students have none of those.
- **Review and selection aren't a price.** Writing a 300-word letter costs effort, but no source I have measures it as raising attendance. Every show-up figure available is split by what the seat cost the holder, not by how hard it was to get.
- **A funded seat is a free seat.** The student pays nothing for the ticket or the travel. Comped and scholarship seats behave as free seats until you measure otherwise.
- **The one data point agrees.** BlackPythonDevs sponsored 47 student tickets for PyCon Uganda 2024 and 22 attended, a 47% show rate. That is one event with no comparison group, so it settles nothing. But it sits inside the ordinary free-ticket band.
- **The bands.** Free events see 40-60% no-shows (Event Tech Live). Paid events see 3-10%. The MLH aggregate across 323 free hackathons puts show-up at about 50%.

## What to plan instead

Figures marked "sourced" come from the references. The rest are my own construction.

| Item | Number | Basis |
|---|---|---|
| Expected scholarship show-ups | **~30 of 60** | 50% free-band rate (sourced) |
| Range to hold in mind | 24-36 | 40-60% show-up band (sourced) |
| Catering line for scholars | **~30, not 60** | Expected show-ups, not registrations |
| Gap | ~30 covers | The overbooking buffer, named separately |

The scholars are not a separate catering line. They fold into the event-wide expected-show-up number. Catering gets that number, never the registration count.

## The room: don't reserve a 60-seat block

A held block of 60 fills about 30 chairs. The other 30 sit unclaimed while people go on the waitlist.

1. **Give scholars a guaranteed seat, not a reserved block.** Count them inside the general registration ceiling.
2. **Set the registration ceiling with arithmetic, and write it down.**
   - Capacity is 350, which assumes this is the binding fire-code or venue number.
   - The sourced hackathon ceiling is double: 350 ÷ 0.5 = **700 registrations, and not one more**.
   - That ceiling is an upper bound for a format the guide wasn't written for.
   - At the optimistic end of the band (60% show), 700 registrations means about 420 arrivals, which is over your room.
   - The safe ceiling against that end is 350 ÷ 0.6 ≈ **583**.
   - My default without a prior edition is to set the ceiling in the 583-700 range. I would take the lower end unless the venue approves overflow space **in writing, before registration opens**.
   - Name the person who closes the form.
3. **Run a waitlist.** Use FIFO, drained on a date you publish when the list opens. Publish the claim deadline for promoted people too.
4. **Run a walk-in lane.** Late arrivals use a separate form and are processed after pre-registered check-in closes. They still complete the full form. Tell the check-in desk the expected volume, which is the gap the ratio predicts.

The occupancy limit is a gate, not something to trade against catering or a full room.

## Two things to avoid

- **A deposit for scholars.** It has no established practice behind it. It would also land hardest on exactly the students a need-gated scholarship exists for. If you still want one, run it as an experiment with a measurement stated in advance.
- **Leaving registration open with no ceiling.** It guarantees registered people get turned away at the door.

## Travel money is a separate exposure

The sponsor's travel funding is not catering. Booked flights and rooms are committed spend that a no-show wastes. Check the sponsor's terms for rebooking or refunds. This skill doesn't cover travel, so treat that as a question for the sponsor and your budget plan.

## Do now

1. **Count scholars separately.** Record registered, attended, and why for no-shows. That gives you your own rate next edition instead of a borrowed one.
2. **Send the scholars through the reminder sequence** (`event-attendee-email-sequences`). Reminders are the lever that reduces no-shows; I don't write them here.
3. **Hand catering the expected-show-up number**, not 60 or 700 (`event-budget`).
4. **Record the numbers.** Write down capacity, the 50% rate and its source, the ceiling and its arithmetic, the published waitlist rule, and the final registered-versus-attended count.

## What I need from you

1. Is 350 the hard cap, and is any overflow space available and approved?
2. Are the 60 scholars inside the 350 or on top of it?
3. When does the catering guarantee lock?
4. Do you have a prior edition's registered-versus-attended count?
5. Is this a one-off or recurring?

The answers could move the ceiling. They don't change the main point: plan on about 30 scholars showing up, not 60.