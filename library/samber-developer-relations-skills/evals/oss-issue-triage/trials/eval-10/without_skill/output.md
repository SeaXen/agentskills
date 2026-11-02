# Support question template

Three fields carry the whole thing; everything else is decoration that gets deleted along with the rest of the template. Design goal: since this is your only support channel and users already strip template contents, each field has to earn its place by directly shortening the back-and-forth that follows a bare "it doesn't work" issue.

```markdown
---
name: Support question
about: Ask how to do something with quartzpipe
title: "[Question] "
labels: question
---

<!-- Search open/closed issues and the README first — most "how do I" questions are already answered there. -->

## What are you trying to do?
The actual goal, not just the symptom (e.g. "stream JSON from S3 into a dedup'd sink" — not "this errors").

## What have you tried?
Paste the relevant code/config and the command you ran.

## What happens vs. what you expected

## Environment
- quartzpipe version:
- Language/runtime version:
```

**Why these four, and nothing more:**

- **Goal, not symptom** — support questions are frequently XY problems ("how do I force a flush" when the real need is "how do I not lose data on crash"). Asking for the goal up front saves a full round-trip.
- **What you've tried** — the single highest-leverage field. Without a code/config snippet, every question becomes "can you share your config?" as a first reply. With it, you can often answer in one pass.
- **Current vs. expected** — kept to one line each on purpose. This isn't a bug-report repro section; don't duplicate that template's structure here or people will bail out at the sight of it.
- **Version** — cheap to fill, and "upgrade to vX" resolves a chunk of these outright. Runtime/OS only, skip anything heavier (stack traces, logs) — that's bug-report territory, not support.

**Two structural moves that matter more than the fields themselves:**

- `title:` and `labels: question` in the frontmatter survive even when someone nukes the whole body. That's the actual fix for "people delete the contents" — the metadata auto-applies regardless, so at minimum you get correct triage and a searchable title prefix even from a blank submission.
- The search-first HTML comment is a maintainer-time investment, not a user-facing field: at 10% of volume with no forum, your issue tracker *is* the FAQ. Pointing people at closed issues before they open a new one is the closest thing you get to deflection without building a channel you don't want.

One thing worth knowing even though you're staying with markdown: GitHub's alternative, YAML issue forms (`.github/ISSUE_TEMPLATE/*.yml`), support `required: true` per field — submission is blocked, not just discouraged, if a field is empty. That's a structural fix for the exact problem you described, where markdown templates can't stop someone from deleting everything. Worth a second look if the deletion rate stays high after this change; not a reason to hold off shipping the markdown version now.