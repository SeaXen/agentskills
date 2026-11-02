# Platform decision: don't sign the $9,000 quote

Run Northwind DevCon on **YouTube Live for video and your existing Discord for everything social**. That costs about $0 in platform fees.

## Why the quote is the wrong shape

Each feature in the quote solves a problem you don't have:

| Quote feature | Your situation | Replacement |
|---|---|---|
| Breakout rooms | Single track, 8 talks, one day | Discord voice channels as a hallway |
| Expo area | No sponsors, nothing sold | Nothing needed |
| Attendee directory | 2,400 people already together in Discord most weeks | Discord member list plus an `Attendee` role |
| Virtual venue | Strangers need somewhere to gather | Your community already has that place |

A new platform also splits attention. 2,400 regulars would have to move to an unfamiliar tool for one day. Most platforms with this feature set also exist to serve sponsor lead capture, which you don't have.

## What you need

1. **Stream:** YouTube Live, public or unlisted.
   - Free, handles 600 viewers easily, and gives you auto-captions.
   - It records automatically, so the 8 talks become a post-event archive.
2. **Speaker side:** OBS (free) plus any call tool speakers already use, such as Zoom or Google Meet.
   - Alternatively, use a browser studio like StreamYard (free tier, or a low paid tier). Check current pricing before committing.
   - Have a producer cut between speakers and slides.
3. **Chat and Q&A:** Discord, not YouTube chat.
   - Create `#devcon-live` for general chat.
   - Create `#devcon-questions` for Q&A, where a moderator reads questions to the speaker.
   - Optionally create one thread per talk.
4. **Hallway and breakouts:** 2–3 Discord voice channels, open between talks.
   - Open them with a topic label (for example `#hallway-go` or `#hallway-infra`).
5. **Directory:** a Discord `Devcon-2026` role, given on registration.
   - Add an `#introduce-yourself` channel.
   - This also keeps attendee data out of a third-party vendor.
6. **Registration:** keep whatever you used for the 600 sign-ups.
   - Email the stream link, and post the same link in Discord.
7. **Event page:** one static page with the embedded stream, schedule, and Discord invite.

Don't use Discord as the main video broadcast for 600 people. It has weaker stream quality and no easy recording. Verify the Stage channel audience limits and screen-share quality before relying on them for anything.

## Sizing check

- Expect roughly 30–50% of registrants live, so about 200–300 concurrent viewers. That is a normal load for YouTube.
- Moderation matters more than tooling. Staff 2–3 moderators, one per channel group.

## Before the day

1. Rehearse with all 8 speakers.
2. Have a pre-recorded fallback for any speaker whose connection fails.
3. Confirm each speaker consents to recording and public archive.
4. Run a 30-minute tech check the day before.
5. Assign one person to the stream, one to Q&A, and one to the hallway.

## When the $9,000 platform would make sense

Revisit it only if one of these becomes true:

- You need gated, attendee-only access.
- Sponsors want an expo and lead capture.
- You add multiple parallel tracks.
- You expect thousands of concurrent viewers.
- You go hybrid with an in-person component.

None applies to this year's event.

## Next steps

1. **Today:** tell the vendor you're passing, or ask for a month-to-month or per-event option so the quote doesn't lapse by default.
2. **This week:** set up the YouTube event, the Discord channels and role, and the event page. This takes about half a day.
3. **Next week:** run a dry-run stream with 2 speakers.

## Questions that could change this

- Does registration need to be gated, for example a members-only stream?
- Do any speakers need to be in a call together (panels), or is it solo talks?
- Is anyone on the team comfortable running OBS live? If not, a small budget for a producer or StreamYard is the one place worth spending.