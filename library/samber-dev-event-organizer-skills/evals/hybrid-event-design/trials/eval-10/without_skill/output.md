**Start here (about 30 minutes):** make one spreadsheet with a row per session (31 rows) and a "remote status" column. Don't build the page yet.

## Why not a separate page

- Two agendas drift. Every room swap, speaker change or time shift gets made twice, and the remote page will go stale first.
- The public grid already exists. A second page means two URLs, two sets of links, and split search traffic.
- The real difference between the two agendas is one attribute per session: whether it is streamed. A column holds that. A second page doesn't need to.

If marketing wants a clean remote landing page, make it a filtered view of the same data, for example `/agenda?format=remote`. Don't hand-maintain it.

## Steps

1. **Build the table.** Columns:
   - session, track, day and time, speaker
   - format (talk, workshop, panel)
   - remote status: `live`, `replay only`, or `in-room only`
   - speaker consent: written, with date
   - remote interaction: chat Q&A, or none
2. **Pre-fill the known rows.**
   - The two opted-out speakers are `in-room only`. Add no replay either, unless they agree to one.
   - The Thursday workshop block defaults to `in-room only`. Hands-on, dense sessions don't stream well, and live Q&A was never the shape of them. If marketing wants something remote there, offer materials plus a later replay, and ask the speakers first.
3. **Get written consent from all speakers, not only the two who spoke up.** Live streaming and a replay are separate permissions. Ask for each separately, and cover slides, audience shots and Q&A voices too. If you are in the EU, add attendee image notices for the rooms being filmed.
4. **Count what is left.** Take 31, subtract the two opt-outs and the Thursday block. If the remaining remote offer is thin, say so to marketing before you promise a full hybrid agenda. It may be a "selected sessions" offer.
5. **Publish a note and a badge on the existing grid.** Add a small "Streamed" badge per session and a filter. Add one line saying which sessions are in-room only. The grid went public Monday, so changing it quietly looks like a bait-and-switch.
6. **Add the remote view last.** Build it from the same data once steps 1–5 are settled.

## Questions to settle with marketing (ranked)

1. What does "hybrid" promise: a live stream of everything, or selected sessions? Is the remote ticket paid or free?
2. Which time zone does the remote audience expect? Show times in the viewer's zone on the remote view.
3. Who handles the stream (platform, camera crew, rooms with AV)? This can cap which sessions are streamable regardless of consent.

**Next action:** create the 31-row table and mark the two opt-outs and the Thursday block. Then send marketing question 1.