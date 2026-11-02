**Reject both.** Streak card upgrade and Spotify widget both fail before they start — you're optimizing decoration on a page that already buries its own message.

## Why

Your page order right now — typing SVG, stats card, streak card, trophy row, language donut, visitor badge, *then* one sentence — means six widgets run before a reader learns what you do. That's a blocking failure (`B2: visitor can name what account does`) on this skill's own scorecard, not a style nitpick.

Your positioning line — "Full-stack developer passionate about clean code" — is this skill's own catalogued **weak example**, near word-for-word: unfalsifiable, describes half of GitHub, says nothing about infra or platform work.

Your target — platform/infra teams at mid-size companies — reads streak cards and trophy rows as noise, not signal. This exact setup (streak + trophy + language donut above the first sentence, aimed at infra reviewers) is the skill's own worked "most expensive mistake" case. A prettier streak card is still noise to that reader. A Spotify widget adds a fourth-plus dependency with zero relevance to "can this person build the thing I need."

Small silver lining: mid-size companies weight portfolios more than large ones (HackerRank 2018, 80% vs 66%) — so this page matters more for your target than average. Raises the stakes on fixing it, doesn't argue for more widgets.

## Fix order (afternoon, not a rebuild)

1. **Delete, don't swap.** Cut typing SVG, stats card, streak card, trophy row, language donut, visitor counter. Keep at most one visual — a project banner with alt text — or none. Decoration cap is 3, you're at 6.
2. **Write the positioning sentence, put it first.** Names audience + what you build. Draft 3, pick one:
   - Mechanical: "I build [specific infra tool] for [runtime/protocol] — maintaining [flagship repo]."
   - Problem-removed: "I remove [operational pain] for platform teams running [tech] — so on-call stops paging for it."
   - Stop-doing: "If your platform team hand-rolls [X], this does it in CI instead."
   Test: could a competitor paste it unchanged? If yes, still too generic — needs your real specifics.
3. **Reset the 6 pins.** Engineer-credibility shape: 2-3 projects each with an outcome line ("handles N req/day", "used by X"), not star count. Skip stats widgets entirely here — the reader is judging judgement, not activity.
4. **Contribution signal, in this order for a credibility goal**: link 2-3 merged PRs in other people's infra/platform repos first (best-evidenced signal there is, and checkable) → enable the anonymized private-contribution toggle if most of your real work is at a job → only then bother with graph mechanics (unlinked commit email, feature-branch-only work). Never touch the graph itself to "fix" it.
5. **One "what's not true" line.** "Not maintaining X anymore", "not taking feature requests until Y" — costs one line, highest-trust content on the page.

Time: ~2 hrs for steps 1-3, ~30 min for step 4.

## Couldn't verify

No network access this session — didn't run the audit script or fetch the actual page. Everything above is built from what you described plus the skill's evidence base, not from your live README, bio field, pins, or link health.

**Next:** open your profile README on GitHub now, delete the streak card, trophy row, language donut, and visitor badge. 2 minutes, reversible in git history if you change your mind.