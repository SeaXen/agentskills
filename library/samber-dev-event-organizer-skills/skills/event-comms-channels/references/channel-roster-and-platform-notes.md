# Channel roster and platform notes

Contents: the published roster · what does not transfer to a conference · the digital-space code-of-conduct rule · platform-category notes · the sponsor-channel question.

## The published roster

Major League Hacking's organizer guide publishes a named-organizer channel roster for a technical event, assigning a **job per channel** rather than listing platforms - exactly the discipline Menu 1 asks for. It is written for a student hackathon, not a conference.

The guide's minimum channel list, with its own stated purposes (verbatim):

| Channel          | Stated job                                                                                                     |
| ---------------- | -------------------------------------------------------------------------------------------------------------- |
| Team-Formation   | "Channel for hackers to form teams"                                                                            |
| Carpool-Search   | "Channel for hackers to find a ride from other hackers"                                                        |
| Ask-Organizers   | "Channel for hackers to ask organizers any questions that come up throughout the event."                       |
| Introductions    | "Channel for hackers to introduce themselves. Have your team set the norm for this by introducing yourselves." |
| Random           | "Channel for anything that isn't hackathon related."                                                           |
| Ask-Mentors      | "Channel for hackers to connect with mentors when they need help on their projects."                           |
| Mentors-Internal | "Channel for mentors to talk with each other and with organizers."                                             |
| Admin            | "Channel for your organizing team. We recommend creating an admin voice channel as well!"                      |

Two structural facts to carry forward:

1. **Ask-Organizers and Admin are different channels.** The space attendees use to reach organizers is public and organizers merely monitor it. The space organizers coordinate in is separate.
   - The Admin half is out of scope here - it belongs to `samber/dev-event-organizer-skills@event-run-of-show`, which states the same split from its side.
2. **The guide names a sponsor channel split.** Its example event runs two sponsor channels "so that sponsors have a dedicated space to talk about their api's or workshops" (stated in the guide). Read this as evidence that sponsor traffic is a distinct message class competing for attendee attention, not as a recommendation to run exactly two.

## What does not transfer

The roster is hackathon-shaped. Do not port it to a conference unchanged:

- **Team-Formation and Carpool-Search have no conference analogue.** They exist because a hackathon's attendees have to organize _each other_ before the event's real work starts. A conference attendee arrives with nothing to form.
- **Ask-Mentors and Mentors-Internal presuppose a mentor population.** A conference's equivalent population is speakers, whose comms are owned by `samber/dev-event-organizer-skills@event-speaker-experience`, not by this roster.
- **The roster assumes a multi-day, overnight event where attendees live inside the channel.** A one-day conference's attendees open a channel occasionally at most, and no published figure says how often. A roster sized for the first case goes silent in the second, which is Menu 1's "channel with no stated job" failure mode arriving by import.
- **It is a digital/hybrid-era document.** The guide recommends its platform partly for free voice chat, which is a remote-participation feature. An in-person conference buys much less from it.

What does transfer:

- The discipline of one job per channel.
- The separation of the ask-us channel from the coordinate-among-ourselves channel.
- The idea that a minimum roster is worth stating rather than growing organically.

## The digital-space code-of-conduct rule

From the MLH guide (verbatim): "Before joining and once on the platform, make hackers know that their behavior and actions are still subject to MLH Code of Conduct, and to be respectful. _Digital spaces can increase harassment as people are hidden behind a computer, so it is key to make sure your attendees know you still take this seriously._"

Two obligations follow for any channel this skill opens, and they hold for the whole time the channel is open - including after the event, which is why Menu 4 carries a compliance-cost axis:

- The code of conduct is stated **at the join point**, not only on the website. A person joining a chat space has not necessarily read the event's site.
- Somebody is **on duty** to act on a report from that space. The reporting path itself is `samber/dev-event-organizer-skills@event-code-of-conduct`'s to design. Confirm that path covers every channel opened, and never open one it does not cover.

## Platform-category notes

Named products appear here only where quoting the source requires it. Choose by category, never by the name a guide happened to use.

- **Persistent chat.** The source names two ("Slack and Discord are two of the most popular") and prefers one of them "because of their free voice chat capabilities" (verbatim).
  - The transferable criteria behind that preference:
    - Whether voice is included at no cost.
    - Whether joining requires an account the audience already has.
    - Whether the free tier retains history (a tier that hides older messages quietly deletes your archive rung).
    - Whether the platform's terms let you export a member list before you delete it.
- **Announcement lists.** Tool choice, sending and consent belong to `samber/dev-event-organizer-skills@event-attendee-email-sequences` in full. The only criterion this skill cares about is delivery latency: a list is an hours-scale channel and must never carry a minutes-scale message.
- **Event apps.** A category, not a product. Evaluate on who is forced to install it, whether the schedule updates without an app-store release, and whether it works with no connectivity in the room.
  - No adoption figure exists for community-run technical events. Do not accept a vendor's.
- **Status pages.** Any page with a stable URL, editable in under a minute from a phone, that survives the outage it is reporting. That last property is the whole point and rules out a page hosted on the same infrastructure as the thing that broke.
- **Broadcast-only channels.** Some chat platforms offer a post-only mode. Where it exists it implements Menu 2's two-channel split at no extra channel cost - worth checking for before creating a second space.

## The staffing failure

An in-person workshop runs late and virtual participants are not notified of the schedule change; check-in communication to remote attendees lags because the team is busy checking in people in person (MLH's hybrid-event failure list, paraphrased from its own bullets). It is the strongest evidence that channel _staffing_, not channel _existence_, is what reaches people.

What does not transfer: MLH declines to work with hybrid events at all, so read this as a cost list, not as a ban.

## Channel directory contents

Workflow step 6 hands this content to `event-marketing-plan`'s comms-hub page rather than publishing a second directory. Per channel, it lists:

- Its name.
- Its one-line job.
- Who answers on it.
- The hours it is watched.
- What it is _not_ for, with a pointer to the channel that is - the line most directories omit.

A directory that only says what each channel is for still routes the awkward messages to whichever channel the attendee saw first.
