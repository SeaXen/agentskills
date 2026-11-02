**One reason: the "every big project has them, so it signals professionalism" belief is exactly the bias the only rigorous study on this measured — and it measured it in maintainers, not readers.**

Trockman et al. (*Adding Sparkle to Social Coding*, ICSE 2018, 294,941 npm packages) surveyed 32 maintainers and 57 contributors: 88% of maintainers rated badge presence as a quality indicator, against 53% of contributors — and 61% of contributors said badges don't influence their decision at all. When you say badges make the project "look professional and serious," you're reporting the maintainer-side number. Your reader is more likely in the 61%.

The same study also breaks your "every big project has them" logic: adopting a badge does not raise popularity — popular projects are simply more likely to already have one. And among already-popular packages, **excessive badge use correlates with decreased popularity.** slotcache, at ~4,000 stars, sits exactly in the population where the correlation runs against you, not for you.

That's the one reason. Applied to your specific row, badge by badge, using the study's own distinction — an **assessment signal** is backed by a check that can't pass unless the underlying fact is true; a **conventional signal** just states an intent:

- **Cut — contributor count.** No check backs it, and it's the study's own example of a badge that "almost never changes an adoption decision." It tells a visitor nothing about whether to depend on slotcache.
- **Cut — 'PRs welcome'.** Textbook conventional signal. Every repo could say this whether or not it's true; it carries zero information.
- **Cut — 'Made with Rust'.** Pure decoration — the crates.io badge already proves the language. This is the "Built with ❤️" pattern the skill flags as a trust-cost, not a trust-gain.
- **Cut or downgrade to a plain link — Discord.** Functionally identical to the "chat" badge in the study's negative example set. If community matters, a text link in a "Community" section does the same job without occupying the scarce top-of-page real estate.
- **Cut — downloads.** No adoption-relevant check backs it, and like stars, it only ever climbs — it can't tell a reader anything about current health, so it's noise dressed as a signal.
- **Reconsider — coverage 94%.** It is mechanically an assessment signal (a real tool produced it), but it's the study's second named example of a badge that rarely moves an adoption decision. Keep it if you're pitching to security/procurement readers who screen on it; cut it for everyone else.

That leaves four real assessment signals worth the space: **build status, crates.io version, docs.rs, MSRV**. Each answers a question a developer actually asks before depending on a crate — does it build, what version, where are the docs, what toolchain do I need. Licence stays regardless of this whole argument; 64–67% of developers rate it as very important to use/contribute decisions (GitHub 2017 OSS Survey) — that's not a badge argument, that's a disclosure one.

The cap of four is a working default from this skill, not a published number — the actual rule is narrower and harder to argue with: for every badge, name the decision a first-time visitor makes differently because of it. If you can't name one, it's decorating the page for you, not informing the reader.