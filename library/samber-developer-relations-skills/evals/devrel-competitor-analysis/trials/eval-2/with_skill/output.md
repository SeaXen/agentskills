Using the devrel-competitor-analysis skill to build this. One note before the numbers: raw stars/Discord/followers are exactly the pattern this skill's own failure-mode list calls "vanity imports" — totals that can only rise, so a single snapshot of them can't actually tell you who's *winning* mindshare, only who's *bigger*. I've built the scorecard you asked for, added the one rate the snapshot legitimately supports, and said plainly what would be needed to answer the real question.

---

# DevRel benchmark: Windlass vs Beacontree, Larkspur, Ashgrove

Observed 2026-09-20 · Peer set: as supplied, roles inferred from scale only (not confirmed via interview — see Method and limits) · Excluded: none stated

## What changes because of this

1. **"Who's winning mindshare" can't be answered from these three fields alone.** GitHub stars, Discord members and X followers are cumulative totals — they only go up, so a snapshot shows *size*, not *momentum* or *mindshare capture*. Verdict: **ignore this framing** until deltas (30/90-day growth rate) or an actual behavioral surface (docs quality, quickstart friction, response times) is added. Owner: you, next pass.
2. **The one real finding in this data: Windlass converts GitHub awareness into community far worse than every rival, not just proportionally worse.** Verdict: **close** — worth a look this week, see Gap plan.
3. **Windlass over-indexes on X relative to GitHub reach** compared to the two bigger rivals — the one place raw scale doesn't fully explain the gap. Verdict: **counter** — lean on it, don't fix what isn't broken.

## Scorecard

One row per observation, ours first. All cells **observed by you**, single snapshot, no source URL or collection date given — see limits below.

| Observation | Windlass (us) | Beacontree | Larkspur | Ashgrove |
|---|---|---|---|---|
| GitHub stars *(vanity — cumulative, can only rise)* | 2,050 | 24,100 | 9,600 | 4,300 |
| Discord members *(proxy for community size)* | 640 | 31,000 | 12,000 | 2,800 |
| X followers *(vanity — cumulative, can only rise)* | 1,900 | 18,400 | 7,200 | 3,100 |
| Discord members per 1,000 stars *(rate, computed)* | **312** | 1,286 | 1,250 | 651 |
| X followers per 1,000 stars *(rate, computed)* | **927** | 764 | 750 | 721 |

The last two rows are the only ones that carry trend-adjacent information from a single pull — a ratio isn't monotonic the way a raw total is, so it's a legitimate structural read even without historical data.

## Per-surface read (partial — one surface only)

**Community reach vs. GitHub awareness.**

- Beacontree and Larkspur convert almost identically: roughly 1,250–1,290 Discord members per 1,000 stars. That consistency across the two biggest players suggests it's close to a category norm, not a company-specific advantage.
- Ashgrove sits lower (651) — plausibly a younger or less community-invested project, can't tell which from this data alone.
- Windlass converts at 312 per 1,000 stars — under half of Ashgrove's rate and roughly a quarter of the two leaders'. This is the one number in this dataset that isn't just "we're smaller," it's "we're worse at turning the awareness we already have into a community," which is a fixable, non-scale-dependent gap.
- On X, Windlass actually leads the pack in conversion (927 vs. 721–764 for everyone else). Worth naming as a strength, not just a smaller-company artifact — X audience-building appears to be working better relative to GitHub reach than either bigger rival manages.

**Everything else — not observed.** Docs and DX, open-source release/response health, content cadence, Q&A tag activity, events, hiring signals: none of this was in what you sent, and none of it can be inferred from stars/Discord/followers. Per the skill's own collection order, the highest-value next steps (in order) would be a timed quickstart for each rival, then a documentation-mode coverage check, then a 12-month forge release/response pull — all three together are cheaper than the community sample you already ran informally here.

## Gap plan

Sorted by impact per unit of cost, highest first.

| Gap | Impact | Cost | Verdict | Owner | Date |
|---|---|---|---|---|---|
| Discord conversion rate (312/1k stars) is ~4x below category norm | high | low–medium | **close** — audit what happens between "starred the repo" and "joined Discord": is the invite link even on the README/npm page? Pin it, add a CTA in the quickstart. | DevRel lead | propose within 2 weeks |
| "Who's winning mindshare" asked of vanity totals alone | medium | low | **ignore as posed** — re-ask once period deltas or a behavioral surface (docs/quickstart) is in hand | you | next pass |
| X conversion rate already leads peers | low | — | **counter** — don't reallocate effort away from X to "catch up" on Discord messaging; the two channels are behaving differently for a reason worth understanding first | — | — |
| Absolute scale gap (Beacontree ~12x our stars) | low (not actionable) | high | **ignore** — company age/funding, not a program lever; restating it doesn't produce a task | — | — |

## Method and limits

- **Single snapshot, no dates or source URLs** on the rival numbers — they were handed to me, not independently observed, so I can't confirm freshness or method (official Discord widget vs. third-party tracker, GitHub API vs. scrape). Treat every rival cell as unverified until re-pulled with a URL and date.
- **No normalization by company age or DevRel headcount** was possible — none of that was supplied, and it's usually what separates "Beacontree is bigger" from "Beacontree's program is better." A 12x star gap on a 5-year-old vs. 1-year-old project reads very differently than the same gap between same-age companies.
- **Stars and followers are flagged by this skill's own methodology as vanity metrics** for exactly this reason: cumulative totals with weak correlation to actual use, and GitHub star counts specifically carry a documented fake-star risk (an ICSE 2026 study identified roughly 6 million suspected fake stars platform-wide) — not saying that's happening here, just that raw star counts alone shouldn't anchor a competitive read.
- **Peer roles (category leader / closest substitute / outlier) are inferred from scale, not confirmed** — I didn't run the interview this skill normally opens with (which product/decision this feeds, audience, deadline, effort ceiling), since you framed this as a quick one-off. If this needs to hold up in a planning or budget conversation, worth a real pass: confirm the peer set and roles, add a timed quickstart + docs-mode read for at least Beacontree, and pull 30/90-day deltas on these same three numbers instead of one-time totals.
- **What would change this read:** if Ashgrove's lower Discord conversion turns out to be because they run a Slack instead (venue misread), or if Windlass's Discord link is simply missing from a high-traffic page (cheap, mundane explanation), the "4x gap" finding evaporates on inspection — check that before treating it as a program failure.