# PortForward Conf: booth power and bandwidth allocation

⚠️ **I can't give you a per-booth number from those two ratios.** The `event-booth-experience` skill says no formula converts an aggregate venue ratio into a per-booth allocation. Both ratios describe a room full of attendee laptops and phones, not exhibitor load (screens, demo rigs, streaming). Any per-booth figure derived from them would be invented.

## What the ratios actually say

| Venue ratio | Arithmetic | What it means |
|---|---|---|
| 1 outlet per 10 attendees | 600 ÷ 10 = **60 outlets** in the room | Attendee-side capacity. It does not say how many outlets are at the booths or how much they can carry. |
| 2.5 devices per attendee | 600 × 2.5 = **1,500 devices** | WiFi sized for attendee devices. It gives no throughput per booth. |

- Dividing 60 outlets by 14 booths would give about 4.3 each. That treats attendee outlets as booth supply, so don't publish it.
- The same goes for dividing WiFi capacity across 14 booths. The venue contact gave you device counts, not bandwidth.

## Power allocation (process, not a number)

1. **Ask the venue contact, in writing:**
   - What is a booth drop (circuit, amperage)?
   - Is it separate from the 60 attendee outlets?
   - What does it cost, who may run it, and does it need electrical sign-off?
   - By what date must it be requested?
2. **Count booths that need a drop, not booths.** A table with a laptop and a banner needs a socket. A table with a screen and a demo rig needs a drop. Poll the 14 sponsors on their equipment before you promise anything.
3. **Honor the Gold promise first.** Gold packages promised a power drop, so reserve one per Gold sponsor before any other allocation. Confirm the venue can supply that many separate from the attendee outlets. If it can't, this is a make-good problem to settle now, not on the morning.
4. **Publish a per-tier line in the floor brief** with the request deadline as a schedule row. The skill's illustrative shape is "R − 2 weeks: power and A/V requests close, nothing accepted after this". The two-week figure is illustrative, so use the venue's real lead time.

| Tier | Power | Who supplies and pays | Deadline |
|---|---|---|---|
| Gold | One drop, as promised | Ask the venue (self-set until answered) | Venue lead time |
| Other tiers | Self-set. Suggested default: none, bring a charged device. A drop only on request, if the venue can supply it. | Ask the venue | Same deadline |

## Bandwidth allocation

- **Treat WiFi as a stated inclusion, not a throughput guarantee.** "Included at no extra cost" is a billing statement. Publish exactly that to sponsors.
- **Don't split the WiFi into per-booth slices.** There's no basis for it. Ask the venue these three questions instead:
  - What is the uplink (the internet connection feeding the WiFi)?
  - Is per-device or per-SSID rate limiting applied?
  - Is wired available at booths at all? Record the answer in the Network row of the tier catalog.

## The cloud-gaming demo

⚠️ **Don't approve this on venue WiFi.**
- WiFi sized for 1,500 attendee devices carries no promise for a sustained, latency-sensitive stream.
- The load will also compete with every attendee's traffic during the busiest hours.

Tell this sponsor, in writing, before the request deadline:
1. WiFi is included but not guaranteed. **Bring a fallback**, such as a recorded or locally hosted demo, or their own connection (cellular or a dedicated uplink).
2. If they want wired, ask the venue whether it exists. Don't promise it.
3. Their own uplink (such as cellular) must not interfere with event WiFi. Check with the venue before they bring it.

## Floor-brief checklist

- [ ] Venue answers on booth drop, cost and deadline, the electrical sign-off requirement, WiFi uplink and rate limits, and wired availability.
- [ ] Sponsor equipment poll: which booths need a drop (the count) and which need only a socket.
- [ ] Gold drops reserved and confirmed.
- [ ] Per-tier Power and Network rows filled, with the request deadline in the schedule.
- [ ] WiFi wording to sponsors: "included, no throughput guarantee, bring a fallback for live demos".
- [ ] Hand the finished brief to `event-sponsor-fulfillment` to execute per sponsor. Don't build a per-sponsor tracking matrix here.

## Open questions

I'd normally ask these one at a time. Your answers decide the allocation:
1. How many of the 14 booths are Gold, and what are the other tiers?
2. Does the venue treat a booth drop as separate from the 60 attendee outlets?
3. What is the last date the venue accepts power and A/V requests?
4. Is there a wired option at booths?

Everything I labelled "self-set" is a default I chose, not a venue fact.