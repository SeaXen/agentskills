**Short answer: no, not now — the ROI doesn't work at 6 hours/month.**

**Why the requests don't hold up**

- Homebrew and apt/Debian solve "I want to run a standalone tool," not "I want to import a library." Unless tallowpy ships a CLI, a Homebrew formula is close to a non-starter anyway — homebrew-core's own acceptance bar wants notable end-user software, not a niche parsing library, so you'd land in your own tap regardless. If there's no CLI, this is off the table structurally, not just on cost.
- Your actual users — data engineers at insurance companies — already have Python and pip as a job requirement. Nobody doing ETL work is blocked by "no brew formula." One issue and one comment is enthusiasm from a couple of users, not a demand signal from your ~4,800 monthly installs.
- Debian's official archive means an NEW-queue review (often months) and a sponsor with upload rights; your own apt repo skips that but you're now maintaining a repo, signing keys, and packaging metadata yourself.

**Why it's a bad trade at your capacity**

- Both are one-time work plus permanent upkeep: every PyPI release means touching the formula/control file, testing, resubmitting. That's recurring, not one-off.
- 6 hours/month for two people is already tight for bug fixes and releases. Two new packaging pipelines to babysit forever will eat a third to half of that some months — for a channel your own users don't need.
- You'll also inherit support burden you don't have today: "brew install fails on Apple Silicon," "apt package conflicts with system Python" (especially now that PEP 668 discourages system-Python installs anyway).

**On the "legitimacy" argument**

That's the only real motivation here, and it's worth taking seriously — but distro breadth isn't what reads as legitimate to the people actually vetting a library at an insurance company. Procurement/security teams there look at PyPI provenance, license clarity, changelog discipline, test coverage, and responsive maintenance — not whether it's on Homebrew. Cheaper, higher-signal moves for the same "we look legitimate" goal:

- Trusted publishing / signed releases on PyPI (OIDC, sigstore) — one-time setup, no recurring cost.
- CITATION.cff, security policy, CI badge — hours, not a channel to maintain.
- **conda-forge**, if you want a second distribution channel at all: this audience is far more likely to be on Anaconda/conda than Homebrew or Debian, and conda-forge's bot auto-opens a PR on every new PyPI release — upkeep is closer to "approve a bot PR" than "cut a release."

**What to tell the two requesters**

Close both issues with the same answer: pip is the intended and supported install path; Homebrew/Debian packaging isn't something the project can commit to maintaining at current capacity, but either of them is welcome to publish and maintain a community tap/PPA themselves and you'll link to it from the README if it stays current. That gets you the legitimacy signal ("community packaging exists") without you owning the maintenance liability.