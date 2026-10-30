# Message templates: reporters, downstreams, users

Read this when writing any message to a co-responder, a reporter, a downstream consumer or the public.

Contents: internal note, acknowledgement, counter-offer, need-info, not-a-vulnerability, payment demand, early-disclosure response, fix review, downstream embargo notice, publication notice, CVE dispute, upstream redirect.

## Rules for every message

- Fill every `<...>` before sending. Values that exist only on release day (advisory URL, CVE id, final version) go in as `<<late: name>>` in messages prepared ahead; fill them on the day and never send one still marked.
- Give dates with a time zone, never "soon".
- State what you will do next and when the reporter will hear from you again.
- Keep it inside the private channel. Never move the discussion to public chat.
- Ask before naming the reporter publicly, and use the name and handle they choose. Name volunteer maintainers to outsiders only with their consent; "the maintainers" is enough.

## 0. Internal note to co-responders

Send through the private advisory draft or direct email, never a team chat or shared list.

```
Subject: Security report received - details in the private advisory only

A security report reached me on <date> through <channel>. I have opened a private
advisory draft and added you. Please read it there, do not discuss it in chat,
issues, pull requests, commit messages or branch names, and do not run any
attachment outside a disposable, network-off environment.
Proposed roles: <who reproduces, who fixes, who reviews and releases>.
Reply by <date> with your available hours until <reporter deadline>.
```

## 1. Acknowledgement with a dated plan

```
Thank you for the report. We received it on <date> and <have reproduced it against
<version> | will attempt reproduction by <date>>. The maintainers are looking at it.

We have noted your planned publication date of <date | none given>. Next step: a
triage decision by <date>. If it is confirmed, we aim to release a fix around
<date, time, time zone>, and we will share the fix with you before release so you
can confirm it.

A few questions so we can coordinate:
- Has anyone else been told about this, or have you requested a CVE yourself?
  We will request the identifier through <CNA path> once the issue is confirmed.
- How would you like to be credited (name, handle, organisation, or anonymous)?
- Which time zone should we use for dates?

Please keep the details private until the agreed date. We will continue in
<private advisory link | this thread>.
```

## 2. Counter-offer to a short deadline

Use when the fix is real work and the reporter's date cannot hold.

```
Thank you for the deadline of <date>. We are taking this seriously and want to
meet it where we can. Here is where we are:

- Confirmed: <yes / partially>, affecting <versions>.
- Work left: <fix + backports to N supported lines + release>, which we estimate
  at <X> days with <N> maintainers.
- Proposed disclosure: <date, time, time zone>, with patched releases out first.

We can offer: credit in the advisory and the CVE record, review of the fix
before release, and a co-reviewed advisory text. For reference, common
coordinated-disclosure defaults run from 45 to 90 days.

If <date> must stand, we will publish an advisory with the workaround
"<workaround>" on that date and the fix as soon as it is ready. Can you agree to
<proposed date>?
```

```
✓ Good - dated plan, the reason, what the reporter gets, a fallback that still protects users
✗ Bad  - "Please don't publish, we're volunteers." (no date, no trade, invites an early drop)
✗ Bad  - "Publishing would be irresponsible and we will report you." (a threat becomes the story)
```

## 3. Need more information

```
Thanks for the report. We could not reproduce it against <version> following the
steps provided. To continue, please send: the exact version, a minimal proof of
concept that runs against a released version, and the output you observed.
If we do not hear back by <date>, we will close the report; you can reopen it any time.
```

## 4. Not a vulnerability

```
Thank you for the detailed report. We have concluded this is not a security
vulnerability: <reason, citing the documentation line or the trust assumption,
e.g. "the docs state this function must not receive untrusted input">.
<We will fix the underlying bug publicly in <issue/PR> | No change is planned.>
If you have a proof of concept showing impact beyond this, please send it and
we will reassess.
```

Keep this reasoning somewhere citable after closing: it is the evidence if a third party later files a CVE for the same behaviour.

## 5. Payment demanded

```
Thank you for contacting us. This project does not run a bug bounty and does not
pay for reports; our process is described in <SECURITY.md link>. We will assess
the issue you describe on its merits and credit you in any resulting advisory.
To proceed, please submit the details through <channel>.
```

Send it once. Do not negotiate amounts. Escalate threats or harassment to the code host and to whoever handles conduct.

## 6. Reporter disclosed early

```
We have seen the public post. We are releasing patched versions <versions>
on <date/time> and publishing the advisory immediately after. We will keep the
credit we agreed. Please avoid adding further technical detail until the release is out.
```

## 6b. Fix review request to the reporter

```
The fix is ready in the private advisory's fork: <link>. Could you confirm by
<date, time zone> that it closes the issue, including on <other supported line>?
Planned release: <date, time, time zone>. Proposed advisory text is in the draft;
comments welcome. Credit will read: <credit as agreed>.
```

## 7. Downstream embargo notice

Send only to named contacts with a need to rebuild or redeploy; recipient and patch-sharing rules are in release-runbook.md. Adapted from the OpenSSF disclosure-guide embargo template.

```
Subject: [EMBARGOED until <date time TZ>] Security fix in <project>

This notice is confidential until <date, time, time zone>. Please do not make it
public, share it beyond the people who must prepare the update, or push related
changes to public repositories before then.

Affected: <package>, versions <ranges>.
Fixed in: <versions>, to be published at <date, time, time zone>.
Severity: <CVSS version and vector>.
Summary: <class of issue and affected API, no exploit steps>.
Interim mitigation until you upgrade: <configuration or usage change | none>.
Patch: <shared at release time | private fork access, only if you must build before release>.
Identifier: <CVE / advisory id, if assigned>.

We will tell you immediately if the date changes.
```

## 8. Publication notice

Post where users look: the advisory itself, release notes, the project's announcement channel.

```
<Project> <versions> fix <severity> <vulnerability class> in <affected API>
(<CVE id>, <advisory link>). Users of <affected versions> should upgrade.
Workaround if you cannot upgrade: <workaround | none>.
Thanks to <credited reporter> for reporting it.
```

## 9. CVE dispute to the assigning CNA

The text becomes part of the public record: state facts, cite sources, no tone.

```
Subject: Dispute of <CVE id> (<product>)

We maintain <product> (<repository URL>) and request that <CVE id> be rejected,
or marked disputed if rejection is not possible.

- Claimed issue: <one line from the record>.
- Why it is not a vulnerability: <the documented trust assumption, with link to the
  documentation line, or the precondition that makes it unexploitable>.
- History: reported on <date> through <channel | not reported to us>; our
  assessment, published at <link>, concluded <conclusion>.
- The record's score <score> assumes <assumption>; our documentation states <fact>.

<We were not contacted before assignment. | We assessed and closed the report on <date>, before the CVE was assigned.>
Please confirm receipt and the next step.
```

Send the same facts as correction requests to the code-host advisory database and each ecosystem database that copied the record.

## 10. Upstream redirect

```
Thank you. The behaviour you describe comes from <dependency> <version range>,
which we use but do not ship inside our package. Please report it to that
project through <its security policy link>. We will update our minimum version
once a fix is released and publish an advisory only if our own code makes the
flaw reachable. Please let us know when it is fixed.
```

When the project vendors, bundles or statically links the dependency, do not send this: release and advise as your own.
