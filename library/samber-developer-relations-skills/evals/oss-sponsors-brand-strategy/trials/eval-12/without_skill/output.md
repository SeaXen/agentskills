## Budget-close sponsorship review — recommendations

**1. hexpath ($9k) — don't pull it as a signal.**
- Separate the two problems. The broken build is an engineering problem: pin the last-good version, patch around the change, or migrate off the new API today, independent of anything else.
- The funding decision is a governance problem, and "maintainer wouldn't do what I wanted" isn't a legitimate reason to cut it. No-strings sponsorship is the only kind serious maintainers accept — tying it to a specific merge decision converts it into a de facto SLA you never actually paid for, and that's the same trap you'd criticize if a vendor did it to you.
- Cutting funding doesn't revert the commit and doesn't fix your build. It does read as retaliation to a maintainer you're still structurally dependent on, and maintainers compare notes — this can cost you goodwill on every other project you sponsor.
- If this is a pattern (unresponsive, hostile to downstream consumers generally) rather than a one-off, that's a real renewal-time signal — "this project's risk/relationship profile changed" — reassess it at the normal cycle with that framing, not as a same-week punitive move.

**2. dustmote ($200/mo, 26 months dark) — let it lapse, but verify first, and don't hide it.**
- Spend 10 minutes confirming "no commits" actually means abandoned: check issue/PR response times and whether it's marked feature-complete vs. dead. Silence isn't always abandonment.
- If confirmed dead: letting it lapse is correct — $4,800 paid over two years bought zero maintenance. No dramatic announcement needed, but don't actively conceal it either; a one-line answer ("no activity in 2+ years") should be ready if anyone asks. "Quiet" is fine, "hidden" is not.
- This is a funding decision only. If dustmote is still a live dependency, the abandonment itself is a separate engineering risk (unpatched, no bus factor) — flag that to engineering regardless of what you do with the sponsorship.

**3. Four other sponsorships — don't do a zero-touch renewal.**
- Full review can wait — that's a legitimate prioritization call under time pressure.
- But "let them run" as literally no review is how you get a second dustmote next year. Spend ~20 minutes total, not zero: confirm each is (a) still an actual dependency, (b) shows any commit/release activity in the last 12 months, (c) amount still looks sane. That's a sanity pass, not a strategic review.
- Put a firm date on next year's calendar for the real review now — "pick it up next year" without a forcing function is exactly how it slips again.

**4. Dependency list — don't fully redo, but don't trust last year's categorization blind either.**
- Diff this year's lockfile/SBOM against last year's list. That's cheap and tells you what's new, what's gone, and what's unchanged — no need to re-derive the whole inventory from scratch.
- Separately, re-check the *methodology* last year's list used, not just its age. Two failure patterns to rule out before trusting it: (a) maintainer counts pulled from GitHub's contributors graph instead of the npm registry's actual `maintainers` field — those diverge often and the registry field is the real bus-factor signal; (b) anything not found during the audit silently marked "fine" — that inflates coverage and hides exactly the low-star, single-maintainer, load-bearing risk (the dustmote/hexpath shape) a stars- or activity-sorted list is built to miss.
- If either shortcut is present, fix the scoring layer for this year's pass even where the package inventory itself hasn't changed — a stale methodology is a bigger risk than a stale list.