# Governance review — Brightsea

## Bottom line

Don't send the GPG key or PyPI rights this week. Not because ferrous_owl is necessarily bad-faith — you don't have enough information either way — but because "pseudonymous contributor builds credibility over months, then a deadline creates pressure to hand a burned-out solo maintainer's signing key" is not a hypothetical. It's the [xz-utils/CVE-2024-3094 timeline](https://en.wikipedia.org/wiki/XZ_Utils_backdoor): credibility built from 2021, pressure on an exhausted solo maintainer, a backdoor shipped in signed releases in February 2024. Your situation matches the shape, not the proof of intent. Treat the shape as the signal.

The instinct to get help is correct. The instinct to solve it with one transfer, this week, under a conference deadline, is the part to stop.

## As-is

- One person (you) holds every credential: repo/org ownership, merge rights, release signing key, PyPI publish rights.
- **Contributor absence factor: 1** — the smallest number of people responsible for 50% of contributions is you, because you're the only one with merge rights regardless of how many PRs ferrous_owl authored. Authored-but-unmerged contribution doesn't reduce concentration; only shared *control* does.
- No written governance exists. That's not a side issue — it's why this is being negotiated as a private, deadline-pressured DM exchange instead of a visible, ruled process anyone could point to.
- 900 dependent projects, 340 open issues, no release in 5 months: this is a **stadium** (Nadia Eghbal's term — many users, very few contributors). The scarce resource is your attention, not code review throughput. That reframes the actual problem: it's not "who gets the keys," it's "how does maintainer load get distributed without concentrating risk in a new single point."

## Concentration gate

The skill's own rule: **an absence factor of 1 makes every shared governance model unadoptable until you recruit co-maintainers.** You're not choosing between governance models yet — you're below the floor for any of them. Fix that first (this *is* the fix you're reaching for; do it in the right order).

## What to do this week

1. **Reply to ferrous_owl now, don't go silent.** Silence under this pressure reads as either avoidance or eventual capitulation. A clear, generous, bounded plan reads as competence.
2. **Grant merge/triage rights now.** Cheap, reversible, evidence-based — seven months and 34 merged PRs is a real track record and the generous half of the trust ladder ("whenever somebody sends a pull request, give them commit access" — @felixge, via opensource.guide) applies here without reservation.
3. **Do not grant PyPI publish or the GPG key this week, and never in the same act as merge rights.** The staged-grant principle (post-xz-utils consensus, cited in this skill's succession playbook) says key-holder rights come after at least one supervised release cycle — release together, you hold the key, they watch and help, then reassess. That's a release cycle, not a deadline.
4. **Decouple 4.0 from the SciPy conference.** That date is ferrous_owl's forcing function, not yours. A legitimate co-maintainer can wait one cycle. If 4.0 genuinely should ship before SciPy, you ship it — signed with your existing key, with ferrous_owl doing the supervised co-release.
5. **Say the quiet part in public, not privately.** Open an issue: "Brightsea is moving from solo to a two-maintainer model. @ferrous_owl is joining as co-maintainer given their track record. Here's the plan and timeline." This does two things: it makes the decision a project decision instead of a personal favor under pressure, and it puts a real name/track record in front of your user base — mild but real identity verification, and exactly what the playbook means by "prefer a verifiable identity or an established public track record, and say so."

## The burnout — separate problem, don't let succession solve it by proxy

"Promoting to fix burnout" is a named failure mode: handing over keys because you're exhausted invites exactly the takeover pattern above, and doesn't even fix the burnout if the new holder turns out to need as much support as you did. Treat relief and succession as two different actions:

- **Pause or slow releases explicitly** rather than silently — a stated cadence beats disappearing for five months unexplained.
- **Triage the 340 issues in bulk**: close stale/duplicate/no-repro, label the rest, don't try to answer each individually.
- **Publish a stated capacity**: "I work on Brightsea 2–5 hours a week" is a legitimate governance clause (see the minimal GOVERNANCE.md below), and it resets expectations for everyone, not just ferrous_owl.
- **Recruit more than one person if you can.** A factor of 2 is still fragile — it's the *smallest* value at which no single departure stops releases, not a comfortable one. If there are other regular contributors, pull them into the triager/reviewer tier now; don't let one highly responsive volunteer become the only option because they're the only one who asked.

## Target end state for credentials — not "hand over everything"

Full handover trades your single point of failure for an identical one under a different name. Inventory every row, aim for two current holders on each, not one owner replacing another:

| Credential | Today | Target |
|---|---|---|
| GitHub repo/org ownership | you alone | you + ferrous_owl, after supervised cycle |
| Merge rights | you alone | you + ferrous_owl, **now** |
| PyPI publish rights | you alone | both, via scoped API tokens/Trusted Publishing, not a shared password — after cycle 1 |
| Release signing (GPG) key | you alone | either a second personal key added as co-signer, or both of you signing — after cycle 1 |
| Security report inbox | you (assume) | both |
| Docs/CI secrets, domain if any | you (assume) | both |

Re-verify this list on a cadence — it rots silently, and a row held by someone no longer active is a security incident waiting to be found.

## Minimal GOVERNANCE.md to publish now

This is the actual gap that let a private DM exchange become the de facto decision process. Publish something this small — it's a page, not a project:

```markdown
# Governance

## Scope
<name> maintains Brightsea. It parses scientific instrument file formats;
new format support is welcome, unrelated tooling (dashboards, GUIs) is out of scope.

## Roles
- Maintainer: <you>. Merge, release, direction. Working 2-5 hours/week — response
  times reflect that.
- Co-maintainer (candidate): ferrous_owl, merge rights granted <date> after 7 months
  and 34 merged PRs. Release-signing and PyPI rights follow one supervised release
  cycle, expected to complete by <date>.
- Contributors: anyone with a merged change.

## Decisions
Routine changes: one maintainer approves and merges.
Breaking changes, scope, or license: both maintainers must agree in a public issue,
7-day comment window.
Adding a maintainer: 3+ months sustained review activity, current maintainers agree
in public. Merge rights on agreement; release-signing/publish rights after one
supervised release cycle — never granted in the same act as merge rights.

## Stepping back
A maintainer inactive 6 months with no return date moves to emeritus, credit kept,
credentials rotated within 30 days. If all maintainers step back, we name a
successor or archive the repo publicly rather than leave it silently unmaintained.

## Changing this document
Any maintainer proposes, all current maintainers agree, 7-day open window.
```

## Decision rule that matters most here

> Key-holder rights (release signing, registry publishing) are granted only after at least one supervised release cycle, and never in the same act as merge rights.

This is a self-set baseline (not a published standard), chosen because it's the minimum separation that would have slowed the xz-utils takeover — the incident analysis's own recommendation. Say that openly to ferrous_owl if they push back; it's a policy applied to anyone, not a judgment of them specifically.

## What I'm not covering

- **Neutrality/vendor audit (step 6)**: not triggered — you're not company-backed and there's no employer-concentration question yet. Worth one question to ferrous_owl though: do they contribute independently, or on behalf of an employer? That changes the seat-cap conversation later.
- **Foundation/fiscal host (step 8)**: not triggered — no money or adopter-neutrality question was raised. Skip until one is.
- **Licensing/CLA**: not covered by this skill — route to counsel if it comes up.

## Review date

Revisit after the supervised 4.0 release cycle completes, or in 90 days, whichever comes first. Triggers to move sooner: ferrous_owl pushes again for keys before a joint release has happened, a second regular contributor appears (worth recruiting into the same ladder), or the issue backlog stops shrinking despite the triage pass.