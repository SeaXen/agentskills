Enterprise Release Advisory for Ridgeway 12.4 LTS below — paste-ready for your ticket system. `{{...}}` marks facts I don't have; fill those before publishing.

---

```markdown
INTERNAL NOTE — remove this block before publishing.

Assumptions made drafting this advisory (confirm or correct):
- Previous LTS line: 12.3.x. "Two to three minors behind" read as customers
  commonly running 12.1.x–12.2.x.
- Versioning scheme is LTS.minor (12.x), not strict SemVer — behaviour changes
  inside a minor are treated as normal for this product line, the way Red Hat
  ships RHBA enhancement/behaviour advisories inside minor releases. If your
  compatibility contract says otherwise, this release either needs a different
  version number or the LDAP entry needs a stronger warning. Pick one.
- No existing advisory numbering scheme was described, so one is proposed
  below (RGW-YYYY-NNN). Replace with your real scheme if one exists.
- Security fix, LDAP behaviour change, and deprecation target are described
  only at the level of detail given ("a security fix", "LDAP sync behaviour",
  "a deprecation") — every {{bracket}} below needs the real fact. Nothing
  bracketed should ship as-is.
```

```markdown
# Ridgeway 12.4 LTS — Release Advisory

**Advisory ID:** RGW-2026-{{NNN}}
**Release date:** {{2026-10-DD}}
**Product:** Ridgeway (on-premises)
**Applies to:** All supported 11.x and 12.x installations. See §2.
**Classification:** {{Public / Customer-confidential}} — contains a security fix; see §3 before distribution.
**Audience:** IT operations, security, and change-approval reviewers evaluating this upgrade.

## 1. Summary

Four items in this release change how the product runs or is supported. Each is detailed in its own section with the affected versions, the required action, and the deadline where one applies.

| # | Item | Category | Action required |
|---|------|----------|------------------|
| 1 | Security fix | Security | {{Yes — upgrade / patch by [date]}} |
| 2 | LDAP directory sync behaviour change | Changed | Yes — review configuration before upgrading |
| 3 | Deprecation of {{feature name}} | Deprecated | Plan migration; no action before 12.4 |
| 4 | Release cadence change | Lifecycle | None for this release; affects planning going forward |

## 2. Applicability

| If you currently run | Recommended action |
|---|---|
| 12.3.x | Upgrade to 12.4.0 directly. |
| 12.1.x–12.2.x | {{Confirm: is 12.4.0 a supported direct upgrade path, or must you step through an intermediate minor?}} |
| 11.x or earlier | {{Confirm: still within support? If out of support, state that explicitly here — do not let the reader infer it.}} |

{{Confirm: does Ridgeway backport the security fix in §3 to any currently-supported 11.x/12.x branch, or is upgrading to 12.4.0 the only remediation? This is the single fact your change board will ask for first — state it explicitly, do not leave it implied.}}

## 3. Security Fix

- **Advisory reference:** {{CVE-ID, once assigned — do not publish without one or an explicit statement that none was assigned}}
- **Severity:** {{CVSS v3.1 score and vector}}
- **Affected component:** {{component/module name}}
- **Affected versions:** {{version range}}
- **Fixed in:** 12.4.0
- **Description:** {{One or two sentences: what an attacker could do, under what precondition — not the internal cause. E.g. "An authenticated user with X permission could Y."}}
- **Workaround if you cannot upgrade immediately:** {{configuration mitigation, or "None — upgrade is the only remediation"}}
- **Required action:** {{Upgrade to 12.4.0 by [date] / Apply the mitigation above and upgrade at your next window}}

## 4. Changed: LDAP Directory Sync Behaviour

**What changes:** {{Precise before/after. Example shape only — replace with the real behaviour: "LDAP group membership sync now fails closed (sync run aborts, last-known-good membership is retained) when the directory server is unreachable, instead of failing open (sync proceeds with an empty group set)."}}

**Who is affected:** {{The actual subset — e.g. "Installations using LDAP-sourced group membership for role assignment. Installations using local role assignment only are not affected."}} Avoid "all customers" unless it is actually all customers — reviewers stop trusting a "Breaking" marker once it is applied to everyone by default.

**Required action:** {{One concrete step. E.g. "Before upgrading, confirm your LDAP server's certificate and network path are current — a sync that previously failed open and went unnoticed will now block role updates and surface as a support ticket."}}

**Is this backward-compatible with the 12.x line?** {{Yes, with no config change needed / No, requires the action above / A temporary compatibility flag (`{{flag name}}`) restores the previous behaviour through {{version}}}} — state one of these explicitly; "behaviour change" with no compatibility statement is exactly the kind of entry that generated the "please provide detail" replies on the last release.

## 5. Deprecated: {{Feature name}}

- **Deprecated in:** 12.4.0
- **Reason:** {{one line}}
- **Replacement:** {{feature/API/config that replaces it}}
- **Still works through:** the 12.x line
- **Planned removal:** {{earliest major/LTS version, e.g. "13.0"}}
- **Required action:** {{migration step, or "None before 13.0; plan migration ahead of that release"}}
- **Migration guide:** {{link, or "Not yet published — target date: [date]"}} — do not ship a deprecation notice without one or the other stated.

## 6. Lifecycle Change: Release Cadence

Starting with {{this release / the release following 12.4}}, Ridgeway LTS releases move from {{prior cadence, e.g. "three times yearly"}} to **twice yearly** (H1/H2).

**What does not change:** {{This is the sentence your customers will actually need — confirm and state explicitly: "Security fixes continue to ship as out-of-band patch releases on the existing schedule and are not gated behind the twice-yearly LTS cadence."}} If that statement isn't true, say what the real security-patch cadence is instead — a bank's change board will ask this before they ask anything else about this section.

**Support window impact:** {{Does N-1/N-2 support duration change as a result? State the new support end dates for currently-supported branches, or confirm they are unchanged.}}

## 7. Upgrade Guidance

- Direct upgrade path: {{from which versions}}
- Estimated maintenance window: {{if known}}
- Rollback procedure: {{link or "unchanged from prior releases"}}
- Pre-upgrade checklist: {{link}}

## 8. Change Log (Keep a Changelog format)

## [12.4.0] - {{2026-10-DD}}

### Security

- {{One-line summary matching §3, cross-referenced}} ({{advisory ID}})

### Changed

- **Behaviour change:** LDAP directory sync {{summary matching §4}}

### Deprecated

- Deprecate {{feature}} in favour of {{replacement}}. Removed no earlier than {{version}}.

### Known issues

- {{List, or: "None carried forward from 12.3.x at time of publication."}}

## 9. References

- Migration guide: {{link}}
- Support policy: {{link}}
- Previous advisory (12.3.x): {{link}}
```

---

**Traceability**

| Entry | Source |
|---|---|
| Security fix | {{internal ticket/CVE}} — not provided, cannot mark as verified |
| LDAP sync behaviour change | {{internal ticket/PR}} — not provided |
| Deprecation | {{internal ticket/PR}} — not provided |
| Cadence change | Product/engineering decision — not a code change, no ticket expected |

**Excluded:** none evaluated — you gave me four items, not a diff or ticket list, so I have no basis to say anything else was deliberately left out. Before publishing, run the rest of the 12.4 changeset (anything besides these four) through the same test: does a consumer observe it? If yes, it needs an entry too, or this advisory undercounts exactly the way your last one did.

**Needs a human (blocking, before this ships):**
1. CVE ID/advisory number and CVSS score for §3 — cannot publish a bank-facing security section without one.
2. Backport policy: does the fix reach any supported branch besides 12.4.0? Drives the whole "required action" framing in §2 and §3.
3. Exact LDAP before/after behaviour and the affected subset — currently a placeholder shape, not a fact.
4. Deprecated feature's name, replacement, and removal version.
5. Whether the twice-yearly cadence changes the security-patch cadence — this is the sentence most likely to trigger a fourth "please clarify" email if left implicit.
6. Confirm the advisory numbering scheme (`RGW-YYYY-NNN` is a placeholder, not yours).

Next: fill items 1–6, then re-run this document past whoever signed off on the last one's "too short" complaint — the structure now forces the detail they asked for, but the placeholders currently make it look diplomatically vague if published as-is.