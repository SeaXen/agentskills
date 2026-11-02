# Ferrolite live streaming: launch plan and Q1 2027 schedule

I answered in one pass, so every gap below is a stated assumption. None of this has been checked against your real numbers. I also didn't browse live platform pages. Platform facts come from the skill's reference file, so re-read the platform pages it lists before the December setup week.

**Assumptions to confirm**
- "Next quarter" means Q1 2027 (Jan 1 to Mar 31).
- You are the only host, and no moderator is named yet.
- Your goal is activating signups, not raw reach.
- Time zone: 17:00 CET (11:00 ET), because most Postgres-buying teams you'd reach work in EU or US hours. Please check this against where your signups and docs visitors sit.
- Ferrolite holds the YouTube channel, the LinkedIn Page and the X account. Twitch is unconfirmed.
- You can show Ferrolite working from a clean demo account.

## 1. Refusals triggered

| Your plan | Verdict | Why |
|---|---|---|
| Merged Restream chat overlay on screen | Declined | Twitch's written rules ban combining other platforms' activity, merged chat included, on the Twitch stream [platform]. Twitch's CEO said in Feb 2026 that enforcement would pause [practitioner]; follow the written rule. Without Twitch, the overlay is allowed but still needs a moderator. |
| "Answer everyone from one window" while hosting | Declined | One host can't read four chats while talking and coding, so questions go unanswered. |
| Same stream to LinkedIn company page and your profile | Impossible | A LinkedIn Live goes to one destination: event, profile or Page. A member can't stream to a Page [platform]. Stream to the Page and reshare from your profile. |
| Hosting alone | Declined | Nobody acts on spam, raids or a vulnerability posted in chat. LinkedIn advises at least one dedicated moderator [platform]. |
| 3 streams a week, 2 hours each, from one advocate | Declined | See section 5. It is a fixed daily-style promise from one person; burnout ends the show. |
| Go live on LinkedIn at any time | Declined | Every LinkedIn Live is a scheduled event, and LinkedIn advises at least two weeks to gather attendees [platform]. |
| Peak viewers as the success metric | Declined | Peak is one minute. Section 9 has the metrics. |

## 2. Existing-show diagnosis

None. This is a new show, so baselines come from episodes 1-3.

## 3. Existence verdict (Menu 1, ranked for you)

Ranked by value per team hour, starting from zero:

1. Guest on established developer streams
2. Guest-led show on one home platform
3. Launch-day streams only
4. Solo build-along on an advocate's channel
5. Multistream variety show

Your plan is rung 5, the costliest and the lowest in value.

**Recommendation:** run rung 2 and rung 1 together.
- Run one guest-led show for one season on one home platform.
- Appear as a guest on 2-3 established Postgres and developer streams during the season. Prepare each with `tech-podcast-interview-prep`.

**Gate:** hosting is deleted if nobody can moderate the slot, or if capacity is below one episode a fortnight. In that case, take only the guest rung and hand recorded video to `devrel-youtube-channel`. A show is a standing job, so a moderator is a precondition.

**What moved the ranking:**
- You are solo and have no named moderator. This pushes hosting below the guest rung until a moderator exists.
- A single host account holds the logins. The solo build-along would tie the channel to you, so the company account must own the show.
- A buyer or architect audience would promote LinkedIn Live. That's why LinkedIn is stage 2 below.

## 4. Home platform and simulcast rule

**Home: YouTube Live.**
- It is the default for devtools companies, and the archive is searchable later.
- Streams under 12 hours auto-archive [platform]. Dual stream is on by default; the vertical copy runs in the Shorts feed with no clickable links [platform]. Turn it off for code shows, or accept that.

**Simulcast rule:** add a destination only when it has its own named moderator who relays questions to you.

**Staged route to what you wanted:**

| Stage | When | Destination | Condition |
|---|---|---|---|
| 1 | Episodes 1-3 (Jan 13-27) | YouTube only | Moderator named, presets set. Native YouTube streaming, no Restream. |
| 2 | Episode 4 onward (Feb 3) | + LinkedIn Live on the **company Page** | A second moderator for the LinkedIn chat. Page has 150+ followers and is 30+ days old [platform]. Event created at least 2 weeks ahead, so by Jan 20. Restream or custom RTMP is fine; the LinkedIn partner tool or custom RTMP is accepted [platform]. |
| 3 | Only if evidence | Twitch | Only if your audience watches there. A moderator is needed, no merged chat on screen, and nothing sending Twitch viewers to YouTube. Don't relay YouTube links in Twitch chat. |
| Never as a weekly | | X | Encoder streaming needs Premium [practitioner]. Use it for launch-day reaction only. |

**Restream account:** if you use it in stage 2, put it on a company login with 2FA. It holds every destination's credentials.

**LinkedIn rules to respect**
- No selling or promotional streams, and no pre-recorded content as "live" [platform].
- Links in comments aren't clickable [platform].
- The starting screen must be under 1-2 minutes [platform].

## 5. Capacity check (why not 3 × 2 h a week)

Host hours per episode ≈ stream length + the same again for prep + about 3 h for clips and recap.

| Plan | Per episode | Per week | Moderation |
|---|---|---|---|
| Yours: 3 × 2 h | 2 + 2 + 3 = 7 h | **21 h** | 6 h/week per chat shown, so 18+ h/week for 3 chats, none of it you |
| Recommended: 1 × 1 h | 1 + 1 + 3 = 5 h | 5 h | 1 h/week per chat shown |

Episodes per month = (host hours a week × 4) ÷ hours per episode.
- At 5 h a week, that is 4 a month.
- At the full 21 h, that is 12 a month. It would take over half your working week, with nothing left for docs, guests or community.

Please tell me how many hours a week you can really give. That number sets the cadence.

## 6. Concept and format (assumed, since you didn't pick)

Options considered:
- **A. Pair programming with a community or customer guest.** Chat steers the build and spots bugs. The guest brings their audience.
- **B. Viewer schema or query review ("slow query clinic").** Chat supplies the material. It fits managed Postgres well and needs written consent per submission.
- **C. Solo live build.** The most effort, and it only works while the series runs.

**Recommended: A as the base, B every third episode.**

**Episode shape:** a goal plus a fallback task. Getting stuck is part of the show [practitioner].

**Rules**
- Never review a viewer's private repo on air without written consent.
- Never show their secrets or connection strings.

Show name: `[to confirm]`.

## 7. Season cadence

**Slot:** Wednesday, 17:00 CET (assumed), published on the YouTube schedule.

**Length:** 60 minutes. Lengthen to 90 only if chat is still active at the end. Keep it fixed so viewers can plan.

**Season 1: 8 episodes** (seasons run 6-8 episodes with a break between).

| # | Date | Format | Guest | Notes |
|---|---|---|---|---|
| 0 | Wed Jan 6 | Private rehearsal | none | Run with the moderator. Check the presets, the privacy scene and local recording. |
| 1 | Wed Jan 13 | Pair programming | `[guest 1: to confirm]` | YouTube only |
| 2 | Wed Jan 20 | Pair programming | `[guest 2]` | Create the LinkedIn event for Feb 3 today |
| 3 | Wed Jan 27 | Viewer query review | viewers (consented) | Baseline episode 3 |
| 4 | Wed Feb 3 | Pair programming | `[guest 3]` | LinkedIn Page simulcast starts if its moderator exists |
| 5 | Wed Feb 10 | Pair programming | `[guest 4]` | |
| 6 | Wed Feb 17 | Viewer schema review | viewers | |
| 7 | Wed Feb 24 | Pair programming | `[guest 5]` | |
| 8 | Wed Mar 3 | Pair programming | `[guest 6]` | Season finale |
| break | Mar 10-24 | none | none | Book season 2 guests and read metrics against the bar |
| S2 | Wed Mar 31 | | | Only if the continue bar passes |

**Mondays and Fridays:** no streams. Use them for the guest-appearance rung. Aim for about one appearance on another developer's stream every two weeks, plus clips and recaps.

**Guest sources, to confirm:** customers building on Ferrolite, Postgres extension authors, community members from your docs or forum. I won't name anyone.

## 8. Moderation roster and pre-flight checklist

**Roster**

| Chat | Moderator | Backup |
|---|---|---|
| YouTube | `owner: to confirm` | `to confirm` |
| LinkedIn Page (from Feb 3) | `owner: to confirm`, a different person | `to confirm` |

The host never moderates. Give moderators the rules and platform roles before episode 0, and the escalation ladder from `developer-community-moderation`.

**Presets before every episode**
- YouTube: blocked words, "hold potentially inappropriate messages" (Basic or Strict), slow mode ready, subscribers-only chat ready, link policy where only moderators post links [platform].
- LinkedIn: moderator can delete, report and mute commenters. Mute covers the live and its replays [platform]. Use a separate device [platform].

**Live escalation**
1. Spam or abuse: delete, time out or hide. You never read it aloud.
2. Raid flood: the moderator switches the preset on and you keep going.
3. Vulnerability posted in chat: delete, thank the reporter, and move them to the security disclosure channel. Never reproduce it live. Note the timestamp, cut it from the archive, and find and delete viewer clips of that window.
4. Product bug or angry customer: acknowledge it, the moderator files the issue with the link, and you return to the plan.

**Pre-flight checklist, every episode**
- Demo cluster with scoped, low-limit credentials. Rotate them after the stream. This covers connection strings, tokens and API keys.
- No customer data in any dashboard on screen. Clear shell history.
- Separate OS user or browser profile: no saved passwords, no personal tabs, notifications off.
- A privacy scene ready before any credential or console screen. The encoder settings window is never in a captured scene.
- Stream key in a password manager, never in the run-of-show doc. Prefer RTMPS.
- Local recording running. Audio checked first. Code font readable on a phone.
- **Disclosure:** the show runs on the Ferrolite company channel, so it is your own product [platform]. Still name the employer on screen, in the title and aloud. If you ever stream from a personal channel, the US FTC Endorsement Guides treat employment as a material connection to disclose [law], and you also tick the branded-content box [platform].
- No copyrighted music or rebroadcast feeds. They cause restrictions or muted archives [platform].
- **Guests:** a test call before the day, written consent to record and reuse their face, voice and code in clips, and a fallback segment if they don't show.
- **Failure plan:** a holding scene, a backup connection, and a line the moderator posts. A LinkedIn Live must start between 15 minutes before and 2 hours after its scheduled time [platform].

## 9. Engagement recipe and dated cadence

**Dated cadence**

| When | Action |
|---|---|
| Dec 7-11 | Company logins and 2FA for YouTube, LinkedIn Page, Restream and X. Named editor roles. Check YouTube live eligibility: verified channel, no live restriction in the past 90 days [platform]. Check LinkedIn Page eligibility. Name the moderator. |
| Dec 14-18 | Schedule episodes 1-3 as YouTube scheduled streams. Invite guests 1-3. Moderation presets set. |
| Dec 15 | **Announce the season** on every channel. This falls before the holiday break and more than 2 weeks before episode 1. Open a questions form. |
| Jan 4 | Schedule the remaining YouTube streams. Reminder post. |
| Jan 6 | Rehearsal (episode 0). |
| Each show week | Reminder post on the day. Stream. Recap and clips within 48 hours. |
| Jan 20 | Create the LinkedIn Page event for Feb 3, and one per episode afterwards at least 2 weeks ahead. Invite your connections. |
| Weekly, off-air | Watch and chat on 2-3 aligned developer streams. Never post your links there. |
| Mar 10-24 | Season break: read metrics, book guests. |

**What each platform rewards**
- **YouTube** [platform]:
  - Publish time matters for Live and Premieres.
  - Subscribers get one go-live notification.
  - A/B title and thumbnail tests work on live archives.
  - Do more: scheduled streams announced days ahead, and a title that names the problem solved.
- **LinkedIn** [platform]:
  - Attendees get reminders 3 days and 15 minutes before, and a notification at start.
  - A subset of followers likely to watch also gets one.
  - Do more: two weeks of event promotion and connection invites.
  - Do less: promotional content.
- Ignore "stream 3+ hours to rank" and "active chat gets boosted"; those are folklore [practitioner].

**Template: season announcement** (fill the brackets)

```
[Show name] is back: 8 live sessions, Wednesdays at 17:00 CET, on YouTube.
Each week we pair-program with someone building on managed Postgres,
and every third week we review your schema or slow query.
Lineup: Jan 13 [guest 1] - [what they will build]. Jan 20 [guest 2] ...
Send the question you want answered live: [link].
I work at Ferrolite; this is our product.
```

**Template: pinned chat rules**

```
Welcome. Ask anything about [topic]; mods relay questions to [host].
Be kind; our code of conduct: [link].
Only mods post links. Found a security issue? Don't post it here: [disclosure channel].
```

## 10. Repurposing

- Drop a marker at every answer worth keeping.
- Within 48 hours, add chapters and cut 2-4 clips. Link any docs page you fixed after viewer questions. Raw live coding edits poorly into tutorials [practitioner]; cut answers, not hours.
- The YouTube archive is automatic for streams under 12 hours [platform]. Record locally anyway. If Twitch is ever added, export before expiry; past broadcasts are off by default and expire after 7, 14 or 60 days [practitioner quoting Twitch help].
- Hand the archive and clips to `devrel-youtube-channel`, which owns titles, Shorts and playlists.
- Do not publish raw LinkedIn replays as a substitute. Teach, don't pitch.

## 11. Metrics, continue bar and stop rule

**Outcome**
- Signups from tagged links in descriptions, the pinned message and recaps.
- "How did you hear about us" answers naming the show.
- Docs or product fixes traced to viewer questions.

**Show health**
- Average concurrent viewers, not peak.
- Unique chatters ÷ average viewers.
- Returning viewers across episodes.
- Archive watch time and average view duration. Don't use public views: since 24 August 2026 YouTube counts a view the moment any video starts to play [platform], so never compare public views across that date.

**Diagnostic**
- LinkedIn attendee-to-viewer rate.
- Minutes to first chat message.
- Clip views.

**Baselines:** episodes 1-3. No published benchmark exists for developer streams, so don't import one.

**Continue bar** (written now, before episode 1, never moved after seeing results):

`episodes 6-8 vs 1-3: average viewers up or flat, chat rate up or flat; at least 30 attributed signups or 3 docs fixes over the season`

The 30 is a proposed placeholder. It is about 0.4% of two months of your ~4k signups a month. Please confirm or change it before Jan 6. It depends on whether you can count signups by source today.

**Stop rule:** at season end, below the bar, drop to the guest rung and say so publicly.

**Pass test:** the home platform, slot, moderator and continue bar each need a named owner. Every one currently reads `owner: to confirm`.

## 12. Open questions

1. How many hours a week can you give the show? This sets the cadence in section 5.
2. Who is the YouTube moderator, and who is the LinkedIn moderator from Feb 3?
3. Does the time zone and slot fit where your signups and docs visitors sit?
4. Which platforms does Ferrolite already hold accounts on, who owns each login, and what are the follower counts? Does the LinkedIn Page have 150+ followers? Is there a Twitch channel?
5. Who are the first 3 guests?
6. Can you count signups by source today (tagged links, a "how did you hear" field, both, neither)? That sets whether 30 is a sensible bar.
7. Is a Ferrolite release planned in Q1? If so, add a release-day stream and promote the launch-day rung.
8. Can the product be shown working live from a clean demo account?
9. Which developers or Postgres streamers already build with Ferrolite?