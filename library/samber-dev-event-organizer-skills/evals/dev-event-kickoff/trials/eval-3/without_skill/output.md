# Nimbus Users Group annual gathering: hybrid setup, venues, hackathon prizes

I don't know your city, budget, or dates, so the venue section is a scoring framework and a method, not named venues. Naming real venues without a location would be invented. Give me the city and a budget range and I'll turn the framework into a named shortlist.

## 0. Settle the format first

Conference versus hackathon versus hybrid is the real decision. Everything else depends on it.

**Recommendation: a 2-day event with a conference day and a hackathon day.**

| Day | Content | Remote role |
|---|---|---|
| Day 1 | Single-track talks, lightning talks, hallway and community time | Watch the stream, ask questions, join a remote "hallway" |
| Day 2 | Hackathon (about 8 hours of build time, then demos) | Full remote teams or mixed teams |

- One track keeps streaming cheap and the audience unified.
- Talks give the hackathon a theme and recruit teams.
- At 2,000 members, expect about 400 on-site and 300 to 600 remote viewers. Most of the remote audience will watch Day 1 only.

**Decision rule:** hybrid is worth it only if remote members get a real role. A stream nobody can talk back to is a recording with extra cost. Pick one of two levels:

- **Level A, "stream plus chat" (recommended for year one).** Talks stream live, remote attendees ask questions in chat, and the hackathon has a remote track. Cost is about 3 to 5 volunteers and 1 to 2 camera operators.
- **Level B, "true hybrid".** Remote attendees appear on screen, join workshops, and have remote hallway rooms. This needs a dedicated remote host and a second production crew. Treat it as a year-two goal.

## 1. Hybrid streaming design (Level A)

**Principle:** treat the stream as a TV show with a producer, not as a camera pointed at a stage.

### Roles (minimum 5 people)
1. **Stream director** runs the switcher and the live graphics.
2. **Audio lead** handles the mixer and the speaker mics.
3. **Remote host** relays chat questions to the MC and welcomes remote participants.
4. **Camera operator** (1 or 2).
5. **Hackathon remote liaison** on Day 2.

Pay a professional AV crew for the stage and audio if you can. Volunteers can cover the remote host and chat roles.

### Signal chain
- **Cameras:** 2 minimum. One wide shot and one tight speaker shot. A third is optional for the audience and sponsor shots.
- **Slides:** capture the presenter laptop HDMI directly. Never film the screen.
- **Audio:** lavalier or headset mic per speaker, plus a handheld for Q&A. Send a dedicated mix to the stream, separate from the room mix.
- **Switching:** ATEM Mini Extreme or similar, or OBS or vMix on a dedicated machine.
- **Encoding and delivery:** 1080p30 at 6 Mbps, via a wired connection.
- **Redundancy:** a bonded or cellular backup uplink (a second ISP or a bonding box). Test failover before the day.
- **Recording:** record locally, separate from the stream, with isolated tracks if possible.

### Platform
- **Public stream:** YouTube Live. It is free, has a DVR, and works for reach and replay.
- **Member-only option:** if some content is for members, use an unlisted link or a gated page.
- **Interaction:** a dedicated chat channel in your existing community space (Slack or Discord). It gives you identity and moderation you already run.
- **Q&A:** Slido or a similar tool with upvotes, so the remote host can pick the top questions. Show remote questions on the same footing as the room's.
- **Remote hallway (optional):** a persistent video room, such as Gather or a Discord stage, open during breaks.

### Rules that make remote members feel included
- Every talk gets a remote question first.
- Speakers repeat audience questions into the mic.
- The schedule is posted in one time zone, with conversions shown.
- Breaks are at least 20 minutes, with a remote activity during each one.
- Subtitles: auto-captions as a baseline. Budget a live captioner if you can afford one.

### Hackathon with remote teams
- Remote teams use a shared repo template, a channel per team, and a mentor rota that covers remote teams explicitly.
- Demos are 3 minutes each. Remote teams demo by pre-recorded video plus live Q&A.
- Judging uses one rubric for both on-site and remote teams.

### Rehearsal and risk
- **Tech rehearsal:** the day before, on site, with a full run of slides, video, mics, and failover.
- **Run sheet:** a minute-by-minute document with cue owners.
- **Common failures:** speaker laptop HDMI/adapter issues, Wi-Fi congestion with 400 devices (keep the production network separate and wired), and echo from remote audio playing into the room.
- **Go/no-go gate:** if the venue cannot guarantee a wired, dedicated uplink of at least 50 Mbps up, drop it from the shortlist.

### Rough streaming budget (order of magnitude, varies a lot by country)
- DIY with volunteers and rented gear: low four figures.
- Professional AV crew, 2 days: mid four to low five figures.
- Venue in-house AV is often cheaper than hiring an outside crew, so ask each venue for a package price.

## 2. Venue shortlist for about 400 people

### Hard requirements
| Requirement | Target |
|---|---|
| Main room | 400 theatre-style (or 250 to 300 cabaret) |
| Breakout space | 2 to 3 rooms of 40 to 80 for workshops, and a hackathon hall |
| Hackathon hall | About 2 to 3 m² per person with tables and power. Many attendees will self-select on Day 2, so plan for 150 to 250. |
| Power | Power strips at every hackathon table |
| Network | Wired, dedicated production uplink (see the gate above), plus attendee Wi-Fi rated for 400+ devices |
| Accessibility | Step-free access, accessible toilets, quiet room |
| Catering | In-house or approved caterers, with dietary options |
| Access | Near public transit, with hotels nearby |
| Hours | Late access on Day 2 (hackathon) |
| In-house AV | Stage, projection, rigging points for cameras |

### Venue types to compare
1. **University or tech campus lecture hall plus labs.** It is cheapest and often has great Wi-Fi and power. Weak points are catering rules and booking lead times.
2. **Conference center or hotel meeting space.** It has everything built in, but it is the most expensive.
3. **Coworking or innovation hub event floor.** It has a good hackathon atmosphere. The main room is often too small, so you may need a second site.
4. **Converted industrial or cultural venue.** It has character and flexibility, but AV and network are often your responsibility.

For this format I'd shortlist two of the first type and one each of the second and third, then compare.

### Scoring sheet
Score 1 to 5 and weight as shown:

| Criterion | Weight |
|---|---|
| Fit of main room and hackathon space | 3 |
| Network and power | 3 |
| Total cost (venue, AV, catering, extras) | 3 |
| Accessibility and transit | 2 |
| AV and streaming readiness | 2 |
| Date availability, mid-fall | 2 |
| Atmosphere | 1 |

### Process
1. Send each candidate one standard request: dates (two options), headcount, the room list above, AV and network questions, and a request for an all-in quote.
2. Visit the top three with the AV lead, not only the organizers.
3. Ask for a hold on dates with a free-cancellation window.
4. Check for exclusive-supplier rules (caterer, AV) before you fall in love with a space.

Fall is peak conference season, so start contacting venues now. Good venues for next fall are often booked 9 to 12 months ahead.

## 3. Hackathon prizes

### What motivates your audience
Users-group members are practitioners, not students. Cash matters less than recognition, career value, and useful tools. Design prizes that serve the community and aren't just a payout.

### Prize structure (adjust to budget)
**Main awards (3 to 5 categories, split by judging criteria):**
1. **Best overall project.** The headline prize.
2. **Most useful to the community.** Judged by members, with a public vote across the whole group (including remote members).
3. **Best use of Nimbus** (or the technology that defines your group). Technical depth.
4. **Best remote team.** A deliberate prize that rewards the hybrid format.
5. **Best first-time hackathon team.** It lowers the barrier to joining.

**Prize types, in order of effectiveness for this audience:**
- **Cash or travel grants.** A modest cash pool, or sponsored travel to a larger conference, is the strongest option. Even a small amount signals seriousness.
- **Sponsor-donated credits and licenses.** Cloud credits, tool subscriptions, and training vouchers cost sponsors little and are worth a lot to winners.
- **Hardware.** Appreciated, but shipping to remote winners adds logistics and customs problems. Use it sparingly.
- **Recognition.** A featured slot at the next meetup, a showcase blog post, and a maintainer-endorsed repo listing. These cost nothing and are valued highly.
- **Mentorship.** One-on-one sessions with a respected member or sponsor engineer.
- **Continuity.** A small follow-up grant or support to turn the winning project into something the community maintains.

**Starter budget, if you have little sponsorship:** the first three categories get cash (for example 1,000 / 500 / 300 in your currency, scaled to what you raise), and everything else is non-cash. Raise this with sponsors, not from the group's own funds.

### Rules that keep it fair
- Publish the rubric before the event: impact, technical quality, completeness of the demo, and community usefulness.
- Use judges with no conflict of interest. Sponsor staff should not judge their own sponsor's prize.
- State the IP position up front. Entrants keep ownership. Consider requiring an open-source license for the prize-eligible work.
- Require that remote and on-site teams are judged by the same rubric and on the same demo format.
- Make eligibility explicit: team size (2 to 5), pre-existing code rules, and conduct policy.
- Check local rules on prize draws and cash prizes, and on taxes for winners in different countries. This is a real issue for remote prizes, so decide who is the payer.

## 4. Suggested next steps (in order)

1. **Decide format and level.** Confirm the 2-day plan and Level A for streaming. This week.
2. **Fix the constraints.** Set the date window, city, budget range, and expected on-site headcount.
3. **Form a team.** Name an owner for venue, production, program, hackathon, and sponsors.
4. **Send venue requests** to 6 to 8 candidates, then shortlist 3.
5. **Open sponsor conversations.** Sponsors fund the prizes and the AV. Build the sponsor pitch from the audience numbers.
6. **Publish a save-the-date** and a call for talks and mentors.
7. **Set a go/no-go checkpoint** about four months out on venue, budget, and registrations.

## Questions I need to finish this

1. Which city or region, and is the group international or local?
2. What is the budget range, and are sponsors lined up?
3. What does Nimbus do? Prizes and hackathon themes depend on it.
4. Roughly what share of the 2,000 members is local to the venue?
5. Do you prefer cash prizes or non-cash prizes?

Answer those and I'll produce the named venue shortlist, a day-by-day program, and a costed budget.