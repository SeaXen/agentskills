**Do first (10 min):** pull attendee and replay-view counts by region for past episodes. The slot decision below depends on that data. I don't have it.

## 1. Season format and timing

**Time math.** Your current slot is 11am ET on Tuesday.

| Season part | 11am ET is | India | Singapore |
|---|---|---|---|
| Until 1 Nov 2026 (EDT) | 15:00 UTC | 8:30pm | 11pm |
| From 1 Nov (EST) | 16:00 UTC | 9:30pm | **midnight** |

- The 40% from India and Singapore is already live-hostile, and from November it gets worse. Singapore is the worst hit.
- India and Singapore are 2.5h apart, and neither has DST. The US has DST, so a fixed ET slot drifts for them twice a year.
- No single slot works for US West, India and Singapore at once.

**Recommendation: alternate two slots (A-B-A-B-A-B).**

| Slot | Time (EST) | Time (EDT) | India | Singapore | US West |
|---|---|---|---|---|---|
| A | Tue 11am ET (keep) | same | 9:30pm | midnight | 8am |
| B | Tue 13:00 UTC | 9am | 6:30pm | 9pm | 5am-6am (replay only) |

- Fix B in UTC, not ET, so APAC time stays stable. Rebase it when US DST changes on 8 Mar 2027.
- Slot B is the only one that gives Singapore a human hour. US East still works at 8-9am.
- Each audience gets 3 live-friendly episodes. The other 3 are replay plus async.
- Test on the numbers from your first step. If India alone is the bulk of the 40%, a single 8am ET slot may beat alternating.
- Check holidays before fixing dates: Diwali (about 8 Nov 2026), US Thanksgiving (26 Nov), the late-Dec dead zone, and Lunar New Year (about 6 Feb 2027).

**Make Discord the equalizer.** Since questions are collected in Discord anyway, give people who can't attend live a way to take part.
1. Open one forum thread per episode, 7 days before. Use reactions as votes.
2. Close submissions 48h before. Engineers triage the top 10-12 questions. Leave about 15 min of the hour for live questions.
3. Credit each asker by handle on air, with their consent.
4. Post a written answer in the thread within 24h for every question you didn't reach, plus the timestamped replay. This is what makes the A-B-A-B plan fair to APAC.
5. Run a 3-question warm-up at the start and the "no questions left" case at the end. A host who is not an engineer keeps pace.

**One primary outcome.** Pick one before the season starts. I suggest community and content: Discord questions per episode, replay views, and engineer hours spent. If pipeline matters more, add registration (see platform below). One outcome beats four.

## 2. Platform pick

**Pick: StreamYard (or a similar studio tool) streaming to YouTube Live. Discord remains the question intake.**

Why:
- Developers rarely register for webinars. Your questions already live in Discord. Registration friction costs you attendance for no gain.
- YouTube gives an instant public replay, search discoverability, built-in moderation tools and unlimited scale. The replay is your APAC product.
- A studio tool gives backstage chat for host, producer and engineers, on-screen question cards, and clean scene switching.

Alternatives, ranked:
1. **Zoom Webinars or Livestorm.** Use only if you need registration and email capture for sales (enterprise buyers, lead routing). Cost is paid seats and lower reach.
2. **Discord Stage.** Free, and the audience is already there. Fine for small episodes where people talk live. It has no public replay and weak discoverability.
3. **Multistream (YouTube + LinkedIn + Twitch).** Skip unless there's a reason. It splits chat and doubles moderation.

Caveats:
- Verify current pricing and viewer limits yourself. I'm not quoting them.
- You lose an email list. Replace it with Discord Event RSVPs and YouTube "notify me".
- Test the stream from India and Singapore before episode 1.

## 3. Chat moderation staffing

**Roles (separate from the engineers answering):**
1. **Host.** Reads questions and keeps time.
2. **Producer.** Runs the stream and the question queue.
3. **Chat mod(s).** Handle spam and abuse.
4. **Question curator.** Pulls questions from Discord and chat to the producer. For small episodes this is the producer.
5. **Engineers.** Answer only. Never moderate.

**Sizing, as a starting point (adjust after two episodes):**

| Concurrent viewers | Staff |
|---|---|
| under 200 | host + producer (producer also moderates) |
| 200-1,000 | + 1 dedicated mod |
| over 1,000 | + 2-3 mods, one per active timezone, one on question curation |

**Coverage for the B slot:**
- Staff in the US cannot cover it in a comfortable way. Recruit 2-3 trusted Discord regulars in India and Singapore as volunteer mods.
- Give them a one-page guide, a 90-minute shift, a backup person each, and a thank-you (swag or a public credit).
- If you rely on volunteers, name one staff member as escalation contact in a private backchannel.

**Set up before going live (most inflow stopped for least work):**
1. Slow mode on.
2. Link posting blocked, or held for review, for non-members. Spam is usually links.
3. Blocked-words list (crypto, job offers, scam phrases) and the platform's auto-hold setting.
4. Pinned message with the code of conduct link and the question rules.
5. Mods can time out for 5 min. Repeat offenders get banned.

**Rules for mods:**
- Delete spam and abuse with no debate. Do not warn spammers.
- Hostile technical arguments: redirect, pin the on-topic version, and don't escalate.
- Harassment of a person: remove, ban, and note it in a private log. It is not a judgment call and not a ratio.
- Hold a 15-min rehearsal before the first episode using two invented cases. One of them should involve a staff member as the subject.

**Check after each episode:** spam removed, mod actions, and whether any real question was missed. If a question was missed, fix the curator step, not the mod count.

## 4. Your guest slot on the partner's webinar

**Ask the partner this week (15 min):**
1. Audience size, profile and region.
2. Format, length, and whether your slot has Q&A.
3. Do you get the registrant list, and with what consent? If no list, you need your own capture link.
4. Who owns the recording, and can you repost it?
5. Which links are allowed, and is there a promotion plan?

**Prepare:**
1. **One takeaway.** Write it as one sentence. A talk with three messages teaches none.
2. **Teach first.** Open with the audience's problem, not Driftwood. Pitch for under 10% of the time. They do not know you yet.
3. **One call to action.** Use a unique trackable link (UTM) to one landing page. Do not scatter links.
4. **Demo plan.** Record a backup of any live demo. Live infra demos fail on conference Wi-Fi.
5. **Tech check.** Join 15 min early. Use a wired connection and a headset. Close notifications. Test screen share.
6. **Q&A.** Write answers for 3 likely questions. Seed one question yourself if the room is quiet.
7. **Chat.** Reply to chat during your slot. Be specific and name people.

**After:**
- Follow up with attendees within 24-48h. Thank the host publicly and share the replay in your Discord.
- Slice the recording into 2-3 clips and a recap post.
- Log the result: attendees, clicks, trials started. This tells you whether partner webinars deserve a place next season.

## Open questions (assumptions I made)

- You have no registration requirement from sales. If you do, platform pick changes to Zoom Webinars or Livestorm.
- The season starts in November or later. If it starts before 1 Nov, the EDT column applies.
- "Bigger episodes" means over 200 concurrent viewers. Tell me your real numbers and I will size the team to them.

**Next (2 min):** open your webinar analytics, export attendee country counts, and send them to me. Then I will fix the A/B slots.