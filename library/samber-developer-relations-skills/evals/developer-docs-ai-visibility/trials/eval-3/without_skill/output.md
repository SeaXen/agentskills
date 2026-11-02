# Larkmoor docs GEO plan (two sprints)

## Summary

Of the six items, I'd run two as asked, rescope three, and not do one. Each change is tied to what the item is trying to achieve, and I flag below where I couldn't verify a claim.

| Item | Verdict | What we do instead |
|---|---|---|
| (a) Stats and quotes on every reference page | Rescope | Add verifiable facts to reference pages. Use stats and quotes only on conceptual and comparison pages. |
| (b) FAQ schema on every page | Rescope | Use FAQPage only where a visible Q&A exists. Use TechArticle and BreadcrumbList everywhere else. |
| (c) Intros of 40-60 words | Rescope | Write answer-first intros without a fixed word count. Pilot first. |
| (d) Monthly "last updated" bump | Do not do | Change the date only on real edits. Add a real review cadence. |
| (e) One-question-per-page fragments | Do not do | Keep guides whole. Make sections self-contained and directly linkable. |
| (f) Buy the tracker showing "AI rank #3" | Do, after a trial | Run a 2-week trial first and build our own baseline. |

## Why each item changes

**(a) Stats and expert quotes.**
- The "+40%" figure appears to come from the Princeton GEO paper (Aggarwal et al., KDD 2024). I recalled it from memory and haven't re-checked it.
- As I remember it, the study measured relative lift in visibility inside a research generative engine on a benchmark of general queries. It did not measure citation rates for API docs on ChatGPT, Perplexity, or Google AI Overviews.
- A reference page defines a parameter, endpoint, or SDK method. An expert quote there adds noise, and an invented or loosely sourced statistic damages trust.
- What carries over is specific, checkable facts that engines can quote. Examples are limits, defaults, evaluation latency, supported SDK versions, and error codes.

**(b) FAQ schema.**
- I can't source the "2.3x" claim. It is most likely a correlation, because pages with schema tend to be better-built pages in general.
- Google restricted FAQ rich results in 2023, and FAQPage markup must match Q&A that is visible on the page. Marking up pages with no real Q&A breaks the guidelines and risks a manual action.
- I also can't confirm that major LLM crawlers read JSON-LD at all. Treat the benefit as unproven.

**(c) 40-60 word intros.**
- The underlying idea is sound: lead with a direct, self-contained answer that an engine can lift.
- The word band is arbitrary. A reference intro may need 20 words and a concept page may need 90.
- Make the rule "answer first, definition in the first two sentences", then check it against results.

**(d) Monthly date bump.**
- Changing a date without changing content is fake freshness. Search engines learn to ignore `lastmod` from sites that do it, which hurts our real updates too.
- Update the date only when the content changes materially.
- Run a real monthly review of the top 30 pages, and show "Reviewed on" only where someone actually reviewed the page.

**(e) One-question-per-page.**
- This produces thin pages with no surrounding context. It dilutes internal links, makes pages compete with each other for the same queries, and makes the docs harder to use.
- The goal behind it is that each answer can be retrieved on its own. We get that with question-style H2s, stable anchor IDs, and sections that make sense out of context.
- Give a question its own page only when query data shows distinct demand for it.

**(f) The tracker and "AI rank #3".**
- AI answers vary by run, model, prompt wording, and user, so no stable "rank" exists. A single number like #3 is probably one sampled run, or a vendor-defined score.
- Check the vendor's definition and have them reproduce the number live before trusting it.
- Buy a tracker only if it reports repeated-sample mention rate and citation share across a prompt set we control.

## Timeline

Assumes two-week sprints starting Monday 2026-11-02. Adjust to the real calendar.

### Sprint 1 (2026-11-02 to 2026-11-13): baseline, fixes, pilot

| Days | Work | Output |
|---|---|---|
| 1-2 | Build a prompt set of about 30 queries ("best feature flag tool", "feature flags for Go", "LaunchDarkly alternatives", migration, SDK questions). | Prompt list, approved by the CMO |
| 2-5 | Manual baseline: run each prompt at least 10 times on ChatGPT, Perplexity, Gemini, and Google AI Overviews. Record mention rate, citation rate, and which domains get cited. | Baseline sheet |
| 2-5 | Tracker trial (14 days, no purchase). Have the vendor reproduce "#3" live and explain the metric. | Tracker evaluation note |
| 3-5 | Technical check: AI crawlers allowed in robots.txt, docs render without JavaScript, clean canonical URLs, accurate sitemap `lastmod`, and a markdown or plain-text view if the platform supports it. | Fix list, then fixes |
| 5-9 | Pilot on the top 20 pages by traffic and by prompt relevance. Apply the answer-first intro, verifiable facts, question-style H2s, anchor IDs, and TechArticle and BreadcrumbList schema. FAQPage goes only where real Q&A exists. | 20 revised pages |
| 8-10 | Stop the monthly date bump if it exists. Add a "last reviewed" field to the template, populated only by real review. | Template change |

### Sprint 2 (2026-11-16 to 2026-11-27): measure, then scale what worked

| Days | Work | Output |
|---|---|---|
| 1-2 | Re-run the same prompts on the 20 pilot pages' topics. Compare with the baseline. | Before/after report |
| 2-3 | Go/no-go on the tracker, based on the trial and the before/after data. | Decision memo |
| 3-8 | Roll out the patterns that moved results to the next 60-80 pages, in order of prompt relevance. | Revised pages |
| 4-8 | Fill content gaps that the baseline shows. Likely candidates are comparison pages, migration guides, and "when to use flags vs config" pages. These are where stats and expert quotes actually belong. | 4-6 new pages |
| 8-10 | Off-site presence. AI engines often cite third-party sources such as Reddit threads, G2, and GitHub, so list where competitors get cited and we don't. | Outreach list |
| 10 | Readout to the CMO, with a recommendation for a quarterly cycle. | Final report |

Two sprints won't cover every page. The pilot-then-scale order is deliberate, because a full rollout of unproven tactics can't be undone cheaply.

## How we'll know it worked

- Mention rate and citation share across the prompt set, using repeated runs and compared with the baseline.
- Referral traffic from AI engines, if analytics can separate it.
- Pilot pages against unchanged control pages of similar traffic.
- Expect noisy results over two weeks. Report ranges, not single numbers.

## Open questions

1. Which docs platform do you use, and can the template add schema and anchors centrally?
2. How many pages are there, and how many are reference versus guides?
3. Who writes and reviews content, and how many hours per sprint are available?
4. Which AI engines matter most to your buyers?
5. Is the "+40%" study the Princeton paper? If you have a different source, send it and I'll re-check the claim.