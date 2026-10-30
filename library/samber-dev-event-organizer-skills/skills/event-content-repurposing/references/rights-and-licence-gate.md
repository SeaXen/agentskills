# Rights and licence gate

Run this before production, not before publication. A planned clip is free to abandon; an edited one is not.

Contents: 1. The per-session consent check - 2. The derivative-works question - 3. Third-party material in slides - 4. Attendee faces - 5. The licence decision - 6. Escalation.

## 1. The per-session consent check

Mark every session in one of three states and write the list down before choosing any format:

- **Usable** - the consent record covers this session's format and this kind of publication.
- **Restricted** - covered for some uses and not others, or covered with a named condition (a slide withheld, a segment cut, no attribution).
- **Off-limits** - not covered, or the record is silent. Silence is off-limits, not permission.

Three rules govern the list, and none of them is yours to soften:

- The record is collected and owned by `samber/dev-event-organizer-skills@event-speaker-experience`; you read it.
- The rule inherited from `samber/dev-event-organizer-skills@event-production` applies one layer down: a recording the consent record does not cover is unpublishable, and so is a derivative of one.
- A camera in the room was never agreement.

PyCon US 2026's recording release (`us.pycon.org/2026/speaking/recording/`) shows what such a record looks like: consent granted at submission rather than negotiated later, and an opt-out that differs by session format - available for some formats, and stated plainly as unavailable for lightning talks. Take the asymmetry as the lesson: one event can run several policies at once, so "the event records talks" is not an answer at session granularity.

## 2. The derivative-works question

Ask of the record: does it grant only recording and publication, or does it reach editing and derivative works?

- PyCon US 2026's release reaches derivatives explicitly - the licence is described as worldwide, royalty-free, fully paid-up, non-exclusive and perpetual, extending to editing and to creating derivative works. Few releases go that far.
- Most releases stop at recording and publication and say nothing about a later re-cut, a translated subtitle track or a re-edit.

Where the record stops at publication, do not read a permission into the silence. The fix belongs upstream, at consent-collection time, in the sibling that owns the form - a sentence added to next edition's release costs nothing, and reconstructing permission afterwards costs a conversation per speaker. Until then, treat that session as restricted: link to the master rather than cutting from it.

## 3. Third-party material in slides

**Nobody owns this, here or at most events.** No skill in this collection covers slide copyright or licensing review, and conferences rarely publish a written policy for it. The checklist below is this skill's own and deliberately minimal, so it does not read as the clearance advice it is not.

Before a clip is cut, look at the frames and the audio for:

- Music under a demo, an intro, or playing in the room.
- Another company's logo, product screenshot, or interface in a demo.
- A stock or licensed image whose licence covers a slide but may not cover a re-published clip.
- A chart, table or quotation taken from someone else's published work.
- A person on screen who is not the speaker.

Then take one of three actions:

- Clear it with whoever holds the rights.
- Cut those frames.
- Drop the clip.

Do not publish and wait to see.

The nearest written rule sits next door and does not transfer cleanly. The DevOpsDays organizing guide warns, of streaming, _"Be very careful not to accidentally include any background music, or YouTube will take your stream down."_ (`devopsdays/devopsdays-web`, `content/page/organizing.md`).

That is a capture-time platform risk on a live feed, not a rights review at republishing time. It proves the exposure is real; it does not tell you how to clear anything.

One written clearance policy does exist, outside this domain. IEEE's conference copyright and consent form makes every presenter warrant, before recording or publication rights transfer at all, that _"the undersigned has obtained all third party permissions and consents"_. IEEE's own policy then states plainly who is on the hook if that warranty turns out false: _"It is the responsibility of the authors, not the IEEE, to determine whether disclosure of their material requires the prior consent of other parties and, if so, to obtain it."_

IEEE runs academic and standards conferences, not independent developer events. Treat it the way this file treats TED's licence below: one large organization's own mechanism, never a convention this skill's users are expected to match. Two things transfer, and the form itself is not among them:

- A presenter warranty taken before publication.
- A named party answerable if that warranty was false.

One documented case shows the other direction - published footage edited after the fact for a reason nobody anticipated at capture. Write the Docs Prague 2017's recap records a discriminatory joke in a talk being removed from the video, alongside the rest of its post-event account (`writethedocs/www` archive, 2017). Plan for the edit you will want to make later: keep the source files, and keep a record of what was cut and why.

## 4. Attendee faces

Any derivative containing an identifiable attendee runs through the badge-based opt-out mechanism owned by `samber/dev-event-organizer-skills@event-accessibility-inclusion`, whose colour-coded sticker scheme includes a signal for someone not interested in being photographed. Read that signal; do not invent a second one, and do not build a parallel consent flow.

Two properties make this the heaviest rung on the compliance axis:

- The signal was given in a moment that has passed, so it cannot be re-collected: re-asking a room of people is not available to you.
- A published face cannot be recalled from the copies already made.

Practical consequence: if the opt-out signal is not retrievable per photo, treat the whole photo set as restricted for close crops and usable only for wide shots where nobody is identifiable - or not at all. Deciding this at planning time is cheap; deciding it after a clip is cut is not.

Do not attribute any of this to `samber/dev-event-organizer-skills@event-code-of-conduct`. Its policy text names harassing photography and recording as prohibited conduct and carries no photo-consent or licensing norm. Reading one into it invents a policy the event never adopted.

## 5. The licence decision

No sibling claims this, and conferences follow no shared convention, so it is yours by default. Decide, and record who decided:

- Whether published derivatives carry an open licence at all.
- Which licence, and whether attribution and share-alike terms are wanted.
- Whether it differs by artifact - a transcript, a clip and a photo are three different things with three different rights-holders behind them.
- Where the licence line appears, so a re-user sees it without asking.

No developer conference publishes a shared licence convention to copy. One large-conference precedent exists outside the domain: TED licenses its talks under Creative Commons BY-NC-ND 4.0, meaning attribution required, no commercial use, no derivative works, and screened in full or not at all. A separate paid licence covers commercial or classroom screening.

TED is not a developer conference, and its scale, production budget and rights-clearance process do not transfer. Cite it as one large event's own choice, never as a standard this skill's users are expected to match.

Two constraints bind. Both are this skill's own reading of the rights position, not legal advice, and neither is optional:

- **You cannot grant more than the record gave you.** An open licence over a talk whose release covers publication only is a grant you never held.
- **You cannot license somebody else's work.** A derivative carrying third-party material licenses that material along with yours if the licence line is applied naively.

Where either bites, publish without an open licence and state that plainly rather than leaving the terms unstated. An artifact with no licence line and no statement is the case a re-user resolves in their own favour.

## 6. Escalation

Five routes, all this skill's own construction rather than a published procedure:

- The record is silent on a session → mark off-limits, route the record gap to `samber/dev-event-organizer-skills@event-speaker-experience` for next edition.
- The record covers publication but not derivatives → mark restricted, link rather than cut, route the same way.
- A clip cannot be cleared of third-party material → drop the clip; there is no partial version of this.
- The photo opt-out is not retrievable per photo → restrict the whole set rather than sampling.
- A speaker asks for a published derivative to come down → take it down first, then work out whether it had to. Reversibility is the whole reason this gate runs before production.
