## The gamification idea won't fix this — here's why, then what will

**Points, badges, and a leaderboard reward *attendance*. Your problem isn't attendance — 40-55 people a month for a year proves attendance is solved. Your problem is that nobody has ever been asked to do anything.** A leaderboard for "came 3 times in a row" tells someone they're a loyal customer. It doesn't tell them there's a door to walk through, or make that door easy to find. Gamification systems convert intent into action for people who already *want* to contribute but lack a nudge — they don't manufacture the desire in people who've never been asked. You'd spend real engineering time (site backend, badge logic, leaderboard UI) optimizing the wrong variable.

There's a second risk: a public leaderboard for a volunteer-run community meetup can read as slightly absurd to the Brazilian K8s crowd you're courting — devs who show up expecting engineering peers, not a loyalty program. Worst case it becomes a running joke ("bro's trying to gamify pizza attendance") that undercuts credibility with exactly the senior engineers you want speaking.

## What's actually broken

Four people means zero redundancy and zero pipeline. If any of you burns out or moves cities, the group stops. That's the real board-level risk, more than "lurkers." The fix is a **volunteer ladder** — a sequence of increasingly-visible, increasingly-committed asks — not a scoreboard.

## The plan

**1. Make the ask explicit and specific, every single event.**
Right now the ask is implicit ("someone should help"), which nobody ever picks up. Replace it with a 30-second announcement + a physical sign-up sheet or QR code at the door, every meetup, for named micro-roles:
- Setup/teardown (arrive 30 min early, fold chairs after)
- Photographer (10 photos on your phone, post-event)
- 5-minute "lightning talk" slot next month (topic can be "a tool I used this week," zero prep bar)
- Newsletter/recap writer (one paragraph, what was discussed)

Small, bounded, one-night commitments. Nobody says yes to "help organize the meetup." People say yes to "hold the door for twenty minutes."

**2. Build a speaker pipeline, not a speaker monopoly.**
One guy always volunteering to speak means you have zero bench and he's quietly carrying the group. Fix: reserve 5 minutes every meetup for a lightning talk from someone new (see above), rotate who gets asked directly, and keep a running list of "who mentioned something interesting at the bar afterward — ask them to turn it into 5 minutes." Direct, personal asks ("hey, what you said about Karpenter was great, want to do 5 min on that next month?") convert far better than an open call for speakers.

**3. Rotate the door duty instead of owning it.**
Your two friends doing the door every month is itself the bug, not just a symptom. Ask two different attendees per event to co-run the door with them. After 2-3 rotations, some of them will want to keep doing it — that's your next generation of core organizers, self-selected by actually showing up to do the job, not by points earned.

**4. Give returning attendees a place to self-organize between events.**
If there's no WhatsApp/Telegram/Discord group, create one and hand moderation to 2-3 regulars (not you). Most conversion happens in the gap between events, when someone asks "anyone doing X with K8s?" and a lurker realizes there's a person, not just a monthly dinner, behind the group.

**5. Recognize specifically and publicly, in the moment — not via leaderboard.**
"Thanks to Marina for running the door tonight and to Diego for his first lightning talk" from the mic, plus a one-line shoutout in the recap post, does more for conversion than a persistent point total. Specific, timely, public credit signals "this group notices and needs people," which is the actual thing that turns a lurker into a volunteer. A leaderboard signals "this group tracks you," which is a different and much less motivating message.

**6. Track a volunteer funnel, not points.**
Measure what the board actually cares about — bus-factor risk — not engagement theater:
- New people who did *any* task (setup, photos, talk, door) this quarter
- First-time speakers this quarter
- People who've done 2+ different roles (your actual organizer pipeline)
- Core team size (currently 4 — target 8-10 within a year)

Report this to the board instead of attendance count. It directly answers "are we still a 4-person single point of failure."

## If the board still wants the badges

Don't build a backend for it. Use what's already visible: name the 3-in-a-row attendees from the mic once a quarter ("these folks haven't missed a meetup since March — if that's you, come say hi, we want your help") and hand *them* the direct ask from step 1. That's the entire useful function of the badge idea — a targeting list for who to approach — achieved with a spreadsheet and a sentence, not a website feature.