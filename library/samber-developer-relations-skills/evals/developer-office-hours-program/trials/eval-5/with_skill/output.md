**Do first, in this order (about 20 minutes):**

1. Revoke the API key shown in the staging dashboard. Treat it as compromised, because the video is public.
2. Check the key's usage logs since the publish date for calls you don't recognise.
3. Unpublish the video, or set it private.
4. Review every screen-share segment for tokens, internal hostnames and customer or partner names. Cut or blur them, then re-upload.
5. Ask legal whether partner or customer names on that dashboard count as a personal-data exposure. That decision is theirs, not yours.

Downloaded and cached copies of the old video may still exist. Revoking the key is the only fix that holds.

## Answers to your three questions

**"Is 'heads up, we're recording, hope that's cool!' enough?"** No. It is the skill's own bad example: consent is assumed and nothing is said about where the recording goes. For German and Dutch partners it falls short of GDPR transparency. A valid notice names the destination, the retention period and a no-record path before anyone speaks.

**"What's the standard GDPR notice other programs use?"** There isn't one. No office-hours program (Kubernetes, Stripe, GitLab, Python, Django) publishes a GDPR recording notice, lawful-basis statement or retention policy. I can't cite one without inventing it.

The wording below is an operational draft for your legal team, not legal advice. Legal owns the final text, the lawful basis and the retention period.

**"Can I record the 1:1s too?"** Not by default. The policy for booked slots is **never record; internal notes only**. Partners bring their own code, customer data and private context to those slots, and Python stopped recording so participants could speak freely. Don't record 1:1s for the library. Take notes, then publish a write-up from the questions that are useful to others. If you still want recordings, treat it as a separate opt-in with legal review: a separate written consent per partner, no auto-publication, and no recording of anything a partner marks as private.

## Recording policy (print this on the scope card)

| Format | Policy |
| --- | --- |
| Monthly livestream | Record and publish with captions. State the destination and retention. Offer camera-off, chat-only and anonymised reading of questions. |
| Booked 1:1 slots | Never recorded. Internal notes only. Questions useful to others go to a write-up. |
| Async thread | The text is the record. Pin a "no logs, keys or customer data" rule and give moderators a redaction path. |

**For the training library**, build from three sources:

- the reviewed livestream recordings;
- 1:1 write-ups, with the asker's consent to be quoted;
- re-recorded demos of recurring 1:1 topics, with no partner present.

## Opener to replace yours

Say it before recording starts, and again when the recording begins so late joiners hear it. It names destination, retention and a no-record path before anyone speaks.

**English**

> This session is recorded and published on [platform] within [3] days, and kept for [12 months]. If you'd rather not appear, keep your camera off and use the chat. We read chat questions without names if you ask. Don't share a screen that shows keys, customer data or internal hostnames. Privacy details: [link].

**Deutsch (draft, needs native and legal review)**

> Diese Sitzung wird aufgezeichnet und innerhalb von [3] Tagen auf [Plattform] veröffentlicht. Die Aufzeichnung bleibt [12 Monate] online. Wenn Sie nicht erscheinen möchten, lassen Sie die Kamera aus und nutzen Sie den Chat. Auf Wunsch lesen wir Chat-Fragen ohne Namen vor. Teilen Sie keinen Bildschirm mit Schlüsseln, Kundendaten oder internen Hostnamen. Datenschutzhinweise: [Link].

**Nederlands (draft, needs native and legal review)**

> Deze sessie wordt opgenomen en binnen [3] dagen gepubliceerd op [platform]. De opname blijft [12 maanden] online. Wilt u niet in beeld komen? Laat dan uw camera uit en gebruik de chat. Op verzoek lezen we chatvragen zonder naam voor. Deel geen scherm met sleutels, klantgegevens of interne hostnamen. Privacyinformatie: [link].

**Items for the linked written notice.** These are my own checklist, not drawn from any published program. Have legal fill them in:

- who is the data controller, and the contact for privacy questions;
- the purpose (training library) and the lawful basis;
- where it is published, and who can view it;
- the retention period;
- how to withdraw or request removal;
- the right to complain to a supervisory authority.

Add to the registration or intake form: "May we read your question out on the recording? Yes / Anonymise it / No, answer me in the write-up only." Honour every "don't read my name" answer.

## Pre-publication gate (every livestream)

1. Run the screen-share test in a scrubbed demo environment 10 minutes before the stream.
2. Watch every screen-share segment for keys, tokens, internal hostnames and customer names. Cut or blur.
3. Revoke any token shown in a demo environment, as GitLab's token guidance recommends.
4. Check the intake form for "don't read my name" requests.
5. Add captions.
6. Publish only after steps 1-5 pass.

The leak happened because step 2 didn't exist. Make it a named checklist item with an owner.

## Open decisions

I couldn't ask the skill's interview questions. These change the design, so answer them when you can:

1. Is the one job of the program unblocking partners, finding docs gaps, or hearing product feedback?
2. Who staffs it? I need names, time zones, and each engineer's cap per month. The default cap is one session per engineer per month.
3. What can never appear on a recording? Think unreleased features and partner code.
4. Do partners have a support contact, a sales contact and a security channel? The scope card needs them as destinations.
5. Which language do sessions run in, and where are partners by region? A single slot may not fit both the Germany/Netherlands audience and any US partners.
6. Is this a standing program or a one-off? This skill designs standing programs.

Partners and plugin authors need their own code on screen. That is the case where the skill promotes booked slots first. Keep them unrecorded and feed the library from write-ups.

**Next action:** revoke the key now. Then send your legal team the opener and the checklist above.