**Answer: no newsletter now, and not "Ferrule Friday".** Set up feed-only: GitHub releases plus an Atom feed and release emails GitHub sends to watchers. Revisit in 90 days with a pre-agreed test. About 40 minutes of setup, then about 20 minutes a month.

**Do this first (≈40 min total):**

1. Rewrite the release-notes template (below) as a `.github/release.yml` or a pinned text snippet. About 15 min.
2. Add a "Watch → Custom → Releases" line to the README, the docs install page, and the footer of each release. About 15 min.
3. Link `https://github.com/<org>/ferrule/releases.atom` from the README and docs. About 5 min.
4. Put a dated reminder for 2027-01-22: run the demand test. About 2 min.

## Why not weekly

- Supply: about 2 releases a month, no blog. A weekly issue needs 4 issues × 5–7 items = 20–28 items a month. You have about 2. Padding would start in week 2.
- Hours: 4 issues inside a 1-hour comms budget leaves 15 min each, with nothing left for everything else.
- Demand: no list, no reader request. "Advisors say so" is not reader evidence.

## Charter

**Gate result: fail, so feed-only.**

| Condition | Result | Evidence |
|---|---|---|
| Supply fills the sections at the supported cadence | ❌ fails weekly. Monthly is **unproven** | 2 time-bound items a month. Evergreen reserve unknown: no docs walkthroughs or tutorials counted. Fastest cadence supply supports: monthly, thin |
| Named owner and backup, with hours | ❌ fails | No owner, no backup named. Ceiling is 1 h/month for all comms |
| Readers want email, not a feed | ⚠️ **unproven** | No list, no requests. Advisors are not readers |

**Shapes deleted:**

- Curated ecosystem: effort ceiling under 4 h and no backup.
- Personal letter: no backup.
- Community-edited: a quarter of setup, no contributor base known.
- Own-surface digest: survives the ceiling rule but fails the gate for now. It is the first upgrade, not the starting point.

**Shape: feed-only.** Your public changelog is the GitHub releases page. It already has an Atom feed and watcher emails. No editor, nothing to hand over, no consent duty on you, because GitHub holds the subscription. Ranked first on efficiency and durability.

**Cadence and rhythm anchor.** No newsletter cadence. Each release note ships with its release, anchored to your release train (about 2 a month).

**Curation rule.** None needed: own content only, no external items, no sponsors. If a digest starts later, the house rule is at least 1 external item per issue, with written criteria. That is a house rule, not an industry ratio.

**Section template.** The release-note template is the only template.

| Section | Source | Owner | Items | When empty |
|---|---|---|---|---|
| What changed | PR titles | releaser (backup: second engineer) | 1–5 | never empty |
| Breaking or upgrade steps | diff | releaser | 0–3 | write "None" |
| Hosted tier impact | deploy log | releaser | 0–2 | write "None" |
| Thanks | contributor list | releaser | 0–n | drop the section |

**Ownership and handoff.**

- Owner: whoever cuts the release. This is a rotating role, not a person.
- Backup: either other engineer.
- Reviewer: not needed for feed-only.
- Hours: about 10 min per release, so about 20 min a month. That leaves about 40 min for everything else in your 1 hour.
- Accounts: the GitHub org owns the repo and feed. No personal accounts hold anything.
- Runbook: the template, kept in the repo next to the release process.
- Running cost: €0.

**Measurement.**

- Primary signals are click-based. For feed-only that means the number of people asking for an email option, and release-page referrals from the docs.
- Outcome signal for the funding answer: **blocked**. Question 2 (why fund this) is unanswered. Pick one: retention, reach to non-users, or contributors.
- Opens are never a target.
- Review quarterly.

**Pause and sunset rules (house rules).**

| Trigger | Action |
|---|---|
| Release notes skipped for 2 releases | Fix the template or drop the section |
| 90-day demand test passes (below) | Start a monthly own-surface digest, not weekly |
| Owner can't be filled | Keep feed-only; there is nothing to hand over |
| Hosted-tier incident or security notice | Send as transactional email, never in a newsletter |
| Digest later has 2 thin issues in a row | Fall back to feed-only with a final pointer issue |

**Demand test, on 2027-01-22. Upgrade to a monthly digest only if all three hold:**

- At least 5 unprompted requests for an email option in 90 days (issues, Discord or chat, DMs).
- A named backup has agreed, and the budget is raised to 3 hours a month.
- At least 2 evergreen items exist, such as docs walkthroughs, to cover the first two issues.

Name it "Ferrule Monthly" if it starts, since the Friday framing implies a weekly rhythm.

**Consent.** Do not add hosted-tier signups to a newsletter list. Keep it as a separate, opt-in stream. UK and EU individual addresses need consent or a valid soft opt-in. Keep newsletter content out of billing, security and account email.

## Open questions

- Who is the owner and who is the backup? **Blocked**, owner is you. Re-check 2027-01-22.
- Who is the primary reader: existing users, evaluators, or contributors?
- Why fund it (Q2)? This sets the outcome signal.
- Do you have docs walkthroughs or tutorials? This sets the evergreen reserve.
- Is the hosted tier's user list already collected, and with what consent? Matters only for a later digest.
- Any off-limits items, such as unannounced features, named customers, or competitor comparisons?

## Pass thresholds

- ✅ Gate states all three conditions with evidence.
- ✅ Cadence is derived from supply and hours.
- ✅ Template sections have source, owner, items and an empty rule.
- ✅ No open-derived primary metric.
- ✅ Every pause trigger has an action.
- ✅ Consent and stream separation are stated.
- ❌ Owner and backup are not yet named people. **Blocked**, re-check 2027-01-22.
- ❌ Outcome signal is blocked on Q2.

Next: do setup step 1, the release-notes template.