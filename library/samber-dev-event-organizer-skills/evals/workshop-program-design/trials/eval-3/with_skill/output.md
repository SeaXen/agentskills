# Does 120 minutes hold up for the Quarry Summit hands-on sessions?

**No. Don't put 120 in the call yet.** The arithmetic is right (150 + 180 + 50 = 380, and 380 / 3 ≈ 127), but the method fails. The skill says to observe session length and never prescribe it, and it says not to pick a slot length by averaging across events.

## Why the average misleads

1. **The 50-minute session isn't comparable.** *Find Your Team* is a team-formation session, a social mechanic with no exercise in it. The evidence file makes this exact point: MLH's team-formation sessions run under an hour, and that figure is "not the short end of a range" that includes hands-on sessions. Including it drags the mean down by roughly 25 to 30 minutes.
2. **The comparable data points are 150 and 180.** The skill's record shows genuine hands-on technical sessions landing at 150–180 minutes: DevOpsDays Amsterdam 2017 ran 150-minute blocks, and Singapore 2025 ran 180 minutes as four 45-minute segments. Your two real data points match that range, and 120 sits below both.
3. **Each event's length reflects its own rooms, cohort and exercise.** The skill says to take the granularity, not the number. The granularity is 45 minutes almost everywhere.
4. **Three events is too few for an average.** The skill's evidence file refuses to compute one for the same reason.

## What should set the number: your exercise

Your exercise has three parts plus a wrap-up. That's close to Singapore's shape of four 45-minute segments. Two ways to get a length:

| Approach | Result | Holds if |
|---|---|---|
| Four 45-minute segments (three parts plus wrap-up) | 180 min | each part really needs a full segment, including stuck-participant recovery |
| Three 45-minute parts plus a shorter wrap-up | about 150 min | the wrap-up is roughly 15 minutes |

These are illustrations of the method, not recommendations. I don't have your per-part timings, and the right number comes from them.

To get it, time each part by someone who isn't the author, or rehearse it. Then add recovery time. The skill says to build troubleshooting and questions into the schedule. It also says to size the opening to the room, so add an icebreaker if the room is small. Round up to the nearest 45-minute multiple, or 15 minutes if the grid needs finer steps.

If the honest total comes out near 120, say so in the CFP. A figure derived from your exercise is defensible. One borrowed from an average isn't.

## Why this matters before the CFP goes out

The length is a promise to speakers and to the grid. `event-schedule-design` consumes it as a fixed input, and a CFP that says 120 is hard to walk back to 150–180 once proposals are written to that length.

## Questions I need answered

1. **How long does each of the three parts take, and the wrap-up?** Is this timed from a rehearsal or only estimated?
2. **Does the exercise need installs, accounts or a live network service?** That drives prerequisites and network posture, which also affect what the CFP should say.
3. **What's the expected headcount, and who besides the instructor will be in the room?** Capacity is the lowest of three ceilings (room, coverage, exercise throughput), and the CFP may need to state it.
4. **What has the venue said in writing about the room's network?** If it hasn't answered and the exercise is network-dependent, the hands-on rung may need to change.

Once I have the answers to 1 and 2, I can give you a length plus a short CFP line. Let me know if you want the full per-session delivery sheet too.