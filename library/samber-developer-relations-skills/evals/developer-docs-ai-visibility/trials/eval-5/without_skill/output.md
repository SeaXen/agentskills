**Do first:** put `run_sync` into a removed-symbols file in the docs repo (step 1 below). Everything else hangs off that file.

**Date check:** today is 2026-10-30, so end-of-support on Nov 18 is 19 days away, not 3.5 weeks. The plan assumes 19 days, which gives your writer three days in total (about Nov 5, 12 and 18). If the date is later, the plan still works with more slack.

**Constraints that shape the plan**
- The SDK team gives you no slot, so you get no interim warnings release, no codemod and no SDK-side deprecation. The migration is a single hop.
- You own the templates and the build, and that is your strongest lever. It needs nobody else's release train.
- Most of the work should be engineering in the docs build. Your writer then has only prose to write.

## Levers, ranked by payoff per hour

**1. Removed-symbols file plus a build gate (about 1 day of your time). This is also the standing practice.**
- Create `removed-symbols.yml`. Each entry has the v1 symbol, the v2 replacement, the exact error text a v2 user sees, the version that removed it, and a stable anchor ID.
- Start with `Flow.run_sync()` → `Flow.run()`.
- Run `python -c "import tessaline; tessaline.Flow.run_sync"` on v2 once, to capture the real error string. Don't guess it.
- Add a build step that fails if any current-version page or snippet uses a listed symbol.
- Generate three things from the same file: the migration page entries, the grep patterns, and the troubleshooting index.
- From then on, the only per-release work is adding rows to this file.
- For leadership, "standing practice" then means one rule: no major release ships without its removed-symbols rows. Ask for that as a release-checklist item. It is not a train slot, so the SDK team only reviews rows, about 30 minutes async.

**2. Stop the `run_sync` bleed (about 0.5 day, by your writer or a Discord mod).**
- Add a Discord bot or mod auto-reply on the keyword `run_sync` that links to the generated troubleshooting entry.
- Pin one message in the help channel.
- Search your own docs for stale `run_sync` snippets with `/usr/bin/grep -rE`, and for old pages that search engines still index.
- Test whether the canonical tags on v1 pages point at v2. Fix this in the template.
- Do this before the migration guide is finished. It is the fastest visible win.

**3. Template changes (about 0.5 day of your time).**
- Add a version-aware banner on every v1 page: "v1 support ends Nov 18", with a link to the guide and the date.
- Add a version switcher that preserves the page path.
- Add a deprecation timeline table (what ends when) to the v1 landing page.
- Template changes cost the SDK team nothing, and they reach everyone who reads the docs.

**4. Migration guide, single hop (writer, days 1–2).**
- Order the entries by blast radius, not alphabetically.
- Give each entry the same six parts: verb heading with anchor, "affected if" with the grep pattern and the literal error, why in at most 3 sentences, before/after code, fix, and escape hatch (or an explicit "none").
- Put the floors first (Python version, dependency minimums).
- End with a housekeeping section covering workarounds that are now dead.
- Rank blast radius from three sources:
  1. Discord paste counts.
  2. Docs search logs and support tickets.
  3. Server-side v1 API usage, by workspace. The 30% figure suggests someone already has this, and server-side logs need no SDK change.
- Write only the top 8–10 entries by blast radius, not the full diff. Publish a visible "more entries coming" line for the rest.

**5. Verify with a cold run (writer, day 3).**
- Take one real v1 example app.
- Have someone who did not write the guide upgrade it using only the guide.
- Fix every undocumented edit, then publish the measured time. Don't publish an estimate you haven't measured.

**6. Stragglers: hand to someone else (0 docs hours).**
- Export the list of v1 workspaces by usage.
- Give it to success or support as named accounts, with the guide link and the date.
- Docs can't move the last ~15% of the tail. Plan for a long tail after Nov 18.
- Ask leadership now whether Nov 18 is a hard cut or a soft one. Docs can't decide that.

## Schedule

| When | Who | What |
|---|---|---|
| Oct 30–Nov 4 | You | Step 1 file with `run_sync`, step 2 bot and pin, step 3 banner |
| Nov 5 (writer day 1) | Writer | Top 5 guide entries from the file, troubleshooting page |
| Nov 6–11 | You | Build gate on, switcher, timeline table, pull telemetry |
| Nov 12 (writer day 2) | Writer | Remaining entries, floors, housekeeping |
| Nov 13–17 | SDK team, async | Review rows, about 30 minutes |
| Nov 18 (writer day 3) | Writer | Cold run, publish, post in Discord |

## Do not do
- Don't promise a codemod or a compat build. You have no owner for either.
- Don't write the full inventory by hand. The file generates it.
- Don't make the guide the gate. The build gate is the gate.

## Questions for you (answer in one line each)
1. Do you have server-side v1 usage by workspace, or only the 30% total?
2. Is Nov 18 a hard cut or a soft one?
3. Can a Discord mod set up the keyword auto-reply this week?

**Next action:** run `Flow.run_sync` on v2, copy the exact error, and create `removed-symbols.yml` with that one row. About 20 minutes.