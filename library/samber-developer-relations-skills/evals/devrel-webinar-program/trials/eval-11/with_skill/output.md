# Ask the Driftwood Engineers: season plan, platform, moderation, guest-slot prep

Nobody was available to answer the interview, so I inferred the answers. Overturn any assumption below and the plan changes where noted.

## Open decisions (assumed answers)

| # | Assumption | If wrong |
|---|---|---|
| 1 | The series' job is unblocking existing users and finding docs gaps. Driftwood has no free tier or open sales deals in the brief, so feature depth is the default. | A job of deal acceleration promotes a live demo and a customer story. |
| 2 | Driftwood has an active Discord with at least five questions from last month that the docs did not answer. | Without them, run the intake thread for a quarter and go live later. |
| 3 | Staff and engineers are US-based. The "rest in the US" split between East and West is unknown. | Staff in Asia make the Asia edition cheap and may change its slot. |
| 4 | Three or more engineers will join the rotation, and their managers agree to a cap of one session per engineer per month. | Fewer engineers means alternating Asia weeks (see the slot plan). |
| 5 | Viewers need no account to watch, so there is no registration and no registrant list. | Registration brings in the handoff and consent work. |

## Routing

Six Q&A episodes is not a webinar program. The webinar skill says to hand a series to the office-hours skill when every planned episode is a Q&A episode. The Q&A format is also the one a webinar series ranks lowest, because its value depends on a standing question backlog. I used the office-hours skill for structure and the webinar skill for replay, measurement and consent rules.

Add one live demo or engineer-conversation episode if you want a series that stays useful past the questions of the month.

## 1. Time zones: the current slot misses 40% of your users

Tuesday 11:00 ET is the wrong hour for India and Singapore.

| | Winter (EST, from 1 Nov 2026) | Summer (EDT, from 14 Mar 2027) |
|---|---|---|
| Tue 11:00 ET | 21:30 IST / **00:00 SGT (Wed)** | 20:30 IST / 23:00 SGT |
| US West | 08:00 PT, before the working day | 08:00 PT |

No single slot reaches both regions inside 09:00-18:00. The US window runs from 14:00 UTC and the Asian window ends by 10:00 UTC. The Asian users are 40%, above the 25% trigger, so they get their own live edition.

## 2. Charter (one page)

- **Series:** Ask the Driftwood Engineers.
- **Job:** unblock existing users. Secondary jobs are docs gaps and product signal.
- **Format:** a recorded 40-minute Q&A session with a permanent async intake in Discord.
- **Season:** 6 episodes, monthly, November to April. The season is the pilot.
  - Two editions per episode, 12 live sessions in total.
  - Check holidays before fixing dates, for example Diwali in early November and Lunar New Year in February.
- **Slots:**
  - **US edition:** Tuesday 11:00 ET, kept as is.
  - **Asia edition:** Tuesday 11:00 UTC, which is 16:30 IST and 19:00 SGT.
    - Singapore sits one hour outside its working day. Moving to 10:00 UTC fixes that (15:30 IST, 18:00 SGT) at the cost of a 05:00 ET start. Poll Discord on this before fixing it.
    - Fixing the Asia edition in UTC means US staff get a 06:00 EST start now and 07:00 EDT after 14 March. I fixed it this way because Asia has no clock change.
  - **If you move US West into the window,** move the US edition to 12:00 ET, which is 09:00 PT.
- **Staffing:** a host and a backup host. Engineers are capped at one session per month. A two-edition monthly cadence needs three engineers: one per edition plus a spare.
  - If you cannot staff 12 sessions, alternate instead. Asia gets live editions on episodes 2, 4 and 6, and the replay plus write-up on the others.
- **Scope card:** published before episode one (section 5).
- **Recording:** both editions are recorded. A named person reviews each recording for tokens and customer data before it goes public.
- **Outputs:** a write-up within 2 business days, docs tickets, and feedback records.
- **Data retention:** no registrant data exists. Delete the raw Discord question log after the write-up.
- **Demand bar** (self-set, no published benchmark exists):
  - Median distinct non-staff askers, live or async, at 3 or more per edition.
  - At least one merged docs fix or feedback record per 2 sessions.
  - A miss on either bar means dropping to the async thread for a quarter.
- **Operating bar:** no silent cancellation, no engineer over the cap, and write-ups on time in all but one session.
- **Continue bar** (reach, live attendance, returning share):
  - Baseline = median of episodes 1-2.
  - Fail if a metric is below baseline on two of episodes 3-6.
  - Stop after two seasons failing the job metric.
- **Interim read:** after episode 3.

## 3. Season plan (provisional beyond season one)

Replace the topics with your top-voted questions. Topics come from repeated community questions, not from a guess. These are placeholders I invented for an infrastructure-as-code tool.

| # | Month | Placeholder theme (title by the problem) | US edition | Asia edition | Replay |
|---|---|---|---|---|---|
| 1 | Nov | "My state is locked or corrupt, now what?" | Eng A | Eng B | Ungated, chaptered per question |
| 2 | Dec | "Drift between code and reality" | Eng B | Eng C | Same |
| 3 | Jan | "Modules and versioning without breaking everyone" | Eng C | Eng A | Same |
| 4 | Feb | "Plan/apply in CI without surprises" | Eng A | Eng B | Same |
| 5 | Mar | "Secrets, policy and review" | Eng B | Eng C | Same |
| 6 | Apr | "Importing and migrating existing infrastructure" | Eng C | Eng A | Same |

Each row needs a named backup engineer. Keep release-driven episodes under a third of the season.

## 4. Episode skeleton and timeline

- **Skeleton (40 min):**
  - 0-2 min: scope and recording notice.
  - 2-36 min: top-ranked questions first, under 4 minutes each, with a link posted for each.
  - 36-40 min: unanswered questions get a written follow-up date.
  - Turn on live captions.
  - An optional unrecorded after-show gives live a reason that more emails cannot.
- **Timeline per episode:**
  - **Intake:** keep it open permanently, not just the week before. A rolling thread keeps the backlog from emptying and lets Asia submit in its own day.
  - **T-72h:** nudge the thread.
  - **T-48h:** triage the queue and send the engineer the brief.
  - **T-24h:** cancel check.
  - **T+2 business days:** publish the write-up.
- **Triage buckets:** answer live, answer async, redirect, docs gap, log for product.
- **Intake form fields:** the question, what you tried, version, may we read it out, time zone and contact.
  - The time-zone field lets you route questions to the right edition.
  - Never ask for logs, state files or configs.
- **Intake thread rule:** pin "no state files, plan output or credentials". Those files carry secrets, which is my own domain judgement. Give moderators a redaction path.

## 5. Scope card (publish before episode one)

- **Bring:** questions in your own words, such as "my remote state lock is stuck after a CI timeout", "how do I split one module across two teams" and "is import safe on a 500-resource stack".
- **Not here:**
  - Account, billing and contract questions go to support.
  - Pricing goes to the sales contact. Answer only what the public docs say.
  - A suspected vulnerability goes to the private security channel, never live.
  - A reproducible bug goes to the issue tracker, and we will help you write it.
  - A feature request is logged live in the feedback record.
  - Debugging your own environment is off topic. Bring a minimal reproduction with secrets removed.

## 6. Which webinar platform

**Pick a one-way public video stream plus your existing Discord for questions.** I chose this because the community already lives in Discord, there is one session at a time, and viewing needs no login.

- The stream goes on a public video platform that works with no account. This also removes registration, so no registrant list needs a consent form.
- Questions arrive in Discord. The host reads the selected ones to the engineer.
- The stream carries the moderator's fallback line on its page.
- A managed virtual-venue platform fails the test. Booths, directories and breakout rooms add contract and data-review cost for a Q&A series with no sponsor deliverable.
- A broadcast tool with a built-in question queue is strictly dominated by the stream plus Discord. Use it only if procurement already bought it.
- Choose by category. The skill names no vendor, so any named product is your pick after you put the questions below to the vendor in writing:
  - Can a viewer watch with no account?
  - What is the concurrent-viewer ceiling, and what happens at it?
  - Can a stream be restarted without changing its address?
  - Who owns the recording, and can you delete it?
  - What captioning is built in, and can you feed in an external captioner?
  - Can a moderator delete a message and lock the space mid-session?
  - Where is attendee data held, and how long is chat kept?
  - Take the data-residency answers to counsel. The skill makes no legal call, and I made none for India or Singapore.
- **Rehearse once, on the real platform,** before episode one.

## 7. Chat moderation staffing

The skill gives no attendee-to-moderator ratio and publishes none, so I invented none. Staffing scales with concurrent sessions and failure stakes, not with headcount.

| Episode type | Staff, by name |
|---|---|
| Standard (one session at a time) | **One moderator per edition,** plus the host and the engineer. The moderator reads Discord, relays and drops questions, holds conduct, and posts the one line when anything breaks. |
| Bigger episode (the last one's moderator fell behind, or the episode cannot be re-run) | Add a **technical watcher** who only checks that the stream is up, audible and in sync, from a second device. |
| Bigger, with a sponsor or an audience with no other way to learn what is happening | Add a **host on the feed** who speaks on air when something fails. |

- **Never** make the engineer moderate their own chat. A presenting speaker cannot hold conduct in their own audience.
- **Never** leave the Asia edition's Discord open with nobody watching. If no moderator can cover Asia hours, close chat for that edition, take questions only through intake, and answer the rest in the write-up. An open space with no responder is the worst failure.
- **Failure drill:**
  - Publish one fallback line before the day, naming where to look.
  - Rehearse once the likeliest failure, the engineer's connection dropping. Agree the moderator's exact opening words.
  - Have the engineer record a local backup.
  - Say something in the first minute of any outage.
  - Warn engineers that incidental music in a demo can get a stream taken down.

## 8. Replay, handoff and consent

- **Replay:** ungated, chaptered by question, within 48 hours, with captions and a transcript.
  - Chaptered replays suit developers who learn from video and documentation.
  - The asker's question becomes the chapter title.
  - Cut two clips per episode if you want them.
  - Tag every link in the description by episode so you can count sign-ups from anonymous viewers.
- **No registration, no routing:** there is no list. Sales gets only what a viewer does themselves, such as a pricing question redirected to the sales contact.
  - Before any sales follow-up, get a named sales owner to sign a written rule.
  - Tell a hand-raiser that sales will contact them.
- **If you add registration later:** use an unticked marketing box, disclose engagement tracking and keep one named controller. Legal review owns the wording. The skill covers the EU, the UK and Canada, not India or Singapore, so that gap needs counsel.

## 9. Measurement

Log each edition separately.

| Signal | Note |
|---|---|
| Unique viewers and peak concurrent, per edition | Upper bound if only views are reported |
| 30-day replay views, all surfaces | Include the public copy |
| Distinct non-staff askers | Live and async |
| Questions answered, redirected, logged | Never drop one silently |
| Docs fixes merged, feedback records | The job metric |
| Returning-asker share | Baseline from episode 1-2 |
| Write-up and replay lag | Hours and days |

Never report registrations alone. Past episodes go into the log as the pilot baseline; you gave me no figures, so I left every cell empty. With no history, no population benchmark fits a no-registration Q&A, so use your first two episodes.

## 10. Guest slot on a partner's webinar next month

This is the podcast-interview-prep skill's territory. It needs four answers before any brief, so ask me for them:

1. Is the show live or recorded?
2. How long is it, and is it you alone, a moderator or a panel?
3. Who is the audience?
4. What topic did they book you for, and is there a pre-call?

With a month's notice, do all twelve prep steps. The highest-value ones, in order:

1. **Fix one sentence:** "We had X, and it worked at small scale, but Y broke, therefore Z." Add three messages, each with a claim, evidence and a so-what.
2. **Write your first answer** to stand alone if clipped. Put the point first and context after, within about 30 seconds.
3. **Write answers to the hard questions.** Concede something real before you bridge. Cover competitors and "who is this not for". Never say "no comment".
4. **Pick an angle only you can give:** something you built, broke or measured.
5. **Collect two or three stories** with real numbers and a mistake you made.
6. **Say your affiliation early.** Pitch only when invited, and keep it under 30 seconds. Name competitors fairly.
7. **Claim only published numbers.** The recording outlives the embargo.
8. **Say one liftable sentence** that names Driftwood next to its category and speaks a figure aloud.
9. **If live:** answers of 15 to 20 seconds, lead with the point and stop.
10. **If it is a panel:** headline in one sentence and jump in unasked.
11. **Prepare a recording-day card:** wired headphones, a local backup recording and a bullet card, not a script.
12. **Ask about the registrant list now.** The partner's list is not yours unless you are named on the form, and the partner then needs a signed arrangement. Do not plan to email it.
13. **Send the host** a bio, links and three quotes before publication.
14. **After publication,** post each sound bite with the link, set up a tagged URL to count sign-ups, and answer comments in the first week.