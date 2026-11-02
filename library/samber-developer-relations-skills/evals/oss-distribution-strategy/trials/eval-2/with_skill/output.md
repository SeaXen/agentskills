## Should tallowpy go into Homebrew and Debian? No.

**Verdict: refuse both, redirect the "legitimacy" instinct to trust signals instead.** Here's the reasoning, and what to do with the hours instead.

### Why this is a wrong-channel-shape problem, not a capacity problem

tallowpy is a Python library, installed with `pip install tallowpy` inside a virtualenv/poetry/conda environment, imported into someone's ETL script. That's the install unit. Homebrew and Debian packaging exist for standalone binaries and system tools — things a user runs from a shell prompt, not things a data engineer imports into a `requirements.txt`. Packaging a library that way doesn't fix a broken install path (pip already works, everywhere your users already work); it adds a second install path that has to stay in lockstep with the first one, forever, for an audience that won't use it.

### The adoption test, answered

- **Recurring cost** — high. Debian packaging means learning `debian/` packaging conventions, finding a sponsor to upload, and tracking Debian's freeze cycles on every release. Homebrew means a formula kept in sync with every tag. Neither is a one-time cost.
- **Decay behaviour** — harmful, not silent. A stale Debian or Homebrew build keeps serving a year-old fixed-width parser to the exact evaluator you're trying to look legitimate for — in a domain (mainframe extract parsing for insurance data) where a silently outdated offset/encoding bug is a real cost, not a cosmetic one.
- **Observable signal** — none. Nobody is currently blocked from installing tallowpy. The two requesters already found it and presumably already have it running — this is a convenience/prestige ask, not a blocked-adoption signal.
- **Kill date** — moot, because it fails on entry (see below), so there's nothing to time-box.

### The specific checklist for promoting downstream packaging (from the framework) — fails on the sharpest line

Downstream packaging only earns priority when all four hold:
1. Company adoption is the *declared* goal — not established here; nothing suggests insurance-company data engineers are procurement-blocked on `pip install`.
2. **The install unit is a standalone binary or container image, not a library inside someone else's dependency file — fails outright.** tallowpy is exactly the library-in-a-dependency-file case.
3. Release hygiene is good enough for a third party to hold the recurring cost — unknown, and irrelevant once #2 fails.
4. The maintainers accept that a shipped package can't be unshipped — also moot.

One failed condition kills it; you have one failed on the least negotiable axis.

### Homebrew specifically has a hard numeric gate you'd likely miss anyway

`homebrew-core` requires roughly 30 forks / 30 watchers / 75 stars on the canonical repo for a third party to submit it, and **3x that (90/90/225) if you submit it yourselves** — that threshold moved pages recently but is still live policy. For a niche mainframe-parsing library, check your actual numbers before spending a minute on this; it's very likely you don't clear it. The fallback is a self-owned tap, which is a private, effectively unbrowsed listing — you'd be doing packaging work for a channel nobody discovers you through.

### Formal refusal

- **Channel:** Homebrew formula, Debian package.
- **Reason:** library install unit, not a binary; no blocked-install signal; recurring cost doesn't fit a 6-hour/month total budget for two people; Homebrew's own acceptance bar is likely unmet.
- **Condition that reopens it:** tallowpy grows a standalone CLI/binary component installed outside a Python project (e.g. a converter tool ops teams run directly) — or a customer's procurement process names "no system package available" as an actual blocker, not a preference.

### What to do with the hours instead — this is what "legitimacy" actually buys

Your co-maintainer's instinct isn't wrong, the channel is. What insurance-company data engineers say moves their trust in a dependency (Larios Vargas et al., ESEC/FSE 2020, 115 practitioners): maturity/stability 62%, usability 55%, documentation 51%, license 45%, active maintenance 44%. None of that requires a second package manager. It requires:

- **PyPI metadata fully filled** — description, classifiers, license, docs/repo/funding links (~1 hour, one-time, minutes per release after).
- **A stable/maintained statement in the README** — cheap, and it's the correction for the exact "is this still alive" doubt a Debian-package request is usually a proxy for.
- **SECURITY.md with a disclosure path, a real CHANGELOG, a stated release cadence** (~2 hours, one-time).
- If you want a genuine trust signal: wire PyPI Trusted Publishing + Sigstore attestations through GitHub Actions (~1–2 hours, one-time setup, then free on every release). This is what actually reads as "legitimate" to a security-conscious evaluator, and unlike a distro package it doesn't decay — you set it once and it holds.

Total: 4–6 hours, one-time, fits inside a single month, and afterward costs almost nothing to hold — the opposite of what packaging would have cost you every month, indefinitely.

### What to tell the two requesters

Close both issues with the same answer: `pip install tallowpy` already works inside any venv, poetry, or conda environment, which is where your actual users are. If either of them is asking on behalf of a company that needs installs to go through a controlled/audited path, point them at pulling PyPI through their own artifact proxy (Artifactory/Nexus/devpi with an allowlist) — that's the real "trusted distribution" mechanism regulated-industry Python shops already run, and it needs nothing from you.