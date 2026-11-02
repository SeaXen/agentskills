# PulseConf format check: hold the two-track announcement

**Verdict: don't announce the split yet.** The numbers you gave don't support it, and they don't show a broken CFP either.

This is a pre-interview read from the numbers you gave. I assumed a community conference: open CFP, volunteer-run, sponsors never buy stage slots. If PulseConf is vendor-run, say so, because the defaults change.

## 1. The numbers

| Fact | Value | Benchmark |
|---|---|---|
| Oversubscription | 105 ÷ 22 = **4.8x** | The only published trigger for adding a track is **~8-10x** (swyx: 200 to 1,200 applicants at JSConf tier). |
| Where it sits | Below the line | At ~8-10x, that means ~176-220 submissions for 22 slots. |
| Is a high ratio a symptom? | No | swyx treats 8-30x at a popular single-track event as normal, not a broken CFP. The 8-10x figure is where the conversation opens. It is not evidence of a failure. |

- ✅ **Your CFP is not broken.** 4.8x is mild. Strange Loop says it turns down "hundreds of excellent talks" a year on purpose, as editorial responsibility.
- ❌ **"Rejecting great talks is wasteful" isn't the same as "the CFP is broken."** Rejection is what curation produces.
- ⚠️ **The split would weaken the program.** Accepting 44 of 105 is a 42% acceptance rate. You would be lowering the bar to fill the slots.
- ⚠️ **The pool divides by topic.** If it splits roughly 50/50, each track sees ~52 submissions for 22 slots. A TypeScript conference probably has an uneven frontend/backend ratio, and a thin side would fill with weaker talks.

## 2. Why frontend/backend is the wrong split

1. **It divides your shared context.** TypeScript is what the 300 people have in common. Five independent single-track events (Strange Loop, GOTO, Monktoberfest, Deconstruct, SmashingConf) chose one stage for shared context, curation, and hallway conversation.
2. **Two rooms for 300 people.** That averages ~150 per room before any session skews. Expect half-empty rooms and attendees choosing between two talks they want.
3. **It misses the skill's second promotion condition.** That condition is two audiences with the same problem at different depths, such as decision-makers versus practitioners. Frontend versus backend is a topic split, not a depth split.
4. **Content policy needs a rewrite.** A "conceptual talks on stage, tool talks elsewhere" rule only works with one curated track. A second track needs its own balance policy.
5. **Cost and effort go up.** You need a second room, AV, volunteers, and a second curation load. Multi-track is the highest-effort option and the lowest on efficiency.
6. **Multi-track is a scale decision.** Treating it as a quality upgrade is a listed failure mode.

## 3. What fixes the real problem

The real problem is that good talks get rejected and people lose speaking opportunities. These options address that without a second track.

**Candidate A: single track plus Ignite block and open-space afternoon (recommended)**
- Curated ~25-30 minute talks in the morning, the DevOpsDays architecture. Keep the 22 slots as they are.
- Add an Ignite block (5 minutes, 20 slides, auto-advancing). It brings in first-time and non-headline speakers cheaply. Collect the slides in advance and run the block from one laptop.
- Open space in the afternoon. Steer tool-specific and framework-specific talks there, so the main stage stays conceptual.
- Invite strong rejected submitters to Ignite or open space. This answers the "wasteful" feeling directly.

**Candidate B: A, plus a separately ticketed workshop day (if depth is in demand)**
- This is the bracketing model SmashingConf, PyCon, and GOTO use.
- It adds hands-on depth without diluting the curated track, and it brings in revenue.
- Ratios vary by event, so don't quote an industry average.
- Track sell-through against a threshold you fix in advance, for example 60% of capacity.

**Candidate C: your plan, two tracks**
- Only if the revisit triggers in section 5 fire.
- It must keep shared plenary moments: opening keynote, shared lunch, closing.

## 4. Checks before deciding

1. **What was the ratio in editions 1 and 2?** Is 4.8x rising or flat? One year doesn't make a trend.
2. **How many of the 83 rejected talks are genuinely at or above the accepted bar?** Count them after scoring, not by feel. If fewer than ~15-20 are equal to the accepted set, a second track has nothing to fill it.
3. **Did the 105 include sales pitches, duplicates, or off-topic submissions?** That shrinks the real pool.
4. **Did the third edition sell out, and how fast?** The skill reads attendee demand from numbers like this. A second track also needs the audience to fill it.
5. **How many days do the 22 slots fill?** swyx's rule of thumb is 8-12 talks per day per track. Is 22 a one-day or a two-day program?
6. **What effort and budget ceiling do the organizers have?** A second track is the highest-effort option.
7. **Why accept twice as many?** Is the goal more speakers, more attendees, or less guilt over rejections? Each goal points to a different fix.

## 5. Triggers that would revise this

- **Add a track when** the ratio stays above ~8-10x (about 176+ submissions for 22 slots) across at least two editions, and the scored pool holds enough strong talks to fill the second track at the same bar.
- **Add a workshop day when** attendees ask for hands-on depth, and you set the sell-through threshold in advance.
- **Revisit this memo** after the next CFP.

## 6. Before you announce

- Don't announce a split. It sets speaker and sponsor expectations you may have to walk back.
- Announce only what you've validated, for example "Ignite block and open space added".
- Improve the rejection experience. Give short feedback and a clear path to Ignite or open space, using `event-cfp-design` and `event-talk-selection`.
- If a second track is approved later, use `event-schedule-design` for the grid and `event-positioning` for what the change says about PulseConf.
- Keep the community guardrail whatever you choose: no sponsor buys a program slot.

## Open questions before this is final

The skill expects one question at a time and explicit approval before finalizing, so treat the above as a recommendation. Answers to checks 1, 2, and 4 would change it most. Tell me those three and I'll firm it up.