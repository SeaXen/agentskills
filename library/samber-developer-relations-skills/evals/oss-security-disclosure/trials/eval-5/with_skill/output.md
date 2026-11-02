# hexmill PNG chunk-reader heap overflow: what to send

**Do not pay $200 and do not call CERT/CC.** Send the reporter a dated counter-offer today. The messages are below.

## Why not the two options you proposed

- **$200 for an extension:** the skill says never pay for an extension. You have no leverage, and the payment becomes the public story. It also reads as a bounty, which you don't run. Offer credit, an early look at the fix, and a co-reviewed advisory instead.
- **CERT/CC:** the skill reserves a coordinator for cases where several vendors must ship together. CERT/CC doesn't write your fix, and its default clock is 45 days from the first report, regardless of patch status. Your real coordination need is the two distributions that package 3.x. Handle that through the distros list or their security contacts, with a short embargo (details in the downstream notice below).

## Severity: don't treat it as a DoS

In C++, a heap overflow is memory corruption until proven otherwise. "It just crashes" only says the PoC doesn't show more. The skill says to score from the worst-case integration, an app that decodes untrusted PNGs.

- **Provisional vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H` (9.8).
- **If it is an out-of-bounds read only:** `C:H/I:N/A:H` (9.1).
- **Open step:** check from the code, or from an ASAN trace, whether it is a read or a write.
- **Reporter's PoC:** per confidentiality rule 3, run it only in a throwaway VM or container with networking off. You said you already reproduced it, so confirm it ran that way. If not, don't rerun it outside one.

## Timeline

| Item | Hours (your estimates unless noted) |
|---|---|
| 5.x fix (chunk-length rewrite) | 12 |
| 4.x backport | 6 |
| 3.x backport (different allocator) | 6 |
| Regression tests, fuzzing, review, release (my estimate) | about 8–10 |
| **Total** | **about 32–34** |
| You have before their deadline | 10 |

- **Ship faster fails.** That path needs the work to fit in about half your available hours, which is 5. It needs about 33.
- **Counter-offer is the default.** That means a specific release date, the reason, and what the reporter gets.
- **Proposed date: Tue 2026-11-24, 14:00 UTC.**
  - It assumes about 10 hours a week. Adjust it to your real hours.
  - It is about 32 days from today, so roughly 5 weeks after the report. That sits inside published norms: CERT/CC 45 days, OpenSSF 45–90 days.
- **Release every line in the same window.** A staged release (5.x first) discloses the bug on 4.x and 3.x early.

| Window | Work | Hours |
|---|---|---|
| Fri 10-23 to Fri 10-30 | Acknowledge and send counter-offer; open private advisory; request CVE; **time-boxed spike for a minimal bounds-check patch**; start the 5.x rewrite | 10 |
| 10-31 to 11-06 | Finish 5.x and its regression test; start 4.x. Send the 5.x fix to the reporter for review | 10 |
| 11-07 to 11-13 | Finish 4.x; do 3.x; start fuzzing | 10 |
| 11-14 to 11-20 | Fuzz all lines; bindings; release rehearsal. About 11-17: notify distros, only if all fixes exist | about 8 |
| 11-21 to 11-23 | Buffer | none |
| Tue 11-24 | Merge, tag and publish all lines; confirm the registries serve them; then publish the advisory | none |

**Decision gate: Fri 2026-10-30.**
- If the minimal-patch spike produced a patch that closes all three lines in about 5 hours total, switch to ship-faster. Release inside their 7 days and do the rewrite later as hardening.
- Otherwise, if the 5.x rewrite is behind plan, tell the reporter that day, not on 11-24.

## Things to check that I couldn't

1. **Python and Node bindings.** If their wheels or npm packages bundle the native library, each is its own affected package. Each needs a release and its own advisory row, which is more hours.
2. **A second pair of hands.** Rule 6 says to have at least two responders. A trusted reviewer added to the private advisory helps with fuzzing and review. Ask for their consent first.
3. **Exploitation or commercial use.** Is there any sign of exploitation? Is hexmill monetised or company-run? If it is monetised, or shipped inside EU products, run the CRA role test in `eu-cra.md`. If exploitation is known, the 24-hour manufacturer clock may already apply to your commercial integrators.
4. **First affected version.** Mark versions you haven't checked as "unknown", never "safe".
5. **A complete workaround.** Without one, drop the fallback paragraph from message 1.

## Confidentiality (until the advisory is out)

- No public issues, PRs, commits, branch names or CI logs may mention this. Use generic names like `fix/input-validation`.
- Run the full test suite locally. CI doesn't run in the private fork.
- Keep details only in the private advisory. Don't put them in any memory, notes or repo file.

## Messages

### 1. To the reporter (acknowledgement plus counter-offer)

```
Subject: Re: <advisory title> - confirmed, dated plan

Thank you for the report. We received it on <date> and reproduced it against the
latest release of each supported line (5.x, 4.x, 3.x LTS).

We are treating this as potential memory corruption, not only a crash, and will
score and describe it that way.

You proposed publication on <date>. We cannot meet it. The fix is a rewrite of
the chunk-length handling, each supported line needs its own backport (3.x uses
a different allocator), and a downstream package of 3.x has to be rebuilt. We
estimate about 33 hours of work, and I am the only maintainer, with about 10
hours available before your date.

Proposal:
- Patched releases of all three lines on Tuesday 2026-11-24 at 14:00 UTC, with the
  advisory published right after.
- Triage decision (done) and a status update by Friday 2026-10-30.
- The 5.x fix shared with you for review by about 2026-11-06, and the 4.x and
  3.x fixes as soon as they are ready.
- Credit in the advisory and CVE record, and you review the advisory text before
  it goes out. How would you like to be credited?
For reference, common coordinated-disclosure defaults run 45 to 90 days.

[Keep only if a complete workaround exists: If <date> must stand, we will publish
an advisory with the workaround "<workaround>" on that date and the fix as soon as
it is ready.]

Questions:
- Has anyone else been told, or do you or your employer already hold a CVE? If so
  we will use it instead of requesting another.
- Which time zone should we use for dates?
- Could you send an ASAN or valgrind trace if you have one, so we can tell whether
  it is a read or a write?

Can you agree to 2026-11-24? Please keep the details private until then. We will
continue in <private advisory link>.
```

### 2. Contingency: reporter publishes early

```
We have seen the public post. We are releasing patched versions <5.x.y, 4.x.y,
3.x.y> on <date/time> and publishing the advisory immediately after. We will keep
the credit we agreed. Please avoid adding further technical detail until the
release is out.
```

Then switch to the fast track: same-day release and advisory, with downstream notice measured in hours. Don't argue in public.

### 3. Downstream notice

Send it only to the packagers of 3.x, and only once all three fixes exist. Use their published security contacts, or the distros list with `[vs]` in the subject. Propose a public date of 2026-11-24, with an embargo of 14 days maximum and under 7 preferred. Share the patch at release time unless they must build before then.

```
Subject: [EMBARGOED until 2026-11-24 14:00 UTC] Security fix in hexmill

This notice is confidential until 2026-11-24 14:00 UTC. Please do not make it
public, share it beyond the people who must prepare the update, or push related
changes to public repositories before then.

Affected: hexmill, versions <ranges per line, unchecked = unknown>.
Fixed in: <5.x.y, 4.x.y, 3.x.y>, to be published at 2026-11-24 14:00 UTC.
Severity: <CVSS 3.1 vector, 9.8 provisional>.
Summary: heap buffer overflow in the PNG chunk reader, reachable through the
image decode entry points. No exploit steps.
Interim mitigation until you upgrade: <none | ...>.
Patch: <shared at release time | private fork access if you must build earlier>.
Identifier: <CVE / advisory id, if assigned>.

We will tell you immediately if the date changes.
```

### 4. Advisory draft (private until release)

| Field | Content |
|---|---|
| Title | Heap buffer overflow in PNG chunk reader |
| Summary | Applications that decode untrusted PNG files with hexmill can suffer memory corruption. |
| Affected / patched | `>= <first>, < 5.x.y`; `>= <first>, < 4.x.y`; `>= <first>, < 3.x.y`. Repeat per bindings package if they bundle the library. Unchecked versions are "unknown". |
| Affected functions | `<exported PNG decode entry points>` |
| Description | Precondition: an application passes untrusted PNG data to the decoder. The fix changes how chunk lengths are validated and allocated. No trigger details. |
| Workarounds | `<real workaround | none - upgrade>` |
| Severity | `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`. Revise after the read-or-write check. Write down your reasoning for Scope and Privileges Required. |
| CWE | CWE-122 (heap-based buffer overflow) |
| Credits | Reporter as agreed, you as remediation developer, any reviewer as remediation reviewer. |
| References | Fix commits and releases. No PoC. |

Request the CVE through the code host's CNA now, since the issue is accepted. The release never waits for the CVE.

### 5. Release-day checklist (Tue 2026-11-24)

1. Re-run the full tests locally on every line.
2. Merge the fix and the backports.
3. Tag and publish all three lines, plus the bindings packages.
4. Confirm each version installs from the public registry or package source.
5. Publish the advisory with the fixed versions per line and credits.
6. Publish release notes and the announcement.
7. Post to oss-security if you used the distro lists.
8. Send the reporter the links.

Avoid releasing at a time when the reporter and the packagers can't act on it.

### 6. Incident record (private advisory only)

```
Report: <id>   Received: <date, private reporting>   Responders: you (second: <none yet>)
Verdict: vulnerability - reproduced on 5.x, 4.x, 3.x
Severity: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (provisional) - precondition:
  untrusted PNG decoded - Scope/PR reasoning: S:U, no privileges needed in worst-case integration
Affected / patched: per line, introduced <unknown>, fixed <5.x.y, 4.x.y, 3.x.y>
Identifier: code-host CNA, request <date>, <status>
Timeline: see table above
Decision gate: 2026-10-30 - minimal patch fits ~5h => ship faster; else keep 11-24
Disclosure: 2026-11-24 14:00 UTC   Reporter deadline: <date>   Agreed: no, pending reply
Downstream notice: 3.x packagers, about 2026-11-17, patch at release time
CRA: <role | not applicable> - open
Open questions: bindings bundle the library?; exploitation?; second responder?; read vs write?
```

Send message 1 today and start the time-boxed patch spike.