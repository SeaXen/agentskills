# Platform selection and vendor questions

Contents: what each platform category actually buys · the one published channel roster and what does not transfer · the questions to put in writing before committing · data, consent and residency · the reversibility test.

Named products appear here only where a source named them. Choose by category, never by the name a guide happened to use: the categories outlive the products.

## What each category actually buys

Read this beside Menu 1 in SKILL.md, not instead of it. The ranking lives there; this file says only what sits behind each rung.

- **Public video platform, one-way.** A stream to a platform the audience already has an account on, or needs none. What you buy is delivery: distribution somebody else operates, a player that works on a phone on a weak connection, and no login between the viewer and the talk. What you do not buy is any relationship between viewers. One real risk: incidental background music in a stream can get the stream taken down by the platform itself, mid-session, per the DevOpsDays organizing guide.
- **Persistent chat space.** A space that exists before and after the sessions. Slack and Discord are the most popular options, per Major League Hacking's organizer guide. Evaluate a candidate space on four things:
  - whether voice is included at no cost
  - whether joining needs an account the audience already has
  - whether the free tier retains history
  - whether you can export a member list before you close it
- **Broadcast tool with a built-in question queue.** One product carrying the video and a structured question list with a moderator view - upvotes, a queue, a "answered" state. What it buys is question discipline; what it costs is that the viewer is now behind a login and a bespoke player. In Menu 1 this rung is strictly dominated and kept only for the case where procurement already bought it.
- **Managed virtual-venue platform.** A single login covering a multi-track schedule, breakout rooms, a sponsor expo, and usually an attendee directory. It buys the things a room buys - moving between sessions, bumping into people, a booth - and it is the only rung that does. It costs procurement lead time, a contract, and a data-handling review, because the directory and the booth exist to move attendee data to third parties.
- **Assembled stack.** Streaming software plus a chat platform plus a schedule page, joined by you. Cheap to start, reversible until the day, and its whole cost is organizer hours plus every seam between components:
  - a schedule that has to be updated in several places
  - a login the audience has to hold twice
  - a question that arrives somewhere the speaker is not looking

  A real network-layer cost for any self-run encoder: FOSDEM's video team publishes a requirement of 10 Mbit/s outgoing bandwidth per streamed room, with a 2 Mbit/s floor it describes as sacrificing resilience rather than as a safe minimum. That figure sizes a venue room's uplink, camera plus slides, not a speaker's home connection. Budget the uplink per stream origin, not per event, and budget above the floor.

## The one published channel roster, and what does not transfer

Major League Hacking publishes an organizer channel roster for a technical event, written for a student hackathon. Its transferable discipline is one stated job per channel, and a hard separation between the space attendees use to reach organizers and the space organizers coordinate in.

What does not transfer to a virtual conference:

- It assumes a multi-day event whose attendees live inside the channel for a weekend. A one-day conference's audience opens a channel occasionally at most. Never assume how often.
- Its team-formation and ride-sharing channels exist because a hackathon's attendees must organize each other before the work starts. A conference attendee arrives with nothing to form.
- The same guide's warning about under-estimating a digital event's work is a hackathon organizer's warning about a hackathon's stack. Read it as a caution about the hours, not as a verdict on any component.

The channel roster itself belongs to `samber/dev-event-organizer-skills@event-comms-channels`. Never rebuild it here. Consume it.

## Questions to put in writing before committing

Ask these of the vendor, of procurement, or of whoever already signed. Get the answers in writing, the same way a venue's bandwidth guarantee goes into a contract rather than a conversation. None of them has a right answer you can guess.

**Delivery**

1. What happens to a viewer on a poor connection: does the player degrade quality, or does it stall? Is there an audio-only fallback?
2. Can a viewer watch without creating an account? If not, what does the account require, and can it be created on the day?
3. What is the concurrent-viewer ceiling on the plan being bought, and what happens at the ceiling - a queue, a refusal, or an upgrade invoice?
4. Can the stream be restarted mid-session without the audience losing their place, or does a restart change the address?

A real scale to calibrate question 3 against: FOSDEM 2021 ran its per-talk interactive video rooms on infrastructure provisioned for about 100 concurrent rooms, and had 46 in use at one point on the first day, across a devroom-heavy schedule with dozens of parallel tracks. A single-track event comes nowhere near that ceiling. A multi-track technical conference can approach it.

**Sessions and speakers**

5. Can a speaker share a screen, a second screen, and system audio? Which of those needs a desktop application rather than a browser?
6. What does a speaker need installed, and does that requirement differ by operating system?
7. Can a session be recorded on the platform, and who owns and can delete that recording afterwards?

**Interaction**

8. Can a moderator delete a message, remove a person, and lock a space - during a live session, without leaving it?
9. Does the question surface have a moderator view separate from what attendees see?
10. Is there a broadcast-only mode? Where it exists, it splits announcement from conversation at no extra channel cost.

**Accessibility**

11. What captioning does the platform provide, in which languages, and can an external captioner be fed into it? Report the answer to `samber/dev-event-organizer-skills@event-accessibility-inclusion`; the bar is theirs to set, not yours.
12. Does the player support keyboard navigation and screen readers?

**Data, consent and residency**

13. Where is attendee data stored, and under which jurisdiction's law?
14. What is exported to a sponsor when an attendee enters a booth or a directory, and does the attendee see that at the moment it happens?
15. How long is chat and question history retained, and can it be deleted on request?
16. Does any part of the platform record attendees on camera - a breakout, a networking room, a Q&A - and is that recording separable from a talk's recording?

Question 16 carries the least obvious exposure. A talk's consent record, held by `samber/dev-event-organizer-skills@event-speaker-experience`, covers a speaker presenting. It does not cover an attendee whose face appeared in a breakout room, and that consent cannot be collected after the fact.

Data-protection duty, platform terms and retention obligations sit outside this skill: the answers differ by country, by platform and by year. Name no jurisdiction and quote no retention period. Take questions 13-16 to the organizer's own counsel.

## The reversibility test

Before signing anything, answer one question: what is the last date this choice can still be reversed, and what does reversing it cost? That date, not the event date, is the deadline the platform menu is ranked against.

- An assembled stack and a public feed can be abandoned the week before at the cost of an announcement.
- A managed platform typically cannot, and its contract is usually signed long before anyone knows how many people registered.
- A platform forced by procurement or a sponsor contract was never reversible; that is a deleted rung, not a demoted one, and the decision energy belongs elsewhere.
