# Q2 DevRel Plan — Halberd Labs (Apr 6 – Jul 5, 13 weeks)

## The shape of the quarter

Everything hangs off two fixed points: **v4 ships week 3**, and **the board decides headcount in week 10**. Read together, those aren't two separate events — the 7 weeks between them are your one shot to turn "we shipped a major release" into "we shipped it, here's the proof it mattered, and here's what we couldn't get to because there are three of us." Build the quarter to serve that narrative. The conference submissions are a wildcard that resolves mid-quarter (week 6) and shouldn't be allowed to distort the first six weeks of planning — you don't know yet if you're going, and travel budget is a second, independent maybe on top of that.

Three phases:

- **Weeks 1–3 — Launch.** Everything points at v4.
- **Weeks 4–9 — Prove it.** Turn launch into evidence: adoption, content performance, community signal. This is the headcount case, built in real time, not written retroactively in week 9.
- **Weeks 10–13 — Reset.** Board decision lands, conference decision has been sitting for a month and needs resolving, plan H2.

## Week-by-week

### Phase 1: Launch (weeks 1–3, Apr 6 – Apr 26)

**Week 1 (Apr 6)**
- You: draft launch blog post + migration guide + breaking-changes doc for the new scheduler. Get Priya's first technical review pass on the scheduler claims now, not week 3 — a rewrite this size will get picked apart on HN/Reddit, and factual errors in the launch post are the single most avoidable credibility hit this quarter.
- Advocate: brief community channels (Discord/Slack/forum) on what's coming, line up 2–3 friendly users already on the v4 beta for launch-day quotes/testimonials.
- Start a running **"cut list"** — anything you decline or defer this quarter because there's no capacity. You'll need it in week 9.

**Week 2 (Apr 13)**
- You: finalize launch post, docs, changelog. Second Priya review on final benchmark numbers specifically — that's where launch claims get challenged first.
- Advocate: seed the beta testimonials, prep launch-day social/community posts, set up a feedback-triage channel for launch day.
- Confirm launch-day roles: who's on call for HN/Reddit/Discord, who's writing follow-up responses, who Priya escalates hard technical questions to.

**Week 3 (Apr 20) — v4 ships**
- All hands on launch day: blog live, changelog, docs, social, community post (Show HN or equivalent), direct email to users.
- Priya on standby for technical Q&A — the new scheduler is exactly the kind of claim that draws "did you actually benchmark this" scrutiny.
- Advocate owns real-time community response; you own written follow-ups (clarifications, corrections, a "known issues" doc if bugs surface — rewrites this size rarely land perfectly clean, plan for a stabilization post rather than assuming otherwise).

### Phase 2: Prove it (weeks 4–9, Apr 27 – Jun 7)

**Weeks 4–5 (Apr 27 – May 10)**
- Amplify, don't idle: migration case study from a real user, a scheduler-internals deep dive (co-credited with Priya — this is the piece that rebuilds any credibility dinged during launch scrutiny, and it's a natural conference-talk draft too, see below).
- Patch whatever launch exposed: docs gaps, a troubleshooting doc for the most common migration snag.
- **Week 6 (May 11): conference decision lands.** Don't wait for it to plan content — the scheduler deep-dive you're already writing is 80% of a DataCon/StreamSummit talk outline regardless of the answer, so the effort isn't wasted either way.

**Weeks 6–7 (May 11 – May 24)**
- On conference acceptance: draft talk outline immediately, but **do not let it consume writer or advocate bandwidth allocated to the board-case content** below — this is where a 3-person team overcommits. If both submissions land, that's a real capacity conflict; decide now which one you'd actually staff, don't assume you can do both.
- **Push finance for a real answer on travel budget by week 7, not the week before a flight.** "Maybe" all quarter is a stalling pattern, not a decision — a conference acceptance is the forcing function to convert it. Build the contingency now: if a talk is accepted and budget is denied, you record/stream it or send whoever's regionally closest — either way, the underlying content (the deep-dive) already exists and ships as a blog post regardless of who's in the room.

**Weeks 8–9 (May 25 – Jun 7): build the board case**
- This is the deliberate work, not a byproduct. Pull together: v4 adoption numbers (upgrade %, not just downloads), content performance (launch post + deep-dive traffic/engagement), community growth delta pre/post-launch, support ticket volume and whether docs deflected repeat questions, and the conference outcome as external validation if it landed.
- Close out the cut list from week 1 with specifics: what got dropped, delayed, or shipped thinner than it should have been because there were three of you during a launch quarter. This is the actual headcount argument — not "we're busy," but "here is precisely what a launch of this size cost us elsewhere."
- Draft the board narrative by end of week 9: what shipped, what it proved, what a second hire would have unlocked instead of displaced.

### Phase 3: Reset (weeks 10–13, Jun 8 – Jul 5)

**Week 10 (Jun 8): board review.** Present the case built in weeks 8–9. Whatever the outcome, don't let it stall — you'll know same week whether H2 planning assumes 3 or 4 people.

**Weeks 11–13 (Jun 15 – Jul 5)**
- Resolve whichever conference thread is still open by now — a talk shouldn't be drifting unstaffed this late. If travel is confirmed, this is prep time; if not, convert the talk material fully into published content so it isn't sunk effort.
- Light content cadence — this is intentionally the comedown after a launch-plus-board quarter, not a second sprint. Use it to clear anything shelved on the cut list that's now worth revisiting, and to scope Q3.

## The two swing factors, explicitly

- **Travel budget ("maybe"):** treat as denied by default when planning content, so nothing depends on it. Treat conference prep as content-first, travel-optional — the deep-dive/talk material pays off whether or not anyone boards a plane. Force a real yes/no out of finance the moment a talk is accepted (week 6–7), not later.
- **Board headcount decision (week 10):** the entire weeks 4–9 stretch should be read as instrumented, not just executed. Track adoption, engagement, and the cut list from week 1 onward — reconstructing this from memory in week 9 will produce a weaker case than logging it as it happens.

## What this plan deliberately doesn't do

It doesn't assume both conference talks get staffed, doesn't assume travel gets approved, and doesn't let conference prep compete with the board-case work in weeks 8–9. With three people and a major launch already fixed in week 3, the biggest risk isn't running out of ideas — it's spreading the same two writers across launch, two possible conferences, and a board deck at the same time. Sequence beats parallelism here.