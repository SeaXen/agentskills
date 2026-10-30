# Session format catalog

The building blocks the session-mix menu in SKILL.md composes. Each entry: what it is, what it costs the organizer, when it earns its slot, and its known failure modes - drawn from the format owners' own documentation.

## Curated talk (~25-30 minutes)

The program backbone. DevOpsDays' guide states ~30 minutes is a deliberately chosen balance point for content, not a scheduling default.

Costs a full CFP-or-invitation cycle per slot; produces the event's durable recorded assets. Community-event guardrail (CNCF, DevOpsDays, NorthSec): ban sales pitches from the curated track explicitly, in writing.

## News recap block

A segment opening a recurring meetup with field news since the last edition.

- **Why it earns a slot:** in a fast-moving field, many attendees value it highly, and some come for it alone.
- **Trade-off:** those who came only for it leave right after, and others find it too long. A long recap taxes everyone who came for the main session.
- **Cost:** real preparation every edition: collecting, filtering and ranking the news. It is not free filler.
- **Rules:** cap it (set the cap yourself; the report's 30 minutes drew "too long" complaints), name one owner per edition, and place it so leavers do not walk out across a speaker. Track departures after it as a session-mix signal.

## Ignite talk (5 minutes, 20 slides, auto-advancing)

A named format from igniteshow.com, adopted as-is by DevOpsDays. Slides advance on a fixed timer - the presenter cannot control pacing; the mechanic, not organizer discipline, is what enforces the length.

That is the transferable lesson for any short format: build the constraint into the mechanics. One rule: no straight sales pitch - socially enforced, not policed.

Why it earns a slot: a lower-commitment, higher-volume speaking format that gets first-time and non-headline voices on stage in a way a full-talk-only program cannot.

Sourced operational failure modes:

- presenters submit slides late or misunderstand auto-advance - collect slides in advance (PDF travels best) and remind presenters same-day that they cannot advance slides and have no notes
- run the whole block from one dedicated laptop, never presenters' own machines

A filler variant exists (Ignite Karaoke: 1 minute, 4 absurd slides at 15 seconds) for padding a light schedule with levity.

## Open space (Open Space Technology)

Self-organized sessions with no pre-set agenda, documented by DevOpsDays citing Harrison Owen. The design contract an organizer accepts when choosing it: the Law of Two Feet (anyone neither contributing nor learning moves elsewhere) and its four principles:

- whoever comes is the right people
- whatever happens is the only thing that could have
- whenever it starts is the right time
- when it's over, it's over

Four-phase ceremony:

1. Opening - show the day's timeline; 1-2 minute topic intros maximum, longer drains energy.
2. Marketplace of ideas - topics on stickies claim timeslots on an agenda wall.
3. Breakout sessions - facilitators handle logistics, never content; capture outcomes on a shared wiki or paper forms.
4. Closing circle - a talking stick, one brief feeling each.

Expect bumblebees (flit between sessions, cross-pollinating) and butterflies (stay put; their quiet conversations are often the most significant).

### Small-group mechanics

Figures are that report's, not a published standard.

- **Cap each discussion group at about 10.** One round of speaking above 10 people takes an hour. A group of 13 was reported unworkable: split it.
- **One convener per group** - naturally the person who proposed the topic. They want to discuss it and need not be an expert. Their job is balancing speaking time, not answering.
- **Rotate after about 20 minutes**, so people meet more than one group.
- **Capture by voice note per group**, then a short plenary synthesis. Cheaper than paper forms at a meetup, and the convener owns it.
- **Quiet attendees benefit most.** People who spoke in a small group interacted more with others for the rest of the evening.

Treat open space as a distinct structural option, not a lesser fixed-agenda track: it trades program control for self-selected relevance. DevOpsDays also uses it as the pressure valve for its content-mix rule - tool- and vendor-specific depth goes here, keeping the curated track conceptual.

## Lean Coffee (single-table unconference)

From leancoffee.org, the creators' own site (Jim Benson and Jeremy Lightsmith, Seattle 2009). Designed for zero organizational overhead: a three-column personal kanban (to discuss / discussing / discussed), everyone writes topics, 1-2 sentence pitches, two dot-votes each, highest-voted topics first. Its power is a topic list the whole table is already motivated to discuss.

Versus full Open Space: no opening/marketplace/closing ceremony, no real facilitator role, vote-based prioritization instead of self-selection-by-attendance. Fits a single-room, single-timeslot slice - a breakfast session, a track filler - where Open Space's multi-room, half-day ceremony would be oversized.

## Keynote, fireside chat, panel

Decision guidance:

- **Keynote** - a single sequenced argument by a strong speaker who controls the narrative. Best when you have that speaker.
- **Fireside chat / moderated interview** - extracts value from a high-profile guest who is not a polished presenter; multiple sources note it "has replaced solo keynotes at many conferences" and makes it "easier to get a 'yes' from business leaders" (Slido, BigSpeak). Known trap, flagged even by proponents: sliding into celebrity-interview mode where the interviewer merely feeds a monologue - prepared, willing-to-challenge questions are the fix.
- **Panel** - the most-criticized format in the sourced record, by name:
  - Fred Wilson's flat "no panels rule"
  - Brad Feld: "panels are awful and should be eliminated from planet earth… consider eliminating the panels altogether"
  - Scott Berkun ("Why Panel Sessions Suck"): the moderator is passive, speakers state the obvious, and organizer-moderators "are afraid to challenge the panelists since the panelists are their guests"
  - Duncan Green (LSE): "coma-inducing panels" and "people (usually men) asking 'questions' that are really comments"

  Structural critique across sources: four panelists × 5-minute introductions burns 20 minutes before any substance.

A panel is worth running only with a strong, prepared, willing-to-interrupt moderator and pre-briefed provocative questions - and it is the hardest format for a first-time organizer to execute, which is why the staged ladder cuts it entirely from a first event.

## Workshop day (bracketing model)

Not an in-program session type but a program-structure move: one or two optional, separately ticketed hands-on days before or after the talk days (SmashingConf, PyCon US tutorials, GOTO masterclasses, DevOpsDays pre-event day). Adds depth without diluting the curated track, and the separate ticket makes it a budget lever. Never express workshop share as an industry-average percentage; none is published.

## Hackathon judging/demo formats

| Format      | Mechanics                                          | Scales to many teams? | Winner narrative        |
| ----------- | -------------------------------------------------- | --------------------- | ----------------------- |
| Expo table  | Judges rotate through team tables, 3-5 min each    | Yes (parallel)        | Weak - no shared moment |
| Stage pitch | Teams pitch a panel, 2-5 min + Q&A                 | No (serial)           | Strong                  |
| Video only  | Async judging from submitted video + write-up      | Best                  | Weakest                 |
| Two-stage   | Expo round narrows to finalists who pitch on stage | Moderate              | Strongest               |

Judge composition shapes the fit:

- technical judges want to touch a live demo (expo)
- business judges want a deliberate narrative (stage)
- domain experts and sponsor reps work in any format, but need explicit rubric prompts to surface their priority in a time-boxed slot

The scoring rubric and weights belong to `samber/dev-event-organizer-skills@hackathon-judging` - this catalog only covers which demo structure to run.

## Recurring meetup variants

The variants SKILL.md lists under the recurring-meetup rung. Figures are absent on purpose: set your own.

### No-prerequisite discussion café

- **What it is:** a monthly open roundtable. No talks, no expert framing. Pitch: "come with your questions and worries; people who know a bit will talk with you."
- **Why:** meetups drift toward insiders, and a talk program assumes a baseline. The café is the on-ramp before deeper sessions.
- **Cost:** a room and someone to host the table; no speakers.
- **Failure modes:** experts take over and it becomes a talk; regulars treat it as their club. Brief the host to redirect to newcomers' questions.
- **Mechanics:** reuse the small-group mechanics under § Open space once the table passes about 10.

### Host-company breakfast

- **What it is:** a weekday morning, roughly 8:00 to 10:30, at a host company that pays the room and coffee. Zero organizer cost. Hosts rotate among large local actors.
- **Program shapes seen:** a news review then a round-table; an expert panel (see § Keynote, fireside chat, panel for the moderator condition); a beginner-friendly session.
- **Side effect:** business introductions between attendees and hosts - a draw for managers and business roles, a cost for a purely technical crowd.
- **Failure modes:** the host's calendar decides the dates, and the host's brand dominates the room. Fix: rotate hosts, keep program control, write down what the host gets.
- **Slot effect:** a morning slot reaches people an evening excludes; see `samber/dev-event-organizer-skills@event-date-selection` § Time of day.

### Bar-hosted after-work

- **What it is:** an evening in a bar, with a sponsor paying drinks.
- **Strength:** lowest setup cost, social by default.
- **Failure modes:** noise kills any talk; the sponsor's role drifts into the program. Keep content to a short intro at most.

### Rotating format

- **What it is:** a series that cycles formats (dinner, lunch, after-work, talk, open session) and never reuses the same weekday and hour twice in a row.
- **Why:** a fixed slot excludes the same people every time. One series reported stable attendance over years this way.
- **Cost:** each edition needs its own announcement; regulars cannot rely on habit.

### Cross-community joint evening

- **What it is:** many local meetup groups (one report: around twenty) each run a stand or session in one venue on one night.
- **Cost:** light coordination - one coordinator, a coworking host - but a real energy cost spread across every participating group.
- **Why:** cross-pollination between communities that rarely meet. Occasional, never the cadence. Partner mechanics belong to `samber/dev-event-organizer-skills@cross-event-promotion`.

### Street-level outreach

- **What it is:** vox-pop video capsules, a stand at a seasonal market.
- **Why:** general-public acculturation on the topic, reaching people who would never open a meetup page.
- **Counting:** report it as outreach, never as meetup attendance.
