Here is the complete 12.4 LTS release notes document, written for change-approval-board intake rather than as a developer changelog. It follows the structure banks and insurers already recognize from vendor security bulletins (CVE/CVSS block, explicit before/after behavior, explicit support-lifecycle dates), because matching a genre they already know how to process is what prevents the "please provide detail" reply — not adding more prose.

Fields only you can fill are marked `[ ]`. Everything else is finished text.

---

# Ridgeway Platform — Release Notes: Version 12.4 (LTS)

## Document Control

| Field | Value |
|---|---|
| Product | Ridgeway |
| Release | 12.4 (Long-Term Support) |
| Classification | `[e.g. Confidential — for distribution to licensed customers only]` |
| Publication date | `[YYYY-MM-DD]` |
| Supersedes | Release Notes — Ridgeway 12.3 LTS |
| Document owner | `[name, role, contact email]` |
| Revision | 1.0 |

## 1. Purpose and Scope

This document lists every customer-impacting change in Ridgeway 12.4 LTS: one security fix, one behavior change in LDAP directory synchronization, one deprecation, and a change to Ridgeway's release cadence. Each item states what changed, why, who is affected, and what action is required before and after upgrade, so this document can be attached to a change record without further clarification from Ridgeway support.

## 2. Change Summary

| ID | Category | Title | Risk rating | Pre-upgrade action required | Downtime required |
|---|---|---|---|---|---|
| CHG-1 | Security | `[short title]` | `[Critical/High/Medium]` | No (patch supersedes) — see §4.7 for interim mitigation if upgrade must be delayed | `[Yes/No — duration]` |
| CHG-2 | Behavior change | LDAP group-membership synchronization | Medium | Yes — directory audit before upgrade, §5.5 | No |
| CHG-3 | Deprecation | `[feature name]` | Low | No — plan migration before removal date, §6 | No |
| CHG-4 | Process | Release cadence change to twice-yearly | Informational | Update internal patch-management calendar | No |

## 3. How to Read This Document

Each numbered change below follows the same structure: **Summary → Previous behavior → New behavior → Why → Who is affected → Required action → Verification**. Sections that don't apply to a given change type (e.g. "previous behavior" for a new security fix) are omitted rather than left blank, so absence of a field is not itself something to query.

## 4. CHG-1 — Security Fix

| Field | Value |
|---|---|
| Identifier | `[CVE-YYYY-NNNNN]` |
| CVSS v3.1 score | `[score] ([full vector string, e.g. AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N]` |
| Severity | `[Critical/High/Medium/Low, per CVSS band]` |
| Affected component | `[e.g. report export service, listening on port NNNN]` |
| Affected versions | `[e.g. 12.0.0 through 12.3.x; 11.x is not affected because ...]` |
| Attack vector (plain language) | `[e.g. "A user with a valid but unprivileged Ridgeway session can retrieve records belonging to another tenant by modifying a request parameter." State authentication and privilege prerequisites explicitly — this is the sentence a risk officer quotes into their own risk register.]` |
| Public disclosure status | `[e.g. Not publicly disclosed; no known proof-of-concept; reported via our responsible-disclosure program on [date]]` |
| Discovered by | `[internal QA / external researcher, credited or anonymous per their preference]` |

**Description.** `[2-4 sentences: what the flaw is and what an attacker gains — enough for a risk assessment, not implementation detail that would itself constitute an exploit guide.]`

**Remediation.** Upgrade to 12.4 or later. The fix is contained entirely within `[component]`; no configuration change is required to activate it.

**Interim mitigation (if upgrade must be deferred).** `[e.g. Restrict network access to the affected port via firewall rule; disable the affected feature via config flag X. State explicitly if no mitigation exists other than upgrading — that itself is a fact the CAB needs, not a gap to hide.]`

**Verification.** After upgrade, confirm the fix is active by `[e.g. checking that /version reports 12.4.0 or later; the fixed behavior has no user-visible confirmation step].`

## 5. CHG-2 — Behavior Change: LDAP Group-Membership Synchronization

**Summary.** `[One sentence naming the mechanism, e.g. "Ridgeway's LDAP sync now resolves nested group membership; it previously evaluated only direct membership."]`

**Previous behavior (12.3 and earlier).** `[Describe precisely: which attribute/query was used, what was and wasn't evaluated.]`

**New behavior (12.4).** `[Describe precisely what changes at the next sync after upgrade.]`

**Why this changed.** `[State the real reason — bug fix, security hardening, alignment with AD/LDAP spec behavior, customer request. Regulated readers weight "why" heavily; a change with no stated rationale reads as arbitrary and gets escalated.]`

**Who is affected.** Any environment where:
- `[condition 1, e.g. users are granted access via nested/transitive group membership rather than direct membership]`
- `[condition 2, e.g. local group overrides exist that assumed flat resolution]`

Environments using only direct group membership are unaffected.

**Impact if not reviewed before upgrade.** At the first sync after upgrade, some accounts may gain access they did not previously have (via a nested group they belong to), and some accounts may lose access that depended on the old resolution behavior. This can change effective authorization without any explicit administrative action, which is why this is flagged as a behavior change requiring pre-upgrade review rather than a routine bug fix.

**Required pre-upgrade action.**
1. Export current effective group membership: `[command/report Ridgeway provides, if any — if none exists, say so and recommend the customer's own AD/LDAP tooling]`.
2. Compare against the nested-resolution result to identify accounts whose access will change. `[Provide a dry-run/report-only sync mode if Ridgeway has one — this is the single highest-value thing you can give a CAB for this change; if it doesn't exist yet, say so explicitly so they know to plan a manual review instead of expecting tooling.]`
3. Have the accountable access owner sign off on any resulting access changes before the sync runs against production.

**Rollback consideration.** Reverting to 12.3 does not automatically restore prior effective access; a subsequent sync under the old binary would need to run to re-resolve direct-only membership. State expected time to re-sync: `[duration]`.

**Verification after upgrade.** `[e.g. re-run the membership report and confirm it matches the pre-upgrade reviewed delta, with no unreviewed changes.]`

## 6. CHG-3 — Deprecation Notice: `[Feature Name]`

| Field | Value |
|---|---|
| Deprecated in | 12.4 |
| Status in 12.4 | Still fully functional; `[emits a warning in logs / admin UI banner / no runtime warning — state which]` |
| Replacement | `[feature/mechanism name and where documented]` |
| Earliest removal release | `[e.g. not before 13.0]` |
| Minimum notice period | 12 months from this notice, per Ridgeway's deprecation policy — see §7 for how this maps to the new release calendar |

**Why this is being deprecated.** `[reason — superseded by replacement, security posture, maintenance cost]`

**Migration steps.**
1. `[step]`
2. `[step]`

**Support during transition.** The deprecated feature continues to receive security fixes until removal. It will not receive new functionality. `[Contact/escalation path for migration assistance, if offered.]`

## 7. CHG-4 — Release Cadence Change

**What is changing.** Starting with 12.4, Ridgeway moves from `[previous cadence, e.g. approximately quarterly minor releases]` to a fixed twice-yearly cadence, with releases in `[month]` and `[month]` each year.

**Why.** `[State the real reason honestly — e.g. "to give customers a longer, predictable window to complete their own change-approval and regression-testing cycles before the next release," or whatever the actual driver is. A cadence change with no stated rationale invites the assumption that it's cost-driven, which itself generates a follow-up question — pre-empt it.]`

**What does not change.** Security fixes are not bound by this cadence. A vulnerability meeting `[severity threshold, e.g. High or Critical]` will ship as an out-of-band patch release regardless of where it falls in the twice-yearly schedule, following the same disclosure and notification process as CHG-1 above.

**Support lifecycle for 12.4 specifically.**

| Milestone | Date |
|---|---|
| General availability | `[date]` |
| End of full support (fixes + new features) | `[date]` |
| End of security-only support | `[date]` |
| Next scheduled release | `[month, year]` |

**Action for your change-management calendar.** Because customers on this product typically run two to three minor versions behind, this cadence change lengthens the interval between your upgrade cycles from `[old interval]` to `[new interval]`. Update internal patch-planning schedules accordingly; no action is required in the Ridgeway environment itself.

## 8. Upgrade Path and Compatibility

| From version | Supported upgrade path to 12.4 |
|---|---|
| `[12.3.x]` | Direct |
| `[12.2.x]` | Direct |
| `[12.1.x and earlier]` | `[Must first upgrade to 12.3.x, or direct — state which]` |

**Platform compatibility changes from 12.3.** `[List any OS, JDK/runtime, database version, or LDAP/AD version floor changes. If none, state "No platform compatibility changes in this release" explicitly — an unstated "no change" reads as an unchecked field, not a confirmed one.]`

**Pre-upgrade checklist.**
- Complete the CHG-2 directory audit (§5.5).
- Back up `[what, and how]`.
- Review CHG-3 if using `[deprecated feature]`.

## 9. Testing and Validation Evidence

`[State what was actually tested, and where, in enough detail that a CAB can cite it as evidence in their own risk assessment rather than asking for it: e.g. "CHG-1 was verified by Ridgeway's security team against the reported reproduction case and by an independent penetration test dated [date]. CHG-2 was validated against a synthetic directory with N levels of nested groups and against sanitized directory structures from two customer pilots." If pilot customers can be named with permission, that materially strengthens this section for other regulated customers.]`

## 10. Rollback Procedure

1. `[Stop service / steps]`
2. Restore `[backup taken in §8]`.
3. `[Any data written under 12.4's new LDAP behavior may not be compatible with 12.3 — state explicitly, per §5's rollback note.]`

Estimated rollback time: `[duration]`.

## 11. Support and Escalation

- Questions on this release: `[contact/queue, with a stated response-time commitment — e.g. "2 business days"]`.
- Security-specific questions on CHG-1: `[dedicated security contact, if different]`.
- Prior advisories: `[where archived, e.g. customer portal path]`.

---

A structural note, not part of the document: the twice-yearly cadence announcement (CHG-4) is the one item here that isn't a code change, and it's tempting to drop it into a cover email instead. Keep it in the formal notes — for a CAB, cadence *is* a change to their own process, and it's exactly the kind of thing that generates a clarifying email if it only appears informally.