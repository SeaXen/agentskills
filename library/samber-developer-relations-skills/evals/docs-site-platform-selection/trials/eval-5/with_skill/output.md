# Docs platform choice for Brindlewick: no winner yet, and a decision you can defend tomorrow

**ASSUMED, because the interview hasn't happened yet:** every requirement below. I don't know your authors, build owner, hard constraints, API spec format, versions, locales, live date, or what triggered this. I also don't know which three platforms A, B and C are.

## Why I won't score the table

Your table can't produce a winner, whatever weights I pick.

- **A and B tie on every row.** B's "✓✓✓✓✓✓ same" means identical ticks. Any weighting gives them the same score.
- **C differs only on SSO.** If you need gated pages, C is out. If you don't, C ties with the others. The weights never matter, only the SSO answer does.
- **The ticks are claims.** They come from a "Top 9 platforms 2026" listicle. These lists are often written by a vendor that ranks itself first. A tick doesn't say whether the feature works on your pages or what it costs at your editor count.
- **Weights chosen after you see the table follow the favourite.** If I pick weights now, I'd be fitting them to a table I've already seen.

I can produce numbers. They would be arithmetic on ticks, and your director could undo them with one question, such as "who maintains it?" or "what does it cost at 12 editors?"

## Root cause check

Before comparing platforms, what is the pain on your current docs site? Findability, stale pages, broken samples and agents misusing the docs are content or structure problems, and they carry over to any new platform. Only these justify a move:

- slow builds, or upgrades that break
- non-engineers who can't edit
- a hard constraint the current platform can't meet
- maintenance eating the team's time

## Draft requirements register

Weights are fixed here, before any candidate is scored. Replace the ASSUMED sources with your real interview answers.

| # | Requirement (outcome) | Source | Type | Weight | Pilot test |
|---|---|---|---|---|---|
| K1 | Standing owner named, within a monthly-hours ceiling | Q3, ASSUMED | knockout | - | Owner name plus one dependency upgrade during the pilot |
| K2 | Content, assets and navigation can be exported | Standing row | knockout | - | Run the export; diff page count, images, nav |
| K3 | Top 10 old URLs resolve or redirect | Standing row | knockout | - | URL check |
| K4 | Customer or partner pages gated behind SSO, if you need them | Q4, ASSUMED | knockout | - | SSO test account: hidden logged out, absent from search |
| K5 | The 220-page site builds or imports | Q5 | knockout | - | Full-size build, minutes recorded |
| K6 | Your real API spec renders, if you have one | Q5, ASSUMED | knockout | - | Real spec renders; a spec change appears without hand edits |
| D1 | The least technical editor publishes a fix unaided | Q2, ASSUMED | differentiator | 3 | Timed unaided edit |
| D2 | Real reader queries return the right page | Support tickets | differentiator | 3 | 10 queries, right page in the top 3 for at least 8 |
| D3 | Versions kept live, if you ship versioned SDKs | Q5, ASSUMED | differentiator | 2 | One page per version, correct banner |
| D4 | Header, analytics and consent match the company site | Q4, ASSUMED | differentiator | 1 | Works on a pilot page |
| D5 | Few proprietary components needed to port the hard pages | Exit cost | differentiator | 2 | Component count after the pilot |

Two adjustments depend on your answers:

- **Cost.** If you pick a hosted platform, price its multipliers (editors, sites, gated tiers) against your counts now and in a year. If you pick a self-hosted generator, price owner hours per month. This goes in Step 6, not in the weights.
- **Game studios.** If they need interactive API examples, SDK downloads or engine-specific content such as Unity or Unreal, add each as a row. The listicle doesn't test any of them.

## What your table shows once it's a register

This is illustrative. It shows how little the ticks tell you.

| Candidate | Knockouts from the listicle | Differentiators |
|---|---|---|
| A | Everything ticked, nothing `tested` | Unknown |
| B | Same as A | Unknown |
| C | SSO missing, so it fails K4 if gating applies | Unknown |

Under the skill's rule, nothing clears a knockout until it is `tested`. All three stay "claimed" today.

## What to take to your director tomorrow

Don't bring a winner. Bring a decision path:

1. **Pain and root cause.** One line on what triggered this and whether it is a platform problem.
2. **The register above, with weights frozen**, so nobody can tune them to a favourite.
3. **A class recommendation.** "Stay and fix" is the default if the current platform has no failing knockout. Otherwise it is hosted versus self-hosted, decided by whether a named owner exists.
4. **A pilot plan.** Port 5 to 8 of the hardest pages to 2 or 3 candidates over 1 to 2 weeks. Include the page with the most custom components, a reference page, the quickstart, the longest page, and a gated page if you have one.
5. **A decision date** after the pilot.

## Questions to answer before I finish the register

Answer these in order, one at a time:

1. What triggered this? Options: a new site, a specific pain on the current one, a forced move (price change, end of life), or a wish list.
2. Who writes and edits docs today, and how many editors will you have in a year?
3. Who keeps the docs build running, and how many hours a month can they give?
4. Any hard constraints? No third-party hosting, SSO or gated pages, data residency (some studios have NDA'd content), or a procurement path that rules out per-seat plans.
5. What are the platforms' real names? I'll check their own docs and pricing pages instead of the listicle.

Once you answer, I'll replace the ASSUMED rows, name the surviving classes, and write the Step 7 decision record.