# Kestrel Hack mentor plan: what to fix before the window opens

I read the skill and both its references. The skill's interview has ten questions and you've answered about two. So this is the fix list the form data forces, not a full plan.

## Next action

Send the 22 mentors a 2-minute follow-up form today. Name, email and job title can't be matched to your four tracks, and that is the main gap. Everything else below depends on the answers.

## 1. Tags: the roster can't route requests yet ❌

The skill says a tag has to use the brief's own words. A tag a participant can't map to the track they entered routes nothing.

- "Senior Backend Engineer, Fintech" hints at fintech. It doesn't say whether they've built with it.
- "Staff SRE" and "ML Platform Lead" map to none of fintech, civic data, accessibility or hardware.
- The skill says to ask depth at sign-up rather than infer it from a job title. A title says what someone is paid for, not what they can unblock at 3am.

**Ask each mentor these questions:**

1. Which tracks can you help with? Allow several, using exactly these words: fintech, civic data, accessibility, hardware, general stack.
2. For each track, have you built with it, or only read the docs? Those are the two depth levels the skill uses. A roster full of "read the docs" looks covered and isn't.
3. Which sponsor technology do you know, by product name? Add this if the brief names any sponsor tech. I haven't seen the brief.
4. Which languages or stacks do you know? Include a free-text line, so Rust, embedded and microcontrollers can surface.
5. Which hours can you commit to? The skill takes the slot at sign-up. Presence beyond the slot is a courtesy and can't be scheduled against.
6. Are you also on the judge list? If yes, you need the contact log (section 5).

Keep the tag list to roughly the four tracks, the sponsor tech and the general stack. A coordinator has to remember it at 3am.

## 2. Embedded Rust: your hunch is untested, but plan for it being true ⚠️

"I don't think anyone does" is an inference from job titles. Question 4 above tests it. Either way, publish the escalation route now. The skill says an improvised route is how a team hears "ask around" as "no".

**Published route for an uncovered skill:**

1. Check the roster's second level first. Someone who has read the docs beats nobody, if they say plainly which level the team is getting. A "Staff SRE" or an ML person who has used Rust may sit here.
2. Ask the sponsor's channel, if the gap is on sponsor tech.
3. Ask the room. Another team's participant may hold the skill. Keep it a request, never an assignment, with no obligation attached.
4. Tell the team plainly that no help exists for this, early enough to change approach. A team told at hour 4 can pivot. A team told at hour 30 can't.

**Do now, before the window:**

- Contact the two Rust teams directly and tell them the likely situation. Waiting until hour 4 burns the pivot window the skill is trying to protect.
- Recruit for the gap. Warm lists answer in days: past participants, a local Rust or embedded user group, a partner company's firmware team, or maintainers of the HAL or toolchain the teams use. The skill's community channel assumes a university with a department behind it, so substitute a user group or past-participant list. Add a free-text "embedded / Rust?" line to the form you're already sending.
- Log it as a coverage gap against the hardware track. It's the most useful thing next edition inherits.

## 3. Hardware track: check whether it's covered at all ⚠️

You've seen 22 titles and I've seen three. If none of the 22 can honestly tag hardware, that track has no coverage, and the Rust teams are probably in it.

- If the brief names a sponsor technology as required for one track, or as the sole substrate, that track needs a guaranteed mentor present for stated hours, not just an available one. The skill removes "no mentor programme" as an option at that depth.
- Decide for each track whether it is unstaffed and published as such, available, or guaranteed. Publish whichever applies. Don't leave it silent.
- Don't size by headcount. The skill refuses mentor-to-participant ratios and any invented staffing formula, so I'm giving none for 22 people. The scarce thing is tagged expertise in the hours a track is worked. Hand that constraint ("this tag, present, these hours") to your volunteer shift plan.

## 4. Four more things missing from what you collected

| Missing | Fix |
|---|---|
| Request mechanic | Pick one and publish it where teams read the brief, before the window opens. Teams that learn it mid-event are a half-served field. |
| Mentor briefing | Needs the help-versus-build boundary: mentors explain, diagnose, unblock and demonstrate, and never write code that ships in a submission. |
| Overnight hours | Decide whether they are staffed, thinly staffed or published as unstaffed, and publish that. |
| Sponsor mentors | If any exist, they are a sponsorship deliverable negotiated in the agreement, with the no-pitching rule written in. A missing one is a fulfilment failure, not a no-show. |

**Request mechanic.** The default is identifiable mentors: a marker and a named role in your channels. At minimum, give every mentor a marker and a chat role. Go further if the event is digital or hybrid, or spans several rooms. Then use a request channel where an organizer routes each request, and put at least two people on the routing. A single organizer's DMs fail when that person sleeps. Office hours are only a supplement for an overnight event.

**Mentor briefing.** Cover logistics, the boundary, the request format, who to escalate to, and the code-of-conduct pointer. Add a rule for admitting what they don't know, and the sponsor no-pitch rule. If any prize has cash value, a briefing with no stated boundary is no longer an option. An unbriefed mentor's commit becomes an eligibility question at the ceremony.

## 5. Mentor-judge conflict

If the form answer to question 6 shows any mentor also judging, keep a contact log during the window of which mentor spent real time with which team. Hand it to whoever runs judging before the judge pool is fixed. The recusal rule itself belongs to the judging process, not the mentor plan.

## Pass check before the window opens

Five items must exist in writing with zero blanks:

1. Expertise tags mapped to your four tracks.
2. A coverage commitment per track.
3. The request mechanic as teams will read it.
4. The mentor briefing, including the boundary sentence.
5. The escalation route for a skill nobody covers.

Today you have none of the five. The follow-up form unlocks items 1 and 2, and the Rust route in section 2 is item 5.

## Questions that change this plan

1. Is the event in person, digital or hybrid, and does the window run overnight?
2. Does the brief name a sponsor technology, and at what depth: bonus, required for one track, or sole substrate?
3. By what date must the roster close and the request mechanic reach participants? A close date favors community and alumni lists over sponsor negotiation.
4. Do any prizes carry cash value?
5. Is any mentor also a judge?

Answer those and I'll write the plan section by section for your validation.