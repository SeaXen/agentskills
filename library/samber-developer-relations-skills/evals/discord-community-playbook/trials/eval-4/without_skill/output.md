**Next action (10 min):** In Server Settings, enable Community, then set Rules Screening and Onboarding. Both replace most of the Carl-bot gate. Then work the checklist below in order.

The Discord decision stays as made. Four parts of your draft need changing before launch:

| Draft | Problem | Change |
|---|---|---|
| 12 SDK channels | 12 empty rooms on day 1, with 2 part-time people to watch them. Empty rooms make a server look dead. | One `#help` forum channel with 12 SDK tags. |
| `#jobs`, `#memes` | No audience yet. Jobs needs heavy moderation. | Defer both. Memes live in `#off-topic`. |
| Carl-bot reaction-role gate | Extra friction. Discord has a native gate. | Use Rules Screening and Onboarding. Keep Carl-bot as optional backup. |
| Welcome DM with docs and newsletter | Bot DMs to strangers get flagged as spam, and users who block DMs never see them. Auto-subscribing EU users to a newsletter breaks GDPR consent. | Put the welcome in `#start-here` and Onboarding. Newsletter is a link only, never an auto-signup. |

---

## Phase 0: Decide before building (30 min, both devrels)

☐ **Owner.** One named person owns the server. The other is deputy.
☐ **Coverage.** One devrel covers EU hours and the other covers US hours. Write down the overlap window.
☐ **Response promise.** Publish "first reply within 1 business day." Two part-timers cannot hold a tighter promise (set here, not an industry standard).
☐ **Escalation.** Name who decides when the two of you disagree or when one of you is the subject of a report. If the answer is "nobody," fix that first.
☐ **Hours.** Write the sustained weekly hours each person can give after launch month. If the total is under about 6 hours a week, shrink the plan further.

## Phase 1: Server skeleton (45 min)

**Settings**
1. Enable Community. Set a verification level of "Medium" (verified email, account older than 5 minutes).
2. Turn on Rules Screening with your short rules.
3. Turn on AutoMod: block invite-link spam, mass mentions, and known-spam keywords. Send alerts to `#mod-log`.
4. Restrict `@everyone`. No embeds, no external emoji, no mass mentions.
5. Turn on 2FA requirement for moderators.

**Channels (7 public, 2 private)**

| Category | Channel | Type | Notes |
|---|---|---|---|
| Start | `#start-here` | Read-only text | Rules, docs link, GitHub link, newsletter link, how to get help |
| Start | `#announcements` | Read-only, announcement channel | Releases only. Webhook from GitHub releases. |
| Talk | `#general` | Text | |
| Talk | `#showcase` | Text or forum | Projects built on Vectrix |
| Talk | `#feedback` | Forum | One thread per idea |
| Talk | `#off-topic` | Text | Memes go here |
| Support | `#help` | **Forum** | Tags: 12 SDKs + "server/core" + "docs" + "solved" |
| Staff | `#mods`, `#mod-log` | Private | |

Forum for `#help` gives one thread per question, so answers stay findable and you can see unanswered threads at a glance.

**Add later, with a trigger:**
- Per-SDK channel: when that SDK's tag gets at least 5 threads a week for 3 weeks.
- `#jobs`: at about 200 active members, with a required post format.
- `#memes`: when `#off-topic` is mostly memes.

## Phase 2: Roles and onboarding (30 min)

☐ **Roles:** `Admin`, `Mod` (devrels), `Helper` (earned: 3+ accepted answers), `Founding member` (cosmetic, assigned by hand), `Member` (automatic after screening).
☐ **Onboarding questions** (all optional): "Which SDKs do you use?" assigns 12 opt-in ping roles. "What are you here for?" can assign Help, Showcase, or Feedback roles.
☐ **Default channels** in Onboarding: `#start-here`, `#general`, `#help`.
☐ **`#start-here` content:** one-sentence project description, 3 links (docs, GitHub, newsletter), "ask in `#help`, tag your SDK," response promise, code of conduct link.
☐ **Newsletter:** link to the signup page, which has its own explicit opt-in checkbox. Nothing is subscribed automatically.
☐ **Welcome DM:** off by default. If you still want one, send it only after a member opts in, and test with a DM-blocked account.

## Phase 3: Safety and moderation (45 min)

☐ **Code of conduct.** Adapt a standard base such as Contributor Covenant. Publish it in `#start-here` and the repo. It must apply to you and the founders too.
☐ **Ladder:** warning, then timeout, then temp ban, then permanent ban. Each rung has a trigger. Serious breaches (harassment, threats) skip rungs.
☐ **Reporting:** a private report path to the mods, plus a second path (email to the other devrel) for reports about a mod. Acknowledge within 1 business day.
☐ **Two people** can execute every action on the ladder.
☐ **Evidence rule:** screenshot or log before deleting anything.
☐ **Rehearse** two fake cases together. One easy. One where a mod is the subject.
☐ **Bots:** Carl-bot only if you need logging or backup roles. Check that every bot has the minimum permissions.

## Phase 4: Seed before opening (1 to 2 weeks, ~5 h total)

☐ **Invite 20 to 50 people by name:** users, contributors, and friendly answerers. Cover all 12 SDKs with at least one reliable answerer each, and both US and EU time zones. Give each a specific ask: answer in your SDK's tag, post once a week for the first quarter.
☐ **Seed 5 to 10 posts:** real questions in `#help` with real answers, one showcase, one feedback thread. Do not leave a seeded question unanswered.
☐ **One weekly ritual:** a "what are you building this week" thread on Monday, posted by the EU devrel.
☐ **Open in stages,** each gated on activity rather than the calendar: founding cohort, then invited beta, then public announcement.

## Phase 5: Public launch (only when gates pass)

Open publicly when the founding cohort has run for 2 weeks and these hold:
- At least 80% of `#help` threads got a reply.
- At least 5 non-staff members posted.
- Both devrels have kept the response promise.

Then add the Discord invite to the docs, README, and website.

## Phase 6: Day-90 review (put it in both calendars now)

Compare against your own trailing baseline, never a launch spike. These starting thresholds are adapted from published practice, so recalibrate them after the first quarter.

| Signal | Pass |
|---|---|
| `#help` threads answered within 24h | >90% |
| Posts by non-staff members | >50% |
| New members who post within 7 days | >40% |
| Monthly active / total members | >20% |
| Threads with at least one reply | >80% |
| Top 5 members' share of activity | <50% |

**Fold-back rule (write it now):** if 2 or more signals miss at day 90, do not push harder on promotion, since more joins into a quiet room lower every ratio. Shrink the surface, go back to the founding cohort, and re-check. If it still fails at day 180, archive to read-only or merge into GitHub Discussions.

## Risks to accept knowingly

⚠️ **Discord is not indexed by search engines.** Answers vanish from Google. Mirror solved threads into docs or GitHub Discussions at a rate of 1 or 2 a week.
⚠️ **Part-time coverage is the real constraint,** not setup. If either devrel drops below the agreed hours, shrink the response promise before the community notices.
⚠️ **Check Discord settings names** against the current UI. Menu labels change.

**Time:** about 3 hours of setup plus 1 to 2 weeks of seeding.

**Next:** do Phase 0 today. Tell me the 12 SDK names and I'll write the exact forum tags, the `#start-here` text, and the rules.