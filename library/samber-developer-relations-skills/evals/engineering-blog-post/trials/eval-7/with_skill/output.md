**Mode:** draft mode. You have raw material and no post.

## Decision: write (a), the outage timeline, as a Bug Hunt

Publish (b) later as a separate post. Don't build (c) for this deadline.

## How I ranked them

The skill says to strike options you can't fill first, then rank the survivors by return per hour. I haven't seen the timeline, so the pick is conditional on the check below.

| Option | Pattern | Verdict | Why |
|---|---|---|---|
| (c) Benchmark vs 3 competitors | Benchmarks and Test Results | ❌ **Struck** | You've never run the comparison, so there is no benchmark post yet. Writing the harness, running it, re-running and publishing scripts takes weeks. That is outside a six-hour ceiling that excludes new evidence. It also invites a legal read and is hard to withdraw once quoted. A rushed benchmark against named competitors is the post most likely to get publicly dismantled. |
| (a) Outage timeline | Bug Hunt | 🥇 **Pick** | Top of the efficiency order. It costs about an hour on top of an incident review you already wrote. Your hard date promotes it. It also travels furthest per hour. |
| (b) "eBPF is overhyped" | Thoughts on Trends | 🟠 **Survives, ranked lower** | It also fits a hard date. But the strongest section is the steelman, and it rests on your weakest evidence class (opinion). It has a short shelf life. It also needs evidence you haven't listed. |

## Check before you commit (10 minutes)

Open the internal timeline and answer two questions. Bug Hunt only works if both answers are yes.

1. **Does it contain at least one wrong hypothesis you chased?** The dead ends carry the post's credibility. If the first guess was right, the post reads as reconstructed.
2. **Does it have a surprise a reader outside your company would care about?** The post needs something counter-intuitive, or a failure mode readers will recognise from their own systems.

If either answer is no, switch to (b). If it is a "no" on the surprise only, you can often still find one in the timeline's slowest moment.

## Risks specific to (a)

- **The review chain is the real cost, not the writing.** An incident post needs a security and customer-confidentiality read. Ask for it on day 1, before you write, because it is what can miss the date.
- **Redact before drafting.** Strip names and handles, service codenames, ticket IDs and wiki links. Decide on purpose whether impact figures ship. Keep the blameless framing.
- **Keynote-morning timing.** An outage post that goes live the same morning as a keynote can look like damage control, or contradict the keynote's reliability story. Ask whoever owns the keynote narrative whether the outage touches anything on stage.
- **No unsourced numbers.** Every figure in the post needs to trace to a log, graph or run.

## Fallback: (b), if (a) fails the check or the security read stalls

- Don't state the opinion as fact. Back it with whatever you've measured or seen in your own deployments, and mark the rest as opinion.
- Build a steelman that an eBPF advocate would recognise as their own view.
- Give the thesis a time horizon, or it can never be wrong.
- **Disclosure:** if your agent uses eBPF, or competes with eBPF-based tools, say so once, early and plainly. Without that, the post reads as positioning.

## Six-hour budget for (a)

| Step | Time |
|---|---|
| Read the timeline, run the topic filter, redact, build the claim ledger | 1.0 h |
| Outline, confirmed by you before drafting | 0.5 h |
| Draft in order: symptom, first hypothesis, investigation, root cause, fix, lesson | 2.0 h |
| Four revision passes (core, clarity, components, consumability) and `scan-draft.sh` | 1.0 h |
| Credibility gate, humanizer pass, preview in the CMS, metadata | 0.5 h |
| Buffer for reviewer fixes | 1.0 h |

- **Day 1:** run the check, then start the security and confidentiality review.
- **Days 2–5:** draft and revise.
- **Days 5–7:** two reads. One engineer who worked the incident checks accuracy. One outsider checks it reads without insider vocabulary. Brief them on what to check, and send the draft to no one else.
- **Days 8–9:** fixes, CMS preview, schedule for the morning.
- **Cap the chain:** the review chain should be one security/confidentiality reader plus the two reads above. More approvers make the post vaguer.

## What to do with (b) and (c)

- **(b):** write it after the conference, once you can give it the evidence and a real steelman.
- **(c):** treat it as a compounding asset with its own multi-week budget, and promote it later. It is the post competitors would have to cite. Promote it only if buyers in your category decide on numbers nobody has published, or if a competitor benchmark is circulating unchallenged.

## Questions that could change the answer

1. Does the outage timeline have dead ends and a surprise? (The check above.)
2. Can security and confidentiality clear it within about five days?
3. Does your agent use eBPF? This only matters if you fall back to (b).