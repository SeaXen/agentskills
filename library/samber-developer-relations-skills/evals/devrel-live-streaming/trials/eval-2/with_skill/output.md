# Quarry v3 launch stream: run-of-show (LinkedIn Live, Thu 2026-11-05)

I didn't re-read the platform pages live. Platform facts come from the skill's reference file, dated 2026, so check the LinkedIn Live pages before Thursday. Gaps I filled are marked **assumption**.

## 0. Do this first (today, Sat 31 Oct)

1. Create the LinkedIn Live event on the company Page. It's the only way to go live, and the event is what notifies people.
2. Link the event in the launch post draft.
3. Name the moderator and a backup (section 6).
4. Run the Page eligibility check: 150+ followers and 30+ days old, which you should meet at 9,000 followers.

## 1. Moves declined

| Your ask | Why not | Instead |
|---|---|---|
| "Just hit go live, 9,000 followers get notified" | Since 22 June 2026 every LinkedIn Live is a scheduled event. At start, event attendees are notified, plus only a subset of likely-viewing followers, not all 9,000 [platform]. | Create the event today. Invite connections and drive RSVPs from the launch post. You have 5 days, not the 2 weeks LinkedIn advises [platform], so expect fewer attendees. |
| Drop a 30% code in the comments with a link | Links in live comments render as plain text [platform], and LinkedIn discourages selling and promotional streams [platform]. | Put the code in the launch post and the recap post, both with tagged links. Don't mention the code on air. |
| Show the pricing page | A pricing walkthrough reads as a pitch, which is the thing LinkedIn discourages. | One 90-second beat, only to explain what's open source versus cloud. No discount talk. |
| VP Eng goes live on their own profile | A member streams as their profile. A Page admin streams as the Page [platform]. A stream goes to one destination only. | Stream as the Page, with the VP Eng as host. Reshare from their profile afterwards. |
| Host alone, reading chat | LinkedIn advises at least one dedicated moderator on a separate device [platform]. | Moderator in section 6. |

## 2. Verdict

This is a **launch-day stream, one-off**. A launch date promotes this rung, and it buys questions answered while attention peaks. It is not a standing show. A recurring show needs a moderator and capacity of at least 2 episodes a month, and I haven't assumed either.

- **Platform:** LinkedIn only, no simulcast. **Assumption:** your launch audience is the Page's followers. A second platform needs its own moderator.
- **Format:** release-day stream, building with the new feature. Chat's role is asking what the docs missed.

## 3. Timing

The stream runs **10:15–10:35 CET** (CET is in effect on 5 Nov). The launch post goes out at 10:00 and links the event.

- Attendees get a 15-minute reminder at 10:00 [platform].
- A LinkedIn Live must start between 15 minutes before and 2 hours after its scheduled time [platform]. That gives you slack if the post slips.
- LinkedIn's minimum is about 15 minutes and the maximum is 4 hours [platform], so 20 minutes fits.

## 4. Run-of-show (20 minutes, hard stop)

Fill the `[bracketed]` items with real v3 facts. I haven't invented any features.

| Clock | Min | Segment | Owner | Notes |
|---|---|---|---|---|
| 09:30 | | Tech check | Host + moderator | Section 5. Start the local recording. |
| 10:00 | | Launch post live | CMO | Links the event. Carries the 30% code and a tagged link. |
| 10:10 | | Holding scene on | Moderator | Starting screen. |
| 10:15 | 0:00–1:00 | Welcome | VP Eng | Starting screen under 1–2 minutes [platform]. Say who they are, what v3 is, and what the next 20 minutes cover. |
| 10:16 | 1:00–3:00 | v3 in 3 lines | VP Eng | Headline changes: `[feature 1]`, `[feature 2]`, `[feature 3]`. No slides. |
| 10:18 | 3:00–11:00 | Live demo | VP Eng | One goal: `[e.g. upgrade a v2 index to v3 and run a query that uses feature 1]`. Fallback task in the box below. |
| 10:26 | 11:00–12:30 | Open source vs cloud | VP Eng | Show the pricing page for 90 seconds, logged out. Say what is free and self-hosted, and what the cloud adds. No numbers beyond what the page shows, and no code. |
| 10:27 | 12:30–17:30 | Chat Q&A | VP Eng + moderator | Moderator relays: "@host Q from [user]: [question]". Questions are collected in the launch post replies. |
| 10:32 | 17:30–19:00 | Wrap | VP Eng | Say where to get v3 and the upgrade guide. Say the offer is in the launch post, one sentence, no pitch. |
| 10:34 | 19:00–20:00 | Close | VP Eng | Thank the audience, then end the stream. |
| 10:35 | | Stream off | Host | Don't run over. |

**Fallback if the demo breaks:** switch to `[pre-written query set / second demo index]` and keep talking. Move to Q&A by minute 9 at the latest. Detailed demo fallbacks and reset belong to `developer-live-demo-design`.

**Chat rules, pinned by the moderator at start:**

```
Welcome. Ask anything about Quarry v3; mods relay questions to [host].
Be kind; our code of conduct: [link].
Only mods post links. Found a security issue? Don't post it here: [disclosure channel].
```

## 5. Pre-flight checklist (Thu 09:30)

- Demo account on the cloud tier, with scoped, low-limit keys. Rotate them after the stream.
- Separate browser profile or OS user: no saved passwords, no personal tabs, notifications off.
- No customer data in any dashboard on screen. The pricing page is shown logged out, so no billing or admin pages.
- Shell history cleared. A privacy scene ready before any credential screen. The encoder settings window is never in a captured scene.
- LinkedIn has no in-app camera [platform], so use a partner tool or a custom RTMP stream. Keep the stream key in a password manager, not in this run-of-show.
- Local recording running. Check audio first. Make the code font readable on a phone.
- Enable English auto-captions in the tool before going live [platform].
- No copyrighted music.
- Failure plan: a backup connection, and a line the moderator posts if the stream drops: "Technical issue, we're back at `[time]`. v3 notes: `[link]`."

## 6. Roster

| Role | Owner |
|---|---|
| Host | VP Eng |
| Moderator (separate device, chat only) | to confirm |
| Backup moderator | to confirm |
| Page admin who creates and starts the event | to confirm |
| Offer and code owner | CMO |

Moderator duties:

- Delete spam and abuse. The host never reads it aloud.
- If a vulnerability is posted: delete it, thank the reporter, and send them to the disclosure channel. Note the timestamp and cut it from the archive.
- File product bugs as issues and relay questions to the host.
- Note timestamps of good answers for clips.

## 7. Engagement

| When | Action |
|---|---|
| Today | Create the event. Invite connections. |
| Mon 2 Nov | Teaser post for the event. Ask for questions. |
| Wed 4 Nov | Reminder post. Brief the moderator. |
| Thu 10:00 | Launch post, with event link. |
| Thu 10:15 | Stream. |
| Within 48 h | Recap post and clips. |

**Event description (draft):**

```
Live: [VP name] walks through what's new in Quarry v3, building with [feature] on [technology].
You'll leave knowing how to [one concrete outcome: upgrade / try the cloud tier].
Ask questions in the comments during the stream; we answer them on air.
[VP name], VP Engineering at [company].
```

## 8. After the stream

Within 48 hours:

1. Export the recording, add chapters, and cut 2–4 clips (answers, not hours).
2. Post the recap with the tagged links. The 30% code goes here too, with its end date.
3. Hand the archive to `devrel-youtube-channel`.

**Recap post:**

```
Quarry v3 live: what we built.
Questions from chat we answered: [Q1 -> chapter link], [Q2 -> docs page we fixed].
Full replay: [link]. Try it: [tagged link]. Offer code: [code], valid until [date].
```

## 9. Metrics, continue bar and stop rule

- **Outcome:** signups and code redemptions from tagged links (launch post, recap, event description), plus any docs fixes traced to viewer questions.
- **Show health:** average concurrent viewers, not peak. Unique chatters ÷ average viewers. Attendee-to-viewer rate.
- **Diagnostic:** minutes to first chat message, and clip views.
- **No benchmark exists for developer streams.** Set targets from this first stream.
- **Continue bar (write the numbers before Thursday):** a second stream happens only if `[n]` attributed signups or `[n]` docs fixes come out of this one, and average viewers hit `[n]`. Owner: to confirm.
- **Stop rule:** below the bar, the next launch gets a recorded video plus guest slots on other developers' streams. Don't build a show.

## 10. Open questions

1. Who moderates, and who is the backup?
2. Can the Page admin start the event from an encoder (partner tool or RTMP)? Who holds that login, with 2FA?
3. What are the three v3 headline features, and which demo goal do you want?
4. Does the CMO accept putting the 30% code in the launch and recap posts instead of the stream? What are its terms and end date?
5. Do you have signup source tagging today (UTM links, a "how did you hear" field)?
6. **Assumption:** the audience is mostly the Page's followers. If you want developers on Twitch or YouTube, that's a second phase with its own moderator and simulcast rules.