# Where the 14 streams went, and how to run this properly

## Short answer

Twitch most likely deleted them. This is a retention rule, not a bug.

- **Non-affiliate channels keep past broadcasts for 14 days.** Affiliates, Partners and Turbo subscribers get 60 days.
- Your last stream was around late September, so every June–September VOD expired by mid-October at the latest.
- If "Store past broadcasts" was off in Creator Dashboard → Settings → Stream, those streams were never saved at all.
- Deleted VODs are not recoverable. Twitch support won't restore them, though a ticket costs nothing if you want to try.

I'm working from Twitch's published policy as I know it. I haven't looked at your channel, so check the details below.

## What you might still have (check today)

1. **Highlights.** Highlights don't expire like VODs do, though Twitch now caps total highlight storage, so confirm the current limit. Check Creator Dashboard → Content → Video Producer → Highlights tab, not Past Broadcasts. The streams you can still see are probably highlights or uploads.
2. **Local OBS recordings.** Check each streamer's machine, under Settings → Output → Recording Path. This is the best case if anyone recorded locally.
3. **Cloud tools.** If you used Restream, StreamYard, Streamlabs or a simulcast to YouTube, those services may have kept their own copies.
4. **Clips.** These are 60 seconds at most. They are only useful for promo, not for the course.
5. **Cold backups.** Look in anyone's Downloads folder, shared drive or Slack for exported files.
6. **Third-party archives and chat logs.** Don't count on these. Usually nothing useful survives.

For anything you find, download it now and make two copies. Highlights can also be exported to YouTube from Video Producer.

## If most are gone

Treat them as source material, not course footage. Raw 2-hour streams make a weak course anyway.

1. Rebuild each episode as a tight 10–20 minute lesson, re-recorded with a script.
2. Reuse what survives: the code repo state per episode, slides, chat questions and any highlights.
3. Cut or reuse any surviving footage only where it is clean.

Marketing gets a better course this way, and it needs no luck with recovery.

## Going forward

**Capture**
1. **Record locally in OBS on every stream.** Use MKV so a crash doesn't corrupt the file, then remux to MP4. Record at higher quality than you stream.
2. **Use separate audio tracks** for the mic, desktop audio and any guest. You can then fix levels or remove music afterwards.
3. **Simulcast to YouTube Live** if you want a second archive. Set it unlisted at first and edit it before you publish.
4. **Turn on "Store past broadcasts"** and confirm the setting.

**Retention**
5. **Within 48 hours of each stream:** copy the local recording to shared storage, with a second copy off-site.
6. **Within 7 days:** create a Highlight from the full VOD, so a copy outlives the 14-day window.
7. **Keep a one-row-per-episode log** with date, title, file location, repo commit and status.

**Turning streams into a course**
8. Plan the course at the start: learning outcomes, order, and what each episode depends on.
9. Edit each episode: cut dead air, add chapters, add captions, and fix errors with a short inserted correction.
10. Pin a repo tag per episode so viewers can follow along.

**Risk review before publishing anything**
11. **Secrets on screen.** Scan footage for API keys, tokens and dashboards. This is the most common live-coding leak.
12. **Music and copyright.** A DMCA claim on YouTube hits harder than muted audio on Twitch.
13. **Guests and chat.** Get consent for guest appearances, and blur or avoid showing viewer names.

## What to do this week

1. Someone checks the Highlights tab and every local drive today, and reports which of the 14 episodes survive.
2. Fix the capture settings (items 1–4) before the next stream.
3. Decide with marketing: salvage surviving footage, re-record, or a mix. I'd go with the mix.

Tell me which episodes survive and I'll draft the episode log and the re-record plan.