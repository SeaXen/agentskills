# Ashgrove Data — developer/partner education review

## Scope check

This is partner/SI enablement — external audience, delivery-quality problem. In scope for `developer-education-strategy`, not for `devrel-strategy` (I'm not redesigning DevRel) or `developer-tutorial` (not writing lessons).

## 1. Gate verdict

**Conditionally yes, and not proven yet.** 3 of 6 contracted SI partners shipped implementations that failed your own architecture review last quarter — that's a real competence signal, not noise, at this sample size (50%).

⚠️ But you haven't ruled out the cheaper alternative. "Failed architecture review after shipping" tells me the review happens *after* build, not before. Before committing to a program, check two things:

- Did the 3 failing partners actually read the current, correct architecture docs before building — or did they skip/misread them? If the latter, this is partly a docs-findability or process problem, not (only) a competence gap.
- Is there a pre-build design sign-off today? If not, add one now — it's a week of process change, it catches the same failures earlier, and it's cheap regardless of whether you also build a curriculum.

If the 3 failures happened *despite* correct docs being read — same shape as "partners find the docs, follow them, and still design the wrong topology" — the gate passes cleanly: that's a competence gap, education is the right tool, and the checklist above becomes a complementary control, not a substitute.

## 2. What's wrong with the plan as written

Going through it claim by claim:

| Plan element | Problem |
|---|---|
| "Build everything inside a hosted interactive-lab SaaS" | Platform dependency. Katacoda's free public platform shut down 15 June 2022 after the O'Reilly acquisition; every vendor who'd embedded scenarios only there lost them that day. Host the *rendering* there if you like; keep lesson/lab source (Markdown, IaC configs) in a repo you own. |
| "DevRel team owns the program" | Team label, not an owner. The reference failure mode is the *orphan academy* — launched by a project, owned by nobody, stale within two releases. You need one named person accountable for curriculum truth, with stated weekly hours. Also worth asking whether DevRel is even the right home — DevRel usually doesn't know *why* the 3 implementations failed review; Solutions Architecture / Partner Engineering does. |
| "We review content regularly" | This is the template's own worked example of a weak refresh trigger, verbatim. Refresh has to bind to the *product's* release cadence, not a calendar habit — e.g. "re-align any module touching a changed architecture surface within N weeks of the release that changed it." |
| "Film video walkthroughs for all 14 modules" | Premature video, and the most expensive kind given a monthly release cadence. Video ages fastest and costs the most to redo — filming all 14 before the curriculum has run one cohort locks in content you don't yet know is stable. Also: are all 14 modules derived from what actually caused the 3 failures, or do they mirror the product's feature list? Unstated derivation is the *feature-tour curriculum* failure mode — every module should trace to a job task from the failure post-mortems; if more than ~20% don't, that's a restart signal, not a rounding error. |
| "Launch in English, German, Japanese on day one... covers our partner regions" | Premature localization, and it conflates HQ geography with actual language need. Each added language multiplies the refresh bill permanently. "Their region is X" is not demand evidence — check whether the partners' implementation *engineers* actually can't work in English before committing two extra locales you'll be re-cutting every release. |
| "Ship a minor release roughly monthly" | Not itself a hole, but it sets the real cost driver everyone above is ignoring: 14 filmed modules × 3 languages, re-aligned against a monthly cadence, is a standing production job, not a launch project. Size the operating model against this number before anything else. |
| No credential decision stated | Left undecided by default, which usually means someone escalates it later by ambition rather than evidence. Decide it now (see below). |
| No measurement plan, no kill rule | Absent entirely. A program without a kill rule survives on sunk cost regardless of whether it's working. |

The single biggest structural issue underneath all of this: **6 partners** is a very small population to be building a hosted SaaS platform, a 14-module video library, and trilingual content for. Check whether the cost per partner reached by this plan is actually smaller than just fixing the 3 accounts directly.

## 3. Tier recommendation

Candidates, in efficiency order:

1. **Curated learning path only** — rejected as the terminal state. If partners already read correct docs and still designed wrong, more curation of the same material won't move the failure rate; reading isn't producing competence. But run this in parallel, immediately, as a one-week bridge while the real fix is built — cheap, reversible, and it's the fastest way to test whether the failures really are competence, not findability.
2. **Structured curriculum with labs (recommended)** — modules derived from a job-task analysis of the 3 failed builds (plus interviews with the 3 that passed, to capture what "good" looks like), each with a graded lab in a disposable environment. This is the only rung that buys practice under observation, which is what "read the docs and still failed" is telling you that you're missing.
3. **Skill badges on the 2-3 highest-consequence competencies only** — not all 14 modules. External consumer: your own partner contract — tie badge counts to partner tier (e.g. a partner needs N badged engineers to keep/reach a given tier). That's a real, already-existing lever; you don't need a third party to make this consequential.
4. **Certification — rejected.** All three promotion conditions fail here: no named buyer or partner contract currently counts certified heads beyond the tier mechanism you can already build with a badge, no recertification budget is stated, and no one owns an item bank. Certification is the highest-value rung on paper and the least justified one for 6 known, contracted partners you already have direct leverage over. Escalation trigger, written as an observable condition: *a partner contract or a customer RFP requires an independently verifiable third-party credential, twice in one quarter.*

Rejected outright, not parked: ad-hoc-only (a partner already failed a review, so "no sequence, no completion state" doesn't meet the bar), and certification (above).

## 4. Competency map (how to build it, not the content itself)

1. Job task analysis from: review notes on the 3 failed implementations, interviews with those partners' engineers, and interviews with the 3 that passed (control group — what did they do differently).
2. Group into competencies, weighted by how often they show up in the failures, not by product surface area.
3. One graded lab per competency as the evidence.
4. Only then map to modules. Re-use whatever existing docs/tutorials already cover a competency correctly — don't re-author what's already true.
5. Pass threshold: every module traces to at least one task from the failure analysis. If more than ~20% of your 14 don't trace, that's this skill's own baseline for "restart from the job analysis," not a hard rule — but it's the check that catches a feature-tour curriculum before you film it.

I can't populate the actual competency list — that requires your review notes and partner interviews, not conversation content.

## 5. Credential decision

Skill badges (rung 4, not certification) on the 2-3 competencies most implicated in the failures. Issue on Open Badges (1EdTech's open, free, portable format) so partner engineers can carry it on their own profiles — the credential should live somewhere they own, not only in your LMS dashboard. No expiry in year one; revisit if the architecture model changes materially. External consumer: your partner-tier requirements, effective next contract cycle — decide with whoever owns partner contracts whether this is legally/commercially workable before promising it externally.

## 6. Operating model — fixed

- **Owner**: one named person, stated weekly hours — recommend someone from Solutions Architecture / Partner Engineering (the function that actually diagnosed the 3 failures), with DevRel co-resourcing production and partner comms. Not a team label either way.
- **Staffing**: authoring, technical review, lab maintenance, learner support — each estimated in hours/week, separately. Headcount ambition isn't staffing.
- **Platform**: hosted lab SaaS for execution is fine; lesson and lab source stays in a repo you own (Markdown + your IaC/config), so a vendor's terms change or shutdown doesn't take the program with it.
- **Refresh trigger**: bound to the *architecture-relevant* surface, not every monthly release — e.g. "re-align any module whose covered surface changed, within N weeks of that release; full curriculum review quarterly." Most monthly releases probably won't touch the 2-3 architecture fundamentals driving the failures; verify that before assuming every module needs monthly attention.
- **Pricing**: free to contracted partners — you're the one paying for the failures downstream.
- **Localization**: English only at launch. Add a language only once a specific partner segment demonstrates it can't operate in English — ask them directly rather than inferring from HQ country.
- **Video**: none at launch. Add it per-module only once that module has survived a cohort without a content change — video should follow stability, not precede it.
- **Partner delivery**: train-the-trainer for your larger partners once the curriculum has run at least one full cohort, not on day one.

## 7. Budget shape

Year-one build vs. year-two recurring, kept separate — recurring is the number that actually decides whether this program should exist. Given a monthly release cadence, the recurring load is dominated by lab maintenance and re-alignment, not authoring the first cohort. If you can't staff year two at that load, cut video and the two extra locales before cutting anything else — they're the two costs the current plan added without evidence, and they're the two that compound fastest against a monthly ship cadence.

## 8. Measurement plan

- **Reaction**: per-module drop-off.
- **Learning**: lab pass rate on graded exercises.
- **Behavior**: partner implementations passing your architecture review **first time** — this maps directly to your stated pain. Baseline is your own 3/6 last quarter; set the cohort-two target yourselves, don't borrow one.
- **Results**: rework/escalation volume on partner-shipped implementations post-training, and/or partner-competence objections in deals if that's also live.
- **Identity join**: partner engineer → lab account → architecture review record. Agree this with whoever runs the review process *before* launch — it can't be reconstructed after the fact.
- **Not measured this year**: revenue attribution — six partners is too small a population for a clean counterfactual.

## 9. Kill rule

State it as a number and a date before launch, e.g.: if first-time architecture-review pass rate hasn't improved past your baseline after two cohorts by a stated review date, stop authoring, keep the existing labs on maintenance, and reopen the gate with new evidence. (I'm not setting the actual number — that's yours to own so it isn't disputable later.)

## 10. First 90 days

1. Confirm the gate: check whether the 3 failed partners read the current docs correctly before building. Add the pre-build sign-off checkpoint regardless.
2. Run the job task analysis: post-mortems on the 3 failures + interviews with the 3 that passed.
3. Curate existing content into a one-week bridge path while the real curriculum is built.
4. Build and pilot one module + lab on the single highest-consequence competency, with one or two partners.
5. Decide badge mechanics with whoever owns partner contracts.
6. Only after cohort one: decide on video for that specific module, and re-open the localization question with actual partner input.

## 11. Where each number came from

- 3 of 6 partners, monthly release cadence — from you, this conversation.
- Katacoda shutdown (15 June 2022, post O'Reilly acquisition) — sourced, vendor's own history.
- Open Badges as free/open/portable (1EdTech, current spec v3.0) — sourced.
- 20% module-trace threshold, five-rung efficiency ordering, "defer localization until one locale proves demand" — this skill's own stated baselines, not industry standards.
- All targets above (cohort-two pass rate, kill-rule threshold, staffing hours) — deliberately left unset. Fill them with your own measured baseline once cohort one runs; don't let me hand you a number that becomes the standard you're held to.

## Open questions before this charter is final

1. Did the 3 failing partners read the *current, correct* architecture docs before building, or did they skip/misread something?
2. Which specific tasks caused the failures — is it consistent across all 3, or three different problems?
3. Do the German/Japanese-region partners' engineers actually need non-English material, or do they work in English day to day?
4. Who's the real named owner — DevRel, Solutions Architecture, or Partner Engineering — and what hours can they permanently commit?
5. Does a partner-tier mechanism already exist that a badge requirement could attach to?
6. What's forcing a fast timeline, if anything — a renewal, an SI contract cycle, a board review?
7. What does existing partner onboarding content look like today — is there already a curated path, or just flat docs?