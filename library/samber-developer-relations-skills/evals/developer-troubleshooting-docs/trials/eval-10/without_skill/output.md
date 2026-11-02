## 1. Epic done after merge? No.

Merge lands text in the docs repo. Bot still serves whatever the last index build baked in. Two separate systems, two separate "done" states.

Close epic only after:
1. Index rebuild actually runs (not "merged", actual rebuild — given "whenever we remember," don't assume it happens automatically)
2. Old chunks from the 6 rewritten entries get deleted from the vector store. Rewrite-without-delete is a classic RAG bug: old + new chunks both retrievable, sometimes old version wins on similarity score, bot contradicts its own new docs.
3. Spot-check: run 8-10 real queries against the 20 new + 6 rewritten entries, confirm retrieval pulls the right chunk and answer reflects it. Passing "no errors during ingest" is not the same check.

⚠️ Real risk here: a fifth of your corpus by word count sits stale until someone remembers to rebuild. That's not a rounding error. Put the rebuild as a required step of the merge (CI hook on merge to main), not a manual follow-up someone owns in their head.

Gate for closing: ✅ rebuilt, ✅ old chunks purged, ✅ spot-checked. "PR merged" alone isn't the gate.

## 2. llms.txt / llms-full.txt: not compliance. Low priority.

No W3C standard. No standards body of any kind — it's an informal convention from llmstxt.org (2024), nobody enforces it, nothing to be "out of compliance" with. Push back on that framing directly with your teammate.

Google's own AI-features guide says explicitly: no special markup or files needed for AI Overviews / AI Mode. Evidence llms.txt improves citation elsewhere (ChatGPT, Perplexity, Claude) is thin — mostly anecdotal, and several site owners report zero crawler fetches of the file in server logs after adding it.

llms-full.txt is even less proven: just a full doc dump, no measured benefit over normal crawlable pages.

Verdict: cheap to add (afternoon, markdown index of the docs site), harmless, not urgent, not blocking anything. If teammate wants real leverage on AI-agent visibility, check `robots.txt` allows GPTBot / ClaudeBot / PerplexityBot / Google-Extended first — that's the lever that actually determines whether those systems can cite you at all. llms.txt is decoration by comparison.

## 3. Bot fabricates fixes: separate bug from the content gap, and merge doesn't fix it.

Root cause: generation isn't constrained to retrieved context, and there's no abstention path when retrieval comes up empty or low-confidence. The 20 new entries only fix hallucination for errors you just documented. Every error still undocumented after the merge — and there will always be some — keeps getting invented answers. Content work and this fix are orthogonal; don't let the merge read as "hallucination: handled."

Fix, engineering side:
1. Add a relevance/similarity threshold on retrieval. Below it → treat as "no match," don't hand weak chunks to the generator as if they're answers.
2. Constrain the generation prompt: answer only from provided context; say "not documented, escalate to support" when context doesn't cover it. Most RAG bots hallucinate because nothing ever told the model *not* to extrapolate.
3. Require a citation per claim in the output. No citation traceable to a doc chunk → drop that claim in post-processing.
4. Build an eval set of known-undocumented errors. Confirm the bot abstains/escalates on all of them, not just the ones covered by the new entries.

Next action: before calling hallucination "fixed," run that eval set. If it still invents plausible fixes for anything outside the 26 entries, the fix isn't done — only the content gap for those 26 got smaller.