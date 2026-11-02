# KernelKamp edition 5: patterns from the four debriefs

I worked only from your summary, not the docs themselves. Anything marked "check" is something I can't confirm from what you gave me.

## Next action (today, ~15 min)

Name one owner for check-in and one for AV/room readiness. Both failed more than once and each seems to have had no single owner. Everything below builds on that.

## Patterns

### 🔴 1. Check-in has failed in 3 of 4 editions, and it's getting worse

| Edition | Symptom | Stated cause |
|---|---|---|
| 2 | Badge printer jammed for 1 hour | Hardware |
| 3 | Queue hit 45 min | 2 laptops couldn't reach ticketing on venue wifi |
| 4 | Queue out into the street | Not recorded ("chaos again") |

- **The causes differ each time, but the failure is the same.** Check-in has a single point of failure on the critical path (printer, then wifi, then probably throughput), and no fallback exists for any of them.
- **Fixing the last failure each year has never worked.** Edition 4's note doesn't even name a cause, so nobody diagnosed it.
- **Rough capacity math (my estimate, check against your arrival data):**
  - Assume 60% of 350 attendees arrive in a 30-minute window. That's about 210 people, or 7 per minute.
  - A station that prints badges on demand handles roughly 3 per minute.
  - So you need 3 or more stations, plus a spare. If edition 4 ran 1 or 2 stations, the street queue is explained.

### 🟠 2. Projector in Room B has failed twice, and that's a process failure

- Dying in edition 3 and again in edition 4 means the edition 3 lesson never reached edition 4's prep.
- Same pattern as check-in: debriefs record problems, but nothing forces them into the next plan.
- **Check:** is it the same venue and the same room? If yes, it's a known-bad asset. If no, it's a general "AV not tested or not backed up" problem.

### 🟢 3. Catering is probably not a pattern yet

- Three complaints, but they are three unrelated problems:
  - cold lunches (delivery or holding)
  - vegan option ran out (no dietary data)
  - coffee station placement (venue flow)
- Editions 2 and 3 aren't reported to have catering issues.
- Don't over-read three people out of 350. **Check:** the attendee survey. If catering scores low overall, upgrade this. If not, apply the cheap fixes below and move on.
- The shared root is that nobody owns catering and registration doesn't capture dietary needs.

### 🟠 4. The meta-pattern: your debriefs don't close the loop

- Two repeated incidents across editions is the evidence.
- A debrief doc is a record, not a mechanism. Nothing converts a note into an owner, a deadline, and a pre-event check.

## What to change

### Check-in (highest priority)

1. **Pre-print and sort badges** alphabetically by surname before the event. This takes the printer off the critical path. Walk-ups and corrections get one on-demand printer.
2. **Offline-first attendee list.** Export the attendee list (CSV or offline-capable scanner app) onto every check-in laptop before doors open. Venue wifi must not be required.
3. **Bring your own connectivity.** Use a wired line or a cellular hotspot for the ticketing system. Test it on site the day before.
4. **Add stations.** Run 3+ stations split by surname range, with one spare. Put the lines indoors, with a greeter outside to direct people.
5. **Send a pre-event email with a QR code**, so scanning replaces name lookup.
6. **Offer early check-in** the evening before or an hour before the first session, to flatten the peak.
7. **Set and measure a target:** median wait under 5 minutes. Have someone log queue length every 15 minutes at the peak, so edition 6 has data.
8. **Hold a dry run** with all of the above 1 to 2 days before the event.

### AV

1. Ask the venue to repair or replace the Room B projector, in writing, before you commit to the room. If the room is a known-bad asset and they won't, drop the room or bring your own.
2. Bring a spare projector or display and cables. Test every room's AV the day before, with a laptop, using HDMI and USB-C.
3. Assign an AV owner on call during the event, with a spare plan for each room.

### Catering (cheap fixes)

1. Add a **dietary requirements field** to registration. Order by actual counts plus a 10 to 15% buffer per dietary category, with vegan held as a separate item.
2. Specify a delivery time in the order, just before serving. Ask the caterer how they hold food hot.
3. Put the coffee station away from room doors and the check-in flow, and ask the venue for a map before you decide.

### The process fix

1. Turn each debrief into an **issues log**: problem, root cause, owner, fix, due date, "verified at dry run".
2. Make edition 5's pre-event checklist generate directly from that log. The first agenda item of every planning meeting is the previous edition's open items.
3. Record the **root cause** in every debrief. "Chaos again" is an unusable note.

## Six-week plan

- **Week 1:** name owners, send the venue its AV and wifi questions, and add the dietary field to the registration form.
- **Weeks 2-3:** decide the check-in design (stations, offline list, connectivity). Get the venue's written answer on the projector.
- **Weeks 4-5:** order catering with counts, order spare AV, and pre-print badges once registration closes.
- **Week 6:** run the on-site dry run, and finalize the pre-event email with QR codes.

## Questions that would sharpen this

1. What was edition 4's real check-in cause? Count stations, staff, and the peak arrival window.
2. Same venue for editions 3, 4, and 5?
3. What did edition 1's debrief say about check-in?