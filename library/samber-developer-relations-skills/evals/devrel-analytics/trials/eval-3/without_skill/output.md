# Orbitlane — Metrics Diligence Response Pack

**For: Samuel | Use: today | Two parts — (1) the "500K developers" slide, (2) the npm -30% week**

---

## PART 1 — The "500K developers" claim

### 1.1 What almost certainly happened

412,000 + 88,000 = 500,000. That's the number on the slide. Not a coincidence — the associate has probably already done that arithmetic; it takes four seconds to spot a round 500K that decomposes into two published registry figures. Assume they know. This is the single most common metric error in dev-tool decks, and it's virtually never dishonesty — someone pulled the two public download numbers, they summed to a clean round figure, and "developers" got typed next to it because that's the word that makes the slide read well.

Why it's still a real problem: the unit is wrong (downloads are events, developers are humans), the aggregation is wrong (summing assumes zero overlap between the two populations), and it's unfalsifiable as stated — nothing at Orbitlane could confirm or refute "500K developers." A sophisticated associate reading a deck isn't just auditing your traffic — they're sampling your relationship to your own numbers. One mislabeled metric owned and corrected cleanly reads as rigor. One defended reads as a flag on every other number in the deck.

### 1.2 Why downloads ≠ developers

Every one of these inflates the counter without a new human touching your product:

- **CI/CD reinstalls** — `npm ci` deliberately wipes and reinstalls on every push. One dev, one active PR, one week: dozens of installs. A 3-version test matrix (Node 18/20/22) triples that.
- **Cacheless Docker builds** — CI Docker builds routinely run without a warm layer cache, re-running `pip install`/`npm ci` from scratch every time.
- **Transitive installs** — if any other package depends on your client, every install of *that* package downloads yours. Biggest silent multiplier, zero relationship to real users.
- **Mirrors/proxies** — Artifactory, Nexus, Verdaccio, PyPI's `bandersnatch` mirrors pull independently of any human action.
- **Multiple machines per developer**, **Dependabot/Renovate auto-PRs**, **security scanners/SBOM tools** — all fetch on their own.
- **npm's own registry statistics documentation explicitly warns against reading download counts as user counts.** Quoting that yourself is the strongest move available — it shows you read the source, not the dashboard.

**Summing npm + PyPI compounds this twice**: it double-counts polyglot teams using both clients, and it adds two numbers with different, non-constant bias structures (different mirror architectures, different CI caching defaults) — the errors don't cancel, they stack. The sum is *less* meaningful than either input alone.

### 1.3 How big is the real gap?

No reliable industry constant exists — anyone quoting you one to two significant figures is guessing. Bottom-up for one active developer on one project/month: ~20-60 CI installs, ×2-3 for a version matrix, +10-30 for cacheless Docker, +5-15 local/reinstalls, +2-10 automated PRs → **30-150 downloads/month per developer**, before transitive installs or mirrors. Applied to 500K/month, the honest read is that real unique humans are most likely **one to two orders of magnitude lower** — low thousands to low tens of thousands, not 500,000. State it as reasoning and a range if asked; don't replace one fabricated precise number with another.

### 1.4 What to say to the associate today

> Hi [Name],
>
> Good question — you've probably already spotted the arithmetic: that figure is last month's npm downloads (412K) plus PyPI downloads (88K). It's package downloads, not unique developers, and labeling it "developers" was wrong. I'm fixing the slide.
>
> Registry download counts include CI/CD reinstalls (a single active repo can generate dozens of installs a month via `npm ci`, matrix builds, cacheless Docker), transitive installs where we're a dependency of another package, mirrors/proxies, and automated dependency-update PRs. npm's own documentation warns against reading download counts as user counts. Summing npm and PyPI also double-counts teams using both clients.
>
> What we can actually defend:
> - **[X] monthly package downloads across npm + PyPI** — same number, correct label.
> - **[X] public repos/packages depending on our client** (GitHub dependents graph).
> - **[X] unique authenticated accounts/API keys active in the last 30 days** — our real usage number, if we track it.
>
> Happy to share the raw pulls.
>
> Samuel

**Delivery rules**: concede in the first sentence, not the third. Don't explain how the mistake happened ("our previous analyst...") — that reads as an excuse. Offer to hand over raw data; it ends the thread.

### 1.5 What to claim instead, ranked

1. **Unique active accounts/API keys (telemetry)** — best if it exists and is consented/disclosed. If you don't have this, start now; it's the number your Series A will require.
2. **GitHub "Used by" dependents graph count** — best available public proxy, third-party verifiable, but undercounts private/enterprise repos (say so — it's a floor, and it excludes your paying users).
3. **"500K monthly downloads across npm + PyPI"** — same number, honestly labeled. Still a good number for seed stage; pair with growth trend, not a static level.
4. **GitHub stars/forks** — weak, directional only.
5. **Named logos/deployments** — five provable production customers beat any six-figure download count in a seed conversation.

### 1.6 Fix the slide permanently

Change the text before your next send: *"500K+ monthly downloads (npm+PyPI) · [X] public repos depending on Orbitlane · [X] monthly active API keys."* Label every metric on every slide with unit + window. Audit the rest of the deck tonight for the same failure shape (events mislabeled as people/companies: sessions→users, signups→customers). A one-page metrics appendix (source, query, unit, window, known bias per metric) turns tonight's worst moment into a differentiator almost no seed deck has.

---

## PART 2 — npm downloads -30% week-over-week

### 2.1 Verdict

**No, not on its own.** A single-week 30% swing in raw npm counts is inside normal noise for registry data — don't act on it, don't mention it in the deck. Run the checklist below this week; the cheap parts take about an hour.

### 2.2 Why this is noisy by default

Download counts measure HTTP fetches through mirrors and caches, not usage. Any of these move the number 20-40% with zero real change: **mirror sync artifacts** (a full-registry mirror crawl running one week and not the next), **partial-week/late-arriving data** (check your date boundaries first — free, often the whole answer), **calendar effects** (a holiday suppresses CI activity ecosystem-wide), **upstream CI changes** at one large dependent (they turn on a cache or pin a lockfile — their real usage is unchanged, your count craters).

### 2.3 Checklist, in order

1. **PyPI down too, or npm-only?** Highest signal per minute. Correlated drop → something real/global. npm-only → JS-ecosystem-specific artifact, not adoption loss.
2. **Pull daily granularity** (`api.npmjs.org/downloads/range/last-month/<package>`). Single-day cliff → outage/reporting gap. Step down to a new flat level → one big consumer changed behavior. Gradual slope over 2+ weeks → only shape that might be real.
3. **Check `status.npmjs.org`** for incidents in that window.
4. **Per-version breakdown** (`api.npmjs.org/versions/<package>/last-week`) — concentrated in one version points to a specific account pinning/migrating, which is a sales conversation, not a metrics problem.
5. **Cross-check internal usage telemetry** — API calls, active keys, DAU. If real usage is flat while downloads fell, it's noise, full stop. If you don't have this instrumented, that's the actual finding here — same gap as Part 1.
6. **Did you ship a release that week?** A broken peer-dependency range or postinstall failure causes CI retries then a pin-back to the previous version, showing up as a delayed download drop. Check against your release timeline.

### 2.4 Bottom line

One week isn't a trend; three-plus weeks against a rolling 4-week average is. Switch your standing view to a trailing 4-week average now — it kills most of this noise by construction. Don't raise this unprompted with investors; if asked, answer: *"Registry counts swing 20-40% week to week on mirror/CI artifacts — our internal usage metric was [flat/up X%] over the same period."* That answer only exists if you run step 5 this week.

**Both problems share one root cause**: npm/PyPI download counts are standing in for an adoption metric they were never designed to be. Instrumenting consented unique-account telemetry fixes the deck slide, answers the -30% question definitively, and is the number the Series A will ask for anyway. If this week produces one action item, make it that.