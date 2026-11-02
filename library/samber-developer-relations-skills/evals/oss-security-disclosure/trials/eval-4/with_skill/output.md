# `tollwarden` path-normalization bypass: reply to Oskar and a 11-day fix plan

I did not draft the firm 90-day email or a 90-day plan. The skill rules out both, and your own numbers show you don't need them.

- **The fix fits his window.** Fix 3h, test 1h, 3.x backport 2h and release 1h come to 7h. Add reproduction on both lines, review, advisory and CVE work (about 4h) and you reach about 11h of the 20h you have. That is roughly half, which is the skill's threshold for "ship faster". You can release about 3 days before his date, so there is nothing to negotiate.
- **14 days is inside published practice.**
  - CERT/CC's default is 45 days.
  - Openwall's distros lists cap embargoes at 14 days.
  - Project Zero uses 90 days.
  - "Everyone uses 90" is therefore wrong, and he would be entitled to point that out.
- **The employer threat and the word "irresponsible" are off the table.** The skill's rule is never to threaten the reporter or demand silence. You have no leverage, and each of those lines becomes the public story. A clean report that you answer with a threat is how a 14-day deadline turns into an early drop.

## Assumptions

I assumed three things. Tell me if any are wrong.

- **His deadline:** Fri 2026-11-06, which is 14 days from today (Fri 2026-10-23). If he counts from the report date, every date below moves earlier.
- **Time zone:** Europe/Paris, for you and Mireille.
- **Hours:** 20h is the combined total for both of you.

## 1. Reply to Oskar (send today)

This is the skill's acknowledgement template, filled in. Send it through the GitHub private report thread.

```
Subject: Re: <report title> - received, reproduced, fix scheduled

Hi Oskar,

Thank you for the clear report. We received it on <date received> and have
<reproduced it against tollwarden <latest 4.x> | will confirm reproduction by
Mon 2026-10-26>. Mireille and I are both on it.

We have noted your planned publication date of Fri 2026-11-06. We intend to meet it.

- Triage decision: Tue 2026-10-27.
- Fix for 4.x and backport for 3.x, both supported lines: shared with you in
  the private advisory by Fri 2026-10-30, so you can confirm they close the issue.
  Please reply by Mon 2026-11-02, 18:00 Europe/Paris.
- Planned release of patched 4.x and 3.x versions: Tue 2026-11-03, 10:00
  Europe/Paris. The advisory goes public right after the versions are
  installable from npm. After that, you are free to publish your write-up.

If the plan changes, you will hear from us before 2026-11-06, with a reason and a date.

A few questions so we can coordinate:
- Has anyone else been told about this, or have you or your employer requested
  a CVE? If one exists we will use it. Otherwise we will request one through
  GitHub's CNA once the issue is confirmed.
- How would you like to be credited (name, handle, organisation, or anonymous)?
- Is Europe/Paris fine for the dates above?

Please keep the details private until the advisory is published. We will continue in this
private advisory thread.

Thanks again,
<your name>
```

Fill every `<...>` before sending. Send only the reproduction line that is true today.

## 2. Internal note to Mireille

Send it through the private advisory draft, not chat.

```
Subject: Security report received - details in the private advisory only

A security report reached me on 2026-10-23 through GitHub private reporting.
I have opened a private advisory draft and added you. Please read it there. Do
not discuss it in chat, issues, pull requests, commit messages or branch names,
and do not run the PoC outside a disposable, network-off environment.

Proposed roles: I fix 4.x and write the regression test; you reproduce on 3.x
and 4.x, then backport to 3.x; we review each other's work; I release.
Reply by Mon 2026-10-26 with your available hours until 2026-11-06.
Decision gate: Tue 2026-10-27.
```

## 3. Plan: 11 days to release, 3 days of buffer

| Date | Action | Owner | Hours |
|---|---|---|---|
| Fri 10-23 | Internal note, add Mireille to the draft, send the reply to Oskar | you | 0.5 |
| Mon 10-26 | Reproduce in a disposable environment, with the PoC read first and networking off. Test the latest 4.x and the latest 3.x. Find the first affected release; mark unchecked versions "unknown". | Mireille | 2 |
| Mon 10-26 | Score independently and run the by-design checks | you | 1 |
| **Tue 10-27** | **Decision gate**: accept, then request the CVE through GitHub's CNA the same day | both | 0.5 |
| Wed 10-28 to Thu 10-29 | Fix on 4.x (3h) and regression test (1h) in the private fork. Check adjacent normalization variants. Run the full suite locally, since fork CI does not run. | you | 4 |
| Fri 10-30 | 3.x backport (2h) and 3.x suite | Mireille | 2 |
| Fri 10-30 | Cross-review of both fixes (1h). Share the fix with Oskar (template 6b). Draft the advisory (1h). | both | 2 |
| Mon 11-02 | Reporter confirmation due 18:00. Resolve feedback. | both | 0.5 |
| **Tue 11-03, 10:00** | **Release**, per the order in section 7 | you | 1 |
| Wed 11-04 to Fri 11-06 | Buffer. Oskar publishes whenever he likes after the advisory. | n/a | n/a |

- **Total:** about 13.5h, since the release row adds 1h on top of the earlier 11h estimate. That leaves about 6h of slack out of your 20h.
- **Release day:** Tuesday, not Friday, so downstream users have time to react.
- **Regression test:** it is effectively a minimal PoC. If the severity ends up High, keep it only in the private fork and land it in a follow-up commit after users have had time to upgrade. Reviewers still see it in the fork.
- **Downstream notice:** only if the severity is High or Critical. Send it to named users who run the affected config, through their security contacts, 1 to 7 days ahead. Use template 7. Most npm libraries need nobody.

### Decision gate (Tue 10-27)

- **Less than about 14h left for the remaining steps:** switch to the counter-offer below. Do not wait until day 12.
- **Verdict is "not a vulnerability":** use template 4, citing the doc line. You said it is real, so this is unlikely.

### Provisional severity (confirm after reproduction)

- **Vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`, base 9.1. I have not seen the PoC, so this is a placeholder.
- **Precondition, in prose:** "An application using tollwarden to protect routes receives a crafted request path that bypasses the access check."
- **Scope and Privileges Required:** write your reasoning down before publishing. Scope is Unchanged unless the bypass reaches a different security authority. Privileges Required is None for the reasonable worst-case integration.
- **Rule of thumb:** use the reasonable worst-case integration. Do not lower the score for how an integrator configured things.

## 4. Contingency messages (do not send unless the gate fails)

**Counter-offer** (template 2). Use it only if the gate shows the hours won't hold.

```
Thank you for the deadline of Fri 2026-11-06. We want to meet it, but
<reason, e.g. "the 3.x backport turned out to need a separate fix because
<generic reason>">.

- Confirmed: yes, affecting tollwarden <versions>.
- Work left: <what remains>, estimated at <X> days with 2 maintainers.
- Proposed disclosure: <date, time, Europe/Paris>, patched 4.x and 3.x first.

We can offer: credit in the advisory and CVE record, your review of the fix
before release, and a co-reviewed advisory text. Published defaults run from
45 to 90 days; we are asking for <N>.

If 2026-11-06 must stand, we will publish an advisory that day with the
workaround "<workaround>" and the fix as soon as it is ready. Can you agree to <date>?
```

Offer the workaround fallback only if it fully mitigates the issue and is easy to apply.

**If he publishes early** (template 6):

```
We have seen the public post. We are releasing patched versions <versions>
on <date/time> and publishing the advisory immediately after. We will keep
the credit we agreed. Please avoid adding further technical detail until the
release is out.
```

Then switch to the fast track: same-day fix, release and advisory. Do not argue in public.

## 5. Advisory draft (private; fill the details only there)

| Field | Content |
|---|---|
| Title | Authentication bypass via path normalization in `<affected middleware/API>` |
| Summary | Applications protecting routes with tollwarden may serve protected paths without authentication. |
| Affected / patched | `>= 4.0.0, < <fixed 4.x>` and `>= 3.0.0, < <fixed 3.x>`. Use exact released versions; unchecked ranges are "unknown". |
| Affected functions | `<exported middleware/function names>` |
| Description | Preconditions, impact, what the fix changes in general terms. No payloads or reproduction steps. |
| Workarounds | `<real workaround | "none - upgrade">` |
| Severity | Full 3.1 vector, plus a 4.0 vector if the host accepts one |
| CWE | `<most specific fit, e.g. path-equivalence class>` |
| Credits | Oskar M. as reporter, in the form he chooses. You and Mireille as remediation developer and reviewer. |
| References | Fix commits, releases, CVE record. No PoC. |

Keep branch names, commit messages and PR titles generic in the private fork (for example "harden request handling").

## 6. Confidentiality reminders

- No vulnerability detail in public issues, PRs, commits, branch names, CI logs, docs or release notes before the advisory is published. A one-line fix is the easiest diff to reverse-engineer.
- Do not run the PoC outside a disposable VM or container with networking off and no credentials mounted. If you can't, reproduce by reading the code and say so.
- Keep incident notes in the private advisory only. I have stored nothing about this incident in memory.

## 7. Release-day checklist (Tue 2026-11-03)

1. Re-run the tests for both lines locally.
2. Merge the 4.x fix, and the 3.x backport into its branch.
3. Tag and publish both patched versions.
4. Confirm each installs: `npm view tollwarden@<4.x fixed>` and `npm view tollwarden@<3.x fixed>`. Consider `npm deprecate` on the vulnerable ranges with a message pointing to the fix.
5. Publish the advisory with fixed versions per line, affected functions and credits.
6. Publish release notes and an announcement on your own channels linking the advisory. GitHub's advisory review can take days to weeks, so scanner alerts will lag.
7. Tell Oskar with links.

## 8. Close-out

- Follow up with GitHub if the advisory review or CVE publication runs late.
- Check that OSV and the ecosystem database imported the right ranges for both lines.
- Thank Oskar with the advisory link.
- Hold a 15-minute retrospective.
- Add any new out-of-scope class to SECURITY.md.
- If you learn of exploitation, tell commercial integrators directly. Check `references/eu-cra.md` if tollwarden is monetised or company-run and distributed in the EU.

## Open questions

- **Dates:** the real report-received date, and whether Oskar's 14 days count from it.
- **Time zones:** Mireille's, and Oskar's if different.
- **Hours:** the split of the 20h between you and Mireille.
- **3.x exposure:** whether 3.x is affected at all and what the first affected release is. Mark it "unknown" until Mireille checks.
- **Severity:** the final score, once the PoC has been reproduced.
- **Exploitation:** any sign of it in the wild. If yes, switch to the fast track.
- **Downstream users:** whether any known users run the affected configuration.
- **Monetisation:** whether `tollwarden` is monetised or company-run and has EU users. If so, run the EU CRA role check.
- **Oskar's side:** whether he or his employer already holds a CVE.