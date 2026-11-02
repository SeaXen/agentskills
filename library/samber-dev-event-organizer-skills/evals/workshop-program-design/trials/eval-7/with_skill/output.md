# Fallback plan: Kafka workshop at Highfield Conf

## Verdict

⚠️ Your fallback can't be an offline version of the hands-on exercise, because none exists. The fallback is a **demonstration run on a connection you control**, with the hands-on exercise published for participants to do afterwards.

The skill's rule also affects the plan itself. Your exercise needs a live network service (Q4), and the venue has given no written answer about the network (Q9). Under that combination the skill strikes full hands-on from the menu. You have eight weeks, so I'd treat hands-on as conditional on a gate, not as a settled commitment. I haven't re-argued your wish to run it hands-on.

I haven't asked the interview questions, so the assumptions below are marked. Correct any that are wrong.

## 1. Hands-on commitment: conditional

- Hands-on stays the goal because reading can't teach watching real consumer lag (Q2).
- **Gate:** by about week 4 (my date, not a standard), get a written venue answer to the three questions in section 4.
- **If the gate passes:** run full hands-on, with the fallback below as insurance.
- **If the gate fails:** run the demonstration and publish the exercise. Three unanswered emails count as the venue's answer. The skill says "the answer being unavailable is the evidence."
- Don't leave hands-on half-alive, because a struck rung that stays on the menu comes back as scope on the day.

## 2. The fallback ladder

Decide the triggers now, and agree the live switch-over with whoever owns `event-run-of-show`. Don't improvise it on the day.

| Rung | What happens | Survives |
|---|---|---|
| **A. Participants use own data** | Prerequisites say: "If the room Wi-Fi fails, use your own mobile data." This is the published pattern, "(Use Wi-Fi or your own data)". | Venue network fails entirely |
| **B. Demonstration only** | You drive on one machine with its own uplink, and the room watches real lag. | Most participants can't connect |
| **C. Publish and do later** | Repo, steps and cluster access go out with an announced access window. Participants run the exercise at home. | Everything on the day |

- **Trigger A to B (my threshold):** if fewer than about 70% of seats are connected and producing or consuming 15 minutes in, switch. Pick your own number in advance.
- **Your uplink (my suggestion, not from the skill):** use a separate mobile hotspot or second SIM for the instructor machine, so the demo doesn't share the venue network.
- **Rung C is the floor.** It's the skill's "no live hands-on" rung, so the content gets delivered whatever the room does. Ship it either way.
- **What the fallback costs:** participants lose doing it themselves. You keep watching real lag, which was the point.
- **Don't build a recorded-lag version as the main fallback.** It's an offline stand-in for the one thing you said has no offline version. Keep it only as a last resort if your own uplink dies too, and label it as a recording.

## 3. Prerequisites that cut failure odds

Split them into knowledge, machine state and accounts. Accounts fail worst at minute zero.

- **Declare the dependency:** "Internet required: hosted Kafka cluster."
- **Known policy breakers:** "Turn off VPN. Pause ad-blockers for the lab domain."
- **Pre-download clients and tools** before the day, so a room of cold installs doesn't hit the network at once.
- **Accounts:** if participants need a vendor signup, they should finish it before arriving.
- **My inference, unverified:** a native Kafka client connects on a non-443 port. Venue networks often block those ports even when HTTPS works. Ask the venue about this specifically. If a browser console exists, it may be the safer path.
- **Credentials and terms:** check who accepts the platform's terms and issues credentials (Q10), and whether any participant is a minor.

## 4. Get the venue to answer

The written questions:

1. How many simultaneous devices does the room hold, and what happens at the limit?
2. Which protocols and ports are blocked, and can they be opened for a day? List the broker ports.
3. Are unusual device classes blocked, and who can grant an exception on the day?

- **Ask differently:** send one short email with these three numbered questions and a reply-by date. Then phone, or go through Highfield's organizers.
- **Test the room:** if you can't reach the venue, ask Highfield's organizers or a local contact to test the cluster from the room.

## 5. Sizing and coverage

- **Capacity:** take the lowest of three ceilings. The one most likely to bind is throughput, meaning per-participant cluster access and logins. State which one bound.
- **Coverage:** if hands-on survives, delete the "solo instructor" rung. Recruit one roaming troubleshooter who can debug setup. That sizing is mine, based on one linear exercise path, not on a ratio.
- **Hand to `event-schedule-design`:** length and capacity. Your real hands-on session length is your call. The published range is 150-180 minutes.

## 6. Revision triggers for next edition

- Venue answers in writing and the room works: keep hands-on with the declared-dependency posture.
- You hit the A to B switch: make "clear the network in writing" a hard gate, or run the demonstration plus rung C by default.
- Metrics to track: **ready at minute zero** (ask at the door) and **started versus finished**. If the first is low, move up the prerequisites menu.

## What to do this week

1. Resend the three questions in the form above and set a reply date.
2. Draft the prerequisites page, including the "own data" line.
3. Write down the A to B threshold and who calls it.

Which role are you in: organizer, or speaker routing through the conference? It changes who should chase the venue.