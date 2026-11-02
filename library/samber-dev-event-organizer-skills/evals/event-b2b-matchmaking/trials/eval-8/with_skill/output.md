# Meridian Exchange edition 3: feedback on the report and the dashboard

**Next action:** replace the report sentence with the version in section 4, then take the dashboard to `event-sponsor-fulfillment`. Don't build it here. Your draft has four problems.

## 1. Your counts

✅ 172 held + 11 refilled + 27 empty = 210. The inputs add up.

❌ The 87% (183/210) adds the 11 standby refills to the 172 held meetings. The counting rule says held-against-booked is meetings both sides attended over pairings accepted and slotted. Refills are counted separately "or a refill hides a no-show."

| Measure | Value | Counting rule |
|---|---|---|
| Held against booked | 172 of 210 | Both sides present, over accepted and slotted pairings. Excludes refills. |
| Refilled from standby | 11 | Reported on its own line. |
| Empty-slot count | 27 | Absolute count: one or both sides absent, not refilled. |
| Slots a booked counterpart missed | 38 (27 + 11) | Derived. This is the real size of the no-show problem. |

⚠️ The 12.9% empty-slot rate is 27/210. It leaves out the 11 slots that were missed and then rescued, so it understates the problem. The skill also reports this measure as an absolute count, not a rate. A rate invites comparison with programs whose counting rules you don't know.

⚠️ I'm assuming the 27 is after refill attempts, because that is the only reading where the figures sum to 210. Please confirm.

## 2. The 61% trade-show benchmark: delete it

- Fill rates published by matchmaking vendors and trade-show sources are sales material. They use their own definitions and haven't been independently verified. The skill says never to quote one.
- Your 87% also counts refills, and that rule probably isn't theirs, so the comparison is apples to oranges even if the 61% were sound.
- The only valid comparison is against your own earlier editions, counted by the same rule.

**Question:** do you hold booked-versus-held counts from editions 1 and 2? If you do, restate them under the rules above before comparing. If you don't, this edition's 172 of 210 is your first usable baseline. Say so in the report instead of claiming a win.

## 3. "Per-supplier details available on request": move them into the report

With contracted quotas, booked-against-promised per sponsor is the only number that says whether a commitment was met. An overall figure hides the one supplier who missed, and that supplier is the one who will raise it. Report all five.

Per supplier, the numerator is meetings held that passed the criteria check. The denominator is the committed number. Use the worksheet's "what does not count" list: a booked meeting that wasn't held, a held meeting with a substitute person, a counterpart from the sponsor's own company, a counterpart they already have a relationship with.

**Decision you need to make before filling the table:** do the 11 refilled meetings count toward a supplier's quota?
- They count only if the standby pairing was accepted by both sides and passes that supplier's criteria.
- Check what each contract says about substitutes.
- Apply the rule identically to all five suppliers.

## 4. Rewritten report sentence

> **Meridian Exchange, edition 3.** 210 pairings were accepted by both sides and slotted. 172 meetings were held with both sides present. 11 slots lost a counterpart and were refilled from the standby line, reported separately. 27 slots ended empty or one-sided. Counts are this program's own; no external benchmark applies. Per-supplier delivery against contracted quota is in the table below. [5-row table: committed / held and passing criteria / refills counted per contract / shortfall.]

Also add the two gate measures. Your draft reports neither:
- **Unwanted-meeting complaints:** the target is zero. Any non-zero count is a defect in the matching or scheduling rung.
- **Confirmation completeness:** every published pair was accepted by both sides before publication.

## 5. The per-sponsor dashboard with payment milestones: don't build it in this program

❌ Per-sponsor tracking, a payment gate and renewal reporting are `event-sponsor-fulfillment`'s job. This program's output is one generic outcome record, one row per pairing:

- The two sides.
- Whether both accepted.
- Whether the meeting was held.
- Whether it was refilled from standby.
- Which criteria it was checked against.

The record has no meeting content and no names beyond what each participant agreed to share. Hand it over with the counting rules attached.

⚠️ Tying payment to quota completion changes the commitment, not only the reporting:
- That is a guaranteed count with a make-good. It needs written criteria and a remedy you can fund after the event.
- `event-sponsor-agreement` drafts the clause. This program decides the shape.
- If the five contracts were signed as best-efforts targets or with no meeting promise, gating payment now is a retroactive contract change.
- Check each contract first. Many may not allow it.
- A payment tied to a bare count rewards filling slots with whoever is free. That produces the wrong people in the numbers, and sponsors judge it after the event.

⚠️ Finance only needs per-sponsor counts: held-passing against committed. Don't give finance attendee-level rows. Don't settle a shortfall with attendee data or program access (a talk slot, a judging seat). A quota is access, and sponsorship never buys program influence.

## 6. Next edition

- **Standby refill:** it saved 11 of 38 missed slots, and 27 stayed empty. Each empty slot means the no-show rung was too light. Check whether the queue was too thin per counterpart, or whether the standby person wasn't there when the slot opened.
- **Reconfirm-and-remind:** if you didn't already run it, it is the only rung that reduces no-shows instead of absorbing them.
- **Overbooking:** keep it deleted. It is justified only by a measured held-versus-booked count from a previous edition of this same program. Treat this edition's 172 of 210 as your first such measurement, and make edition 4 prove it.
- **Record per edition:** the matching criterion, pairs booked, meetings held, slots left empty, which side cancelled, and every unwanted-meeting complaint.

## What I need to finish the table

1. Are 27 the empty slots after refill attempts?
2. Do you hold counts from editions 1 and 2, and how did they treat refills?
3. What shape is each of the five supplier commitments (best-efforts, guaranteed with criteria, bare count), and do they include a remedy?
4. Do refilled meetings count toward quota in those contracts?