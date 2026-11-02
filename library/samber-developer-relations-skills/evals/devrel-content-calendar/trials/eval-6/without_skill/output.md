Here's the full answer, clean-room (nothing under `skill-wip/` read or used).

## 1. The 80/20 evergreen/trending ratio

It's a reasonable default and the wrong thing to optimize. Three problems:

- **It measures decay, not value.** The highest-value devtools post type — the deep engineering story — is neither evergreen nor trending. It won't rank and won't spike, but it converts trust harder than both. A ratio-only view would schedule it out of existence.
- **Devtools evergreen rots fast.** A setup guide decays with every major version of the toolchain. 80% evergreen with no refresh budget is a slowly dying archive — part of that 80% must be *updating* pages, not just adding.
- **Trending only pays with speed.** Reactive posts (new Actions features, K8s releases, language versions) have a ~48–72h window. If you can't ship inside it, the 20% is wasted effort.

Two corrections if you keep the ratio: measure it by **effort, not post count** (one deep-dive ≈ five listicles), and treat devtools content as a three-way portfolio — search-driven evergreen, credibility engineering stories, reactive news. 80/20 silently collapses two of those.

## 2. The idea pile

**✅ Scheduler rewrite in Rust — the quarter's flagship.** Uniquely yours, real numbers, real tradeoffs. Write it honestly or not at all: the bottleneck analysis that justified the rewrite, what broke, where Rust *didn't* help, what you'd do differently. A thin version gets shredded on HN; a solid one is a front-page candidate, a hiring ad, and your best trust asset. Slice it into a talk and a "six months later" follow-up.

**✅ Handshake-timeout guide — best ROI per hour in the pile.** 34 tickets = proven demand in exact user phrasing. Publish as a diagnostic guide: causes, fixes, environment matrix. One caveat: if that error string only exists in Ferrite, search volume is ~zero — its value is ticket deflection and onboarding, so measure tickets deflected, not traffic. If the same error text appears with other runners/agents, it also catches competitor long-tail.

**🔧 "7 tips for faster builds" — cut as written, transform or drop.** "Faster builds" is exactly the territory a CI runner should own, but the tips listicle is the most commoditized format in CI content — you won't outrank every vendor's identical post. The upgrade path: you sit on platform build data nobody else has. "We analyzed N builds: what actually cuts build time, with measured p50/p95 deltas" is a definitive guide and a genuine differentiator.

**❌ "Why we love open source" — cut.** No search demand, no specificity, no proof. Developers read unbacked OSS love letters as cheap signaling. Want the sentiment? Attach it to an act — ship a tool, upstream patches, open-source the agent — and write about that instead.

Gap worth one slot: nothing in the pile is product-adjacent (migrate-from-X guides, comparisons, a build-cost calculator). For a CI runner those often convert better than anything listed.

Realistic quarter at small-team capacity: one flagship deep-dive, the handshake guide plus one more piece mined from ticket data, the data-driven builds piece, and a refresh pass on your fastest-decaying evergreen pages. Four strong pieces beat twelve listicles.

## 3. Hero / Hub / Help

Adopt it as vocabulary, not as the year's structure.

What it gets right: it forces portfolio thinking, and — the biggest win for a devtools blog — it legitimizes Help content (troubleshooting, docs, migrations), which is chronically underproduced because it's unglamorous, yet is where devtools blogs actually win.

It maps onto your pile almost perfectly: Hero = the scheduler post; Help = the handshake guide; Hub = the builds-data piece *if* made recurring (a quarterly "state of build times" series) — a genuine hub has a reason to return, not just a shared theme.

Where it misleads: it comes from YouTube, where audiences subscribe to channels. Blog readers arrive via search and social. "Hub" presupposes a returning audience — with no newsletter to serialize for, a hub becomes the classic B2B failure mode: a series quietly cancelled after four posts. And Hero only pays off with distribution muscle (HN, launches, talks), which is a separate capability to plan, not a content calendar row.

The real risk of any consultant framework: it optimizes the shape of the calendar, not the substance of the pieces. Content fails at the piece level — a framework that gets the OSS love letter published on schedule hasn't helped.

Verdict: use it for budget allocation — per quarter, roughly one Hero, Help as a steady baseline, Hub only alongside a newsletter — and judge every piece on its own merits. That it independently validates the same cuts above is what "worth doing" looks like here.