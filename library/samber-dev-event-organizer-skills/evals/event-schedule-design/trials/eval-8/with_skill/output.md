# DevSecCon Valencia: schedule verdict on the two contested slots

**Both slots are wrong, and your co-organizer's instinct is right.** I can't give you a defensible attendance number for either. The skill's sources give direction only, and their magnitudes come from lab and economics-conference data, so I won't invent one. I do give you a check you can run on your own data below.

I skipped the full interview to deliver this in one pass. Everything marked *assumed* needs your confirmation before the grid goes public.

## 1. Deep dive at 13:15 is the dip, not the cure

- **Sourced, direction only:** the post-lunch alertness dip is circadian. It happens "even when the individual has had no lunch" (Monk, *Clinics in Sports Medicine* 24(2), 2005). That is the physiological reason to avoid dense content right after lunch.
- **The same sources cover your slot exactly.** 13:15 to 14:45 is a 90-minute lecture with no internal break, sitting across the whole dip. Putting your strongest and densest content there is the opposite of what you want.
- **13:15 may also be a fill-the-room problem.** If lunch ends at 13:15 (PyCon US runs about 12:30-1:15), the first 10 to 15 minutes go to people finishing food and walking. This is judgment.
- **Possible Valencia factor (my knowledge, not the skill's):** local lunch often runs late. Check Q3, the catering window. If lunch is only 12:00-13:15, locals may be at their sleepiest, and the dip may land differently for them.
- **Format substitution, from DevOpsDays:** swap the format, don't fight the energy state. Put a hands-on lab, a panel, or lightning talks after lunch.
- **Wrong slot length too.** The skill says to standardize slots (FOSDEM about 50 minutes, PyCon US 45). A 90-minute slot is a bespoke duration.
  - Either declare it a deliberate double slot, or split it into 2×45 with a break and give it two parts.
  - Publish a 100-minute slot for a 90-minute talk. That 10 minutes is *self-set*, with no benchmark behind it.

**Move:** put the eBPF deep dive in the morning of day 1, after the opening keynote and the first break. I assumed 10:30-12:00 (see section 3). The NBER paper finds second-day mornings best at economics conferences, so day-2 morning is also defensible. Choose by speaker availability and by whether you want the strongest content on the day with the most attendees.

## 2. Headliner closing at 16:30 on a Saturday is the graveyard slot

- **Sourced:** the last slot of the last day has the worst outcomes at the conferences studied (Gorodnichenko, Pham and Talavera, NBER WP 26240). Henderson and Henderson give "graveyard slot" its academic definition. Cite the direction, not the magnitude. Those are economics conferences, not developer events.
- **Saturday raises the risk.** DevOpsDays' organizing guide recommends weekdays only, because a weekend day competes with protected family and rest time. Day 2 is a weekend day, so the whole day is at risk.
- **Travel (my judgment):** attendees who fly or take a train home Saturday will leave before 16:30. That is a bet against your own headliner.
- **You are betting on the slot's pull.** A big name does help, but you are asking it to beat the most structurally weak position on the grid.

**Move:** put the biggest-name speaker in a plenary at the start of a day. Day 2 morning (assumed 09:15) is the strongest option: a re-sync point, when more people are present. Close the event with a short plenary of 20 to 30 minutes, with lightning talks, thanks, and announcements.

- To keep people to the end, tie something attendees want to the closing plenary, such as a prize draw requiring presence. This is my suggestion, not a sourced practice.
- **If the speaker can only land or present late Saturday**, that is a fixed point, not a free choice. Tell me their window (Q7) and we redesign around it.

## 3. Settling it with numbers

The only numbers I can give are arithmetic on your own grid. The skill says any threshold here is one you set, not a benchmark.

- **Your own data is the real test.** If you have last edition's scan-ins or session counts by hour, compute `r = attendees in the final slot ÷ peak attendance`.
  - Headliner reach at 16:30 ≈ `r × peak`. Headliner reach in the morning ≈ the day's attendance at that hour.
  - Whatever `r` comes out below 1.0 is the share of your headline audience you give away by closing with them.
  - No last-edition data? Use day-1 scan-ins this edition as a proxy. Day 2 is Saturday, so expect it to be lower than day 1 (judgment).
- **Slot-level diagnostic:** record no-show rate per slot position, edition over edition. That turns "which slot is a graveyard here" from received wisdom into your own measurement.
- **Pick two or three metrics and write the revision each triggers before the event.** Start with room-fit outcomes (overflow versus near-empty) and no-show rate per slot.

## 4. Proposed skeleton (assumed times, to be confirmed)

Everything here is *assumed*: track count, rooms, capacities, lunch window, and doors. The skill says to place fixed points and breaks first, then rooms.

**Day 1 (assumed Friday)**

| Time | Item |
|---|---|
| 09:00-09:15 | Opening plenary |
| 09:15-10:00 | Keynote |
| 10:00-10:30 | Break (plenary re-sync) |
| 10:30-12:10 | eBPF deep dive, 100-minute slot (90 min of content) |
| 12:10-13:15 | Lunch, adjusted to the catering window (Q3) |
| 13:15 onward | Hands-on lab, panel, or lightning talks, not lecture |

**Day 2 (Saturday)**

| Time | Item |
|---|---|
| 09:00-09:15 | Welcome |
| 09:15-10:15 | Headliner keynote, in the room that holds every track |
| … | Remaining sessions |
| ~15:30 (end by) | Short closing plenary, 20-30 minutes |

I did not touch the other sessions. Fill them after the fixed points are confirmed.

## 5. Open questions (the interview, shortened)

1. How many rooms run in parallel, and how many sessions are you placing across the two days? Single-track needs no clash checks; multi-track needs all four types.
2. Room names, seated capacities, and walking minutes between them. The deep dive is a strong draw, so does it fit in a single room?
3. What did the venue contract fix: doors, catering windows, room hire end time on Saturday?
4. When does the schedule go public? Per the skill, publish early and iterate. Lock-late is deleted for events people travel to.
5. Which sessions are fixed points, and when is the headliner available? Is the 16:30 slot a speaker constraint or a choice?
6. What changes physically in the deep-dive room before and after it (AV, labs, furniture)? That sizes the turnover buffer.

## 6. Pacing read (judgment, not measurement)

- The skeleton front-loads intensity before lunch and uses format change after it.
- The sourced direction is: structured talks in the morning, looser formats later (DevOpsDays), and no dense content right after lunch.
- Neither the heijunka analogy (manufacturing) nor the sourced studies give a number for this.

## 7. Disruption priority order (hand to event-run-of-show)

1. Protect the keynote and plenary slots.
2. Protect the headline commitments the audience came for: the eBPF deep dive and the headliner.
3. Minimize how many other sessions the fix disturbs.
4. Lock the revised grid for the rest of the block. Don't keep re-shuffling.

## 8. Publication posture

Release early and iterate. Add a visible "what changed" marker once tickets are sold and people are building personal agendas. I don't know your publication date (Q4). Today is 2026-10-14, so tell me your target and I'll date the posture.

**Next step:** answer Q1 to Q3, plus the headliner's availability window. Then I'll fill the full grid and run the clash checks.