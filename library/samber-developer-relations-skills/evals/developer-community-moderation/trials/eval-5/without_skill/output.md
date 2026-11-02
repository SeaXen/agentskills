# Pinegrain Moderation Setup

Two enforcement surfaces, two different power levels. On r/pinegrain, mods hold full native tooling. On the foundation Slack, Pinegrain controls the **#pinegrain channel** only — not the workspace, not account bans, not rate limiting (Slack has no slow-mode). Every section below says explicitly which side can act unilaterally and which side needs the foundation.

## 1. The four-rung ladder

| Rung | Action | Typical trigger | Duration | Who can issue |
|---|---|---|---|---|
| ℹ️ 1 — Notice | Public or DM warning, content removed if rule-breaking | First offense, good-faith rule break (off-topic spam, mild snark, self-promo) | N/A, logged only | Trusted Helper or Mod |
| ⚠️ 2 — Restriction | Reddit: comment lock on the thread + Automod-tagged account (flagged for manual review on next post). Slack: DM warning + message deleted, name added to watch list | Repeat of rung-1 behavior within 90 days, or a single sharper incident (personal jab, bad-faith argument) | 7 days of active watch | Mod only |
| 🟠 3 — Temp ban | Reddit: native temp ban, 7–30 days, with a mod note explaining why. Slack: escalation request to the foundation Slack admin for a timeout/removal from #pinegrain, since channel mods cannot suspend accounts | Harassment, targeted insults, brigading participation, ban evasion signals, or two rung-2s in 90 days | 7–30 days, mod's judgment, logged | Mod, 2nd mod co-signs if duration >14 days |
| 🔴 4 — Permanent ban | Reddit: native permanent ban. Slack: formal written incident file handed to the foundation's Slack admin requesting workspace-level removal — Pinegrain mods only guarantee removal from #pinegrain itself | Doxxing, targeted harassment campaigns, hate speech, repeat rung-3, or organizing a pile-on | Permanent | 2 mods co-sign, logged with evidence |

**Severity skip clause.** Doxxing, slurs, or organizing/leading a pile-on goes straight to rung 3 or 4 on first offense. The ladder is for accumulating minor friction, not a shield for a first-time severe violation — this is the direct lesson from this quarter's two pile-ons, where linear escalation would have been too slow.

**Appeal path.** Rung 4 only: one written appeal to a mod who wasn't part of the original decision, reviewed within 14 days. No appeal for rungs 1–3 — friction there is cheap enough not to need one.

## 2. Raid-night rate limits

**Trigger to declare raid mode:** a spike of reports, new-account replies, or coordinated traffic from an outside link (a hostile Twitter/Discord thread pointing at a post) within a short window. Any mod can declare it; no vote needed — speed matters more than consensus here.

### Reddit — mods act unilaterally

1. Lock the specific pile-on thread first — stops the bleeding before touching sitewide settings.
2. Set Crowd Control to Strict (collapses suspicious-account content pending review).
3. Raise posting restrictions temporarily: minimum account age and karma thresholds (e.g. 30 days / 50 karma), verified email required.
4. Flip the sub to require manual approval on new posts, or restrict submissions to approved users, and add the current Trusted Helper cohort as approved submitters so regulars aren't locked out.
5. Confirm Ban Evasion Filter and Harassment Filter are both on Strict (should be default — verify, don't assume).
6. Put 2 on-call mods on modqueue/modmail live; log every raid-related action with Toolbox usernotes so the pattern is traceable afterward.
7. Stand down: revert thresholds once report volume returns to baseline for 2+ hours. Don't leave the sub locked down after the raid passes — that just pushes newcomers away.

### Slack — process, not settings, because Pinegrain doesn't own the workspace

Slack has no slow-mode and no per-channel ban. The only real levers:

1. Ask the foundation's Slack admin (named contact, agreed in advance — see §5) to flip #pinegrain to "trusted members only can post," if their plan supports it. Confirm today whether it does; don't discover this during a raid.
2. If that's unavailable, it's manual: Trusted Helpers and mods delete/flag messages in real time and log offenders for rung 1/2, mods DM warnings directly.
3. Pin a "raid mode active, we see it, stay out of the pile" message — tell Trusted Helpers to react-emoji, not reply publicly; public replies feed a pile-on.
4. Anything needing account-level action (mute, remove, ban) goes to the foundation contact — that's the actual rate limiter on Slack: the bottleneck is a person, not a setting, so keep that relationship warm outside of raid nights.

## 3. Trust levels

| Level | Who | Earned by | What it unlocks |
|---|---|---|---|
| L0 — Member | Everyone by default | Joining | Normal post/comment access |
| L1 — Established | Regulars | Reddit: 30+ days, positive history, no rung-2+ in that window. Slack: 30+ days, in good standing | Reddit: on the Automod allow-list, exempt from raid-night posting restrictions. Slack: on the trusted roster (see below), stays able to post if the channel gets locked down |
| L2 — Trusted Helper | Hand-picked by mods, not automatic | Consistent, calm, high-quality participation; nominated, not self-applied | Priority-flagged reports, can give a rung-1 nudge informally, public flair/badge — **zero unilateral enforcement power**: no mutes, no bans, no thread locks. Their job is pattern-spotting and fast escalation, not policing |
| L3 — Moderator | Core team | Invited after time as a Trusted Helper | Full ladder authority, scoped Reddit mod permissions (skip "manage mod team" to avoid governance sprawl), Slack channel-manager role |

Keep L2 powerless by design. Giving 4,000-person-community veterans ban authority is exactly how a pile-on turns into a second, mod-caused pile-on — L2 exists to widen the mods' eyes, not their hands. Demote quietly (no public announcement) if an L2 starts acting past their scope.

**Implementation:**
- Reddit: a "Trusted Helper" user flair template, plus the same names on the Automod allow-list and approved-submitters list.
- Slack: since a User Group may need admin approval to create, don't depend on it — pin a Trusted Helpers roster in the channel canvas/pinned message as the source of truth, request a User Group from the foundation as a nice-to-have, not a blocker.

## 4. Logging and evidence

- Reddit: Toolbox usernotes on every rung 2+ action — this is the de facto audit trail serious subreddits run on.
- Slack: no admin-level audit log is available to Pinegrain. Keep a private incident doc (shared doc, not a public channel) with timestamp, screenshot, rung applied, mod who acted. This is also what backs up an escalation ask to the foundation — bring evidence, not a vibe.

## 5. Before this can work: the one relationship to build now

None of the Slack-side enforcement works without a named human on the foundation's side who can act on the workspace. Get, in writing, before the next incident:

1. Who that contact is, and a fallback if they're unreachable.
2. Confirmation of the Slack plan tier and whether channel-level posting restrictions are available.
3. Agreement that a rung-4 Reddit-style permanent ban request, backed by the incident doc, gets acted on within a stated SLA (propose 48h).

Everything above this line is Pinegrain's to run. Everything Slack-account-level sits on that relationship — treat it as infrastructure, not a favor to ask mid-raid.