# Your Ferrolane Devcon Lightning Talk (5 min)

## Title options (pick one)
1. **"Our Queue Was on Fire: A Redis Streams Postmortem"**
2. **"How We Killed Our On-Call Pager With Redis Streams"**
3. **"Consumer Groups Lied to Us: A 5-Minute Incident Story"**

Go with #3 if you want the room hooked in the first sentence — lightning talks live or die on the first 10 seconds, and "X lied to us" promises a war story, not a tech pitch.

---

## Speaker script (timed for ~5:00 at a normal pace)

**[0:00–0:15] Hook**
> "Six months ago our queue backlog hit [N hundred thousand] messages, our on-call engineer was getting paged at 3am [X] nights a week, and the fix turned out to be one line of config we'd misread from the docs. This is that story in five minutes."

**[0:15–1:00] The backlog problem**
> "Here's what we were running: [old system — e.g. a single Postgres-backed job table / RabbitMQ / SQS]. It worked fine until traffic grew. Once we crossed [N events/sec], the backlog started growing faster than we could drain it — not a spike, a slope. Every deploy, every traffic bump, the lag went up and never fully came back down. By the time we started this project, worst-case processing lag was [N minutes/hours], and it was trending the wrong way."

Slide: one chart — backlog size over time, climbing. That's the whole slide.

**[1:00–1:45] Why Redis Streams**
> "We evaluated three options: [Kafka, SQS, keep patching the old system]. We picked Redis Streams for three reasons: we already ran Redis in production so zero new infra, consumer groups gave us at-least-once delivery and per-consumer tracking out of the box, and XPENDING/XCLAIM gave us a built-in dead-letter story without bolting on a separate DLQ system. Kafka was more powerful but was a new ops surface for a team of [N] — we didn't want a second database to learn under pressure."

**[1:45–3:15] The consumer group bug — the centerpiece**
> "Here's where it got interesting. Two weeks after launch, we noticed messages being processed twice — not occasionally, consistently, for one specific consumer. Took us [N hours] to find it: when a consumer pod got OOM-killed mid-batch, the messages it had claimed via XREADGROUP stayed in the Pending Entries List forever — nobody was reclaiming them. We'd read the consumer group docs and assumed Redis would auto-expire stale pending entries. It doesn't. You have to run XCLAIM yourself, on a timer, checking idle time.
>
> So a rolling deploy — a totally routine event — was silently orphaning a batch of messages every single time, and they'd just sit there until someone manually intervened. The fix was a background reaper goroutine: every [N seconds], XPENDING to find entries idle longer than [N seconds], XCLAIM them back, retry with a cap, then dead-letter. Fifteen lines of code. It just had to exist, and it didn't."

This is your money section — slow down here, this is the part people remember.

**[3:15–3:45] Metrics we added**
> "We were flying blind before this, so we instrumented: consumer lag per group, pending-entries count, claim/retry/dead-letter rates, and processing latency per message type. That last one mattered most — it's what caught the duplicate-processing bug in the first place, because latency for that consumer had a weird bimodal shape."

**[3:45–4:05] The dashboard**
> "One Grafana dashboard, four panels: lag, pending count, throughput, error rate — per consumer group, not just globally, because the bug above only showed up on one group out of six. That granularity is the whole point; an aggregate dashboard would have hidden it."

**[4:05–4:25] On-call rota change**
> "Once lag and pending-count had real alert thresholds instead of 'the queue looks big,' we cut the rota from [N] engineers on a [weekly] rotation down to [N], because the false-positive pages — the ones that trained people to ignore the pager — mostly disappeared. Page volume dropped [X%]."

**[4:25–4:40] Cost savings**
> "Net effect: we decommissioned [old infra], and total messaging infra cost dropped [X%] / $[N]/month, mostly because Redis Streams ran on infra we already paid for."

**[4:40–5:00] What we'd do differently + close**
> "Two things: we'd write the reaper on day one, not day fourteen — 'consumer groups handle failure for you' is a myth worth distrusting by default. And we'd have built the per-group dashboard before launch, not after the bug forced our hand. If you're running consumer groups in production right now without something calling XCLAIM on a timer, that's your action item — go check. Thanks."

---

## Slide count: 7–8 max
1. Title
2. Backlog chart (climbing line)
3. Why Redis Streams (3 bullets)
4. The bug (diagram: consumer dies → PEL entry orphaned → duplicate processing)
5. The fix (reaper loop, 4 steps)
6. Dashboard screenshot
7. Before/after: page volume + cost
8. "What we'd do differently" + contact/handle

Delivery note: at 5 minutes, you will lose time somewhere — it's always the bug section, because it's the fun part to over-explain. Rehearse with a timer once, and if you're over, cut from the "why Redis Streams" section, not the bug — that's what people came for.

---

## On your acceptance-rate question

I don't have real numbers for Ferrolane Devcon specifically — I have no data on that conference's CFP stats, and I'd be guessing if I gave you a figure, so I won't invent one. Worth checking directly: some conferences publish CFP acceptance rates in a retro blog post or the organizers will just tell you if you ask.

What's true in general, industry-wide, and worth calibrating on instead of a fabricated number:

- Lightning-talk slots are almost always easier than main-track, for structural reasons, not just lower standards: there are more slots (a 5-min format lets organizers fit 8–10 talks in the time of two main-track talks), the commitment they're asking speakers for is smaller so more people apply relative to how many actually show up polished, and the bar is "tell one good story fast," not "carry 40–45 minutes."
- The gap varies a lot by conference — anywhere from "main track is 3x harder to get into" at large well-known events, to "barely different" at smaller/regional conferences that struggle to fill their lightning slots at all.
- Some conferences run lightning talks as first-come/sign-up-at-the-door with no review at all, which makes "acceptance rate" not even a meaningful concept for that slot.

If you want an actual number for Ferrolane Devcon, check their CFP page, past-year retro posts from organizers, or ask them directly — happy to help you draft that email if useful.