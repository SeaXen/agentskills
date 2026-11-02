Do not post the "he broke the agreement" reply. Do not pull his credit. Both make you the story, and neither shortens the window before users can upgrade. The skill's rule for a reporter who publishes early is fast track: ship the fix and advisory the same day, and don't argue in public.

⚠️ Today is Friday 2026-10-23. The payload is public now, so Monday is too late.

**Next action, 5 minutes:** open the private advisory draft, add your second responder, and check the thread for what exactly was agreed for Nov 5. If it is not in writing, say so in the incident record.

**On pulling the credit:** the credit is part of what he was promised. Removing it reads as retaliation and gives him and the forum a second story. Ask him how he wants to be credited, and keep the credit. Raise "too slow" and the broken date in the post-release retrospective, privately.

**On SECURITY.md:** the skill defers Setup until the advisory is out. A SECURITY.md committed today also reads as a rebuttal in a trending thread. A draft is at the bottom. Commit it after the advisory, once you've filled the 4 blanks.

## 1. Incident record (keep in the private advisory draft only)

```
Report: <advisory id>   Received: <date, channel>   Responders: <you>, <second responder>
Verdict: pending until 2026-10-23 <time> - reproduce by reading code and tests first
Severity: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (provisional, 9.8)
  precondition: an application passes untrusted input to `order_by`
  Scope/PR reasoning: S:U because impact stays in the database the app already uses;
  PR:N because the worst-case integration lets any submitter of the sort parameter reach it.
  Lower C/I after reproduction if only read-side or blind extraction is possible.
Affected / patched: <line A: introduced ?, fixed ?> <line B ...>  unchecked = unknown, never "safe"
Identifier: request the CVE through the code-host CNA today. If Bram already holds one, use it.
Timeline: 2026-10-23 <time> - fix hours estimate - <owner>
  then regression test, backports, local full test run, release, advisory
Decision gate: 2026-10-23 12:00 <TZ>
  estimate <= half the available hours: release today
  otherwise: workaround notice today (below), release by Mon 2026-10-26
Disclosure: already public (Bram's post, 2026-10-23)   Reporter deadline: 2026-11-05 agreed: <yes/no, in writing?>
Downstream notice: known large users only, hours of notice, no embargo (already public)
CRA: ask the 4th interview question below; run the role test today if exploitation is known
Open questions: see "What I need from you"
```

## 2. Internal note to co-responders

Send through the private advisory draft or direct email, not team chat.

```
Subject: Security report received - details in the private advisory only

A security report reached me on 2026-10-<xx> through <channel>. I have opened a private
advisory draft and added you. Please read it there, do not discuss it in chat,
issues, pull requests, commit messages or branch names, and do not run any
attachment outside a disposable, network-off environment.
The reporter published a write-up today, so we are on the fast track: fix, release
and advisory today if the estimate fits.
Proposed roles: <who finishes the fix>, <who reviews and backports>, <who releases>.
Reply by 2026-10-23 <time> with your available hours until Monday 2026-10-26.
```

## 3. Reply to Bram (private channel only)

This is template 6 plus the fix review request.

```
Thank you for the report. We have seen your public post. We are releasing patched
versions <versions> on 2026-10-23 at <time, TZ> and publishing the advisory
immediately after. We will keep the credit we agreed.

Please avoid adding further technical detail until the release is out. Once it is
live, we would appreciate a link to the advisory in your post so readers find the
fixed versions.

Could you confirm by <time, TZ> that the fix in the private advisory fork closes
the issue, including on <other supported line>? <link>
How would you like to be credited (name, handle, organisation)?
Do you or your employer already hold a CVE for this? If so, tell us now so we
request no duplicate.

You will hear from us again at <time, TZ>, or sooner when the release is out.
```

Do not add a complaint about the date. Do not threaten. Do not ask him to retract the post.

## 4. Public reply in the forum thread

Post it only after you fill the date and time, or hold it until release and post the shorter release-day version. Do not name Bram. Do not confirm or deny his payload.

```
We have seen the write-up about `order_by` in vashti-orm. Patched releases are
coming on <date, time, TZ>, with a security advisory right after. Until then:
if your application passes user input to `order_by`, restrict it to a fixed
allow-list of column names. We will post the advisory link here.
```

Release-day version, from template 8:

```
vashti-orm <versions> fix SQL injection in `order_by` handling
(<CVE id or advisory id>, <advisory link>). Users of <affected versions> should upgrade.
Workaround if you cannot upgrade: restrict `order_by` input to an allow-list of columns.
Thanks to <credit as agreed> for reporting it.
```

Say nothing about timelines, "too slow" or the agreement. Anything defensive in that thread is the headline.

## 5. Contingency: the fix does not fit today

If the 12:00 gate says the estimate exceeds about half your available hours, publish a workaround notice today and release Monday.

- Name the class (SQL injection), the API (`order_by`) and the allow-list workaround.
- Add no trigger, payload or fix detail.
- Use it only if the allow-list fully mitigates and is easy to apply. If not, release today anyway.

The "advisory now, tag in an hour" shortcut is the one the skill forbids. An advisory with a fixed-version table and no release gives users no upgrade path.

## 6. Downstream notice

Send it only to known large users or packagers, using their published security contact. The issue is already public, so no embargo header.

```
Subject: Security fix in vashti-orm, release <date, time, TZ>

Affected: vashti-orm, versions <ranges>.
Fixed in: <versions>, published <date, time, TZ>.
Severity: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (provisional).
Summary: SQL injection in `order_by` handling. A write-up is already public.
Interim mitigation: restrict `order_by` input to an allow-list of columns.
Patch: shared at release time.
Identifier: <CVE / advisory id, if assigned>.
```

## 7. Advisory draft

| Field | Content |
|---|---|
| Title | SQL injection in `order_by` handling of vashti-orm queries |
| Summary | Applications passing untrusted input to `order_by` let an attacker alter the generated SQL. |
| Affected / patched | One row per supported line: `>= X, < X.y.z` and `>= A, < A.b.c`. Unchecked lines marked unknown. |
| Affected functions | `<exported functions that reach the flaw>` |
| Description | Precondition: untrusted input reaches `order_by`. Impact: attacker-controlled SQL. The fix validates and quotes ordering input. No payload. |
| Workarounds | Restrict `order_by` input to an allow-list of column names. |
| Severity | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, adjusted after reproduction |
| CWE | CWE-89 |
| Credits | Reporter: Bram, in the form he chooses. Fix author and reviewers as remediation developer and reviewer. |
| References | Fix commit, release. No proof of concept. |

Do not link his write-up from the advisory.

## 8. Release-day checklist

1. Finish the fix in the private fork or a private mirror. The CI does not run there, so run the full tests locally.
2. Add the regression test. For High or Critical, land the triggering test in a follow-up commit after users had time to upgrade.
3. Check adjacent variants of the same flaw class, such as other ORDER BY or GROUP BY inputs.
4. Backport to every supported line, with each line's own tests.
5. Send the fix to Bram for confirmation.
6. Merge, then tag and publish every supported line. Use generic commit and PR titles, nothing that names the bug.
7. Confirm each version installs from PyPI: `pip install vashti-orm==<version>`.
8. Publish the advisory with fixed versions, affected functions and credits.
9. Post release notes, the project announcement, and the forum reply from section 4.
10. Tell Bram, with links.
11. Within 3 days, follow up if the code-host database review has not run.

## 9. SECURITY.md draft (commit after the advisory is out)

Fill the 4 blanks marked `<...>`. This is written for a volunteer project with private reporting enabled, so check each promise against your real hours.

```markdown
# Security Policy

## Supported versions

| Version | Security fixes |
|---|---|
| <latest major.minor> | Yes |
| <previous major> | Until <date or "6 months after the next major"> |
| Older | No - upgrade |

## Reporting a vulnerability

Report privately through the repository's "Report a vulnerability" button
(Security tab). Do not open public issues, pull requests or discussions for
security problems.

Please include: affected version, a minimal reproducible proof of concept
against a released version, the impact you observed, and any suggested fix.
If you used AI tools, say so and confirm you verified the result yourself.
Reports without a reproducible proof of concept may be closed.

## What to expect (<volunteer-maintained | maintained by <company>>)

- Acknowledgement: within 5 business days, with a dated plan.
- Triage decision (accepted, not a vulnerability, or more information needed):
  within 14 calendar days.
- Coordinated disclosure: we aim to publish a fix and advisory within 90
  calendar days of the report, and we agree the date with you in writing.
  If the date cannot hold, we propose a new date before it expires.
- We may pause intake during <holidays / announced periods>; pauses are announced here.

## Scope

In scope: the public API of vashti-orm, used as documented.
Out of scope: inputs the documentation declares trusted or invalid; examples,
tests and internal tooling; vulnerabilities in dependencies our code does not
reach; unsupported versions; reports from automated tools without a verified
proof of concept.

## Advisories and identifiers

We publish security advisories on the repository's advisory page, request CVE
IDs through the code host's CNA, and score severity with CVSS 3.1 base metrics.

## Credit

We credit reporters in the advisory unless you ask otherwise. This project does
not run a bug bounty and does not pay for reports.
```

I left Safe harbor out. Individual maintainers can waive only their own claims, so add it only after every named maintainer agrees, and after legal sign-off if a company is behind the project.

The lesson from this incident goes into the retrospective, not the file. The 2-day acknowledgement had no dated release plan, so "80% done" looked like silence. The new 5-day acknowledgement must carry a date.

## What I need from you

1. Which release lines are supported, and how do they live (branches or separate module paths)?
2. Who besides you can publish a fix and the advisory, and how many hours does each have today?
3. Is `vashti-orm` monetised or company-run, and is there any sign of exploitation?
4. Does your agreement with Bram exist in writing, and does it say anything about credit?

Send me answers 1 and 2 and I will fill the timeline, the version ranges and the 12:00 gate decision.