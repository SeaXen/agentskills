# Booth staffing plan: 20x20, 3 days, 9:00-18:00

## Short answer

Don't staff 8 at once. Staff 4 on the floor, rotating in 90-minute blocks, with exactly one engineer in every block. Pull in the off-shift people only for the break-time rushes.

## Why not 8 at once

- **50 sq ft per person is a ceiling, not a target.** It assumes an empty box. A counter, demo screen, storage and a space for attendees to stand take roughly half your 400 sq ft. That leaves about 4 comfortable staff.
- **Six non-engineers on the floor at once would hurt you.** At a Python conference, attendees look for someone who can answer technical questions. A crowd of people who can't answer them makes the booth look like a sales stand.
- **Eight people for 9 hours is 72 person-hours a day.** Four on the floor is 36. Over 3 days, the first plan burns everyone out. The second is sustainable.
- **The binding constraint is the two engineers, not the headcount.**

## The plan

**Rule:** 4 on the floor in every block, made up of 1 engineer and 3 non-engineers. Blocks are 90 minutes, and each person works 90 minutes on, then 90 minutes off.

| Block | Time | Team |
|---|---|---|
| 1 | 9:00-10:30 | X |
| 2 | 10:30-12:00 | Y |
| 3 | 12:00-13:30 | X |
| 4 | 13:30-15:00 | Y |
| 5 | 15:00-16:30 | X |
| 6 | 16:30-18:00 | Y |

- **Team X:** Engineer A, plus marketing M1 and M2, plus customer success C1.
- **Team Y:** Engineer B, plus marketing M3, plus customer success C2 and C3.
- **Day 2:** Swap the teams, so Y takes blocks 1, 3 and 5. Nobody owns the 9:00 opening or the dead 17:00 hour all three days.
- **Day 3:** Reshuffle the non-engineers across teams, but keep one engineer per block.
- **Load per person:** Each person works 3 blocks, or 4.5 hours, per day. The engineers get 4.5 hours of booth time and 4.5 hours free to attend talks and hallway conversations, which also helps your technical credibility.

## Break-time surge

- **Get the session schedule first.** Booth traffic follows the program: it spikes in the breaks between sessions, at lunch, and after the keynote. It drops while talks are running.
- **At the 2-3 biggest breaks each day, the off-shift engineer and one or two others join for about 30 minutes.** That takes you to 6 on the floor for a short burst, which fits the space.
- **During talk sessions, drop to 3** by letting one non-engineer step off.
- **Hand-offs:** Overlap by 10 minutes, and don't swap all four people at the same minute. The outgoing person briefs the incoming one on who is mid-conversation.

## Making non-engineers useful

Give the six a defined job, so they aren't improvising technical answers:

1. **Greeter and qualifier.** Open with a question, not a pitch. Ask what they build, which Python stack they use, and what hurts today. Log it in the lead scanner as a one-line use case, not just a badge scan.
2. **Demo driver.** Train one or two people to run a 3-minute scripted demo. They should be able to say "I'll get an engineer for that part" without embarrassment.
3. **Escalation signal.** Agree on a hand-off, such as a glance or a "engineer to the counter" call. The non-engineer stays with the person, introduces the engineer with the context already captured, then steps back.
4. **Customer success on existing customers.** Customers at the show are a real use of CS time: check-ins, feedback, and referrals. Send them to CS rather than the general queue.

Run a 30-minute rehearsal before the doors open on day 1, with the engineers playing hard-question attendees.

## Biggest risk and the fix

You have one engineer on the floor at a time, and a single hard question can tie them up for 10 minutes. Mitigate it in order of effort:

- **Best:** Add one or two more technical people for the 3 days. A DevRel colleague, a solutions engineer, a contractor, or a community contributor who knows the product would all work. Even half-days at the break peaks help most.
- **Next:** Put a visible "ask an engineer" slot on the booth sign and schedule 30-minute office hours at the peak breaks.
- **Fallback:** Let attendees book a 15-minute follow-up with an engineer through a QR code. This turns queue overload into a qualified lead.

## Checklist

1. Get the conference program and mark the break times.
2. Fix the A/B teams and the day 2 and day 3 swaps.
3. Write the 3-minute demo script and the 3 qualifying questions.
4. Book the 30-minute rehearsal.
5. Decide whether to add a third technical person.

## Assumptions to check

- The hall is open continuously 9:00-18:00 with no closed-hall windows.
- Your booth contract doesn't cap badge-holder numbers. Check how many exhibitor badges the package includes, since 8 staff plus any extra technical help may exceed it.