Before the document: the real risk here isn't the CoC's wording, it's that a rule with a known unstated exception has a way of surfacing publicly — someone screenshots a "your design is embarrassing" comment next to the CoC and asks why the CTO is exempt. I've written this so you don't need an exception: it draws the line at *work vs. person*, not at tone. Blunt, harsh criticism of a design stays allowed; it only becomes a violation if it's aimed at the person. That means Dario can keep calling architectures "embarrassing" without anyone needing to look away — as long as it stays about the architecture. Worth a read before you post it, since it does commit you to enforcing that line consistently if a comment ever does cross from the work to the person.

---

```markdown
# Loomwright Community Code of Conduct

This Code of Conduct applies to the Loomwright Discord server, including all
text channels, voice channels, threads, DMs sent in the context of server
business, and any Loomwright-run events. It applies to every member,
contributor, moderator, and team member, without exception for role, tenure,
or seniority.

## Why we have this

We're a community of people building and running load tests, often on
systems where getting it wrong is expensive. Technical disagreement is
normal here, and #architecture in particular runs hot — that's fine. This
document exists to draw one line clearly: criticize the work as hard as you
want, never the person.

## Expected behavior

- Focus feedback on code, designs, and decisions — not on the people who made them.
- Assume good faith. Most bad questions are just early questions.
- Disagree openly, but back it up: cite a benchmark, a failure mode, a spec, a tradeoff.
- Help newcomers find the right channel or doc instead of dismissing the question.
- Respect maintainers' and moderators' decisions on scope, even when you disagree with them.

## Work vs. person

This is the distinction the rest of this document hangs on.

**Allowed, even when blunt:** "This design is embarrassing," "this approach
won't survive a real load test," "this PR is broken and here's why," "I
don't understand how this passed review." Harsh, technical, aimed at the
work.

**Not allowed, regardless of who says it:** name-calling, insults about
someone's intelligence or competence as a person, mockery of how someone
writes or speaks, and any comment that would read the same if you swapped
out the technical topic entirely. If a critique would still make sense with
the code deleted from the sentence, it's not a code review anymore.

Leadership and maintainers get no pass and no extra latitude here. A blunt
technical take from someone senior lands harder precisely because of their
standing — that's a reason to hold the line tighter, not looser.

## Unacceptable behavior

- Personal attacks, insults, or demeaning remarks about a person rather than their work.
- Harassment, including repeated unwanted contact after being asked to stop.
- Discriminatory jokes, slurs, or comments related to identity, background, gender, orientation, disability, or religion.
- Sexual content or unwelcome sexual attention.
- Doxxing: sharing someone's private information without consent.
- Sustained disruption of channels, voice chats, or events (spam, trolling, derailing on purpose).
- Impersonating staff, moderators, or other members.
- Encouraging or organizing any of the above, even "as a joke."

## Reporting

If something crosses the line, tell the moderation team:

- DM any role tagged `@Moderator` in the member list, or
- Use `/report` in any channel (routes privately to the mod team), or
- Email conduct@loomwright.dev if you'd rather not use Discord at all.

Reports are handled by moderators who were not involved in the incident.
You won't be asked to confront the other person yourself, and we won't
share your name with them without your OK.

## Enforcement

Moderators use judgment based on severity and pattern, not a fixed script,
but the general ladder is:

1. **Private warning** — explain what crossed the line and what's expected instead.
2. **Timeout** — temporary loss of posting ability, usually 24 hours.
3. **Kick** — removed from the server, free to request reinstatement after reflection.
4. **Ban** — for severe or repeated violations, or anything in the unacceptable list above.

Serious violations (harassment, doxxing, discrimination) can skip straight
to a kick or ban on a first offense. This ladder applies the same way to
every member, including the team behind Loomwright.

## Scope

This applies inside the Discord server and to Loomwright-branded spaces
(events, official social accounts when representing the community) and to
DMs sent because of a Discord interaction. What you do on your own accounts,
unrelated to Loomwright, isn't covered here — unless it directly targets
someone from this community.

## Changes

We'll revise this as the community grows past 2,800 people and new
situations come up. Material changes get announced in `#announcements`
before they take effect.

---

Questions about this document go to conduct@loomwright.dev.
```