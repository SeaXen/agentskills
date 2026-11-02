🔴 First, the live issue: a working auth-bypass PoC has been sitting in a public issue for 40 minutes. Before anything else, get it out of public view — edit the issue to strip the PoC/reproduction details (or delete and ask the reporter to resubmit privately), and turn on **Settings → Security → Private vulnerability reporting** on this repo so future reports like this land in a private advisory instead of a public issue at all. The template below is your fallback for reports that arrive via the public tracker anyway (most reporters won't find the private path first).

## `security` label

- Name: `security`
- Color: `#d73a4a` (GitHub's default "bug"-red, reserved so it's visually distinct from other labels at a glance)
- Description: `Security vulnerability report — do not discuss exploit details publicly`

## `.github/ISSUE_TEMPLATE/security_report.yml`

Use GitHub's issue-forms format (not a markdown template) so fields are structured and required ones can't be skipped:

```yaml
name: 🔒 Security Vulnerability Report
description: Report a security vulnerability. For anything with a working exploit, use Private Vulnerability Reporting instead (Security tab → Report a vulnerability).
title: "[SECURITY] "
labels: ["security"]
body:
  - type: markdown
    attributes:
      value: |
        ⚠️ **If you have a working proof-of-concept or exploit, stop — do not post it here.**
        Use the "Report a vulnerability" button on the Security tab instead, so details stay private until a fix ships.
        Only use this public form for reports with no working exploit, or already publicly known issues.

  - type: input
    id: affected-version
    attributes:
      label: Affected version / commit
      description: Exact version, tag, or commit SHA where you confirmed this
      placeholder: v1.4.2 or commit abc1234
    validations:
      required: true

  - type: dropdown
    id: vuln-type
    attributes:
      label: Vulnerability type
      options:
        - Authentication / authorization bypass
        - Injection (SQL, command, header, etc.)
        - Request smuggling / parsing confusion
        - Information disclosure
        - Denial of service
        - Remote code execution
        - Cross-site scripting
        - Other (describe below)
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: Description
      description: What's the vulnerability and why is it exploitable? No PoC/payload here — that goes in private reporting.
    validations:
      required: true

  - type: textarea
    id: impact
    attributes:
      label: Impact
      description: What can an attacker actually do — bypass auth, read other users' data, crash the process? Who is affected (default config, or only specific setups)?
    validations:
      required: true

  - type: dropdown
    id: severity
    attributes:
      label: Your severity estimate
      description: Rough CVSS-style gut check, not binding
      options:
        - Critical (full compromise, no auth needed)
        - High (significant impact, some precondition)
        - Medium (limited impact or hard to reach)
        - Low
        - Not sure
    validations:
      required: false

  - type: textarea
    id: reproduction
    attributes:
      label: Steps to reproduce
      description: High-level steps only if this form is public. Full requests/payloads belong in a private report.
    validations:
      required: false

  - type: textarea
    id: suggested-fix
    attributes:
      label: Suggested fix (optional)
    validations:
      required: false

  - type: checkboxes
    id: disclosure
    attributes:
      label: Disclosure
      options:
        - label: I have not published exploit details anywhere else (blog, social media, other trackers)
          required: false
        - label: I'm open to coordinated disclosure and can wait for a fix before this becomes fully public
          required: false

  - type: input
    id: contact
    attributes:
      label: Contact (email or handle)
      description: So maintainers can follow up privately if needed
    validations:
      required: false
```

## `.github/ISSUE_TEMPLATE/config.json`

Point people at private reporting before they even reach the form list:

```json
{
  "blank_issues_enabled": true,
  "contact_links": [
    {
      "name": "🔒 Report a vulnerability privately",
      "url": "https://github.com/samber/otterlink/security/advisories/new",
      "about": "Preferred for anything with a working exploit — stays private until a fix ships."
    }
  ]
}
```

## Getting notified without a mailing list

Since there's no security list yet, wire a lightweight alert instead of standing up infrastructure: a repo GitHub Action on `issues: [labeled]` that fires when the label is `security`, posting to whatever channel you actually check (email via `dawidd6/action-send-mail`, or a Slack/Discord webhook). Cheaper than a list, and it also fires automatically for advisories once private reporting is enabled.

Add a one-line pointer in `SECURITY.md` at repo root: "Report vulnerabilities via [Private Vulnerability Reporting], not public issues" — that's what most reporters check before opening an issue at all.

Want me to actually create these files (label, template, config, `SECURITY.md`) in the repo now?