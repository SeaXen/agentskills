Assumption stated up front: "harness" = GitHub Actions (schedule + repo-event triggers), with `claude -p` doing the judgment-heavy steps — matching the `claude -p` scripting patterns already in use elsewhere. If the actual CI system is different, the `claude -p` calls are the only parts that'd need porting; the trigger/data-flow design carries over.

Four workflows, wired to reinforce each other: tag pushes announce themselves immediately (time-sensitive), the backlog gets sliced into a weekly 2-minute read instead of one 340-item wall, CFP reminders fire on the same 3-week horizon already mentioned, and Discord gets one consolidated signal per week instead of three separate pings.

## Setup (one-time)

**Create the required labels:**
```bash
gh label create needs-triage --color FBCA04 --description "Awaiting first pass"
gh label create bug --color d73a4a
gh label create feature-request --color a2eeef
gh label create question --color d876e3
gh label create docs --color 0075ca
gh label create needs-info --color d4c5f9
gh label create possible-duplicate --color cfd3d7
gh label create bug-confirmed --color b60205
gh label create security --color b60205
gh label create roadmap --color 5319e7
gh label create pinned --color 000000
gh label create cfp --color 0e8a16
gh label create triage-digest --color 0e8a16
gh label create help-wanted --color 008672
```

**Set secrets and variables:**
```bash
gh secret set ANTHROPIC_API_KEY
gh secret set DISCORD_RELEASE_WEBHOOK_URL
gh secret set DISCORD_DIGEST_WEBHOOK_URL
gh variable set RUN_CFP_RESEARCH --body "true"   # set to "false" to pause the monthly deep-research pass
```

**Create the CFP data file** (source of truth the automation reads but never writes):

`.github/cfp-targets.yml`
```yaml
# Plimsoll CFP tracker — read by cfp-tracker.yml. The workflow never writes here;
# it only reads. Reminders fire for entries with status: open, based on cfp_close.
# Set status to submitted / accepted / declined / closed to stop reminders for one entry.
#
# Example shape (nothing below is a real deadline — replace with real targets):
# - conference: "Monitorama PDX"
#   url: "https://monitorama.com/"
#   cfp_close: "2026-11-15"
#   event_date: "2027-05-01"
#   status: open
#   notes: "Talk idea: agent-based root-causing from Plimsoll traces"

[]
```

---

## `.github/workflows/release.yml`
Reacts to the repository event (`push: tags`), so a Thursday tag can't ship silently.

```yaml
name: Release notes on tag push

on:
  push:
    tags:
      - 'v*.*.*'

permissions:
  contents: write

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Resolve previous tag
        id: prev
        run: |
          CURRENT="${GITHUB_REF_NAME}"
          PREV=$(git describe --tags --abbrev=0 "${CURRENT}^" 2>/dev/null || git rev-list --max-parents=0 HEAD)
          echo "prev=$PREV" >> "$GITHUB_OUTPUT"
          echo "current=$CURRENT" >> "$GITHUB_OUTPUT"

      - name: Collect conventional commits since last tag
        run: |
          git log "${{ steps.prev.outputs.prev }}..${{ steps.prev.outputs.current }}" \
            --pretty=format:'- %s (%h)' --no-merges > commits.txt

      - name: Set up Claude Code CLI
        run: npm install -g @anthropic-ai/claude-code

      - name: Draft release notes
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          PROMPT="You write release notes for Plimsoll, an open-source observability agent (MIT, Go). \
          Input is Conventional Commits since the last tag. Group into Keep-a-Changelog sections \
          (Added / Changed / Fixed / Security) from each commit's type prefix (feat/fix/perf/security/etc), \
          dropping pure chore/ci noise unless security-relevant. Put anything with '!' or 'BREAKING CHANGE' \
          under a ## Breaking heading at the top. Name the affected command/flag/endpoint specifically — \
          never just 'improved X'. Output plain Markdown only, no preamble. Commits:
          $(cat commits.txt)"
          claude --system-prompt "" --tools "" --setting-sources "" --model sonnet \
            -p "$PROMPT" > release-notes.md

      - name: Create GitHub release
        env:
          GH_TOKEN: ${{ github.token }}
        run: |
          FLAGS=""
          case "${{ steps.prev.outputs.current }}" in
            *-rc*|*-beta*|*-alpha*) FLAGS="--prerelease" ;;
          esac
          gh release create "${{ steps.prev.outputs.current }}" \
            --title "${{ steps.prev.outputs.current }}" \
            --notes-file release-notes.md $FLAGS

      - name: Announce in Discord
        env:
          WEBHOOK: ${{ secrets.DISCORD_RELEASE_WEBHOOK_URL }}
        run: |
          TAG="${{ steps.prev.outputs.current }}"
          SUMMARY=$(head -c 1500 release-notes.md)
          BODY=$(jq -n --arg tag "$TAG" --arg repo "${{ github.repository }}" --arg summary "$SUMMARY" \
            '{content: ("🚀 **Plimsoll " + $tag + "** is out.\n" + $summary + "\n\nFull notes: https://github.com/" + $repo + "/releases/tag/" + $tag)}')
          curl -sS -X POST "$WEBHOOK" -H "Content-Type: application/json" -d "$BODY"
```

---

## `.github/workflows/cfp-tracker.yml`
Weekly urgency pass (matches the "3-week" horizon already in play) plus a monthly research pass that only ever *suggests* — it never writes to `cfp-targets.yml` itself, so a hallucinated date can't silently become a tracked deadline.

```yaml
name: CFP tracker

on:
  schedule:
    - cron: '0 9 * * 1'   # Monday 09:00 UTC — adjust to your TZ
  workflow_dispatch: {}

permissions:
  contents: read
  issues: write

jobs:
  weekly-status:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Compute urgency per tracked CFP
        run: |
          pip install --quiet pyyaml
          python3 - <<'PY' > status.md
          import yaml, datetime

          with open(".github/cfp-targets.yml") as f:
              targets = yaml.safe_load(f) or []

          today = datetime.date.today()
          urgent, upcoming = [], []
          for t in targets:
              if t.get("status") != "open":
                  continue
              close = datetime.date.fromisoformat(str(t["cfp_close"]))
              days = (close - today).days
              line = f"- **{t['conference']}** — CFP closes {close.isoformat()} ({days}d) — {t.get('url','')}"
              (urgent if days <= 21 else upcoming).append(line)

          out = []
          if urgent:
              out.append("### ⚠️ Closing within 3 weeks\n" + "\n".join(urgent))
          if upcoming:
              out.append("### Tracked, not yet urgent\n" + "\n".join(upcoming))
          if not urgent and not upcoming:
              out.append("No open CFP targets tracked in `.github/cfp-targets.yml` yet.")

          with open("status.md", "w") as f:
              f.write("\n\n".join(out))
          PY

      - name: Update pinned tracker issue
        env:
          GH_TOKEN: ${{ github.token }}
        run: |
          TITLE="📣 CFP Tracker"
          NUM=$(gh issue list --search "in:title \"$TITLE\"" --state open --json number --jq '.[0].number')
          if [ -z "$NUM" ] || [ "$NUM" = "null" ]; then
            URL=$(gh issue create --title "$TITLE" --body-file status.md --label cfp)
            NUM=$(basename "$URL")
            gh issue pin "$NUM" || true
          else
            gh issue comment "$NUM" --body-file status.md
            gh issue edit "$NUM" --body-file status.md
          fi

  monthly-research:
    runs-on: ubuntu-latest
    if: ${{ vars.RUN_CFP_RESEARCH != 'false' }}
    steps:
      - uses: actions/checkout@v4

      - name: Only run on the first Monday of the month
        id: gate
        run: |
          DAY=$(date +%d)
          [ "$DAY" -le 7 ] && echo "run=true" >> "$GITHUB_OUTPUT" || echo "run=false" >> "$GITHUB_OUTPUT"

      - name: Set up Claude Code CLI
        if: steps.gate.outputs.run == 'true'
        run: npm install -g @anthropic-ai/claude-code

      - name: Research new CFP candidates
        if: steps.gate.outputs.run == 'true'
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          pip install --quiet pyyaml
          TRACKED=$(python3 -c "import yaml;print([t['conference'] for t in (yaml.safe_load(open('.github/cfp-targets.yml')) or [])])")
          PROMPT="Search for observability, SRE, platform-engineering, and DevOps conferences with a call \
          for proposals opening or closing in the next 60 days that Plimsoll (an open-source observability \
          agent) doesn't already track. Already tracked: $TRACKED. For each new candidate give: name, CFP \
          close date (cite the source URL — do not guess), event date, one sentence on fit. If unsure of a \
          date, say so explicitly rather than estimating. Markdown, max 8 candidates."
          claude --model sonnet --allowedTools "WebSearch,WebFetch" -p "$PROMPT" > research.md \
            || echo "Research step failed — check logs." > research.md

      - name: Post research as a comment for human review
        if: steps.gate.outputs.run == 'true'
        env:
          GH_TOKEN: ${{ github.token }}
        run: |
          TITLE="📣 CFP Tracker"
          NUM=$(gh issue list --search "in:title \"$TITLE\"" --state open --json number --jq '.[0].number')
          if [ -n "$NUM" ] && [ "$NUM" != "null" ]; then
            { echo "### 🔍 Monthly CFP research — review before adding to \`.github/cfp-targets.yml\`"; echo; cat research.md; } \
              | gh issue comment "$NUM" --body-file -
          fi
```

---

## `.github/workflows/issue-triage.yml`
Doesn't try to force ownership onto anyone — it structures intake so the pile stops growing unstructured, sweeps genuinely dead issues, and turns the existing 340 into a bounded weekly read.

```yaml
name: Issue triage

on:
  issues:
    types: [opened, labeled]
  schedule:
    - cron: '0 8 * * 5'   # Friday 08:00 UTC — adjust to your TZ
  workflow_dispatch: {}

permissions:
  contents: read
  issues: write

jobs:
  triage-new-issue:
    if: github.event_name == 'issues' && github.event.action == 'opened'
    runs-on: ubuntu-latest
    steps:
      - name: Set up Claude Code CLI
        run: npm install -g @anthropic-ai/claude-code

      - name: Classify issue
        id: classify
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ISSUE_TITLE: ${{ github.event.issue.title }}
          ISSUE_BODY: ${{ github.event.issue.body }}
        run: |
          PROMPT="Classify this GitHub issue for the Plimsoll observability agent. Respond with ONLY \
          compact JSON: {\"category\":\"bug|feature-request|question|docs|needs-info\"}. \
          Title: $ISSUE_TITLE. Body: $ISSUE_BODY"
          claude --system-prompt "" --tools "" --setting-sources "" --model haiku -p "$PROMPT" > classification.json
          echo "category=$(jq -r '.category // "needs-info"' classification.json)" >> "$GITHUB_OUTPUT"

      - name: Apply labels
        env:
          GH_TOKEN: ${{ github.token }}
        run: |
          gh issue edit "${{ github.event.issue.number }}" \
            --add-label "needs-triage,${{ steps.classify.outputs.category }}"

      - name: Flag likely duplicates
        env:
          GH_TOKEN: ${{ github.token }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ISSUE_TITLE: ${{ github.event.issue.title }}
        run: |
          gh issue list --state open --limit 60 --json number,title --jq '.[] | "\(.number): \(.title)"' > recent-titles.txt
          PROMPT="New issue title: \"$ISSUE_TITLE\". Below are existing open issue numbers and titles. \
          If the new one is very likely a duplicate of one, respond with ONLY that issue number, else \
          respond with ONLY the word none. Existing:
          $(cat recent-titles.txt)"
          MATCH=$(claude --system-prompt "" --tools "" --setting-sources "" --model haiku -p "$PROMPT" | tr -d '[:space:]')
          if echo "$MATCH" | grep -qE '^[0-9]+$'; then
            gh issue edit "${{ github.event.issue.number }}" --add-label "possible-duplicate"
            gh issue comment "${{ github.event.issue.number }}" \
              --body "🤖 This might be a duplicate of #$MATCH — a maintainer will confirm, leaving both open until then."
          fi

  clear-triage-label:
    if: github.event_name == 'issues' && github.event.action == 'labeled'
    runs-on: ubuntu-latest
    steps:
      - name: Remove needs-triage once a maintainer has categorized the issue
        if: contains(fromJSON('["bug-confirmed","wontfix","duplicate","accepted","roadmap"]'), github.event.label.name)
        env:
          GH_TOKEN: ${{ github.token }}
        run: gh issue edit "${{ github.event.issue.number }}" --remove-label needs-triage

  weekly-stale-and-digest:
    if: github.event_name == 'schedule' || github.event_name == 'workflow_dispatch'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Mark and sweep stale issues
        uses: actions/stale@v9
        with:
          days-before-issue-stale: 120
          days-before-issue-close: 14
          stale-issue-label: stale
          exempt-issue-labels: 'bug-confirmed,security,roadmap,pinned'
          stale-issue-message: >
            This issue hasn't had activity in 120 days. It'll auto-close in 14 days if nothing changes —
            comment to keep it open, no judgment either way.
          close-issue-message: >
            Closing due to inactivity. If this is still relevant, reopen or file a fresh issue referencing this one.
          days-before-pr-stale: -1
          days-before-pr-close: -1

      - name: Pull open-issue snapshot
        env:
          GH_TOKEN: ${{ github.token }}
        run: |
          gh issue list --state open --limit 400 \
            --json number,title,labels,createdAt,updatedAt,comments > snapshot.json

      - name: Set up Claude Code CLI
        run: npm install -g @anthropic-ai/claude-code

      - name: Draft weekly digest
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          PROMPT="You produce a weekly issue-triage digest for Plimsoll's one active maintainer, alone \
          against a large backlog. Terse, scannable, readable in under 2 minutes. From the JSON snapshot \
          of open issues below, produce Markdown with: (1) total open count and new-vs-closed-this-week \
          signal; (2) the 5 oldest issues by createdAt, number + title; (3) the 5 with the most comments; \
          (4) count still labeled needs-triage; (5) up to 5 issues that look small/well-scoped enough to \
          hand to the Discord community as help-wanted candidates (short clear title, low comment count, \
          category bug or feature-request) — suggest, don't assume anyone will pick them up. Never invent \
          an issue number or title not present in the data. Snapshot:
          $(cat snapshot.json)"
          claude --system-prompt "" --tools "" --setting-sources "" --model sonnet -p "$PROMPT" > digest.md

      - name: Update pinned digest issue
        env:
          GH_TOKEN: ${{ github.token }}
        run: |
          TITLE="📋 Weekly Triage Digest"
          NUM=$(gh issue list --search "in:title \"$TITLE\"" --state open --json number --jq '.[0].number')
          if [ -z "$NUM" ] || [ "$NUM" = "null" ]; then
            URL=$(gh issue create --title "$TITLE" --body-file digest.md --label triage-digest)
            NUM=$(basename "$URL")
            gh issue pin "$NUM" || true
          else
            gh issue comment "$NUM" --body-file digest.md
          fi
```

---

## `.github/workflows/weekly-digest.yml`
The single weekly touchpoint into the 900-person Discord — deliberately one consolidated message, not three separate pings, so it stays worth reading.

```yaml
name: Weekly community digest

on:
  schedule:
    - cron: '0 15 * * 5'   # Friday 15:00 UTC, after issue-triage's morning run — adjust to your TZ
  workflow_dispatch: {}

permissions:
  contents: read
  issues: read

jobs:
  digest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Gather this week's headline numbers
        id: facts
        env:
          GH_TOKEN: ${{ github.token }}
        run: |
          LATEST_TAG=$(gh release list --limit 1 --json tagName,publishedAt --jq '.[0] | "\(.tagName) (\(.publishedAt))"' 2>/dev/null || echo "none")
          OPEN_COUNT=$(gh issue list --state open --limit 1000 --json number --jq 'length')
          NEEDS_TRIAGE=$(gh issue list --state open --label needs-triage --limit 1000 --json number --jq 'length')
          echo "latest_tag=$LATEST_TAG" >> "$GITHUB_OUTPUT"
          echo "open_count=$OPEN_COUNT" >> "$GITHUB_OUTPUT"
          echo "needs_triage=$NEEDS_TRIAGE" >> "$GITHUB_OUTPUT"

      - name: Read urgent CFP targets
        id: cfp
        run: |
          pip install --quiet pyyaml
          python3 - <<'PY' >> "$GITHUB_OUTPUT"
          import yaml, datetime
          try:
              targets = yaml.safe_load(open(".github/cfp-targets.yml")) or []
          except FileNotFoundError:
              targets = []
          today = datetime.date.today()
          urgent = [t["conference"] for t in targets
                    if t.get("status") == "open"
                    and (datetime.date.fromisoformat(str(t["cfp_close"])) - today).days <= 21]
          print(f"urgent={', '.join(urgent) if urgent else 'none'}")
          PY

      - name: Set up Claude Code CLI
        run: npm install -g @anthropic-ai/claude-code

      - name: Compose Discord digest
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          PROMPT="Write a short, friendly weekly update for Plimsoll's ~900-person Discord (#announcements). \
          Max 6 short lines, no fluff, no hashtags, plain language a developer would actually read. Cover, \
          skipping any line with nothing to say: latest release = ${{ steps.facts.outputs.latest_tag }}; \
          open issues = ${{ steps.facts.outputs.open_count }} (${{ steps.facts.outputs.needs_triage }} \
          awaiting first triage); CFPs closing within 3 weeks = ${{ steps.cfp.outputs.urgent }}. End with \
          one line inviting people to grab a help-wanted issue, linking to the issues page filtered by \
          that label. Plain text, no markdown headers."
          claude --system-prompt "" --tools "" --setting-sources "" --model sonnet -p "$PROMPT" > post.txt

      - name: Post to Discord
        env:
          WEBHOOK: ${{ secrets.DISCORD_DIGEST_WEBHOOK_URL }}
        run: |
          BODY=$(jq -n --rawfile msg post.txt '{content: $msg}')
          curl -sS -X POST "$WEBHOOK" -H "Content-Type: application/json" -d "$BODY"
```

---

## Notes on what's deliberately not automated

- **No forced assignment.** The digest surfaces small/scoped issues as suggestions for the Discord community — it never assigns them, since forcing ownership onto reluctant maintainers is exactly what isn't working now.
- **No auto-added CFP entries.** The monthly research pass only comments with candidates; a human adds real ones to `cfp-targets.yml`. Letting an LLM write directly into the deadline source of truth risks a fabricated date costing a real submission.
- **No auto-closing on first pass.** `possible-duplicate` and `stale` both flag, never auto-close, on the first sweep — only the 14-day-after-stale grace period actually closes something, and security/roadmap/pinned issues are exempt.
- **Timezone:** all crons are UTC; comments mark where to shift for Europe/Paris. GitHub Actions schedules don't support named timezones directly.

One low-effort addition worth considering separately (not "recurring automation," so left out here): a structured issue template (bug/feature forms) to cut the `needs-info` loop at intake — happy to draft if useful.