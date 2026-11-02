Here's a message you can send back to her:

---

Hi [name] — pushing back a bit before we shelve the whole section, because I think there are two separate claims bundled together here, and I only agree with one of them.

**On "CHAOSS says don't compare projects":** CHAOSS builds its metrics around a Goal-Question-Metric approach — you start from a specific goal, then pick metrics that answer it. The caution that comes out of that is against naive, context-blind comparison: raw metric values aren't meaningful across projects of different age, domain, governance model, or scope. That's real and I don't dispute it. But that's not the same as "never compare projects." Several CHAOSS-aligned use cases are explicitly comparative — dependency risk assessment, vendor/OSS due diligence before adoption, the whole OpenSSF Scorecard line of work — all of that is one project measured against another, on purpose, because the goal is "which of these should we depend on." So the question isn't comparison vs. no comparison, it's whether our goal and our metric matching are legit. Can you point me to the specific line or model you're reading this from? I'd rather we calibrate against the actual text than against each other's paraphrase of it.

**On the elephant factor of 1:** I think this one needs a correction, not just a caveat. Elephant Factor isn't an individual bus-factor metric — it's an organizational concentration metric: the minimum number of distinct *companies* whose employees account for more than 50% of contributions. An EF of 1 means one company's employees dominate the repo — that could be one person, but it could just as easily be a five-person team, all on the same payroll. If what we actually want to say is "one individual is doing all the work," that's Bus Factor or Pony Factor, and we should check which number the tool reported before we describe it either way.

There's also a second issue worth raising ourselves, before someone else does: that number came from their `community` repo specifically. Repos named `community` are usually docs/governance, not the core codebase — low contributor counts there are typical and don't necessarily say anything about the project's actual maintenance health. Leaning on that one repo to make a claim about their overall project is arguably the same context-blind move CHAOSS warns against, just pointed the other way.

Proposal: let's not kill the section, let's fix the framing. Two options —
- Self-benchmarking: each project measured against its own history / against CHAOSS-recommended thresholds, no head-to-head ranking. Cleanest, zero methodology risk.
- Matched comparison: if we keep a side-by-side, restrict it to like-for-like artifacts (core repo vs. core repo, same metric definitions, methodology disclosed, no cherry-picked single repo), with the goal/question stated up front per GQM.

Happy to pull the exact CHAOSS citation together with you before we decide which way to go.