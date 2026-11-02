**Mode: edit mode.** The draft exists and a colleague has checked it for accuracy. I don't have the post text, so I can't give line-level edits or write the metadata yet. Paste the post (or its path) and I'll do the pass.

**Next action:** send me the draft, plus the answers to the three questions at the end.

## What is left, in order

The technical review covers the facts only. It does not cover the credibility gate, the prose, the CMS render, or the metadata.

1. **Run the credibility gate** (about 15 min). The accuracy check does not replace it.
   - Every claim is measured, shown, sourced, or marked as opinion.
   - Every number traces to a run, a log, or a citation.
   - The tables carry the benchmark disclosure: hardware, versions, workload, tuning of both sides, run count and variance, script link.
   - The post states at least one specific limitation.
   - No unsupported superlatives.
   - The three code blocks are pinned to versions and the post is dated, with the full version linked.
   - The two benchmark tables need a methodology section before the results, absolute values next to ratios, and at least one chart. Tables alone fail this pattern.
2. **Run `scripts/scan-draft.sh <draft.md> --no-numbers`** (about 2 min). Use `--no-numbers` only after every figure is in the ledger. Review each hit yourself. It catches superlatives, absolutes, adoption claims, internal IDs, and "latest version" wording.
3. **Check the pasted command output** (about 5 min). Look for hostnames, internal paths, ticket IDs, and usernames. This is the likeliest leak point in a technical post.
4. **Do the humanizer pass** (about 20 min), with these items kept byte-for-byte:
   - code blocks
   - command output
   - benchmark tables
   - version numbers
   - the title

   Target the following:
   - hollow transitions
   - uniform sentence rhythm
   - significance inflation
   - tidy triples

   The skill does not name a humanizer. Use `humanizer` from your skill list.
5. **Do the clarity and consumability passes.** Have someone outside the team read it for insider vocabulary. Skim-test the headings. Edit mode should return a fix list, not a rewrite, so I will not touch your voice without approval.
6. **Write the metadata.** Do this last, once the text is frozen.
   - Title tag: the human title may stay as is.
   - Meta description.
   - URL slug.
   - Link targets.
   - Alt text for images and charts. The tables are text and need none. Describe each chart's finding, not "bar chart".
   - Tags.
7. **Preview in Contentful before publish.** The skill says code blocks and tables break in the CMS, not in the draft.
   - Open the preview on the real template.
   - Check that the code blocks, the tables, and the pasted output keep their spacing and fences.
   - Check that the title tag and description render in the page head.
8. **Add a dated correction note if a reader finds an error later.** Do not edit silently.

## Gaps in the skill

- It does not cover Contentful. I don't know your field types (Rich Text vs Markdown), your SEO fields, or your preview setup. The skill only says to preview in the CMS and then handle metadata.
- It sets no length limits for the title tag or the meta description. Any numbers I give would be my own, not the skill's.
- If you cross-post to dev.to, set a canonical URL back to your site. The full rules live in the `devto-playbook` skill, which is not in my list.

## Questions

1. Which pattern is the post: Rewrote It in X, Benchmarks, or something else?
2. Where does it publish: company blog, personal blog, or a third-party publication?
3. Is there a commercial interest to disclose, such as your own product or a competitor in the benchmark? This decides whether the post needs a disclosure paragraph and a fairness check.