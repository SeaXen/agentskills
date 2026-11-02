**Bottleneck: every issue needs your judgment right now. Fix: cut human decision points to two per month.** Five phases, do in order.

1. Labels + issue forms (intake structure)
2. Automation (stale/close, no bot maintenance)
3. Recruit triage-only volunteers (no commit needed)
4. One-time 380-issue backlog reset
5. Your 20-min/month loop

Everything below is copy-paste ready. Swap `OWNER/cindermark` for real path.

## 1. Labels

**Run this once — creates 24 labels on the repo:**

```bash
REPO="OWNER/cindermark"

# type
gh label create "type:bug"        --repo "$REPO" --color d73a4a --description "Incorrect behavior"
gh label create "type:regression" --repo "$REPO" --color e99695 --description "Worked before, broke now"
gh label create "type:security"   --repo "$REPO" --color b60205 --description "Vulnerability — should arrive via private report, not this label"
gh label create "type:feature"    --repo "$REPO" --color a2eeef --description "New capability or syntax"
gh label create "type:docs"       --repo "$REPO" --color 0075ca --description "Documentation only"
gh label create "type:question"   --repo "$REPO" --color d876e3 --description "Should probably be a Discussion"

# priority
gh label create "priority:0-critical" --repo "$REPO" --color b60205 --description "Same-day attention: security, data loss, common-path crash"
gh label create "priority:1-high"     --repo "$REPO" --color d93f0b --description "Next monthly pass"
gh label create "priority:2-normal"   --repo "$REPO" --color fbca04 --description "Default"
gh label create "priority:3-low"      --repo "$REPO" --color c5def5 --description "Nice to have, no urgency"

# status (workflow)
gh label create "status:needs-triage"             --repo "$REPO" --color ededed --description "Not yet looked at — default on new issues"
gh label create "status:needs-repro"              --repo "$REPO" --color fef2c0 --description "Missing minimal reproduction"
gh label create "status:needs-info"               --repo "$REPO" --color fef2c0 --description "Waiting on reporter"
gh label create "status:confirmed"                --repo "$REPO" --color 0e8a16 --description "Reproduced and valid"
gh label create "status:needs-maintainer-decision" --repo "$REPO" --color 5319e7 --description "Judgment call only the maintainer can make"
gh label create "status:blocked"                  --repo "$REPO" --color 5319e7 --description "Blocked on something external"
gh label create "status:wontfix"                  --repo "$REPO" --color cfd3d7 --description "Valid but declined"
gh label create "status:duplicate"                --repo "$REPO" --color cfd3d7 --description "Duplicate of another issue"
gh label create "status:stale"                    --repo "$REPO" --color eeeeee --description "Auto-flagged for inactivity"

# area — rename to match cindermark's real module names
gh label create "area:parser"           --repo "$REPO" --color 1d76db
gh label create "area:renderer"         --repo "$REPO" --color 1d76db
gh label create "area:extensions"       --repo "$REPO" --color 1d76db
gh label create "area:cli"              --repo "$REPO" --color 1d76db
gh label create "area:spec-compliance"  --repo "$REPO" --color 1d76db
gh label create "area:performance"      --repo "$REPO" --color 1d76db

# community
gh label create "good-first-issue" --repo "$REPO" --color 7057ff
gh label create "help-wanted"      --repo "$REPO" --color 008672
```

## 2. Issue forms

Force structure at intake — kills the back-and-forth that eats your 20 minutes.

**Write `.github/ISSUE_TEMPLATE/bug_report.yml`:**

```yaml
name: Bug report
description: Something renders incorrectly, crashes, or diverges from spec.
title: "[bug]: "
labels: ["type:bug", "status:needs-triage"]
body:
  - type: checkboxes
    id: searched
    attributes:
      label: Checked for duplicates
      options:
        - label: I searched open and closed issues and didn't find this reported already.
          required: true
  - type: input
    id: version
    attributes:
      label: cindermark version
      placeholder: "e.g. v2.4.1, or commit SHA"
    validations:
      required: true
  - type: textarea
    id: repro
    attributes:
      label: Minimal Markdown input that reproduces the bug
      description: Smallest possible input. Issues without this get labeled needs-repro and may close after 3 weeks of silence.
      render: markdown
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Expected output
    validations:
      required: true
  - type: textarea
    id: actual
    attributes:
      label: Actual output
    validations:
      required: true
  - type: input
    id: environment
    attributes:
      label: Environment
      placeholder: "OS, runtime/version, extensions enabled"
```

**Write `.github/ISSUE_TEMPLATE/feature_request.yml`:**

```yaml
name: Feature request
description: Propose new syntax support, an extension, or an API change.
title: "[feature]: "
labels: ["type:feature", "status:needs-triage"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Problem
      description: What can't you do today? Concrete use case, not "it would be nice."
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Proposed solution
  - type: dropdown
    id: pr
    attributes:
      label: Are you willing to submit a PR for this?
      options: ["Yes", "No", "Maybe, with guidance"]
    validations:
      required: true
```

**Write `.github/ISSUE_TEMPLATE/config.yml`** — kills unstructured issues, routes questions and security reports off the tracker:

```yaml
blank_issues_enabled: false
contact_links:
  - name: Question / usage help
    url: https://github.com/OWNER/cindermark/discussions
    about: Issues are for bugs and feature requests only.
  - name: Report a security vulnerability
    url: https://github.com/OWNER/cindermark/security/advisories/new
    about: Do not open a public issue for security vulnerabilities.
```

## 3. Automation — no bot to maintain

**Enable private vulnerability reporting**: repo Settings → Security → Enable "Private vulnerability reporting." Security reports now bypass the public queue entirely and notify you directly.

**Write `.github/workflows/stale.yml`** — auto-closes what you'd never get to anyway:

```yaml
name: Triage automation

on:
  schedule:
    - cron: "0 6 * * *"
  workflow_dispatch:

permissions:
  issues: write

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9
        with:
          only-labels: "status:needs-info"
          stale-issue-label: "status:stale"
          days-before-stale: 14
          days-before-close: 7
          exempt-issue-labels: "priority:0-critical"
          stale-issue-message: >
            Closing due to no response in 21 days. If this is still an issue,
            reopen with the requested information.

      - uses: actions/stale@v9
        with:
          only-labels: "type:feature"
          stale-issue-label: "status:stale"
          days-before-stale: 180
          days-before-close: 30
          exempt-issue-labels: "help-wanted,good-first-issue,priority:0-critical,priority:1-high,status:confirmed"
          stale-issue-message: >
            No activity in 6 months. Closing to keep the backlog honest —
            reopen any time if it's still wanted.
```

## 4. Recruit triage-only volunteers

Key unlock: GitHub has a **"Triage" repo role** — label, assign, close, mark duplicate, manage issues. No push, no merge, no commit access at all. This is the role for people willing to help who don't want the responsibility of shipping code.

- Post a pinned issue/discussion asking for volunteers.
- Grant via Settings → Collaborators → role "Triage."
- One person "on call" per week, rotating: they clear `status:needs-triage`, apply `type:`/`area:` labels, close obvious duplicates, escalate anything real to `status:needs-maintainer-decision`.
- **If zero volunteers show up: skip the rotation.** Automation + your monthly pass still holds the line, just slower on feature requests.

**Add to CONTRIBUTING.md:**

```markdown
## Help without writing code

cindermark needs triage help more than it needs more code. If you want
to help sort incoming issues, you get GitHub's "Triage" role — full
ability to manage issues, no commit access. See [TRIAGE.md](./TRIAGE.md).
```

**Write `TRIAGE.md`** (public — sets expectations so silence doesn't read as neglect):

```markdown
# Triage policy

cindermark has one maintainer with about 20 minutes a month for issue
work, and no one else with commit access. This explains how issues get
handled.

## What happens to a new issue

1. The issue form requires a minimal reproduction, expected vs. actual
   output, and version. Skip it and you get `status:needs-repro`.
2. A volunteer triager labels it, closes duplicates/invalid reports,
   and marks it `status:confirmed` or `status:needs-maintainer-decision`
   if it needs a real judgment call.
3. The maintainer checks two label filters, monthly:
   `priority:0-critical` (same day) and `status:needs-maintainer-decision`.
4. Everything else stays open and labeled. That's a valid end state —
   it means "seen, ranked, waiting for capacity," not "ignored."

## Becoming a triager

You don't need to write code. GitHub's "Triage" role lets you label,
assign, and close issues without commit access. Comment on the pinned
recruitment issue if you want it.

## Stale issues

`status:needs-info` closes after 21 days of silence. Feature requests
close after 6 months of no engagement. Auto-closed isn't rejected —
reopen with new information.

## Security

Don't open a public issue for a vulnerability. See [SECURITY.md](./SECURITY.md).
```

**Write `SECURITY.md`:**

```markdown
# Security policy

cindermark is a single-maintainer project used by roughly 40,000
downstream projects. Report vulnerabilities privately:
https://github.com/OWNER/cindermark/security/advisories/new

Don't discuss an unpatched vulnerability publicly before a fix ships.

## Response time

Best-effort, one maintainer, no SLA. Target: acknowledgement within 7 days.

## Scope

Most relevant for a Markdown renderer: XSS via crafted input, ReDoS/
catastrophic backtracking, memory/resource exhaustion on adversarial
input. Unsure if it qualifies? Report privately anyway.
```

## 5. One-time 380-issue backlog reset

**Warning — this bulk-closes issues. Reversible (anyone can reopen), but noisy: every author gets an email. Run the count check before the close.**

```bash
REPO="OWNER/cindermark"

# 1. Label everything untouched so nothing falls outside the new system
gh issue list --repo "$REPO" --state open --limit 500 --json number,labels \
  --jq '.[] | select(.labels | length == 0) | .number' \
  | xargs -I{} gh issue edit {} --repo "$REPO" --add-label "status:needs-triage"

# 2. Dry run — check the count BEFORE closing anything
gh issue list --repo "$REPO" --state open --search "created:<2025-09-23" \
  --json number --jq 'length'

# 3. Only after confirming the count looks right: bulk-close issues open
#    >1 year, excluding anything already confirmed or critical
gh issue list --repo "$REPO" --state open --search "created:<2025-09-23" \
  -l "-status:confirmed" -l "-priority:0-critical" --json number --jq '.[].number' \
  | xargs -I{} gh issue close {} --repo "$REPO" --comment \
  "Backlog reset: closing issues open over a year with no update. Still relevant? Reopen or comment with a minimal repro and it'll get triaged fresh."
```

## 6. Your 20 min/month, exactly

1. Open saved search `is:open label:priority:0-critical`. Anything here: drop everything, same day, not monthly.
2. Open saved search `is:open label:status:needs-maintainer-decision`. 1–2 min per item, yes/no/later.
3. If triagers are behind, spot-check `is:open label:status:needs-triage sort:created-asc` for the oldest untouched ones.

Nothing else needs your eyes. A labeled, un-actioned issue is the system working, not the system failing.

**Next: run the label-creation script in section 1, then commit the two issue-form YAML files.**