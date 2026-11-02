❓ **Q1** - **Root cause of the 3 failures**: Did the 3 SI partners fail architecture review because of (a) a genuine knowledge/skills gap, (b) unclear or inconsistent review criteria on Ashgrove's side, (c) staffing turnover / wrong people assigned on the partner side, (d) incentive misalignment (rushed delivery to bill hours vs. get the design right), or (e) something else? A training program only fixes (a).

➡️ Pull the 3 failed-review write-ups and tag each with a root cause before designing any modules. Default assumption: it's a mix, not pure knowledge gap — pure training won't close (b)/(c)/(d).

---

❓ **Q2** - **Success metric**: What's the measurable target this program has to hit? Options: "0 of N SI-led designs fail architecture review next quarter," "≥90% certification completion within 60 days of assignment," "time-to-first-approved-design drops by X%," or something else.

➡️ Anchor on a review-outcome metric (pass rate on next review), not a completion/watch-time metric — module completion doesn't correlate with applied competence, and this is exactly the metric this program will be judged against later.

---

❓ **Q3** - **Build vs. buy the hosted interactive-lab SaaS**: Is a fully custom-built platform justified, or should this run on an existing lab/LMS platform (Instruqt-style sandboxes, Pluralsight/A Cloud Guru, Docebo + sandbox integration)? Building this is itself a software project — with its own architecture-review risk, ironically.

➡️ Evaluate 2-3 existing platforms before committing to build. Only build custom if none support the specific sandbox/architecture constraints you need.

---

❓ **Q4** - **DevRel ownership scope**: Does "DevRel owns the program" mean DevRel owns curriculum/content/partner relationship while a separate engineering/IT team builds and operates the SaaS platform (infra, uptime, security patching, localization pipeline) — or does DevRel own all of that too?

➡️ DevRel owns content + relationship only. Platform build/ops sits with an engineering team; otherwise DevRel becomes an unstaffed de facto software team, and platform reliability becomes the thing that fails next.

---

❓ **Q5** - **Enforcement/gating**: Is completing the modules (or passing an assessment) a hard prerequisite before a partner can staff or bid a project, or is it optional/recommended?

➡️ Make it a gating certification tied to project-staffing eligibility. Optional training gets skipped disproportionately by the partners most likely to fail review again — the ones you're building this for.

---

❓ **Q6** - **Language need verification**: Is EN/DE/JA chosen because each of the 6 partners' actual delivery engineers work in that language day-to-day, or because partner HQs sit in those regions while delivery staff may work in English internally?

➡️ Confirm real working language per partner before committing to 3-language day-one localization — translating 14 modules × 3 languages on a monthly release cadence is a large recurring cost to carry if the real need is narrower (e.g. EN + one other).