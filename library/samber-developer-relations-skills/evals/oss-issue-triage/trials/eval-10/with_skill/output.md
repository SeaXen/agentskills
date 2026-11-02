## Support-question template for quartzpipe

Five fields, in this order. Each one earns its place because its absence forces a round-trip; nothing here is decorative.

```markdown
---
name: Support question
about: Ask how to use quartzpipe — not a bug report or feature request
title: "[Support] "
labels: ["kind/question"]
---

<!--
Check the README and docs first. If you found a page that was close but
didn't answer this, name it below anyway — that's useful even if you skip
the rest.
-->

## What are you trying to do?

<!-- The end goal, not the symptom. "Read a CSV, dedupe rows, write Parquet",
not "this throws an error." -->



## What you've tried

<!-- Paste the actual pipeline/config code you're running. Strip anything
unrelated to the question. -->

```
# your quartzpipe code here
```

## What happened, and what you expected instead



## quartzpipe version

<!-- `quartzpipe --version`, or your lockfile. "Latest" isn't answerable. -->



## Docs already checked

<!-- Which page(s), if any. "None" is a fine answer. -->
```

**Why these five and not more:**

- **Goal first, not the error.** A support question is usually an XY problem — someone describes their attempted workaround, not what they actually want. Asking for the goal before the attempt stops the thread from wasting a reply on the wrong layer.
- **Actual code, not a description of code.** For a data pipeline library, "how do I do X" is unanswerable without seeing the real pipeline/config. This is the same principle as a bug report's minimal reproduction, just framed as "show me," not "reproduce."
- **Expected vs. actual is what tells you it's a question and not a bug.** If the gap turns out to be "quartzpipe is broken," that's your signal to relabel and move it into the bug path — the field does double duty as a routing check.
- **Version as a fixed ask, not free text.** Same reason as your bug template: "latest" costs a round-trip every time.
- **Docs-checked is the field worth having even when the rest is empty.** It filters the fraction that's already answered in the README, and it's a live feed of doc gaps — when the same page keeps getting named as "checked but didn't help," that's a documentation bug, not a support queue problem. Route those into the docs, not into more triage capacity.

No environment/OS field — unlike a bug report, reproducibility rarely hinges on it for a "how do I" question. Adding it back would be exactly the kind of optional field that teaches people the form is skippable.

**One thing worth naming directly, since you already have the failure mode:** a markdown template can't require anything — the reporter can delete the whole body, which is exactly what's happening to your other three. This template doesn't fix that; nothing about markdown does. If the gutting is frequent enough to matter, the fix is switching to a GitHub YAML issue form (`.github/ISSUE_TEMPLATE/*.yml` with `validations: required: true`) — same five fields, but the submit button is disabled until they're filled. That's a bigger lift than "add a fourth markdown file," so I'd only do it if the deletion rate is actually costing you round-trips, not on principle. Keeping this one short (five fields, not more) is the best mitigation available within markdown's limits — the longer a form is, the more attractive it is to gut entirely.

The front-matter `labels: ["kind/question"]` auto-applies the type label on submission, which is the one piece of automation you get for free even without a validated form — no triage minutes spent classifying inflow that already self-identified by which template it came from.