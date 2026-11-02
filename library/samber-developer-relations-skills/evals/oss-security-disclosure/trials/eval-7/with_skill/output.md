**Not good to go.** Do not publish Friday at 6pm. Eight things are wrong.

## Blockers

1. **Advisory before tag.** The advisory is public the moment you publish it. A tag two days later leaves a weekend with no upgrade path. Order must be: merge, tag every line, confirm the proxy serves them, then publish the advisory.
2. **Friday 6pm.** If "Friday" means today, 2026-10-23, nothing is tagged yet. The runbook says to avoid Friday evenings, because nobody is around to deploy. Proposal: tag Tue 2026-10-27 at about 10:00 Paris, advisory right after. Confirm this against your hours and the reporter's deadline.
3. **Affected range `< 2.3.4` is incomplete.** There are two modules, so write one range per line:
   - `github.com/pelmont/marrowq/v2`: `>= <introduced>, < 2.3.4`, patched 2.3.4.
   - `github.com/pelmont/marrowq`: `>= <introduced>, < 1.9.12`, patched 1.9.12. This version does not exist yet. A single `< 2.3.4` would also mark 1.9.12 as vulnerable.
   - 0.x: list it as affected and unsupported, with no fix and no separate CVE. Mark any version you did not test as unknown, not safe.
4. **Title carries the trigger.** `http://169.254.169.254/latest/meta-data` names the payload. Use "SSRF via unvalidated broker URL in `Dial` and `DialContext`".
5. **PoC gist in References.** Remove it. The advisory names the class, the affected functions and the versions, not a working attack. If the gist is already public, tell me, because that is the fast track.
6. **"Dependabot will alert everyone" is false on day 0.** Alerts start only after the code-host database reviews the advisory. That can take days to weeks. On release day, announce through release notes and your own channels.
7. **"Workarounds: None" is probably wrong.** Callers can allow-list broker hosts before calling `Dial`. Operators can block egress to link-local and private ranges. Never write "none" by default.
8. **Severity "High" has no vector.** Score it yourself and publish the full vector. Candidates:
   - `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N` = 7.5.
   - `S:C` = 8.6.
   - Decide Scope and write the reasoning down. Check whether a response can come back to the attacker. A queue client may speak a non-HTTP protocol, which would lower C:H.

## Also fix

- **"Tag from my working branch."**
  - If that branch is public, the fix is already disclosed. Tell me.
  - Otherwise use a private fork or mirror, with generic branch and commit names.
  - Run the full tests locally for both lines. Private-fork CI does not run.
- **Reporter.** Send them the fix before release (template below). Ask for credit wording and consent. Ask whether anyone else knows, and whether they already hold a CVE.
- **CVE.** Request it now through the repository advisory. The release does not wait for it.
- **`retract`.**
  - It is optional. The Go vuln database and govulncheck are the primary signal.
  - If you want it, put it in the `go.mod` of the same release, one per module path. A separate retract release is extra work.
  - Keep the comment neutral.
  - Afterwards, fill the symbols `Dial` and `DialContext` in the Go vuln DB import. Otherwise govulncheck flags every dependent.
- **By-design check.** Confirm no doc line says the broker URL is trusted input. If a doc says it is safe for untrusted input, the report is in scope.
- **Second responder.** Add one person with advisory access. You are currently the only one.
- **Downstream notice.** High severity: name the largest dependents. Use the embargo template, 1 to 7 days ahead, patch shared at release.
- **CRA.** Is Pelmont a company or monetised, with EU users? If yes, note the role. If exploitation is known, the 24-hour clock may already run.

## Incident record (private advisory only)

```
Report: <ghsa id>   Received: <date, channel>   Responders: <you, second person>
Verdict: pending until <date>. Reproduce on 1.9.11 and 2.3.3 first.
Severity: CVSS:3.1/<full vector> - precondition: app passes untrusted broker URL to Dial/DialContext - Scope reasoning: <write it>
Affected / patched: v2 >= <?> < 2.3.4 -> 2.3.4 | v1 >= <?> < 1.9.12 -> 1.9.12 | 0.x unknown/EOL
Identifier: GitHub CNA, request <date>, status <>
Timeline: <hours per step: v1 backport, tests x2, reporter review, tags, advisory>
Decision gate: <triage date>. Fits in half the hours before deadline: ship faster. Else: counter-offer.
Disclosure: <Tue 2026-10-27, ~10:00 Paris, if agreed>   Reporter deadline: <?>   Agreed: no
Downstream notice: <named dependents | none>   CRA: <role | n/a, reason>
Open questions: see below
```

## Advisory draft (fill the brackets)

```
Title: SSRF via unvalidated broker URL in Dial and DialContext
Summary: Applications that pass an attacker-influenced broker URL to Dial or
DialContext make the client connect to attacker-chosen internal hosts.
Affected:
  github.com/pelmont/marrowq/v2  >= <?>, < 2.3.4   patched 2.3.4
  github.com/pelmont/marrowq     >= <?>, < 1.9.12  patched 1.9.12
  0.x: affected, end of life, no fix
Affected functions: Dial, DialContext
CWE: CWE-918
Severity: <full vector + label>
Workarounds: Validate the broker URL against an allow-list of hosts before
calling Dial or DialContext. Restrict egress from workloads to link-local
and private address ranges.
Credits: <reporter as chosen> (reporter); <you> (remediation developer)
References: fix commits, releases, CVE record. No proof of concept.
```

## Message to the reporter (fix review)

```
The fix is ready in the private advisory's fork: <link>. Could you confirm by
<date, time zone> that it closes the issue, including on the v1 line?
Planned release: <Tue 2026-10-27, ~10:00 Paris>. Proposed advisory text is in
the draft; comments welcome. Credit will read: <as agreed>.
```

## Release-day checklist

1. Run tests for v1 and v2 locally.
2. Merge the fix and the backport.
3. Tag `v2.3.4` and `v1.9.12`, with `retract` in the same commit if wanted.
4. Run `go list -m github.com/pelmont/marrowq/v2@v2.3.4` and `go list -m github.com/pelmont/marrowq@v1.9.12`.
5. Publish the advisory with ranges, functions and credits.
6. Publish release notes and the announcement, using the publication-notice template.
7. Send the reporter the links.
8. Check the Go vuln DB and OSV imports. Follow up if the database review runs late.

## Questions I need answered

1. Is the fix on a public branch or a gist today?
2. Does the v1 backport exist and pass tests?
3. What is the reporter's deadline, and have they agreed to any date?
4. Is anyone exploiting this?
5. Who is the second responder?
6. Is Pelmont a company or monetised?
7. First vulnerable release per line?

**Next, under 2 minutes:** answer 1 and 3. Everything else hangs on them.