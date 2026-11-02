# DevSecCon Valencia: running order verdict

Your co-organizer is right on both. I have no data from your event, so the numbers below come from a model with stated assumptions. Swap in your own figures.

## 1. Deep dive at 13:15 ❌

**Why it's wrong**
- **Circadian trough.** Alertness dips in early afternoon, roughly 13:00 to 15:00. This is mostly body clock, not lunch. Studies often report vigilance 10 to 20% worse. I'm treating that as an assumption, not a precise figure.
- **Worst slot for the hardest content.** Kernel eBPF internals needs the most concentration, and 13:15 to 14:45 sits across the whole trough.
- **Late returns.** People finish lunch and hallway chats, so about 10 minutes of the 90 are lost to arrivals.
- **Length.** 90 minutes without a break is far beyond the 25 to 45 minute slots people expect. Attention lapses are well documented after 10 to 20 minutes.

**Illustrative arithmetic (assumptions, not data)**

| | 13:15, 90 min straight | 10:45 day 1, 2×40 min + 10 min break |
|---|---|---|
| Alertness | 0.8 | 1.0 |
| Usable minutes | 80 (after late arrivals) | 80 (break absorbs arrivals) |
| Attentive minutes | 80 × 0.8 = **64** | 80 × 1.0 × 0.95 = **76** |

That's about 19% more effective attention from moving it. Late morning on day 1 is the best slot: people are fresh, coffee has landed, and day 1 has the fullest room.

**If it must stay post-lunch:** split it into two blocks and make the second a hands-on lab. Active formats resist the dip.

## 2. Biggest name closes at 16:30 on day 2 ❌

**Why it's wrong:** a Saturday-afternoon close competes with travel.
- Venue to Valencia airport plus check-in means leaving about 2 hours before departure.
- A 16:30 talk ending at about 17:15 loses anyone with a flight before roughly 19:30.

**Room size at 16:30 (assumptions)**
- f = share of attendees from out of town: **60%**
- g = share of those with departures before about 19:30: **50%**
- Local fatigue loss: **10%**

Retention at 16:30 = 1 − (0.6 × 0.5) − 0.10 = **60%**

At 14:15 on the same day, with only fatigue loss, retention is about **90%**. Moving the big name earlier gives about **+50% audience** (90 vs 60).

**Break-even:** keeping 16:30 only wins if "stay for the headliner" recovers more than 30 points of retention. It rarely does for travelers with fixed flights. The closing-slot logic works for local, non-travel crowds, or when something like a raffle or party follows.

## 3. Proposed order

**Day 1**
1. 09:30: opening keynote.
2. 10:15: coffee.
3. **10:45 to 12:15: eBPF deep dive**, in two blocks with a 10-minute break.
4. 12:15: lunch.
5. Afternoon: lighter and shorter talks.

**Day 2 (Saturday)**
1. Morning: strong talks from 10:00.
2. 13:00: lunch.
3. **14:15 to 15:00: headline speaker.**
4. 15:00 to 15:30: closing remarks, raffle and announcements.
5. 15:30: end. Anyone with a flight after 18:00 can still make it.

To keep people through the end, announce the headliner on day 1 and put the raffle after the talk.

## 4. Get real numbers in 15 minutes ⏳

1. **Origin.** Get the share of attendees from outside Valencia from registration data. That's your f.
2. **Departures.** Send a one-question poll: "When does your departure leave on Saturday?" That's your g.
3. **Retention.** If you ran a previous edition, compare badge scans or check-ins for day 1 morning vs day 2 afternoon.

Plug the results into: retention(16:30) = 1 − f·g − fatigue. If it comes out above about 85%, keep the headliner at 16:30. I expect it won't.