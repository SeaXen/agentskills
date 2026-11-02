**Not quite. The order is wrong and the review list is too long.** I haven't seen the draft, so this is advice on the plan. It isn't a gate report.

**Mode:** Edit mode, since a draft exists. I'd return a fix list and rewrite nothing you haven't approved.

## What to change

1. **Don't start with a prose polish.** Facts and structure come first. If a reviewer cuts a claim or a section, you've polished sentences that no longer exist.
   - Do the four revision passes in order: core (facts, focus, flow), clarity, components (code, tables, images), consumability.
   - Prose polish and the humanizer pass come last. Leave code blocks, command output, benchmark tables, version numbers and the title exactly as written.
2. **Run the credibility gate before anyone sees it.** It has six checks, and each must pass:
   - Every claim is measured, shown, sourced, or marked as opinion.
   - No unsourced numbers.
   - Benchmark disclosure is complete, if the post has comparisons.
   - At least one specific limitation is stated.
   - No unsupported superlatives.
   - Snippets are pinned and dated.

   Run `scripts/scan-draft.sh` over it as a grep pass, and review each hit yourself. This catches what a reviewer would otherwise burn their round on.
3. **Don't send one draft to six people.** The skill's sources warn that too many reviewers leave posts vaguer, because each approver removes specifics ("too many cooks"). The blogs Dan Luu rated well kept one clear owner and a short chain.
4. **Don't forward the draft and collect comments.** Send each reviewer a brief: what you want checked, the background they lack, and any blocker question. Without one you get line edits instead of a fact check.

## Suggested chain

| Step | Who | Checks | When |
|---|---|---|---|
| 1 | One staff engineer | Technical accuracy, using your claim ledger as the checklist | First |
| 2 | Someone outside the team | Reads without insider vocabulary | After step 1 fixes |
| 3 | Legal | Only if the post touches a named competitor, customer data, security detail, or unannounced roadmap | Once, on the near-final text |
| 4 | Product marketing | Only for commercial disclosure, if you sell what the post covers. Not for tone. | Same time as legal |
| 5 | CEO | Approve or veto. Not line comments. | Last |

- **Your manager** is the owner who unblocks. They don't need to be a reviewer.
- **The second staff engineer** is redundant unless the post spans two systems. In that case, give each of them their own section.
- **Product marketing** should check disclosure only. Marketing edits are what turn engineering posts into press releases.

## What I need to finish the job

Please send the draft or its path. I'll then return the gate report and a fix list in three tiers (blocking, strong, optional), ordered by trust damage and quoting each offending line. I also need answers to these, one at a time:

1. What is the post about: a bug hunt, a rewrite, a design write-up, a benchmark, or a product post?
2. Where does it publish: company blog, personal blog, or third party?
3. Is there a publish date?
4. What must stay unpublished?
5. Do you have a commercial interest to disclose?

## Before sending

Once the fixes are in, three things should be true:
- All six gate checks pass.
- Each reviewer has a written brief.
- One person owns the final call.