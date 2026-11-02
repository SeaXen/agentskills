## Where "500K developers" actually comes from

It's **412K + 88K = 500K**, npm downloads plus PyPI downloads, last month. That arithmetic is on the skill's explicit refuse-list, for two independent reasons:

- **A downloads count is not a users count.** npm counts "the number of HTTP 200 responses served that were tarball files" — every CI run, Docker build, and lockfile reinstall counts as a download. One developer's project can generate hundreds of installs a month with zero new humans involved. npm's own guidance treats sub-~50/day as mostly automation; above that, it's still a request count, not a person count.
- **You can't sum two registries.** npm and PyPI use different counting policies (PyPI excludes known mirrors by default and publishes a separate with-mirrors series; npm doesn't exclude mirrors, bots, or CI at all). Adding them produces a number that isn't measuring one consistent thing, and there's no dedup for the same developer pulling both the JS and Python client (a full-stack team, or a CI matrix testing both, is double-counted).

So: **there is no legitimate reading of "500K developers" from the numbers you have today.** It's 500K download-events, most of which are almost certainly machines, not people.

## What to tell the associate today

Don't defend the 500K/developers framing — it won't survive five minutes of their own npm-stats lookup, and getting caught on an easily-checked number is worse for the round than a smaller, correct one. Send this:

> "The 500K figure is combined package-manager downloads last month (412K npm + 88K PyPI), not a unique-developer count — we don't currently have telemetry that resolves downloads to distinct developers, since npm/PyPI download counts include CI, Docker builds, and mirrors by design. We're correcting the deck to say '500K downloads/month across npm + PyPI (Sept 2026)' and are scoping install-level telemetry to get a real developer-count metric for the next update."

That's honest, sourced, and still a strong number — half a million monthly installs is real signal of adoption, it's just not "developers."

**Fix the deck now:** change the slide to "500K package downloads/month" (or split npm/PyPI with their own labels) before this goes out again. If you want an actual developer estimate later, the only credible paths are: authenticated calls to a hosted backend/API if Orbitlane talks to one (unique API keys = real developers), or opt-out CLI/install telemetry documented like Next.js's (command/version/OS only, no code/paths/args, one env var to disable) — both are weeks-to-quarter builds, not something to cite today.

## Should you worry about the npm drop?

Not on this data alone. A single week-over-week swing in a registry download count is close to expected noise, not a signal, for a few concrete reasons:

- **Registry downloads are dominated by machines, not people.** A 30% WoW move is easily explained by CI cadence, a version bump (bumps typically cause a temporary spike as everyone's lockfiles reinstall, then a reversion the following week that looks like a "drop" but is really the spike week that was the anomaly), or one large downstream dependency changing its pin.
- **One week is below the noise floor.** Volatility in a rate is expected; the fix is a longer window, not a reaction. Look at trailing 8-12 weeks of npm's daily series, not one delta.
- **It's single-source.** Trust ratios inside one source, not absolutes across sources — check whether PyPI moved the same week. If PyPI is flat while npm alone dropped, that points to something npm/CI-specific (a downstream project's pipeline, a registry-side hiccup) rather than real developer attrition.

**What to actually check before Monday, in order:**
1. Pull npm's daily download series for the last 8-12 weeks (not just last week vs. this week) — is this a trend or a blip?
2. Did you ship a release recently? Check if the prior week was an unusually *high* spike (reinstall wave) that this week is reverting from.
3. Compare PyPI's trend for the same period — moved together or diverged?
4. Check GitHub repo traffic (clones/views — only a 14-day window, so pull it today or lose it) for the same week.
5. Check npm's status page for a registry incident that week.

If the drop persists across multiple weeks after controlling for release timing, *and* it's corroborated by a second signal (PyPI, repo traffic, support volume, actual telemetry) — worth investigating. A single week, on a metric that's mostly CI noise, is not.