# Oakmere: what to publish now for the four 3.4 deprecations

You don't need a 5.0 migration guide yet. 5.0 is two majors away and its breaking set isn't frozen. Publish a **deprecation timeline plus a "What disappears in 5.0" page** now. The version-migration-guide skill calls this the mid-deprecation case. The full guide ships with 4.0 and 5.0, built on this page.

I could not fill in everything from your message. Items in `<ANGLE BRACKETS>` need your answer, and I did not invent them.

## 1. Assumptions and open questions

You are an open-source project and users upgrade whenever they like. So the runway is counted in releases, not dates, and the page has to answer "why bother" before it answers "how".

Answer these, in this order:

1. **What replaces `Session.renew()` and `--legacy-cache`?** You gave replacements only for `timeoutMs` and none for `errCode`. A deprecation without a replacement or an explicit "none" is unfinished. Nobody can act on it, so it will still be in use on removal day.
2. **What does 3.4 do today for each item?** Is it docs-only, or does it emit a runtime warning? If docs-only, nobody has been told yet.
3. **Can 3.x still ship a minor release (3.5)?** If yes, put the runtime warnings there now. Otherwise the four months to 4.0 produce no signal. If no, the first warnings land in 4.0.
4. **What is `errCode` today?** "We stopped exposing it" has two readings:
   - It is still populated but hidden from the types. Then it can warn on read.
   - It is already gone at runtime. Then there is nothing to remove in 5.0, and the honest entry is "already removed in 3.x, with no replacement".
5. **What unit does `Config.timeout` use?** If `timeoutMs` was milliseconds and `timeout` is seconds or a duration object, the rename is a behavior change and a codemod must not rewrite it blindly.
6. **Which wins in 4.x when both `timeout` and `timeoutMs` are set?** I assumed `timeout`, with a warning.
7. **Do you have usage telemetry on these APIs?** For open source the answer is usually no. The substitute is a code search across public dependents, which also gives the blast-radius order below.
8. **Until when do 3.x and 4.x receive security fixes?** Open-source readers need this plainly stated.
9. **Who maintains any codemod after release?** If nobody, the page ships search patterns and exact messages only. A codemod nobody owns rots into a wrong answer.

I assumed JS/TS-style code from the camelCase names. Adapt the snippets to your language.

## 2. Inventory

| Change | Type | Blast radius | Evidence |
|---|---|---|---|
| `Config.timeoutMs` → `Config.timeout` | Rename | Probably highest, since config is touched on every project | **Provisional.** Confirm with a code search for `timeoutMs`. |
| `Session.renew()` | Removal | `<medium>` | **Provisional.** Confirm with a code search for `\.renew\(`. |
| `--legacy-cache` | Removal (CLI flag) | `<medium>`, and hidden because it sits in CI files and scripts | **Provisional.** Confirm with a search of CI files and scripts. |
| `Result.errCode` | Removal, no replacement | `<unknown>`, the highest risk per user because there is no way out | Unknown. Hyrum's Law says somebody depends on it. |

The page order must come from measured counts, not from my guess. Replace the order after the code search.

## 3. Path shape

**Staged.** 3.4 deprecates, 4.0 warns, 5.0 removes. That is Django's rule (deprecated in N, warning in N+1, removed in N+2). 4.0 is your free interim release, so the staged path costs almost nothing.

The reader's advice at 5.0 will be: upgrade to the last 4.x first, because its warnings list every call site you must fix.

Keep these removals out of the 4.0 *breaking* list. In the 4.0 guide they belong under "New deprecations", with 5.0 as the removal version.

## 4. What to publish

### 4a. Ship in 3.5, if 3.x can ship one

- Runtime warnings, application code only. Warnings raised inside dependencies teach people to ignore all warnings.
- A stable ID on each, and the exact text, so search and coding agents can match it.
- Proposed text:

```
DeprecationWarning: [OAK-DEP-0001] Session.renew() is deprecated and will be removed in 5.0. Use <REPLACEMENT>. See https://<docs>/migrate/5.0#removed-session-renew
```

- Use the same shape for `OAK-DEP-0002` to `0004`.
- `errCode` can only warn if it is still populated (open question 4).
- If 3.5 is impossible, ship this in 4.0 and say so on the page.

### 4b. Deprecation timeline table

Publish it at one canonical URL, organized by removal version.

| ID | Deprecated | Replacement | Warning level now (3.4) | Planned warning level | Removed in |
|---|---|---|---|---|---|
| OAK-DEP-0001 | `Session.renew()` | `<REPLACEMENT>` | `<docs-only?>` | Runtime, app code (3.5 or 4.0); runtime, all code in the last 4.x | 5.0 |
| OAK-DEP-0002 | `--legacy-cache` | `<REPLACEMENT or "none: the new cache is always on">` | `<docs-only?>` | Same ladder | 5.0 |
| OAK-DEP-0003 | `Config.timeoutMs` | `Config.timeout` (`<unit note>`) | `<docs-only?>` | Same ladder | 5.0 |
| OAK-DEP-0004 | `Result.errCode` | **None.** No longer exposed | `<see question 4>` | Warn on read only if still populated | 5.0 (or "already removed") |

The "Removed in" column states a version, not a date. If a dated promise turns out to be impossible, say that on the page and don't promise a month.

### 4c. The page "What disappears in 5.0"

Open with two lines on what 5.0 buys the reader, then the runway in releases:

> Four APIs deprecated in 3.4 are removed in 5.0. 4.0 (expected `<month>`, no commitment) warns at every use. Upgrade to the last 4.x before 5.0 and your warning output is your to-do list. 3.x receives security fixes until `<date or release>`.

Use one block per change, in this order and with the stable anchors shown. The order is provisional until the code search is done. Each block has the six parts the skill requires: verb heading with anchor, affected-if line, what and why in three sentences or fewer, before/after, fix, escape hatch.

````markdown
### Renamed: `Config.timeoutMs` is now `Config.timeout` {#renamed-config-timeout-ms}

**Affects you if** your config sets `timeoutMs`. Search: `timeoutMs` (also check
JSON/YAML/env config files and string-keyed access like `config["timeoutMs"]`).
At runtime on 4.x you will see:

    DeprecationWarning: [OAK-DEP-0003] Config.timeoutMs is deprecated ...

`<One to three sentences on why: for example, one name for one setting, and the unit
is now explicit.>` Confirm before publishing: `timeout` is `<ms | seconds | duration>`,
and `timeout` wins if both are set.

```js
// Before (3.4)
const config = { timeoutMs: 5000 };

// After (4.x and 5.0)
const config = { timeout: 5000 }; // <adjust if the unit differs>
```

**Fix:** rename the key, then run your tests. `<If a codemod exists: exact command,
residue named: dynamic keys and config loaded from files survive.>`
Otherwise write "No codemod exists; the search above finds every site."

**Escape hatch:** none. `timeoutMs` stops being read in 5.0. 4.x still accepts it with a warning.

### Removed: `Session.renew()` {#removed-session-renew}

**Affects you if** you call `renew()` on a `Session`. Search: `\.renew\(`
(this also matches unrelated `renew` methods, so check the receiver type).
Warning: `DeprecationWarning: [OAK-DEP-0001] ...`

`<Why, three sentences max.>`

```js
// Before (3.4)
await session.renew();

// After
<REPLACEMENT>
```

**Fix:** `<numbered manual steps or codemod command + residue>`
**Escape hatch:** none after 5.0. `<If 4.x keeps a flag, name it.>`

### Removed: the `--legacy-cache` flag {#removed-legacy-cache-flag}

**Affects you if** any script, CI file, Dockerfile, Makefile or docs passes
`--legacy-cache`. Search: `--legacy-cache` in all of those, not only source files.
Runtime message in 4.x: `<exact stderr text>`

`<Why.>`

```sh
# Before (3.4)
oakmere build --legacy-cache

# After
oakmere build   # <or the replacement flag>
```

**Fix:** delete the flag. `<State what the default does instead.>`
**Escape hatch:** none after 5.0. `<Say so, with the last release that has it.>`

### Removed: `Result.errCode`, with no replacement {#removed-result-err-code}

**Affects you if** your code reads `result.errCode`. Search: `errCode`.
`<Runtime message if it is still populated; otherwise: "it is already undefined
since 3.x".>`

We stopped exposing `errCode` because `<real reason, three sentences max>`.
There is no direct replacement.

```js
// Before (3.4)
if (result.errCode === "E_TIMEOUT") retry();

// After: no equivalent field. <If you can, show what the reader should
// branch on instead, such as the error type or message. If nothing is
// reliable, write that.>
```

**Fix:** remove the dependency on the field, or branch on `<…>`.
**Escape hatch:** none. If you rely on it, tell us what for in `<issue link>`.
That feedback is the only evidence you have for what depends on it.
````

Rules that apply to all four:

- Quote the warning strings exactly, with punctuation.
- Keep the anchors permanent. Lint rules and support replies will link to them.
- Where `<…>` appears, delete the line or fill it in. Never publish a placeholder.
- Don't add an FAQ, a "what's new" section or a rationale essay. That is the anti-pattern outline.

### 4d. Search patterns (the cheapest automation)

These cost almost nothing and are what a coding agent needs to do the work unattended:

```
timeoutMs
\.renew\(
--legacy-cache
errCode
```

Say plainly on the page that no codemod or lint rule exists, unless one does. Readers who assume one exists lose an hour looking for it. If a lint rule is cheap, add it later. It is about a day of work and it stops the old API creeping back after the migration.

## 5. Verification

Before publishing, **run the four search patterns against a real project on 3.4**. Use an example app or a community project, with someone who didn't write the page at the keyboard. Confirm:

- Every hit is covered by an entry.
- Every entry's "after" compiles and passes the tests.
- No undocumented edit was needed.

Don't publish a time estimate you haven't measured.

Re-run this cold check at 4.0 against the real warning output, and again at 5.0 with the oldest promised starting version.

## 6. KPIs, in order of cost

1. **Tickets quoting these warnings**, and which ID generates the most. Free. That entry is the one to rewrite.
2. **Code search counts of public dependents** still using each pattern, now and monthly. This stands in for telemetry. The count should fall before 5.0. If it is flat a month out, the date is wrong or the page isn't reaching people.
3. **Guide behavior**: in-page search for `errCode` and the warning IDs, and exits to your support channel. Both signal a missing entry.
4. **Adoption of 4.x** at 30, 60 and 90 days. This needs a download-by-version join and is the metric that says the migration worked. Start the join before 4.0 ships. Plan the last ~15% as named dependents to contact directly, not as a docs problem.

Don't start hard enforcement (brownouts, early removal) until the dependents count visibly flattens. Transitions like this take years, not months.

## What I did not do

I did not write the full 5.0 migration guide, because its breaking set isn't frozen. I did not invent replacements for `renew()` or `--legacy-cache`. I did not invent the `timeout` unit. I did not run any search against your repo, since I had no access to it.