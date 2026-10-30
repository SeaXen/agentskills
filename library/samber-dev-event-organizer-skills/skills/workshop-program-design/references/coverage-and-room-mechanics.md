# Facilitator coverage and in-room mechanics

Contents: the four coverage rungs written out · the in-room mechanics · after the workshop · the mentor-model contrast · three decisions the menu leaves to you · a negative example.

## The four coverage rungs

- **Solo instructor.** One person presents and answers. Costs nothing to arrange. In a room doing an exercise, someone is stuck while the instructor is mid-sentence, and nothing in this rung addresses it - which is why the skill deletes it outright once the session is genuinely hands-on rather than demonstrative.

- **Roaming troubleshooter.** One additional person who knows the material, moving through the room. The published guidance is explicit: _"You might want to have a backup speaker walking around to help troubleshoot for those who start falling behind and ask them to share their screen to troubleshoot their issues."_ Three things are worth reading carefully in that sentence.

  - **"backup speaker"** - the guide's own word. Somebody who could deliver the session, not a logistics volunteer. Recruiting that person is the whole cost of this rung, and it is why the effort axis puts it above peer pairing.
  - **"those who start falling behind"** - the trigger is observed, not requested. The roaming person's job is to spot the participant who has not raised a hand, which is a different job from answering a queue.
  - **"share their screen"** - that phrasing assumes a remote or hybrid room. In a physical room the equivalent is looking over a shoulder, and the consent question that raises belongs to whatever code of conduct the event runs.

  The Carpentries run the scaled version of this rung and publish its size: _"We recommend 1 helper for every 8-10 students, not counting the two Instructors."_ Their instructor training rounds it to _"at least a 1:10 helper-to-learner ratio for in-person workshops (not counting instructors) and more if teaching online"_. Three conditions travel with the figure:

  - **Two instructors first.** The ratio counts helpers on top of a teaching pair, not the person presenting.
  - **Helpers who know the tools.** A helper who cannot debug the install counts toward headcount, not coverage.
  - **Its home domain.** Two-day research-computing workshops for scientists, taught by volunteers. A developer-conference workshop is shorter, and its cohort is more uneven. Cite it as a starting point, then adjust.

  The sticky-note flag (see In-room mechanics) is what turns "those who start falling behind" from a guess into something a roaming helper can see from across the room.

- **Stationed helpers per work area.** A helper posted at each place the exercise physically happens - a shape rather than a count. In a hardware context where the stations are literal, the guide's tool-station table repeats _"ensure a mentor is stationed nearby"_ for two of its four stations, and says to _"Ensure these stations are staffed by experienced volunteers."_

  It also carries a supervision requirement beyond a service question: _"Have makerspace staff or trained volunteers supervise these zones. Display and share all safety protocols ahead of time."_ Where an exercise involves hot tools or machinery, supervision is a condition of running it at all, not a coverage rung - route that to the event's own risk and venue work rather than deciding it on an efficiency ratio.

  Software workshops rarely have literal stations. The transferable test is whether the exercise has physically or logically distinct steps that people arrive at in different order - a build step, a deploy step, a debug step - because a helper who owns one step answers the same question repeatedly and gets fast at it.

- **Structured peer pairing.** Pair participants at the start and ask them to solve for each other first, leaving the instructor and any helper only what a pair cannot solve. It earns its place on the growth axis by definition: pairing capacity grows with attendance. CS-classroom pair-programming pedagogy gives that definition a mechanism. The UK National Centre for Computing Education's pair-programming teaching guidance (Raspberry Pi Foundation) assigns a driver, who controls the keyboard, and a navigator, who "watches with a keen eye for any errors being made" and swaps into the driver's seat every five to ten minutes. That puts a second set of eyes on every screen for the whole session, rather than a helper reached only after a hand goes up. "Structured" is the load-bearing word in the rung's name: the same guidance calls plain, role-free pairing the version that "can often lead to one, or both, learners quickly losing focus" - this rung's own unmanaged failure under a different name.

  Its failure mode is real regardless: two stuck people is a stable state that produces no signal. The fix the same guidance gives is to "check in regularly with pairs" - fold that into the roaming rung's sweep when you run both together, and treat a pair that has gone quiet as the thing the roamer is watching for.

  The learning-outcome evidence behind pair programming is mixed, not settled. Know that before leaning on this rung as proof the technique works rather than as a structure that plausibly helps. Classroom studies report gains in confidence and code quality, with the largest effect on less-experienced or lower-confidence learners. Against that, a small preprint study of 36 introductory Java students at one university found pairing experience had no significant effect on the quiz score used to measure learning, while the students' own self-efficacy did. Every source behind this rung is K-12 or university CS-classroom pedagogy, not a technical-conference workshop. Treat it as a plausible, structurally argued fit, not a workshop-specific measurement.

## In-room mechanics

From MLH's workshop-hosting guidance in the order the session runs, then two Carpentries mechanics:

- **Plan the recovery time, do not hope for it.** _"You should also build time into your schedule to do breakout sessions, troubleshooting, and questions."_ Troubleshooting appears in the schedule beside content, which is the practical difference between a workshop plan and a talk plan.
- **Size the opening to the room.** _"For workshops with fewer attendees, we recommend starting with an icebreaker to ensure everyone knows each other."_ The condition is stated - a small room - without a number that makes a room small. The example it gives is name, institution, and something recently learned.
- **Ask for participation explicitly.** _"You should prompt your attendees for active participation."_
- **Lower the cost of admitting you are stuck.** _"As you’re working through the workshop content, be extremely aware of how intimidating code reviews and questions will be for participants."_ The named fix is normalisation: _"Remind participants that if they’re facing an issue others probably are as well."_ This is the cheapest mechanic in the whole reference and it costs one sentence at the front of the session.
- **Give the room a silent help flag.** The Carpentries hand each learner sticky notes in two colours, which _"act as 'flags' that may be placed on a laptop screen to indicate when a learner needs help or when they have completed a task and are ready to move on"_. The stated reasons: _"it is more discreet (which means they are more likely to actually do it), they can keep working while their flag is raised, and the instructor can quickly see from the front of the room what state the class is in."_ They advise colours other than red and green. Online, a video tool's reaction icons stand in.
- **Collect minute cards.** The same programme asks for one good and one bad point on the two notes at lunch and at the end of each day - feedback the instructor can act on before the next block, not after the event.

## After the workshop

- Close it deliberately rather than trailing off: sign off and thank participants when the material is finished.
- Keep the instructor available: the guidance is to keep talking to attendees afterwards rather than leaving with their laptop.
- Give the topic somewhere to live: _"Have a channel in slack/Discord so hackers can ask follow-up questions about the workshop topic after it ends."_
- Publish how long the material and any environment stay reachable. The published workshop pages do exactly this, in their own prerequisite blocks, with windows measured in hours and in weeks - see the environment sheet for those two figures and the pages they come from.

## The mentor-model contrast

A hackathon's mentoring model looks adjacent and is not the same shape. Its help is pull-based across a whole multi-day window: a request channel, an identifiable role, a walk-up area, office hours. A workshop's help is push-based inside a fixed block: the person who is behind late in the block will not ask, and the whole coverage menu exists to reach them before the session ends.

Two consequences:

- Do not size workshop coverage from a mentoring roster, and do not let workshop coverage be the same people if their mentoring shift overlaps the session.
- The pull-based mechanics still transfer for the _after_ window, which is exactly what the follow-up channel above is.

## Three decisions the menu leaves to you

- **The adjustment to the helper ratio.** The Carpentries convention gives a starting count. The exercise's structure moves it: how many distinct steps it has, how often each one fails, and how many people in the room can debug each of them.
- **The participant ceiling for a hands-on session.** Set it from the room, the furniture and the exercise; the capacity reference works it through.
- **What a helper may do to a participant's machine.** The Carpentries' rule is the default: _"when receiving assistance, learners should be doing the typing whenever possible."_ Brief helpers on it explicitly, because without a rule a helper takes the keyboard. `samber/dev-event-organizer-skills@hackathon-mentoring` answers the same question for a participant's repository. Take its keyboard boundary, never its staffing figure: "about every four non-expert participants" sizes experts and projects for a multi-day build, not helpers in a fixed block.

## Negative example: the right ratio, the wrong helpers

Invented and illustrative.

> _"It's a 40-person workshop. The Carpentries say one helper per ten, so four volunteers from the registration desk will cover it."_

The ratio is real; everything around it is dropped. The convention counts helpers on top of two instructors, and this plan names no second instructor. It assumes helpers who know the tools, and four registration volunteers who cannot debug a failed install supply headcount, not coverage. It also ignores whether the exercise has distinct steps a helper could own.

The honest version states the convention, the context and the adjustment:

> _"Two instructors plus three helpers who have run the exercise themselves. Three helpers at the Carpentries' eight to ten each cover 24-30 learners, so coverage binds. We take the low end, 24, because most of this room has never used a container, and put the rest on a waitlist for a second section. If the build step separates from the deploy step, we post a helper at each and revisit."_
