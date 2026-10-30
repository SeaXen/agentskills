# Sourcing channel evidence

Directories change, so re-check filters before relying on them.

Contents:

1. Standing directories, with real filter mechanics
2. The pattern across all three, and what it implies for the channel ranking
3. Proactive contact as the stated CFP backup plan, in the guide's own wording
4. What looks like sourcing infrastructure but is not

## 1. Standing directories, with real filter mechanics

Each entry below is a real, live, browsable directory. None is a general-purpose "any topic, any region" speaker index - each reaches one specific population, which is why a program of any breadth needs several plus a non-directory channel.

### speakerinnen.org - women+ speakers, explicitly organizer-facing

The only one of the three that states organizer sourcing as its purpose, in its own words: the project README gives the goal as to _"provide a way for conference and event organizers to find and contact appropriate women speakers"_. The homepage says it to the organizer directly: **"Organizers, find your speakers"** / "Find women speakers & moderators for your conference."

Mechanics:

- Ten browsable topic categories; the largest are Companies & Start-ups (~2,391 speakers), Science & Technology (~1,379) and Career & Education (~1,369) as of a 2026-09-11 re-check (all three directories in this file re-verified live on that date; treat the counts as an order of magnitude, not an exact current figure - they were ~2,382 / ~1,373 / ~1,361 at the prior check).
- Free-text search on name or topic, on top of category browsing.
- Speakers self-register for free with their expertise, prior conferences, and a contact route - the supply side is speaker-driven, not organizer-curated, so a listing means someone chose to be findable.
- Regional offshoots exist (Vorarlberg, Upper Austria) alongside English and German interfaces - a partial precedent for a localized variant of the same model.
- The directory publishes its own code of conduct, separate from any event's.

Why it matters for the ranking: this is the cleanest answer to the warning that under-represented people in tech are much less likely to respond to an open call. A directory whose members opted in to being found is the right mechanism, and it is also the compliant one - you are searching a population that self-identified, not inferring a protected characteristic about someone who did not.

### Google Developer Experts directory - expertise by specialization

Visit `developers.google.com/community/experts`. More than 1,000 recognized professionals, with a public directory browsable by area of specialization. Speaking at events is named as one of the program's core member activities.

Two caveats that must survive into any recommendation:

- The organizer-sourcing use is **inferred from the directory's structure and its speaking-focused member activity, not stated as the program's purpose**. Say so rather than presenting it as a speaker directory.
- Experts are explicitly independent and not affiliated with Google. That matters for how an invitation is framed: it is a direct approach to an independent practitioner, not a request routed through a vendor.

### CNCF Ambassadors directory - region, language and project together

Visit `cncf.io/people/ambassadors/`. This directory demonstrates strong international-sourcing mechanics, because three filter dimensions are published and usable together:

- **Geographic location** (e.g. China, Brazil, France)
- **Languages spoken** (e.g. Chinese, Portuguese, English)
- **Project expertise** (e.g. Kubernetes, Istio, Helm, OpenTelemetry)

Region plus language in one query is exactly what an international shortlist needs and what a plain search cannot do. Region alone returns people you cannot brief in a shared language; language alone returns your own country again.

Same caveat as the previous entry: the page does not instruct organizers to use the directory for event recruitment. The filtering infrastructure supports the use case; the program does not state it as its purpose.

## 2. The pattern across all three

Every real directory found works the same way: an expert self-registers once and is then discoverable by topic, region or language across many events, instead of being found fresh per event. Two consequences for how the channel is ranked in the skill:

- A standing directory search costs far less per candidate found than community scouting or referral-chasing - this is why it sits at the efficient end of the menu despite returning unvouched names.
- It only reaches whoever opted into that specific directory's population: women+ in tech, one vendor's technology ecosystem, one foundation's projects. A program broader than one of those populations cannot be sourced from directories alone, and a menu offering only directory search would quietly narrow the program to whoever already registered somewhere.

## 3. Proactive contact as the stated CFP backup plan

From the DevOpsDays organizing guide, "Call for Proposals" section:

> "Don't be surprised if proposals don't flow in quickly at first. People usually wait a bit before sending them in and need some extra calls. It's good to have a backup plan and contact individual speakers as well."

That is the _supplement_ trigger specifically: proactive sourcing running alongside a live, on-schedule call, prompted by thin early volume. The guide frames it as expected and ordinary - "don't be surprised" - not as a rescue. Keep it distinct from the _replacement_ trigger, where a sub-floor timeline deletes the open call entirely and the program goes fully invited; that one is a timeline failure, this one is normal practice.

Two more statements from the same guide that bound sourcing decisions:

- Speaker travel: "People will usually need at least 4-6 weeks to arrange for travel or time off." This is the lead-time floor for any invited candidate who has to travel.
- Direct payment to speakers "can bring with it complex issues around taxes, visas, and conflict of interest/employment agreements"; treat that as the binding constraint on speaker money at community technical events, and never invent an honorarium norm or amount to sit beside it.

## 4. What looks like sourcing infrastructure but is not

**speakerline.io** is a speaker-side CFP-transparency tool, not an organizer-facing directory, despite the name. Its stated purpose is to _"demystify the CFP process and help new speakers get started"_ by centralizing proposals and event timelines; its navigation is Speakers / Proposals / Events / Tags. That is a discovery layer for people submitting to calls, not a browsable index of speakers available to invite with a contact route.

**Conference archives and recorded-talk collections** are the opposite case: they are not directories and have no browse-by-availability mechanic, but they are the raw material for the prior-talk review channel. A past program of an adjacent event gives you names, topics, and - where the talk was recorded - the delivery evidence the qualification step needs, in one place.
