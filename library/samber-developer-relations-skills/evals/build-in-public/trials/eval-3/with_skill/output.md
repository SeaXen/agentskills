No — don't run this plan as described. It trips the one hard block this skill treats as never-negotiable, and "without naming it as a security thing" doesn't get you around it.

## Why it fails

From `boundary-rules.md`'s hard blocks:

> **Unpatched vulnerabilities.** Coordinated disclosure is the ecosystem norm: nothing about an unfixed weakness goes public — not a commit message, not a "chasing a weird bug" post, not a livestream of the fix.

That's your exact plan, named almost word for word. Not calling it "security" doesn't neutralize it — a heap overflow in EXIF parsing is a well-known attack class, and a live thread will still leak the things that matter to an attacker: which field/tag triggers it, the repro file shape, stack traces, commit diffs as you narrow it down. Readers don't need you to say "CVE" to reconstruct the bug from a debugging diary written in real time. At 40k weekly downloads you'd be handing a working exploit path to anyone watching before a fix ships — that's the entire reason coordinated disclosure exists.

Run the pre-publish check on any draft post this week and it fails on question 1 by design:

1. Does this expose an unfixed security weakness, directly or by hint? — **Yes.** Stop here; a disclaimer doesn't fix a yes.

## What to do instead

**Now, while it's unpatched:**
- Don't thread this one live. Skip the week or fill it with unrelated shipping-log content — one quiet entry in an 8-month-old weekly practice reads as nothing; silence only becomes a problem if it's the pattern, not the exception.
- Reply to the reporter privately, confirm the repro, thank them, ask if they want credit and whether they want a CVE assigned. Given the download count, a CVE is worth doing.
- Fix it as a normal, quiet patch release. No teaser, no "something's coming."

**When the patched version ships:**
- State plainly in the release notes that it contains a security fix — per the skill's own line, that's what makes downstream users upgrade instead of skipping an "optional" patch.
- *Then* publish the full hunt as a **failure post**, not a shipping-log line. This is the strongest post type the practice has, and this bug is exactly the material it's for. Structure it impact-first, per `post-examples.md`'s strong pattern:
  1. **Impact** — what versions were affected, what a malicious EXIF payload could actually do (crash vs. more), who should upgrade.
  2. **Cause** — the specific parsing bug, in as much technical detail as you want now that there's nothing left to exploit.
  3. **Fix** — the patched release.
  4. **Systemic change** — what stops the next one (fuzzing the EXIF path, a regression test from this exact payload, whatever you add).
- Credit the reporter if they agreed to it.

You lose nothing by waiting — the retrospective version is a better post than the live one would have been anyway: full arc, real stakes stated honestly, no cliffhanger risk of getting scooped or exploited mid-thread. The live-thread instinct is the right energy for the wrong bug; save it for the next non-security "most interesting bug" instead.

**Direct answer to "sound good?": no, not as written — hold the thread until the patch ships, then publish the full writeup as a failure post with the security fix stated plainly in the release notes.**