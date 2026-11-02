No. The board's "bus factor of 4" looks like it was read straight off `git shortlog -sn` — count the humans above some noise floor (drop the bot, keep Priya/Tomas/Ines/Karl, ignore the four in the tail) — but that's a commit-volume ranking, not a bus factor. Bus factor asks: how many people can disappear before something breaks irrecoverably. That's determined by the *thinnest* point of knowledge/access, not by how many names clear a volume threshold.

Two single points of failure sit right in the data you gave me:

- **Windows backend: bus factor 1 (Karl).** Nobody else has touched it in two years. If Karl leaves, that subsystem has zero people who understand it — full stop, regardless of how active Tomas or Ines are elsewhere.
- **Release process: bus factor 1 (Priya).** She's the sole holder of the npm token and the signing key. If she's unavailable, nothing ships — doesn't matter how many people can write and merge code, publishing is gated on one person's credentials.

So the real number is **1**, not 4 — and it's 1 for two independent reasons (a knowledge silo and a credentials silo), which is worse than a single bus factor of 1 usually implies.

Also worth flagging: even the "4" is inflated on its own terms. 610 of Priya's 980 commits are merge-queue merges — mechanical clicks, not authored changes. Her actual authorship volume is ~370, still second-highest, but it means the shortlog overstates how much distributed codebase knowledge that number represents. A raw commit count treats a one-line merge commit the same as a deep authored change, which is exactly the kind of thing that makes "count committers above a threshold" a bad proxy for resilience.

What would actually fix the metric:
- Compute bus factor per subsystem (git blame / ownership by directory, not just aggregate commits), since Windows backend and "everything else" are clearly not the same population.
- Treat credentials/access (signing key, npm token, deploy keys, admin on CI) as their own bus-factor dimension — a person can be replaceable on code and still be a single point of failure on shipping.
- Exclude bot commits and separate merge commits from authored commits before ranking anyone by "contribution."

Recommend correcting the board deck to bus factor 1, with the two named risks (Karl/Windows, Priya/release credentials) as the explicit callouts — that's a more useful and more alarming number than "4," and it's actionable: rotate a second person onto Windows backend, and get the signing key/npm token into a second pair of hands (or a shared secrets/CI-managed release flow) before either becomes an incident.