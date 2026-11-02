## Recommendation: Bronze ($500), not Gold

Your CMO's instinct — "take the tier with the most visibility" — is reading this as a marketing buy. It isn't one, and that's the whole answer.

**Who actually sees each tier:**

| Tier | Surface | Who's looking at that surface |
|---|---|---|
| $100 Supporter | Name in BACKERS.md | Almost nobody — a backers file is not a page anyone browses |
| $500 Bronze | Logo in the README | Developers evaluating or integrating dayforge |
| $2,000 Gold | Logo on the docs homepage + release notes | Developers using dayforge's docs and changelog |

All three tiers put your logo in front of **developers who use dayforge** — never in front of hospital operations directors, who don't read a dependency's README, docs site, or release notes. You sell to non-developer buyers, so none of this ladder is a media buy against your actual customer. The most it can return is employer-brand exposure to engineers (people who might apply to Kestrel), and that's the same return at $500 as at $2,000 — the docs homepage isn't a bigger audience of *your buyers*, it's a bigger audience of *other engineers*, most of whom aren't evaluating a hospital shift-scheduling vendor. Paying 4x for a bigger developer audience only makes sense if recruiting engineers is the actual goal — and if so, size that against your hiring budget, not a marketing case, because "Gold got us brand exposure" won't survive being asked "exposure to whom, and did it move any deals."

**What this sponsorship is actually for:** you said you use dayforge everywhere — that's a supply-chain/dependency-health signal, not a reach signal. The mandate here is keeping a load-bearing dependency maintained and having a relationship with the person who ships it, not buying a billboard. For that mandate, the tier price should track "smallest recurring amount that establishes the relationship," not "biggest logo." Bronze clears that bar with room to spare; Gold buys prominence you have no audience match for.

**Before you commit, get one number from the maintainer:** ask for the docs homepage's actual monthly traffic. Some maintainers publish this on their sponsor page (view counts are the standard the $2,000+ tier should be priced against); if dayforge's maintainer can't produce a number, that's itself evidence the Gold placement isn't the media buy the ladder implies.

**Two checks before paying anything, regardless of tier:**
- Confirm dayforge is actively maintained (recent commits/releases) — a sponsorship changes nothing for a dependency that's already dormant.
- Make it recurring, not a one-off. A $500/year sponsorship that quietly lapses at your next budget cycle reads worse to the maintainer than never sponsoring at all.

**Bottom line:** pick Bronze. It's the cheapest tier that buys real visibility and a documented relationship with a dependency you rely on heavily, without your CMO booking a marketing win against an audience — hospital operations directors — that will never see any of these three placements.

If Kestrel has (or is about to have) a broader open-source spend beyond dayforge — i.e., this is one line in a larger budget, not a one-off decision — that's a different, bigger question (mandate, budget split across your whole dependency graph, measurement). Say the word and I'll run that version instead of the single-vendor tier pick.