Here's the reply, ready to send to her:

---

**Subject: Re: OSS section of the devrel benchmark**

She's right that CHAOSS says that — but she's citing one half of CHAOSS's own guidance, not the whole of it, and the half that applies to a different decision than the one we're making.

**CHAOSS actually publishes two models, not one rule:**

- **Starter Project Health** — the model that says "we do not compare projects against each other." This governs *self-improvement* decisions: using metrics to make your own project better. Comparing your health score to a rival's tells you nothing useful there, because the two projects have different ages, staffing, and goals.
- **Practitioner Guide: Assessing Viability** — comparative by design. It ranks applications against each other and compares defect-response rates, because its decision is different: *should I depend on this?* That's an inherently comparative question.

**Our open-source section is the viability question, not the self-improvement one.** We're not running CHAOSS metrics to score our own repo and feel better or worse about it. We're judging the credibility of Beacontree's open-source motion as one input into "what are they doing for developers that we're not" — which is a dependency/credibility judgment, not a health-improvement one. That's exactly the use case CHAOSS built the Assessing Viability guide for, and it explicitly reads a rival's repository.

**On the elephant factor of 1 — she's not wrong, she's making the point the metric exists to make.** Elephant Factor (the fewest orgs producing 50% of activity) is a published CHAOSS metric from that same viability guide. A value of 1 on their flagship "community" repo isn't us dunking on them — it's the finding itself: their "community" repo is a single-vendor surface wearing community clothes. That's not a knock on us; it's a discount we apply to every other number in their column. If their community/contributor story rests on a repo that's really one company's internal work, that changes how much weight their other community and content signals deserve too — which is directly useful to how we read the rest of the benchmark, not just this row.

**What this section will not do**, so she can hold us to it:

- No star counts, follower counts, or any "we're bigger than them" row — those are explicitly excluded (they're bookmarks, not usage, and easy to fake).
- Every field is symmetric — same metrics collected for our own repos, same treatment.
- Every row gets a verdict (close / ignore / counter) tied to a decision, not a scoreboard.

If it'd help, I'll walk her through the actual scorecard rows for this section before it ships, so she can flag anything that still reads as "who's bigger" rather than "what does their OSS motion signal, and what does that mean for how we act."