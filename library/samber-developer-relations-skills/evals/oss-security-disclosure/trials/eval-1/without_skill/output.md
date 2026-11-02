# Verdict on your plan

Push the fix today and leave the issue up. Change the advisory timing.

- ⚠️ **Don't publish the advisory tonight.** It would tell everyone about a crash they can't fix yet. The reproducer is already public, so the advisory adds no secrecy, but it does alert people before a patched release exists. Publish it once 1.4.3 is on crates.io.
- ⚠️ **Fix both supported lines.** You support 0.9.x too. Backport the check and release a 0.9.x patch alongside 1.4.3. Otherwise the advisory has to say "0.9.x: no fix".
- ℹ️ **Lena doesn't need to approve.** Send her a short note so she isn't surprised when she lands.
- ℹ️ **Put the real depth limit in the text.** I left `<N>` placeholders for the limit, the affected versions and the 0.9.x patch number. Fill them in before sending.

Sequence:

1. Today: push the fix to `main` and backport it to the 0.9.x branch. Post the issue reply.
2. Tomorrow: CI green, publish 1.4.3 and 0.9.`<Y>`, then yank nothing (older versions stay vulnerable, so only the advisory warns).
3. Right after the release: publish the GitHub advisory and file it with RustSec (`rustsec/advisory-db`).

---

## 1. Commit message

```
fix(parser): reject table nesting deeper than 128 levels

Parsing recursed once per nested table with no limit, so a short
input of deeply nested tables overflowed the stack and aborted the
process. Return a ParseError::NestingTooDeep once depth exceeds
MAX_TABLE_DEPTH (128) instead of recursing further.

The limit is far above any real-world config. Add regression tests
at depth 127, 128 and 129, and for both table and inline-table
nesting.

Fixes #<issue-number>
```

Your original subject, `fix: bounds check in table nesting parser`, is valid but vague. It's the line people will scan in the changelog, so name the behavior.

Before you push, check two things:

- Does inline-table nesting (`a = {b = {c = ...}}`) recurse through the same path? If it doesn't, it needs its own check.
- Does the INI side have the same pattern?

One check covers only one of these paths.

## 2. Advisory text (publish after release)

**Title:** Uncontrolled recursion in `quillparse` TOML parser causes stack overflow (denial of service)

**Severity:** High, CVSS 3.1 `AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H` (7.5). This applies when the application parses untrusted input.
**CWE:** CWE-674 (Uncontrolled Recursion)
**Ecosystem / package:** crates.io / `quillparse`
**Affected versions:** `>= <first-affected>, < 1.4.3` and `>= <first-affected-0.9>, < 0.9.<Y>`
**Patched versions:** `1.4.3`, `0.9.<Y>`

### Summary

`quillparse` parsed nested TOML tables recursively with no depth limit. A small, crafted document with deeply nested tables exhausts the stack, and the process aborts.

### Impact

Any application that parses TOML from an untrusted source can be crashed by a document of a few hundred bytes. Examples are web services accepting user-supplied configuration and CI tools reading third-party manifests.

A Rust stack overflow aborts the process. It can't be caught with `catch_unwind`. There is no memory corruption and no information disclosure. The impact is availability only.

Applications that parse only trusted, self-authored files are not meaningfully affected.

### Patches

Versions 1.4.3 and 0.9.`<Y>` limit table nesting to 128 levels. Deeper input now returns a `NestingTooDeep` parse error instead of overflowing the stack. Upgrade with:

```
cargo update -p quillparse
```

### Workarounds

If you can't upgrade right away:

- Cap the size of untrusted input before parsing.
- Parse on a thread with an enlarged stack. This only raises the threshold; it doesn't remove the problem.
- Pre-scan the input and reject documents with excessive table-header depth.

### Credit

Reported publicly by `@<reporter>` in #<issue-number>. Thank you.

### References

- Issue: #<issue-number>
- Fix: `<commit-sha>` (1.x), `<commit-sha>` (0.9.x)

## 3. Reply to the issue (post today)

> Thanks for the report, and for the minimal sample. It made this easy to confirm.
>
> You're right that this has security implications. The parser recursed per nested table with no depth limit, so deeply nested input overflows the stack and aborts the process. For anyone parsing untrusted TOML, that is a denial of service.
>
> What's happening:
> - A fix is on `main` in `<commit-sha>`. It caps table nesting at 128 levels and returns a parse error beyond that.
> - I'm backporting it to the 0.9.x line, since both lines are affected.
> - Releases (1.4.3 and 0.9.`<Y>`) are planned for tomorrow, once CI is green. I'll publish a security advisory right after, so there is a patched version to point to.
>
> Until then, if you parse untrusted input, cap its size or reject deeply nested table headers before parsing.
>
> I'll update this issue when the releases are out.

Two notes on the reply:

- It doesn't repeat the crashing sample or say "fixed in 1.4.3", since that isn't true yet.
- When the release ships, post a follow-up on the issue linking the advisory, then close it.