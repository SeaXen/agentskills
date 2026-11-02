# Live stream plan: Terraform drift CLI, 6-person startup

I read the skill and both reference files. I did not re-check the platform pages, so the platform rules below come from the skill's snapshot. Re-check them before you publish a schedule.

Where you didn't say, I assumed the following. Each is also listed under open questions:
- The goal is signups and activation.
- The CEO has about 4 hours a week.
- The CEO would host from a company-owned channel.

## 1. Refusals triggered

- **A 2-hour weekly show with the CEO alone, reading chat.** Nobody would act on spam, raids, or a secret posted in chat.
- **Spending first.** Gear doesn't decide whether this works. The moderator and the pre-flight checklist do.
- **Merged multistream.** I decline it from day one.
- **Twitch because Prime does it.** I'm not refusing Twitch outright. I'm declining it as the default for lack of a reason (section 4).

## 2. Existing-show diagnosis

No show exists, so there are no baselines yet. Episodes 1-3 set them.

## 3. Existence verdict

Menu 1, ranked for you:
1. Guest on established developer streams.
2. Guest-led show on one home platform.
3. Launch-day streams only.
4. Solo build-along on an advocate's channel.
5. Multistream variety show.

**Verdict: as requested, don't run it.** The skill says to delete every hosting rung when nobody can moderate during the slot or capacity is below one episode a fortnight. "Nobody else has time" fails the first test.

**Capacity check.**
- One episode costs the host about stream length, plus the same again for prep, plus a few hours for clips and a recap. A 2-hour episode is roughly 6-8 CEO hours.
- That is about 25-30 CEO hours a month at weekly cadence, plus a second person for 2 hours every week.
- With 4 CEO hours a week, the formula gives `(4 × 4) ÷ 7 ≈ 2` episodes a month.

**What I recommend instead**
- **Now:** the CEO guests on 2-3 established infra, DevOps and Terraform streams. Prepare each with `tech-podcast-interview-prep`. This needs no production and no moderator. Their audience already trusts the host, and you get a tagged link in each.
- **Season 1:** a guest-led show, **60 minutes, every other week**, once one named person moderates. Ninety minutes a fortnight from a teammate unlocks everything. That covers the 60-minute show plus setup, and one engineer who is already in the Slot anyway can do it.
- **Stretch:** go weekly or 2 hours only if season 1 beats its continue bar.

The CEO's real constraint is time, and a fortnightly show costs half of what a weekly one does. A show that stalls after episode 3 hurts more than one that runs fortnightly for a season.

## 4. Home platform and simulcast rule

**Recommendation: YouTube Live as home.**
- Terraform and drift problems are searched, and a YouTube archive gets found later. A Twitch archive expires after 7-60 days [practitioner quoting Twitch help], unless you export it.
- A new channel with no followers gets no help from Twitch's category browsing, and Affiliate status needs 50 followers and 3 average viewers [practitioner]. Prime's audience took years to build around a personality, not a product.
- If the CEO insists on Twitch, accept it, with these rules:
  - Record locally every time.
  - Export the archive inside the window.
  - Tick the branded-content box [platform].
  - Never paste a YouTube link in Twitch chat [platform].

**Simulcast rule: none in season 1.** Add LinkedIn Live later, with its own moderator. It fits platform and DevOps leads, but you need 150+ followers and a 30-day-old Page, and it is scheduled-events-only [platform]. No merged chat on any stream.

**Ownership.** Put the channel and any multistream service on a company login with 2FA and named editor roles. Don't use the CEO's personal account.

## 5. Concept and format

I considered three, from Menu 2:

| Concept | Format | Trade-off |
|---|---|---|
| **"Who drifted?"** (recommended) | Pair programming with a guest | Guest builds a small Terraform stack in a sandbox cloud account. Chat picks a manual console change to sneak in. The CLI hunts for it. Chat steers and spots bugs, and each guest brings their audience. Needs a guest each episode. |
| **Drift Clinic** | Viewer code review, submitted with consent | Chat supplies the material. Terraform state and plans contain secrets, so the sanitizing work is heavy. Better as an occasional episode. |
| **CEO solo live build** | Solo live build | Cheapest to book, but the channel and show tie to one person, and chat adds little. |

**Recommended: "Who drifted?"**, fortnightly, 60 minutes. This is an assumption; say if you prefer another.

Each episode has a goal and a fallback task: the goal is "find the planted drift", the fallback is "tour a real drift report". Getting stuck on air is fine [practitioner]. Demo-breaking risk goes to `developer-live-demo-design`.

**Guest sources:** platform engineers who already stream or post about Terraform, your design partners and customers, OpenTofu and Terraform community members.

## 6. Season cadence

- **Slot:** one fixed weekday and hour, in the time zone where most signups sit. I assumed Thursday; time to confirm.
- **Season 1 (6 episodes, fortnightly).** Dates assumed:
  - Dec 3 and Dec 17, 2026.
  - A holiday break.
  - Jan 14, Jan 28, Feb 11 and Feb 25, 2027.
- **Why December 3 and not "next month".** Four things have to be ready first:
  - a named moderator,
  - the sandbox and pre-flight checklist,
  - three booked guests,
  - a season announcement two weeks ahead.
  - A November 19 start is possible only if the moderator is named by about November 5. I'd rather not rush it.
- **Between seasons:** a few weeks to book guests and read metrics.
- **Length:** 60 minutes. Lengthen only while chat is still active at the end.

## 7. Moderation roster and pre-flight checklist

**Roster**
- **Host:** the CEO (owner: confirm).
- **Moderator:** one named teammate, never the host (owner: **to confirm**; this is the blocking question).
- **Backup:** a second name for absences.
- The moderator gets the rules, the escalation ladder from `developer-community-moderation`, and platform roles before episode 1.

**Preset before every episode** (names per platform in the platform-facts reference)
- Blocked terms.
- Held-message filter.
- Slow mode ready.
- Follower- or subscriber-only mode ready.
- A one-click raid preset where the platform has one.
- Links posted by moderators only.

**Live escalation**
1. Spam or abuse: delete or time out. The host never reads it aloud.
2. Raid flood: the moderator switches the preset on and the host keeps going.
3. Vulnerability in chat: delete, thank, send the reporter to your security disclosure channel. Never reproduce it live. Note the timestamp, cut it from the archive, and find and delete viewer clips of that window.
4. Product bug: acknowledge, the moderator files the issue, the host returns to the plan.

**Pre-flight checklist, every episode**
- **Throwaway cloud account** with scoped, low-limit credentials and a budget alarm. Rotate the credentials after the stream.
- **Terraform leaks secrets in ways other tools don't.** Check each before going live:
  - State files contain resource attributes in plain text.
  - `terraform plan` output can print secrets.
  - Environment variables hold cloud credentials.
  - The cloud console shows account IDs.
  - `~/.aws` and `.env` files.
  - Shell history.
  - Marking values sensitive isn't a reliable mask. Treat everything on screen as public.
- **Separate OS user or browser profile.** No saved passwords, no personal tabs, notifications off.
- **A privacy scene** ready to cut to before any credential screen. The encoder settings window never appears in a captured scene.
- **Stream key** in a password manager, never in the run-of-show doc. Prefer RTMPS.
- **Local recording** running. Audio checked first. Code font readable on a phone.
- **Disclosure** (section on the engagement recipe's templates): "I work at [company]; this is our product", in the title, on screen and aloud. Tick branded content when staff stream the employer's product, or when a guest is paid [platform]. In the US, the FTC treats employment as a material connection [law]; check your own market's rules.
- **No copyrighted music** or rebroadcast feeds [platform].
- **Guests:** a test call before the day, written consent to record and reuse their face, voice and code, and a fallback segment if they don't show.
- **Failure plan:** a holding scene, a backup connection, and a line the moderator posts.

If a key or customer record already appeared on a past stream, revoke it now, audit archives and clips, and hand it to your security owner as an incident.

## 8. Engagement recipe

**Home platform (YouTube Live) [platform]**
- Scheduled streams announced days ahead; subscribers get one go-live notification.
- A title that names the problem solved ("Find the drift someone hid in our Terraform").
- A/B title and thumbnail tests work on live archives.

**Cadence**
1. **Weeks -4 to -1 (November):** company accounts, 2FA, roles; name the moderator; set moderation presets; build the sandbox; book the first three guests and schedule the first three episodes.
2. **Week -2:** announce the season with dates. Ask for questions.
3. **Each show week:** reminder on the day, stream, then a recap and 2-4 clips within 48 hours.
4. **Weekly, off-air:** watch and chat on 2-3 aligned developer streams. Never post your links there.
5. **End of season:** read metrics against the continue bar; book the next guests or stop.

**Templates:** the season announcement, pinned chat rules, moderator brief, guest invitation, disclosure line and recap are in `references/templates.md`. For example:

```
Who drifted? is back: 6 live sessions, Thursdays at [time + zone], on YouTube.
Each session we pair with someone building on Terraform while chat picks the sneaky change.
Lineup: Dec 3 [guest] - [what they will build]. ...
Send the drift you want us to catch live: [link].
```

```
Welcome. Ask anything about Terraform drift; mods relay questions to [host].
Be kind; our code of conduct: [link].
Only mods post links. Found a security issue? Don't post it here: [disclosure channel].
```

## 9. Repurposing

- Drop a marker at every answer worth keeping.
- Within 48 hours:
  - export the archive,
  - add chapters,
  - cut 2-4 clips,
  - link any docs pages fixed after viewer questions.
- Cut answers, not hours. Raw live coding edits poorly into tutorials [practitioner].
- Hand the archive and clips to `devrel-youtube-channel`, which owns titles, Shorts and playlists.

## 10. Metrics, continue bar, stop rule

- **Outcome:** signups from tagged links in descriptions, pinned messages and recaps; "how did you hear" answers naming the show; docs or product fixes traced to viewer questions.
- **Show health:** average concurrent viewers (not peak); unique chatters ÷ average viewers; returning viewers; archive watch time and average view duration. Don't use public views: YouTube has counted a view from the first frame since 24 August 2026 [platform].
- **No benchmark exists** for developer streams. Set targets from episodes 1-3.
- **Continue bar, written before episode 1:**
  `episodes 4-6 vs 1-3: average viewers [up/flat], chat rate [up/flat]; at least [n] attributed signups or [n] docs fixes over the season`
  I need your current signup volume to choose `n`. Set it before episode 1 and never move it after seeing results.
- **Stop rule:** below the bar at season end, drop to guest appearances and say so.

## 11. What to buy

Gear is the smallest part of this. Order of spend: **audio, stability, then camera, then overlays.** Prices below are my rough estimates, not sourced figures.

**Buy**
- **A USB dynamic mic or a headset (roughly €60-150).** Bad audio loses viewers faster than bad video [practitioner].
- **A second monitor, if you don't have one.** One screen for the capture, one for chat and the encoder.
- **Wired ethernet or a USB-to-ethernet adapter.** A dropped connection kills a live demo.
- **Local disk space** for recordings.

**Optional**
- **A 1080p external webcam** (roughly €60-100). The laptop webcam is fine for a small face-in-corner.

**Free**
- **OBS** for encoding.
- **A password manager** for the stream key.

**Don't buy yet**
- A capture card, Stream Deck, studio lights, green screen, a second PC, or paid custom overlays.
- Revisit after the continue bar passes.

**Overlays: four plain OBS scenes, nothing branded and animated.**
1. **Starting soon**, kept under a minute or two for LinkedIn [platform].
2. **Live:** screen share, small camera, and a lower third with the show name, employer and a tagged link.
3. **Privacy / BRB**, to cut to before any credential screen.
4. **Holding**, for failures.

Make the code font large enough to read on a phone.

## 12. Open questions

1. **Who moderates?** One named teammate for about 90 minutes a fortnight. This decides whether the show happens. Owner: **to confirm**.
2. **How many hours a week does the CEO really have?** I assumed 4.
3. **What is the goal?** I assumed signups and activation. It could instead be launch awareness or recruiting.
4. **What time zone and slot?** I assumed Thursday; the time is open.
5. **Which accounts exist already,** and who owns each login?
6. **Can you count signups by source today** (tagged links, a "how did you hear" field)? This sets `n` for the continue bar.
7. **Can the CLI run on a clean sandbox cloud account,** with low-limit credentials? This is the pre-flight blocker.
8. **Is the CEO set on Twitch,** or open to YouTube as home?
9. **Which Terraform and OpenTofu streamers or customers could be the first three guests?**

**Next step:** answer 1 and 2. That fixes the verdict, the slot and the first date.