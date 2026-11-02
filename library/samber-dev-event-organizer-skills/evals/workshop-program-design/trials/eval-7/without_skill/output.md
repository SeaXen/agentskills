# Fallback plan: Kafka workshop, Highfield Conf

**Next action (15 min):** stop emailing the venue. Phone the Highfield Conf organizers and ask them to chase the venue for you. Three unanswered emails show the venue's IT contact isn't reading them. Details are in step 1 below.

## Recommendation

Build a **local, offline version of the lag exercise** and keep it ready as the fallback. You said there's no offline version, so this is new work. It is the right fallback because your claim doesn't need the hosted cluster. The claim is "you can watch consumer lag grow and recover", and a local broker produces real lag.

Lag is `log-end-offset − committed-offset`. Run a producer at a steady rate and a deliberately slow consumer, and lag climbs for real. Speed the consumer up and it drains. Nothing is faked.

What you lose is the hosted cluster's real network latency and shared-cluster behavior. You keep the lesson itself.

The fallback ladder (a default from the live-demo-design skill, not an industry standard):

| Tier | What runs | When |
|---|---|---|
| A | Hosted cluster over venue Wi-Fi | Network works at the room check |
| B | Hosted cluster over hotspot or tethering | Wi-Fi is bad but cellular is good in the room |
| C | **Local broker on each attendee laptop, same lag exercise** | Both fail. This is the real fallback. |
| D | Presenter-only local demo on the projector, plus a recording | Attendee laptops can't run the stack |
| E | Recorded screencast with live narration | Presenter laptop trouble |

## Steps

### 1. Escalate to the venue (this week, 15 min)

- Phone the organizers and ask for a named IT contact and a direct number.
- Ask four things:
  - Is guest Wi-Fi available for N attendees?
  - What is the bandwidth and the client cap?
  - Are outbound ports open? Kafka needs your broker port, typically 9092/9093 or TLS 9094. Many venue networks block everything except 80 and 443.
  - Can you test from the room the day before?
- Set a deadline: no answer by **week 4**, so assume the network is unusable.
- Test your hosted cluster against a locked-down network now: a phone hotspot, and a laptop on a captive-portal Wi-Fi if you can find one. If it only works on open ports, say so in the attendee prerequisites.

### 2. Build the local lag exercise (weeks 2–4, roughly 1–2 days of work)

- Use a single-broker KRaft setup. Redpanda or Apache Kafka in a container are both fine.
- Ship one `docker compose up` (or a plain tarball with a start script) with:
  - a topic with 3 partitions,
  - a producer at a fixed rate, such as 50 msg/s,
  - a consumer with an adjustable delay, such as `SLOW_MS=200`,
  - a lag view: `kafka-consumer-groups --describe` in a watch loop, or a small Grafana/Kafka UI container.
- Match the hosted exercise step for step. The worksheet should differ only in the bootstrap server address and credentials.
- Write the exercise steps so each one starts from a restore point. A broken step then can't block the next one:
  1. Baseline: lag near 0.
  2. Slow the consumer: lag grows.
  3. Add a second consumer: partitions rebalance.
  4. Recover: lag drains.
- Make the reset one command, run from a cold machine.
- Don't fake output. Seeded data and a fixed producer rate are fine. Pre-filled lag numbers are not.

### 3. Pre-pull everything for attendees (weeks 5–6)

- The fallback fails if attendees need the internet to download images in the room.
- Put the image tarball (`docker save`) and the compose files on **USB sticks**, or on a local hotspot-served file share. Test on both macOS and Windows.
- State the requirement in the pre-event email: "install Docker and run `./verify.sh` before arriving". Have the script check for Docker, free RAM and free ports.
- Ask attendees to run the local stack once at home. Expect around 20–30% to skip it, so keep spare sticks and a plan for pairing.
- Cap the broker's memory (for example 512 MB heap) so it runs on low-end laptops.

### 4. Plan the day (week 7)

- **Day before or morning of:** at the room, test the hosted cluster on venue Wi-Fi and on your hotspot. Bring a hotspot with a real data plan. Check the signal at the back of the room.
- **Decision rule, decided now:** if the hosted exercise isn't working within **5 minutes** of the start, switch to tier C. Do one repair attempt, then switch.
- Put a Go/No-Go line on the opening slide so attendees see it as a plan, not a failure. For example: "We run this on a hosted cluster. If the network disagrees, we run the identical exercise locally."
- Write the switch line in advance: "The network isn't cooperating, so we're running the same exercise on a local broker. The lag behaves the same way."
- **Human redundancy:** ask a co-presenter or helper to hold a clone of the repo, the image tarball and the recording on a second laptop.

### 5. Rehearse the switch (week 7, about 1 hour)

- Disconnect the network and run the full local exercise from a cold state, three times in a row.
- Time the switch from hosted to local. The target is under 60 seconds for you, and a few minutes for attendees to start the stack.
- Run one pass at the venue's resolution (see the live-demo skill's environment hardening checklist).

### 6. Record the tier E backup (week 7)

Record a screencast of the full exercise run locally, with captions. It covers a dead presenter laptop or a projector that won't mirror.

## Open questions

These change the plan if the answer differs from my guess:

1. **How many attendees?** Over about 30 makes tier C (local on every laptop) harder to support. Plan pairs.
2. **Do attendees bring their own laptops?** If yes, tier C is feasible. If you provide machines, you control the stack.
3. **Does the hosted cluster support many simultaneous consumers?** Test it with a load rehearsal, because it's your tier A and B dependency.
4. **Does the lesson depend on shared-cluster behavior** (several attendees' consumers in one group, noisy neighbors)? If so, tier C loses that part, and you should say so in the worksheet.

## Timeline

| Week | Action |
|---|---|
| 8 (now) | Phone the organizers, test the hosted cluster on a restricted network |
| 6–4 | Build the local exercise and the verify script |
| 4 | Deadline for the venue's answer; after it, assume no usable network |
| 3 | Pre-event email with prerequisites, USB sticks prepared |
| 2 | Cold-start rehearsals, offline run |
| 1 | Record the backup screencast, brief your helper |
| Day before | Room check: hosted cluster and hotspot |