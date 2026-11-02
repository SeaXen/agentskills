**Next action:** don't send anything yet. Spend 30 minutes on re-triage (step 1 below). The dispute becomes public record, and right now nobody has written down why this is by-design.

## Corrections to your plan

- **MITRE may not be the right recipient.** Disputes go to the CNA that assigned the ID. Check the CVE record's assigner (cve.org record, "assigner" field) first. It may be GitHub, VulDB, or MITRE.
- **Expect DISPUTED, rarely REJECTED.** Both curl cases ended as DISPUTED or lowered scores. Ask for REJECT, accept DISPUTED, and make sure the record carries the tag.
- **Becoming a CNA won't kill this CVE.** CNA status does not reach back to IDs another CNA assigned. curl's CVE-2023-52071 is the example: it was assigned just before curl became a CNA, and it took weeks of escalation to reject. Becoming a CNA is still a sound long-term move, since a third party has now filed against you, but it won't help this week.
- **The thread must not attack the reporter.** Public arguing and tone become the story. Naming the reporter needs their consent, and so does quoting their email.
- **Your own process left a gap.** Kofi's private "working as documented" left no public record, so you have no citable evidence. Fix that first (step 2).

## Steps

1. **Re-triage (30 min).** I have not seen the report, the docs, or the code, so I can't confirm "by-design". Answer these before dispute text goes out:
   - Does any project doc (README, godoc, examples) call this option safe for untrusted input? The more specific safety claim governs. If one exists, this is in scope and the plan changes.
   - Can untrusted data set the option? That means an env var, a config file, or a request field. If only Go code sets it, the attacker cannot.
   - What exactly did the reporter claim? Reread the email. It may be narrower than "the option exists".
   - Which CNA assigned the ID, and who is the assigner on the CVE record?
   - Does the option log or warn at runtime?
2. **Publish a citable public note (20 min).** Put a "Not a vulnerability: `InsecureSkipVerify` passthrough" section in the docs or SECURITY.md, with the doc line and reasoning. Leave out the reporter's details. This is your dispute evidence.
3. **Email the reporter privately (10 min), using template 4.** Ask them to support the dispute, because CNAs weigh the reporter's view. Do not mention a CNA, and make no threats.
4. **File the dispute (10 min).** Text below.
5. **File corrections with every copy (30 min).** Send the same facts to:
   - the GitHub advisory database
   - the Go vulnerability database, requesting a NOT_A_VULNERABILITY exclusion
   - the OSV entry, after the imports are corrected

   While waiting, reply to the three dependents with the text below.
6. **Post the thread**, only after steps 2 and 4 are done, so it can link both.

Total: about 2 hours of work. Database responses take days to weeks.

## Dispute to the assigning CNA

```
Subject: Dispute of <CVE id> (saltwick)

We maintain saltwick (<repository URL>) and request that <CVE id> be rejected,
or marked disputed if rejection is not possible.

- Claimed issue: improper certificate validation (CWE-295) through the
  InsecureSkipVerify passthrough option.
- Why it is not a vulnerability: the option is opt-in, set only by the
  application developer in code, and documented as "disables verification, for
  tests only" (<link to doc line>). An attacker cannot enable it. It mirrors the
  documented semantics of crypto/tls Config.InsecureSkipVerify. <Add only if
  verified in step 1: the option cannot be set from environment variables,
  configuration files or network input.>
- History: reported on <date> through <channel>; we assessed it and replied
  on <date> that the behaviour is as documented. Our published assessment,
  <link>, concludes it is not a vulnerability.
- The record's score of 9.8 assumes an unauthenticated network attacker needing
  no privileges. Enabling the option requires the privileges of the application
  developer, who chose to turn verification off.

We were not contacted before the CVE was assigned.
Please confirm receipt and the next step.
```

Delete the last line if the reporter or the CNA did contact you. Fill every `<...>` before sending.

## Reply to the three dependents

```
Thanks for raising this. <CVE id> concerns the InsecureSkipVerify passthrough
option, which is documented as disabling verification for tests only. It does not
affect applications that leave it unset. We have disputed the record with
<CNA> and asked the GitHub and Go vulnerability databases to correct their
entries (<links>). Until then, govulncheck flags the module regardless of
whether you call the option. Our assessment: <link to public note>.
```

## Thread (6 posts)

Each post is under 280 characters. Neutral, factual, and it owns the process gap.

1. `A CVE (<CVE id>, CVSS 9.8) now exists against saltwick for its InsecureSkipVerify passthrough option. We believe it is not a vulnerability and have disputed it. Here is what happened and why. 🧵`
2. `The option does what its docs say: "disables verification, for tests only." Only the application developer can turn it on, in code. It mirrors Go's crypto/tls InsecureSkipVerify. No attacker can enable it remotely.`
3. `Eight months ago the issue was reported to us privately. We concluded it was working as documented and closed it. We should have published that reasoning then. We did not, and that gap is on us. It is now public: <link>.`
4. `We have asked <CNA> to reject or mark the CVE disputed, and asked the GitHub and Go vulnerability databases to correct their entries. If you see govulncheck flags on saltwick: they should not affect apps that leave the option unset.`
5. `We are also reviewing whether the docs and the option's name make the risk clear enough, and will say so publicly if we change anything. Dependents: details and reply in your issues.`
6. `Process fix: every closed security report now gets a public note of the conclusion. <If true: we are also considering becoming a CNA.> Questions: <contact>.`

Check three things before posting:
- Post 3 keeps the reporter anonymous. Name them only with their consent.
- Post 5 promises a docs review. Delete it if you won't do one.
- Post 6's CNA clause is optional.

**Open questions that block sending:** the five items in step 1.

**Next:** open the reporter's original email and answer the first two re-triage questions.