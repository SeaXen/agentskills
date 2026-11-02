**Do not publish "about an hour" yet.** Nobody has measured it, so publish a number only after the cold upgrade run in step 5. I haven't seen the guide, so the checks below are the plan to run on it.

"17 entries, all with code" shows the guide is complete in shape, not that it is correct. A codemod existing does not make it correct either.

## Answer to marketing

- **Today:** put no duration at the top. A wrong estimate makes readers distrust every other number in the guide.
- **After the cold run (step 5):** use measured wording, for example: "Median 45 min across 3 real apps (range 20 min to 3 h). Apps that use X take longer."
- **Check "most apps".** The claim holds only if the test apps look like your real users.
- **Treat the engineer's hour as a hypothesis.** Write it down now, then compare it to the measured time.

## How to check the guide (about 2.5 working days)

Times are my estimates. Order matters because early steps are cheap and catch the most.

1. **Completeness diff (about 3 h).**
   - Diff the public API between the v3 tag and the v4 tag. Use `api-extractor`, `tsc --declaration` output, or similar.
   - Every removed or behavior-changed symbol needs an entry. Do not use the changelog as the inventory.
   - Add anything support or early adopters already saw break. Users depend on undocumented behavior, so the diff alone undercounts.
   - Missing symbols are defects. Fix them before step 2.
2. **Entry audit (about 2 h).** Each of the 17 entries needs all six parts:
   - a verb-prefixed heading with a stable anchor;
   - an "affects you if" line with a search pattern and the exact error or warning text;
   - a rationale of at most 3 sentences;
   - before/after code that can be pasted;
   - one fix, either a codemod command or numbered steps;
   - an escape hatch, or an explicit "none".

   Code in every entry is only part 4. Expect many entries to lack the detection signal and the escape hatch.
3. **Structure audit (about 1 h).**
   - **Order:** entries run by blast radius, not alphabetically or by module. Use telemetry first, then a search of dependent repos, then maintainer estimates.
   - **Floors:** Node, TypeScript and peer-dependency versions come first, as checkable comparisons such as `Node >= 20.19`.
   - **Path:** the guide states the path shape (staged, single hop or compat build) and names any known-bad intermediate version.
   - **Missing sections:** deprecation timeline table, housekeeping (what is now dead), troubleshooting keyed by exact error text, and one canonical URL with stable anchors.
4. **Codemod check (about 1 day).** The check has three parts:
   - Run the jscodeshift codemod on every app you can clone: example apps, internal consumers and public dependents. One repo is not a sample.
   - After each run, typecheck and run the test suite. Review the diff.
   - Write the residue into the guide, next to the command. The usual survivors are dynamic dispatch, re-exports, generated code and string-keyed access.

   Also state which of the 17 entries the codemod covers, and give per-change commands as well as the run-everything command.
5. **Cold upgrade run (about 4 h of wall clock per app, 3 apps).**
   - Pick a small app, a typical app and an awkward one (heavy TypeScript, dynamic usage).
   - Someone who did not write the guide upgrades each app using only the guide, with a timer running.
   - Log every stall, every edit the guide did not describe, and every time they opened the source, the changelog or the issue tracker.
   - Fix the guide and rerun until the pass threshold below holds.
   - Use the elapsed times for the marketing line.
6. **Executable docs in CI (about 0.5 to 1 day).**
   - Compile every snippet in CI so a stale snippet fails the build.
   - This catches broken commands only. It does not catch a wrong narrative, so it does not replace step 5.

## Pass threshold (all six must hold)

1. Every changed or removed public symbol in the diff has an entry.
2. Every entry has a search pattern and the exact error text.
3. The upgrade finishes with no edit the guide omits.
4. Every claimed codemod has been run on the test apps, its residue is named in the guide, and typecheck and tests pass afterwards.
5. If you promise multi-hop jumps such as v2 to v4, the oldest promised version has been run through the full path.
6. The reader never leaves the guide to find out what to do next.

## Open questions

Your answers may change the plan:

- **Telemetry:** do you have usage data on the changed APIs? Without it, blast-radius order is a guess. Say so in the plan.
- **Warnings in v3:** did the last v3 release emit deprecation warnings for these changes? If not, ask whether a warnings-only interim release can still ship. It gives the best return.
- **Codemod owner:** who maintains the codemod after release? With no owner, a codemod that goes stale gives wrong answers. Stay on search patterns and error text instead.
- **Audience:** are the readers open-source users, paying customers or internal teams? The audience changes what goes at the top of the guide: benefits, a deadline, or an ownership map.

## After publish

- **Adoption:** track v4 share of installs at 30, 60 and 90 days. Start the data join before release. Plan the last 15% or so as named accounts to contact directly.
- **Support and search:** count tickets that quote an upgrade error, and watch in-page search for error strings. Both point to the entries to rewrite.

**Next action:** give me the guide path and the codemod repo. I can run steps 1 to 3 as a read-only audit and return a fix list.