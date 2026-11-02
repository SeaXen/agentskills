**Do this first (about 3 hours this week):** email 15 clients who found a consultant through the directory, and survey the 400 consultants. Ask "Did a client ask for a certification, and what did they plan to do with the answer?" Decision 1 below depends on the replies.

I made the calls myself and listed my assumptions where I had to. Numbers marked **[own]** are my baselines. Numbers marked **[src]** come from the education skill's reference notes, which I did not re-verify online.

# Lumenshift certification charter

## 1. Gate verdict

Competence is a real gap, but demand is only anecdotal. Consultants say clients ask "are you certified?", yet no tender names it and no buyer counts certified heads. So this is a signal problem before it is a psychometrics problem. The cheapest fix that works is a verifiable credential shown in the directory clients already use. A proctored, procurement-grade certification is not justified yet.

## 2. Audience and motion

- **Learner:** freelancers (400) and small IT firms (30).
- **Consumer:** the client choosing a partner. Our own "Find a partner" directory is the one place we control how that client sees a credential.
- **Motion:** partner-quality and trust signal, not a funnel. Individuals pay for a signal their clients can read.

## 3. Tier and rejected alternatives

I split "both exam-based, six months" into three parts.

**Professional** launches at month 6 as a performance exam: a 2-hour hands-on lab in a disposable environment, auto-graded. This is the skill-badge rung, and it is cheap to grade and hard to cheat. I rejected multiple-choice because it is easy to cheat, and "pass" would be indefensible to a client.

**Expert** is the headline, and it launches at month 6 through a **Founding Expert route**: application, portfolio of 2 referenceable production projects, a human-graded scenario, and a panel interview. The cap is about 25 people **[own]**. The full Expert exam follows at about month 14, once the founding cohort has done the standard-setting study. I rejected a day-one Expert exam for three reasons:
- Human-graded practicals need reviewers, and 10 hours a week cannot cover them.
- A cut score set without experts is not defensible, and Expert's reputation is the whole point.
- Setting it needs 5–15 experts **[src]**, and the founding cohort is exactly that panel.

**Curated learning path** goes up in week 3 and stays free. It reuses existing docs in an ordered path. I gate the credential, not the knowledge.

Rungs deleted:
- Ad-hoc content, which is not a program.
- Full proctored certification with partner trainers, until the triggers in section 9 fire.
- Localization, until one locale proves demand.

**If the CEO insists on two exams at month 6:** budget a part-time exam operator and a paid grading panel. Expect Expert to launch with a provisional cut score, and say so publicly.

## 4. Competency map

These are hypotheses until the job task analysis (weeks 1–3) confirms them. Every module must trace to a real task. If more than 20% of modules fail the trace, restart **[own]**.

**Professional:**
1. Build and deploy a standard workflow.
2. Configure connectors and data mapping.
3. Set permissions and roles.
4. Debug a failing run.
5. Upgrade within the supported window.

**Expert**, which includes all of the above plus:
1. Architect multi-team solutions.
2. Handle scale and performance.
3. Design for security and governance.
4. Migrate across major versions.
5. Fix a broken production system.
6. Scope work with a client.

**Source of the analysis:** interviews with 12–15 of the consultants clients fight over, 5–8 firms, and support-ticket clusters. Do not build it from the feature list.

## 5. Credential decision

The consumer is the client, through the directory. The mechanics:
- Every credential gets a public verification URL.
- The directory gets a "Certified" filter.
- A firm badge requires at least 2 Professionals **[own]**.
- Ship a one-page "what this credential proves" sheet that a client can paste into a tender.

**Validity** matches the two-year support window. Each credential names the major version it was earned on, for example "Professional v7".
- **Renewal** is a short lab on the current version, free of charge. This follows Microsoft's free-renewal model; Microsoft renews yearly, AWS every 3 years, CKA every 2 years **[src]**. These models disagree, so mine is a choice and not an industry norm.
- **Expiry** is 2 years, with at most 2 concurrent exam versions.
- **Exam refresh** happens within 8 weeks of each major release. CKA realigns within about 4–8 weeks **[src]**.

**Cut score:**
- **Professional:** beta data plus a 5–8 SME modified Angoff panel **[src for method, own for panel size]**, marked provisional for the first 6 months.
- **Expert:** a full standard-setting study at month 12–14.

**Fraud and privacy:**
- **Lab design:** randomized lab parameters, a 14-day retake wait **[own]**, and no leaked fixed answers.
- **Expert panel:** graders recuse themselves from their own firm and from direct competitors, and grading is blind where possible. Founding Experts are competitors, so this matters.
- **Identity:** I avoided biometric proctoring. If you are EU-based, check the privacy rules with legal before adding any.

## 6. Operating model

**Owner:** you, 10 hours a week, with the named successor as shadow reviewer from month 3.

**Weekly split after launch**, which assumes lab and platform upkeep is contracted, not done by you:
- 3 hours on exam and refresh coordination.
- 2 hours on appeals and grading oversight.
- 2 hours on metrics and the directory.
- 3 hours of buffer.

**The honest staffing gap:** 10 hours a week is about 520 hours a year, which cannot also build the labs. Spend budget on:
- A contract lab and item author for the build.
- A part-time exam operator, about 6–8 hours a week.
- Paid SME graders.

**Platform:**
- **Content and labs:** a repository you own.
- **Lab environment:** a disposable instance of the product.
- **Credential registry:** your own verification page, or a hosted one if cheaper.

Do not let courseware live only in a hosted tool. Katacoda shut down on 15 June 2022 **[src]**.

**Refresh trigger:** the annual major release. Labs break when the product ships, so budget a lab regression run in the release checklist. Video ages fastest, so avoid it until the curriculum is stable.

**Pricing:**
- **Path:** free.
- **Professional exam:** paid, with the price set from lab hosting and grading cost per attempt. The price must filter casual attempts without pricing out freelancers.
- **Founding Expert:** free, by application.
- **Renewal:** free.

## 7. Budget shape

You gave no total, so these are shares **[own]**, weighted to year 1:
- 40% contract lab, item and curriculum build.
- 20% lab hosting and the credential registry.
- 20% SME panel and graders.
- 20% reserve.

In year 2, shift most of the build share to the annual refresh and the Expert exam build. Budget the annual refresh as a permanent line item.

## 8. Measurement

Capture a pre-launch baseline now, because you cannot rebuild it later.

**Reaction and learning:**
- Beta survey results.
- Pass rates by section.
- Item discrimination (does each task separate strong from weak candidates?).

**Behavior:**
- Join credential holders to product usage by account ID. Decide this join now, because it cannot be rebuilt later.
- Compare production deployments and support tickets per holder against non-holders. Selection bias is a risk, since stronger consultants certify first.

**Results:**
- Directory contact-to-engagement rate for certified versus uncertified listings, measured against today's baseline.
- Partner retention.
- Clients per certified firm.

## 9. Kill and escalation rules

**Escalate to full proctored certification only when all three hold:**
1. A named buyer or tender counts certified heads.
2. Year-2 recertification is funded.
3. One person owns the item bank indefinitely.

**Kill review, 12 months after launch.** Freeze new development if both of these hold **[own]**:
- Fewer than 60 Professional holders (15% of 400).
- Certified listings do not beat uncertified ones on directory contact rate by at least 20%.

Existing credentials stay valid until expiry, and you publish the retirement.

## 10. First 90 days

**Weeks 1–3, evidence and analysis:**
1. Run the client and consultant survey.
2. Run the job task analysis.
3. Build the curated path from existing docs.
4. Make a go/no-go call with the CEO on the evidence.

**Weeks 4–13, build:**
1. Write the blueprint and the lab environment spec.
2. Recruit the contract author and the SME panel.
3. Draft Professional labs.
4. Open Founding Expert applications.

The successor shadows from week 6.

## 11. Where the numbers came from

**Sourced:** CKA's 2-hour, 2-year, 4–8 week realignment, AWS's 3 years, Microsoft's 1-year free renewal, the 5–15 expert panel for modified Angoff, and the Katacoda shutdown date.

**My own baselines:** everything else with **[own]**, plus the 25-person cap, the 2-Professional firm threshold, the 20% failed-trace rule, the 14-day retake wait, the 12-month kill thresholds, and every budget share. Replace them with numbers from your first cohort.

## What I need from you

1. Ask the CEO whether a Founding Expert launch counts as "Expert at month 6". This is the biggest risk to the plan.
2. Tell me the total budget, so I can turn the shares into amounts.
3. Tell me where your learners are based. EU or not changes the identity and privacy checks.

**Next step:** send the survey in the first action above. I can draft both emails if you want.