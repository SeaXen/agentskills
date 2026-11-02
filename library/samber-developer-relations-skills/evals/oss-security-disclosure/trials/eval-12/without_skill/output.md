I did one half of this. I wrote the thread reply and SECURITY.md, but I'm recommending against pulling Bram's credit.

I haven't touched any repo. This session is not in `vashti-orm`, so SECURITY.md is below for you to commit.

## Why I'd keep his credit

- **Credit isn't a reward for good behavior.** It's the record of who found the bug. Removing it reads as retaliation, and the thread will screenshot it. You'd turn "reporter published early" into "maintainer punished reporter".
- **It weakens your case.** You have a clean story: acknowledged in 2 days, fix nearly done, he published 13 days before the agreed date. A credit dispute gives the thread something else to argue about.
- **It's hard to undo.** If you remove it and later regret it, the edit history is public.

If you want a consequence, put it in the policy for next time (see SECURITY.md below). Don't apply it retroactively.

## Do first, before replying

1. **Finish and release the fix now.** The payload is public, so every day of delay is exposure. Ship a patch release, even a narrow one that only validates `order_by`.
2. **Publish the advisory and request the CVE** at the same time as the release.
3. **Post a mitigation in the thread today.** Users can protect themselves before the release lands (see the reply).

## Thread reply (draft)

Fill in the `<…>` placeholders. I'd post it only after the release is ready or the ETA is firm.

> Thanks to everyone looking at this. Here is where things stand on the `order_by` SQL injection in vashti-orm.
>
> **What you can do right now**
> If you pass user input to `order_by`, restrict it to an allowlist of column names until you upgrade:
>
> ```python
> ALLOWED = {"created_at", "name", "id"}
> col = request.args.get("sort")
> if col not in ALLOWED:
>     col = "id"
> qs = Model.objects.order_by(col)
> ```
>
> **Fix and timeline**
> A fix is in progress and lands in `<version>`, targeted for `<date/time>`. The advisory and CVE request go out with the release.
>
> **Timeline**
> - `<date>`: reported privately by Bram
> - `<date>`: acknowledged (within 2 days)
> - `<date>`: coordinated disclosure date agreed as November 5
> - 2026-10-23: details published ahead of that date
>
> I'd have preferred to keep to November 5, because it would have let us ship the patch before the payload was public. I'm not disputing that the report was valid and well done. Bram will be credited in the advisory as the reporter.
>
> I'm adding a written disclosure policy (SECURITY.md) so the process is explicit for the next reporter.

The timeline tells the story without accusing anyone, and the readers who matter will draw the conclusion themselves. Don't reply to the "too slow" claim beyond the dates. If you want to answer it, the acknowledgment date in the timeline already does.

## Advisory credit line

> Reported by Bram `<surname/handle>`. Thanks for the report and the reproduction.

If you need to record the early publication, put it in the advisory's timeline as a neutral line: "Details were published on 2026-10-23, ahead of the agreed 2026-11-05 date."

## SECURITY.md (draft)

```markdown
# Security Policy

## Supported versions

| Version | Supported |
| ------- | --------- |
| `<latest minor>.x` | Yes |
| `<previous minor>.x` | Security fixes only |
| Older | No |

## Reporting a vulnerability

Do not open a public issue, pull request, or discussion for a security problem.

Report privately through either channel:

1. GitHub: **Security** tab, then **Report a vulnerability** (private vulnerability reporting).
2. Email: `<security@your-domain>`. PGP key: `<fingerprint or link>`.

Include:

- Affected version and Python version.
- A minimal reproduction or proof of concept.
- Your assessment of the impact.
- How you want to be credited, if at all.

## What to expect

| Step | Target |
| ---- | ------ |
| Acknowledgment | 3 business days |
| Triage and severity assessment | 10 business days |
| Fix or mitigation for confirmed issues | 90 days from the report |
| Status updates | At least every 14 days |

We will tell you if we confirm or reject the report, and why.

## Coordinated disclosure

- We follow a 90-day disclosure window, counted from the day we acknowledge your report.
- We will agree a disclosure date with you in writing. Both sides keep to it.
- We may ask to extend the window if a fix needs more time. We will give reasons, and you may decline.
- If you intend to publish before the agreed date, tell us first so we can ship a patch or mitigation.
- If we miss our own targets above, you may disclose after giving us 7 days' notice.
- If the vulnerability is being actively exploited, we may shorten the window by mutual agreement.

## Credit

- Reporters are credited in the advisory by default, using the name or handle they give us.
- Credit is for the finding, not for how the disclosure went, and we do not remove it afterward.
- You can ask to stay anonymous.

## Safe harbor

We will not take legal action against, or ask platforms to act against, anyone who:

- Reports in good faith, following this policy.
- Tests only against their own installations.
- Avoids privacy violations, data destruction, and service disruption.

## Scope

In scope: the `vashti-orm` package in this repository, including its query builder, migrations, and bundled backends.

Out of scope: vulnerabilities in applications that use vashti-orm unsafely (for example, building raw SQL from user input), third-party dependencies (report those upstream), and social engineering.

## Advisories

We publish fixed vulnerabilities as GitHub Security Advisories, request CVEs for confirmed issues, and note the fix in the changelog.
```

A few choices in the draft:

- **The 7-day notice clause** gives reporters an escape hatch if you stall. That makes "too slow" harder to claim, because the policy defines slow.
- **The "tell us first" line** is the closest thing to a rule against what Bram did. It's a request, not a penalty.
- **Targets are placeholders.** Only commit to numbers you will meet. Check that `<security@…>` exists and that private vulnerability reporting is enabled in the repo settings before you merge.

## Optional: a private note to Bram

A short, calm message often helps more than the thread:

> Hi Bram, thanks again for the report. I'm disappointed the details went out before November 5, since it forced us to respond in public before the patch was out. The fix ships `<date>`, and you're credited in the advisory. If you'd like to see the SECURITY.md draft and give feedback, I'd welcome it.

Whether to send it is your call. It costs nothing, and it may be the only way to get the agreement to stick next time.