# PortAndAdapter Conf: clip outreach plan

I drafted the outreach with four changes to your plan. Nothing below is sent. The skill's gates run before any send, and your plan fails them in four places.

## What changed from your plan

| Your ask | Verdict | Why |
|---|---|---|
| Email all 30 speakers the full-talk link plus their clip | ❌ Changed | Only 6 clips exist, so at most 6 speakers have a clip. Full-talk links are already sent by `event-production` and `event-speaker-experience`. This message covers the clip and nothing else. |
| Tag the keynote speaker on the event post | ⚠️ Changed | A tag is "no ask". With 120k followers she is the case for a dated joint push, which needs her agreement to a date. The post and tag belong to `event-social-media`. |
| Sponsor report: 10,000 views per clip, 50% of speakers sharing | ❌ Dropped | The skill sets no view target. A number nobody measured becomes what the plan is judged on. The report states measured actuals instead. |
| Send asks on the 2 unreviewed clips | ❌ Deleted | Asking a speaker to amplify a clip they haven't seen puts their name on it before they've watched it. They get a review request instead. |
| Keep the 20-second workshop teaser | ❌ Off-limits | The host never signed the release, and silence is off-limits. Length doesn't matter, and there is no partial version. |

## Do first (today, ⏳ ~15 min)

1. **Take the workshop teaser down.** It is live without a release. Take it down first and work out later whether it had to come down. Send the host nothing yourself. Hand the gap to whoever owns `event-speaker-experience`, since consent collection is theirs (note 5 below).
2. **Check that your consent record reaches derivatives.** Most releases stop at "recording and publication". If a speaker's release stops there, mark that session restricted and link to the master instead of the clip. I couldn't see your record, so everything below assumes it covers the 5 remaining clips. That assumption is unverified.
3. **Name an owner and an end date** for this wave. Every planned artifact needs both before anything ships.

## Usable-session status (6 clips)

| Clips | Status | Action |
|---|---|---|
| Workshop teaser (1) | Off-limits | Take down, no ask, no tag |
| Unreviewed (2) | Held | Review request only (Email A) |
| Reviewed (3) | Usable, if the record covers derivatives | Amplification ask (Email B) |

The keynote clip, if one exists, falls in one of the last two rows.

## Email A: review request (the 2 unreviewed clips)

This is not an amplification ask. The clip is already live, so say so plainly.

> **Subject:** Your PortAndAdapter Conf clip: could you watch it?
>
> Hi {first_name},
>
> We cut a short clip from your talk and published it before checking it with you. That was our mistake.
>
> Here it is: {clip_link} ({duration}, starts at "{opening_words}")
>
> Could you watch it and reply with one of these?
> 1. Happy with it as is.
> 2. Fine, but please change {timestamp}.
> 3. Please take it down. We'll do it the same day, no questions.
>
> We aren't asking you to share it. If you'd like to, we'll send a ready-made caption once you've said yes.
>
> Thanks,
> {organizer_name}

Fire this once each, with no reminder chain. If a speaker says nothing, the clip stays unconfirmed and gets no amplification ask.

## Email B: clip ask (reviewed clips)

The default is the one-line ask. Coordinate it with the follow-up `event-speaker-experience` already sends, so the speaker gets one message. Where that follow-up is going out anyway, add this single line:

> "Your clip from the talk is live: {clip_link}. If you'd like to share it, a ready-made caption is below. No pressure either way."

Promote to a standalone email with the ready-made asset only for speakers whose sessions people asked about (Q7). I don't have that list.

> **Subject:** Your clip is live
>
> Hi {first_name},
>
> A short clip from your talk is up: {clip_link}
>
> If you'd like to share it, here is a caption you can paste or edit:
>
> "{drafted_caption} {clip_link}"
>
> Licence line for re-users: {licence_line}
>
> Thanks again for speaking.
> {organizer_name}

Do not include the full-talk link here. That link is sent by the other two skills.

The other 24 speakers have no clip, so this skill sends them nothing. They get only whatever `event-speaker-experience` already sends.

## Keynote speaker: dated joint push

Skip tag-only. She has a large audience of her own and the event is a keynote, so the dated joint push fits. It only works if she agrees to a date, so ask for one:

> **Subject:** A clip from your keynote: same-day post?
>
> Hi {first_name},
>
> We cut a short clip from your keynote: {clip_link}. {Reviewed and approved by you on {date}. / Please watch it first and tell us if anything should change.}
>
> Would you be up for a joint post on {proposed_date}? We'd post from the event account and tag you, and you'd post from yours the same day, tagging us. A ready-made caption is below if useful.
>
> "{drafted_caption} {clip_link}"
>
> If another date suits you better, we'll move to it. If you'd rather not, that's fine.
>
> {organizer_name}

Send it only if her clip is reviewed and approved. If she hasn't seen it, use Email A first. Don't tag her on the event post until she agrees to the date. The tag and the post itself go to `event-social-media` as a handover row.

## Sponsor report: replacement text

Drop the two targets. Report what you measured:

> **Clips from PortAndAdapter Conf**
> - Clips published: {n} on {dates}. Views to date: {actuals per clip, with date measured}.
> - Speakers asked to share: {n_asked}. Speakers who shared: {n_shared}.
> - Not published: 1 workshop teaser (release not on file). 2 clips held until speaker review.
> - Inventory available to the next campaign: {artifact types, counts, dates, licence status}.

A take-up rate is a diagnostic, not a goal. A low rate usually means an ask that arrived without the asset attached. If the sponsor needs a goal, set it with `event-marketing-plan`, which owns targets. This skill hands up inventory only.

## Handover rows for `event-social-media`

One row per scheduled piece. Fields: artifact and file location, go-out date, licence line, rights restriction, speaker ask status.

| Clip | Date | Restriction | Ask status |
|---|---|---|---|
| Reviewed clip(s), up to 3 | {date} | None, if the record covers derivatives | Email B sent, asset attached |
| Unreviewed clips (2) | Hold | Do not tag, do not promote | Email A sent |
| Keynote clip | {agreed date} | Tag only after she agrees | Joint-push ask sent |
| Workshop teaser | None | Off-limits. Do not tag the host | None |

## Licence

No sibling owns this, so by default it is your decision. I recommend publishing with no open licence for now and stating that on each clip: "© {event}. All rights reserved. Shared with speaker permission." A grant can't exceed what the consent record gave you, and I haven't seen that record. Revisit once you know whether it covers derivatives. Record who decided.

## Notes for the other owners

1. **Rights check on the five clips.** The skill's third-party checklist (music, other companies' logos, stock images, other people on screen) and the attendee-face check haven't been run on any clip. Run both on the five clips left. A clip that can't be cleared gets dropped.
2. **Photo opt-out.** If the badge opt-out isn't retrievable per photo, treat any clip with identifiable attendees as restricted.
3. **Plan fit.** A batched release is the default. A drip only works with a named owner and an end date.
4. **Record per edition.** Which sessions the record covered, what shipped against plan, who amplified, and who chose the licence.
5. **Note to the `event-speaker-experience` owner.** "The workshop host never signed the release, and a 20-second teaser was published. It has been taken down. Please reach out about the release. Also consider adding a sentence on derivative works to next edition's form."

## Questions that would change this plan

1. Does the consent record reach derivatives, or stop at "recording and publication"?
2. Is the keynote clip one of the 6, and has she seen it?
3. Which sessions did people ask about? These get Email B as a standalone with the ready-made asset.
4. Who owns publishing after this week, and until what date?
5. Is there a hard sponsor-report deadline?