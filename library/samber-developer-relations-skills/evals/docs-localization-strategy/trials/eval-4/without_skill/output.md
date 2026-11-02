**Next action (30 min):** Copy the German-docs clause from the contract. Then count the pages in the go-live version that cover Ingest and Access Control. Every number below depends on that count.

## Verdict

"LLM everything, Lotte skims" fails on three counts:

- **Scope.** The contract covers two modules, not 1,100 pages and not three versions. Translate only those two modules, in the version the agency goes live on. Probably v6, but confirm.
- **Lotte's hours.** 6 h × ~10 releases ≈ 60 h total. Careful review of technical German is roughly 800–1,200 words/h, an assumption you should measure. That is ~130 pages at most, with no time left for other work. She cannot review everything. Spend her hours where an error costs most.
- **Skimming.** LLM errors in Access Control docs are semantic: swapped allow/deny, dropped negation, "role" and "permission" mixed up. Skimming does not catch these. A federal agency reader will.

## Plan

Today is 2026-10-30. Go-live is about end of March 2027, roughly 21 weeks. Aim to finish by week 16 and keep 5 weeks as buffer.

1. **Weeks 1–2: scope and decisions (~2 days of your time).**
   - Read the contract wording. Does "documentation" mean the admin guide, API reference, or release notes?
   - Does the agency also need acceptance criteria or a named German reviewer?
   - Inventory in-scope pages. Include shared pages they depend on (concepts, auth, getting started).
   - Get quotes from a professional German technical translator for a one-time full review pass.
   - Ask legal whether a "machine-assisted translation, English is authoritative" disclaimer is allowed. Do not assume it is.

2. **Weeks 1–3: glossary and style guide (Lotte, ~10–12 h, mostly up front).**
   - Build a termbase of 150–300 terms: Ingest, Access Control, role, permission, policy, deny, and so on.
   - Set formal "Sie" register.
   - Decide the UI question: is the product UI German? If not, keep English UI labels verbatim with a German gloss. Screenshots stay English unless you recapture them.
   - The glossary is the highest-leverage use of her time. It feeds the prompt and the automated checks.

3. **Weeks 3–4: pilot on 10 pages.**
   - Translate with the LLM and have Lotte review the 10 pages.
   - Record her edit rate (the share of segments she changes) and her words/h.
   - This pilot sets the real budget. If her edit rate is above 30%, fix the prompt and glossary before scaling.

4. **Weeks 5–12: baseline translation, tiered by risk.**
   - **Pipeline.** Translate by segment, not by page. Cache by source-segment hash so only changed segments retranslate. Use a second LLM pass that critiques the translation and flags risky segments.
   - **Automated gates (fail the build).** Code blocks unchanged. Link, heading and number counts match the source. Glossary terms enforced. No untranslated English paragraphs. Placeholders intact.
   - **Tier 1, 100% human review by Lotte:** permission semantics, security warnings, destructive procedures, compliance statements.
   - **Tier 2, sampled by Lotte:** procedures and concept pages. Raise the sample rate if the sample shows defects.
   - **Tier 3, automated gates only:** reference tables and parameter lists.

5. **Weeks 13–16: professional review of the full in-scope baseline.**
   - The external translator reads everything once. This is your contract-compliance gate and covers what Lotte cannot.
   - Fix findings, then send the draft to the agency for early feedback.
   - Weeks 17–21: acceptance, German site build (navigation, search, language switch) and buffer.

## Keeping German in sync after the baseline

v6 gets ~30 docs commits a week, but most will not touch Ingest or Access Control.

- **CI hook.** When a commit touches an in-scope English file, mark the German segments stale. Retranslate only the changed segments.
- **Release-boundary policy.** Publish German snapshots at release boundaries. German may lag English by one release. Agree this with the agency in writing.
- **Lotte's 6 h per release.** Review Tier 1 deltas only. If a delta exceeds her hours, the overflow waits one release. It does not get skimmed.
- **Docs team rule.** Ask them to batch edits to in-scope pages and flag changes that alter behavior.
- **v4 and v5.** Do not touch them unless the agency runs them. If it does, treat each as its own scope decision.

## What to measure (weekly, 5 numbers)

- Lotte's edit rate and her words/h.
- Defects found per 1,000 words by the external reviewer.
- Automated gate failures per run.
- German lag behind English, in releases.
- Tier 1 backlog hours against her budget.

## Costs

- **LLM cost** is small. Bulk translation of ~70k words is roughly tens of euros plus reruns.
- **External reviewer** is the real line item. At ~70k words, expect low-to-mid thousands of euros. That is an order of magnitude from my assumptions, so get quotes.
- **Lotte** is already budgeted, but make sure her manager protects the 6 h.

## Questions that change the plan

Defaults are in brackets.

1. Which version does the agency go live on? [v6]
2. How many in-scope pages are there? [~100–250]
3. Is the product UI localized in German? [No, keep English labels with a gloss]
4. Does the contract require the German to be authoritative, or only to exist? [To exist, but check]
5. Can the agency review the German and give feedback early? [Yes, ask]

**Next:** Send me the contract clause and the in-scope page count. I will then tighten the timeline and Lotte's hours.