## Verdict: don't run any of the three as written

All three break rules this skill states explicitly — two are outright prohibited (not "risky," prohibited), one wastes effort on a metric the skill tells you to drop. Here's each, then what a working version looks like, then what the plan is missing overall.

### 1. Personal Discord account, month-long, sitting in Beacontree's server ❌

This is the exact case the skill names: *"Never conceal who you are: no fake accounts in their community, no attending their developer events under a hidden affiliation... Joining a rival's community or attending their developer conference under a concealed affiliation is the same act, and the closest documented precedent for it — a retailer running a shell company to attend rivals' seller conferences — became a news story rather than an advantage."*

A personal Gmail account with "no company affiliation anywhere," built specifically to sit in a rival's Discord, is concealed affiliation — whether or not you ever post. It doesn't become fine because you're only lurking.

It's also disproportionate even ignoring ethics. The skill's own community-sampling convention is **4 separated weeks**, not a continuous month, chosen to survive burstiness without needing a standing presence. And raw messages-per-channel isn't the metric that carries signal — median time to first reply and staff-share-of-replies are (a support desk wearing a community badge vs. a real peer community). A month of manual counting gets you the wrong number, slowly, at ethical cost.

**Fix:** if the server has public/logged-out read access, use that. If it requires membership, join under your real identity — disclosure of who you are and why is the line the skill (and SCIP's own code of ethics) draws, not whether you participate. Sample 4 separated weeks. Track reply latency and staff-share, not raw volume.

### 2. Intern crawler, overnight, all three docs sites, diffing page counts + last-modified ❌⚠️

Two separate problems:

- **Page counts are explicitly excluded**: *"Skip: visual design opinions, page-count totals, anything requiring a paid account."* You'd be automating collection of a number the skill tells you not to put in the report.
- **Full-site crawl overnight, no ToS check mentioned**: *"Collect periodically and narrowly rather than crawling a competitor's whole site... there is no codified industry rule to hide behind"* — meaning you're on your own politeness norm, not a legal safe harbor. An unattended overnight crawl of three separate properties is exactly the shape this warns against. Nobody in the plan checked robots.txt or each site's terms first.

Last-modified dates *are* a legitimate signal — but scoped to the top 10 pages per competitor for freshness, not a full-site diff.

**Fix:** drop the crawler. Point the intern's hour-per-competitor at the two cheapest, highest-value rungs the plan currently skips entirely — timed quickstart (rung 1) and doc-mode coverage: is each major feature covered by tutorial / how-to / reference / explanation (rung 2). That's the structural read behind "why evaluators pick them," which page counts never were. If a competitor's docs live in a public forge repo, last-modified and release cadence come free from the repo's own API (rung 3) — no scraping needed.

### 3. Buying ~200 stars to calibrate the trending algorithm, then reading Beacontree's curve against it ❌

This is close to verbatim the case the skill names as off-limits: *"Never participate in what you are measuring. Buying stars to see how the market works funds the abuse; the researchers who quantified fake-star campaigns declined to run exactly that experiment for that reason."*

It's also a direct GitHub Acceptable Use violation — Section 4 forbids rank abuse, "including automated starring or following, and fake accounts" — independent of your intent being research rather than promotion. And it's calibrating an instrument to measure a number the skill excludes from the scorecard outright (*"Skip: star totals... Stars are bookmarks with weak correlation to use... any all-time total can only rise"* — named again under the Vanity-imports failure mode).

**Fix:** don't build this instrument. If adoption trend matters, use registry download trend or dependent-repository count instead, labeled `proxy: adoption proxy` per the skill's proxy table. If you report Beacontree's stars at all, report the period delta or rate — never a total, never something calibrated against a bought baseline.

---

## What the plan is missing, beyond the three items

- **No peer set.** Only Beacontree has a name and (implicitly) a role. "All three competitors" appears once for the crawler but the other two are never named or roled. Name 3–5, assign each a role (category leader / closest substitute / adjacent outlier worth stealing from), add the demand-side entry — what a developer uses if Beacontree vanished, often a DIY or open-source substitute — and write down who you excluded and why.
- **No "ours" column.** Nothing here measures your own product on the same fields. Symmetry is a hard target in this skill (100%): every row needs a value for your own product too, or the row gets deleted, not left ragged.
- **Rungs 1–2 are skipped entirely.** Timed quickstart and doc-mode coverage are the cheapest, most direct, most evaluator-felt signals in the whole method — an hour or two per competitor — and this plan spends a month plus an overnight crawl plus $ on stars before touching either. Do rungs 1–3 first, then check whether the question is already answered, before spending anything on community.
- **No Q&A tag pass.** Cheapest surface on the list, and the only one where developers describe Beacontree in their own words. Missing entirely.
- **No source URL / observation date on anything.** Collection discipline requires both on every value — none of the three methods as described produces that.
- **No stated decision.** The skill's first interview question — what decision this feeds — isn't answered. Without it you can't tell whether a month of Discord time is proportionate, or what effort ceiling applies.
- **No gap plan.** Even a clean scorecard isn't the deliverable here — every gap needs close / ignore / counter with an owner and a date, or it's trivia.
- **No re-run plan.** Save the dated raw observations so next time is a diff, not a fresh opinion.

## What I'd actually do this week

1. Name and role the other two competitors; confirm the peer set with you.
2. Timed quickstart + doc-mode coverage, one hour or two each, all peers including your own product. (Kills the crawler and most of the "what am I missing" gap in one pass.)
3. GitHub/forge API pull for release cadence and response times — cheap, ToS-clean, dated.
4. Drop the star-buying instrument entirely; use download-trend/dependent-repo proxies if adoption trend is the real question.
5. For community: real-identity access (or public read-only if available), 4 separated weeks, tracking reply latency and staff-share — not a month-long sockpuppet counting messages.
6. Write the gap plan with verdicts before calling it done.