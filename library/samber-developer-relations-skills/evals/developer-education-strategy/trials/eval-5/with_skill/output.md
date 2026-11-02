# Developer education charter — Halcyon Learn, Q4 2026 measurement plan

Built using `developer-education-strategy`. This is retroactive: the program already shipped, so the interview and tier-selection steps are compressed into stated assumptions — flagged below — instead of a multi-turn Q&A. Confirm or correct the flagged ones before you present this.

## 1. Gate verdict

Education passed the evidence gate on paper (a streaming-data platform has real sequential concepts to learn), but you have never actually tested that verdict — you have Reaction and Learning data (rating, pass rate) and zero Behavior or Results data. That's not a failed program; it's an **unmeasured** one. The CFO didn't get nothing because the course failed — they got nothing because levels 3 and 4 were never wired up, and by design, they can't be reconstructed for these 640 people now (see §8). The fix for Q4 is instrumentation, not more modules.

## 2. Audience and motion

⚠️ Open question, not stated in your prompt: is Halcyon Learn aimed at **prospects** evaluating the platform pre-signup, or **activated users** you're trying to retain/expand? The "no login, don't hurt signups" design implies a top-of-funnel, bottom-up motion — I'll assume that below, but it changes what "Results" means:

- Prospect-funnel motion → Results = signup / trial-to-paid conversion.
- Activated-user motion → Results = expansion, retention, support-cost reduction.

Design the plan to catch both (below) and let the first real cohort tell you which signal is bigger; don't guess it away now.

## 3. Chosen tier — no change recommended

Eight sequenced modules with graded quizzes is rung "structured curriculum" territory, minus confirmed hands-on labs (not mentioned — if there are none, that's worth knowing, since labs are what actually move competence rather than recall). Rejected for now: badge/certification promotion — no named external consumer (no buyer or partner counting certified heads) has asked for one. Don't let the CFO's question push you into certification; it wouldn't answer it. It would add a permanent recertification obligation without adding a single new data point about business impact.

## 4. Competency map

Out of scope for this exercise — not what was asked, and retrofitting a job-task-analysis-derived map onto an already-shipped curriculum is a separate piece of work. Flag if you want it done before Q1 module revisions.

## 5. Credential decision — add one lightweight instrument, not a real credential

Recommend a **free, optional, non-blocking completion certificate**, offered only after someone finishes a module or the full path. Its job is not procurement currency (no named consumer for that yet) — its job is to be the one moment you can ask, "want an email to send this to, or to save your progress?" without gating anything upstream of it. This is the mechanism that solves §8's identity-join problem while keeping your "don't hurt signups" constraint intact: access, quizzes, and the rating prompt all stay fully open; only the optional certificate touches identity, and it never blocks.

Side benefit: a shareable certificate is itself a soft top-of-funnel play (people post it, it references Halcyon Learn) — but don't sell it internally on that basis, sell it on the instrumentation it unlocks.

## 6. Operating model

⚠️ Not specified — you'll need to fill in: named owner (not "DevRel," a person, with weekly hours), who maintains the eight modules against product changes, and what platform hosts them (matters for whether an opt-in email capture is even a small lift or a rebuild). Refresh trigger should bind to your release cadence, not a calendar — state it once you know how often streaming-platform APIs/UI referenced in the modules change.

## 7. Budget shape

The eight modules are sunk cost — don't let them anchor the Q4 decision. The incremental ask for Q4 is small and mostly one-time: wiring an optional email capture + certificate issuance, tagging per-module analytics events, and getting analytics/data eng to build one matched-cohort query. Recurring cost after that is mostly a quarterly reporting cadence, not new engineering.

## 8. Measurement plan — the part you actually asked for

Design backwards from Results, per Kirkpatrick. You already have levels 1–2; you're missing 3–4, and that's specifically what the CFO was asking about.

**Level 1 — Reaction.** ✅ You have the aggregate (4.6/5, 640 enrolled). Missing: per-module completion/drop-off — you can't tell which of the eight modules is losing people. Instrument this in Q4; it's cheap (page/event analytics, no identity needed) and it's the fastest fix to a real content problem if one exists.

**Level 2 — Learning.** ✅ 82% pass rate is a healthy number — not suspiciously near 100% (which would mean the quizzes don't discriminate) nor collapsed near 0% (which would mean a broken quiz, not weak learners). Add item-level failure clustering: which specific questions fail most, across which module. That's a real, cheap signal for what to fix in the content itself, and it's something concrete to bring to the QBR even before behavior data exists.

**Level 3 — Behavior.** ⚠️ This is the gap, and it's the one the CFO's question actually lives in. Kirkpatrick Partners' own definition matters here: behavior is "performing critical behaviors in the environment **and being supported in and accountable for** that performance" — so if this program is aimed at prospects who haven't signed up yet, there's no "environment" for them to apply anything in yet, and Level 3 for that segment folds into Level 4 (did they convert and then behave like an activated user). For anyone who *is* a signed-up user, primary metric: **rate of production usage tied to what the modules teach (e.g., building a working pipeline, configuring a connector — swap in your actual module topics), 30/90 days after completion, for opted-in completers vs. a matched control group of similar accounts who didn't take the course.** First cohort sets the baseline; there is no external number to benchmark against.

**Level 4 — Results.** ⚠️ Also missing, also gated on the same identity join. Primary metric — pick one based on §2's answer:

- Prospect motion: trial-to-paid conversion rate, opted-in completers vs. matched non-completers.
- Activated-user motion: support ticket rate on covered topics, and/or usage-driven expansion, opted-in completers vs. matched non-completers.

**Identity join (the actual unlock):** opted-in email from the §5 certificate → your product/marketing analytics account ID → the matched-cohort comparisons above. This only covers people who complete a module *after* the certificate ships — it cannot be applied retroactively.

**What you cannot measure this year:** Behavior and Results for the 640 people already enrolled. They learned anonymously, by design, and that can't be un-done after the fact. Say this explicitly at the QBR rather than let it surface as a gap someone else finds — "we deliberately kept it anonymous to protect signups; that traded away individual attribution for the first cohort; here's the plan starting with cohort two" is a defensible answer. A vague retroactive estimate isn't.

**Don't chase a dollar ROI number yet.** The CFO's question sounds like it wants Phillips' Level 5 (ROI), but computing one without validated Level 4 data is inventing a number, not measuring one. Get one clean Level 4 signal first (e.g., "completers convert at X% vs Y% for matched non-completers"); ROI is a follow-on calculation once that exists, not a Q4 deliverable.

## 9. Kill rule

Two separate rules — don't let a broken instrument masquerade as a proven-worthless program:

- **Instrumentation health check, at the Q4 review date:** if fewer than ~50 completers have opted into the certificate by then, the capture mechanism itself is the problem — fix that before drawing any behavior/results conclusion from the data. (50 is a baseline I set for a program this size; replace it once you know your realistic completer volume per quarter.)
- **Program kill rule, reviewed at the following quarter (assuming the instrument is healthy):** if the opted-in-completer cohort shows no visible difference from its matched control on the Level 3/4 metric chosen in §8, stop authoring new modules, keep the existing eight on maintenance only, and reopen the gate in §1 with that evidence.

## 10. First 90 days

- Weeks 1–2: ship the optional certificate + email capture (must not add friction to existing access); instrument per-module completion events.
- Weeks 2–4: with analytics/data, define the matched-control methodology (tenure, plan/segment, no-course) for whichever motion §2 resolves to.
- Weeks 4–8: tag support tickets by topic against the eight modules; start tracking the chosen Level 3 product-usage signal for anyone who opts in.
- Weeks 8–12: first read on cohort-two data (small n, say so); item-level quiz failure clustering delivered as a concrete Level 2 finding regardless of cohort-two volume.
- End of Q4: bring the CFO Levels 1–2 solid, Level 3/4 as "instrumented and running, first real read in Q1," and the explicit "here's what we can't recover from cohort one, and why" line from §8.

## 11. Where each number came from

- 640 enrolled, 4.6/5 rating, 82% quiz pass rate — sourced from you, as reported 2026-09-20.
- 50-completer opt-in threshold, the "15-point drop-off gap" framing, the "<60% first-attempt item" flag — this charter's own baselines, not benchmarks; replace with your own once real per-module and per-item data exists.
- Kirkpatrick's four levels and the Level 3 "supported and accountable" definition — Kirkpatrick Partners, cited as published, not invented for this charter.
- Everything under §2 (audience/motion) and §6 (owner, platform, refresh cadence) — unresolved; flagged, not assumed.