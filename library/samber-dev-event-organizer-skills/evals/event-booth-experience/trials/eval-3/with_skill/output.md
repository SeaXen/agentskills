# NorthStack Summit: load-in and load-out schedule

I read `event-booth-experience/SKILL.md` and its three references. Two parts of your plan can't go ahead, so I replaced them. This is the schedule that results.

## What changed from your plan

| Your plan | Verdict | Why | Replacement |
|---|---|---|---|
| Overnight build the evening before, sold as a premium perk | ❌ Deleted | The venue gave no access before 06:00 and no overnight storage. The skill says this removes the rung entirely. If you sold it, you would be promising a large sponsor something you can't deliver. | A dedicated early Platinum slot from 06:00 (tiered windows) |
| Sponsors start packing during the 17:30 closing keynote | ❌ Deleted | Teardown never starts before the last session ends. Packing tape during the keynote hurts the session, and it breaks the full-event floor presence the sponsors paid for. | Teardown opens at 17:30, with staggered dock slots and a 20:30 hard stop |

The 21:00 clear-out still works without early packing. Teardown opens at 17:30 and the hard stop is 20:30, which gives about 3 hours. The schedule below is built to fit that.

## Anchors

- **R1** is registration opening on day one. Move-in is written as offsets from it.
- **R2** is the floor opening on day two.
- **Fixed by the venue:** 06:00 access and 21:00 clear.
- **Fixed by you:** 17:30 closing keynote end on day two.
- **Condition:** the zone slots below only fit if R1 is 08:00 or later. If R1 is earlier, tell me and I'll redraw them.

## Pre-event

Every row has a published deadline. Items marked *(self-set)* are my proposed values, not venue facts.

| When | What |
|---|---|
| R1 − 3 weeks | Shipping window opens. Venue address, routing and receiving fees published. *(self-set)* |
| R1 − 3 weeks | Platinum submits its stand plan: footprint, height, assembly hours, crew size, and whether anything is rigged or attached to the building. *(self-set)* |
| R1 − 2 weeks | Power and A/V requests close, with nothing accepted after. The venue's real lead time overrides this. *(self-set)* |
| R1 − 2 weeks | Venue answers on rigging and on dock and labour rules, in writing. |
| R1 − 1 week | Return-freight pickup booked for day two, 18:00–20:30. Crate and pallet labels issued. *(self-set)* |

## Day one: load-in

| When | What |
|---|---|
| 06:00 | **Venue access opens.** This is the earliest anything can happen. |
| 06:00 → R1 − 1h | **Platinum dedicated build slot.** The dock and floor are reserved for the Platinum stand alone. This is the premium perk. |
| R1 − 1h | **Platinum hard stop.** The stand must be finished and walked by the organizer, checking height, aisle clearance and nothing overhanging. |
| R1 − 2h to R1 − 30 min | **Zone slots for the other 15 booths.** Zone A opens at R1 − 2h, B at R1 − 100 min, C at R1 − 80 min, D at R1 − 60 min. All must finish by R1 − 30 min. The split into 4 zones is *(self-set)*. |
| R1 − 30 to R1 − 15 min | **Floor walk.** Aisles clear, nothing overhanging, every booth staffed, every promised drop live. |
| R1 | Registration opens. |
| Floor hours | Every booth staffed whenever the floor is open. |

## Overnight between day one and day two

The venue has "no overnight storage". It hasn't said whether assembled stands may stay on the floor overnight.

- **Assumed:** stands and tables stay standing and unstaffed overnight. Otherwise Platinum would rebuild every day and the whole plan breaks.
- **Rows if that holds:**
  - At close, sponsors remove laptops, demo hardware and anything valuable.
  - The venue's security arrangements are published to sponsors.
  - Sponsors know the stand is at their own risk.
- **Day-two restock:** 06:00 access again, with no heavy work.

## Day two: load-out

| When | What |
|---|---|
| R2 − 30 to R2 − 15 min | Floor walk. |
| R2 → 17:30 | Floor open, every booth staffed. |
| 17:30 | **Closing keynote ends. Teardown opens, not before.** |
| 17:30 | **Platinum and Zone A start.** The Platinum stand takes longest to take down, so it gets the dock first. |
| 17:50 | Zone B starts. |
| 18:10 | Zone C starts. |
| 18:30 | Zone D starts. |
| 18:00 → 20:30 | Booked return-freight pickup. |
| 20:30 | **Hard stop.** Sponsors have cleared their space, and the organizer sweeps the floor. |
| 20:30 → 21:00 | Buffer and final walk. |
| 21:00 | **Room clear.** This is the venue's deadline. |

**Anything left at 20:30:** the venue has no storage, so nothing can be held. Organizers remove it or dispose of it per the sponsor agreement. Send this clause to `event-sponsor-agreement` so sponsors agree to it before they book.

## The Platinum perk, reworded

- **Sell:** "Dedicated early build slot from 06:00, reserved dock, and first priority on teardown." Don't use the word "overnight".
- **Price it:** route the pricing to `event-sponsor-pricing`.
- **Optional extras (self-set):**
  - Receiving of pre-shipped crates.
  - Staging of those crates at the stand.
  - Venue-labour assistance, if the venue offers it.

## Platinum build-time check

The Platinum build window is 06:00 to R1 − 1h. With R1 at 09:00, that's 2 hours. If the stand needs more than that, the options are:

1. Ship it pre-assembled in modules.
2. Move R1 later. Registration and floor opening can be separate times.
3. Downscale the stand.

This is not a pure scheduling fix, so ask Platinum for the real assembly hours first.

## Open questions

These change the schedule. Answer in this order:

1. May assembled stands stay on the floor between day one and day two?
2. What time does registration open on day one, and what are the floor hours on day two?
3. How many hours does the Platinum stand need to build and to take down, with how many people?
4. Does the Platinum stand hang from the ceiling or attach to the building? Does the venue require its own or a union crew for dock or rigging work?
5. What's the venue's shipping window and receiving fee?
6. When must power drops be requested, and what do they cost?

When these are answered, `event-sponsor-fulfillment` takes the floor brief and runs it per sponsor.