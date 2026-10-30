# Email craft and worked copy

## Table of Contents

- [Subject lines](#subject-lines)
- [Preview text](#preview-text)
- [The body shape](#the-body-shape)
- [Formatting](#formatting)
- [Banned moves](#banned-moves)
- [The humanizer pass](#the-humanizer-pass)
- [Worked copy: the last-call email](#worked-copy-the-last-call-email)
- [Worked copy: the day-before nudge](#worked-copy-the-day-before-nudge)

## Subject lines

- **Name the event.** The recipient is searching their inbox for it. Roughly 40-60 characters, since most opens happen on a phone and the tail gets truncated.
- **Clear beats clever, specific beats vague.** "DevOpsDays Chicago: what to know before Thursday" beats "Almost time!".
- **A first name is welcome, not suspicious.** Cold-email research says a personalization token signals automation and hurts replies - that finding inverts here, because the sender legitimately holds a registration record and the recipient knows it.
- **Never disguise the sender.** Lowercase fragments and colleague-imitating phrasing exist to defeat a stranger's spam filter. Your recipient consented; hiding your identity makes their search fail.

## Preview text

Treat it as a real field, not a leftover. 40-90 characters that **extend** the subject rather than repeat it. If the subject is "What to know before Thursday", the preview carries "Doors 8:30, check-in on the 2nd floor, full details inside" - the reader gets a usable fact before opening anything.

## The body shape

Five parts, one job per email:

1. **Hook** - the first line earns the open. For an event email that means the single most useful fact, not a greeting.
2. **Context** - why this matters to _this_ recipient right now, in one sentence.
3. **Value** - the actual content: the sections, the dates, the instructions.
4. **CTA** - one primary action, one link. A second competing link halves the first one.
5. **Sign-off** - a human name and a real reply route. The organizer's own voice is the credibility in this channel.

## Formatting

- Short paragraphs, one to three sentences.
- Scannable headings and bullets for anything with more than three facts - the sourced email is almost entirely headed sections for exactly this reason.
- Mobile-first: assume a narrow screen and a thumb.
- Bold sparingly, on facts the reader will look for twice (times, addresses, deadlines).
- Put the address and the time in **text**, never only inside an image. Images are blocked by default in many clients, and the address is the one thing that must survive that.

## Banned moves

- Manufactured urgency. If the deadline is real, the date carries it. If it is not real, do not invent one.
- Two CTAs of equal weight.
- New information in the day-before nudge.
- Promotional content inside a transactional confirmation.
- Any claim about the event you have not confirmed with the sibling that owns it.

## The humanizer pass

Run every drafted email through your preferred humanizer skill before it goes anywhere. Never ship a raw first draft - a room of developers reads model-shaped prose all day, and this is the channel where the organizer sounding like a person is the entire point.

What to look for on the way out:

- Stock openers ("We're thrilled to announce", "As you may know", "In today's fast-paced world").
- Adjective inflation - "incredible", "amazing", "unforgettable" - carrying no fact.
- Rule-of-three lists that pad rather than enumerate.
- Uniform sentence length across a whole paragraph.
- Em-dash rhythm repeated in every paragraph.
- A sign-off from a role rather than a person.

Read the result aloud. If it does not sound like the organizer talking, it is not finished.

---

## Worked copy: the last-call email

Written for this skill, not a send anyone observed. The event, the names and the dates are invented; the rules they demonstrate are the ones above.

**Positive.**

> **Subject:** Early-bird pricing for PyConf Nantes ends Friday
> **Preview:** Standard tickets start Saturday; nothing else changes.
>
> Early-bird tickets for PyConf Nantes close this Friday, 14 March, at 23:59 CET. After that, standard pricing applies for the rest of the sale.
>
> That's the only change - same programme, same venue, same two days on 8-9 May. If you were already planning to come, it's worth doing before Friday.
>
> [Get a ticket]
>
> - Claire, on behalf of the organizing team

Why it works: one dated fact stated exactly, no invented scarcity, one link, and a named human. The reader can act or ignore it in five seconds.

**Negative.**

> **Subject:** ⏰ LAST CHANCE - don't miss out!!
> **Preview:** ⏰ LAST CHANCE - don't miss out!!
>
> This is your FINAL opportunity to secure your spot at the most anticipated Python event of the year. Tickets are going fast and we'd hate for you to miss this incredible experience.
>
> Spots are limited! [Register now] or [see the schedule] or [follow us on social]
>
> The Team

Why it fails:

- the event is never named in the subject, so the email is unfindable later
- the preview repeats the subject and wastes the field
- "Going fast" and "limited" are unverified claims
- three competing CTAs
- no date anywhere, the one fact the email exists to deliver
- no human signs it

## Worked copy: the day-before nudge

**Positive.**

> **Subject:** PyConf Nantes tomorrow - doors at 8:30
> **Preview:** Check-in is on the ground floor, Halle 6. See you there.
>
> PyConf Nantes starts tomorrow. Check-in opens at 8:30 on the ground floor of Halle 6, 24 boulevard de Chantenay. Bring something with your name on it; badges are printed on site.
>
> Everything else - schedule, food, transit, accessibility - is in [last week's email].
>
> - Claire

Why it works:

- three lines, one job
- time and address in text, so they survive blocked images
- one link, pointing back rather than forward
- nothing new appears here for the first time

**Negative.**

> **Subject:** See you tomorrow!
> **Preview:** We can't wait!
>
> We're so excited to welcome you tomorrow! Quick reminder that we've moved the workshop track to Room B, and there's now a pre-event breakfast at 8:00 for anyone who wants to join. Also, please remember to bring your own laptop charger as we have limited outlets.
>
> Can't wait to see everyone!

Why it fails:

- the event is unnamed, so it is unsearchable
- three pieces of genuinely new information (a room change, a new breakfast, a hardware requirement) land in the send with the lowest read rate of the whole arc
- anyone who does not open it arrives to a moved room
- no time, no address
