## Short answer

🔴 The plan doesn't hold up **as the measurement system**. ✅ It holds up as baseline hygiene. UTMs count web sessions; your funnel's decisive events — `npm install`, signup, first successful API call — happen where UTMs can't see. You'd report an answer to a different question than the one your head of DevRel asked.

## Where it breaks

- **Sessions ≠ developers.** "Which channels bring developers in" is a question about installs and activated accounts. UTM totals answer "what did people click before a pageview."
- **Last-click lies.** Newsletter → branded search two days later → docs → signup credits "organic search." Closing surfaces get credit; demand generators (talks, newsletter, word of mouth) get zero.
- **Repo links are invisible.** The visit happens on github.com, where your analytics never runs. Query params don't fix that.
- **QR scans leak.** Mangled URLs, truncated params, people typing the domain later from a phone photo — arrives as direct/organic, uncounted.
- **Your audience blocks you.** Developers over-index on ad blockers (uBlock kills GA4) and incognito. Counts skew non-randomly.
- **The dark funnel stays dark.** Coworker recs, Discord mentions, podcasts, AI assistants recommending your package — no link you control, invisible in totals, plausibly your biggest channel.
- **Totals reward traffic, not quality.** 1,000 slide-scan tourists beat 50 podcast listeners who install. Report install rate per channel, not raw volume.
- **"Absolutely everything" decays.** Freehand tagging fragments (`Twitter` / `twitter` / `x`) into separate rows. At 3h/week you can't police it.

✅ Keep: newsletter UTMs (email is where they actually work), consistent tagging as a floor.

## What I'd do first

Total build ≈ 6–9 hours across 2–3 weeks, then ~45 min/week. Ordered:

**Week 1 — define "came in" as an event.** Pick one acquisition event: install, first API call, or signup. Recommend install-with-activation (install that later makes a real API call). Every later number reports against this.

**Weeks 1–2 — capture the channel inside the SDK path.** The install happens in a terminal, so bind the ref there:
1. Docs/landing pages carry `?ref=talk-xyz` into the quickstart's copy-paste command (`npx thistledown init --ref talk-xyz`).
2. First SDK run reports ref + salted, hashed install ID.
3. Persist ref on first docs visit too, stamp it on later signup — covers devs who never copy the command.

Survives blockers, cookies, cross-device. Ties channel → install → activation. 🔐 Document it, honor `DO_NOT_TRACK`, hash only — a payments-adjacent audience punishes covert telemetry.

**Week 2 — own the links.** Stand up `go.thistledown.dev/xyz` redirects: server-side click log (blocker-proof), 302 to destination, works even for GitHub-bound traffic. One short link per placement; the link generator enforces the convention, so no tagging discipline needed. Slides, READMEs, newsletters, show notes all use it.

**Week 3 — one question, asked once.** "How did you hear about us?" free-text at signup / Discord join. Noisy, but the only instrument that sees word of mouth.

**Ongoing — ~45 min/week:**
- Join redirect clicks + installs by ref into one per-channel funnel table.
- Snapshot GitHub clones weekly (repo Traffic tab, 14-day window only) and npm downloads (`api.npmjs.org` — totals, no attribution, good denominator).
- Per talk: check the direct/organic bump over the following 48h — that's the real signal, not the QR count.

The report to your head of DevRel becomes:

| Channel | Clicks | Installs | Install rate | Self-reported |
|---|---|---|---|---|
| Conference talks | 340 | 21 | 6.2% | 9 |
| Newsletter | 890 | 14 | 1.6% | 4 |
| Word of mouth | — | — | — | 31 |

First-touch ref on the install event — not session totals. That table answers "which channels bring developers in" and directly prices next quarter's talk vs. newsletter spend.

**Don't build at 3h/week:** multi-touch attribution models, per-link granularity past placement level, a warehouse, channel A/B tests. Six well-instrumented placements beat tagging "absolutely everything."

**Literally first, this week:** pick the acquisition event, ship the `--ref` flag in the init command. Everything else hangs off that.