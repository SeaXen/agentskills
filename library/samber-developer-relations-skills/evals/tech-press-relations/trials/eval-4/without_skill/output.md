## The play: don't launch a report — launch an instrument

"The name people cite for years" is not a PR outcome, it's an infrastructure outcome. Verizon's DBIR, Cloudflare Radar, Sonatype's State of the Software Supply Chain, Have I Been Pwned — none of these won citation share with a single big launch. They won it by being the **standing instrument** a beat reporter, a CISO, or an academic reaches for by reflex, every time, for a decade. That's built, not announced. Drop the "placement" framing entirely; you're not pitching a story, you're building the thing stories get built on top of.

You have the one input this requires that almost nobody else in supply-chain security has: **resolution-level telemetry, not registry metadata.** That distinction is the entire strategy. Everything below is built around widening that gap, not around a launch date.

## Why your data beats everyone else's data

Sonatype, Snyk, Socket, Chainguard, ReversingLabs, GitHub's Octoverex — they all report on what's **published**: package existence, static manifest scans, advisory counts. None of them see what actually gets **pulled**. A registry mirror sitting in the resolution path sees revealed demand, in real time, at the version level. That's a structurally different and harder-to-replicate dataset. Concretely, it lets you say things nobody else can say with a straight face:

- **Patch half-life** — % of resolution traffic still pulling the pre-patch version of a CVE'd package at 7/30/90/365 days post-disclosure. This is the single most citable metric in the industry: it turns "patch faster" from a slogan into a chart every CISO screenshots into a board deck.
- **Blast radius by traffic, not by graph** — "X package has 40,000 dependents" (everyone reports this) vs. "X package accounts for 2.3% of all resolution volume across the ecosystem this week" (only you can report this — it's weighted by actual usage, not declared dependency).
- **Attack-in-progress signal** — dependency-confusion probes and typosquat traffic show up as anomalous resolution requests *before* anyone downstream notices anything. You're not analyzing an attack after disclosure, you're watching it happen.
- **Abandonment exposure** — how much live production traffic resolves to packages with no maintainer activity in N months. Nobody else can separate "unmaintained but harmless" from "unmaintained and load-bearing."

Everything else in this plan exists to keep pointing at this wedge. If a piece of content could have been written by someone reading `npm audit` output, it's not worth your time — it doesn't defend the moat.

## The three-layer engine (build in this order)

**1. The Index — an always-fresh stats/data page.** This is the unglamorous, highest-leverage piece. Per the backlink-format data, curated statistics pages earn roughly **4.25x** the links of an equivalent original-research piece, because they're what other writers actually cite from — original research gets cited *through* the roundup that aggregates it, not directly. Build one durable URL (`/supply-chain-index` or similar), update it on a fixed cadence (weekly or monthly, not "when we feel like it"), and design every stat as a standalone one-liner a journalist or an LLM can lift verbatim with attribution. This is also your AI-citation play — structured, dated, single-fact statements are exactly what gets pulled into ChatGPT/Perplexity answers. This should exist before the flagship report, not after.

**2. The flagship report — quarterly, not annual, at least for the first two years.** Annual cadence (DBIR-style) is right once you're established; early on it's too slow to compound trust or headlines. A quarterly "State of Dependency Resolution" report, each one narrower and sharper than a DBIR-style kitchen-sink report — one hero finding per issue, not forty charts. Publish the methodology page alongside it, in full, including your aggregation/anonymization thresholds. Security researchers will pick apart the numbers before they cite them; a report that survives scrutiny is worth ten that don't.

**3. The incident desk — reactive, fast, ongoing.** Because you see resolution traffic, you're structurally positioned to be first to publicly flag a live supply-chain attack (compromised maintainer account, dependency-confusion campaign, malicious version spike) with real data, not speculation. This is the "have an enemy" story angle, except the enemy is a literal attacker and you have the receipts. Being first and right, repeatedly, over years, is what makes "as first reported by Hollowbrook" become a sentence journalists write without thinking about it. This needs an on-call rhythm, not a content calendar — someone owns "does this week's anomaly deserve a same-day writeup."

## The founder problem: don't start with the founder

A founder with zero public track record is a liability on day one of a credibility play, not an asset. Two moves:

- **Build the institutional brand first.** Name the research function — "Hollowbrook Research" or "Hollowbrook Labs" — and byline the Index and the reports to that name, not to an individual. This is how Unit 42 (Palo Alto), Socket's research team, and Chainguard Labs all work: the institution accrues citation equity independent of any one person's writing history, and it survives personnel changes.
- **Bring the founder in through voice, not analysis.** Founder's first public appearances should be the founding story and the "why we built this" angle — low-risk, high-authenticity, doesn't require a track record of technical writing. Pair with press/podcast training before pitching podcasts; a founder's first public rep should not be a live interview. Ghostwrite the first 5-10 pieces closely, then hand off gradually as their voice solidifies. Data-heavy technical writeups stay bylined to Research for at least a year regardless of who drafts them.

## Distribution: owned first, then earned, reactive throughout

Run all three PR modes, not just one:

- **Owned (do this now, it's a one-afternoon job):** press page with methodology docs, research-team bios, logo pack, and a real press contact email — not a form. This is infrastructure for every pitch you'll ever send; build it before you need it.
- **Proactive:** build a beat list of reporters who specifically cover supply-chain security (not general infosec) — Dark Reading, The Daily Swig/PortSwigger, BleepingComputer, The Register's security desk, Ars Technica. Pitch the *data*, never the company. "Here's a pattern in resolution traffic nobody's reported" is a pitch; "we run a registry mirror" is not.
- **Reactive:** this is where the incident desk pays off directly — when a real supply-chain attack breaks, you should be able to comment with your own telemetry inside hours, not days. Speed beats polish here.
- **Inbound:** get onto HARO/Qwoted/Featured for supply-chain and dependency-security queries — cheap, low-effort, compounds the same beat relationships.

## Sequencing (no launch date needed, but don't drift)

Roughly 18 months to "known," not weeks:

- **Months 0-2:** methodology + anonymization thresholds finalized and documented, press page live, research brand named, Index page shipped with first real numbers.
- **Months 2-4:** first flagship report — narrow, one hero stat, pitched proactively to 10-15 specifically-chosen reporters, not a wire blast.
- **Months 4-12:** quarterly reports continue, Index updates on fixed cadence, incident desk responds to anything real that surfaces in the telemetry, founder starts light public presence (founding-story pieces, 1-2 podcasts).
- **Year 2:** shift cadence toward annual flagship (DBIR-style authority move once quarterly has built the base), start offering vetted researchers/academics narrow data access — a citation in a paper is the most durable citation there is, and it's the one competitors can't buy or newsjack.

## Guardrails that protect the credibility, not just the legal exposure

- Never publish anything that fingerprints a specific customer or org, even indirectly — k-anonymity thresholds on every published cut, reviewed by legal *and* by someone thinking like an attacker trying to de-anonymize it.
- Publish the methodology in full, always, next to the numbers. A number without a visible method is a marketing claim; a number with one is a citation.
- Don't let "aggregate" quietly become "actionable target list" — patch-lag stats about the ecosystem are fine; patch-lag stats that could out a specific unpatched org are not, even if technically aggregated at a small enough scale.

## How you'll know it's working

Track coverage count and domain rating like normal PR, but the metrics that actually indicate "the name people cite" are further downstream: unprompted citations of your numbers in other people's reports/decks without you pitching them, inbound journalist queries where you weren't the one who reached out first, and AI-citation rate (ask Perplexity/ChatGPT supply-chain-risk questions periodically, see if you show up unprompted). That last one is the modern proxy for "industry standard reference" — it's the same status DBIR has held for a decade, just measured in a channel that didn't exist when DBIR started.