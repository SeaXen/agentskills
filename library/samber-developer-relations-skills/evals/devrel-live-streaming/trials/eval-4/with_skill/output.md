# Shipping Fridays: is it working, and what to report Monday

## Short answer

**I can't tell from those three numbers, and neither can your VP.** Peak viewers, follower count and public views are the three metrics this kind of review should not rest on. None of them says whether the show changes what the audience does.

- **Peak 34:** it is one minute of one episode. It says nothing about how many people stayed or whether anyone talked.
- **410 followers:** this is a running total. It doesn't show how many of them watch.
- **12.4k YouTube views:** YouTube has counted a view from the first frame of play since 24 August 2026 **[platform]**. That includes autoplay and people who clicked away. It works out to about 1,240 per episode, and no one knows how much of it was watched.
- **No benchmark exists** for developer streams. Any "34 is good" or "34 is bad" claim would be invented.

So don't report "it's working," and don't concede "it's failing." Report that the dashboard metrics can't decide it. Then offer a decision date with a pre-written bar.

## 1. Moves I'm declining

- **Judging the show on peak, followers or public views.** Use the metric tiers in section 9.
- **Setting the success bar after seeing the results.** That would be rigging the verdict in either direction. Section 9 explains how to write the bar fairly for a show that already exists.
- **Merged chat on the Twitch stream.** Twitch's Simulcasting Guidelines name it as banned **[platform]**.
- **Pasting the YouTube link in Twitch chat.** Twitch bans anything that sends Twitch viewers to another streaming platform **[platform]**.

## 2. Diagnosis of the existing show

| What you have | What it means | What's missing |
|---|---|---|
| Peak 34 (Twitch) | Best single minute | Average concurrent viewers, per episode |
| 410 followers | Cumulative audience | Returning viewers across episodes |
| 12.4k YT views | Starts of play, not attention | Archive watch time and average view duration |
| (nothing) | Chat activity | Unique chatters ÷ average viewers |
| (nothing) | Business outcome | Signups from tagged links, "how did you hear" answers, docs or product fixes from viewer questions |

Ten episodes is already more than one season. The skill recommends seasons of 6-8 episodes. Your VP is effectively holding a season-end review with no bar written in advance.

**Pull these before Monday.** Plan about 1-2 hours. Both platforms' native analytics should have them. Check that your Twitch Creator Dashboard and YouTube Studio show each one.

1. Average concurrent viewers per episode, Twitch and YouTube live separately.
2. Unique chatters per episode. Divide by average viewers.
3. Returning viewers across episodes.
4. YouTube archive watch time and average view duration.
5. Any signup that came from a show link. If you have no tagged links, say so plainly.
6. Docs or product fixes that came out of viewer questions. Search your notes and issue tracker.

## 3. Existence verdict: keep, shrink or kill?

I'm ranking the skill's "whether to host" options for you. You have a running show, so this is about which rung to stay on.

1. **Guest on 2-3 established developer streams.** Low effort, with a live audience that already trusts the host.
2. **Guest-led show on one home platform.** Your own audience, and each guest promotes their episode.
3. **Launch-day streams only.**
4. **Solo build-along.**
5. **Multistream variety show.** It splits your reach across chats nobody fully serves.

**Recommendation: don't kill it yet, and don't continue as is.** Move to rung 1 + 2 for one more short season (6 episodes). Make it guest-led, on one home platform, with a written bar. Run rung 1 in parallel.

I'm making these assumptions, because I haven't asked you the interview questions. Correct any that are wrong:

- The goal is reaching new developers or driving signups.
- You have no dedicated moderator today.
- The host spends roughly 3-4 hours a week on the show.

**Delete the hosting rungs entirely** (guest on others' streams, hand the recordings to the YouTube channel plan) in either of two cases. First, nobody can moderate during the slot. Second, host capacity is below one episode a fortnight. If either is true, tell your VP the show moves to guest appearances and recorded video, not that it's dead.

## 4. Home platform and simulcast rule

You currently run Twitch with a YouTube simulcast.

- **Test:** where do your chatters actually come from? Check the per-platform chatter counts from section 2.
- **If most chat is on YouTube,** make YouTube the home platform and drop Twitch. YouTube is the default for devtools because the archive is searchable later **[practitioner]**.
- **If most chat is on Twitch,** keep Twitch as home. Live channels are given priority over offline ones in Twitch ranking **[platform]**.
- **Keep the simulcast only if** each chat has its own named moderator who relays questions to the host. One host can't read two chats while coding.
- **Twitch rules apply** **[platform]**: no merged chat on the Twitch stream, a Twitch experience no worse than elsewhere, and no pointing Twitch viewers to YouTube.
- **Local recording:** record locally every episode. Twitch broadcasts are off by default and expire after 7, 14 or 60 days **[practitioner quoting Twitch help]**. Export the archives now if you haven't.

## 5. Concept and format

Three options, with a recommendation. In a one-pass reply I proceed with it, and you can overrule me.

1. **Pair programming with a community or customer guest.** Chat steers the build and spots bugs. It compounds, because each guest brings an audience. Effort is low-to-moderate.
2. **Viewer code or architecture review.** Viewers supply the material, with written consent. It compounds. Effort is low.
3. **Solo live build.** Chat debugs alongside the host. Effort is high and the show depends on one person.

**Recommended:** format 1 as the main show, with a format 2 episode when guests fall through. The question is whether Shipping Fridays currently works like a recorded video. If the show would run the same with chat switched off, record it instead of streaming it.

## 6. Season cadence

- Keep the Friday slot. Viewers have learned it. Publish it on the platform schedule.
- Run a **6-episode season**, then a break of a few weeks to book guests and read the metrics.
- Episodes per month = (host hours per week × 4) ÷ hours per episode. Hours per episode ≈ stream length + the same again for prep + a few hours for clips and recap. Below two a month, take the guest rung instead.

## 7. Moderation and pre-flight

- **One named moderator per chat shown, never the host.** Owner: to confirm.
- **Presets before every episode:** blocked terms, held-message filter, slow mode ready, followers-only ready, a one-click raid preset on Twitch, and only moderators post links.
- **Escalation:** delete spam. A moderator switches on the raid preset when hit. If someone posts a vulnerability, delete it, move the reporter to your security disclosure channel, and cut that window from the archive. Product bugs get filed by the moderator while the host returns to the plan.
- **Pre-flight checklist, every episode:**
  - Demo account with scoped, low-limit keys, rotated after.
  - Separate OS user or browser profile.
  - A privacy scene ready.
  - Stream key in a password manager.
  - Local recording running.
  - Employer disclosure on screen, in the title and aloud.
  - Branded-content box ticked.
  - Guest test call plus written consent to reuse.
  - A holding scene as the failure plan.
- **If a key or customer record was ever shown on an earlier episode,** revoke it, audit the archives, Highlights and viewer clips, and report it to security as an incident.

## 8. Engagement and repurposing

- **Before the season (weeks -4 to -1):** fix company logins with 2FA, set the moderation presets, schedule three episodes, invite three guests.
- **Two weeks out:** announce the season with dates and ask for questions.
- **Each show week:** reminder on the day, stream, raid an aligned channel at the end on Twitch, and publish the recap and clips within 48 hours.
- **Off-air weekly:** watch and chat on 2-3 aligned developer streams. Never post your links there.
- **Repurposing:** mark timestamps live. Within 48 hours, export the archive, add chapters, cut 2-4 clips of answers (not hours), and hand them to your YouTube channel plan.
- Use the templates in `references/templates.md` for the announcement, guest invite, pinned rules and recap.

## 9. Metrics, continue bar and stop rule

**Metric tiers**

- **Outcome:** signups from tagged links, "how did you hear" answers that name the show, docs or product fixes traced to viewer questions.
- **Show health:** average concurrent viewers (not peak), unique chatters ÷ average viewers, returning viewers, archive watch time and average view duration (not public views).
- **Diagnostic:** minutes to first chat message, clip views.

**Continue bar.** Write it now, against the last 3 episodes (episodes 8-10), and judge only the next season. Don't judge the past ten with a bar written after the fact. Use this form:

> Episodes 4-6 of the next season vs. episodes 1-3 of it: average viewers [up/flat], chat rate [up/flat]; at least [n] attributed signups or [n] docs fixes over the season.

Pick `n` from your goal and current signup volume. Never set or move it after seeing results. I haven't filled it in because I don't have your signup volume. Owner: to confirm.

**Stop rule.** At season end, below the bar means you drop to the guest rung (rung 1) and say so. That is the honest alternative to killing the show outright.

## What to report on Monday

Suggested text for your VP:

> **Status:** Shipping Fridays has run 10 episodes. The dashboard numbers (peak 34 viewers, 410 followers, 12.4k YouTube views) are the wrong tools for a go or no-go. Peak is a single minute, followers is a cumulative count, and YouTube counts a view on first play.
>
> **What I measured instead:** [average concurrent viewers, chatter rate, returning viewers, watch time, attributed signups: fill from section 2].
>
> **Proposal:** run one 6-episode season, guest-led, on one home platform ([Twitch/YouTube]) with a named moderator. The continue bar is written today: [fill in]. If the season misses it, we stop hosting and drop to guest appearances on established developer streams plus recorded video.
>
> **Cost:** [host hours per week] of host time and [moderator hours] per episode.

If the pulled data shows near-zero attributed signups, no chatters and flat average viewers, say that plainly. In that case the honest recommendation is the rung-1 fallback now, not another season. The numbers decide that, not me.

## Open questions

1. What's the goal: new developers, activation, retention, a launch moment, or recruiting?
2. Who can moderate during the Friday slot, and how many hours a week does the host have?
3. Does the Twitch channel have Affiliate status, and who owns each platform login?
4. Can you count signups by source today (tagged links, a "how did you hear" field, both, neither)?
5. Can the product be shown working live from a clean demo account?
6. Did any episode ever show a key, token or customer data on screen?

Two caveats. I didn't browse the platform help pages, so re-read the Twitch Simulcasting Guidelines and YouTube's view-count change before you cite them to your VP. The data pull in section 2 is yours to run, and I haven't seen any of those numbers.