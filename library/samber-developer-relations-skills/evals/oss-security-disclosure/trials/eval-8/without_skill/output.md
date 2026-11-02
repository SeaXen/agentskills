# saltwick CVE dispute and thread

Two corrections to the plan come first, because they change what to send.

## Corrections

1. **Becoming a CNA won't work.**
   - A CNA can only reject or edit IDs it assigned, and only within its own scope.
   - It has no power over a CVE that GitHub's CNA or MITRE assigned.
   - Onboarding takes weeks to months. A CNA whose first act is killing a CVE against its own product is a conflict of interest the program would likely refuse. Drop this path.
2. **MITRE only rejects if MITRE is the assigning CNA.**
   - Find the CNA on the CVE record: "Assigner" on cve.org.
   - Dispute to that CNA first. Escalate to MITRE (CNA-LR) or the CNA's root only if that fails.
   - Without that step MITRE will bounce you back.
3. **Post the thread after you file the dispute, not before.**
   - A public pile-on before the CNA has your dispute reads as pressure and hurts you.
   - The weak point in our record is that the reporter's escalation followed a private "working as documented" reply, with nothing public.
   - The thread should stay on the facts. Don't name or blame the reporter. Don't quote Kofi's email.

Realistic outcomes, best to worst: **REJECTED**, then **DISPUTED** tag, then rescored to something low. A DISPUTED tag alone doesn't stop govulncheck. So also ask the Go vulndb for withdrawal, and consider the code change below.

## Do this first: remove the dependents' pain

- Rename or gate the option so it can't ship to production by accident. For example:
  - `InsecureSkipVerifyForTests`, or
  - panic unless `testing.Testing()` is true.
- That also answers "improper certificate validation" on the merits. Say so in the dispute.

## Facts to confirm before sending

- CVE ID, assigning CNA, and the exact description text.
- Whether the option can be set from untrusted input (env var, config file, request). If yes, the dispute argument below is weaker and you should say so.
- Which versions the CVE marks affected.
- Whether `SECURITY.md` exists and states test-only options are out of scope.
- Whether the reporter ever contacted the CNA before assignment.

## 1. Dispute to the assigning CNA

**To:** the assigning CNA's contact (cve.org record, "Assigner")
**Subject:** Dispute and rejection request: CVE-XXXX-XXXXX (saltwick)

> I am a maintainer of saltwick (github.com/\<org>/saltwick). I dispute CVE-XXXX-XXXXX and ask that it be REJECTED. If you do not reject it, I ask that you add a DISPUTED tag and rescore it.
>
> **Claim in the record:** improper certificate validation (CWE-295), CVSS 9.8, via the `InsecureSkipVerify` passthrough option.
>
> **Why this is not a vulnerability:**
> 1. The option does what it says. It is a documented passthrough of Go's `tls.Config.InsecureSkipVerify`. Our documentation states: "disables verification, for tests only."
> 2. It is off by default. A caller must explicitly set it. The library never disables verification on its own.
> 3. A caller who sets it makes a choice in their own code. Nothing in saltwick lets a remote party turn it on. \[Confirm this before sending.]
> 4. The same passthrough exists in the Go standard library. If this counts as a vulnerability in saltwick, it counts in `crypto/tls`.
> 5. The 9.8 score assumes network-reachable, no privileges, no user interaction, full impact. It describes an attack the library does not expose. The score does not fit the behavior.
>
> **Process:** the reporter contacted us about 8 months ago. We replied that the behavior was as documented and closed the thread. We did not publish a statement. That was our gap, and we have now added \[SECURITY.md / README note] stating the position. I did not see a request to us to review the CVE before assignment. \[Edit if wrong.]
>
> **Impact:** dependents' govulncheck runs now flag them, and they have opened issues. This is false-positive noise for them.
>
> **What I changed:** in \[version], the option is renamed to `\[new name]` / gated to test builds \[delete if not done]. This does not concede a vulnerability. It removes the misuse risk.
>
> **Request:**
> - REJECT the CVE; or
> - add `** DISPUTED **` and correct the vector/score.
>
> Please tell me what evidence you need and the expected timeline. I can provide the docs, the code path, and the commit history.
>
> \[Name, role, project URL, contact]

## 2. Escalation to MITRE (use only if the CNA is not MITRE and does not act, or if it is MITRE)

> Escalation of CVE-XXXX-XXXXX. I filed a dispute with the assigning CNA on \[date] (copy attached) and received \[no reply / a refusal without reasoning]. The record describes documented, opt-in, test-only behavior as a 9.8 certificate-validation flaw. I request review under the CVE dispute process and rejection, or a DISPUTED tag at minimum. Attachments: dispute email, documentation excerpt, code path, change log.

Attach everything. Keep it to facts.

## 3. Downstream databases (send at the same time)

**GitHub Advisory Database:** use "Suggest improvements for this vulnerability" on the advisory page, or contact the advisory curators.

> Request withdrawal of GHSA-xxxx-xxxx-xxxx (CVE-XXXX-XXXXX). We have disputed the CVE with its assigning CNA. The behavior is documented, opt-in, test-only. Details: \[link].

**Go vulnerability database:** open an issue at golang/vulndb.

> Request withdrawal of GO-YYYY-NNNN (CVE-XXXX-XXXXX, saltwick). The report describes the documented `InsecureSkipVerify` passthrough. It is off by default and never set by the library. govulncheck flags dependents who call the option. We have disputed the CVE with its CNA \[link]. Please consider withdrawing or marking the entry until the dispute resolves.

## 4. The thread (post after sections 1 to 3 are filed)

> **1/** A CVE (CVE-XXXX-XXXXX, CVSS 9.8) was assigned against saltwick, our Go TLS helper. We dispute it and have filed that dispute. Here is the situation and what we're doing.
>
> **2/** The report is about our `InsecureSkipVerify` option. It passes Go's own `tls.Config.InsecureSkipVerify` through. It is off by default. The docs say: "disables verification, for tests only."
>
> **3/** We think the 9.8 doesn't fit. A caller has to opt in, in their own code. The library never turns it on, and no remote party can. The standard library exposes the same switch.
>
> **4/** We got this wrong in one place. The reporter wrote to us months ago. We replied privately and closed it, and published nothing. A public note then would have saved everyone this. We're sorry for the noise it caused.
>
> **5/** What we've done: filed disputes with the assigning CNA, GitHub's advisory database, and the Go vulndb. We're also \[renaming/gating] the option in vX.Y.Z so it can't reach production by accident. SECURITY.md now states our scope.
>
> **6/** If saltwick is flagged in your govulncheck run: it fires because your code calls the option. Check that the call is only in tests. If it's in production code, you do have a real problem, and we'll help you fix it.
>
> **7/** We'll post the outcome here, whatever it is. Questions: \[issue link]. Security reports: \[SECURITY.md contact].

Post 4 keeps the thread from reading as defensive. Keep it unless you disagree with the facts.

## 5. Reply to the three dependents' issues

> Thanks for flagging. govulncheck reports this because your code calls saltwick's `InsecureSkipVerify` option. We dispute the CVE (link) and have asked for withdrawal. Meanwhile:
> - If the call is test-only, it is not exploitable in your deployment. You can suppress it in your tooling with a note linking our dispute.
> - If the call is in production code, remove it. That is a real misconfiguration regardless of the CVE.
> - vX.Y.Z \[renames/gates] the option. We'll update this issue when the CVE status changes.

## Next steps, in order

1. Confirm the facts list above.
2. Ship the rename or gate (about an hour).
3. Send sections 1 and 3.
4. Post section 4 and reply with section 5.
5. Send section 2 only if the CNA has not answered. A reasonable wait is 2 weeks.

I can also draft the `SECURITY.md` scope paragraph and the changelog entry for the rename.