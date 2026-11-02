Using the tech-podcast-interview-prep skill (and its reference files) to build your brief. Two hours, recording at 9am — here's the re-ranked plan and the actual brief.

## Why this isn't a generic 12-step brief

The skill's own default for a two-hour ceiling is "spine + opening answer only, drop everything else, say what you dropped." I'm overriding that in one place: you sell a Postgres tuning product on the exact topic you were booked for, so "isn't this just an ad" is close to guaranteed, and the skill ranks hard questions above almost everything except the spine itself — one bad clip costs more than three good answers gain. So tonight buys you: angle, spine, opening answer, hard questions, disclosure line, two stories, recording-day card. Dropped, in order of what I cut first: full show reconnaissance (I have no real access to Bytecode Weekly's back catalogue tonight — see the 10-minute substitute below), the rest of the sound-bite set beyond three, the promotion loop (that's a tomorrow-afternoon problem).

Assumptions I made without being able to ask you one at a time — correct any of these before you start writing:
- Outcome you want: product credibility with technical evaluators + a hiring signal, not pure OSS-adoption (fix this if wrong, it changes message 3).
- Buying motion: B2B — someone on the call tonight is a future buyer's proxy, not just a hobbyist, so every number you say has to be one Tarnhelm already publishes.
- Off-limits, my default until you tell me otherwise: no named customers, no unpublished benchmark numbers, no pricing specifics, nothing about deals in flight.
- You haven't been on this show before.

Real reconnaissance substitute (10 min, do this before you start, not instead of it): pull up Bytecode Weekly on Apple Podcasts, skim the last 3-4 episode titles and descriptions. You're checking two things only — has a guest already done "war story about running Postgres huge," and does Priya's SRE-at-a-logistics-company background give you one rapport line (a supply-chain/inventory-database analogy lands with her specifically). Skip this and you're just trusting that your angle is fresh.

## Time box (2:00 total)

- **0:00–0:15** — Pick the angle (below), write the disclosure line.
- **0:15–0:35** — Spine + 3 messages, say each one out loud once.
- **0:35–0:55** — Write the opening answer, say it aloud until it survives being interrupted at second 10.
- **0:55–1:40** — Hard questions: read each cold in Priya's likely phrasing, answer, time it, redo your worst three.
- **1:40–1:55** — Slot your two real stories under the messages they back.
- **1:55–2:00** — Recording-day card. Sleep.

---

# Bytecode Weekly — prep brief

Recording: tomorrow, 9:00 · audio-only, edited · 45 min · solo host
Host: Priya — ex-SRE at a logistics company, now hosting. Rapport hook: she's felt what happens when a database becomes the thing standing between a warehouse and a truck leaving on time. Use an inventory/fulfillment-adjacent metaphor if one fits your story naturally; don't force it.
Audience: hands-on backend engineers. Anchor in API surface, failure modes, migration cost. Leave out org framing and market size.
Booked topic (host's words): "what nobody tells you about running Postgres at 40TB"
Off-limits: named customers, unpublished benchmarks, pricing, anything mid-negotiation.
Disclosure line (say this in the first five minutes, don't wait to be asked): **"I'm a staff engineer at Tarnhelm Data — we build a Postgres tuning product, so I've got a horse in this race. Everything I'm about to describe is stuff you'll hit whether or not you ever buy anything from anyone, including us."**

## Angle — pick one, don't try to cover all three

"40TB Postgres" is a topic; the host already handed you a contrarian frame ("what nobody tells you"), which does most of step 2's work for you. Narrow it to the one specific thing:

1. **Autovacuum is the wall, not disk.** *(recommended)* Everyone preps for storage cost and IOPS; the thing that actually corners teams at this scale is vacuum falling behind on the biggest tables — bloat, XID wraparound anxiety, freeze storms competing with production I/O. This is the most contrarian, most clippable, and it's the thing a tuning vendor is most credibly positioned to have war stories about.
2. **Nobody has actually restored the backup.** Backups complete fine at 40TB; restore time (not backup time) is the real RTO, and almost nobody has run a full timed restore end-to-end because it costs a day of someone's life. Strong if you have a real "we tested it and were shocked" moment.
3. **Replication lags exactly when you need it not to.** Physical streaming mostly holds up; it's initial sync of a *new* replica, or anything logical (single-threaded apply, no DDL), that quietly becomes a multi-day project. Pick this only if you have a sharper personal story here than on #1.

If none of these match what you've actually lived through, swap in your own — but keep the same shape: a thing everyone assumes is the problem (disk, backup completion, replica count) versus the thing that's actually the problem (vacuum throughput, restore time, sync time).

## Spine (ABT)

*(written for angle 1 — swap the clause if you pick 2 or 3)*

"Teams plan for 40TB like it's a storage problem, and disk is genuinely cheap enough that it isn't, **but** autovacuum runs out of runway long before the disk does, **therefore** the thing to instrument isn't free space, it's how far behind vacuum is on your biggest tables."

Say it out loud once. If it comes out as three facts with no "but," it's not done yet.

## Messages

1. **Claim:** Disk was never the constraint at this scale — vacuum throughput was.
   **Evidence:** [Pull one real number tonight: a table's dead-tuple percentage, an autovacuum duration, or how close a table got to the wraparound threshold, from your own dashboards or a customer engagement you're allowed to talk about in aggregate.]
   **So-what:** Watch `age(relfrozenxid)` and per-table dead-tuple ratio, not disk-free percentage, as your early-warning metric.

2. **Claim:** The fix that works at small scale (crank `autovacuum_vacuum_cost_limit` and walk away) stops working once a single table's vacuum takes longer than the interval between autovacuum runs.
   **Evidence:** [Your own before/after tuning number — e.g., how a per-table `autovacuum_vacuum_scale_factor` override, or splitting a monolithic table via partitioning, changed vacuum completion time on a real table.]
   **So-what:** Tune autovacuum per-table, not instance-wide, once any single table crosses roughly the hundred-million-row mark — the instance-wide default is sized for your smallest table, not your biggest.

3. **Claim:** At 40TB, the operational cost isn't the database — it's the fact that almost nobody on the team has ever watched a maintenance operation finish.
   **Evidence:** [A real example: how long a REINDEX CONCURRENTLY, a full ANALYZE, or a partition backfill actually took for you, and what that implied for who could be on-call for it.]
   **So-what:** Before you hit 40TB, someone on the team needs to have run every maintenance op you'll eventually need — vacuum, reindex, restore — at a scale big enough to see it not finish instantly.

Don't ship these with the bracketed placeholders still in them. If you can't fill in a real number for message 1 or 2 in the next twenty minutes, that message is weaker than you think and message 3 should move up.

## Opening answer

Punchline first, no credentials, survives being clipped with zero setup:

> "The thing that took down a Postgres cluster I worked on wasn't the disk filling up — it was autovacuum losing a race it had been quietly losing for weeks, on a table nobody was watching, until we were staring at transaction ID wraparound with hours, not days, to fix it."

Say it out loud, time it — aim for 20-25 seconds. If Priya would cut in before you finish, the important part is already out, which is the point.

## Hard questions

| Question | Concession (say first) | Bridge |
|---|---|---|
| "Isn't this whole episode just an ad for Tarnhelm?" | "Fair — I make money if teams hit this problem and come to us." | Message 1: the vacuum-vs-disk distinction costs nothing and works whether you tune it yourself or pay anyone. |
| "Why not just throw more hardware at it — bigger instance, more IOPS?" | "For a while, that genuinely buys you time, and cheaply." | Message 1: it buys you time against disk pressure specifically; it does nothing for a vacuum process that's single-threaded per table. |
| "Couldn't a DBA just watch dashboards and catch this early?" | "Yes, if someone's actually watching the right metric — most teams aren't, because it's not the metric people default to." | Message 1: `age(relfrozenxid)` and dead-tuple ratio, not disk-free. |
| "How is this different from just reading the Postgres docs / using pgtune?" | "Generic tuning advice is a fine starting point and gets most teams 80% of the way." | Message 2: the remaining 20% is table-specific, and that's where the instance-wide defaults stop being enough. |
| "Why not just use a managed service — RDS, Aurora, Cloud SQL — and let them handle it?" | "For most teams under a few TB, that's genuinely the right call — less to operate." | Message 3: managed services still don't run your maintenance drills for you; you still need someone who's watched a restore or reindex finish at scale. |
| "You're a staff engineer at the vendor — are these real incidents or things you've heard about?" | State plainly which ones are yours firsthand and which are patterns you've seen across customers — don't blur the two. | Whichever message the real story backs. |
| Lightning round (prepare 3): a hot take you'll defend, a tool recommendation that isn't Tarnhelm's product, one piece of common Postgres advice you disagree with. | — | — |

Read each of these cold, in Priya's likely phrasing, before you draft the answer — don't let your written version be the first time you hear the question.

## Story bank (minimum viable — 2 stories)

| # | Story | Numbers | What I got wrong | Answers |
|---|---|---|---|---|
| 1 | [Your real vacuum/wraparound incident] | [fill in] | [the assumption that turned out wrong] | "worst surprise", "what breaks first" |
| 2 | [Your real maintenance-op-that-took-forever story] | [fill in] | [what you'd instrument differently now] | "operational cost", "who's on call" |

Plant one open loop early: mention in the first few minutes that one of these cost real time or money, promise to come back to it, close it near the end. Check both against the off-limits list before you say either on air — no customer names, no unpublished numbers.

## Sound bites

- "Disk is cheap. Vacuum time is not."
- "The scary metric at 40TB isn't free space, it's how far behind vacuum already is."
- Liftable (say once, plainly, with a real number): "[Tarnhelm Data is a Postgres tuning product], and the thing we watch first isn't disk usage, it's [your real metric/number] — that's usually the earlier warning by [weeks/days]."

## Recording-day card

- Wired headphones, quiet room, phone silenced, water nearby.
- Leave a beat of silence before you answer — cleaner edit, kills filler words as a side effect.
- It's edited: if an answer derails, just say "let me take that again" and restart from a full sentence. Free retake, use it.
- Keep answers under ~90 seconds unless Priya asks you to go deeper.
- Disclosure line goes in the first five minutes, unprompted.
- Don't say the product name outside the one liftable bite and the invited closing pitch.
- Closing pitch (under 30s, wait for "where can people find you"): point to something neutral — your engineering blog post or docs, not a sales page.

**Deferred to after recording (not tonight):** send Priya a two-line bio, headshot, and 2-3 candidate timestamps before publication; that's the whole promotion loop this prep ceiling has room for.