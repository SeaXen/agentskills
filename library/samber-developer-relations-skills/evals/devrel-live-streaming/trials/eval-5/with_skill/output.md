# Kestrel stream recovery and a durable stream plan

I read the skill and both reference files. I did not browse, so the Twitch retention figures below are **[practitioner quoting Twitch help]**, not re-read. Re-read the Twitch "video on demand" help page before you rely on them.

## 1. Where the 14 streams are

**Most of them are probably gone from Twitch, and Twitch support cannot bring them back.**

- Past broadcasts are off by default **[practitioner]**. If nobody switched on "Store past broadcasts", nothing was saved.
- If it was on, a non-Affiliate channel keeps broadcasts for 7 days. Affiliates get 14 and most Partners get 60 **[practitioner quoting Twitch help]**.
- At about 180 followers you are not an Affiliate, so every Tuesday stream from June to September expired weeks ago. The last one would have been around 29 September.
- Twitch support cannot recover a broadcast that was not saved **[practitioner quoting Twitch help]**.
- A few survive only if someone turned them into Highlights or uploads. Highlights and uploads have no expiry, and the cap is 100 hours **[practitioner quoting Twitch]**. That is almost certainly why you can find some.
- Affiliate status would not have fixed this: 14 days is still short.

**Do these checks in order. The first takes about 5 minutes.**

1. Open the Videos tab and cycle through every filter: Past Broadcasts, Highlights, Uploads, Clips. Then open Creator Dashboard → Content → Video Producer. You may be looking at one filter only.
2. Check who owns the Twitch login. If an advocate's personal account did the streaming, the files may sit there.
3. Look for local recordings. Ask each host and moderator to search OBS or Streamlabs output folders, the "Videos" folder, external disks and cloud backup. Search for `.mkv`, `.mp4` and `.flv` dated Tuesdays from June to September. The skill requires a local recording every episode, but you do not need to have followed that rule for a file to exist.
4. Check any recording from a guest call, a streaming studio tool or a screen recorder. Guests sometimes recorded their own side.
5. Collect clips. Clips are 60 seconds or less and are no substitute for episodes, but they give timestamps for what was worth keeping.
6. Ask regulars in your community if anyone recorded a session. This is a last resort. You would need their permission and a quality check before using anything.
7. Write down which episodes survive. Stop treating the rest as recoverable.

## 2. What to do with the course

Treat the course as a new product, not as a re-upload. The skill says raw live coding edits poorly into tutorials **[practitioner]**: cut answers, not hours.

- **For surviving episodes:** run the exposure review in section 6 before publishing anything. Then cut the answer segments and add chapters.
- **For missing episodes:** re-record the course topics as scripted lessons. Your repo history from each stream day is the outline. Use `samber/developer-relations-skills@technical-video-script` for scripts and `developer-tutorial` for the written steps. Use `samber/developer-relations-skills@devrel-youtube-channel` for titles, playlists and Shorts.
- **Guests:** if any episode had a guest or showed a viewer's code, you need written consent before reuse. Without it, drop that segment.
- **Disclosure:** if staff streamed on personal channels, check whether the employer was disclosed on screen, in the title and aloud (see section 6).

## 3. Refusals triggered

- **"Trust the platform to keep the recording."** This is what happened. Decline it.
- **Merged chat on Twitch.** Not requested, but it applies the moment you simulcast. Twitch's written rules ban it **[platform]**.
- **Reporting peak viewers or followers.** Decline. See the metrics in section 8.

## 4. Existing-show diagnosis

- **Format:** 14 consecutive weekly episodes with no season break. The skill recommends seasons of 6–8 episodes with a break of a few weeks to book guests and read metrics.
- **Platform:** a Twitch channel with about 180 followers, no Affiliate status and no durable archive.
- **Unknown:** average viewers, chatters, attributed signups, who moderated, and whether keys were exposed. I have no data for the last 6 episodes. Pull whatever Twitch Insights still shows. Do not guess.

## 5. Existence verdict and platform

**Keep the show.** Move from "weekly stream on a Twitch channel" to the default rung: a guest-led show on one home platform, plus 2–3 guest appearances on established developer streams. Prepare those appearances with `tech-podcast-interview-prep`.

Menu 1, ranked for you:

1. Guest on established developer streams
2. Guest-led show on one home platform
3. Launch-day streams
4. Solo build-along
5. Multistream variety show

Answers that moved the ranking:

- Your goal is a YouTube course, which favors a durable archive.
- Your Twitch audience is small.

**Recommended home platform: YouTube Live. This is an assumption.**

- The archive is searchable and not on a 7-day clock. Streams under 12 hours auto-archive **[platform]**.
- It needs a verified channel and no live restriction in the past 90 days **[platform]**.
- Keep Twitch only as a simulcast, and only if you can name a moderator for its chat. Under the Twitch Simulcasting Guidelines **[platform]**: no merged chat on the Twitch stream, a Twitch experience no worse than elsewhere, and no sending Twitch viewers to another platform. Moderators must never paste the YouTube link in Twitch chat.
- If no moderator exists, drop Twitch for now. At about 180 followers you lose little.
- Stay on Twitch as home only if the audience lives in Twitch culture. That would mean raids and chat-first community matter more than search. You have not told me that.
- Whichever you choose, record locally every time and own the account through a company login with 2FA.

## 6. Concept, cadence, moderation and safety

**Concept (assumption):** pair programming with a community or customer guest, building something real with Kestrel. Chat steers the build and spots bugs. The guest brings their audience. If you have no guests yet, run a solo live build of a real sample app until you do. Plan each episode as a goal plus a fallback task.

**Cadence:**

- Fix one weekday and hour. Keep Tuesday, since viewers learned it. Use the time zone where most signups or docs visitors sit and publish it on the platform schedule.
- Run seasons of 6–8 episodes with a break of a few weeks.
- Episodes per month = (host hours per week × 4) ÷ host hours per episode, rounded down. Below two a month, switch to the guest rung only.
- Host hours per episode ≈ stream length, plus the same again for prep, plus a few hours for clips and recap.
- Proposed dates, assuming one hour a week of capacity is available, which I have not confirmed:
  - Mon 2 Nov to Fri 27 Nov 2026: recover files, create company accounts, set moderation presets, line up three guests.
  - Tue 15 Dec 2026: announce the season, since the holiday gap makes the usual two-week lead too short. Re-post on Tue 5 Jan 2027.
  - Tue 12 Jan to Tue 2 Mar 2027: 8 episodes.
  - Early March 2027: read metrics, then book or stop.

**Moderation roster (owner: to confirm):** one named moderator per chat shown, and never the host. Give each moderator the rules, the escalation ladder from `developer-community-moderation`, and platform roles before episode 1. Set these before every episode: blocked terms, held-message filter, slow mode ready, followers- or subscribers-only mode ready, a one-click raid preset, and a link policy where only moderators post links.

**Live escalation:**

1. Spam or abuse: delete, time out or hide. The host never reads it aloud.
2. Raid flood: the moderator switches the preset on and the host keeps going.
3. Vulnerability posted in chat: delete, thank the reporter and move them to the security disclosure channel. Never reproduce it live. Note the timestamp, cut it from the archive, and find and delete viewer clips of that window.
4. Product bug or angry customer: acknowledge it, the moderator files the issue, and the host returns to the plan.

**Pre-flight checklist, every episode:**

- A demo account with scoped, low-limit keys. Rotate them after the stream. Shell history cleared. No customer data in any dashboard on screen.
- A separate OS user or browser profile with no saved passwords or personal tabs, and notifications off.
- A privacy scene ready before any credential screen. The encoder's settings window never in a captured scene.
- Stream key in a password manager, never in the run-of-show document. Prefer RTMPS.
- Local recording running. Audio checked first. Code font readable on a phone.
- Disclosure set. For staff on personal channels, name the employer in the title, on screen and aloud, and tick the branded-content box. The US FTC Endorsement Guides treat employment as a material connection **[law]**. Twitch exempts only "your own products", and an employee's case is unclear **[platform]**. Ticking costs no discovery.
- No copyrighted music or rebroadcast feeds. They get archives muted, claimed or restricted **[platform]**.
- Guests: a test call before the day, written consent to record and reuse their face, voice and code in clips, and a fallback segment if they do not show.
- Failure plan: a holding scene, a backup connection, and a line the moderator posts.

**Before you publish the old streams:** audit every surviving recording for exposed keys, tokens or customer data. If one is found, revoke and rotate it now, audit the archives, Highlights and viewer clips, and hand it to your security team as an incident.

## 7. Engagement recipe

Surfaces: the scheduled stream page, the platform schedule, the archive with chapters, clips, raids at the end, guest episodes on others' channels, the recap post, and a community space where regulars wait between episodes.

**Cadence:**

1. **Weeks -4 to -1 (Nov 2026):** company accounts, 2FA, roles. Moderation presets. Schedule the first three episodes. Invite the first three guests.
2. **Announcement (15 Dec):** post the season with dates and ask for questions.
3. **Each show week:** reminder on the day, stream, then recap and clips within 48 hours. On Twitch, raid an aligned channel at the end. Elsewhere, name a partner's next stream.
4. **Weekly, off-air:** watch and chat on 2–3 aligned developer streams. Never post your links there.
5. **End of season:** read metrics against the continue bar. Book the next guests or stop.

**Platform notes:**

- YouTube **[platform]**: publish time matters, subscribers get one go-live notification, and A/B title tests work on live archives. Announce days ahead with a title that names the problem solved.
- Twitch **[platform]**: live channels get priority over offline ones. Set a correct category and tags, use raids and guest swaps, and skip off-schedule streams.
- LinkedIn Live is not recommended now. It needs more than 150 followers, a 30-day-old account, and every live scheduled as an event **[platform]**.

Filled templates:

```
Pinned chat rules: Welcome. Ask anything about Kestrel; mods relay questions to [host].
Be kind; our code of conduct: [link].
Only mods post links. Found a security issue? Don't post it here: [disclosure channel].

Staff disclosure (title + on screen + aloud): "I work at [company]; this is our product."
```

## 8. Repurposing

- Drop a marker or note the timestamp at every answer worth keeping.
- Within 48 hours: export the archive if it lives on Twitch, add chapters, cut 2–4 clips, and link docs pages fixed after viewer questions.
- Hand the archive and clips to `devrel-youtube-channel`. It owns titles, Shorts and playlists.
- Record locally every episode. That file is your master copy, not the platform archive.

## 9. Metrics, continue bar and stop rule

- **Outcome:** signups from tagged links in descriptions, pinned messages and recaps. "How did you hear" answers naming the show. Docs or product fixes traced to viewer questions. If you cannot count signups by source today, set up tagged links first (`devrel-analytics`).
- **Show health:** average concurrent viewers, not peak. Unique chatters ÷ average viewers. Returning viewers across episodes. Archive watch time and average view duration, not public views. Since 24 August 2026 YouTube counts a view from the first frame of play **[platform]**, so do not compare public views across that date.
- **Baselines:** no published benchmark exists for developer streams. Set targets from episodes 1–3.
- **Continue bar,** written before episode 1: `episodes 6-8 vs 1-3: average viewers [up/flat], chat rate [up/flat]; at least [n] attributed signups or [n] docs fixes over the season`. Pick `n` from your goal and current signup volume. Never set or move it after seeing results.
- **Stop rule:** at season end, if you are below the bar, drop to the guest rung and say so.

## 10. Open questions

| Question | Owner |
|---|---|
| Who owns the Twitch login, and who has access? | to confirm |
| Did anyone record locally? What survives, and in which folders? | to confirm |
| Home platform: YouTube Live (assumed) or stay on Twitch? | to confirm |
| Named moderator for each chat shown | to confirm |
| Host and moderator hours per week, to compute episodes per month | to confirm |
| Did the 14 streams have guests or viewer code on screen? Is there written consent? | to confirm |
| Were keys, tokens or customer data ever shown on stream? | security team |
| Was the employer disclosed on personal channels? | to confirm |
| Goal for the course: reach, signups or onboarding? | marketing |
| Can you count signups by source today? | to confirm |
| Value of `n` in the continue bar | to confirm before episode 1 |