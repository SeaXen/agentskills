# Antenna Conf, Edition 3: Culture Brief (draft for your approval)

**Do these first:**
1. Replace the purpose sentence (section 1). The current one fails the skill's test.
2. Fix your culture thresholds before the event, not after (section 7). Sellout speed and return rate don't measure culture.
3. Confirm or correct the assumptions below.

## Assumptions

The skill asks ten questions one at a time. You asked for the full answer, so I assumed the following. Each is a place where I could be wrong.

| # | Assumption | Effect if wrong |
|---|---|---|
| Pole | Community-run, volunteer or CFP-driven, cost-recovery sponsors | If vendor-funded, the hosting and swag defaults flip |
| Register | Hacker, leaning newcomer-welcoming | Changes every attribute |
| Maturity | Established: editions 1 and 2 have run | I have no list of your existing traditions |
| Horizon | Compounding annual asset | A one-off would demote the tradition rungs |
| Effort ceiling | Small volunteer team, a few rehearsal hours | Caps the ritual rung |
| CoC | Exists, probably enforcement-only (unchecked) | Section 6 changes |
| Format | Two days, single track, venue control unknown | Affects the signature tradition |

## 1. Purpose sentence

**Your sentence:** "Antenna Conf brings together wireless developers for two days of talks, workshops, and networking."

**Verdict:** it is a category label. Any wireless conference could say it. Parker's test says that if the sentence could describe a competitor's event, rewrite it.

**Provisional replacement** (a working sentence, not a positioning decision):

> Antenna Conf is where people who make radios work in software stop debugging alone: you leave with a fix for today's problem and someone to call about the next one.

Run it through `event-positioning` before you lock it. Anything in it that your past attendees wouldn't recognize is a guess I made.

Two more candidates, if you want a different emphasis:
- "The conference for the part of the stack where the physics shows through."
- "Two days with the people who've already hit your wall."

**Recommendation:** the first. "Stop debugging alone" is an emotional claim you can filter talks by.

## 2. Register

**Pole:** community/hacker.

**Anti-midpoint lean:**
- Spontaneous over choreographed.
- Newcomer-welcoming over insider.
- Dry over formal.
- Austere over lavish.

Your brief didn't say where you sit on these. Correct me if you lean the other way.

**Attributes**

You gave no past-edition history, so the anti-examples below are borrowed archetypes, not your events. Replace them with real moments from editions 1 and 2.

1. **Bench-honest, but never bragging.**
   - Do:
     - Invite talks about what broke.
     - Show measurements, not claims.
     - Credit the person who found the bug.
   - Don't:
     - Run keynote-as-pitch.
     - Use "best-in-class" language.
     - Treat speakers as "content".
   - Example: a talk titled "Why our link budget was wrong for six months."
   - Anti-example: a sponsored slot that is a product demo with no failure in it.

2. **Deep, but never gatekeeping.**
   - Do:
     - Define the acronym once.
     - Mark talk difficulty.
     - Seat first-timers with regulars.
   - Don't:
     - Use "obviously".
     - Run in-jokes that need two editions to decode.
     - Hold well-actuallys.
   - Example: an MC who says "if SNR is new to you, it means this" without condescension.
   - Anti-example: a Q&A where someone corrects a slide detail to show off.

3. **Hands-on, but never chaotic.**
   - Do:
     - Make workshops run on hardware people can touch.
     - Name a workshop owner.
     - Publish the kit list in advance.
   - Don't:
     - Run workshops that are demos with a laptop audience.
     - Leave a no-show without a fallback.
     - Hand out untested setup instructions.
   - Example: a workshop where everyone gets a signal on screen in 15 minutes.
   - Anti-example: a workshop that loses half an hour to driver installs.

4. **Dry-funny, but never unsafe.**
   - Do:
     - Joke at your own expense.
     - Drop the humor instantly when something goes wrong.
     - Keep it in plain English.
   - Don't:
     - Punch down.
     - Joke about someone's accent, gear budget, or level.
     - Use exclamation-mark whimsy in an incident announcement.
   - Example: a host acknowledging that the projector died with a one-liner, then fixing it.
   - Anti-example: a joke at a first-time speaker's expense.

**Banned-register list**
- "Synergy" and "leverage".
- "Thought leader".
- "Networking" as a noun on signage (see section 3).
- Sponsor press-release voice.
- Logistics as an opening.
- "Obviously", "simply", "just".

**Check:** your current line, "talks, workshops, and networking", sits at the midpoint on every axis. That is why it reads as no register at all.

## 3. Tone-modulation matrix

The register is fixed. Only the expression changes per cell. I filled only the cells where the attributes don't already answer.

| Moment \ Touchpoint | MC/host | Signage & print | Swag | Catering | Volunteer briefing | Email & social |
|---|---|---|---|---|---|---|
| **Opening** | Open cold with a live demo or a failure story. No logistics. | Name the room by its purpose ("Main stage"), not a sponsor. | n/a | n/a | Tell volunteers the opening has no logistics, so they hold questions. | Pre-event mail tells people what to expect, not what to bring. |
| **Session transitions** | Host adds one honest sentence on why the next talk matters, not the speaker's resume. | Difficulty marker on each talk ("newcomer-friendly" / "deep"). | n/a | n/a | n/a | n/a |
| **Breaks & meals** | Name the hallway track as the point of the break. | A conversation prompt on tables, replacing "networking". | n/a | Food labeled by what is in it, with dietary needs visible. | Volunteers eat at the same table and time as speakers. | n/a |
| **Sponsor interactions** | Thank sponsors in the event's voice, one sentence, never their copy. | Tier labels in the event's own voice. | No sponsor logo on the main item. | n/a | Briefing: sponsors don't pitch from the stage. | Sponsor mentions never lead a mail. |
| **Incident / crisis** | Drop the humor entirely. Plain, direct, factual. Name the next concrete step. | Calm, plain wording. | n/a | n/a | Named person owns the incident script. | No exclamation marks, ever. |
| **Closing** | Designed final moment (section 4). Not "thanks, see you next year". | n/a | n/a | n/a | Volunteers thanked on stage by name. | The post-event mail restates what happened and asks the retro questions. |
| **Post-event** | n/a | n/a | n/a | n/a | n/a | Publish a short "what we learned" note, including a CoC summary. |

## 4. Rituals

**Ladder position:** pop-up rules plus a scripted opening and closing form the base rung. Because the event recurs, add one protected signature tradition on top. The throughline rung needs a sharp emotional claim, and the provisional sentence in section 1 may qualify. Test it against your program before committing.

**Pop-up rules** (announced in the opening, 3 of them):
1. No feigning surprise (Recurse Center).
2. No well-actuallys (Recurse Center).
3. Say what you measured. If you don't know, say so. This one is mine, written for an RF audience where hand-waving is the common failure.

**Opening** (no logistics in the first minutes):
- A live demonstration that makes the room's own radio environment visible, for example a receive-only spectrum view of the venue.
- Receive-only is passive. Check local rules and the venue's rules anyway.
- Then state the purpose sentence and the three rules.
- Logistics get their own slot after the first talk.

**Closing:**
- A deliberate final moment.
- Candidate: the host asks the room to name one problem they plan to solve differently Monday.
- Volunteers are thanked by name.
- It ends on the hallway track, not on a sponsor slide.

**Signature tradition: 3 candidates, one recommendation**

First, ask your regulars whether they already invented something. Naming and protecting an attendee-coined ritual is the cheapest option (the PyCon hallway-track mechanic). If nothing exists:

| Candidate | Mechanic imported (the why) | Cost |
|---|---|---|
| **Postmortems hour:** lightning talks only about failures | Attendees see that depth and honesty are the norm | Low |
| **The air in the room:** a persistent, visible receive-only spectrum wall | Makes the topic physical, like a locally-flavored unique moment | Medium (hardware and a volunteer) |
| **Bring-a-dead-radio table:** people bring broken kit for the room to diagnose | Turns "stop debugging alone" into an act | Low |

**Recommendation:** the postmortems hour, unless attendees already coined something. It fits attribute 1, costs the least, and matches your purpose sentence.

**Do not copy** a mariachi band, a ball pit, or an exclamation-mark brand. Import the reason, then derive a local form.

## 5. Hosting and swag

**Hosting: single organizer-host** (efficiency default, community pole).
- Use one primary host per day.
- Name a backup who owns the incident script.
- Skip the professional MC. A generic host contradicts a hacker register.
- If your identity says "everyone's conference", move to distributed hosting.

**One-page host brief** (mandatory):
1. Purpose sentence.
2. Register attributes with never-clauses, plus the banned list.
3. The three pop-up rules and the words to announce them in.
4. The opening beat sheet. No logistics.
5. The closing ritual and who owns it.
6. Pronunciation list: speakers, RF terms, sponsors.
7. **Incident script**, written in advance. Drop the humor, go plain, name the next step.
8. One rehearsal, minimum.

**Swag: less-but-better.**
- One useful, well-made item that matches the register. Candidate: something people use at a bench.
- If the budget doesn't support that, run none-plus-donation and announce where the money went.
- Sizing is asked at registration, never guessed, and goes beyond S-M-L-XL.
- If sustainability is a stated value, drop disposable swag entirely.

## 6. CoC alignment

I haven't seen your CoC. Check for these, which are the culture layer. They are yours to place in the room:
- The social-rules layer (the pop-up rules above).
- Pronoun norms.
- Photo and consent culture.
- Quiet-room framing.

If the CoC is enforcement-only under a "welcoming" claim, that contradicts the register where attendees read most carefully. Policy text, reporting channels, and enforcement belong to `event-code-of-conduct`. Hand that skill the register from section 2.

## 7. Measurement: where I disagree with your plan

**Your plan:** wait for post-event feedback, then decide what good looks like. Success metrics are ticket-sale speed and attendee return rate.

**Two problems.**

1. **Thresholds set after the data are not thresholds.** You'll rationalize whatever you see. The skill's rule is that every threshold is self-set and fixed before the event.
2. **Those two metrics don't measure culture.**
   - Sellout speed and return rate are real, but they belong to `event-market-fit`. They read on the whole event.
   - Both are confounded by price, lineup, dates, marketing, and competing events.
   - If return rate rises, you can't tell whether the culture worked or the lineup did.

Keep both as event health metrics. Don't credit or blame the culture work for them.

**Culture metrics to fix now.** The numbers below are my proposals. Change them if you like, then freeze them before you open the survey.

| Metric | What it is | Proposed target (confirm before the event) |
|---|---|---|
| **Worked/not-worked retro** | Capture within a week, reopen when planning edition 4. Add the probe: "What do you remember, and what was the point?" | Held within 7 days. Probe answered by the team. |
| **Identity echo** | Share of free-text feedback and public posts that use the register's own words (honest, hands-on, "stop debugging alone") rather than generic praise ("great talks, nice venue") | Set a baseline from the edition 2 feedback, then target baseline plus 15 points. |
| **Tradition pull** | Unprompted mentions of the signature tradition, plus returning attendees who name it as a return reason | ≥10% of free-text responses mention it. Under 5% for two editions running means replace it, not protect it. |
| **Return-reason question** | Ask returning attendees why they came back, in free text | Turns the return rate into a culture signal. |
| **CoC transparency report** | Publish what was reported and how it was resolved (!!Con West model) | Published within 30 days. |

**Spectacle check:** if attendees remember the party or the demo but not the purpose, cut spectacle and reinvest in content and connection.

## 8. Consistency audit

I can't audit your actual touchpoints, since I haven't seen your site, MC footage, or signage. Run the check below against each matrix column. Every contradiction is either fixed or written down as a deliberate exception.

- **Venue:** a civic or unusual venue, or at least not a convention-center feel?
- **Pricing and labor:** moderate pricing and volunteer-run, or a sold-stage-time economy?
- **Format:** single track with a real hallway track?
- **Commercial norms:** no sold keynotes, no sales pitches?
- **Hosting:** distributed or organizer-hosted, not a hired generic MC?
- **The inconsistency row:** a "community" opening that is a sponsor-logo reel, a party that outspends the program, or volunteers eating standing while speakers get a green room.

**Deliberate exceptions to state, if you keep them:**
- A sponsored workshop slot.
- A hired AV crew.

## Approval needed

The skill requires explicit approval per section before finalizing. Please give a verdict on each:

1. Purpose sentence.
2. Register and the four attributes.
3. The matrix.
4. Rituals, and the signature tradition.
5. Hosting and swag.
6. Measurement targets. These must be frozen before the event.

If you approve, I'd record the register, matrix, protected traditions, and retro outcomes in a memory file for edition 4. I'll do that only on your go.