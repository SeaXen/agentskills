# DevRel budget cut — Northwind Data, discretionary $300K

## Entry point

Finance gave a percentage and a deadline, not a strategy change. Per the budget-allocation framework, that means cut list first, using the current shape as the baseline — not a full re-zero of the budget. I'm treating your $90K/$70K/$55K/$40K/$25K/$20K split as this program's own **program baseline**, and cutting from that, not from an industry ratio.

Two things I don't have and am flagging rather than guessing: an **hours envelope** (named people, hours/week on each line), and whether any of the six lines carry **committed** spend — signed booth contracts, prepaid annual newsletter deals, OSS foundation memberships with notice periods. If any of the $90K conference line or the $25K OSS line is already paid or contracted, that portion isn't cancellable by Friday regardless of what the ranking below says. Check notice dates before you promise Finance a number.

## Classify each line before ranking

The framework ranks lines by what kind of bet they are, not by cost-per-outcome (comparing "cost per qualified conversation" against "cost per published piece" would just crown whichever pillar is easiest to instrument). Here's the classification:

| Line | Cash | Kind | Why |
|---|---|---|---|
| Conference booths | $90K | Rented reach | Stops producing the moment you stop paying; no compounding surface left behind beyond swag and a deck |
| Agency content pipeline | $70K | New compounding line, promoted twice | You've defended it as the long-game bet at two consecutive reviews — that's the framework's exact trigger for "don't cut this first" |
| Docs & sample maintenance | $55K | Foundational maintenance, actively-wrong decay | Neglect here isn't quiet — it's four SDK repos going red in CI, which is the specific failure mode this framework protects last |
| Discord + champions | $40K | Proven renewal | Already running; no baseline given on whether it's clearing any threshold, so treat as protected-but-unverified |
| OSS sponsorships | $25K | Rented reach (assume breadth, not depth, absent other info) | Goodwill and coverage across dependencies, not a named maintainer relationship you'd lose sleep over cutting |
| Newsletter sponsorships | $20K | Rented reach, paid distribution | The purest case: decays to zero the day the invoice stops, by design |

Ranking cuts by efficiency read from the bottom, rented reach goes first, foundational maintenance goes last, and a compounding line you've promoted twice doesn't take the first hit or the second defense was theater.

## The headline finding

Your three rented-reach lines — booths, OSS sponsorships, newsletter — total **$135K, or 45% of the $300K discretionary budget** (program baseline). That's larger than even the 40% Finance hinted at. Which means: **both the 20% cut and the 40% contingency can come entirely out of rented reach, without touching the content pipeline, Discord, or docs at all.** That's the answer to "what should I cut" — not a partial trim across all six lines.

## Cut list

| Cut | Removes | Consequence |
|---|---|---|
| **−20% ($60K)** | Newsletter sponsorships in full (−$20K); OSS sponsorships cut to 2–3 load-bearing dependencies only, breadth dropped (−$15K); one booth tier or add-on package dropped, one flagship kept (−$25K) | No paid newsletter placements this year. OSS presence narrows to relationships that matter, not coverage. One fewer event, still a physical presence at your flagship. Content pipeline, community, and docs: untouched. |
| **−40% ($120K)** | All of the above, plus: OSS sponsorships to zero (−$10K more); booths cut to token presence, one regional workshop or speaking-only slot, no more sponsored floor space (−$65K more) | Zero owned OSS relationships — flag this one specifically if any of those three dependencies sit on your critical path; that's a supply-chain-exposure question, not just a goodwill one. No more conference floor presence, only speaking where you're accepted for free. Content pipeline, community, and docs: **still untouched.** |

The split within each cut ($20K/$15K/$25K, then the further $10K/$65K) is a **self-set proposal** — move the dollars between the three rented-reach lines however you want, the point is the order (paid distribution first, breadth sponsorship second, booths last and hardest because it's your biggest single line) not the exact figures.

## If Finance comes back past 40%

You'd be past what rented reach alone can absorb ($135K caps out at 45%). In order, next:

1. **Discord + champions** — cut the champions recognition/swag budget before cutting moderation coverage. Exit cost here is the one genuinely unrecoverable one in your whole budget: a wound-down community damages trust in a way a cancelled sponsorship doesn't. Scale back, don't kill.
2. **Agency content pipeline** — only here, and say out loud that this reverses a position you've defended twice. If forced, the framework's own guidance is "cut agency volume, keep review capacity" (halve the outsourced piece count, not the in-house review pass) rather than killing the line outright — a compounding bet cancelled after being promoted twice bought nothing for the two periods you spent defending it.
3. **Docs & sample maintenance** — cut last, and never below whatever keeps the four repos green. This is the one line where "invisible until it snaps" doesn't apply; it's visibly broken CI and a support queue the day it slips.

## One thing that helps your case, not just the math

Cutting booths frees staff hours — fewer travel weeks for whoever runs events. The content pipeline's actual bottleneck, per the framework's own cost model, is never the agency writer, it's your in-house technical reviewer capacity. If the same person (or team) absorbs both roles, redirecting freed travel hours into content review is a concrete, fundable reason the agency line survives this round on more than just precedent — worth saying to Finance explicitly, since it turns "we're protecting our pet project" into "we reallocated capacity, not just cash."

## What I'd confirm before you send this

1. Any of the $90K or $25K under signed contract with a notice date? Pulls that amount out of what's actually cuttable by Friday.
2. Named hours per person on each surviving line — a cash-only cut looks complete and fails in Q2 if nobody checks capacity.
3. Individual-developer adoption or enterprise/company-decided? If enterprise, collapsing booths to near-zero at 40% removes your main proof surface for approvers who need to see a human — worth knowing before, not after.

## Five-sentence version for Finance

We're taking the 20% out of rented reach — sponsored newsletters, breadth OSS sponsorships, and one conference tier — none of which leaves anything behind once the invoice stops. If it goes to 40%, the same three lines absorb it in full; the content pipeline, community, and docs stay untouched at both levels. Docs stay protected because letting them decay doesn't save money quietly, it breaks four SDK repos' CI and generates support load instead. The content pipeline stays funded because we've defended it as our compounding bet for two reviews running, and cutting it now would mean neither of those defenses meant anything. Past 40%, the next dollar comes from community recognition budget, then agency volume — never the review capacity that keeps published pieces accurate.

## Quality gate check

- Envelope: cash stated, hours flagged as missing — open item above, not silently assumed.
- Committed vs. discretionary: flagged as unverified for booths/OSS — open item above.
- No pillar compared to another by cost-per-unit anywhere in this document.
- Ordering axis named throughout (efficiency, read from the bottom) with its overrides (two-period compounding promotion, actively-wrong foundational decay) stated and applied.
- Cut list is ordered and non-empty at both requested thresholds; consequence stated per cut.
- Every dollar figure tagged program-baseline (your current split) or self-set proposal (the within-category split); no figure presented as an industry number.
- Unfunded/ruled-out lists: not populated — this was a cut exercise on an existing six-line budget, not a full re-allocation; note this rather than omit the section.