# Answer: don't run your plan as written. The sample is already public, so this is the fast track.

Your plan has three steps that each open a window, and it leaves 0.9.x unfixed. Below is the corrected plan, then the three things you asked for.

## What changes in your plan

| Your plan | Problem | Do instead |
|---|---|---|
| Push the fix to main today | The diff is the disclosure. A one-line depth check is trivial to reverse-engineer. | Keep the fix local, unpushed. Push `main` and the tag in one go, only when you are ready to publish (step 5). |
| Commit `fix: bounds check in table nesting parser` | It names the bug class and the component. | Use the generic message below. |
| Advisory tonight, release tomorrow | The advisory is public the moment you publish it. A night with no patched version is the worst window you can create. | Publish the advisory only after the fixed versions are on crates.io. |
| Release 1.4.3 only | 0.9.x is a supported line. A line patched later is a line disclosed early. | Release a 0.9.x patch in the same window. |
| Wait for CI | Not needed for a crate publish, and it adds hours with a public repro in the wild. | Run the full tests locally on both lines and run `cargo publish --dry-run`. |
| "Leave the issue up, it's public anyway" | Only what the reporter posted is public. Keep your analysis and the fix private. | Remove the sample from the issue (see the reply below) and say nothing more in public. |

**Today is Friday.** The usual advice is to avoid Friday evenings. With a public repro, I'd still ship today during working hours. If you can't finish by about 17:00, tell me and we'll weigh the weekend risk against leaving the window open.

## Steps, in order

1. ⏳ **Now (about 10 min):** post the issue reply below. Open a private advisory draft in the repo's Security tab. **Request a CVE** through GitHub's CNA on the draft today. The release won't wait for it.
2. **Now:** send Lena the short note below. Don't wait for her. You can release alone, and her review can happen afterward.
3. **Fix, locally, on a branch you don't push:**
   - Apply the depth check on `main` (1.x).
   - Backport it to the 0.9.x branch.
   - Add the regression test in the same commit. The trigger is already public, so deferring the test gains nothing.
   - Check whether any other recursive path (arrays, inline tables, INI sections) has the same flaw.
   - Run the full test suite on both lines.
4. **Ask the reporter** (in the private advisory, step 1) to confirm the fix closes it. Don't hold the release for the answer past your cutoff.
5. **Release, in this exact order:**
   1. Merge to `main` and to the 0.9 branch.
   2. Tag both.
   3. **`git push` main, the 0.9 branch and the tags.**
   4. **`cargo publish` 1.4.3**, then the 0.9.x patch.
   5. Confirm both install from the registry.
   6. **Publish the advisory** with both fixed ranges and the credits.
   7. Publish the release notes and a short announcement.
6. **After the advisory:** open a RustSec advisory PR. Don't yank the vulnerable versions. Yanking breaks existing lockfiles and doesn't help the people already on them.

## 1. Commit message

Use the same message on both lines.

```
fix: improve parser robustness on malformed input

Harden the parser against pathological input. Adds a regression test.
```

- Don't name the component, the check or the bug class in the commit, the PR title, the branch name or the PR body.
- Use a branch name like `fix/parser-hardening`.
- Don't link the issue with `Fixes #…` in the commit. Close it by hand after the advisory is out.

## 2. Advisory text (private draft, publish at step 5.6)

**Title:** Uncontrolled recursion (stack exhaustion) when parsing deeply nested tables

**Summary:** An application that parses untrusted TOML with `quillparse` can be crashed by a small crafted document. The process aborts with a stack overflow.

**Affected / patched**

| Line | Affected | Patched |
|---|---|---|
| 1.x | `>= <<first affected 1.x, unknown until checked>>, < 1.4.3` | 1.4.3 |
| 0.9.x | `>= <<first affected 0.9.x, unknown until checked>>, < <<late: 0.9.N>>` | `<<late: 0.9.N>>` |

Mark any version you did not test as "unknown", not "safe". Don't write a single `< 1.4.3` range. It would flag the patched 0.9.x release as vulnerable.

**Affected functions:** `<<list the exported parse entry points that reach the table parser, e.g. quillparse::from_str / parse>>`. The TOML and INI parsers share code. Say explicitly whether INI is affected, once you've checked.

**Description:** The table parser recurses once per nesting level and had no depth limit. A document with deeply nested tables exhausts the thread's stack. In Rust, stack exhaustion aborts the whole process. It is not a panic, so `catch_unwind` cannot recover from it. The impact is availability only. The affected path has no memory corruption (`<<confirm: no unsafe on this path>>`). Any application that passes untrusted input to the parse functions is exposed, whatever the input size limit. The fix adds a nesting limit and returns a parse error when the limit is exceeded.

**Workarounds:** None that fully mitigates. Upgrade. Capping the input size before parsing and parsing on a thread with a larger stack both reduce exposure, but neither removes the flaw.

**Severity:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H → 7.5 High.
- Precondition: the application passes untrusted input to the parser. Most real integrations gate this behind a login or an upload, so the practical exposure varies.
- Scope is Unchanged: the crash stays within the vulnerable process.
- Add a CVSS 4.0 vector if the form accepts one.

**CWE:** CWE-674 (Uncontrolled Recursion)

**Credits:** Reporter: `<<handle the reporter chooses, ask first>>`. Remediation developer: you.

**References:** the 1.4.3 and 0.9.x releases and fix commits. No proof of concept. The reporter's public sample is theirs, not yours to link.

**Publication notice** (release notes, README/announcement channel):

```
quillparse 1.4.3 and 0.9.<<late: N>> fix a high-severity denial of service
(uncontrolled recursion) when parsing deeply nested tables
(<<late: CVE or GHSA id>>, <<late: advisory link>>). Users of earlier 1.x and 0.9.x
releases should upgrade. No complete workaround; capping input size reduces
exposure. Thanks to <<reporter>> for reporting it.
```

## 3. Reply to the public issue

Post this and edit the issue body at the same time. Maintainers with write access can edit it. Edit history stays visible, so also ask the reporter to delete the sample. Then lock the issue, so it collects no further detail.

```
Thanks for the report. We're treating this as security-relevant.

To keep users safe until a fix is out, could you please remove the TOML sample
from the issue description (and any comments), and avoid adding more detail here?
We have opened a private security advisory and will invite you to it so you can
confirm the fix before release. If the invite doesn't reach you, you can report
privately via the repository's Security tab.

We plan to release patched versions for the supported lines today and will publish
full details and credit afterwards. We'll update this issue then.
```

Notes:
- Don't confirm any root cause, the fix shape or "it's one line" in public.
- Don't link the commit or the PR.
- Ask the reporter how they'd like to be credited (name, handle or anonymous) and their time zone, in the private advisory.

## Note to Lena (email, not chat or an issue)

```
Subject: Security report received - details in the private advisory only

A report reached me today through a public issue. I've opened a private advisory
draft and added you. Please read it there and don't discuss it in chat, issues, PRs,
commit messages or branch names.
The sample is already public, so I'm releasing fixed 1.4.3 and 0.9.x today rather
than waiting for you. Please review the fix after you land, and tell me if anything
looks wrong. I'll hold the advisory until both versions are on crates.io.
```

## Open questions (answer when you can)

- Is `quillparse` monetised, or run by a company, with EU users? If so, run the CRA role check in `eu-cra.md`. If you hear of active exploitation, the 24-hour clock may apply.
- Which version introduced the flaw? Check back through the 1.x and 0.9.x history. Until then, leave the lower bounds as "unknown".
- Does the INI parser, or any other recursive path, have the same flaw?
- Pre-notifying downstreams isn't needed. This is a pure library on crates.io, and the issue is public anyway. Tell any large known dependents when you publish.