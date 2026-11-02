# TinkerNight marketing plan: spine, calendar, targets and zero-cash fallback

**Short answer**
- **Use neither extreme.** Track sales percentages like a conference, with no free-meetup over-booking multiple.
- **The fallback is not a small ad buy.** With zero cash, paid ads are deleted from the plan, so a bad checkpoint is answered with diagnosis and free channels.

**Assumptions** (you didn't tell me these, so check them)
- The event is community-run, since there is no cash.
- Positioning and the demand read haven't been done. The plan below is only as good as those two inputs, so route to `event-positioning` and `event-market-fit` if they don't exist.
- Doors date, comps count, existing list, prior edition and partner roster are unknown. Each is a placeholder below.

## 1. Spine: percent of expected sales (Spine A), capped at the room

A 12 EUR ticket with a hard cap is the in-between case. The rule is to pick the spine by the failure you fear, run it as the only target line, and read the other spine only as a sanity check.

**Why not the free-meetup curve (Spine B)**
- Its 200%-of-goal rule exists to absorb a 30-50% drop-off. That figure is MLH's, for free hackathons.
- Your fee exists to shrink that drop-off, and your no-show rate is unmeasured. Never carry MLH's multiple onto a paid ticket.
- The room holds 150. A 200% curve means roughly 150 people turned away at the door of an evening they paid for.

**Why Spine A**
- With zero spend, the risk you can't buy your way out of is under-selling.
- The cap sets the denominator at 150 minus comps.

**Over-booking rule**
- Edition one: sell to the cap, with no oversell.
- Run a waitlist. Release no-show seats by a stated cutoff, such as noon on the day.
- Allow a small oversell only after you've measured your own no-show rate. Set that rate from your own data, not from MLH's.

**Comps**
- Net target = 150 − comps (speakers, organizers, volunteers, sponsor or partner passes).
- Example: 15 comps means you sell 135. Replace 15 with your real number.

## 2. Calendar and targets

Doors date is unknown, so the checkpoints are anchored to marketing moments. Pin real dates once you give me doors.

DevOpsDays' T-7-months start isn't available to you (registration opens in six weeks), so the runway is compressed. That favors fast-acting rungs: a partner's next send, an in-person pitch, a list you already own. Building a list from zero is slow.

**Pre-launch (now, 2026-10-14, to registration open, about 2026-11-25)**
- Build the comms hub: one page, one QR code.
- Open an interest list with a documented opt-in, so the later mailing has consent.
- Create one tracked link per channel. This must be decided before launch because it can't be added later.
- Line up partner posts for launch week.

| Moment | Target (example: 135 net sold) |
| --- | --- |
| Registration opens | A real first-week spike. No spike is the earliest sign that no audience exists |
| Early-bird close | Only if `event-ticket-pricing` sets one. With a flat 12 EUR there is none; if there is one, ~15% (about 20) |
| Program or speaker announcement | About 10% more |
| One month before doors | 40-50% (about 54-68). 25-30% means an execution gap, not a demand verdict |
| Final two weeks | A surge. No surge after healthy earlier checkpoints points at the page or the price |
| Doors | About 135 sold, plus comps equals 150 |

**Reading the targets**
- The DevOpsDays percentages are published for conferences and are an order-of-magnitude guide at 150 seats, not a formula.
- Per-channel targets are yours to set, so the plan sets none yet.
- Launch week measures reach, not demand. Judge from week two. A quiet middle is the normal shape.
- Use the MLH figure only as a side check. If you're far under 100% of the cap two weeks out, don't switch spines.
- If you have a prior edition, its own curve beats this ladder.

## 3. Channels (barter-only, which is the whole menu)

Names are placeholders until you tell me where electronics people actually gather.

1. **Own mailing list plus comms hub**
   - This is the default top rung, but only if you already own a list.
   - If you don't, the rung is empty. Promote local engagement instead.
2. **Partner channels**
   - Targets: hackerspaces, makerspaces, university electronics clubs, parts-shop newsletters, and sibling meetups for reciprocal swaps. Name the real ones.
   - Give each community its own tracked code. It shows which community converts and reads as an invitation made for them.
3. **Local engagement**
   - Showing up at meetups, clubs and makerspace nights is high effort, but it's the rung that reaches people no owned channel does.
   - Promote it if you have no list, or if the audience is one metro.
4. **Own social presence**
   - This is the baseline underneath the others, with low weight.
5. **Pre-event press**
   - This is optional and light, such as a local outlet or a university paper.
6. **Paid ads: deleted**
   - No budget line and no discretionary float means they don't exist.

**Budget posture**
- Barter-only. The SaaS-derived percentage table doesn't apply.
- The event has no float and an unknown cost base, so I'm not assuming ticket revenue can fund anything. Ticket money arrives after the promotion it would pay for.

## 4. Fallback if numbers look bad halfway

Decide this before launch. A miss alone calls for diagnosis, not spending.

1. **Weak reach** (low page traffic, low opens, no partner referrals)
   - This is an execution shortfall.
   - Re-weight to the free fast rungs:
     - Ask a partner for an extra send.
     - Do in-person pitches at the next club or makerspace night.
     - Re-contact last edition's "not available then" segment, if you have one.
2. **Healthy reach, low conversion**
   - The problem is the page or the price, not the channels.
   - Route to `event-landing-page` or `event-ticket-pricing`. Don't buy reach.
3. **Healthy reach and conversion, still short**
   - This is a real demand shortfall.
   - Route to `event-market-fit`.
   - Pre-agree a floor, such as running at 100 of 150 seats. A 150-seat room doesn't have to sell out for the evening to work.
4. **If you later decide to spend anyway**
   - That's a budget decision made outside this plan.
   - It would start as a capped test with one named segment and a tracked link, never as the first reaction to a miss.

## 5. Routing

- **Partner swaps and media deals:** `cross-event-promotion` and `event-media-partnerships`.
- **Send moments:** `event-attendee-email-sequences`, at launch, program announcement, month-out and final-fortnight reminders.
- **Link hub roster:** `event-comms-channels`.
- **Social content:** `event-social-media`.
- **Registration page:** `event-landing-page`.
- **Price:** `event-ticket-pricing`.

## What I need from you

To turn the placeholders into dates and numbers, tell me:
1. The doors date.
2. The number of comps.
3. Whether you own a list, and its size.
4. Whether there was a prior edition, and its no-show rate.
5. The real communities, clubs and shops your audience uses.