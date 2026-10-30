# Published-call evidence

Quoted guidance behind the skill's timeline, criteria, benefits, anonymization, and measurement. Sources: the DevOpsDays organizing guide, PyCon US's live CFP and program pages, swyx's "CFP Advice", the Write the Docs organizer guide, the `jlengstorf/awesome-speaker-diversity` community list, and PyCon 2010's own CFP-distribution target wiki page.

## Timeline (DevOpsDays organizing guide, verbatim)

- "open your CFP as soon as possible, and close it at least 6-8 weeks before your event."
- "you'll want your call to be open for at least a month, and you'll want at least 2 weeks to consider proposals and fill in any gaps."
- The reason is the speaker's side of the table: "People will usually need at least 4-6 weeks to arrange for travel or time off."
- The guide's master timeline:
  - CFP launch at **T-7.5 months** before the event.
  - "initiate voting of submissions with the organizers" at **T-4.5 months**.
  - Program launch at **T-3.5 months**.
  - A roughly three-month review-to-launch runway, as the guide's own default, well above the 6-8 week floor.

## The six published criteria (DevOpsDays organizing guide, verbatim)

Criteria the call itself should communicate - a de facto published review rubric:

1. "no speaker spots can be bought by sponsors: not ever - period."
2. "encourage new content: if the content has already been presented/published online we will consider it but it's less attractive."
3. "a good balance between local and out-of-town speakers."
4. "favor new speakers: devopsdays is a supportive environment to encourage new voices in our space."
5. "encourage bold subjects: we don't want to hear the same things over and over."
6. "shy away from specific technology/product talks: always try to elevate it to the conceptual part... for specific tools talk, there are open spaces not the main conference talks." The call routes vendor/tool pitches to open space rather than rejecting them outright, which presumes the structure chose an open-space block.

## Speaker benefits

- The floor: "at minimum, all speakers should receive a free event ticket" (DevOpsDays).
- Travel reimbursement is "a good use of funds if available," with the caveat that direct payment "can bring with it complex issues around taxes, visas, and conflict of interest/employment agreements" (DevOpsDays).
- PyCon US travel-grant language worth reusing:
  - Purpose framing: "speaker grants to ensure that if assistance is needed and your proposal is accepted, you can speak at PyCon US" - enabling attendance, not rewarding talk quality.
  - Cap: "one speaker travel grant per accepted proposal."
  - Self-selection ask: "if you can attend PyCon US without financial assistance, please refrain from requesting a travel grant."
- Honorarium: no published norm exists, but individual named events do publish a figure, and the two disagree by more than 2x:
  - !!Con's own CFP page states: "Preparing an amazing conference talk is hard work. To show our appreciation, we're paying all our speakers a $256 (USD) honorarium." The same sentence and amount appears unchanged in !!Con's 2018, 2019, 2020, and 2021 CFP pages through its final 2024 edition - a stable per-event policy, not a one-off.
  - ffconf's CFP page states: "£500 honorarium - we know it's not much for the work you've put in, but it's a _thank you_" - on top of paid travel, a hotel, and meals for every speaker, with no distinction between speakers.
  - SeaGL took a third shape: an honorarium restricted to Black and Indigenous People of Color speakers, framed as an equity measure rather than a universal perk, with the amount deliberately left undetermined ("We have not yet determined an exact dollar amount") at the time of announcement.
  - Treat these as three real but disagreeing data points, not a market rate: two flat per-speaker amounts an order of magnitude apart in different currencies, and one targeted, amount-unspecified policy. Any figure a user adopts is still self-set against their own budget.

## Anonymization - both sides of the evidence

- Per swyx: "blind CFP review is important for some level of equity... In my experience, most CFP's are NOT blind." Named review is the field's de facto norm.
- PyCon US (implemented at scale): "During initial review, proposal author information is not displayed to reviewers." The stated practical consequence: speakers must keep identifying details out of titles, descriptions, and outlines themselves - the platform hides the author field, not the free text.
- The blind phase is "initial review": identity enters later for program-level decisions, which is why mandatory blind is a two-phase process, not a switch.
- Tooling posture: anonymization ships as an optional mode on the commercial platforms surveyed - opt-in is the tooling default, mandatory blind is an organizer policy layered on top.

## First-time-speaker mechanisms

- Stated intent (DevOpsDays): criterion 4 above - "favor new speakers."
- Worked examples (PyCon US): the CFP page points first-timers at prior years' proposals as calibration for what a strong submission looks like.
- Structured program (PyCon US): **Proposal Mentorship** - a pre-submission pairing sign-up run separately-timed alongside the CFP, with its own deadline. This is a documented example of the mechanism.

## Outreach and notification notes (DevOpsDays)

- "under-represented people in tech are much less likely to respond to your CFP" - if diversity is a goal, reach actively into those communities; the open call alone under-delivers.
- Schedule announcement practice: selection need not be 100% finished before announcing ("it's ok to leave some space until the end"), but a finished schedule helps attendees justify attending - and announcing only a handful of speakers risks "unwarranted assumptions about your demographics."

## Promotion channel practice

- Sequencing (Write the Docs organizer guide, Communications page): write the announcement, post it to the blog, send a tweet linking to the post, then wait one to two hours before the mass email - "We write up the emails to send and post them on our blog. Generally, it's best to send a tweet with the blog post, and then wait for an hour or two to send the email." The delay lets the community catch errors before the wider list sees them.
- Targeted equity outreach, two concrete examples of the DevOpsDays warning above put into practice:
  - `jlengstorf/awesome-speaker-diversity` (maintained GitHub list): names roughly twenty community groups (Women Who Code, Black Girls Code, Girls Who Code, Techqueria, Lesbians Who Tech, Code2040, and others) with a template email organizers send directly to each group's own list inviting CFP submissions.
  - PyCon 2010's own CFP-distribution target wiki page: a real, categorized precedent for the same move at conference scale - local user groups, computer-science departments, women-in-tech organizations, and organizations serving other underrepresented groups, naming specific targets (e.g. Spelman College, listed explicitly for reaching Black women in tech).
- No conference organizer or CFP platform (Papercall.io, Sessionize) has published a channel-by-channel breakdown of where submissions actually came from. The sequencing pattern and the two outreach lists above are the concrete floor found, not a measured ranking.

## Oversubscription benchmarks

- PyCon US 2025 (official blog): "this year's final count totalling 938 proposals... Our volunteer Program Committee has worked hard to select only 15% of the many strong proposals" - roughly **6.5:1** submissions to slots, framed by the organizers as abundance, not failure.
- Per swyx: "A rule of thumb is 8-12 speakers per day, per track... So a 3 day single track conference has a max of 36 talks." "The applicant pool for a conference ranges from an average 200 to something like 800-1200 for a JSConf." - 8-30x oversubscription is normal at a popular single-track conference.
- DjangoCon Europe 2024: 174 proposals from 138 submitters, 51 first-time speakers - submitter diversity as a health signal alongside raw volume.
- On a first CFP: even 2-3:1 oversubscription is a strong go signal. Undersubscription - not filling slots with quality talks - is the stop signal that indicates the topic lacks a speaker base yet.

## Organizer incentives

Per swyx, organizers optimize a program to "sell tickets, have a great content mix, and sell next year's tickets, in roughly that order." Implied selection factors: speaker name recognition, deliberate avoidance of topic clustering, audience fit, and a talk's video/marketing-asset value. Use this as the honesty check on published criteria - publish what will actually be applied.
