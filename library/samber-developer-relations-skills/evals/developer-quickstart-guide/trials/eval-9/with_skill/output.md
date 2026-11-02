**Automated check for Palisade's quickstart**

Both breaks (config-key rename, upstream default change) share one root cause: nothing executed the quickstart against the real published artifact after each change. Fix per the skill's CI-regression-job pattern — add two jobs, not one, since the two incidents need different triggers.

1. **Annotate the command blocks.** Tag each copy-paste block in the quickstart source (e.g. a fenced-code attribute `quickstart-exec`) so an extractor script can pull and run them verbatim — no hand-copied duplicate that drifts from the real page.
2. **Pre-release gate (catches the config-key rename).** Add a required check to Palisade's own release pipeline: before a minor/patch version publishes, spin up a clean container, install the release-candidate build, run the extracted commands, diff output against the documented output (normalize IDs/timestamps with patterns, not deletion). Release blocks on failure. This is a rename *you* control — catch it before publish, not after a customer hits it.
3. **Faster signal for the same case: a schema-diff PR check.** Any PR touching config parsing gets a bot comment/fail if a config key referenced in the quickstart no longer exists in the SDK's schema. Fires at PR time, before merge — cheaper than waiting for the full cold-run job.
4. **Scheduled drift job (catches the upstream default change).** Run the same extracted commands nightly, resolving dependencies fresh (not from a lockfile) against the currently published Palisade version. An upstream package publishing a new default breaks this run the same day, with no commit on your side — exactly the case a release-gate job can't see.
5. **Throwaway credentials per run**, both jobs — no shared state leaking between runs.
6. **Assert the five pass-threshold criteria**, not just exit code: command ran unedited, output matched, no prerequisite appeared mid-run, elapsed time inside the 10-minute SDK budget, and the fail branch text still points at a real error.
7. **On failure, fail the build / page someone — never file-and-forget a ticket.** A stale quickstart that still looks green cost you both incidents; loud failure is the whole point.

**Ownership**

One writer drafting every page and running 3 weeks behind is the same root cause as the two breaks: the person writing the page is never the person who knows the command or output changed. Fix the model, not the backlog:

1. **Move the quickstart into the SDK's own repo and PR workflow** (docs-as-code). It stops being a separate deliverable someone queues behind other writing.
2. **Shipping engineer writes the first draft**, at merge time, on the same PR that changes the behavior — they're the only one who currently knows the real command and real output.
3. **Writer reviews, doesn't author.** Review is faster than drafting from scratch, and N engineers can draft in parallel instead of serializing through one person — this is what actually clears the 3-week backlog, not asking her to work faster.
4. **Split final authority explicitly**, don't leave it ambiguous: writer has final say on voice/structure/consistency; engineer has final say on technical accuracy (commands, output, config keys); CI (above) has final say on whether it merges at all — nothing ships if the cold-run job fails, regardless of who signed off.
5. **Make the merge gate literal**: the PR that renames a config key is required to update the quickstart's config-key references before merge (the schema-diff check from above enforces this automatically — same mechanism, now doubling as the ownership handoff trigger).

Next: pick which repo becomes the source of truth for Palisade's quickstart, so the extractor script and the two CI jobs have somewhere to live.