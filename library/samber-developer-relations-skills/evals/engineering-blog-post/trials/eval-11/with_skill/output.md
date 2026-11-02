**I haven't drafted the post, and I won't until I have your v2 material.** I read the `engineering-blog-post` skill and its three reference files. It needs two things this request doesn't give me.

## Why I stopped

**1. I have no raw material.**
- I don't know the SDK, what changed in auth, why you changed it, or what broke between v1 and v2.
- A 3,000-word draft from me would be invented. That fails the skill's credibility gate (claims classified, no unsourced numbers, an honest limitation).
- I won't write you a plausible-sounding auth story that never happened.

**2. The request bundles three artefacts, and the skill says to split them.**

| You asked for | Artefact | Where it belongs |
|---|---|---|
| "everything that broke between v1 and v2" | Migration guide | `version-migration-guide` skill |
| "walk a new reader through their first integration" | Quickstart or tutorial | `developer-quickstart-guide` or `developer-tutorial` skill |
| "why we redesigned the auth layer" | Engineering blog post | This skill |

- The skill's scope check covers this directly: "a post that links to a tutorial or migration guide" is in scope, but "writing that companion artefact" is out.
- Its pattern rules say: "Split rather than merge. Two patterns in one post produce a piece that satisfies neither reader."
- A v1 user wants a checklist and a detection signal for each break. A new reader wants a first success. A peer engineer wants the design trade-offs. A single post means two of the three groups skim past most of it.

## What I recommend

- **Mode:** draft mode.
- **Pattern:** How We Built It, with the auth redesign as the spine. It's the best fit if you have design decisions to show.
- **Fallback:** Rewrote It in X, if v1 auth failed visibly and you have before/after evidence. That pattern is struck if you have no "what went wrong" material.
- **Length:** about 2,000–2,500 words, because the other two artefacts carry the rest.
- **Outline:**
  1. Goal and the v1 problem (10%)
  2. Constraints (15%)
  3. The new design, with one diagram (20%)
  4. Key decisions, each framed as options, choice and cost (30%)
  5. What we'd change and where v2 auth doesn't fit (15%)
  6. Takeaways, plus links to the migration guide and quickstart (10%)

If you still want one URL, the skill's answer is a short hub post that links the three pieces, not a merged 3,000-word post.

## What I need from you

1. **Split or not?** Pick one:
   - (a) Write the auth-story post, and I'll also draft the migration guide and quickstart as separate pieces.
   - (b) Write only the auth-story post, linking to guides that already exist.
   - (c) Write a hub post (shorter) plus the three pieces.
2. **Raw material.** Point me at any of these:
   - the auth design doc or RFC
   - the v1→v2 diff or changelog
   - the issues or support threads that triggered the redesign
   - any measurements
3. **Disclosure.** Is this the company engineering blog, and is there anything that must stay unpublished (customer names, security detail, unannounced roadmap)?
4. **Reviewer.** Who checks technical accuracy before it ships?

Once I have answers to 1 and 2, I'll return the claim ledger, an outline for your approval, the draft, the gate report and a handoff list. That is the skill's required order.