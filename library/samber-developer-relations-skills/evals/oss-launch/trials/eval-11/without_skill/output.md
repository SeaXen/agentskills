## Day-one targets

**Before anything else: snapshot your baseline today, not Thursday.** "Day one" only means something as a delta. Record current star count, current npm downloads (if the package is already published), and today's date/time in whatever you use to track this. Without a T0 number, Thursday's count is meaningless — you won't know if 80 stars is "the launch worked" or "that's what it already had."

**GitHub stars, first 24h (delta from your Thursday-morning baseline):**
- 🟢 Solid, credible launch: **100–200 net new stars**. Realistic floor for a well-executed dev-infra launch with no pre-existing audience push.
- 🎯 Good outcome: **250–400**. Means you cleared HN front page for several hours and/or got a second pickup (newsletter, Twitter thread).
- 🏴‍☠️ Exceptional: **500+**. Usually needs either a genuinely novel angle in a crowded category, or your own existing distribution (talks, newsletter, community) doing real work on top of the cold-audience number.

Webhook gateways are not a blank category — Svix, Hookdeck, Convoy and others already exist. Calibrate down from "define a new category" numbers; calibrate up if your differentiation is sharp and easy to state in one line.

**Upvotes — pick one primary channel, don't average two different audiences:**
- **Show HN** is the better fit for this product (infra tool, backend/platform engineers — see `hacker-news-strategy`). Target: 40–60 points in the first 90 minutes to clear the new-post ranking and reach the front page, **100–150 points and 40+ comments by end of day** as a "this landed" outcome, 250+ as exceptional.
- **Product Hunt** is optional and secondary here — its audience skews indie-SaaS/maker, weaker overlap with "people who operate webhook infra." If you run it anyway: top 5 of the day ≈ 200–350 upvotes, #1 Product of the Day ≈ 400–800+. Don't treat a PH number as validation of product-market fit for this category; treat it as extra top-of-funnel.

Treat the upvote number as a **leading indicator**, not the goal — it evaporates by tomorrow. Stars, clones, and dependents are what persist and compound. If you have to choose which number to defend in a retro, defend the star delta and the referrer breakdown, not the HN score.

---

## What to track after launch day (GitHub Insights + npm only)

**From GitHub Insights:**
| Signal | Where | Why it matters more than it looks |
|---|---|---|
| Star velocity over time | star-history.com (reads the public API — no new tool/account needed) | Native GitHub Insights doesn't chart cumulative stars at all; you need this or you have no curve, only a single number |
| Traffic: unique visitors, views, clones | Insights → Traffic | ⚠️ **Only a 14-day rolling window** — export/screenshot it weekly or launch-week data is gone by the time you'd want to write the retro |
| Referrers | Insights → Traffic | Tells you which channel *actually* drove traffic (HN vs. Twitter vs. a blog pickup) — this is more decision-useful than the total, because it tells you what to repeat |
| Clones vs. stars | Insights → Traffic | A star is a bookmark; a clone is someone actually pulling the code. Ratio of clones-to-stars is your realest usage proxy from GitHub alone |
| Issues/PRs opened | Insights → Pulse / Issues tab | Someone filing an issue has run the thing and hit a wall — much stronger signal of real usage than a star |
| Forks | repo page | Intent-to-modify/self-host signal, useful for a gateway people will want to customize |

**From npm:**
| Signal | Where | Caveat |
|---|---|---|
| Daily/weekly downloads | npm-stat.com or `api.npmjs.org/downloads` | ⚠️ Heavily inflated by CI reinstalls and mirrors — track the **trend**, not the absolute number, and expect a very noisy first two weeks |
| Dependents ("N packages depend on this") | npm registry page | This is the one npm number that's hard to fake — other projects actually importing you is the strongest long-term signal you have |

**Cadence — set 4 checkpoints, don't stare at it daily:**
- **Day 1 (end of launch day):** referrer breakdown — what actually worked, so you know what to repeat.
- **Day 7:** star velocity decay (spike-then-flatline is normal; watch how fast it flattens), first substantive issues vs. drive-by stars, clone/star ratio.
- **Day 30:** npm download trend stabilizing, dependents count moving at all, whether contributors beyond you have opened a PR.
- **Day 90:** dependents growth, contributor count, whether clone volume has a steady floor (recurring real usage) vs. dropped to zero (launch tourists only).

One thing to actively resist: don't let "stars" or "downloads" stand in for "usage" in whatever you report internally later — clones, dependents, and issue quality are the closer proxies, and stars/downloads are the ones people will misquote as user counts if you're not precise about the label now.