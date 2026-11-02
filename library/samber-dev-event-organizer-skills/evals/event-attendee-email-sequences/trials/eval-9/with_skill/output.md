# Lintfold Community Day, Ghent: email plan

**The sequence you asked for doesn't apply to this event.** The skill I followed treats a no-registration event as having no list to sequence. Its answer is one practical-info page plus one announcement. That is the full program, not a cut-down version.

## Why the sequence collapses

- With "no tickets, no registration, just turn up", nobody holds a "registered" state. Confirmation, last call, know-before-you-go and day-before nudge all fire on registration or on a ticket cutoff. Neither exists.
- The skill says not to build a list just to make the arc apply. A signup form for an event with no signup would do that.
- A day-before nudge would reach only people who volunteered an address. That is a few of the people who might show up, and the rest would never see it. The page has to carry the information, because it is the only place everyone can find it.
- This also matches FOSDEM's published posture: "There is no registration. Just turn up!"

## Decision for you: the signup form

I recommend **not** building it.

If you want one anyway, that's your call. It would be a voluntary "keep me posted" subscription, not an attendee list:

- It needs its own recorded opt-in and an unsubscribe.
- It should be labelled as optional.
- It should state that no registration is needed to attend.
- It must not be used to build a headcount. Anyone who joins and doesn't come would otherwise look like a no-show.

I haven't written sequence copy for it. The skill doesn't support one for this posture, and the page below already covers that audience.

## The plan (2 deliverables, 1 send)

| # | Deliverable | When | To whom |
|---|---|---|---|
| 1 | Practical-info page on the Lintfold site | Live before the announcement, then kept current | Public, linked from everything |
| 2 | One announcement email | Date set by your marketing plan (not given to me) | Release-announcements list, if the consent check passes |

Counts per segment: the 4,000 addresses get 1 send. That is inside the skill's cap of 2 to 4 for the whole arc.

Today is 2026-10-12, so the runway to 7 February 2027 is about 17 weeks. Nothing is compressed. I haven't picked an announcement date, because the skill says that date comes from the marketing plan. If it is still open, pick one that leaves time for the first wave of travel planning. Note that 7 February 2027 is a Sunday. That is your date, and I'm not suggesting a change.

## Consent check on the 4,000 addresses

⚠️ **This is the part that can go wrong, and it can't be undone.**

- People joined for release notes. An event announcement is promotional and is a different purpose from what they signed up for. The skill's rule is that consent for one purpose doesn't carry over to another unless an opt-in was recorded.
- Your list is Lintfold's own, run by a community project, and the event is the project's own. That makes the case for relevance reasonable. I can't call it consent, though.
- Before sending, check:
  1. What the signup form or text said at collection. Did it mention project news or events, or only releases?
  2. Whether you hold provenance per address (source, date, box ticked).
  3. Your legal basis. Many recipients will likely be in the EU or Belgium, where consent and ePrivacy rules apply. I'm not giving a legal verdict. Get sign-off first, ideally from someone who knows your jurisdiction.
- If provenance is unclear, don't send to the whole list. Post on the channels people follow instead: repo, release notes page, social. Or send one release-notes email whose footer links to the event page.
- Whatever you send needs a working unsubscribe, honoured immediately, and one line saying why they are getting it.

## Deliverable 1: the practical-info page

The skill's know-before-you-go structure, adapted for a free, open-door day. I don't have any on-site facts. The skill says never to invent them, so every `[TBD]` is a fact you must supply from whoever owns the venue and attendee experience before the page or email goes out.

Open with the event name, exact date, and opening time. Put the address in text, not only in a map image.

1. **Lintfold Community Day.** Sunday 7 February 2027, doors `[TBD hours]`, `[TBD venue and full address]`, Ghent. Free. No tickets, no registration, just turn up.
2. **Code of conduct.** Link, consequence, and contact `[TBD: owned by your code-of-conduct doc]`. Venue rules apply too.
3. **Accessibility.** Step-free access `[TBD]`. What needs advance notice, by when, and who to ask `[TBD]`.
4. **Getting in.** Which entrance, which floor, what to expect `[TBD]`. Say whether there's a badge or name tag, a bag or coat policy, and re-entry `[TBD or "none apply"]`.
5. **Getting there.** Train to Gent-Sint-Pieters and the onward route from the station, plus driving and parking `[TBD, verify before publishing]`. Include airport routes if you expect travellers, such as Brussels airport.
6. **Schedule.** Link or short list `[TBD]`. Say whether sessions are drop-in.
7. **Food and drink.** Whether it's provided, where, and dietary handling `[TBD or "not provided"]`.
8. **Wifi.** `[TBD]`.
9. **Nursing or parents' room.** State it if it exists, or state that there isn't one.
10. **Capacity.** Open doors have a limit. If the venue has one, say what happens when it fills, and how people will know `[TBD]`. This matters more here than at a ticketed event, since you can't turn anyone away in advance.
11. **Social.** Hashtag and handles.
12. **Contact on the day.** How to spot an organizer, plus a contact route that works during the event.
13. **Sponsor thanks**, if any.

Evening events and health and safety are conditional sections. Include them if they exist, and mark them "not applicable" if not.

The page is the single source of truth. Update it in place rather than sending corrections by email.

## Deliverable 2: the announcement email

One job: it exists, it's dated, here is where to look. One link only. Placeholders mark facts I don't have.

> **Subject:** Lintfold Community Day, Ghent: 7 February
> **Preview:** Free, no registration. Just turn up. Details on the site.
>
> Lintfold is holding a free community day in Ghent on Sunday 7 February 2027, at `[venue]`.
>
> There are no tickets and no registration. Doors open at `[time]`, and you can come for as long as you like.
>
> `[One line on who it's for and what happens, e.g. "Meet maintainers and other users, and work on Lintfold together."]`
>
> Venue, how to get there, the schedule and accessibility details are all on one page: [link]
>
> You're getting this because you joined the Lintfold release-announcements list. This is the only email we'll send about the event, and you can unsubscribe at the bottom of this message.
>
> - `[Name]`, for the Lintfold maintainers

Choices made, and why:

- The subject names the event and date in plain words, with no hook. Readers are searching their inbox for it later.
- There is one CTA and no countdown. Nothing is sold, so there's no scarcity to claim.
- The "why you're getting this" line is for the consent check and for readers who don't remember joining.
- I did not write the employer-forwardable paragraph. It's an optional add-on for events where an employer pays. For a free day, consider it only if you expect people to need travel approval.

**Humanizer pass.** I drafted this without stock openers, adjective inflation or three-item padding. Before sending, read it aloud, put a real person's name in the sign-off, and rework any sentence that doesn't sound like you.

## What I deliberately left out

- **Confirmation, agenda release, last call, know-before-you-go and day-before emails.** There's no registration to confirm and no ticket cutoff to react to. The know-before-you-go content lives on the page above. If you publish a schedule later, announce it on social and the repo, not by a second email to the 4,000.
- **A post-event thank-you.** It would go to a list of attendees, and you have none. If you want to thank people, do it publicly. If you still want a feedback survey, that's a separate decision, and the skill routes the instrument to its feedback sibling.
- **No-show handling.** With free entry and no registration there are no no-shows, and nobody to remind. A capacity problem is the open-door equivalent, and it is covered in section 10 of the page.

## Open items I need from you

1. The announcement date from your marketing plan, if one exists.
2. The consent provenance answer above, and who signs off.
3. Every `[TBD]` on-site fact: venue, hours, access, food, capacity.
4. Your decision on the optional signup form.
5. Which of the two measures you will track, with what each would change. For this event, desk questions the page already answered, counted at the door, and unsubscribes or complaints on the one send, are the usable ones. Record both before the event.

Nothing has been scheduled or sent, and I haven't created or edited any files.