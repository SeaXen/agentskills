The short version: the 26,000-session post wasn't a content format that worked — it was a rare industry event multiplied by your speed. You can't put "a big CVE drops here" on a calendar. What you *can* schedule is the **capacity** to catch those events, and that reframe is the difference between a calendar that works and four disappointing posts. Everything below follows from that.

---

## 1. How to build the four slots into the plan

**Why the literal version fails.** Container/runtime security produces roughly 0–2 "everyone is talking about it" events per quarter — a runc-class escape, a supply-chain compromise, a KEV listing in your domain. Four fixed "news reaction" dates will mostly land on quiet news days, and forcing a reaction post to nothing (a minor patch release dressed up as big news) trains your audience to ignore the format. Worse: when the real event *does* drop on a Tuesday, publishing it at the scheduled Thursday slot throws away the only advantage you had — same-day speed.

**Schedule reserves, not dates.** Mark one slot per month, mid-month:

| Slot | If a qualifying event fired that month | If nothing fired |
|---|---|---|
| Reserve 1 (Oct, W2) | Reaction post — published the moment it's ready, not on the slot date | Evergreen backfill #1 |
| Reserve 2 (Nov, W2) | Same | Evergreen backfill #2 |
| Reserve 3 (Dec, W2) | Same | Pre-banked or skip (Dec 19+ is dead air) |
| Reserve 4 (Dec, W3) | Same | Skip; roll capacity forward |

Three rules make this work:

1. **The slot is bookkeeping, not a publish gate.** Speed beats calendar discipline every time. When news fires, you publish within hours and the reserve slot is "used."
2. **Never force a reaction to nothing.** If nothing qualified, the backfill ships. A forced "our take on a routine release" post costs more credibility than the slot is worth.
3. **Pre-bank two evergreen deep-dives before the quarter starts.** Write them in September, hold them ready. This is what lets rule 2 exist without shipping nothing.

**Define "qualifying event" in writing** so go/no-go isn't a debate under pressure. Criteria: (a) container runtime, orchestrator, or supply-chain component; (b) escape/RCE/auth-bypass class; (c) near-universal deployment; plus at least one attention signal (KEV listing, HN front page, major coverage). Require (a) + (b) + one signal.

**Build the fast lane.** The 26K post worked because nobody waited for the normal editorial cycle. Institutionalize that: a fixed page template, a pre-agreed on-call technical reviewer, the go/no-go decision delegated to the DevRel lead with **no CEO signoff in the loop**, and pre-cleared guardrails (no detail beyond public PoCs, no customer names, hedged impact language, public "last updated" corrections). Target: advisory-public to post-live in under 6 hours.

**Add the schedulable sibling: a monthly digest.** "This month in container security," first Friday of the month. It won't do 26K — it does something more important for the news play: it teaches Google and your readers that Stavepoint is where you come when a CVE drops, so the next same-day post starts from a bigger base and ranks for the CVE-name query immediately.

**What to tell the CEO up front** (week 1, in writing, so month three isn't a surprise): the 26K post was an event × speed outlier at ~29× your baseline. Realistic expectation for the four slots is that 0–2 convert to real events; the others backfill with evergreen. Judge the program on time-to-publish and event-capture rate; the traffic spikes are upside the industry hands you, not output you manufacture.

---

## 2. What to report each month

Design principle: **report what you control separately from what the industry hands you.** If the report only shows sessions per post, a quiet month reads as failure and the CEO kills a program that's actually working. One page, six blocks:

```
Stavepoint — content report, <YYYY-MM>

1. SHIPPED
   Planned X, published Y on time. Slipped: <why>.
   Reserve slots: 1 converted to news (event: ...), 1 backfilled evergreen.

2. NEWS READINESS          ← the part we control; the trend line that proves the calendar works
   Advisories triaged: 214. Met big-event threshold: 3. Covered same-day: 3/3.
   Time advisory→publish: 5h10 (last month 7h02; target <6h).

3. REACH BY CLASS          ← never averaged across classes
   Deep dives: rolling 3-mo avg 940 vs 900 benchmark.
   Monthly digest: 1.8K.
   News reactions: reported per post, with event context
   ("CVE-… was KEV-listed container escape; 18K sessions/48h; #3 for 'CVE-… docker'").

4. COMPOUNDING             ← did spikes convert to durable audience?
   Newsletter adds: 312 (+190 from the news post).
   Return-visitor rate on news posts: 8%. Backlinks earned: 9.

5. BUSINESS
   Demo requests attributed to content: 14 (3 from the news spike).

6. NEXT MONTH + one ask/risk
```

Reporting hygiene, four rules:

- **Fixed definitions all quarter.** Same analytics property, same session definition, decided in week 1. Never redefine mid-quarter.
- **Rolling 3-month windows** for baseline classes — monthly n is too small and noisy to trend.
- **Every news number carries its event's context**, never an average. "News posts averaged 6K" is a meaningless statistic across events of different sizes.
- **State the benchmark bands in the report itself**: deep dives ~900, digest ~1–2K, news = f(event size), historical: 26K on one KEV-class event. This is the written version of the expectations memo and it's what stops the CEO anchoring on 26K as the bar.

The readiness block is the answer to "is the calendar working": in a month with zero qualifying events, falling time-to-publish and 3/3 capture *is* the win, and the report says so in numbers.

---

## 3. The draft post

Framing: you can't draft a reaction to news that hasn't happened, so this is the **rehearsal draft** — the format fully worked on a real, verifiable historical case (CVE-2024-21626, the runc "Leaky Vessels" escape — squarely Stavepoint's domain). Two ways it goes live: a qualifying event drops and the team swaps the case in within hours, or a reserve slot backfills and it publishes as-is, as an evergreen. Bracketed fields `[...]` are the deliberate swap-points. Bonus: time the team doing the swap — that's your baseline time-to-publish, drill #1.

---

**Title:** CVE-2024-21626 ("Leaky Vessels"): how the runc escape works and what to do right now
*Alternates: "The runc fd leak, explained" / "Leaky Vessels: the container escape underneath Docker and Kubernetes"*

*Last updated: 2024-01-31 14:00 CET — corrections posted in public, timestamped.*

**TL;DR**
- **What:** runc — the runtime underneath Docker Engine, containerd, and Kubernetes — leaked a host file descriptor into containers. A malicious image or exec request can turn that leak into a full container escape. It's the worst of four flaws disclosed today as "Leaky Vessels" (CVE-2024-21626, plus lower-severity CVE-2024-2365/2366/2367). Severity: High `[CVSS — verify vs NVD at publish]`.
- **Who's exposed:** any Linux host running runc `[< 1.1.12]` that runs or execs images you don't fully trust. Multi-tenant CI runners are the worst case.
- **Do now:** patch your *hosts* to runc `[1.1.12]` — the fix comes through distro/docker/containerd packages, not through your images. Then hunt for exec events with a working directory under `/proc/self/fd`. No mass container restart is required.

### What happened

The runc maintainers disclosed four vulnerabilities today, the most serious being CVE-2024-21626. During container start and exec, runc unintentionally leaked an internal file descriptor — referencing a directory on the host's cgroup filesystem — into the container's process. Fixes shipped in runc `[1.1.12]`. `[Link advisory, release notes, NVD entries.]`

Because runc sits at the bottom of the stack for effectively every Linux container platform, the exposure question isn't "do we use runc" but "where do we run images we didn't build."

### Am I affected?

- **Single-tenant clusters, trusted images only:** lower urgency. Patch on your normal host cadence.
- **Anything executing untrusted images or builds** — self-hosted CI runners, multi-tenant platforms, anything that runs third-party or user-submitted images: treat as urgent. This is the attack's intended audience; a malicious image is the delivery mechanism.
- Note the fix lives on the node, not in the image: your containers are only as patched as the hosts underneath them.

### The bug, mechanically

runc opens file descriptors internally while setting up a container (cgroup configuration among them). One of them wasn't closed before handing control to the container's process — it lacked the close-on-exec flag.

That matters because of how `/proc/self/fd/N` magic symlinks work: opening a path through one re-opens whatever the fd actually references, and a relative path walk from that fd follows the fd's *own* filesystem — host-side — regardless of which mount namespace the process sits in. Container isolation is enforced on path resolution from the container's root. An inherited fd is a hole punched before the gates closed.

The attack is almost anticlimactic once you see it: a malicious image sets its working directory (`WORKDIR` / exec cwd) to `/proc/self/fd/[9]`. The process starts "inside" the host's cgroup directory, and file operations from there land on host filesystem objects. From that foothold, a motivated attacker reaches full escape depending on what else is reachable and writable.

Two things make this class worth internalizing:

- **No control you're used to stops it.** It's not a syscall you can seccomp away — opening `/proc/self/fd` of *yourself* is normal behavior. Capability checks pass. It's lifecycle hygiene: fd state at the moment of exec.
- **It recurs.** runc's previous famous escape, CVE-2019-5736 (overwriting the host runc binary via `/proc/self/exe`), was a different mechanism in the same place: the boundary failing through the runtime's own lifecycle, where image scanning and admission control have no line of sight.

### What to do in the next hour

1. **Inventory runc versions per node** (`runc --version` across hosts, or your asset view — `[Stavepoint product screenshot: nodes below 1.1.12]`).
2. **Patch hosts** via distro/docker/containerd packages. The flaw is exercised at run/exec time — upgrading the binary protects every future operation, so patch rolling, without a workload restart.
3. **Hunt** for the indicator below, CI runners first. Also check historical exec events for cwd values under `/proc/self/fd` — presence means someone probed.
4. **If you can't patch today:** pause third-party builds on self-hosted runners and restrict exec paths on untrusted workloads.

Detection rule (Falco-style syntax; same logic in any runtime sensor or auditd pipeline):

```yaml
- rule: Container process started via /proc/self/fd working directory
  condition: evt.type=execve and container and proc.cwd startswith /proc/self/fd
  output: "escape-suspect exec (user=%user.name proc=%proc.name cwd=%proc.cwd)"
  priority: WARNING
```

This rule doesn't know about CVE-2024-21626 — that's the point. It catches the *behavior* the bug enables, which covers this instance and the next variant of the class.

### What we don't know yet

`[Fill at publish: exploitation observed in the wild? KEV status? vendor CVSS disagreements?]` Same-day analysis carries its unknowns explicitly. We'll update this section, timestamped, as facts land.

*We sell runtime security for containers. The analysis and detection above are vendor-neutral and work without our product. If you want the rule as a drop-in plus a node-level runc version audit, it's here: `[link]`.*

**References:** `[runc advisory | runc 1.1.12 release | NVD entries | original disclosure credits]`

---

**Go-live swap checklist** (when a real advisory drops — this is the fast lane, rehearsed):

- **0:00** — Event confirmed against threshold criteria. DevRel lead calls go. No escalation.
- **0:00–0:30** — Fill every `[bracketed]` fact from the *primary* source (vendor advisory, patch, NVD — not press coverage). TL;DR and affected versions first.
- **0:30–2:00** — Rewrite "The bug, mechanically" from the actual patch diff or PoC. Adapt the detection rule; test it once if you can.
- **2:00–3:00** — Pre-named reviewer pass against the pre-cleared guardrails.
- **Publish** — distribute to HN/Lobsters/r/kubernetes, newsletter, Slack communities. Stamp every correction publicly.
- **+48h** — snapshot sessions, rank for the CVE query, and signups: that's block 3 and 4 of next month's CEO report, already written.

If you want, I can next turn the slot rules and threshold criteria into the actual Q4 calendar with the digest and backfill dates placed, or draft the two pre-banked evergreen topics.