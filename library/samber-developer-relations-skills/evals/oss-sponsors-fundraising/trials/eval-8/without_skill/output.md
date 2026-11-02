Here's how to carry the application forward from your opening, mapped onto NLnet's actual form structure so you can drop each block straight into the online form. (Field wording shifts slightly release to release — pull up the live form on nlnet.nl before you paste anything in, but the structure below has been stable for years.)

**Fund and timing, first.** For a mesh networking stack this is almost certainly **NGI Zero Core** (the fund explicitly themed around resilient, decentralised, "keeps the internet working" infrastructure) rather than Commons or Entrust — apply there unless the current call text on nlnet.nl says otherwise. NLnet runs quarterly deadlines (Feb 1 / May 1 / Aug 1 / Nov 1); from today that's **November 1, 2026** — confirm the exact date on the site, they occasionally shift by a day or two. Portugal is an EU member state, so your Lisbon residency and individual-applicant status aren't an eligibility problem — don't spend words justifying that.

**The throughline your opening sets up:** NLnet funds *sustainability of things that already work*, not moonshots. A reviewer's first question after "what is this" is "why does it need money now." Your 2019-to-now story is the answer — use it to earn the "why now," then get concrete fast. Don't linger in narrative past the "have you been involved before" field; reviewers reward specificity over sentiment from that point on.

---

### Abstract (≈50 words)

> Ferrolink is a low-power mesh networking stack for environments without reliable infrastructure — disaster response, remote sensing, off-grid communities. In production use since 2019, maintained by one person. This grant funds a year of dedicated hardening — security review, protocol robustness, power-budget tuning, test coverage — so it can be depended on, not just used.

### Have you been involved with projects or organisations relevant to this project before?

This is where your drafted opening lands almost unmodified — NLnet wants exactly this kind of first-person continuity, not a CV. Structure it as: *origin → what sustained it → what solo maintenance has cost you → why that's the actual bottleneck now.*

> I started ferrolink in 2019 [— insert your existing opening here]. Since then it has [insert real facts: adoption points, who's using it, notable deployments, stars/downloads if they exist, any dependents]. I have been the sole maintainer for [N] years — writing the protocol, the implementation, the documentation, triaging every issue, and reviewing every contribution, alongside [day job / other constraints]. That has been sustainable for keeping the project alive, but not for making it *rigorous*: [name the specific debt — e.g. no independent security review, thin test coverage on the radio layer, undocumented wire format, power profiling done ad hoc rather than systematically]. This grant is the difference between a project that works because I know where the bodies are buried, and one that other people can build on without me.

Fill the bracketed parts with what's actually true — this section is the one place where a reviewer is explicitly checking "is this person credible to do the work," so understatement reads better than any amount of polish.

### Explain what the project is about

Plain language, no jargon a non-specialist reviewer can't follow (NLnet's first-pass reviewers are often generalists; the domain experts see it in round two).

> Ferrolink lets devices form a resilient network without cellular towers, ISPs, or centralized infrastructure, using [your actual radio/transport layer — LoRa? sub-GHz? BLE? multi-radio?] to route messages hop by hop across nodes running on [battery / solar / coin-cell — state the actual power envelope, this is your headline differentiator given the grant title]. It's used for [real use cases: disaster response comms, remote agricultural or environmental sensor networks, community networks in areas without carrier coverage — keep only the ones that are true]. The stack is MIT-licensed so it can be embedded in both open and commercial hardware without license friction.

### Explain what the project does NOT do

Reviewers use this to sanity-check scope creep — a tight answer here is a credibility signal, not a weakness.

> Ferrolink does not provide internet connectivity or gatewaying to the wider internet [unless it does — adjust]. It is not a hardware product — we do not design or sell radios or devices. It does not include [mobile app / UI layer — state if out of scope]. This grant does not fund new protocol features; it funds hardening the existing one: security, robustness, and testability of what's already deployed.

### Ecosystem — target users, existing/competing efforts, and how ferrolink differs

This is one of the most heavily weighted fields — NLnet explicitly avoids funding duplicated effort, so name real alternatives and be precise about the axis of difference (license, power envelope, target hardware, deployment model — not vibes).

> The closest comparable projects are Meshtastic (LoRa mesh, GPL-licensed, oriented toward consumer off-grid messaging on commodity dev boards), Reticulum/RNS (transport-agnostic mesh networking stack, MIT-licensed but general-purpose rather than power-budget-first), and B.A.T.M.A.N./Yggdrasil/cjdns (mesh routing overlays, generally assuming always-on, mains- or battery-rich nodes rather than [your actual constraint — e.g. coin-cell, multi-month deployments]). Ferrolink differs on [pick the true ones]: (1) license — MIT rather than GPL, which matters for [embedding in commercial or closed products / avoiding copyleft friction for integrators]; (2) power model — [specific numbers: duty cycle, sleep current, expected battery life under X traffic load]; (3) footprint — runs on [specific constrained hardware / RAM-KB envelope] where [comparable project] requires [more capable hardware]. Target users are [community network operators / disaster-response NGOs / environmental sensing researchers — be specific, name any real deployments if you have them].

### Significant technical challenges you expect to solve

This is the section that actually justifies "hardening," not new features — lean into it.

> - **Security review**: the wire protocol and node-authentication scheme have never had independent scrutiny. [If you know the gaps: e.g. no replay protection, no formal threat model against a hostile relaying node, key management is ad hoc.]
> - **Fault tolerance under real network churn**: nodes joining/leaving, partitions, and lossy links are handled by [current approach], which has known failure modes under [specific condition].
> - **Power-budget correctness**: [current duty-cycling/sleep strategy] has been tuned empirically rather than verified; needs systematic profiling across [radio hardware variants].
> - **Test infrastructure**: currently [manual / minimal], with no fuzzing of the parser and no hardware-in-the-loop CI, which is the main reason regressions land undetected.
> - **Interoperability / spec clarity**: the wire format is documented only in the implementation itself, blocking independent reimplementations.

Keep only the ones that are real — a shorter, true list beats a padded one.

### Workplan — milestones and deliverables (12 months, €48,000)

NLnet wants a plan with verifiable, dated deliverables, not a prose paragraph about "iterating." Six bi-monthly milestones matches their expected granularity for a one-year individual grant:

| Milestone | Months | Deliverable |
|---|---|---|
| M1 | 1–2 | Formal wire-format spec published; threat model document |
| M2 | 3–4 | Test harness + CI with hardware-in-the-loop coverage on core routing paths |
| M3 | 5–6 | Fuzzing of the parser/protocol layer; fixes for issues found |
| M4 | 7–8 | Power-consumption audit and duty-cycle rework, with measured before/after figures |
| M5 | 9–10 | Independent third-party security review, remediation of findings |
| M6 | 11–12 | Stable versioned release, updated docs, interoperability guide for reimplementers |

Adjust the technical content to match your actual codebase, but keep the shape: each milestone should end in an artifact a reviewer can point at (a report, a tagged release, a published doc), not a vague "improved X."

### Detailed budget — how the €48,000 will be spent

> - Core development and hardening work: ~1,650 hours at €25/hour (a modest self-employed rate for Portugal) ≈ €41,250, covering M1, M2, M3, M4, M6.
> - Independent security audit (M5): €5,000–6,000, engaging a third-party firm.
> - Test hardware (radio modules, dev boards across the target hardware range): €1,000–1,500.
> - Contingency: remainder.

One thing worth checking directly with NLnet rather than assuming: they've historically been able to **facilitate a security audit through their own network of partner firms outside the grant budget**, at no cost to you. If that's still current, you could shrink the audit line and redirect that money to development hours — ask this in your application or in a pre-submission email to NLnet's team, don't just assume it.

### Requested amount — one-line justification

> €48,000, covering approximately a year of substantially full-time work at a modest self-employed rate, plus a small hardware and third-party audit budget, structured around the milestone plan above.

---

**Before you submit:**
- Cut anything that reads like pitch-deck language ("revolutionary," "game-changing") — NLnet's reviewer culture is technical and allergic to hype; plain, falsifiable claims outperform enthusiasm.
- Every claim about current state (adoption, test coverage, power figures) should be something you could show evidence for if asked — don't round up.
- If this round doesn't land, NLnet gives feedback and lets you reapply next quarter — treat a first "no" as notes, not a dead end.