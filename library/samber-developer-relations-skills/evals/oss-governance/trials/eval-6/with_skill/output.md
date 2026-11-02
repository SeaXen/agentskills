Straight values, each with the project that actually uses it — the skill this answer follows is explicit that this field has *conventions*, not standards, so I've kept the owner attached to each number rather than presenting them as universal. Adjust the one flagged below for your timezone spread (Lisbon/Bangalore/Vancouver spans ~12.5 hours, wider than most single-region projects these figures come from).

**Comment period before a breaking change**
10 days minimum (at least 5 business days) — Rust RFC process, final comment period.
Fits Tinpot better than Node's general 72-hour window because it's specifically the breaking-change/API-removal case, and your timezone spread needs the longer window to actually reach everyone once.

> Changes to public API behaviour require a design proposal, a 10-day comment period, and approval by two maintainers with no unresolved objection.

**Threshold to remove a maintainer**
Two-thirds supermajority of existing maintainers — pattern shared by Python PEP 13 (removal/amendment) and CNCF/GitHub Minimum Viable Governance templates.
For Tinpot's 4 maintainers, two-thirds rounds up to 3 of 4.

> Maintainer removal requires approval from at least 3 of the 4 maintainers, by vote.

**How long before someone counts as inactive**
6–12 months of very low activity — CNCF elections/maintainer-council templates and GitHub's Minimum Viable Governance; no tighter published figure exists. For a 4-person maintainer set (not a large committee that can absorb one quiet member), pick the low end so the project doesn't carry a silent vacancy for a year:

> A maintainer who has had no commits, reviews, or triage activity for 6 months moves to emeritus status, reversible by rejoining.

**How many approvals to merge**
Two approvals normally, dropping to one once the change has sat 7 days — Node.js `GOVERNANCE.md`. This is the one the skill's own reference flags as the single most useful import for a small maintainer set, specifically because it stops the project stalling when one of four people is unavailable (which, across Lisbon/Bangalore/Vancouver, will be often).

> Routine changes require approval from two maintainers, or one maintainer if the change has been open for review for at least 7 days with no objection.

One flag before you paste these in: none of the four is Tinpot-specific — they're what Node, Rust, Python, and CNCF happen to run. If any of your 4 maintainers has run an OSS project with different numbers before, that experience should outweigh these defaults.