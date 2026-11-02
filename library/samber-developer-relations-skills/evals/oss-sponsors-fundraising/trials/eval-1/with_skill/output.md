Reviewed `oss-sponsors-fundraising/SKILL.md` plus `references/tier-ladder-examples.md` and `references/platform-mechanics.md`. Your current ladder is the skill's own worked example of a "weak ladder" almost verbatim, so I'm applying its diagnosis to your specific edits, not just relabeling prices.

# Sponsorship ladder — zodiac-rs

## The rewrite, as you specified it

| Tier | Price/mo | Reward |
|---|---|---|
| Backer | $5 | Name in README |
| Supporter | $10 | Name in README, bigger |
| Sticker Club | $15 | Sticker pack |
| Early Access | $20 | Early access to release-candidate builds |
| Priority | $25 | Name in README + I answer your questions faster |
| Champion | $250 | All of the above + monthly 1:1 call + logo somewhere |

Drop $1. That's the literal ask. Before you publish it, four things in this exact shape will bite you later — same failure modes the reference "weak ladder" diagnosis names, not new ones I'm inventing:

## What to fix before it goes live

**1. GitHub Sponsors tiers are permanent once published — you're not editing $50, you're retiring it.** A published tier's price can never change; you retire it and publish a new one, and everyone already on the $50 tier stays there at $50 with the old reward forever unless they manually move. Same for the $1 tier you're dropping — its sponsors don't disappear, the tier just stops accepting new ones. Price the $250 tier for two years out, because this is the last time you get to set it without another retire-and-replace.

**2. "Monthly 1:1 call" doesn't survive its own success.** Run the ten-times test the skill specifies: if Champion ever has 20 sponsors, that's 20 calls a month — a part-time job, sold at $250. This is the exact failure the reference diagnosis calls out on the original $50 tier, and bumping the price doesn't fix it, it just delays when it breaks. Cap it (first N sponsors/month, waitlist after) or downgrade to quarterly group office hours, which is a bounded reward instead of a standing job.

**3. "I answer your questions faster" is the same trap at $25.** Priority *triage* (I look at sponsor questions first) is sellable; priority *outcomes* (implied faster fixes/answers) isn't, and it reads as a queue-jump to every non-sponsor watching the issue tracker. Reword to something you can honor mechanically without a promise — "sponsor questions get a first pass" — or move a real SLA to a future retainer tier with a written scope, not a $25 add-on.

**4. "Logo somewhere" is still unpriceable.** Name the actual placement (README, docs footer, crates.io description) and, if you have it, the traffic it reaches — pull it from repo Insights → Traffic or docs.rs page views. An approver — and at 1.1M downloads/month you likely have company users, even if none sponsor yet — can defend "logo in README, ~X views/month." They can't defend "somewhere."

**5. Sticker pack is a physical-fulfillment reward, not a near-zero one.** Mailing costs, addresses, customs on international sponsors — all fine at today's sponsor count, all a real logistics job at 10x. Ship it once per new sponsor as a welcome item, not monthly, to keep the cost bounded regardless of how many sponsors you get.

**6. Six live tiers is above the 3-5 baseline, and $5/$10/$25 still sell the same reward at different font sizes.** Not something you asked to change, and not urgent, but it's the exact "nothing distinguishes $5 from $10 except size" issue the reference diagnosis flags — most people will just pick $5. Leave it if you want, but don't expect $10 to convert much on its own merit.

## The one thing not on your list worth naming

Your top tier tops out at $250. At 1.1M downloads/month, $180/month total income is the textbook "no company tier" story — the money is in companies that depend on the crate, and a company can't buy a tier that doesn't exist. That's a separate, bigger lever than anything above (corporate outreach, invoiced sponsorship, a placement tier priced against real traffic) — say the word if you want that lane opened; it's a different motion, not just another row in this table.

## If you want the safer version of the same ladder

| Tier | Price/mo | Reward |
|---|---|---|
| Backer | $5 | Name in README |
| Supporter | $10 | Name in README, bigger |
| Sticker Club | $15 | One-time welcome sticker pack |
| Early Access | $20 | Release-candidate builds ahead of public tag |
| Priority | $25 | Name in README + sponsor questions get first pass |
| Champion | $250 | Above + logo in README (state placement/traffic) + quarterly group office hours (capped seats) |

Same prices you asked for, same order, only the delivery risk on the top two rows is bounded instead of open-ended.