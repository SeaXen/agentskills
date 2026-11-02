# Dana's Twitch show: what to change before Thursday 2026-11-05

I followed `devrel-live-streaming` (SKILL.md, `platform-facts.md`, `templates.md`) as a one-pass run. I couldn't browse, so the platform facts come from the skill's reference file and may be out of date. Each gap below is marked as an assumption, and owners are "to confirm".

## 0. Do now: this is an incident, not a stream fix

The skill says a key or secret shown on a past stream must be handed to security as an incident. Here, a vulnerability was also reproduced on air. Do these in order. Total effort is about 2–3 hours of security time, plus Dana's time to audit.

1. **Tell the security team today.** They own the decision about public statements. Dana and the team should say nothing publicly until security agrees.
2. **Triage the unsigned-webhook claim.**
   - Test it yourself, on a non-production endpoint if possible.
   - Find out which endpoint Dana hit. It is either our production webhook receiver or the sample app she built on stream. Both need fixing, but they are different fixes (see item 8).
3. **Cut the vulnerability moment out of the archive.** Note its timestamp.
   - Delete or mute that stretch of the Twitch VOD and any Highlight that contains it.
   - Find and delete viewer clips of that window. Twitch lets viewers clip, so look in the channel's clips list.
   - You can't un-share what chat saw. This step limits the spread; it doesn't contain it.
4. **Thank the chat member and move them to the security disclosure channel.** They may know more than they posted. Dana never reproduces a vulnerability live again.
5. **Audit the last episodes for exposed secrets.** Scrub through every VOD, Highlight and clip for the `.env` file, the admin console and any dashboard with customer data.
   - If any secret or customer record was visible, revoke and rotate it now, and treat it as an incident.
   - **My call, beyond the skill's text:** rotate Dana's live keys now regardless of what the audit finds. She keeps live keys on a streaming laptop and "sometimes opens" the file on air. Rotation is cheap, and a miss in the audit is not.
6. **Check the Twitch stream key.** If it ever appeared in a run-of-show doc or a captured settings window, regenerate it.
7. **Review admin console exposure.** If the console showed customers, balances or API logs on screen, security decides whether that triggers a customer-data review.
8. **Fix the webhook.**
   - Product endpoint: it must reject unsigned or badly signed payloads, with a replay window.
   - Sample app: it must verify signatures. Samples get copied, so verify signatures in every sample and in the docs (`docs-code-sample-standards` covers this).

## 1. Refusals triggered

| Dana's current setup | Skill rule |
|---|---|
| Live-coding on her work laptop, logged into the admin console | Refused: "Live-code on the engineer's daily machine and accounts" |
| Her own sandbox and live keys in a `.env` she opens on air | Refused for the same reason. Live keys never belong on a stream machine. |
| Hosting alone and reading chat herself | Refused: "Host alone, reading chat". Nobody can act on spam, raids or a vulnerability posted in chat. |

Two more rules might apply, depending on answers I don't have:
- **Archive:** Twitch past broadcasts are off by default and expire after 7, 14 or 60 days [practitioner quoting Twitch help]. If Dana relies on the VOD, she needs a local recording.
- **Disclosure:** an employee on a personal channel must say who employs them, which Dana may not be doing.

## 2. Existing-show diagnosis

I don't have Dana's last 6 episodes' average viewers, unique chatters or attributed signups. The metrics section below sets what to pull. Don't judge whether the show is worth keeping until that data exists.

**Assumption:** the show is a solo build-along, "solo live build of a real sample app", on Dana's own channel. The skill ranks this as costly, and says the channel leaves with the person unless the company holds the account.

## 3. Existence verdict

**Keep the show, but hold Thursday's live episode until the gate in section 5 passes.**

- The skill says to delete every hosting rung when nobody can moderate during the slot. Today nobody moderates, so a live Thursday is conditional.
- **If there is no named moderator and no clean setup by Thursday morning:** skip the live episode. Instead, either record it and publish after a security review, or have Dana guest on another established developer stream while this is fixed.
- A skipped week costs less than a second public incident.

## 4. Home platform and simulcast

- **Home platform: Twitch**, as it is today. **Assumption:** it's the audience's habit and Dana has an existing following.
- **No simulcast** until each extra platform's chat has its own moderator. If you add one later, Twitch's written rules apply [platform, Simulcasting Guidelines]:
  - No merged chat on the Twitch stream.
  - No sending Twitch viewers to another platform, so moderators never paste a YouTube link in Twitch chat.
- **Account ownership:** the channel and its stream key should sit on a company-controlled login with 2FA and named editor and moderator roles, not Dana's personal login.
  - Owner of the channel, Affiliate or Partner status, and the stream key: to confirm.

## 5. Chosen concept and gate

**Concept:** keep the solo live build of a sample app. **Assumption:** it's the existing format, and I'm not changing it in one week.

Add a goal plus a fallback task per episode, so Dana can recover when something breaks.

**Thursday gate: all must be true, or the live episode doesn't run.**

- [ ] A named moderator for Twitch chat who isn't Dana. Owner: to confirm.
- [ ] Setup in the checklist below done on a separate OS user or browser profile.
- [ ] Demo account with scoped, low-limit sandbox keys. No live keys on the machine.
- [ ] Security has cleared the topic. Dana doesn't discuss or demo the webhook issue unless security says so.
- [ ] Local recording tested.

## 6. Season cadence

- **Keep the fixed weekly slot.** Don't add or move episodes this week.
- **Season length:** 6–8 episodes with a break of a few weeks afterwards to read metrics.
- **Capacity check:** `(host hours per week × 4) ÷ host hours per episode`, rounded down. Host hours per episode are the stream length, plus the same again for prep, plus a few hours for clips. If that is below 2 a month, switch to the guest rung.
- Dana's weekly hours are an open question.

## 7. Moderation roster and pre-flight checklist

**Roster**
- One named moderator for Twitch chat, never Dana. Owner: to confirm.
- Brief them using the moderator template, and give them Twitch moderator roles before Thursday.
- The moderator uses the escalation ladder from `developer-community-moderation`.

**Preset in Twitch before Thursday** [practitioner summaries of Twitch help]
- AutoMod on, at a level the moderator chooses.
- Blocked terms for known spam and exploit phrases.
- Shield Mode saved as a one-click preset.
- Slow mode ready.
- Followers-only chat ready.
- Link policy: only moderators post links.
- Raid settings checked.

**Live escalation (applies to Thursday)**
1. Spam or abuse: delete or time out. Dana never reads it aloud.
2. Raid flood: the moderator switches on Shield Mode and Dana keeps going.
3. **Vulnerability posted in chat or tested live:** delete the message, thank the reporter, redirect to the security channel, don't reproduce it. Note the timestamp, cut it from the archive, and find and delete clips.
4. Product bug or angry customer: the moderator files it, Dana returns to the plan.

**Pre-flight checklist for Thursday and every later episode**
- Separate OS user or browser profile: no saved passwords, no personal tabs, notifications off.
- No admin console on screen. Use a demo account instead. No customer data in any dashboard on screen.
- Sandbox-only keys that are low-limit and scoped. Rotate them after the stream.
- `.env` never opened on screen. Keys come from a secrets manager or environment variables, with `.env` hidden from the editor sidebar. Shell history cleared.
- Privacy scene ready to cut to before any credential screen. The encoder's settings window never in a captured scene.
- Stream key in a password manager, never in the run-of-show doc.
- Local recording running and checked. Audio checked first. Code font readable on a phone.
- Disclosure set: Dana names her employer aloud, in the title and on screen, and ticks Twitch's branded-content box [platform]. Twitch exempts "your own products" from the box, but an employee's case is unclear, and ticking costs no discovery [platform].
- No copyrighted music.
- Failure plan: a holding scene and a line the moderator posts.

## 8. Engagement recipe

**Not now.** Fix safety first. Once the gate passes:
- Pin chat rules (template in `templates.md`): welcome, only moderators post links, found a security issue? Use the disclosure channel.
- Correct Twitch category and tags. End each episode by raiding an aligned channel, not demanding reciprocity.
- Clips and recap within 48 hours.

## 9. Repurposing

- Export the archive before it expires, using the Twitch retention windows above.
- Cut 2–4 clips of answers, not hours. Don't publish any clip that contains the incident moment.
- Hand the archive to `devrel-youtube-channel`.

## 10. Metrics, continue bar and stop rule

- **Outcome:** signups from tagged links, "how did you hear" answers naming the show, and docs or product fixes traced to viewer questions.
- **Show health:** average concurrent viewers (not peak), unique chatters ÷ average viewers, returning viewers.
- **Pull now, for the existing show:** last 6 episodes' average viewers, chatters and attributed signups.
- **Continue bar, to write before Thursday's episode:** `episodes 6-8 vs 1-3: average viewers [up/flat], chat rate [up/flat]; at least [n] attributed signups or [n] docs fixes over the season`. Choose `n` from signup volume; don't move it after seeing results.
- **Stop rule:** below the bar at season end, drop to the guest rung.

## 11. Open questions

1. **Which endpoint accepted unsigned payloads:** our production webhook receiver or Dana's sample app? This decides who owns the fix.
2. Whether any live key, `.env` contents or customer data was visible in past VODs. This decides whether it's a full incident.
3. Who can moderate Thursday, and for how many weeks?
4. Whose login owns the Twitch channel and stream key? Is it company-controlled with 2FA?
5. Is Dana's channel personal or a company channel? This sets what the disclosure must say.
6. Dana's weekly hours, and the last 6 episodes' numbers.
7. Does `devrel-context.md` exist for this program? I didn't write one.

**Summary for Thursday:** run the security triage today, rotate and audit, and run the episode only if there's a moderator, a clean machine profile, demo-only keys and a security sign-off. Otherwise skip it.