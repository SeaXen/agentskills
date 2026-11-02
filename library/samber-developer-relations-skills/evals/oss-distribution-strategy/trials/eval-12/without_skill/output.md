Next action, today, under 10 min: open `Cargo.toml`, check `keywords`/`categories` fields match how platform teams would search crates.io (`http`, `staging`, `traffic-replay`, `chaos-engineering`, `cli`), add repo topics to match on GitHub. Free, one-time, done now.

## Core reframe — this decides everything else

Qualmstone today gets used as an incident tool: SRE grabs it mid-investigation, runs once, closes laptop. Low frequency, high pain in the moment.

Platform teams don't adopt incident tools. They adopt release-gate tools — something wired into CI that runs on every deploy. Same binary, different frequency: occasional → continuous. That shift in framing, not new features, is what makes platform teams buy in. Every move below serves that reframe.

## Design constraint, stated plainly

12 hours/month, 2 people, forever, already covers normal maintenance (issues, PRs, releases). Growth work gets whatever's left over — call it thin. So the filter for every tactic: does it cost time once and then run itself, or does it tax the 12 hours every single month forever? Only ship the first kind. This kills community platforms, content calendars, events, and ambassador programs before they start — not because they don't work, but because "12 hours a month forever" cannot fund their upkeep.

## Phase 1 (month 1–2, ~10h total, one-time): ship binaries, not just source

Biggest gap: nothing packaged downstream. Platform teams standardize on tools they can pin, checksum, and pull without a Rust toolchain. Individual SREs tolerate `cargo install`; platform teams won't.

1. **cargo-dist** — run `cargo dist init`, wire it into your release tag workflow. Generates GitHub Release binaries, install shell script, checksums, for every target triple, on every tag push. ~4-6h to set up once, 0h recurring — it fires on its own on every release.
2. Homebrew tap — `brew tap-new <org>/tap`, point formula at cargo-dist's output (it can generate the formula for you). ~1-2h once, ~5 min per release after.
3. Container image — GH Actions job, `docker buildx build --push` to GHCR on tag. ~2h once, 0h recurring. Platform teams running this in k8s/CI want a pinned image, not a binary fetch.
4. Nix — one PR to nixpkgs. ~1-2h once; nixpkgs maintainers own upkeep after merge, not you.

This phase eats most of 2 months' discretionary time. Worth it: everything after compounds on top of it, and it's the one item platform teams will actually block adoption on if missing.

## Phase 2 (month 2, ~2h, one-time): make the README speak platform-team

1. Add a "run in CI" section: drop-in GitHub Actions snippet, one copy-paste block, value in under 5 minutes. This is the self-serve path platform teams evaluate tools by.
2. Add a short doc: "use as a release gate" — same tool, framed as pipeline step not incident script. This is the reframe from Section 1, written down.
3. Leave a placeholder "used by" section — fill it in Phase 4.

## Phase 3 (month 2-3, ~2h, one-time, ~15 min/quarter after): widen discoverability

You have 1 accurate awesome-list entry. Add, don't multiply effort:

1. awesome-rust
2. awesome-sre or awesome-observability
3. awesome-chaos-engineering
4. LibHunt Rust category

Each a single PR following that list's contribution rules, ~15 min. No ongoing cost — they sit there and accrue backlink/discovery value forever.

## Phase 4 (month 3, ~3h, one-time, then opportunistic): turn 61 dependents into platform-team entry points

You already have a list of companies using qualmstone: your 61 dependents. That's warm, zero-outreach-cost signal most projects don't have.

1. Scan dependents for org/company accounts vs. personal projects (~1h).
2. Personally message 3-5 that look like real company usage: ask if they'll let you name them in "used by," or write 2-3 sentences on how they use it (~2h, they do the writing).
3. Publish that as social proof on the README and docs site. Platform teams adopt what other platform teams already run — this is the credibility signal that does the convincing, not you.

No formal ambassador program. Just a plain ask, maybe twice a year.

## Phase 5 (month 3, ~5-7h, one-time): one flagship asset, reused everywhere

Write once: "Replaying production traffic safely — lessons from building qualmstone," anchored on the release-gate reframe. Post it on your own site/GitHub Discussions, cross-post as-is to dev.to, submit yourself to r/rust and r/sre (accept the removal risk, don't hedge the post to please rules), and Hacker News as a plain technical post, not a launch. One asset, four placements, zero recurring cost, and it's the kind of page AI search tools cite when someone asks "how do I test staging with real traffic."

## Explicitly cut, and why

1. Podcasts — off-limits, per you.
2. Paid placements — off-limits, per you.
3. Discord/Slack community — recurring moderation tax you cannot afford at 12h/month forever; your users already live in existing SRE/Rust spaces.
4. Conference talks/CFPs — real value, but travel + prep cost is not sized to your budget; leave opportunistic, not planned.
5. Content calendar / regular blogging — unsustainable commitment; replaced by the single flagship asset above.

## Steady state after month 3

Roughly 30-60 min/month: bump the Homebrew formula version on release (cargo-dist mostly automates this), glance at new dependents quarterly, reply if a named user follows up. That returns ~11 of your 12 hours to actual maintenance, which was the point.

## Watch monthly, cheap to check

1. crates.io downloads trend
2. dependents count trend
3. GitHub clone/referrer numbers (Insights → Traffic)
4. install counts once brew/docker/nix are live
5. count of distinct companies among dependents/used-by — this is your real platform-team-adoption number, not downloads

## Open decisions, not glossed over

1. Whether either of you has ~2h to personally message the 3-5 champion companies in Phase 4 — this step is the one substitute for outreach you're not doing elsewhere; if it doesn't happen, platform-team adoption stays passive.
2. Nixpkgs PR review can stall for weeks outside your control — treat as best-effort, not a blocker for the rest of Phase 1.