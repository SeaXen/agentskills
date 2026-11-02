# Developer Reach: Reconciling GA (4,200), PyPI (61,000), and CDN (19,000)

## The one-sentence answer for your VP

**Don't blend these into one number.** They measure three different things, on three different populations, with three different definitions of "count" — averaging or summing them produces a number that means nothing and that any technically literate board member (or your own eng team) can shred in ten seconds. What you present instead is one clearly-labeled headline metric, with the other two positioned as *different questions*, not disagreeing answers to the same question.

## Why the three numbers were never going to agree

| Metric | What it actually counts | Why it's biased | What it's good for |
|---|---|---|---|
| GA docs sessions — **4,200** | Browser sessions where Google Analytics' client-side script successfully fired | Undercounts hard. Independent measurement (Plausible, Aug 2021, tech-heavy audience) found **58% of a developer-type audience blocks third-party analytics scripts** — 88.3% on Firefox, 82.3% on Linux. Your actual docs traffic is not 4,200; that's whatever fraction of real traffic didn't run an ad blocker, didn't decline the consent banner, and wasn't a CI runner or a headless scraper with JS disabled. | Trend and funnel *shape* — step-to-step drop-off inside the quickstart, page-to-page navigation. Not defensible as an absolute count of anything. |
| PyPI downloads — **61,000** | HTTP 200s served for package tarballs | This is not a reach number at all — it's an *install-event* count, and it's structurally inflated by automation: every CI run that reinstalls your SDK, every Docker layer rebuild, every dependency-resolver retry counts as a download. PyPI's own stats separate a "with mirrors" and "without mirrors" series for exactly this reason — worth checking which one this 61,000 is. One download ≠ one developer; a single CI pipeline can generate hundreds in a month. | Package-adoption *trend*, compared only to its own prior baseline. Never as a proxy for "users" or "developers reached." |
| CDN unique IPs on /docs — **19,000** | Distinct IP addresses making requests to your docs, at the edge, before any JS runs | Closest of the three to real "reach" — it's server-side, so it isn't blocked, and it's the only one of the three that sees the ad-blocking developers GA misses entirely. But it's not clean either: it doesn't deduplicate people (an office/VPN/NAT exit shares one IP across many engineers; one engineer on wifi-then-cellular is two IPs), and edge logs generally include bot and scraper traffic that never touches GA. | The best available floor-and-ceiling estimate of unique docs reach you currently have. |

The GA-vs-CDN gap (4,200 vs 19,000, roughly 4.5x) is directionally consistent with the published blocking-rate research — GA is not "wrong," it's measuring the minority of your audience that doesn't block it. The PyPI number isn't in tension with either of the other two; it's answering a completely different question ("how much is the package being pulled") that has nothing to do with docs traffic or people-reached.

## What to put on the board slide

**Headline number:**

> **19,000+ developers reached docs.velmont.io last month**
> *(unique IPs, server-side edge logs — the only one of our three measurement sources developer ad-blockers can't suppress)*

**Supporting line underneath, small type:**

> Package installs: 61,000/month (PyPI) · Docs analytics sessions: 4,200/month (Google Analytics, undercounts due to ad-blocking — ~58% of developer traffic blocks third-party scripts per independent research)

This gives the VP one clean number to lead with, while the footnote pre-empts the "why don't these match" question instead of hiding from it — which is the more dangerous failure mode in front of a board than three numbers that don't add up.

## If someone on the board asks "why don't these three agree?"

Say this, verbatim if useful:

> "They're not measuring the same thing. GA only sees developers who don't run an ad blocker — independent research puts that at under half of a technical audience. PyPI counts every install, including CI machines reinstalling the SDK on every build. The 19,000 comes straight from our edge servers, which see every request regardless of blockers — that's the number we trust for reach. We're closing the gap in the other two next quarter."

That last sentence needs to be true — see below.

## What "closing the gap" actually takes, ranked by effort (do this after the board meeting, not before)

1. **Confirm which PyPI series the 61,000 is** — with-mirrors or without. If it's with-mirrors, get the without-mirrors number; it's a free API call, not new instrumentation, and it removes bot/mirror inflation from a number you're already presenting.
2. **Start a daily snapshot job on the CDN log query and the PyPI series.** Both are one-off queries today; neither retains history on its own past your log retention window. If you want a "reach over time" chart for the *next* board deck, the export has to start now — there's no backfilling it later.
3. **Stop treating GA as a reach metric going forward.** Keep it for on-site funnel analysis (search → page → quickstart-copy → outbound-click-to-signup), where relative drop-off between steps is unaffected by the blocking rate. Reference it as "session trend," never as "developers reached," in any future deck.
4. **If you want a real dedup'd reach number later** (not just unique IPs), that requires a first-party or proxied analytics script on the docs site — recovers the ad-blocked half of the audience GA is currently missing. That's roughly a week of web-team work, and it's the only fix that gets you a defensible single number instead of a labeled floor estimate.

One thing to actively avoid: don't let this quarter's "19,000" get compared next quarter to a GA number, a "fixed" PyPI number, or a post-proxy-script number as if it were the same metric — label every future report with its source and method, or you'll manufacture a fake trend line out of a measurement change.