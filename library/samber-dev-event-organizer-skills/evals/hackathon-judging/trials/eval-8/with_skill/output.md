# Quillmark Hack rules page: sponsor centrality and criteria weights

I ran this against the hackathon-judging skill. The skill's interview didn't happen, so I made three assumptions. I flag each one at the end.

## 1. Decision on weights

**Publish the criterion names and the full elimination list. Keep the percentages internal.**

- Disclosure fails when a team enters without knowing what is judged. Named criteria plus a complete knockout list prevent that.
- Withholding the numbers is a legitimate anti-gaming choice. It stops teams tuning to a decimal against a figure they never earned.
- Tell the Discord person this: the weights are fixed in writing before submissions open, they won't change, and if a result is challenged the answer names which criterion decided it.
- Publish the tie-break ladder. Rung 1 breaks ties on the highest-weighted criterion, which reveals that criterion's name but no numbers. I'd accept that leak. A tie-break invented at the podium is worse. The alternative is to open the ladder with a different rung, but then your weights stop doing the tie-breaking.

## 2. Sponsor centrality: three layers

You can't make a bolt-on literally impossible. You can make it fail a test a judge can run in the slot. Use a gate, a ladder and an observable proof step. Keep the gate separate from the rubric, because a knockout folded into a score reads as merely low-scoring.

### Layer A: elimination gate (yes/no)

A gate is only as strong as its definition of "central". Define it as a test, not as the word "meaningful".

### Layer B: ladder inside the sponsor criterion (degree)

Only entries that pass the gate get scored here.

| Rung | Delta |
|---|---|
| Call works, but a hardcoded value or another provider would give the same result | -5 |
| One endpoint feeds one secondary feature | 0 |
| The core user flow depends on the API, across more than one endpoint | +5 |
| The product's main value comes from capabilities specific to the sponsor's API | +8 |

Normalize ladder totals across the track's cohort to the 1-5 scale with `(score - min) / (max - min) × 4 + 1`. Raw ladder totals can go negative and look arbitrary, so teams and the sponsor see only the normalized figure.

### Layer C: make it observable in the slot

- Add a required submission field: "Which feature stops working if the Quillmark API is removed, and where in the code?" Judges then verify a claim instead of hunting for it.
- At live tables, the judge may ask the team to disconnect or revoke the API key and re-run the flow.

## 3. Rules page text, ready to paste

> ### How projects are judged
>
> Every project is scored on these criteria: **[criterion 1 – your brief's exact wording]**, **[criterion 2]**, **[criterion 3]**, and **[criterion 4]**. The criteria are not equally weighted. The weights are fixed before submissions open and will not change.
>
> ### Quillmark track: the API must be central
>
> To compete in the Quillmark track, your project must pass the **removal test**: take the Quillmark API away, or replace it with a stub, and a core feature a user would notice must stop working.
>
> A project is **removed from the Quillmark track** if any of these is true:
> - Removing the API changes nothing a user can see.
> - The API is called once, at startup or in the background, and its result is logged, displayed as decoration, or ignored.
> - The call could be replaced by a hardcoded value or another provider with the same result.
>
> A removed project stays eligible for the general prizes.
>
> **How we check.** Your submission must name the feature that depends on the API and where it lives in the code. At the judging table, a judge may ask you to disconnect the API key and run that feature again. *(Keep that sentence only if judging is live. For video-only judging, ask for a recorded run with the key revoked.)*
>
> The track score then rewards depth of use, not just presence.
>
> ### Other disqualifications
> *[Your event's other knockout rules, for example no public code where the checklist requires it, or a design file with no working build.]*
>
> ### Ties
> Ties are broken in this order, stopping at the first rung that separates the teams:
> 1. Highest score on **[name of your top criterion]**.
> 2. The project that most judges ranked first among the teams they saw.
> 3. A named tie-break judge, **[name/role]**, decides on the record in one sentence.
> 4. *[Include only if the prize is divisible.]* The prize is split.
>
> ### Challenging a result
> Send challenges to **[named role, not "the organizers"]** within **[window, closing before prizes are paid]** of the announcement. We can correct an arithmetic error, a missed submission or an eligibility fact. We cannot change a judge's opinion. The answer will cite the criteria and name the one that decided the result. It will not give individual judges' scores.
>
> ### Sponsor judges
> *[If the Quillmark contract puts their representative on the Quillmark track, say so here: they judge that track only, alongside at least one neutral judge, and not the overall prizes. Disclosing this before submissions close makes it a rule teams entered under. Disclosing it after the ceremony makes it a scandal.]*

## 4. Internal notes (not for the page)

- **Sponsor-track weight.** Put real weight on "use of Quillmark" in the track total and zero in the general total. For a starting point, the skill's worked example uses 30% on the track and 0% on the general track. Debate it, don't adopt it blindly. A project can win the track and place nowhere overall. Tell the sponsor before the event that this is the design working.
- **Last year's second place.** Under this design a single-call entry fails the gate and never reaches the ladder. A borderline entry lands on the -5 rung and falls behind. Timing doesn't matter. A late integration is fine if it is truly central, and the test is function, not commit time.
- **Judge brief.** Add the removal test as an explicit prompt for the sponsor representative. Otherwise their enthusiasm for their own API bleeds into their other scores.
- **Drop-test.** Run the track ranking with and without the sponsor judge's scores. If the winner changes, tell the sponsor before the ceremony.

## 5. Assumptions to confirm

1. **Format.** I assumed live judging at tables, where the key-revoke step works. If it is video-only, use the recorded variant.
2. **Gate scope.** I scoped the gate to removal from the Quillmark track, not disqualification from the event. The general rubric gives the sponsor's tech zero weight, so a full DQ would be unfair. Say if you want it harsher.
3. **Contract.** I don't know whether the sponsor contract requires their representative to judge the track.

I can also draft the judge brief and the allocation arithmetic if you give me your team count, judge count and judging-window minutes.