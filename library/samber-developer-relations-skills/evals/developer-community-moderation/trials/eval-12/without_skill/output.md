Assume Discord (raid/ban language fits Discord, not Slack). Correct.

## Today — 30 min, zero planning

1. **Server Settings > Safety Setup > raid protection** — on. Auto-locks server on mass-join spike, kicks accounts under set age.
2. **Verification Level → High** (must be member 10+ min) or **Highest** (verified phone). Kills throwaway-account raids at join, not after.
3. **AutoMod: enable "Block Spam Content" + custom keyword list** (crypto terms: airdrop, giveaway, wallet, mint, claim, free nft, DM me). Auto-deletes, no mod click needed.
4. **AutoMod: Mention Spam rule** — cap mass-mentions per message. Stops raid pile-on pings.
5. **Slowmode 10-30s** on #general and any public channel raids hit.

This alone cuts the "delete same spam every evening" work close to zero. Ban queue still exists but shrinks hard.

## This week — few hours, light config

1. **Add raid bot (Wick or Security Bot, free tier)**: auto-bans mass-join bursts by pattern (same-age accounts, same default avatar, join velocity). This is what would've ended your 60-account raid in under a minute, not four hours.
2. **Add mod-log bot (Carl-bot or built-in audit log webhook)** to dedicated #mod-log channel. Every ban/mute/delete visible, no manual tracking.
3. **Turn on Membership Screening / rules gate** — new members must tap-accept rules before posting. Free friction against bots.

## This month — needs real planning, don't rush

1. **Trusted-member role tier.** Auto-grant via bot (Carl-bot leveling or account age + message count threshold, e.g. 30 days + 50 messages). Decide what it unlocks first: bypass slowmode? see a #flag-for-mods channel? Nothing more until decided.
2. **Volunteer moderator onboarding.** Write down, before inviting anyone: what can they do (mute/report only, vs. full ban), private mod channel access, response-time expectation. Undefined scope is how volunteers quit as fast as your current two.
3. **Escalation ladder doc.** Warn → mute → kick → ban, one line each on when. Removes "is this bannable" judgment calls from tired mods at 11pm.
4. **Raid runbook.** One page: who flips verification to Highest, who pings the raid bot's lockdown command, who posts the "we're aware" message. Write this before next raid, not during.
5. **Mod rotation.** Two mods covering 11,000 members alone is the actual root cause. Trusted-tier helpers should feed into a real rotation, not just extra hands with no schedule.

Next: turn on raid protection + AutoMod keyword list in Server Settings today — 10 minutes, stops tonight's spam cleanup already.