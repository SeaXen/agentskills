**Verdict: keep the credential, change all three renewal ideas.** Each one breaks a rule in the skill (`developer-certification-program`) or contradicts your own facts. Draft section 6 and part of section 7 of the charter follow, then the open questions.

## Fixes to your plan

1. **Re-certify every release → no.** Biweekly releases mean 26 re-certifications a year per holder. Bind the credential to the major version instead: one 30-minute delta task per year. The credential still proves currency, because the exam is re-aligned on every release (internal work, not holder work).
2. **Void v3 holders when v4 lands → no.** v3 stays supported for 24 months, so v3 operators still run supported systems after v4 ships. Your two contracts name certified operators, so voiding breaks your customers' compliance through no fault of theirs. Retirement stops new issuance and never revokes what holders earned. Revocation is for proven misconduct only.
3. **Copy cloud vendors: 2-3 years, ~$300 full-price retake → no.** Vendors made different choices, so there is no standard to copy (list below). Compute your fee from your own costs.

Your goal, "nobody is certified on an old version", is met differently. The verification page shows the version and a supported-through date, and the buyer sets the minimum version in their contract.

## Section 6: Renewal, version binding, retake, retirement

**Tier.** Role certification. Gate ceiling holds: two buyer contracts name certified operators, two years of funding exist, and an owner exists. Still missing: a named successor.

**Version binding**
- The credential carries the major version passed, e.g. "Keldrick Certified Operator v3".
- The credential changes only when the blueprint changes, which is once per major (every 12 months).
- Validity: until v3 end of support, which is 24 months after v3 general availability.
- At most 2 majors are supported at once, so you run at most 2 live exam versions plus 1 delta task.

**Renewal (delta task)**
- Opens at v4 general availability, free to hold-and-upgrade while v3 is supported.
- It is a hands-on, auto-graded task covering only what changed from v3 to v4.
- Same sampled live explanation as the initial award (self-set: 1 pass in 10, 15 minutes). Names are in the contracts, so proxy sitting is the named threat. Renewal must not become the proxy route.
- A pass issues "v4", valid until v4 end of support. The v3 credential stays listed until its own end of support.
- Grace: holders may still sit the delta for 6 months after v3 end of support (self-set). After that, the full exam is required.
- Delta covers all changes since the version the holder holds, so a holder who skips v4 can still reach v5 inside the grace window.

**Re-alignment per release (biweekly)**
- Checkers run in CI on every release. Reference solutions must pass.
- A failing checker pulls that task variant from live forms until fixed.
- Window (self-set): fix before the next release, so within 2 weeks. Two consecutive misses trigger the kill rule review.
- Manual blueprint review: once per quarter (self-set). A change inside a major is a patch to the tasks, not a new credential version.

**Retake**
- Wait 14 days after a fail (self-set; AWS also uses 14 days, read 2026-10-21).
- Cap: 3 attempts per rolling 12 months (self-set).
- Fee: paid per attempt, so failed attempts cover their own sitting cost. No free retake bundled in.
- Failed candidates get a per-domain score report to target the retake.
- Delta task: a 24-hour wait between attempts after the second try (Microsoft renewal rule, read 2026-10-21; self-set for you).

**Exam-version retirement (v3 exam)**
- Announce 6 months ahead (self-set). Stop selling the v3 exam 6 months after the v4 exam launches (self-set).
- Existing v3 holders stay valid until v3 end of support. Show "valid" with the date, then "expired" with the date.
- Never show "not valid" for a version change. That status is for revocation only, with no reason shown.

**Program retirement**
- Honour every unexpired credential.
- Keep verification live for 3 years after the last issue (self-set).
- Honour or refund sold vouchers.
- Notify every buyer with named holders at least 12 months ahead (self-set), because their contracts depend on it.

**Revocation**
- Only for proven misconduct, under the candidate agreement, with an appeal to a named decision-maker.
- A new major version is never a ground.

## Section 7 (part): Price, aimed at your plan

- Do not set $300 from other vendors. Sourced facts, quoted as their choices and not as a norm:
  - CKA: $445 exam, 2 years, retake at full price, one free retake included (read 2026-10-21).
  - HashiCorp: 2 years, full price renewal, $70.50 Associate and $295 Professional per attempt (read 2026-08-28, oldest read, unverified).
  - AWS: 3 years by retake, or 1 year by maintenance activities; 50% discount voucher for holders (validity figures unverified, no read date).
  - Microsoft role-based: 1 year, free renewal assessment (read 2026-10-21).
- Your consumer is buyer contracts, so the skill's pricing rule is a full fee, bundled into enterprise training or support contracts.
- Compute the fee as:

  ```
  fee per attempt = (yearly fixed + yearly operating) / expected attempts per year
                    + cost per attempt
                    - amount a contract absorbs
  ```

  - Yearly fixed = build cost / credential version life in years. Use 2 years for a major.
  - Yearly operating includes the biweekly re-alignment hours.
  - Cost per attempt covers hosting, proctoring and no-shows.
- Price the delta task near its per-sitting cost, or bundle it into the enterprise contract. Every number is self-set until you supply the inputs.
- Tell each buyer the tier is a role certification. Reword any "certified" wording in partner agreements if you ever ship a lower tier.

## Open questions

Decide these before I finalize the section:

1. Do the two contracts name a version, or just "certified"?
2. Does a v4 holder qualify for an account still running v3?
3. Who is the named successor to the owner?
4. How many sittings per year do you expect? Fee and hosting cost depend on it.

**Next (2 minutes):** paste the exact certified-operator clause from one contract. It decides questions 1 and 2.