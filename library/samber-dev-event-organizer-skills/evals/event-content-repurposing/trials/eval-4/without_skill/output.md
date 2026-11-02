# Plan: 60-second vertical cuts and Portuguese subtitles for StackHarbor Conf

I can't call consent "sorted" yet. Two things block a clean start, and they change the plan.

## 1. Clearance gate (do this first)

| Group | Count | Status | Action |
|---|---|---|---|
| Speakers with a signed release | 27 | ✅ Cleared for recording and publishing on the conference's channels | Eligible for cuts and subtitles, subject to the scope check below |
| Speaker signed on condition: slide 14 stays out of anything public | 1 | ⚠️ Conditional | Eligible only with slide 14 excluded everywhere (see §2) |
| Two workshop hosts, no signed form | 2 | ❌ No release | Exclude entirely until signed |

- **Knowing about the cameras isn't consent.** Hosts who never returned the form haven't agreed to publication. Don't make cuts or subtitles of their sessions.
- ⚠️ **The full recordings are already live.** If the hosts' workshop recordings are among them, that is an existing gap, not one the cuts create. I recommend unlisting those two videos until the forms are signed. Chase the forms now, or ask the hosts to confirm in writing by email. This is your call, so confirm it before anything else happens.
- **Check how far the release goes.** It says talks "may be recorded and published on the conference's channels." Before you cut, confirm it covers three things:
  - **Editing and excerpting:** Clips are edited excerpts, not the full talk.
  - **Translation:** The Portuguese subtitles are a derivative of the speaker's words.
  - **Channels:** The clips go on the conference's own accounts. Sponsor accounts, paid ads and partner reposts are probably outside the release.
- If the form is silent on any of these, send speakers a one-line heads-up and an opt-out, or get a lawyer's read. A short "your clip is going up on X, reply to object" email costs little.
- **Audience and Q&A:** Cut around identifiable attendees and audience questions. Attendee notice at the venue was probably not written for social clips.

## 2. Slide 14 (conditional speaker)

1. Find every place slide 14 appears in the **already published full recording**. If it's visible, the condition is already broken. Fix it first by blurring, cutting or replacing it, then re-upload.
2. Exclude the slide 14 segment from all cuts. Also check wide shots, transitions and thumbnails where it could show in the background.
3. Check the subtitle track. If the speaker reads out customer names or figures, redact them in the Portuguese text. Do the same for any burned-in captions.
4. Show this speaker their clips before publishing. They set the condition, so a quick sign-off is cheap protection.

## 3. Selecting the best moments (cleared talks only)

1. **Transcribe** all 28 eligible talks, with word-level timestamps.
2. **Shortlist** 3–5 candidate windows per talk (about 100 candidates) using:
   - A self-contained claim or story that needs no earlier context
   - A clear hook in the first 3 seconds
   - A quotable line, a demo reveal or a counterintuitive result
   - Strong audio and a speaker who is well framed
   - Applause or laughter, but not a stretch that depends on a slide the viewer can't see
3. **Reject** any window that shows customer data, an identifiable attendee, unreleased roadmap information or an unverifiable claim.
4. **Pick one or two clips per talk.** You review the shortlist. I don't auto-publish.

## 4. Production spec (vertical)

- 1080×1920 (9:16), 60 seconds maximum, aiming for 45–58 seconds.
- Speaker framing: face-tracked crop from the 16:9 master. Where a slide matters, use a split screen with the speaker above and the slide below.
- Burned-in English captions in the safe zone, away from the platform UI at the bottom and right.
- Outputs: MP4 per clip, a thumbnail, and the SRT or VTT sidecar.
- Tooling: the repo's HyperFrames `talking-head-recut` flow fits this (recut the speaker, add captions).

## 5. Portuguese subtitles (whole programme, cleared talks only)

1. Transcribe, correct names and technical terms using a glossary, then translate EN→PT.
2. Decide on Brazilian or European Portuguese before translating. It changes wording.
3. Deliver sidecar VTT/SRT tracks on the full recordings, since the whole programme is covered. The vertical clips get burned-in or sidecar tracks as a separate file set.
4. Have a native speaker spot-check each talk, concentrating on jokes, numbers, product names and anything that could put words in a speaker's mouth.
5. Label the tracks "machine-translated" or "reviewed" so readers know which they have.
6. Hold the tracks for the 2 hosts' talks. Hold the conditional speaker's track until the slide 14 redaction is checked.

## 6. Sequence

1. **Today:** decide on unlisting the two host recordings, send the form reminder, and check the release wording on editing, translation and channels.
2. **Next:** audit slide 14 in the published recording and fix it if it shows.
3. **Then:** transcribe, shortlist and pick clips (you review).
4. **Then:** produce clips and subtitles, with the native spot-check.
5. **Last:** speaker preview for the conditional speaker, then publish in batches.

Work on the eligible 27 can start now, in parallel with the open items. Only the 2 hosts and the conditional speaker are held back.

## Decisions I need from you

1. Do you want the two host recordings unlisted until their forms are signed?
2. Does the release wording cover excerpts, translation and your social accounts, or does it need a heads-up to speakers?
3. Is the Portuguese Brazilian or European?
4. Where are the master recordings and transcripts? Give me the path and I'll start step 3.