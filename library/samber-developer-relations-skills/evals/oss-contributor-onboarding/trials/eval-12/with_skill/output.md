# Ashgrove Contributor Onboarding Plan

**Target: 1.0 release, November 14, 2026 (~7.5 weeks from today, September 24, 2026)**

## Before you use this

I could not read the actual Ashgrove repository — no URL or local path was provided, and my sandbox blocked filesystem search for one. Per your "no back-and-forth, assume standard best practice" instruction, this plan is built on stated assumptions about a Kotlin serialization library at pre-1.0 stage, and every assumption is flagged inline. It is built to the [`oss-contributor-onboarding`](../skill-wip/samber/developer-relations-skills/skills/oss-contributor-onboarding/SKILL.md) skill's method: measure the real path first, fix the two failures that leave no trace (broken cold setup, silence on PRs), then write the file, then design the review loop.

**The one thing that cannot be skipped:** run the audit script and the cold-run protocol below against the real repo before you act on anything in this plan. Everything downstream — the CONTRIBUTING draft, the first-issue examples, the scorecard — is written to be *adapted to what the audit finds*, not applied blind. Where I've made a Kotlin-ecosystem assumption (Gradle, KSP, Kotest, Maven Central) that turns out wrong, swap the specifics; the structure holds.

**Assumptions stated up front** (correct these first if wrong):
- Gradle Kotlin DSL, multi-module, targeting JVM + Kotlin Multiplatform (JS/Native)
- Hosted on GitHub, MIT or Apache-2.0 licensed
- Solo or small-team maintained, no existing corporate backing or foundation
- No CLA in place today (DCO or nothing)
- No dedicated community/DevRel headcount — you are reading this because you're doing this yourself
- 1.0 is a stability/API-freeze milestone, not a feature-complete milestone, so contributor scope should skew toward tests, docs, format adapters, and platform coverage rather than core API changes in the final weeks

---

## Part 1 — Run this first (Step 1: Baseline)

Do not write or change anything before this returns real numbers. A recommendation with no evidence attached is an opinion.

### 1.1 Run the mechanical audit

```bash
./scripts/contributor-path-audit.sh <path-to-ashgrove-repo>
```

If you're running this from within the `developer-relations-skills` skill checkout, the script lives at `skill-wip/samber/developer-relations-skills/skills/oss-contributor-onboarding/scripts/contributor-path-audit.sh`. It needs only bash, git, and standard POSIX tools — no network, no credentials. It will report:

- which of `CONTRIBUTING`, `CODE_OF_CONDUCT`, `SECURITY`, `SUPPORT`, `GOVERNANCE`, `CODEOWNERS` exist, and where
- which of ten CONTRIBUTING topics are mentioned (this is a keyword grep, not a coverage check — read the file yourself before trusting a "mentioned" result)
- the setup surface: `Makefile`/`Taskfile`/`.devcontainer`/`.tool-versions`/lockfiles present
- CI workflows that touch secrets (these cannot run on fork PRs — every one is a red check a stranger can't fix)
- git contributor history: distinct authors, one-commit-only rate, CHAOSS absence factor, new authors per year

### 1.2 Pull what the script can't see

From GitHub's UI or API, over a 90-day window:

- median time to first human response on issues/PRs opened by non-maintainers
- current count and age of open `good first issue` / `help wanted` items
- outcome of the last 10 external PRs (merged / stalled / declined / vanished), oldest comment first, noting where each one stalled

### 1.3 Walk it cold yourself (Step 2)

From a machine or container that has never built Ashgrove:

1. Read only the README and CONTRIBUTING — nothing else.
2. Execute the documented setup literally. Log wall-clock time to first passing test run.
3. Log every undocumented requirement: JDK version, KMP toolchain (Kotlin/Native needs platform-specific tooling if targeting iOS/macOS/Linux natives), a Gradle property, an environment variable, a signing key stub for publish tasks that shouldn't be required for `test`.
4. Don't fix anything mid-run — that hides the size of the problem.
5. Second run: from the beginner-issue list, can a stranger pick one, understand the ask, and find the file to change in under 15 minutes with no question asked?

### 1.4 Score it

Fill this in with real numbers before touching anything else. Template (full rubric in the scorecard reference):

```markdown
# Contributor path audit — Ashgrove — 2026-09-24 (fill in actual date run)

## Verdict
<PASS | FAIL> — blocking: <n>/4, scored: <n>/16

## Blocking checks
| Check                        | Result | Evidence |
|-------------------------------|--------|----------|
| B1 Contribution is invited    |        |          |
| B2 Documented setup runs cold |        |          |
| B3 ≥3 unclaimed beginner issues exist |  |    |
| B4 Median first-response time inside published target | | |

## Scored checks (0–2 each, 16 total)
S1 Out-of-scope stated · S2 Prerequisites pinned · S3 Local gates match CI ·
S4 Fork CI is useful · S5 First issues complete · S6 Claiming convention defined ·
S7 Legal gate pre-announced · S8 Credit + next-step given

## Funnel baseline
New external contributors (last 4 quarters): __, __, __, __
Second-contribution rate within 90 days: __%
Median time to first response: __ days
External first-PR merge rate: __%
Contributor absence factor: __
```

Pass threshold: all 4 blocking checks, plus 12/16 scored. This is the skill's own baseline, not a published standard — say so if anyone asks where "12" comes from.

**Given the November 14 deadline, sequence the fix order below by damage-per-hour, not alphabetically.** A broken cold setup or silent PR queue outranks every wording improvement in Part 3, however fast that wording is to ship.

---

## Part 2 — Fix the environment before the prose (Step 3)

For a Gradle/Kotlin/KMP project, in efficiency order (cheapest fix that removes what the cold run actually found — don't jump to the container tier unless the cold run shows toolchain pain the cheaper tiers can't fix):

1. **Pin the toolchain, if not already done.** Gradle's [toolchain support](https://docs.gradle.org/current/userguide/toolchains.html) (`kotlin { jvmToolchain(21) }` or similar) plus a committed `gradle/wrapper` pins the JDK and Gradle version without asking a contributor to install anything by hand. If Ashgrove targets Kotlin/Native, confirm the README states which host OS each native target needs (Linux binaries need a Linux host or cross-compile setup; iOS targets need macOS) — this is the single most common undocumented requirement in KMP libraries, and it produces no issue, just a contributor who gives up.
2. **One command, clone to green tests:** `./gradlew test` should work with zero manual steps on a machine with only a JDK installed. If Ashgrove needs a KSP-generated build step, confirm `./gradlew test` triggers it automatically rather than requiring a separate `./gradlew kspKotlin` first — an implicit two-step build is exactly the kind of undocumented requirement the cold run exists to catch.
3. **Split CI into a credential-free lane and a privileged lane.** Anything that needs a Sonatype/Maven Central signing key or a publish token must not run on fork PRs — if it does today, every external PR shows red on a check the contributor cannot fix, which reads as "your code is broken" when it's actually "you're not a maintainer." Gate the publish-dry-run and any KMP native cross-target builds you can behind `pull_request_target` only if a maintainer explicitly approves the run.
4. **Turn on "allow edits from maintainers"** on the repo's default branch protection, and say so in CONTRIBUTING — this is the cheapest fix in this entire plan and it directly saves stalled PRs from being closed.
5. **State the merge style** (squash is the default that keeps a Kotlin project's history clean across a small formatting commit and a real change) in CONTRIBUTING.
6. **Consider a `.devcontainer/` only if the cold run shows real toolchain pain** — e.g., if Kotlin/Native cross-compilation or a native library dependency (common in serialization libs with CBOR/protobuf C bindings) makes local setup genuinely hard. Don't build one preemptively before Nov 14; it's the highest-maintenance tier and the one most likely to rot if you don't personally develop inside it.

Re-run the cold run after each fix. Stop when nothing new surfaces.

---

## Part 3 — CONTRIBUTING.md (Step 5, draft)

Every command below must be one you've actually run in Part 2 before you publish this — a contributing guide describing a setup that doesn't work is worse than no guide. Replace bracketed placeholders with your real values once Part 1–2 confirm them.

```markdown
# Contributing to Ashgrove

Thanks for being here. Ashgrove is a Kotlin serialization library heading to 1.0
on November 14, 2026 — we're prioritizing stability, test coverage, format
adapters, and documentation over new core APIs right now.

We take code, tests, documentation, format-adapter contributions, and
Kotlin Multiplatform target coverage.

We do not take: new core-API surface changes before 1.0 ships (open an issue
to discuss first — anything landing after 1.0 will go through a design
review), style-only rewrites, or new runtime dependencies without prior
discussion.

## Ways to help without writing a codec

- Reproduce and confirm open bug reports
- Improve an error message that confused you
- Add a missing test for an existing code path
- Fix or expand the KDoc on public API surfaces
- Report which Kotlin/Native targets you've verified working

## Get the project running

    git clone <your fork> && cd ashgrove
    ./gradlew test

Expect: `<N> tests passed` in under `<M>` minutes.

Prerequisites: JDK `<version>` (pinned via Gradle toolchain — you do not need
to install a specific version yourself), no other manual setup.

If you're working on a Kotlin/Native target, see [platform notes] — building
`<target>` requires a `<host OS>` host.

Run the same checks CI runs, locally:

    ./gradlew ktlintCheck detekt test

## Find something to work on

Beginner-friendly issues: [label query link]. Comment on the issue to claim
it — claims expire after 14 days with no activity, so someone else can pick
it up. Fewer than 3 open? Ping us in [channel] and we'll stock more.

Nothing fits? Open an issue describing what you want to change before
writing code — especially for anything touching the core `Encoder`/`Decoder`
API before 1.0 ships.

## Before opening a pull request

    ./gradlew ktlintCheck detekt test

Target the `main` branch. Sign your commits with `git commit -s` (DCO — a
one-line sign-off, not a signing workflow).

## After you submit

A maintainer responds within `<your honest target — see note below>`. We
squash-merge. Merged changes ship in the next release and you're credited
in the changelog. If your PR goes quiet for two weeks, we'll check in with
options to finish it ourselves (with your authorship kept), hold it open,
or close it with a follow-up issue — never a silent auto-close.

## Stuck?

Ask in [Discord/Slack/Discussions link] — usually answered within
`<latency>` — or comment directly on your issue or PR.

## Recognition

Merged contributions are credited in the release changelog. Repeat
contributors are invited to become reviewers on their area of the codebase.
```

**On the response target line:** don't publish "within 24 hours" because it sounds good. Publish the number you can actually hold from your real weekly bandwidth — "a stated seven days that is met beats a stated 48 hours that is missed." The two-clock rule in Part 4 below is what makes even a slower target survivable: the *acknowledgment* clock is same-day regardless of what the *review* clock says.

**On the DCO/CLA choice itself:** that decision belongs to license strategy, not this plan — but its *placement* does. If you're keeping DCO, `git commit -s` costs a drive-by typo-fixer nothing. If Ashgrove is heading toward a CLA before 1.0 for IP-cleanliness reasons, state it in CONTRIBUTING *before* the setup section, not at the PR gate where it stops someone who's already written the fix.

**For agent-assisted contributors:** an increasing share of first PRs on Kotlin/Gradle projects now arrive via a coding agent reading this file cold. State branch naming, commit format, and required checks literally near the top — not only inside a PR template — and write out `./gradlew ktlintCheck detekt test` rather than only `make check`, since agents are typically instructed not to execute a wrapper command they haven't seen the literal steps for, and not to fetch any linked URL for a mandatory step.

---

## Part 4 — Stock the first-issue queue (Step 4)

For a pre-1.0 serialization library, the highest-value beginner-issue categories are ones that don't touch core API surface (which you're freezing) but genuinely need doing:

1. Format adapter edge cases (e.g., a specific JSON/CBOR/YAML encoding edge case that has a clear expected output)
2. Kotlin Multiplatform target verification/CI coverage for a target not yet tested
3. KDoc completion on public API surfaces
4. Error-message clarity fixes (a wrong-type deserialization error that currently says "unexpected error" instead of naming the field and expected type)
5. Missing test cases for already-fixed bugs

Size each at roughly one evening including setup. Every issue needs: observed vs. expected behavior, the file and its test, an explicit "design is settled, no discussion needed" where true, the exact verification command, and a named mentor (you, until you have co-reviewers). Label by the *skill/domain* required (`skills/serialization-cbor`, `skills/kmp-native`) rather than by difficulty — newcomers pick issues by "can I already do this," not by an assumed difficulty rating.

**Worked example, adapted to Ashgrove:**

```
Title: CBOR decoder reports "unexpected error" on truncated byte array
Labels: good first issue, area/cbor, skills/kotlin-io

**Current behaviour**
`Cbor.decodeFromByteArray<T>(truncatedBytes)` throws a bare
`SerializationException("unexpected error")`.

**Expected behaviour**
Throws `SerializationException("unexpected end of CBOR input at offset <n>, expected <N> more bytes for field '<field>'")`.

**Where**
`ashgrove-cbor/src/commonMain/kotlin/CborDecoder.kt`, the `readBytes()` bounds check.
Tests: `ashgrove-cbor/src/commonTest/kotlin/CborDecoderTest.kt`.

**Suggested approach**
The bounds check already exists; it just discards the offset and field name
before throwing. Thread them through. No design discussion needed.

**Verify**
`./gradlew :ashgrove-cbor:test --tests "*TruncatedInput*"`

**Mentor**
@<you>. Comment here to claim; claims expire after 14 days.
```

Keep a standing floor of at least 3 unclaimed, currently-valid issues like this — someone who finds zero doesn't come back to check later. Given the Nov 14 deadline, spend an hour now stocking 5–6 of these rather than trying to backfill during release week.

---

## Part 5 — Review and recognition playbook (Step 6)

Turn this into something you actually reference, not prose you read once:

1. **Acknowledge same day, review on a separate clock.** "Thanks — this is in scope, full review by [day]" costs two minutes and prevents the silent-PR failure, which is the single most damaging and most invisible leak in the whole path.
2. **Answer scope in the first comment**, not after three review rounds.
3. **Review in fixed order:** scope → correctness and tests → design (with reasoning) → style. `ktlintCheck`/`detekt` catches formatting — never raise it as a human comment if the linter already flagged or would flag it.
4. **Label every comment Blocking or Optional.** An unlabeled wall of comments reads as more failure than it is.
5. **Decline fast and kindly** when something's out of scope: thank them, name the rule, point at CONTRIBUTING's scope section, offer an alternative issue, close. Don't let it rot.
6. **Credit at merge**: keep them as commit author, name them in the changelog, and separately record non-code contributions (docs, triage, KMP-target testing) somewhere visible — the commit graph doesn't show those.
7. **Invite the second contribution by name** — "if you want another one, #123 is the same area, slightly deeper." This is the moment a drive-by becomes a contributor, and it doesn't happen by itself.
8. **Write down the stall protocol** and use it: check in, offer to finish it yourself with them kept as author, or close with a follow-up issue — never let a bot silently close it.

Reply templates (first response, decline, merge message, stalled-PR check-in) are in [`first-issue-and-review-examples.md`](../skill-wip/samber/developer-relations-skills/skills/oss-contributor-onboarding/references/first-issue-and-review-examples.md) — copy the shape, not the wording.

**One evidence-backed thing to build into your own review habit, not just policy:** a 3M-PR study (Terrell et al., PeerJ CS 2017) found that among *outside* contributors specifically — exactly this funnel — women's PRs merged at 58% against men's 61% where gender was identifiable, while gender-neutral profiles scored highest of all. Review against the written scope rule and the fixed order above, never against an impression of the contributor — it's the cheapest available control you have on that gap.

---

## Part 6 — What NOT to spend Nov-14 runway on (Step 7)

With ~7.5 weeks and (per the stated assumption) no dedicated community headcount, don't buy:

- **A structured mentorship program** (GSoC, Outreachy, LFX). Real value, but it's a standing seasonal commitment you can't abandon halfway, and it only pays off once Steps 3–6 above already hold. Hosting one under-mentored around your own 1.0 crunch is worse than not hosting one — and the two most-cited studies on outcome (GSoC's 63.5% continuation vs. Mozilla's finding that mentored-bug starters were *less* likely to become long-term contributors) actively disagree, so don't promise yourself it fixes retention.
- **An onboarding event or sprint.** Costs a week of prep for the least-measured return of the three options; even Kubernetes retired its own flagship version of this because it "never led to any people who weren't already contributing... becoming dedicated contributors."
- **A reward with no quality gate** (e.g., a Hacktoberfest-style badge/swag hook with no review capacity behind it) — this buys PR volume you can't review in the run-up to a release, which is a cost right now, not a benefit. Delete it explicitly rather than quietly not doing it.

**Do install a bot** for purely mechanical work (stale-claim nudges, auto-labeling by changed path) — near-zero effort, reversible in one commit, and it never should be allowed to touch the acknowledgment or decline messages, which stay human per Part 5.

---

## Part 7 — Sequencing against November 14

Ordered by damage-removed-per-hour, per the skill's own ranking rule — a broken blocking check always outranks a scored wording fix, however fast the wording is:

| When | Action |
|---|---|
| This week | Run the audit script + cold run (Part 1). This determines whether anything below is even needed, or already true. |
| This week | Fix any B2 (setup) failure the cold run finds — nothing else matters if a stranger can't get to green tests. |
| Week 2 | Split fork CI into credential-free vs. privileged lanes (S4); turn on maintainer-edit access; state merge style. |
| Week 2–3 | Publish CONTRIBUTING.md (Part 3), agreed section by section if you have a co-maintainer to review it with. |
| Week 3 | Stock 5–6 beginner issues (Part 4); write and pin the claiming/expiry convention. |
| Ongoing from week 2 | Apply the two-clock review habit (Part 5) to every incoming PR — this is a behavior change, not a one-time deliverable, and it's the one thing most likely to silently regress under release pressure. |
| Week 6–7 (pre-1.0) | Re-run the scorecard. Target: all 4 blocking checks pass, ≥12/16 scored, before the release goes out — a broken first-contribution path discovered *by your new contributors* during your own 1.0 launch week is the worst possible timing for it. |
| Post-1.0 | Re-audit quarterly and after any build/test command change. If your environment supports scheduled tasks, automate the reminder rather than relying on memory. |

---

## Part 8 — What to track after November 14

At Ashgrove's likely volume, these are dated anecdotes, not a dashboard yet — a single conference mention or Hacker News hit will move every number below more than any process fix will, so log confounders next to the numbers:

- **New external contributors per quarter** — the headline number, and the noisiest one.
- **Second-contribution rate within 90 days** — the actual retention number this whole plan exists to move.
- **Median time to first human response** (bots excluded) — against your own published target, not the 48-hour reference point unless you can actually hold that.
- **External first-PR merge rate and median time to merge** — tracked separately from your own PRs, which are always faster and will hide the real number if mixed in.
- **Contributor absence factor** (from the audit script) — should rise slowly over time; it's the only metric here that measures whether the project got less dependent on you alone.
- **Setup support load** — issues/messages that are really "I couldn't build it." Should trend toward zero once Part 2 is done; it's also the fastest-visible sign the fixes worked.

Don't import another project's outcome number ("80% of our interns kept contributing") as if it transfers — measure Ashgrove's own funnel.

---

**If the assumptions at the top turn out wrong** — different build tool, existing CLA, an existing co-maintainer team, a KMP target set I didn't guess — the fix is local: swap the Gradle commands, the scope lines, and the response-target math in Parts 2, 3, and 7. The sequencing logic (measure → fix the two invisible failures → write the file → fix the review loop → decide against shortcuts → hold the score) doesn't change with the tech stack.