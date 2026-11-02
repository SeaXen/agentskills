## Quick verdict

Directionally reasonable, but each of the three legs has a design flaw that will either corrupt the data or expose you to platform enforcement. None are individually fatal — fixable before you spend the month/night/money.

## 1. Discord lurking (Beacontree)

**Problems:**
- One month is a single snapshot, not a trend. Message volume swings hard around releases, launches, AMAs. A month with no event undercounts baseline engagement; a month with one overstates it.
- Raw message count ≈ noise. Bot spam, off-topic channels, and 5 hyperactive users vs. 200 lurkers all look identical in a per-channel tally. Count unique active authors per channel, not just messages, and separate staff replies from community chatter (response time is often the more useful signal than volume).
- A personal Gmail + zero affiliation account is a sockpuppet, not a crime, but many Discord communities explicitly ban "corporate lurking" for competitive intel in their ToS/rules — read Beacontree's server rules first. If discovered, it's a reputational hit, not a legal one.
- No baseline for the other competitors. If the benchmark compares three companies, either monitor all three Discords the same way or don't use Discord activity as a comparison axis at all — one-sided data isn't a benchmark.

**Fix:** run it as an ongoing weekly pull (member count, messages/unique-authors per channel, staff response latency), not a one-off month; timestamp against their public changelog/release dates so spikes are explainable; apply identically across every competitor with a public Discord.

## 2. Intern's overnight docs crawler

**Problems:**
- One overnight run = one data point. Page-count and last-modified diffs only become meaningful as a *rate* (pages added/week, doc-freshness half-life), so this has to run on a recurring cadence, not once.
- "Overnight over all three sites" from one intern machine, unthrottled, risks tripping Cloudflare/WAF bot detection and getting your office/intern IP rate-limited or blocked — annoying, and it also poisons future runs. Add delay between requests, respect `robots.txt` and `Crawl-delay`, and use a plain, honest user-agent string. This is public documentation, so legal risk is low, but being polite avoids getting blocked mid-crawl.
- Page count and last-modified date are shallow proxies. A competitor can inflate page count with auto-generated stub pages, or bump "last modified" via a template change with no real content edit. Pull word count, code-block count, and versioned-docs count too if you want "docs investment" rather than "docs sitemap size."
- You can get a free historical baseline before the crawler ever runs: Wayback Machine snapshots of each sitemap.xml, going back as far as it has coverage, instead of only measuring forward from today.

## 3. Buying ~200 stars to calibrate the trending algorithm

This is the riskiest leg, for three separate reasons:

- **ToS**: buying stars is explicitly inorganic-activity abuse under GitHub's Acceptable Use Policy. Enforcement risk lands on whatever account/payment method/IP touches it — if that throwaway repo, the seller's checkout, or the browser session shares any fingerprint with your real GitHub account (same browser profile, same office IP, same card), the exposure isn't actually contained to a "throwaway."
- **The calibration won't transfer.** A single 200-star burst is not what a real inorganic campaign looks like — sellers drip stars over days with staggered, aged accounts specifically to avoid detection. If Beacontree bought stars for real, their curve won't resemble your one-shot burst; you'd be calibrating against the wrong shape. If you want a usable reference curve, you'd need to buy in the same drip pattern real sellers use, which increases both cost and ToS exposure for no better data.
- **GitHub already filters this.** GitHub runs its own fake-star detection and has publicly discussed purging batches of them; there's also published third-party research characterizing fake-star account clusters (creation-date clustering, empty bios, no other repos, mass-follow patterns) — cheaper to apply that detection heuristic *directly to Beacontree's existing star history* than to run a live purchased-star experiment to reverse-engineer it yourself.

**Recommendation:** skip the purchase. Pull Beacontree's star history (`gh api` or a star-history tool) and check it against the published fake-star heuristics (account age clustering, burst timing, no-bio/no-other-repo accounts, unfollowed-after pattern) — same conclusion, no ToS exposure, no money spent, no risk to any account.

## What's missing from the plan overall

- **No shared methodology doc.** Before collecting, define the same metric set for all competitors — otherwise you get three inconsistent datasets that can't be compared, which defeats "benchmark."
- **No recurring cadence.** All three legs as written are one-time snapshots. A benchmark that matters is a tracked trend — schedule this quarterly (or monthly for GitHub/Discord, which move faster) and diff against the prior run.
- **No GitHub/npm engineering signals beyond stars**: issue response time, release cadence, contributor count, open-issue backlog — all pullable via `gh api` and far more informative than star count alone.
- **No pricing/positioning history**: Wayback Machine snapshots of each competitor's pricing and homepage headline over time — free, and often the sharpest trajectory signal.
- **No hiring signal**: job postings are a cheap proxy for where a competitor is investing (docs team, DevRel, enterprise sales).
- **No publication plan.** If any of this benchmark surfaces externally, do not disclose the collection method — undisclosed Discord lurking and (especially) a purchased-star experiment would undercut the benchmark's credibility if traced back, independent of the ToS issue above. Report only the resulting comparison, keep sourcing internal.