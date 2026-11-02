Here's the completed submission, ready to paste into each field:

---

**Title** (75/100 chars)

From a 40-Minute Wait to 6: Rebuilding CI Queue Scheduling Across 210 Repos

---

**Abstract** (~1,290/1,500 chars)

Our CI queue had a 40-minute median wait time across 210 repositories. Engineers gave up on pre-merge checks and started batching commits just to avoid it. This talk covers how we cut that median to 6 minutes without buying our way out with more hardware.

We'll walk through the diagnosis: instrumenting the scheduler and finding the real bottleneck wasn't runner capacity, but a first-in-first-out queue that let a handful of monorepo-scale jobs starve hundreds of small ones. Then the fixes: priority-aware scheduling weighted by job duration and repo size, runner pools that scale with queue depth instead of fixed reservations, splitting slow test suites so short jobs stop waiting behind long ones, and a feedback loop that catches queue-health regressions before they become incidents.

You'll leave with a concrete playbook: how to instrument CI to find your actual bottleneck instead of guessing, which changes gave the biggest wins for the least effort, what we tried that made things worse, and how we rolled the new scheduler out across 210 independently-owned repos without a mass migration freeze.

A practical, numbers-driven talk for anyone running CI at scale — the infrastructure work that rarely gets stage time but decides how fast every engineer in the company ships.

---

**Outline**

Our CI queue had a 40-minute median wait time across 210 repositories. Engineers gave up on pre-merge checks and started batching commits just to avoid it. This talk covers how we cut that median to 6 minutes without buying our way out with more hardware.

We'll walk through the diagnosis: instrumenting the scheduler and finding the real bottleneck wasn't runner capacity, but a first-in-first-out queue that let a handful of monorepo-scale jobs starve hundreds of small ones. Then the fixes: priority-aware scheduling weighted by job duration and repo size, runner pools that scale with queue depth instead of fixed reservations, splitting slow test suites so short jobs stop waiting behind long ones, and a feedback loop that catches queue-health regressions before they become incidents.

You'll leave with a concrete playbook: how to instrument CI to find your actual bottleneck instead of guessing, which changes gave the biggest wins for the least effort, what we tried that made things worse, and how we rolled the new scheduler out across 210 independently-owned repos without a mass migration freeze.

A practical, numbers-driven talk for anyone running CI at scale — the infrastructure work that rarely gets stage time but decides how fast every engineer in the company ships.

---

**Audience level**

Intermediate (adjust to match this form's exact dropdown wording — this isn't a talk for people new to CI, but it's also not a deep-dive requiring specialist infra background).

---

**Track**

The Future of Engineering

---

⚠️ Two calls worth a second look before you submit, both already decided by you, flagging once and moving on:

- **Track fit**: reviewers usually score submissions partly on track fit. A CI-scheduler war story reads as textbook "Platform & Infrastructure" — "Future of Engineering" tends to draw forward-looking/industry-trend talks. Prestige of the track name doesn't help if the review committee scores it as a mismatch. Your call stands as submitted above.
- **Outline = abstract**: some committees use the outline specifically to check you have real time-boxed structure (not just restated content) before accepting. Low risk here, just flagging why some CFPs ding this.