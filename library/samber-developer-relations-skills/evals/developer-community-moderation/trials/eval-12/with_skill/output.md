Read the moderation skill and its three reference files (platform controls, incident-response runbook, code-of-conduct outline, published findings) in full. Here's the answer, built on the skill's platform-controls ranking and its promotion rules.

---

## The reframe first

You framed this as "bans today, planning later." One correction before the list: bans are the *least* efficient control on the skill's own ranking, and the *lowest* value against everything you described — a raid returns under new accounts, and spam returns from a new account too. Banning is what you do while the real fixes aren't live yet, not the plan itself. Keep banning today's active spam. Don't let it be the strategy past this week.

Two things are true at once here, and both fixes are overdue by the skill's own trigger, not just "nice to have":

- Crypto spam is a **volume problem** (skill: "a spam campaign is a volume problem, and banning accounts one at a time just burns the team's hours"). The fix is rate limits and filters, not more triage.
- The raid — 60 accounts in 20 minutes — is the same volume problem at a different rate. The fix is entry friction on new accounts, not faster banning.
- Your two moderators quitting is the skill's explicit promotion trigger for earned trust levels: *"promote them the moment moderator load crosses the agreed cap, or after the community survives its second flood."* You're past cap, and you've had your flood. Don't park this at the bottom.

## Turn these on, in this order

### Today — single settings, no design work, do these before anything else

1. **Turn on slow mode** in your highest-traffic channels. Rate limits are tied for the cheapest control that exists (one config change, self-running) and they're what actually stops a flood's velocity — nothing else on this list does that as fast.
2. **Turn on the platform's automatic spam/keyword filter**, seeded from the crypto spam you already delete by hand. Pull the last month of phrases and links straight into the block-list — you have a perfect training set sitting in your moderator's memory.
3. **Raise the join bar for new accounts** — account-age or email/phone verification, or a rules-acceptance gate, before someone can post. This is the direct answer to "60 fresh accounts in 20 minutes": a raid is 60 joins, and this is one setting, not 60 individual judgment calls. (If your chat platform is Discord: Verification Level → High or above does most of this in one click.)
4. **Archive before you delete.** Chat evidence disappears the moment a message is removed. If your filter can log the message before auto-removing it, turn that on now — you'll want the pattern data in step 6, and you'll want proof if a raider comes back and disputes a ban later.

Keep banning whoever's still active from before these go live. That's fine — it's manual triage, the bottom of the list, worth doing today only because it's already running.

### This week — a script or a setting, not a daily grind

5. **Route filter hits to a private mod-alert channel** instead of silent auto-delete-only. You want visibility into what's getting caught, both to tune the filter and to feed step 6.
6. **Start designing the earned-trust role.** Draft what a "Regular" gets to do — flag a message for instant hide, maybe a timeout — and who qualifies: a visible track record helping newcomers, not seniority or a nomination. This is the one item here that takes real design time (roughly a week, per the skill), but you already meet both promotion conditions, so start now rather than after the next raid.
7. **Put a load cap and a rotation on the two current moderators, on paper, this week** — independent of everything else. The reason they're both close to quitting is almost certainly zero rotation and no ceiling on their hours, and that's fixable before a single other document exists.

### This month — needs the volunteers and one short working session

8. **Turn your long-timers into that Regular role.** Recruit from who is already de-escalating and answering newcomers in the room, not from who asked first.
9. **Give them a narrow, explicit power set** — flag and hide, maybe time-out. Hold ban authority back with a smaller reviewing body until the ladder exists, so a volunteer is never put in the position of inventing a sanction on the spot.
10. **Write down what each control does and who can flip it** — a one-page platform control sheet. It's the cheapest deliverable on the list and it's what keeps "who turned off slow mode" from becoming its own incident.

## Why this order (the skill's ranking, applied to your case)

| Control | Effort | Value here | When to use |
|---|---|---|---|
| Rate limits (slow mode) | Minutes, self-running | Cuts flood velocity at the source | Today |
| Automatic filters | Minutes, self-running | Catches the *known* crypto-spam pattern, nothing new | Today |
| Entry gates (account age / verification) | One setting + ongoing join-friction cost | Directly targets the 60-fresh-accounts raid shape | Today |
| Earned trust levels | ~1 week design | Raises the floor permanently, the only one that scales past your two mods | Start this week — you're past the promotion trigger |
| Individual bans | Minutes each, forever | Removes one actor who can return under a new account | Keep for today's backlog only, not the plan |
| Manual triage of everything | A standing job that grows with the server | Resolves each item, prevents nothing | What you're trying to exit |

The one thing that doesn't fit this table: real harassment or targeted abuse isn't a volume problem, and no filter or rate limit touches it. That still needs an actual ban ladder with a trigger and a consequence per rung — which is exactly the planning work you correctly deferred.

## What still needs planning, and the order to plan it in

Once the above is live and the immediate bleeding has stopped, the skill's write-order (reports protected per hour of writing, not shortest-first) is:

1. Reporting channels — who receives a report, named, plus an alternate for reports about a moderator.
2. Enforcement ladder — trigger and consequence per rung, built from the raid/spam decisions you've already made rather than invented fresh.
3. `CODE_OF_CONDUCT.md` — adapt a base document (Contributor Covenant 3.0 is the current recommendation), don't write from scratch.
4. Platform control sheet — formalize what you turned on above.
5. Private incident-response runbook, for the volunteers and the two existing mods.
6. Moderator roster and agreement — formalizes the long-timers, with powers, load cap, recusal, and a way to step down without drama.
7. Announcement post — an hour of writing, once there's something to announce.

## Before you rely on any of this

- **Which platform is Nettlefold actually running on** (Discord, Slack, self-hosted)? The setting names above are generic — the skill is explicit that vendors rename these controls often; verify each one against your platform's own moderation docs before you build a runbook around it.
- **Is there any entity above the two moderators** — a company behind Nettlefold, or pure volunteers? That decides who can hand ban power to the long-timers and who arbitrates if a decision is contested.
- **Are minors plausibly present** in an 11,000-member ORM community? Email/phone verification gates collect personal data, which changes both the moderation design and what you owe under privacy law.
- **Would a ban ever apply to a top maintainer or the loudest long-timer?** If the honest answer is no, say so now — the skill's hardest rule is that a conduct policy that exempts its most powerful people is worse than none, and it's cheaper to notice that before you publish anything than after.