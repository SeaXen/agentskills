# v6 migration tooling plan: what to build with 3 engineer-weeks

**Next action (2 min):** Name one person who owns the v6 guide page, and the v5 security-fix end date, after the rotation. Without a name, everything below stays cut.

## 1. Assumptions and open questions

The interview was not run, so these are assumptions. Each one changes the plan if wrong.

1. **Churn Rule side:** the consumers are other people's codebases, so a guide is the right deliverable. If Rossiter also runs internal services on this SDK, migrate those yourselves. They become the test corpus in step 5 of the plan below.
2. **Breaking set:** frozen at 23 changes. If it is still moving, the inventory step grows.
3. **Hyrum's Law:** the 23 changes are the documented contract. Support tickets will find more, so add anything support has already seen break.
4. **Can v5 still ship a release?** I assume yes. If a release date inside the window rules out an interim v5.x release, switch to single hop (see section 3).
5. **Telemetry:** I assume none on deprecated APIs. The fallback is PyPI downloads by version, dependent-repo search and support tickets.
6. **Audience:** I assume open-source or self-serve users. If they are paying customers on a notice window, lead the guide with the deadline, add a support path and a rollback story, and get legal/comms sign-off.
7. **Open question for you:** is the compat flag meant to keep the old auth behaviour? A flag that keeps insecure auth defaults alive is a liability. Say so in the plan.

## 2. Inventory table: fill this first

| Change | Type | Blast radius | Evidence |
|---|---|---|---|
| (23 rows: client and auth) | removal / rename or signature / behavior or default / floor / wire format | rank by readers hit | telemetry, then dependent-repo search, then maintainer estimate |

- Source the rows from the public-API diff between the v5 and v6 tags, not the changelog. `griffe check` does this for Python.
- Add rows from `Removed`/`Changed` changelog entries, example-app migration commits and early-adopter tickets.
- Guide order is blast radius, never per-module and never alphabetical. Auth changes with the biggest blast radius go first, even though they are a separate module.
- If several changes share one cause (for example a config or import move), write one entry per fix, not per symbol.

## 3. Recommendation: do not build the codemod or the compat shim

Rung ranking by reader hours saved per engineering hour:

`search patterns + literal messages > deprecation warnings in N-1 > lint rule > codemod > compat build`

The team's two picks are the bottom two rungs. They are also the two that need a standing owner. The skill says: no named owner after release means delete the compat build and the codemod before costing them.

- **Compat shim:** it keeps v5 behaviour alive, so it needs a standing job of dual code paths and flags. Nobody holds it after the rotation. Every project that adopts it ends up half-migrated on an unmaintained path. Delete it.
- **libcst codemod:** a week to build, plus corpus validation, plus a rewrite every time the API moves. With no owner it rots into a wrong answer, and it discredits the whole guide. Delete it.
- **Revisit the codemod only if one of these becomes true.**
  - A named owner appears.
  - Telemetry shows hundreds of call sites per consumer.
  - Most of the 23 changes turn out to be mechanical renames.

  Even then, build it after rungs 1 and 2 are done. Then scope it to the top mechanical renames, and run it across a corpus.

**Path shape: staged.**
1. Ship an interim v5.x release that is identical to the previous v5.x apart from warnings for every v6 change.
2. Readers upgrade to that release first. Their own test output becomes their personal inventory.
3. Then they jump to v6.

If a v5.x release cannot ship, use single hop and move that time to the guide and the cold run.

**What replaces the codemod:** each entry's search pattern plus the exact message text. A coding agent can run the guide unattended with those two things, and they need no maintenance.

## 4. The 3 weeks (15 days)

| Days | Work | Output |
|---|---|---|
| 2 | Inventory and blast-radius ranking | Table in section 2, filled, with evidence source per row |
| 4 | Interim v5.x warnings release | One warning per change, each with a stable ID, linked to the guide anchor |
| 3 | Guide entries | 23 six-part entries with search pattern, literal message, before/after, fix, escape hatch |
| 2 | Guide frame | Floors, path shape, timeline table, housekeeping, troubleshooting by error text |
| 2 | Cold upgrade run, then fixes | Measured elapsed time, defect list closed |
| 1 | Adoption join before release | Version-by-install or account baseline, started before v6 ships |

Warning implementation notes for Python:
- Use a dedicated `RossiterDeprecationWarning` subclass of `DeprecationWarning`, so readers can filter or escalate it by name.
- `DeprecationWarning` is hidden by default outside `__main__` and test runners. Tell readers to run their tests with `-W error::rossiter.RossiterDeprecationWarning`.
- Use `stacklevel=2` so the warning points at the reader's call site, not at your SDK.
- Warning level: application code only, escalating to all code just before removal.

## 5. The guide skeleton

Outline: library/SDK, in this order.

1. Scope and expected effort. Publish the measured cold-run time and nothing else.
2. Before you start. State the staged path and name any known-bad v5.x hop.
3. Requirements, as machine-checkable floors: `Python >= X.Y`, peer dependencies, v5.x interim version.
4. Install, pinned, for every package manager.
5. Automation and its boundary. State plainly: "There is no codemod. Use the search patterns and warning text in each entry."
6. Breaking changes: 23 entries, ordered by blast radius.
7. New deprecations, with the timeline table below.
8. Behavior changes. Nothing breaks, but defaults or output differ.
9. Housekeeping: config that became a default, workaround flags, pins and patches that are now dead.
10. Troubleshooting keyed by the literal error string.

Entry format, shown with a placeholder. Fill the real symbols from the API diff.

````markdown
### Removed: <symbol> {#removed-<stable-slug>}

**Affects you if** you call `<symbol>`. Search: `<regex>`.
v5.x warning / v6 error text: `<exact string, punctuation included>`

<Max 3 sentences: what changed, and the harm the old behaviour caused.>

```python
# Before (v5)
...
# After (v6)
...
```

**Fix:** numbered manual steps.

**Escape hatch:** none. v5 receives security fixes until <date>.
````

Timeline table (one per major, sorted by removal version):

| Deprecated API | Replacement | Warning level in v5.x | Removed in |
|---|---|---|---|
| (one row per change) | replacement, or an explicit "none" | documentation-only, application-code or all-code | v6.0 |

A row with no replacement is an unfinished deprecation.

Auth entries with a security motive:
- Say "escape hatch: none" and give the v5 security-fix end date.
- Do not restore an insecure default behind a flag.

## 6. Verification plan

1. **Who:** someone who did not write the guide, such as a support engineer or a design-partner customer.
2. **What:** a real project on v5. Upgrade it using only the guide, with the interim release first.
3. **Run it on at least two projects.** Use the internal consumers if you have any.
4. **Pass threshold (all six):**
   - Every removed or behavior-changed public symbol in the tag diff has an entry.
   - Every entry has a search pattern and the exact message text.
   - The upgrade completes with no edit the guide does not describe.
   - No automation is claimed that was not run. The guide states there is no codemod.
   - Any multi-hop path promised has had its oldest version run.
   - The reader never opens source, the changelog or the tracker.
5. **Measure:** elapsed time of the run. Publish that number or none.
6. **CI:** run the guide's snippets with `pytest --doctest-modules` where possible, so a stale snippet fails the build.

## 7. KPIs, in wiring order

1. Tickets per thousand upgrades that quote an upgrade error, and which change causes most. Support already collects these.
2. Deprecation-warning counts trending to zero before removal. Do this only if you already have SDK or install telemetry. Otherwise skip it.
3. Guide behavior: in-page search for error strings, and exits to support.
4. Adoption curve at 30/60/90 days, against v5's own curve. Start the join before release, or the first 90 days cannot be measured.
5. Stragglers: named accounts still on v5 after the deadline. Plan the last ~15% as named-account work, not docs work.

KPIs 4 and 5 are a standing job after the rotation. Give them to support or success by name, or accept they will not exist.

## 8. Needed after the rotation

Three things need an owner after the team moves to streaming. All three are cheap.

1. The canonical guide URL and its stable anchors. Do not rewrite it in place.
2. The v5 security-fix end date.
3. A section in the PR or design-doc template that requires a migration entry for every breaking change. This makes future breaks produce guide entries automatically, with no standing tooling.

**Next:** send me the 23-change list, or the v5 and v6 tags. I will fill the section 2 table and draft the top entries.