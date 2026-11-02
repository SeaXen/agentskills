# Distribution advisory — northreef-sync

## Direct answers first

- **Data-integration vendor marketplace: yes, but sequence it — don't submit this month.** It's the right channel (a connector belongs inside the platform people already use to move data), but it's a company-adoption, procurement-gated surface. The vendor's review will check exactly the things you don't have yet: license clarity, semver, a security contact, a maintenance signal. Submitting now gets you rejected or, worse, accepted into a "community/unsupported" tier that reads as a red flag to the exact enterprise evaluator partnerships wants to reach.
- **Terraform module: not yet — this is a test-ring bet, not a foundation commitment, and possibly not needed at all.** It only has value for customers who *self-host* the connector. If the vendor marketplace is how most customers will actually run it, the marketplace listing *is* the provisioning path and the module is solving a problem few people have. Find out which before building it.
- **14k Hugging Face downloads vs. npm downloads: stop comparing them, they're not the same unit.** Tell leadership why, and give them a number that actually compares.

Everything below is the reasoning and the plan those three answers sit inside.

## Assumptions (confirm these — they gate the whole plan)

I don't have your real numbers, so I'm stating what I assumed and flagging the two that matter most:

- **Adopter type: company, not individual.** A connector that reads production data and writes into someone's warehouse is approved by a data-platform owner or security review, not picked by a lone developer on a whim. This is the load-bearing assumption — if wrong, most of the recommendation below inverts.
- **Goal:** partnership-driven funnel and credibility, not stars or contributor growth.
- **Capacity: unstated — I'm assuming ~4-6 hours/month** across the small team that owns this, since it rides alongside your actual product. Confirm this number; it decides how many of the moves below run in parallel versus queue.
- **Horizon: semi-urgent.** A "head of partnerships wants it listed" ask usually has a real conversation or co-marketing moment behind it. Get the actual date — it changes how much foundation work you can skip vs. must do first.
- **The 60 clones is a GitHub traffic-panel number.** That panel only retains 14 days — if nobody's been snapshotting it, that baseline is already partially gone. Start capturing it weekly now.

## Position today (what I can infer, what to go check)

- **Registry metadata:** unknown whether northreef-sync is published to a language registry (PyPI/npm/etc.) at all. Check first — if it isn't, that's the actual foundation gap, not the marketplace.
- **Trust signals:** almost certainly absent (no mention of signing, SBOM, `SECURITY.md`). This is the one that blocks the marketplace ask specifically, not a nice-to-have.
- **Artifact hub presence:** one already live and getting real traffic — the embedding model on the model hub. Audit its model card the same way you'd audit a registry page (current description, license, links) — it's already forming an impression on evaluators, unmanaged.
- **Connector hub presence:** none yet — this is the actual ask.
- **Terraform Registry presence:** none.
- **Baseline:** 60 cloners (window and date unknown — capture now), 14k model-hub downloads (real but not npm-comparable, see below), everything else unmeasured.

## Adopter

Company, primarily. The marketplace ask and the Terraform suggestion are both company-adoption moves; treat individual-developer discovery (registry search, awesome-lists) as secondary polish, not the growth lever.

## Why the marketplace listing outranks the Terraform module here

Both sit in the same channel family — artifact/connector hubs — so the usual efficiency ranking (registry metadata cheapest, connector hubs near the bottom on raw efficiency) doesn't decide between them; they cost about the same shape of hours. What decides is validated demand and who's asking:

- The marketplace ask came from **partnerships**, presumably because there's an actual relationship or customer pull behind it.
- The Terraform module came from **"someone suggested"** — no named customer, no confirmed self-hosting need.

A channel with no observable signal attached is a hobby, not a channel. Before building the module, ask: *do any prospective adopters run their own infrastructure to install connectors, or do they all consume through the vendor's platform?* If the marketplace listing is how 90% of customers will get this, the Terraform module serves a small self-host minority — worth a test-ring experiment, not a parallel commitment this quarter.

One more cost the "someone suggested" framing hides: Terraform Registry listings are naming-convention-gated (`terraform-<PROVIDER>-<NAME>`, public repo, semver tags). That's not a subfolder in northreef-sync — it's a **new, separate repository** with its own versioning lifecycle and its own compatibility tax against every provider version bump, forever. Renaming it later silently breaks the listing. That's a second surface to hold, not a rebadge of the first.

## Foundation ring — do this before either marketplace submission (weeks 1-4, ~3-4 hours)

Company adoption is the goal, so the trust posture ships in this same pass, not later:

- Signed releases (Sigstore/cosign), a published SBOM, `SECURITY.md` with a real disclosure path, an OpenSSF Scorecard run in CI. This is what a marketplace reviewer and a downstream security team both check — frame it internally as procurement enablement, not a growth bet (the causal link from signing/scores to downloads is unestablished; don't oversell it upward).
- Fix registry/repo metadata: description in the *buyer's* vocabulary ("sync `<product>` data into your warehouse"), license file detectable, semver tags, a versioning/support statement in the README — the exact things a support-tier label on the marketplace will surface if missing.
- Audit and refresh the model hub listing while you're in there — it's already an active channel.
- Snapshot the clone/traffic baseline now, dated.

## Test ring (this quarter, ends in ~8 weeks)

- **T1 — Vendor marketplace listing.** Read the vendor's actual current docs before anything else (terms and review mechanics change without notice — don't plan against secondhand knowledge of a competitor's process). Confirm which support tier a community-submitted connector lands in and what label it carries; a listing marked "not officially supported" in front of the exact enterprise buyer you want is worse than no listing if you haven't set expectations with partnerships first.
  Signal: listing goes live in the tier you expect; installs/pulls from that hub; any inbound lead or deal partnerships can tag to it.
  Kill/promote date: end of quarter — promote to core if it's producing tagged pipeline, not just installs.
- **T2 — Terraform module, conditional.** Only start this if you can name one prospective adopter who self-hosts. If you can't name one in the next two weeks, this is your Refused entry, not your T2.
  Signal (if run): module downloads *plus* at least one adopter confirmed to be provisioning through it rather than the marketplace path.

## Core channel (candidate)

The vendor marketplace listing, if T1 shows tagged pipeline by quarter-end — this is the one channel here that puts you directly in front of your actual target buyer with no separate awareness spend, which is exactly what artifact/connector hubs are for.

## Refused (for now)

- **Terraform module, unconditional build:** no named customer demand yet, and it duplicates the marketplace listing's provisioning path for most adopters. Reopens if T2's demand check finds a real self-hosting segment, or if the marketplace relationship itself later asks for a Terraform-based deploy path.
- **Comparing model-hub downloads to npm downloads as a single leadership metric:** not a channel to refuse, but stop reporting it this way — see below.

## Release rhythm

Set a maximum interval (e.g., "a fix ships within N weeks") before the marketplace submission — a stale connector is exactly what reads as abandoned inside someone else's paid product, and a support-tier label with no recent tags is the first thing a downstream evaluator checks.

## Review sweep

Quarterly: re-check marketplace listing status and label, model-hub card accuracy, metadata completeness. Re-decide the Terraform module and the core-channel promotion at the same checkpoint.

## Threshold check (run before you submit anywhere)

- Metadata 100% filled on every registry the project actually ships to — unverified, go check.
- Trust posture (signing, SBOM, `SECURITY.md`, Scorecard) shipped before the marketplace submission — not yet done.
- Recurring cost of the committed channels (foundation + T1) fits inside your real monthly capacity, leaving room for sweeps — can't confirm until you give me the real hours number.
- No harmful-decay channel entered without a named owner and review date — applies to the marketplace listing once live.

## On the 14k vs. npm downloads comparison specifically

They're not the same measurement. A language registry like npm counts install-time hits against the package. A model hub counts every `GET`/`HEAD` request against a fixed set of query files (the model card's `config.json` by default, plus every weights file) — a single clone of the repo, a CI job re-pulling it, or a mirror re-caching it can each register as a "download" without a single new user ever running the model. Deduplicated, request-level counts exist only as a paid publisher-analytics feature on that hub.

Neither number is fabricated, but stacking them side by side implies a shared unit that doesn't exist, and it will eventually produce an obviously wrong comparison the first time one metric spikes for reasons unrelated to real usage. Two options for leadership reporting: report each number separately with its counting caveat attached, or replace both with a metric that *is* comparable across the two surfaces — unique cloners, dependents, or (best) confirmed customer connections created, which is the number partnerships actually cares about anyway.