## Tessellate Maps docs — what changes for round two

**Verdict.** The 2025 reorg wasn't wrong — six people converged on a better structure and it held together well enough that everyone agreed it improved things. What decayed is process, not classification: nothing after launch made "procedures don't live in concepts," "reference doesn't live in tutorials," and "one canonical routing-profiles doc" cheaper to keep true than to violate. Eighteen months of normal, well-intentioned edits by six engineers with no writer and no docs CI was enough to erase it. Fix the governance gap this time, before — or alongside, not after — you touch a single page.

### Why it came back: this is a maturity problem, not a structure problem

A structure that was fixed once and decayed back to the same failure types is the textbook signature of JoAnn Hackos's Information Process Maturity Model (*Managing Your Documentation Projects*, 1994), which places a documentation organization on five levels:

1. Ad hoc
2. Rudimentary
3. Organized and repeatable
4. Managed and sustainable
5. Optimizing

A team at level 1 or 2 has no repeatable process, so **any** structural fix decays — the specific fix doesn't matter, the next well-meaning PR just reintroduces the same three failure types because nothing catches it before merge. Tessellate Maps' setup — six engineers, no writer, no docs CI, one big-bang reorg with no follow-up mechanism — is a clean level-1/2 profile. That's the actual finding to put in front of the team, not "the nav needs fixing again." Put it up front, not buried under the fix list: the reorg drifted back *because* it was a one-off event, not because Diátaxis was the wrong framework or the six of you classified badly.

That reframes the question. "What do we fix" is the easy part — you already told me the three answers. "What stops this from being a recurring quarterly chore" is the one that was skipped last time.

### The queue: governance ships with the surgery, not after it

Normal ranking (SKILL.md Step 8) would put the cheap moves first and the process work last, because moves ship in an hour and CI setup takes longer. Skip that ordering here — it's what produced round one's result. A team stuck at ad hoc/rudimentary needs the enforcement layer landing in the *same* queue as the content fixes, or you'll have a clean docs set and the identical unenforced conditions that decayed it last time.

**1. Declare content type in front matter, validate it in CI.**
Give every page a `type: tutorial | how-to | reference | explanation` field and add a schema check to whatever CI you already run for code — these are engineers, they have CI, you're extending it, not standing up a docs pipeline. A page whose declared type disagrees with its folder becomes a build failure the day someone opens the PR, not something an audit rediscovers in another 18 months. This one control directly prevents two of your three named symptoms: a `type: reference` page can't land under `tutorials/` once the check exists.

**2. Ship page templates so nobody improvises structure.**
Pull the Good Docs Project's four templates (or write your own four-file set) and commit them to the repo. A concepts template with no steps section is what actually stops "procedures in the concepts section" from recurring — not a rule someone remembers, a blank the engineer can't fill with a procedure because there's no procedure section to fill.

**3. Lint prose, structure, and links in CI.** Wire in:
   - **Vale** for prose/style — fast enough to not be an excuse (GitLab runs it across 2,827 pages in under 20 seconds).
   - **markdownlint** for structural conventions.
   - **lychee** for link/anchor checking, on a daily cron that opens an issue on failure.

**4. CODEOWNERS per subtree.** One named reviewer per `tutorials/`, `how-to/`, `reference/`, `explanation/` (or your existing folder names) among the six of you. Misplacement gets flagged by a person before merge, not discovered at the next audit.

**5. A redirect for every moved URL — non-negotiable, not optional.** You're about to move four pages and merge two docs; each move needs its redirect in the same PR, or you'll trade a findability problem for a broken-links problem.

**6. A quarterly re-audit on the calendar**, not dependent on one person remembering: inventory → score → prioritize → refresh → measure, 90-day vs. prior-90-day analytics. Put the date in a recurring calendar invite or CI-scheduled issue, not a TODO.

Then, landing in the same wave, the three fixes you already diagnosed:

**7. Split — procedures out of the concepts section.** This is the named Diátaxis mixing symptom "concepts page that ends with a setup procedure." Extract each procedure into its own how-to page under the new how-to template, leave one link back from the concept page. An hour or two per page, no SME arbitration needed.

**8. Move — the four reference pages out of tutorials.** Straight placement error, not mixing. An hour each plus a redirect. Do this after #1 lands so the front-matter check keeps it from happening again, not before.

**9. Merge — the two routing-profiles docs.** This is the one item that needs a person with authority to say which text is correct, so it costs more than the moves above — but promote it above its normal rank anyway: two contradictory answers on what is very plausibly adoption-path content for a routing API is actively costing readers today, every day it's unmerged, not just at the next audit.

### What not to do

- **Don't run this as a second "big effort."** That's the exact shape of the thing that already failed once — a one-time project with no enforcement layer behind it. Small, shippable actions, same as the loop above, not a Q3 initiative.
- **Don't add new top-level sections to fix this.** Nothing here calls for new structure — you have a structure, it drifted, patch and enforce it.
- **Don't skip recording the decisions this time.** Surface list, the mode you assigned each contested page, the agreed CI thresholds, the queue's state — write these down somewhere durable (repo doc, wiki, wherever the six of you actually look). Round one apparently didn't, which is exactly why a re-check now has to start from scratch instead of a five-minute diff against last time's decisions.

### Before you execute

Three things worth confirming, since they change *how* items 1–5 get implemented, not *whether*:

- Which generator/CI system you're on (MkDocs, Docusaurus, mdBook, etc.) — determines whether you get a built-in strict/broken-link mode for free alongside Vale/lychee.
- Whether URLs are load-bearing enough that redirects need to survive a CDN/proxy layer, or a generator-level redirect plugin is enough.
- Which of the six has standing to arbitrate the routing-profiles merge — naming that person now avoids the merge stalling the whole queue.

One thing *not* worth spending time on: this isn't a case for outside help (CNCF TechDocs, Google Season of Docs) the way a no-writer team with zero prior structure would be — you proved in 2025 you can classify correctly. The gap isn't judgment, it's enforcement. Spend the effort on items 1–6, not on finding someone else to redo what you already did once, correctly.