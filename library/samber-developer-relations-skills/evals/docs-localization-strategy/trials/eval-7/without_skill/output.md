**Use an LLM pipeline, with Claire and Yannis as the human review gate. Do not hire an agency.**

Next action: ask Claire and Yannis to pull the 20 most-viewed French-traffic pages, quickstart first. That takes about 30 minutes and starts the pilot.

**Why LLM pipeline**
- The docs change every release. An agency charges and waits per batch, forever. A pipeline translates only the diff.
- You already have a French UI. Extract its terms into a glossary. It makes the output consistent and keeps it matching the product.
- Claire and Yannis give 10 hours per release together. That is enough to review diffs. It is not enough to review 300 pages cold.
- French readers are technical, and an LLM handles technical French docs well. Review catches the product-specific errors.
- I can't price this reliably. Get one agency quote for 20 pages as a sanity check. Don't let it delay the pilot.

**Plan**
1. Weeks 1–2: build the glossary from UI strings. Set up the pipeline: source diff, then LLM translation, then PR to a `fr/` folder in Mintlify. Check the exact i18n config in the Mintlify docs.
2. Weeks 3–6: pilot on the top 20 pages. Claire and Yannis review everything. Log every correction they make and feed the corrections into the glossary and the prompt.
3. Weeks 7–12: backfill the next 80 pages by traffic. Ship each page only after review.
4. By month 3–4: go live with the reviewed set. Mark remaining unreviewed pages "traduction automatique" with a link to English, or leave them English-only.
5. Ongoing: each release translates only the changed paragraphs. Review should take 2–4 hours per person. Spend the rest of the budget on the backfill.

Live within 6 months is realistic. The unknown is how many hours the pilot reviews take. If the pilot shows Claire and Yannis can't keep up, cut scope. Don't lower the review bar.

**Guardrails**
- Never publish unreviewed code samples, commands or error messages. Keep these identical to English.
- Version the glossary and the prompt in the repo.
- Add a CI check that code blocks and links match the English source.
- Set one owner. Make it Claire or Yannis, not both.

**Do not expect the 48% vs 61% quickstart gap to close from translation alone.** French-browser readers may differ in other ways. Measure the quickstart completion rate on the French pages after launch. Compare it against 48%. Keep the 40 French tickets per month as a second signal.

**Switch to an agency for these cases**
- Legal, pricing or compliance pages.
- Review hours consistently exceeding the 10-hour budget.
- Repeated errors reaching customers after review.

An agency can also do a one-off audit of the first 20 pages. That is cheap and gives you an independent quality check.

Next action: send Claire and Yannis the top-20 page request.