# Corvid Launch Readiness — Verdict: **Go, with reduced scope**

Oct 14 is 20 days out. That's enough time to close every blocker below except possibly one — and that one isn't on your list. Read Clearance first; it's the actual critical path.

## Clearance (you didn't ask, but this gates the date)

⚠️ **Name/trademark clearance status: unknown, and unstated.** Step 1 of this skill treats this as the one item that isn't a fixable defect — it's a rename-trigger, and once "Corvid" is in a CTO's public keynote, it's expensive to undo. Two flags:

- "Corvid" has prior art as a software product name: Wix's low-code platform launched as **"Corvid by Wix"** and was rebranded to "Velo" in 2020. That doesn't tell you the legal outcome, but it's exactly the kind of colorable conflict the clearance search exists to catch — phonetic/visual/conceptual, not just identical matches.
- Standard lead time for this is 8+ weeks. You have under 3. That gap doesn't mean skip it — it means it starts **today**, in parallel with everything else, in front of counsel, not at the end of the punch list.

⚠️ **License / CLA-DCO position: not mentioned.** Confirm an OSI-recognized license file is in the repo, matches whatever the README claims, and is dependency-compatible. Since Fennmark is the owner, state the CLA-vs-DCO position before the first external PR arrives — don't let it get decided by whichever template got copied in.

❓ **Is anything paid or planned to be paid?** If Fennmark has a hosted/enterprise angle on Corvid, disclose it in the announcement itself. Readers accept a stated business model; they don't forgive discovering one later.

If clearance comes back clean this week, everything else below is very achievable by Oct 14. If it doesn't, that's the conversation to force now, not on Oct 10.

## Blocker-by-blocker

| # | Blocker | Status | Verdict |
|---|---|---|---|
| Name | ⚠️ Unclear | See above — start today |
| License | ⚠️ Unstated | Confirm file + CLA/DCO this week |
| Install | ⚠️ Half-verified | Windows untested = fails the gate as written |
| First success | Presumed OK | Confirm with a real cold run (below) |
| Ten-second read | Presumed OK | README is written, not separately flagged as broken |
| Reachability | ⚠️ Partial | Issues-at-launch is fine timing-wise; day-of *availability* is the real risk (see Risks) |
| Distribution | ❌ Open | Nothing published anywhere — must close |
| Hygiene | 🔴 Open, highest-severity | Full monorepo history is the single biggest risk on this list |
| Claims | ⚠️ Open | Staging-cluster benchmarks aren't defensible as-is |
| Security contact | ❌ Open | No SECURITY.md — mandatory, cheap, no excuse |
| Contribution channel | ⚠️ Partial | Issues yes; CONTRIBUTING.md / comms channel unstated |

### 🔴 Hygiene — fix this first, it's the one that can't be caught by a cold read

"History intact back to 2023, pulled from the internal monorepo" is the highest-risk single item here, and it's easy to underrate because "keeping history" sounds like the responsible choice. It isn't automatically safe:

- Commit **messages** carry over even when a path-filtered extraction (`git filter-repo --path`) strips unrelated files — internal ticket references, other service names, "wire into fennmark-auth" style notes, all of it.
- If the extraction instead kept the literal monorepo tree rather than a clean path-filtered history, you may have full diffs of *other* internal services sitting in old commits.
- Two years of commits is a lot of surface for a stray key, internal hostname, or staging credential that was fine in a private repo and isn't fine in public.

Run a secrets scanner (gitleaks or trufflehog) across the **full history**, not just HEAD, and grep commit messages/diffs for internal hostnames, service names, and ticket IDs before this repo goes public. If anything turns up, the standard fix is a clean history rewrite (or a single-commit squash) rather than trying to redact after the fact — cheaper to decide that now than to discover it in an HN comment.

### ⚠️ Windows install — untested is a fail, not a maybe

The blocker is "works on a clean machine for every OS the README claims" — an untested Windows path means the README is currently making a claim you haven't verified. Two ways out, both fit in 20 days:

- Run the actual cold-run protocol on a clean Windows machine this week: someone who's never touched Corvid follows only the README, no help, and you log every hesitation. Fix and re-run.
- If it doesn't pass in time, cut it: pull Windows from the README and ship Linux/macOS only for launch. That's a **reduced-scope** move, not a failure — a broken install command posted as the top comment does permanent damage; a narrower supported-OS list does not.

### ⚠️ Benchmark numbers — staging-cluster numbers are a liability, not an asset

An unreproducible number is explicitly called out as the one booster that backfires: it invites "reproduce this on what instance type, what mesh version, versus what baseline" — questions a staging-cluster run usually can't answer for a stranger. Two options:

- Document hardware, versions, and method, and ship a runnable reproduction command in the repo (e.g. `bench/README.md`), ideally against something a reader can actually rent, not your internal cluster.
- If that documentation doesn't exist and can't be produced credibly by Oct 14, drop the numbers from the announcement. Publish them later, properly reproducible, as their own write-up — that's more credible than a number nobody can check.

### ❌ Distribution — cheap, but must actually happen

"Registry publish" is near-zero effort but ranks first for a reason: it's what every other channel's traffic depends on. For a sidecar this likely means a container image (Docker Hub/GHCR) plus a tagged GitHub release, possibly a Helm chart. Confirm what "the registry" is for this project specifically and get it live — not on Oct 14 morning, earlier, so it's boring by launch day.

### ❌ SECURITY.md — non-negotiable given what this project is

A service-mesh sidecar sits in every request path it touches — a vulnerability report here is inherently higher-severity than for a typical library. No `SECURITY.md` means no private channel to move a live disclosure into during the launch thread, which is exactly when one is most likely to show up. This is an hour of work with no reason to skip it.

### ⚠️ Contribution channel — half done

Issues-enabled-at-launch is fine; the checklist's concern is a public place existing *when the announcement lands*, and that's satisfied. Add a `CONTRIBUTING.md` and name a communication channel (even just "open an issue") — an hour of work, and it's what keeps early contributor interest from turning into unstructured DMs to you personally.

## Explicitly not blockers — don't spend the 20 days here

- **No demo video.** It's a booster (highest lift-per-hour for individual adoption), worth an hour or two if time allows late, but it does not gate the date.
- **No docs site.** The checklist is explicit: a docs site is only warranted once the README has outgrown itself, and building one early is "a second place to go stale." A good README is correct at this stage — don't build one to feel more ready.

Given Corvid is infra a company has to get approved internally, if you do have spare hours, put them into a short comparison table (real alternatives, at least one row you lose) and a maintenance/release-cadence statement — those are what an approver forwards up the chain, and they rank above a demo video for this specific audience.

## Risk: "nobody home"

Your announcement is a CTO keynote at a conference. That's also exactly the scenario where the engineering team is on a plane or in a hallway track, not sitting on GitHub. Reachability requires a maintainer actually available launch day and the day after — name who is *not* traveling and is on triage duty while the keynote is happening, before Oct 14, not that morning.

## 20-day punch list, in order

1. **Today:** start trademark/name clearance in parallel with everything else. This is the only item that can still move the date.
2. **This week:** full-history secrets/hygiene scan; decide squash-vs-redact if anything surfaces.
3. **This week:** cold-run the Windows install on a clean machine; cut Windows from the README if it doesn't pass in time.
4. **Next week:** publish to the registry, tag a release; write SECURITY.md; write CONTRIBUTING.md.
5. **Next week:** decide on the benchmark numbers — document+reproduce, or cut them from the announcement.
6. **Before Oct 14:** confirm license file + CLA/DCO stance; confirm paid/commercial disclosure language if applicable; name who is on-call during the keynote.

Nothing here needs the date to move if clearance comes back clean. If it doesn't, that's the conversation to have this week, not the week of.