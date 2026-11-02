# Board slide: DevRel (draft for Monday)

I changed one thing from your plan: **"700k developers using us" is off the slide.** Downloads count installs, not people. CI runs, mirrors, and reinstalls inflate them, and one developer on both npm and PyPI is counted twice. A board member only has to ask "700k *people*?" and the slide stops being credible. The replacement below gives you a number that holds up.

## Slide

**Title: DevRel: reach is growing, and we now measure what it brings in**

| Layer | Metric | Value | How to read it |
|---|---|---|---|
| Reach | GitHub stars | 14.2k (cumulative) | Awareness signal, not usage |
| Reach | Package downloads, last month | 700k (410k npm + 290k PyPI) | Install events. Includes CI and mirrors, so not a user count |
| Community | Discord members | 6,800 (cumulative) | Joined, not active. 30-day active count to follow |
| Programs | Meetups run | 9 | Attendance and sign-up follow-through to follow |
| **Impact** | **Signups attributed to DevRel channels** | **~207 of 1,150 (18%)** | **Self-reported "how did you hear about us" (talks, blog, community). Likely a floor** |

**Headline line:** "About 1 in 5 signups says it found us through talks, blog, or community, roughly 207 people."

**Bottom strip: what we're changing**
- This is the first measured baseline. No targets existed before this quarter.
- Next report adds: active (not cumulative) community, downloads trend, and signup-to-activation by source.
- **Ask:** approve the metric set below as the official DevRel scorecard.

## Why the 18% is your strongest number

- It is the only metric tied to a business outcome.
- It is probably an undercount. People who saw a talk and later searched your name often tick "search".
- Say "self-reported" on the slide. It is more credible with a caveat than without.
- Don't call it "pipeline" or "revenue". You have no data for either.

## Proposed official metrics (for the "approve" ask)

1. **Signups from DevRel channels** (self-reported, with the 18% as baseline). *Primary.*
2. **Activated users from those signups.** Define "activated" with product, for example first successful API call.
3. **Monthly active community members** (posted or reacted in the last 30 days).
4. **Download trend**, month over month, presented as a trend and never as a headcount.

Stars, total Discord members, and meetup count stay as context rows only. Set targets after one more quarter of data. Inventing them now would be the same problem as the 700k.

## Speaker notes and likely questions

- **"Is 700k developers real?"** "No. Those are installs. We don't claim a user count from them, and we're building one from signups and activations."
- **"Why is only 18% attributed?"** "It's a free-text, self-reported question. It undercounts word-of-mouth and repeat exposure. We treat it as a floor."
- **"Is 14.2k stars good?"** Without a comparison, don't say it is. If you can name 2 or 3 comparable projects' stars, add one line. If not, say "awareness signal only".
- **"What did the 9 meetups produce?"** If you can't answer, say that is the gap being closed next quarter. Don't guess.
- **"What's the target?"** "We set it after this baseline quarter."

## Pull before Monday (about 1 to 2 hours)

1. Signups per month for the last 3 to 6 months. This lets you show whether the 18% is stable.
2. Discord 30-day active members (Discord's server insights has it).
3. npm and PyPI downloads for the last 3 months, to show a trend line instead of one point.
4. Attendance across the 9 meetups, if you tracked RSVPs.
5. Of the 207 attributed signups, how many activated. It's the single most persuasive addition if you can get it.

## Design notes

- Put the impact row first visually, with the large "~207 signups (18%)" figure. Keep the reach rows smaller.
- Use one chart at most: monthly downloads as a trend line.
- Add a footnote: "Cumulative figures as of Oct 2026. Downloads are install events, not unique users. Attribution is self-reported."

If you want, I can build this as a .pptx.