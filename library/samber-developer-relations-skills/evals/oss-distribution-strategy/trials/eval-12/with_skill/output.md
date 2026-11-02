# Distribution plan — qualmstone

## Interview answers on record

| # | Question | Answer |
|---|---|---|
| 1 | Project / install path | Apache-2.0 Rust crate + standalone binary, HTTP-traffic replay against staging. Installs via `cargo install` or a downloaded binary. |
| 2 | Ecosystems | One language registry (crates.io) + a standalone binary. No container image, no extension. |
| 3 | Adopter today / next | Individual SREs today → platform teams inside companies next. Both paths in play, sequenced. |
| 4 | What distribution must produce | Not stated directly. No commercial product, no funnel, no hiring signal, no standard-setting claim was made — inferred target is **users**, specifically company-embedded usage by platform teams. Flagging this as inferred, not confirmed. |
| 5 | Capacity | 12 maintainer-hours/month total, 2 people, forever. **"Nobody else can execute any of it"** — nothing here can be delegated. |
| 6 | Deadline | None. |
| 7 | One-off vs compounding | Compounding, explicitly: *"something that keeps paying without us re-spending."* |
| 8 | Already in place | crates.io page, GitHub repo, one accurate awesome-list entry. Nothing downstream. |
| 9 | Baseline | 7,900 monthly crate downloads · 61 dependents · 340 unique cloners / 14 days (2026-09-24). |
| 10 | Off-limits | No paid placements. No podcasts, either maintainer. |
| 11 | What changes in 2 quarters | Not stated — treat as no dated milestone. |

Three answers do the real work here: **Q5** (12h/month, zero delegation) deletes every per-release-tax family outright rather than shrinking it. **Q7** (compounding mandate) drops creator seeding on its own. **Q10** (no podcasts) drops it a second, redundant way. **Q3** (company adoption is the explicit next target, and the install unit includes a standalone binary) is what makes downstream packaging a live candidate here rather than a default refusal — this is the exact case the skill's own invocation examples describe: *"a standalone binary aimed at company laptops... a downstream-packaging plan."*

## Step 1 — Coverage audit

I don't have live access to your crates.io account or GitHub settings, so the fields below are **unknown, not zero** — run the literal checklist in `coverage-audit.md` before spending anything on new channels. Two findings I can predict with high confidence from the pattern this skill sees every time ("Expect two findings... a half-configured foundation channel... two or three listings that are simply wrong"):

- **Registry metadata** — unknown completeness. Check: all 5 keyword slots used, categories from the live `crates.io/category_slugs` list (not invented), `documentation` link set (or confirm docs.rs fallback renders cleanly), funding link, description written in SRE/staging-replay vocabulary rather than internal naming.
- **docs.rs quality** — this is your pkg.go.dev-equivalent: it's generated from your exported-item doc comments. Those comments are marketing copy whether you intended that or not.
- **The one awesome-list entry** — audit it anyway for link, description, and version currency even though it's reported accurate; that's a 5-minute check, not a finding to skip.
- **GitHub cloners baseline** — the 340/14-days number is on a rolling panel GitHub does not retain beyond ~14 days. **Snapshot it now, and put a recurring 2-weekly note in your tracker to re-read it** — the pre-today history is already gone and can't be reconstructed later.

## Step 2 — Brainstorm, explicitly, before proposing anything

Entering brainstorming mode. Widening with the eleven-family catalog, then applying the default efficiency order and re-ranking it against your specific interview answers — not the raw list order.

**Families deleted outright** (12h/month with zero delegation — the rule is delete, not shrink):

- **Creator seeding** — triple-refused: compounding mandate kills it, "no podcasts" kills it again, and it's explicitly the highest recurring, least-delegable cost of any family. No condition reopens this short of a hire.
- **Extension/plugin marketplaces, artifact/connector hubs** — not applicable. No editor extension, no platform-connector form factor. Not a refusal, just out of scope.
- **Full distro packaging beyond one target** (apt/rpm review, an owned repo) — high entry cost, compatibility tax per release, and your capacity can't carry more than one downstream-packaging relationship. Refuse for now; reopen if a third-party packager volunteers to own it (moves the recurring cost off you) or platform-team demand explicitly asks for it.

**Families promoted above the default order**, and why:

- **Downstream packaging** normally sits near the bottom on efficiency. All four promotion conditions hold here: company adoption is the declared next goal; the binary is a standalone install unit, not just a library; release hygiene is fixable in the foundation pass (see below); the only open item is whether you accept the irreversibility of a shipped package — flagging that explicitly for your sign-off, not assuming it.
- **Trust and procurement signals** rank low on efficiency for individual adoption, near the top for company adoption. Your adopter target just flipped to company — this ships in the foundation pass or it doesn't enter the plan.
- **Dependency-graph position** is *already partly earned* — 61 dependents is a real structural asset (context: only ~27.5% of npm packages have any dependent at all; crates.io's base rate differs but the direction holds). Near-zero cost to hold once earned, so this gets mined, not built fresh — see below.

### Rank the mixes out loud

- **Coverage-first** — foundation ring only, no core channel. Cheapest, but under-serves the stated company-adoption goal on its own.
- **Ecosystem-depth** — pour everything into crates.io/Rust surfaces. Best for individual-adopter volume, which you already have; doesn't move the needle on platform teams.
- **Downstream-first** — packaged into the channel companies already trust. Best fit for the stated goal, but highest effort and the only one carrying compliance/irreversibility exposure.

Given 12h/month, **pure downstream-first is too heavy** — it would consume the entire capacity ceiling on one bet before the foundation ring is even fixed. Recommended: **coverage-first foundation, with downstream packaging carried as a single, bounded test-ring bet rather than the whole mix.** This matches the "re-rank against the interview answers" instruction directly: your capacity answer caps the *mix* even though your adopter answer promotes the *family*.

## Step 3 — Adoption test, per channel entering the plan

| Channel | Recurring cost | Decay | Signal | Kill date |
|---|---|---|---|---|
| Registry metadata | ~10 min/release | Harmful (misleads every visitor) | Registry downloads, referred sessions | Re-check every minor release |
| docs.rs / doc comments | Near zero | Slow | — (quality proxy, not separately measured) | With metadata |
| Trust posture (signing, SBOM, SECURITY.md, Scorecard) | ~15 min/month + per-release SBOM | Harmful (lapsed pipeline fails downstream) | Score > 7, green attestations; stalled evaluations resuming | Monthly automated check |
| cargo-binstall metadata | Near zero, one-time | Slow | Binstall installs (if trackable) | With releases |
| GitHub topics/social preview/README versioning statement | ~1.5h one-time | Slow, mild | Referrals from topic pages | Quarterly sweep |
| Curated lists (2, SRE/testing/chaos-eng category) | ~90 min entry, ~15 min/quarter sweep | Actively harmful (dead links, stale desc.) | Referral arrivals > self-set bar/month | 2026-12-15 |
| Dependency-position mining (top existing dependent) | ~30 min/month | Negligible once earned | Case-study/"used by" placement secured | 2026-12-15 |
| Homebrew homebrew-core submission | High entry, low to hold if hygiene good | Harmful (stale formula reads as abandoned) | Formula accepted; install-source mentions in issues | 2026-12-15 |

## Step 4 — Match to adopter type

- **Individual SREs (today)** — served by registry findability + cargo-binstall + the existing dependency position. No new spend needed here; hold what's already working.
- **Platform teams (next)** — the approver, not the evaluator, decides. Legibility is the lever: license is already clear (Apache-2.0), the gaps are versioning promise, security contact, release rhythm, artifact signatures — all foundation-ring items. Add a visible "used by" wall once you have even one nameable company (real name, or an anonymized description if that's all they'll allow) — per Crossing the Chasm's mechanism, one named peer reference here outsells any download count.

## Step 5 — Sequence

**Stage 1 — Foundation, weeks 1-4 (by 2026-10-22), ~12-14h one-time, split across both of you:**

- Rewrite crates.io description in SRE/staging-replay vocabulary; fill all 5 keyword slots; set categories from the live `crates.io/category_slugs` list; confirm docs/funding links.
- Bring exported-item doc comments up to docs.rs-as-marketing-copy standard.
- **Ship the minimum trust posture now, because company adoption is the next-quarter goal**: SECURITY.md with a disclosure path, Sigstore/cosign keyless signing on releases, an SBOM per release (cargo-cyclonedx or syft), OpenSSF Scorecard workflow in CI targeting >7. Present this internally as procurement enablement, not a download lever — the evidence doesn't support the latter.
- Standardize release artifacts (checksummed binaries, consistent naming — `cargo-dist` covers this well for a Rust CLI) — this is also the release-hygiene precondition Homebrew and cargo-binstall both need.
- Enable `cargo-binstall` (a `[package.metadata.binstall]` block or standard artifact naming) — near-zero cost, no review gate, unlocks a real one-line company-install path immediately.
- GitHub topics tagged (rust, http, sre, testing, chaos-engineering, staging), social preview image, a one-paragraph versioning/support statement in the README linked from the crates.io page.
- Sweep the existing awesome-list entry.

**Stage 2 — Passive discovery, months 1-3, ~1h/month:**

- Mine the 61 existing dependents for the highest fan-in one; ask for a testimonial and permission to name them (or describe anonymized) in a "used by" section. Do not commit to building new integration code — that's engineering capacity you don't have, not distribution hours.
- Contribute something unrelated to two curated lists in the SRE/testing/traffic-replay category, then submit qualmstone in the list's own entry format.
- Opportunistic only, no scheduled hours: if a GitHub topic ally surfaces, pursue curation. Never self-submit — it gets closed by policy.

**Stage 3 — The one bounded downstream-packaging bet, decided 2026-12-15:**

- Submit to `homebrew-core`. Before doing this, **check current stars/forks/watchers against Homebrew's self-submission threshold (90 forks / 90 watchers / 225 stars — 3x the base rate, since this is a maintainer self-submission)**. If unmet, don't force it — wait, or ask a third party to submit.
- **This is an irreversible commitment once accepted — a shipped formula can't be unshipped. Confirm you both accept that before I take this past "candidate."**
- Signal to watch: formula acceptance, and whether support requests start naming `brew install` as the install path (evidence platform teams found it there).

## Step 6 — Release stream

- Maximum interval: 6 weeks ("a fix lands within 6 weeks"), never a minimum.
- Security fixes out of band, within 72 hours.
- Batch small changes into one readable release; every release ships real notes — cadence theater (dependency-bump-only releases) trains downstream bots to ignore the channel.
- No milestone (1.0, rewrite, rename) is currently on record — none of the plan is timed against one. If one appears in the next two quarters, that's the trigger to reopen the aggregator/relaunch refusal below.

## Step 7 — The plan

```markdown
# Distribution plan - qualmstone

## Position today
- Registry metadata completeness: unknown - audit not yet run against live crates.io fields.
- Packaged downstream: nowhere. No mirrors or forks with an audience known.
- Listings: 1, reported accurate, not yet independently swept.
- Dependents: 61, structural position already earned, not yet leveraged for testimonials.
- Baseline 2026-09-24: 7,900 monthly crate downloads, 340 unique cloners / 14 days
  (rolling-window panel - snapshot going forward, pre-today history unrecoverable),
  61 dependents.

## Adopter
Both, sequenced. Individual SREs are the existing volume path, held by registry
findability and cargo-binstall. Platform teams inside companies are the growth goal
and need legibility - versioning promise, security contact, release rhythm, artifact
signatures - before any company-facing channel is worth entering.

## Foundation ring (weeks 1-4, ~12-14h one-time across 2 maintainers, then minutes/release)
- Rewrite crates.io description (staging/replay/SRE vocabulary); fill 5 keyword slots
  and categories from the live crates.io/category_slugs list; confirm doc/funding links.
- Bring exported-item doc comments to docs.rs-as-marketing-copy standard.
- Ship SECURITY.md, cosign-signed releases, per-release SBOM, OpenSSF Scorecard >7 in CI.
- Standardize checksummed release artifacts (cargo-dist).
- Enable cargo-binstall metadata - near zero cost, no review gate.
- GitHub topics, social preview image, README versioning/support statement.
- Sweep the existing awesome-list entry.

## Sequence
1. Foundation - weeks 1-4, 2026-10-22.
2. Passive discovery - months 1-3: mine top dependent for testimonial/"used by" wall;
   2 curated-list submissions after unrelated contribution.
3. Downstream bet - decided 2026-12-15, gated on Homebrew's self-submission threshold
   and on explicit sign-off that a shipped formula is irreversible.
Trigger: if a 1.0/rewrite/rename lands in the next 2 quarters, that's the one condition
that reopens an aggregator relaunch - currently refused.

## Test ring (ends 2026-12-15, ~2h/month)
- T1 - 2 curated lists (SRE/testing/chaos-engineering category), after unrelated
  contribution to each. Signal: referral arrivals, self-set bar derived from current
  crates.io-referred baseline once measured.
- T2 - homebrew-core submission, gated on the fork/watcher/star threshold. Signal:
  formula acceptance; support requests naming brew as the install path.

## Core channel (candidate, decided 2026-12-15)
Downstream packaging (Homebrew), if T2 clears the threshold and shows platform-team
uptake - it is the only family whose value-for-company-adoption ranking matches the
stated next goal. Falls back to the dependency-position relationship (top existing
dependent) if T2 stalls on the threshold or on the irreversibility sign-off.

## Refused
- Creator seeding (all forms): compounding mandate + explicit no-podcasts + highest
  recurring, non-delegable cost of any family. No condition currently reopens this.
- Paid placements: off-limits by constraint, not capacity. Never.
- Full distro packaging beyond one target (apt/rpm, owned repo): exceeds 12h/month
  capacity for compatibility-tax upkeep. Reopens if a third-party packager volunteers
  to own it, or platform-team demand explicitly requests it.
- Aggregator/Show-HN relaunch: no milestone exists to justify a repost reading as news.
  Reopens at a named 1.0/rewrite/rename.
- Directory sprint (mass submission): stale listings actively damage the
  company-adoption goal; capacity only supports 2 curated, targeted lists.
- Self-submitting GitHub topics: against explore-repo policy; pursue only through a
  genuine community ally, opportunistically, not on a schedule.

## Release rhythm
Maximum interval 6 weeks; security fixes out of band within 72 hours; batch small
changes; every release ships real notes.

## Review
Listing and package sweep quarterly, first 2026-12-15 (aligned with test-ring end date).
Metadata re-check at every release. GitHub cloners snapshot every 2 weeks starting now
- the panel's rolling window means missed snapshots are unrecoverable.

## Threshold check
- Sourced (stale listings fixed before new channels added): pending - audit not yet run.
- Supply-chain score > 7 with green attestations: pending - not yet built, scheduled
  for foundation stage.
- Metadata 100% across all fields: pending - audit not yet run.
- Recurring cost within 60% of 12h/month capacity: ~2h/month estimated in this plan
  (17%) - well inside budget, leaving room for the unplanned. PASS on paper; re-verify
  once the foundation stage's actual per-release time is measured.
- Every channel has owner/cost/signal/review date, no harmful-decay channel without a
  scheduled sweep: PASS - built into this document.
```

Two things need your explicit answer before Stage 3 gets executed, not just planned: whether you accept that a shipped Homebrew formula can't be unshipped, and whether "users, specifically platform-team-embedded usage" is really what you want distribution to produce — I inferred that from what you ruled out (Q4 was never answered directly).