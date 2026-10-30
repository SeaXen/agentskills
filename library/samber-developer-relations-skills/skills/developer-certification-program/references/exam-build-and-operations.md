# Exam build and operations

Read when sizing the build (workflow step 5) and when setting the fee. Every hour figure you produce here is your own estimate: label it self-set.

## Contents

- Item and task lifecycle
- Sizing the build
- Cost per certified holder
- Issuing and verification: build or buy
- Hosted environments
- Delivery logistics checklist
- Leak and incident runbook

## Item and task lifecycle

Most of a credentialing team's work sits between the blueprint and the cut score:

1. **Write.** Item writers or task authors trained on the blueprint and a style guide; each item or task traces to one blueprint task.
2. **Review.** Technical accuracy by a second expert, plus a bias and clarity review (plain language for non-native speakers, no culture-specific references).
3. **Pilot.** Run a beta exam or seed unscored items into live forms; never score an item that has not been piloted. Below a few dozen pilot candidates, use the pilot for clarity and checker correctness only, and defer item statistics until live volume accrues.
4. **Analyse.** Per item: difficulty (share passing), discrimination (do strong candidates pass it more than weak ones), and, for multi-language exams, whether one language group fails it unusually. Per form: reliability and pass/fail consistency.
5. **Set the standard.** Run the panel once the blueprint and pilot data exist (see assessment-integrity.md).
6. **Equate and assemble forms.** Anchor items or a calibrated scale keep forms of unequal difficulty under one pass mark.
7. **Monitor.** Item exposure, pass-rate drift, candidate comments; retire or rewrite items that drift.
8. **Re-align.** Per release, re-run checkers and review items the release touched; per blueprint change, return to step 1.

For auto-graded tasks, the checker is the item: version it, test it in CI against each product release, and keep a reference solution that must pass.

## Sizing the build

Turn the blueprint into hours before choosing a design:

| Line | Unit | Driver |
|---|---|---|
| Tasks or items | per domain, times variants for rotation | blueprint weights, rotation need |
| Authoring and review | hours per task or item | complexity; reviewers' time counts |
| Environments and checkers | per task | disposable tenant, seeded data, end-state checks |
| Pilot | one cohort | recruit candidates, analyse results |
| Standard setting | one panel session per blueprint | panel size, preparation |
| Issuing and verification | one-off setup plus per-holder | build or buy (below) |
| Candidate agreement, accommodations, privacy review | one-off | legal and privacy owners' time |
| Per-release re-alignment | hours per release | release cadence, share of tasks touched |

Compare the total with the effort ceiling. When it does not fit, cut variants, domains or the tier, never the pilot or the review.

## Cost per certified holder

Keep every term yearly:

```
yearly fixed     = build cost / credential version life in years
cost per attempt = per-sitting cost (delivery, proctoring, hosting, payment, no-shows)

break-even fee per attempt = (yearly fixed + yearly operating) / expected attempts per year
                             + cost per attempt
                             - amount a partner program or contract absorbs

cost per holder (reporting only) = (yearly fixed + yearly operating
                                    + cost per attempt x attempts per year) / holders per year
```

- Build cost: authoring, environments, pilot, standard setting, issuing setup.
- Yearly operating: re-alignment hours, item refresh, appeals, support, issuing-service fees.
- Charge the fee per attempt, so failed attempts pay their own sitting cost; never set the fee equal to cost per holder, which recovers failed attempts twice.
- Vouchers lower revenue per attempt without lowering cost: model them as their own line.

## Issuing and verification: build or buy

- **Buy** a credential-issuing service when the team is small: it handles signing, Open Badges export, verification pages, wallet and profile sharing. Check data residency and export of all records if you leave the service.
- **Build** only when the platform already runs identity and signing infrastructure, or volume makes per-credential fees dominant.
- Either way, keep the master record of holders, versions and status in a system you own.

## Hosted environments

- One disposable tenant per sitting, created on demand, destroyed after grading.
- Cap compute, network egress and lifetime per tenant; free sittings attract people who want free compute.
- Require a verified account and cap attempts per window.
- Seed deterministic data so the checker's expected end state is stable.

## Delivery logistics checklist

- Exam languages, and extra time for candidates sitting in a non-native language.
- Countries where delivery or payment is legally restricted (sanctions and export controls).
- Credential name and logo usage rules for holders; avoid protected titles ("engineer" is a regulated title in some jurisdictions, such as Canadian provinces).
- Candidate handbook: booking, rescheduling, identity, conduct, AI policy, results, appeals, accommodations.
- Per-domain score report for failed candidates, so a retake is targeted.
- Accessibility of lab environments: screen readers in browser terminals, keyboard-only navigation, colour contrast.

## Leak and incident runbook

1. Detect: pass-rate jump on a form or item, dump site found, proxy sitting reported.
2. Contain: pull affected items or forms, switch to reserve forms.
3. Investigate: item exposure data, sitting recordings where held, candidate statements.
4. Decide: revocation per the candidate agreement, with appeal.
5. Recover: write replacement items, re-equate, file takedown requests.
6. Record what changed so the next leak is caught sooner.
