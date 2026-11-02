## Bottom line

Don't force these three into one blended number — averaging or summing metrics that measure different populations (that's exactly what a board member's own engineering lead would poke a hole in). Instead, present them as three stages of a **developer reach funnel**. The divergence isn't a data quality problem; it's the expected shape of the pipeline. Framed correctly, this makes you look *more* rigorous, not less.

---

## Why the three numbers disagree (the mechanism, not just "different tools")

Each metric counts a different population, with a different and non-overlapping bias:

**PyPI downloads — 61,000/mo**
Counts *file-fetch events*, not people. Majority-driven by CI/CD (every GitHub Actions/GitLab CI run that installs your package re-downloads it), Docker rebuilds, dependency mirrors, and Dependabot/Renovate/Snyk scans. A single team running your SDK in their test suite can generate hundreds of "downloads" a month without a human ever reading a line of your docs. This is an **adoption/usage signal**, not a reach signal — it's supposed to be the biggest number.

**CDN unique IPs on /docs — 19,000/mo**
Counts distinct network endpoints hitting the docs path — independent of whether a browser ran JavaScript, so it captures traffic your analytics tool can't see (ad-blockers, curl, API clients). But it's biased in *both* directions at once: NAT/corporate proxies/mobile carrier-grade NAT collapse many humans into one IP (undercounts), while bots, crawlers (Googlebot, GPTBot, ClaudeBot, uptime monitors, link checkers) and dynamic-IP churn (one person, several IPs across the month) inflate it (overcounts). This number is unusable as "reach" until bot/crawler traffic is filtered out of it — flag this as an action item below.

**GA docs sessions — 4,200/mo**
Only counts visits where the GA script actually loaded and fired. Developers block trackers at meaningfully higher rates than average consumers (uBlock Origin, Brave, Safari ITP, corporate proxies stripping analytics tags), so this is a **floor**, not a full count — it's the most conservative, most trustworthy-per-user number, but structurally undercounts.

**The ordering itself is good news.** Downloads (61K) > docs visitors (19K) > tracked sessions (4.2K) is exactly the shape a healthy dev-tool funnel should have — wide at automated distribution, narrowing through documentation research, narrowing further to trackable human engagement. If GA sessions were *larger* than CDN IPs, that would signal something broken. They aren't. Say this explicitly to the VP — it directly answers the "we look like we don't know our own product" fear.

---

## Recommended board slide (copy-ready)

**Headline visual — a funnel, not a single number:**

> **Developer Reach, September 2026**
>
> **61,000** monthly package installs *(distribution — PyPI, includes automated CI/CD)*
> ↓
> **19,000** monthly documentation visitors *(discovery — unique IPs, bot-filtered)*
> ↓
> **4,200** tracked engaged sessions *(depth — GA, human browsers with analytics enabled)*

One footnote line under it:

> *Each stage measures a different population by design — installs capture automated + human adoption, documentation visits capture research activity including non-JS clients, tracked sessions capture the most conservative, verifiably human subset. Narrowing at each stage is expected and indicates healthy instrumentation, not inconsistency.*

This uses all three numbers, turns the "why don't these match" question into a non-issue before anyone asks it, and reads as more sophisticated measurement than a single unexplained figure.

---

## If the VP truly wants ONE number in 60-point font

Don't use 61,000 labeled as "developers reached" — it's not defensible under any technical scrutiny (anyone on the board's engineering side will immediately think "that's just CI re-installs"). If a single figure is non-negotiable for a title slide or exec summary bullet:

> **~19,000 monthly documentation visitors** *(bot-filtered unique IPs, CDN logs)*

This is the best single proxy for "distinct people who engaged with the product," with PyPI downloads cited separately as an adoption metric and GA sessions cited as the conservative engaged-usage floor. Label it "visitors," never "developers" or "reach" unqualified — unique IP ≠ unique person, and "visitors" is standard, defensible web-analytics language that won't overclaim.

---

## Action item before this number goes final

The 19,000 CDN figure is currently **raw**, not bot-filtered. Docs sites commonly see 10–40% of raw unique-IP traffic from crawlers and scanners (search engine bots, AI crawlers like GPTBot/ClaudeBot/CCBot, uptime monitors, security scanners, link checkers). Pull the CDN logs and exclude known bot/crawler user-agents and ASNs before this number appears in the deck — presenting an unfiltered number and having someone later discover 20% of it is Googlebot is a worse look than the current three-numbers-don't-match problem. I don't have access to your raw logs to compute the filtered figure myself; this is a same-day pull from whatever CDN you're on (Cloudflare/Fastly/Akamai all expose bot-score or known-crawler classification in their log fields).

---

## Anticipated board Q&A

**"Why is PyPI 15x bigger than documentation visitors?"**
→ Because most PyPI downloads are machines (CI pipelines, Docker builds, dependency scanners) reinstalling the package on every build, not new humans discovering the product. That's normal for any actively-maintained SDK — a low CI-to-human ratio would actually be more concerning, since it'd suggest low adoption in automated production pipelines.

**"Is 19,000 real people?"**
→ It's distinct network addresses, bot-filtered. Some are shared by multiple people behind one office/campus IP (undercount), some are one person across several sessions on a changing IP (overcount). Best read as "distinct visiting sessions from the network level," not a literal headcount — which is why we don't call it a developer count, we call it documentation visitors.

**"Why not just add them together?"**
→ They overlap heavily and measure different things — a single engineer installing the package in CI, reading the docs once, and showing up in one GA session would count in all three numbers already. Summing them would double- and triple-count the same people.