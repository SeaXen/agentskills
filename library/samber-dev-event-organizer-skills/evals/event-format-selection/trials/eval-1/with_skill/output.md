# ElixirNorth: format brief (proposal, needs your approval)

**Recommendation: run a single-day, single-track conference with an open-space afternoon. Do not run two days of talks in year one.**

I assume a community-run event: open CFP, volunteers, sponsors only recover costs, and no sponsor ever buys a stage slot. If ElixirNorth is vendor-backed, tell me, because the defaults change.

The brief follows the `event-format-selection` skill. I couldn't interview you live, so unanswered questions appear as assumptions, with their cost in the last section.

## 1. Your 500-member rule doesn't hold up, but your meetup numbers still justify a conference

- **No published threshold exists.** Organizers who graduated used very different headcounts. DartUP jumped at 250+. GopherCon debuted at 700. North Bay Python ran a credible first single-day event on a $40,000 budget, planned in under 6 months.
- **The real gates are content depth, speaker supply, and willingness to carry venue risk.**
- **Your Slack count doesn't help.** 900 members is not a measured audience.
- **Your meetup attendance does.** 130-140 at every monthly session for three years meets the published graduation trigger (a meetup consistently at 100-150+).
- **Speaker supply and risk tolerance are still unproven.** The CFP will test supply. Venue deposits and contracts will test risk tolerance.

So the answer to "should we launch a conference" is yes, for a different reason than the rule of thumb. The open question is how big a first edition should be.

## 2. Three candidate structures

| | A. One day, single track + open-space afternoon | B. Workshop day + talk day | C. Two days of talks (your current plan) |
|---|---|---|---|
| Shape | One curated morning, ignite block, open space | Optional separately ticketed hands-on day, then A | Single track, 16-24 curated slots |
| Effort | Lowest of the three | A plus a workshop program | Highest |
| CFP load | About 5-8 curated slots | Same as A | 16-24 slots, all curated by people who have never run a CFP |
| Main risk | Feels small if attendees travel | Workshop instructors, rooms, and setup add a second program | Thin or uneven talks, and the largest venue deposit |

**Why A wins for your situation.**

- Four people with day jobs and no CFP experience have the tightest effort ceiling.
- Two days of talks is the "starved" option: highest value, lowest efficiency. The published case for it is travel justification (Strange Loop: "1-day conferences are not worth the travel time"). That argument fits events that draw travellers. Your evidence is a local meetup.
- B is the safe next step because the workshop day can be added later without touching the curated track. It is also a revenue lever.
- C stays available once the CFP shows you have the speaker supply.

## 3. Track count: one track, with a content-mix rule

- **One track, no second curated track.** A second track needs a CFP oversubscribed roughly 8-10x beyond slots. You have never run a CFP, so you have no such evidence. Below that ratio you get empty rooms and a fragmented event.
- **Content-mix rule (DevOpsDays model).** Curated talks stay conceptual or cultural, for example OTP design, how teams run Elixir in production, and lessons learned. Library- or tool-specific talks go to open space. A single track makes this enforceable.

## 4. Session mix and day architecture

Order is a sketch. `event-schedule-design` builds the real grid.

1. **Opening, ~15 minutes.** Organizer intro.
2. **Morning curated talks, ~25-30 minutes each.** This is the backbone and your recorded asset. DevOpsDays runs about four per day, and swyx's ceiling is 8-12 speakers per day per track. Plan roughly 5-8 with the afternoon given over to open space, and adjust to the quality of submissions.
3. **Long lunch and breaks.** Treat the hallway track as a design goal.
4. **Ignite block after lunch, 5 minutes per talk.** The auto-advancing 20-slide format is the lowest-cost way to put first-time speakers on stage. Collect slides in advance and run them all from one laptop.
5. **Open space all afternoon, scheduled live.** It needs near-zero curation and gives tool-specific content a home. Keep opening-circle topic intros to 1-2 minutes.
6. **Closing.**

**What to cut for edition one:**

- **Panels.** They are the most-criticized format and the hardest to execute. Reconsider only with a strong moderator who is willing to interrupt and has pre-briefed questions.
- **A keynote built around a famous guest.** If you invite a headliner who isn't a polished presenter, do a fireside chat.
- **Sold slots.** Sponsors get expo space, side events, and short 1-minute inter-talk slots, never stage time. Funding structure belongs to `event-budget`.

## 5. Delivery: in-person, record and post

- **In-person is the default.** Record the talks and post them afterwards.
- **Skip interactive hybrid.** It needs roughly double the AV and logistics budget. CHI 2022 lost $484,886 on a fully hybrid format. These are academic-conference figures, the closest published record, not tech-conference data.
- **Your Q8 evidence is missing.** "People asked for a stream" doesn't count. Hybrid needs remote registrations reliably above ~25-30% of paid attendance, covering their marginal cost.

## 6. What would change each choice next edition

Write these down now so next year doesn't re-argue the defaults.

| Choice | Revise when |
|---|---|
| One day | CFP has the speaker supply for more slots and attendees travel, so add a day. Sell a bracketing workshop day first. |
| Single track | Applicant-to-slot ratio reaches ~8-10x. Read that as the point where the conversation opens, not proof the CFP is broken. |
| Workshop day | It sells below a threshold you fix in advance (self-set example: 60% of capacity), so cut it next edition. |
| Record-and-post | Remote registrations reliably exceed ~25-30% of paid attendance and cover their cost. |
| Panels | A prepared, willing-to-interrupt moderator exists. |
| Session mix (self-set) | Pick 2-3 signals and the revision each triggers: open-space wall filling, ignite application volume, walkouts. |

## 7. Questions that would change this

Answer in any order. Each shows what it would change.

1. **How many unique attendees came over the past year, versus the 130-140 repeat count?** A smaller unique base weakens the evidence for a ticketed event.
2. **How many credible Elixir speakers can you name for a curated day?** This decides between A and C. If it is thin, lean on ignite and open space.
3. **Is the date fixed, or free?** A fixed date favors invited content over a long CFP cycle.
4. **Is this a one-off bet or an annual asset?** An annual asset favors the slower, trust-building choices: open CFP, no sold keynotes.
5. **What can your four organizers actually give, in hours per week and in deposit risk?** A budget ceiling could rule out C.
6. **Do you already have a free or sponsored venue, AV skill, or a recording setup?** Any of these can overturn a default.
7. **Do you have a workshop instructor pool?** This decides whether B is realistic.

## Next steps

1. Approve or reject A, then tell me which sections to rework. The skill treats this as a strategy deliverable, so nothing is final until you approve.
2. Answer questions 1-3 above first. They carry the most weight.
3. Once approved, hand off to:
   - `event-first-edition`, to size and launch edition one
   - `event-cfp-design` and `event-talk-selection`, for your first CFP
   - `event-venue-sourcing` and `event-budget`
   - `event-schedule-design`, for the grid
   - `event-positioning`, since a single-track curated day signals a different identity than a multi-track expo

I didn't write anything to memory. The triggers in section 6 are the part worth keeping, so decide where they should live.