Here are the numbers, with the convention each one is drawn from — pull straight from the Apache-style "lazy consensus" model and the CNCF/Kubernetes/Node.js governance templates, which is where most small OSS projects' GOVERNANCE.md numbers ultimately trace back to. No single body owns these, but this is the de facto convergence.

## Decision Making (draft section)

### Breaking changes
Minimum **14-day** public comment period (RFC/proposal filed as a GitHub issue or discussion) before a breaking change may be merged. Extend to **30 days** for changes affecting the public API broadly.
— 14 days is the standard lazy-consensus window; comfortably spans weekends and holidays across Lisbon/Bangalore/Vancouver.

### Approvals to merge
- Routine PR: **1 approval** from a maintainer who is not the author.
- Breaking / public-API change: **2 approvals** from maintainers who are not the author.

### Maintainer removal
Removal requires a **2/3 supermajority** vote of the *other* maintainers, excluding the maintainer being voted on. For Tinpot's 4 maintainers, that's **2 of the remaining 3** votes. Grounds: sustained inactivity, code-of-conduct violation, or voluntary resignation.

### Inactivity
- **3 consecutive months** with no commits, reviews, or issue/PR activity → flagged inactive.
- **6 consecutive months** inactive, or no response to a direct inquiry within 30 days → eligible for emeritus status / removal vote.

These are conventions, not a formal standard — but they're the values you'll see repeated almost verbatim across small-to-mid OSS governance docs, so they'll read as unsurprising to anyone who's seen a few.