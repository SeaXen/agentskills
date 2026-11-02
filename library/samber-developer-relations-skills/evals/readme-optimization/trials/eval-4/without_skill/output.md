Badge count doesn't read as "serious" — it reads as insecure. Look at the Rust projects with real trust (tokio, serde, rayon): their badge rows are four items, not eleven. Past 5-6 badges, each additional one subtracts credibility rather than adding it, because it signals you're padding.

Here's the row, badge by badge:

**Cut — coverage 94%**
A coverage percentage is gameable and doesn't measure correctness, especially for a cache crate where the real risk is concurrent/unsafe edge cases, not line count. It invites a reviewer to ask "what's in the missing 6%" — a question you can't win, since the honest answer is usually "the hard part."

**Cut — downloads**
crates.io download counts include every CI run and every `cargo build` after a lockfile bump, not unique users. It's a number that looks impressive until someone who knows crates.io points out what it actually measures.

**Cut — 'PRs welcome'**
Unverifiable self-praise — any repo can claim it, so it carries zero information. Worse, it invites unfiltered drive-by PRs with no contribution bar; put that expectation in CONTRIBUTING.md where it can carry actual rules.

**Cut — 'Made with Rust'**
GitHub already shows the language bar, and 100% of the visible code is Rust. This badge states something the visitor's eyes already told them — pure decoration, no signal.

**Cut — contributor count**
Next to 4,000 stars, a small contributor count doesn't say "healthy community," it says "bus factor of one or two." You're volunteering evidence of your own fragility.

**Cut (or make conditional) — Discord**
A member-count badge is a liability the moment the server is quieter than the number implies — anyone can click through and see "12 online." Link to Discord in the text if you want it discoverable; only badge the count if it's genuinely impressive.

**Keep, but only if enforced — MSRV**
An MSRV badge nobody's CI actually checks is a claim you're not testing, which is worse than no claim at all. Keep it only if a pinned-toolchain job fails your build on violation.

**Keep — build status, crates.io version, docs.rs, licence**
These answer the four questions a new user actually has: does it build, what version, does it document, can I legally use it. Everything else on your list is decoration or downside.

Net: cut five (coverage, downloads, PRs welcome, Made with Rust, contributor count), make Discord conditional, verify MSRV is real — land at 4-5 badges, not 11.