# RiverforkJS 2027: carbon saving check and remote tier design

## 1. Can I confirm the carbon saving? No.

⚠️ A remote ticket removes no emissions by existing. Carbon drops only when someone who would have flown buys remote instead. The board's claim ("fully hybrid fixes our footprint") depends on that substitution rate. No data in this conversation shows what that rate will be.

I can show where the carbon is, and which substitutions matter.

### Estimated baseline, edition 6 (illustrative)

Per-trip figures are round-trip economy from Toronto, taken from typical airline per-passenger factors. They are my assumptions, not your data. Expect ±40%.

| Group | People | Avg round trip | Total | Share of travel CO2e |
|---|---|---|---|---|
| US (40%) | 480 | ~0.6 t | ~288 t | ~38% |
| Europe + Asia (15%) | 180 | ~2.0 t (Europe ~1.4, Asia ~2.6) | ~360 t | ~48% |
| Canada (45%) | 540 | ~0.2 t (many local or ground) | ~108 t | ~14% |
| **Total travel** | 1,200 | | **~756 t** | |

Hotel, food and venue energy add roughly 60–120 t. Streaming is negligible, at about 2 kg per remote viewer for a full conference. Multi-camera production adds a small fixed amount.

### What hybrid saves, by substitution rate

| Scenario (share of in-person attendees who go remote) | Saved | % of travel |
|---|---|---|
| Europe/Asia 25%, US 10% | ~74 t | ~10% |
| Europe/Asia 50%, US 20% | ~148 t | ~20% |
| Europe/Asia 100%, US 0% | ~360 t | ~48% (ceiling for this group) |

Three findings follow:

- **Europe and Asia are 15% of heads but about half the travel carbon.** Your instinct to target them is right.
- **The US group is the second big lever.** A 20% switch there saves about 58 t, as much as 29% of the Europe/Asia group switching. A nudge aimed only at Europe and Asia leaves that on the table.
- **Remote buyers who would never have flown add no saving.** Counting remote sales as "carbon avoided" is the classic greenwash error. Only substitution counts.

### What to do before the board repeats the claim

1. Pull city of origin from the edition 6 registration data and recompute with a standard calculator (ICAO, myclimate). This replaces my assumptions with your baseline.
2. State the claim as "up to X t if Y% of long-haul attendees switch", not "fully hybrid fixes it".
3. Measure substitution at checkout. Ask remote buyers: "Would you have attended in person without a remote option?"
4. Consider cheaper levers alongside hybrid: remote speaking for long-haul speakers, and regional watch-party hubs.

### Two questions that change the numbers

- What is the in-person ticket price?
- How many speakers fly in, and from where?

## 2. Remote tier design

### Platform

Keep it light: a gated stream plus the community tools your audience already uses.

- **Streaming:** a gated player behind ticket login. Options are Mux or Vimeo Enterprise embedded in your site, or an event platform like Airmeet or Swapcard if you want turnkey chat and networking. I haven't verified current vendor pricing, so get quotes.
- **Replays:** publish every talk within 2 hours of its slot. This is the key requirement for Asia (see timezones below).
- **Chat and Q&A:** Discord, with a channel per track and per region, plus Slido-style upvoted Q&A.
- **Accessibility:** live captions, plus transcripts on replays.
- **Production:** a multi-camera feed and a speaker-slide mix from your AV vendor. Streaming production is likely your biggest fixed cost, so ask for a quote early.

### Tiers

| Tier | Price | Includes |
|---|---|---|
| Remote Live | **$49** | All live tracks, chat, live Q&A, 12-month replay access |
| Team Hub pass | ~$199 (test) | One license for a team watching together, up to 10 people. A shared screen cuts per-head friction and cost. |
| Free keynote registration (optional) | $0 | Keynotes only, to build the email list and feed next year's funnel. Test whether it cannibalizes $49 sales. |
| In-person to remote switch | Refund of the price difference | Open until about 60 days before the event. Offer a credit toward next year's in-person ticket. |

Remote buyers get digital swag only, since shipping adds carbon.

### Economics check

Net result = (remote sales × $49) − (substitutions × (in-person price − $49)) − added streaming cost.

Example with hypothetical figures, since I don't have your price or quote: if in-person is $600 and 25% of Europe/Asia switch (45 people), you lose about $25k in ticket revenue. The $49 tier needs about 500 sales to cover a $25k production cost on its own. Run this with your real numbers before committing. Also ask sponsors how they value in-person attendance.

### Timezones: the main design constraint

A 9:00–17:30 Toronto programme falls at 15:00–23:30 in Central Europe, which is workable. It falls at roughly 22:00–06:30 in Tokyo and 18:30–03:00 in India, which is not workable. So:

- Lead the Asia pitch with replays within 2 hours and a recap, not live viewing.
- Add a 07:30 ET speaker AMA slot. That is 13:30 in Central Europe, 17:00 in India and 20:30 in Tokyo, a decent hour in all three.

## 3. Nudging Europe and Asia toward remote

These are hypotheses to test, not benchmarks. I don't have a trusted conversion figure.

1. **Announce remote at the first announcement and the CFP.** Once someone has booked a flight, the sunk cost kills the nudge. This is the biggest lever.
2. **Ask country at registration** and show both options side by side. Don't use IP profiling.
3. **Lead with total cost and time, not guilt.** Show ticket plus flight plus hotel plus 4–5 days away against $49. For most of this group cost and time will move behavior more than carbon will.
4. **Add an accurate carbon line.** For example: "Round trip from London ≈ 1.4 t CO2e. Remote ≈ 2 kg." Keep it factual and keep the in-person option equally visible.
5. **Make remote good.** Offer a regional AMA hour, and volunteer-run watch parties in cities like London, Berlin and Tokyo at meetup venues. These keep the social side that people fly for.
6. **Offer the switch path** (section 2) to anyone already registered.
7. **Credit remote buyers toward next year's in-person ticket.** That keeps the door open without penalizing the switch.
8. **Avoid:**
   - long-haul surcharges
   - hiding the in-person option
   - guilt messaging
   - offset claims you can't back

Apply the same nudge, in softer form, to US attendees, per the table in section 1.

## 4. KPIs

- tCO2e per attendee, against the edition 6 baseline recomputed from registration data
- Substitution rate, from the checkout survey question
- Remote tier break-even, per the formula above
- Remote completion rate, meaning replays watched

## 5. Next steps

1. Send me the in-person ticket price and speaker travel counts.
2. Pull origin-city data from edition 6 registrations.
3. Get two or three streaming production quotes.
4. Take the revised claim ("up to X t if Y% switch") back to the board.