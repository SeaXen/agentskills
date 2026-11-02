# APIcon Amsterdam attendee Slack: wind-down plan

**Scale and assumptions:** one Slack workspace, 900 members, one-off edition, nobody on duty since the closing keynote. I didn't interview you, so these are my assumptions:
- No register exists (the `event-cultural-identity` answer is empty), so the notice wording below is provisional.
- Nobody can be on duty after the closing date.
- The member list was collected under whatever basis the registration form gave, and I haven't seen it.

All rankings come from the skill's own constructions, not measured benchmarks.

## Decision

**Do not delete tonight, and do not keep it open as is. Export the workspace, announce a deletion date on the Slack itself, then delete on that date.** Both board members get part of what they want:
- The "delete" camp is right about the destination. A one-off's member list has no next edition to spend it on.
- The "community space" camp is right that people shouldn't be surprised. A hand-off needs a named owner and a next edition, and you have neither.

## Why not each option

| Option | Verdict | Reason |
|---|---|---|
| Delete tonight, quietly | ❌ | A silent wind-down is the skill's "delete, do not demote" case. It destroys trust in future announcements on any APIcon channel. 900 people also lose it with no chance to save their own links or contacts. Deletion is irreversible, and it should come after the counsel review, not before. |
| Keep open as a community | ❌ | Hand-off needs two things together: a compounding series, and a named person committed to running the space. This is a one-off, and the team is dissolving. Handing off to a space nobody owns is leave-open with extra steps. |
| Leave open as is | ❌ | The skill treats it as a conditional delete when nobody is on duty after the closing date. The code-of-conduct duty is still live in a space carrying the event's name, with nobody to answer a report. |
| Read-only archive | Interim only | Cheap and reversible, so use it as the holding state while counsel answers. It is not the end state, because the member list stays in the workspace. |
| **Export, then scheduled deletion** | ✅ | This is the default for a one-off. It is the only irreversible rung and the only one that forces the retention question first. |

**One exception.** If a board member wants the community to continue, they can be the named person. They must commit in writing before the freeze date to run a separate space they own, with their own rules and moderators. Then do the hand-off the skill's way:
- Invite people, don't migrate them. Moving them is a new purpose applied to old consent.
- Hand over open questions, not just members.
- Still wind down the APIcon workspace.

## The GDPR retention question

I won't give you a number, and this is deliberate. The skill I'm following says to name no jurisdiction, quote no retention period, and take the question to your own counsel, because the answer depends on:
- jurisdiction
- platform terms
- the year
- the lawful basis you actually used

I don't know your basis, and a figure from me could be wrong. Take this list to a Dutch data-protection lawyer, or to the DPO if the sponsoring entity has one:
1. What lawful basis covered collecting the member list, and does it cover keeping it after the edition ends?
2. How long may the list be kept, and what has to happen at the end of that period?
3. Does moving people to a different space require asking them again?
4. What do Slack's terms say about exporting a member list, and about the data if the workspace is deleted or the account lapses?
5. Who holds the moderation duty for a space still carrying the event's name after the event, and for how long?
6. Does anything change if attendees included minors?

Decide the retention window and its reason before you export anything.

## Wind-down plan

**Channel:** the attendee Slack.
- **Job:** attendee conversation for the edition. This is now closed.
- **Owner:** one named board member, for the wind-down only.
- **End state:** exported, then deleted.

All dates are self-set. Adjust them to when counsel can answer.

| Date | Step |
|---|---|
| **Tue 2026-10-13** | Name the interim owner. Read the channels for unhandled reports and act on any. Confirm the code-of-conduct reporting path reaches a real person, and check it with the `event-code-of-conduct` sibling. Post the notice below. |
| **By Fri 2026-10-16** | Freeze posting. Set the workspace to organizer-post-only or read-only, and remove bots and webhooks that would keep writing. |
| **By Fri 2026-10-23** | Counsel answers the list above. Fix the retention window. |
| **By Fri 2026-10-30** | Take the export. Include only what the event needs: decisions taken, unanswered questions, post-event content links. Include the member list only if counsel confirms a basis to keep it. Store it under the same basis as the original and record who can reach it. |
| **Mon 2026-11-09** | Delete the workspace, including invites, integrations and any mirror. A second person confirms the deletion actually happened. |

Before the freeze, check the free-tier history limit. A plan that hides older messages has already deleted the archive you think you have.

Publish the deletion date on the Slack and in the closing note on the mailing list. The list's copy and consent belong to `event-attendee-email-sequences`.

**Notice to post on the Slack (provisional wording, no register applied):**

> APIcon Amsterdam was a one-off, and this workspace is closing. Posting is frozen from 16 October. The workspace will be deleted on 9 November. Save anything you want to keep before then. Talks and slides: [link]. Questions or conduct reports: [named contact and address]. Thank you for being part of it.

## Check against the skill's own gates

- **Code of conduct:** it binds this workspace until the day it is deleted. Don't let the notice go up without a named responder behind the contact line.
- **Wind-down completion** is the one binary gate. It passes only when the workspace has a closed state and the date was met.

## For the debrief

The skill says to decide the wind-down before the event. That didn't happen, so leave-open happened by accident for five weeks. Send that, and the lack of a post-event owner, to `event-debrief`.

The skill also expects a record of the roster, the wind-down decision and its date. I haven't written that, because I treated your request as a deliverable only.