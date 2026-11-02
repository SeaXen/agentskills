Don't publish the advisory first, and don't email 400 dependents. Four things in the plan break the process. The reordered checklist and the downstream email follow.

## What changes

1. **Advisory first is backwards.** Publishing the advisory deletes the fork, so you'd lose the fix before merging it. The advisory is public the moment it goes out. Nothing patched would be on npm yet, which is the worst window you can create. Order: merge, publish, confirm the registry serves both versions, then publish the advisory.
2. **Green checks are not proof.** CI and integrations cannot run in a temporary private fork. Run the full test suite locally on 6.x and on 5.x before merging. Find out what produced the green you saw.
3. **Three fork PRs will not merge as planned.** The fork merges all open PRs at once, and only one may target the default branch. Your main PR and docs PR probably both target `main`. This assumes the docs PR targets `main`. Fold docs into the main PR, or hold the backport and docs in a private mirror. Branch protection is not enforced on that merge, so review deliberately.
4. **400 emails is a leak, not a notice.** One mail to 400 inboxes will not stay embargoed. Notify only named contacts who must rebuild or who run the affected configuration. Use their published security contact. Send the patch at release time, not 5 days ahead. The other ~390 dependents learn at publication, through the advisory and your announcement.
5. **linux-distros: skip it.** That list is for software distributions package. An npm library has no packagers, so it gets no post unless a distro actually ships `pelmont-sso`. Ask first. If one does, the subject needs `[vs]`, the embargo is 14 days maximum and under 7 preferred, and a fix already in a public repo counts as public.

Two more:

- **Exploit test.** For Critical, the minimal triggering test normally lands in a follow-up commit after users had time to upgrade. Reviewers see it in the private fork either way. Keep it out of the merge PR, and check the npm `files` list so it does not ship in the tarball. The fix PR is only the exception if the fix cannot be reviewed without it. Land a non-triggering test with the fix.
- **Date.** Today is Fri 2026-10-23. If Tuesday is 2026-10-27, "5 days ahead" was yesterday. The runbook allows 1 to 7 days, so notice on Fri or Mon is fine.

## Downstream email

Send one email per recipient, never a mailing list or bulk BCC. Do not attach the patch. This is for named contacts only. The email names a class and an API, never the trigger.

```
Subject: [EMBARGOED until Tue 2026-10-27 <time> <TZ>] Security fix in pelmont-sso

This notice is confidential until Tuesday 2026-10-27, <time> <TZ>. Please do not
make it public, share it beyond the people who must prepare the update, or push
related changes to public repositories before then.

Affected: pelmont-sso, versions >= <first affected 6.x>, < <fixed 6.x> and
>= <first affected 5.x>, < <fixed 5.x>. Versions older than <x> are
unsupported and not checked.
Fixed in: <fixed 6.x> and <fixed 5.x>, to be published on npm at
Tuesday 2026-10-27, <time> <TZ>.
Severity: <CVSS 3.1 full vector>, <label>.
Summary: authentication bypass in <affected API or feature>. <One line: who is
affected, what an attacker gains.>
Interim mitigation until you upgrade: <configuration or usage change | none>.
Patch: not attached. It is published with the release. <If you must build
before release, reply and we will discuss private access.>
Identifier: <CVE id | requested, pending>.

We will tell you immediately if the date changes. Please send security replies
to <private contact>, not to a public issue.
```

Fill every `<...>` before sending. Do not send one still marked.

## Release checklist

Today is Friday 2026-10-23, and Tuesday is 2026-10-27.

**Now to Monday**
1. Confirm the Tuesday release time and time zone. Avoid a time when Yuki or the downstream contacts are away.
2. Name a second person who can publish advisories.
3. Request the CVE now through the repo advisory. Do not wait for it. The release uses the advisory's own ID, and you add the CVE later.
4. Run the full tests locally on `main` and on `release-5.x`. Fix the PR structure from point 3 above.
5. Pull the exploit test out of the merge PR. Keep it on a private branch for the follow-up commit.
6. Send the fix to Yuki to confirm, on both lines. Confirm the credit wording.
7. Fill the advisory draft:
   - Title and summary, class plus API only.
   - Two ranges, one per line: `>= first 6.x, < fixed 6.x` and `>= first 5.x, < fixed 5.x`. Mark unchecked versions as unknown. Name older lines as affected and unsupported.
   - Affected functions.
   - Workaround, or "none - upgrade".
   - Full CVSS 3.1 vector. Write the Scope and Privileges Required reasoning. Score it independently, not from "Critical".
   - CWE and credits.
8. Send the embargo email to the named list on Friday or Monday.

**Tuesday**
1. Re-run tests on both lines locally.
2. Merge the fix into `main`, and the backport into `release-5.x`.
3. Tag and publish both versions. Publish the 5.x patch with `npm publish --tag <your 5.x tag>`. Plain `npm publish` would move `latest` to the older line.
4. Confirm `npm view pelmont-sso@<6.x>` and `npm view pelmont-sso@<5.x>` both return, and smoke-install each. Check that the tarball has no exploit test.
5. Publish the advisory, which deletes the fork. Then publish the release notes and announcement linking it.

**After Tuesday**
1. Run `npm deprecate` on the vulnerable ranges, with a message pointing to the fixed versions.
2. Send Yuki the advisory and release links.
3. Post to oss-security only if a distribution list was used.
4. Scanners alert only after the advisory database reviews it, which can take days to weeks. Chase the review and CVE publication if they run late, and check that the ecosystem databases import the correct ranges.
5. Land the exploit test in a follow-up commit once users have had time to upgrade. Set that date now, and hold a 15-minute retrospective.

## Open questions

- First affected version on each line?
- What produced the green checks?
- Is `pelmont-sso` monetised or company-run, for the EU CRA role test? Any sign of exploitation in the wild? If exploited, release the same day.
- Does any Linux distro package it?
- How do you pick the named downstream list? Start from dependents that run the affected configuration.

Next: run `npm test` on `release-5.x` locally and paste the result.