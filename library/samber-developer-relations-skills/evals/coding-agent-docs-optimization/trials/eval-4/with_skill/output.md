## Verdict

Not sound. Two structural choices will invalidate the measurement itself, two of your three tasks are the skill's own documented anti-patterns, and the task set is too small and too narrowly scored to trust an eventual percentage.

## What breaks the measurement

**1. One long session for all eight tasks.** The cold-run protocol is explicit: never run several tasks in one session — "knowledge leaks between them and inflates every score after the first." What you're calling a feature ("keeps context about OAuth") is exactly the leak. Once the agent works out your refresh flow on task 2, that knowledge carries free into every later task that touches auth, and you can no longer tell whether a pass came from your docs or from earlier trial-and-error. A real developer's agent starts every new task cold. Fix: fresh context per task — parallel sub-agents if your tooling supports it, separate sequential sessions if not.

**2. Full web access, including GitHub issues and Stack Overflow.** Run rule #2: restrict sources to published agent-facing surfaces; if the agent needs something you didn't publish, that absence *is* the finding — you let it fail, you don't let it route around the gap. If your OAuth refresh quirk is only explained correctly in a two-year-old GitHub issue, giving the agent web access means it passes task 2 by reading your issue tracker, and you report "docs work" when they don't. You'd be scoring the internet's ability to compensate for your docs, not your docs. Fix: restrict the graded run to your published docs, spec, and SDK. If you want to know what SO/GitHub threads reveal, run that separately and turn any real answer found there into a findings-list item ("this is only documented in issue #482 — promote it to the troubleshooting page").

## Task quality

**Task 1 fails the "hands over the surface" test.** The skill flags this exact shape as weak: *"Call `client.webhooks.constructEvent`" — the task hands over the surface the agent was supposed to discover.* Naming `meridian.shipments.track()` does the same thing — you're testing whether the agent can execute a given call, not whether it can find the right one from your docs. Rewrite as an outcome: "Look up the current status of shipment tracking number `MF-...` and print it." Let the agent discover the method itself; that's the actual failure mode you're trying to catch.

**Task 2 fails the "no verifiable end state" test.** Also called out verbatim: *"Explain how authentication works — no runnable end state, so nothing can fail."* Prose can't be graded pass/fail. Rewrite as something with a checkable outcome: "Write a script that authenticates via OAuth, makes an API call, and automatically refreshes the token on expiry without manual intervention." Verify by forcing a token to expire and checking the retry succeeds unattended.

**Task 3 is correct as written** — it's the protocol's own worked example, verbatim. Keep it, but pin down the verifiable end state before you run it: valid signature accepted, tampered payload or bad signature rejected with the right error path.

## Task set size and sourcing

Three tasks isn't enough — the protocol wants five to ten, composed from three sources: the two or three integrations that drive adoption, your top-traffic doc pages, and known-painful areas (webhook verification, pagination, auth refresh, retries, anything support answers weekly). You have one of each of the first and third categories and nothing from top-traffic pages. For a logistics API, obvious gaps: paginate all shipments created in the last 30 days to CSV, handle a 429 on the tracking endpoint with backoff, create a shipment end-to-end, handle a duplicate/retried webhook idempotently, map a specific error string (invalid tracking number, expired credentials) to its documented fix.

## What you're not measuring

Pass/fail percentage alone is explicitly called out as insufficient — "success rate alone hides a corpus that works only after six expensive retries." Track all five metrics per task: first-attempt success, invented-surface rate, corrective turns per task, context cost per task, fetch-path length. Two of your exit criteria depend on metrics you're not collecting at all — zero invented API surface on your top three tasks, and no more than three documents fetched for a routine task. Also stamp every score with the model identifier and the date; a score only means something within one model generation.

## Missing step before any of this

Verify the agent's user-agent can actually fetch your docs — status codes, from outside your network — before grading content at all. A CDN blocking AI crawlers by default fails every task silently and looks identical to bad documentation in your results.

## Other misses

- Freeze the task set once written. Don't touch it between baseline and re-run or the delta means nothing.
- Capture full transcripts, not just pass/fail — the corrective turns are the data you'll actually fix from.
- Log any intervention you make (e.g. handing over a sandbox credential) separately from a documentation failure.
- Don't re-grade a task in a session that already solved it earlier in the same run.
- 80% first-attempt unattended is the calibrated *stretch* target from published benchmarks, not a floor — don't let the team read your first number against that as a minimum.

## Corrected shape

- One agent, one task, fresh context, no carryover — parallel if you can, sequential if you can't.
- Sources restricted to published docs/spec/SDK for the graded run; web access only in a separate, clearly-labeled exploratory pass.
- 6-8 tasks: fix tasks 1-2 as above, keep task 3, add pagination, backoff/retry, and one error-mapping task.
- Record all five metrics + model + date per task, not just pass/fail.
- Check crawler access first.
- Report against the skeleton in `references/cold-run-protocol.md` (baseline, surface inventory, findings ranked by fixes-per-hour, fix plan, re-run delta) rather than a single percentage to the team.