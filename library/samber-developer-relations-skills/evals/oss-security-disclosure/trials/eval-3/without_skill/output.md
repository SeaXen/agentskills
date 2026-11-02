Three of your four asks don't survive 3-4 volunteer hours a month. I changed them, and `SECURITY.md` and the settings checklist below reflect that.

## Decisions I changed

1. **24-hour response is now 3 business days.** You have no on-call, so a report on Friday night or during a holiday would break the promise. The adopter's security team will check whether you kept it. A promise you keep beats a faster one you miss.
2. **No $500 bounty.** You have no budget line, no payer and no payment process. Bounties also attract a flood of low-quality and AI-generated reports, and you can't triage a flood. The policy offers credit in the advisory and requires a working proof of concept. If a sponsor funds it later, add it then.
3. **Safe harbor is rewritten, not copied.** A big project's clause usually rests on a legal entity, counsel and a hosted service they can authorize testing of. You are individuals with a personal-account repo and a library, so the clause is narrow: research on the reporter's own copies only. Have a lawyer or your adopter's counsel glance at it before you publish. I'm not a lawyer.
4. **`security@ferrokv.dev` must reach all three of you before you publish.** I can't verify that the domain or alias exists. If it reaches only one person, you have a single point of failure.

## SECURITY.md

Placeholders in `[brackets]` need your input.

````markdown
# Security Policy

## Supported versions

| Module                 | Status                                   |
| ---------------------- | ---------------------------------------- |
| `ferrokv/v2` (2.x)     | Supported: latest minor release gets fixes |
| `ferrokv` (1.x)        | [Critical fixes only until DATE / Unsupported] |

Fixes ship as a new patch release of the latest supported minor version.
We do not backport to older minors.

## Reporting a vulnerability

Do not open a public issue, pull request, or discussion for a suspected
vulnerability.

Use either channel:

1. **GitHub private reporting:**
   [Report a vulnerability](https://github.com/OWNER/ferrokv/security/advisories/new)
2. **Email:** security@ferrokv.dev

We do not monitor DMs, social media, or chat. If you reach out there, we will
ask you to resend through one of the channels above.

Please include:

- affected module and version, Go version, OS and architecture
- a minimal proof of concept that reproduces the issue
- the impact you believe it has (crash, data corruption, data disclosure, ...)

Reports without a working proof of concept may be closed until one is provided.

## What to expect

ferrokv is maintained by three volunteers. These are our commitments:

| Step                  | Target                                         |
| --------------------- | ---------------------------------------------- |
| Acknowledgement       | within 3 business days                         |
| Initial assessment    | within 10 business days: accepted, declined, or need more information |
| Fix for critical/high | within 30 days of acceptance, best effort      |
| Fix for medium/low    | within 90 days of acceptance, best effort      |

We keep you updated at least every 14 days until the issue is resolved.
If you hear nothing within the acknowledgement window, resend through the
other channel.

## Disclosure

We follow coordinated disclosure with a 90-day maximum:

1. We confirm the issue and develop a fix privately.
2. We release the fix and publish a GitHub Security Advisory, with a CVE
   where applicable. Advisories feed the Go vulnerability database.
3. You may publish your own write-up after the advisory is public.

If we have not fixed the issue 90 days after your report, you may disclose it.
We will ask you to wait if a fix is close, and we will agree a shorter timeline
if the issue is being actively exploited. We credit reporters in the advisory
unless you ask us not to.

## Scope

In scope: vulnerabilities in the code of the `ferrokv` and `ferrokv/v2`
modules, for example memory-safety bugs, corruption or crashes triggered by
crafted input or crafted data files, path handling flaws, and integrity
failures in crash recovery.

Out of scope:

- issues that need the attacker to already control the host process, the
  database files, or the machine running ferrokv
- resource use caused by legitimate API usage, unless a small input causes
  disproportionate cost
- vulnerabilities in dependencies (report them upstream; tell us if ferrokv
  is exposed in a way the upstream project may not know about)
- vulnerabilities in products that embed ferrokv (report them to that vendor)

## Safe harbor

If you act in good faith and follow this policy, we consider your research
authorized, we will not take or support legal action against you for it, and
we will say so to anyone who asks.

Good faith means:

- you test only against copies of ferrokv that you run yourself, on systems
  and data you own
- you do not access, modify, or keep data that is not yours; if you encounter
  such data, stop and report it
- you do not disrupt services or systems used by others
- you give us the time described above before disclosing

This statement binds the ferrokv maintainers only. We cannot grant permission
on behalf of companies that ship ferrokv. Do not test their production
systems without their consent. It is not legal advice.

## Rewards

We do not run a bounty program and do not pay for reports. We thank reporters
in the advisory and release notes.
````

## GitHub settings

Do these in order. Total time is about 45 minutes.

1. **Settings → Code security → Private vulnerability reporting → Enable.** This makes the second reporting channel real.
2. **Notification access.** A personal-account repo has no "Security manager" role, which is an org-only feature. Verify who actually gets notified of private reports. Add the other two maintainers as collaborators with admin, or move the repo to a GitHub org (better for bus factor). Have each person set Watch → Custom → Security alerts.
3. **Dependabot alerts and Dependabot security updates → Enable.**
4. **Secret scanning and push protection → Enable.**
5. **Code scanning → set up CodeQL** (it supports Go). Add `govulncheck ./...` to CI for both modules.
6. **Branch protection on `main`:** require PRs, require status checks, block force-push, and require review for changes to `SECURITY.md`.
7. **Require 2FA** for all three maintainers' accounts.
8. **Commit `SECURITY.md` at the repo root.** GitHub then shows it under the Security tab and in the "Report a vulnerability" flow. Check that the link renders.
9. **Test end to end.** Send a test mail to `security@ferrokv.dev` and file a test private report. Confirm all three of you are notified, then delete the test advisory.

## Internal runbook (don't publish)

- **Weekly rota.** One maintainer is on duty each week and checks the mailbox and the Security tab every 2 business days. That costs about 1 hour a month each.
- **Auto-reply on the alias:** "Received. We acknowledge within 3 business days."
- **Fix in private.** Use the advisory's temporary private fork to develop the fix, then publish the advisory and the release together.
- **Past reports.** Check whether the two DM reports from last year were ever fixed or disclosed. If not, treat them as the first two cases under this process.

## Before you publish

- **Supported-versions table:** choose the v1 status and date.
- **Alias:** confirm `security@ferrokv.dev` exists and reaches all three of you.
- **Adopter:** tell them you offer no private pre-notification list. They can watch the repo's releases and security advisories.
- **Safe-harbor wording:** have someone qualified review it.
- **Scope:** correct the list if ferrokv has features I haven't seen, such as a network listener.