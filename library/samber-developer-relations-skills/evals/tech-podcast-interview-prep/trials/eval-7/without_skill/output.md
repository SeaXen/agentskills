# Production Story Bank — 60-min audio podcast

Two flags before the scripts — resolve both before you record:

- **Thornbury Logistics** — confirm they've cleared being named publicly (case-study/reference sign-off). If not confirmed yet, use "our biggest customer — about 4,000 seats" instead of the name.
- **3.2x benchmark** — it's unpublished. Frame it as your own internal testing, not an established fact. Don't lead with the competitor's name.

## Question map

| Host asks | Use |
|---|---|
| "Worst thing that's happened to you in production?" | Story 3 |
| "Biggest customer / proudest result?" | Story 1 |
| "How do you compare to [competitor] / why switch?" | Story 2 — only if asked, don't volunteer it |
| "What keeps you up at night?" | Story 3, reframed toward the gap it exposed |

## Audio-only rules

- Numbers get said once, then repeated once — a listener can't glance back at a screen. ("Six hours. Down to forty minutes.")
- Give each story one concrete image a listener can picture: a job running overnight while people wait, a dashboard gone quiet over a weekend.
- Land every story on a single clean sentence — that's the line that gets clipped and transcribed.
- Speak each story in 60–90 seconds, then stop and let the host follow up. Don't try to front-load every detail — nuance lives in the follow-up, not the opener.

---

## Story 1 — Thornbury Logistics (the win)

**Triggers:** biggest customer, proof it works at scale, favorite success story

> Our biggest customer — about 4,000 seats — used to run a batch job every night that took six hours. Someone would kick it off before they left and just hope it finished before the morning shift needed the numbers. Six hours is a long time to hope. After they migrated to us, that same job finishes in forty minutes. And the real change wasn't the speed — it's that forty minutes is short enough to run on demand, mid-shift, instead of something you plan your evening around.

**Pull quote:** "Six hours is a long time to hope."

**Have ready:** what was actually the bottleneck (parallelism? indexing? architecture?), how long migration took, what the fallback plan was if it had gone wrong.

---

## Story 2 — the 3.2x benchmark (use only if asked)

**Triggers:** how do you compare, why would someone switch, what's your edge

> We ran our own internal benchmark against our main competitor a while back — same workload, same hardware, as apples-to-apples as we could make it. We came out 3.2 times faster. We haven't published the full methodology yet, so treat that as "here's what we're seeing internally," not a marketing claim we're standing behind publicly yet — we'd rather publish the numbers open before leaning on them hard. But it lines up with what we hear anecdotally from people who've run both.

**If pressed on the competitor's name:** "I'd rather point at the number than the name until we've shown our work — wouldn't be fair otherwise."

**If pressed for the data:** "Not public yet. Happy to send you the write-up once it's out, for the show notes."

---

## Story 3 — the staging cluster (the guaranteed question)

Memorize the opener verbatim — this is the one question you know is coming, so don't improvise the hook under nerves.

**Opener:** "Oh, I've got one — still makes me wince a little."

> This was staging, not production — thankfully — but it was close enough to prod that it scared us the same amount. [Fill in: what actually started the runaway consumption — e.g. a misconfigured retention job, a backfill that didn't have a ceiling] started eating through event data over a weekend, and by Monday it had chewed through about two terabytes. Nobody caught it Friday because [fill in: no weekend alerting on that pipeline / alert threshold set too loose]. We found it Monday morning when [fill in: dashboards looked wrong / a sync stopped]. Recovery took [fill in: timeframe]. The real lesson wasn't the two terabytes — it was that we had zero visibility into that system over a weekend, on infrastructure we fully trusted. So we fixed the visibility gap, not just the one job: [fill in: the actual monitoring/process change]. It's the reason we don't ship anything that touches data retention on a Friday anymore.

**Non-negotiable structure:** never end this story on the disaster. The last sentence has to be the concrete thing that's different today — that's what keeps "worst production incident" from reading as a red flag instead of a credibility signal.

**Follow-ups to have one-liners ready for:**
- "Did it hit any customers?" — have the true answer memorized, don't reconstruct it live.
- "How'd you find out?"
- "What's different today because of it?"
- If the host jokes "should I trust your production system" — bridge: "Fair question — that's exactly why staging exists, so this happens there instead of in front of a customer. It did its job."

---

## Before you record

1. Confirm Thornbury Logistics clearance for public naming.
2. Fill in the four `[fill in]` gaps in Story 3 with the real specifics — a false detail here is the hardest kind of PR mistake to walk back once a podcast is live and transcribed.
3. Rehearse the Story 3 opener out loud twice — that's the one line you don't want to fumble.