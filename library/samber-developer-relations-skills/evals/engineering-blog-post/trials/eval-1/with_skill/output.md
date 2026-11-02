**Mode: edit mode.** A draft exists, so I'm returning the gate report and a prioritised fix list, with no full rewrite. I only have your summary, so I quote your lines instead of citing line numbers. I haven't run `scan-draft.sh`, because it needs the draft file.

**Pattern.** I'm assuming Rewrote It in X: a before/after on index build time. If this is a product announcement, it is Non-markety Product Perspectives, and the gate still applies.

## Credibility gate report

| # | Check | Result |
|---|---|---|
| 1 | Claims classified | ❌ At least 3 claims are in no evidence class |
| 2 | No unsourced numbers | ❌ "12x", "thousands of teams" |
| 3 | Benchmark disclosure | ❌ A chart and nothing else |
| 4 | One honest limitation | ❌ None |
| 5 | Zero unsupported superlatives | ❌ "fastest columnar index builder available today" |
| 6 | Snippets pinned and dated | ❌ No imports, stale API, no version |

Six of six fail. Each failure has a fix, and none needs a rewrite.

## Fix list

### Blocking (do not publish until fixed)

1. **Intro: "Kestrel is the fastest columnar index builder available today."**
   - This is an unsupported superlative. It implies a cross-vendor measurement, and nothing in the post shows one.
   - Cut it. Open with the measured fact instead, in the shape *"Building the index for [dataset] now takes X minutes instead of Y."*
   - The only other way to keep the claim is a full benchmarketing post against named competitors, which is weeks of work and cannot be done by Thursday.

2. **Results: "index builds are 12x faster" next to a bar chart.**
   - Faster than what? No baseline, hardware, versions, workload or run count appear, and a ratio hides the absolute gap.
   - Add a "How we measured" block **before** the results. It needs hardware, Kestrel version before and after, dataset size and shape, configuration on both sides, number of runs with median and p5/p95, and a link to the scripts.
   - Label the chart with absolute times such as `41 min → 3.4 min`, not just the ratio.
   - The "12x" must equal the measured median ratio. If it came from one run or a best case, change the number to what the runs support.
   - Say whether both sides were tuned. If only one was, label the result indicative.

3. **Paragraph four: "thousands of teams rely on Kestrel in production."**
   - This is an adoption claim with no source. It is also marketing in an engineering post, and it adds nothing to the build-time story.
   - Cut it. Keep it only if you can link a public, current number.

4. **The 40-line Python snippet.**
   - It has no imports and calls `kestrel.build_index()`, which was renamed in 2.0. A reader who copies it gets an error on the first line.
   - Run it against a pinned Kestrel version and add the imports and the expected output.
   - Use the current method name. I don't know it, so I won't guess.
   - If the post compares pre-2.0 and post-2.0, show both names and say which is which.
   - Cut it to about 20 lines, or split it into two one-concept blocks. Link the full script in a repo. State the version and the post date next to it.

5. **No limitations section.**
   - The post recommends something and never says where it fails, which fails gate check 4.
   - Add "Where this does not help" with three or four boundaries a reader can check against their own system:
     - dataset sizes or shapes where the gain disappears
     - memory or CPU cost paid for the speedup
     - Kestrel versions and platforms you did not test
     - workloads where the old path was equal or better
   - This needs facts from the engineer, since I can't invent them. If they don't know where it doesn't help, that is a measurement gap to close before Thursday.

### Strong (fix unless you disagree)

6. **Closing: "we're thrilled to share this journey with the community."**
   - This is press-release register, in a post that is otherwise an engineer's voice.
   - Replace it with the last concrete things: what is still slow, what you will measure next, and where the scripts live.

7. **Commercial disclosure.** This is a company blog post about your own product.
   - State once, early and plainly, that Kestrel Data builds Kestrel.
   - Put a named engineer on the byline. An unsigned corporate post starts with a trust deficit.

### Optional

8. Check the title against the final numbers. "Cut Our Index Build Time" is fine once the baseline is explicit. Don't change it to carry the "12x".
9. After the fixes, run the humanizer pass. Leave the title, the code, the numbers and the versions unchanged.

## Claim ledger for the open claims

| Claim | Class today | Action |
|---|---|---|
| "fastest columnar index builder available today" | unsupported | **Cut** |
| "12x faster" | unsupported (chart only) | **Go get the evidence**, or restate to the measured median |
| "thousands of teams rely on Kestrel" | unsupported | **Cut**, or link a public source |
| `build_index()` snippet works | unverified | **Run it** on a pinned version and show the output |
| "we're thrilled…" | register, not a claim | Replace |

## Before Thursday

Thursday is 2026-11-05, so you have about 4 working days.

- **Cheapest path:** the engineer already has the run data. Fill the disclosure block, fix the snippet, write the limitations, and cut 3 lines. That is a few hours plus one review.
- **If the "12x" can't be reproduced by Wednesday**, publish with the smaller number you can defend, or hold the post. A challenged "12x" costs more than a one-week delay.
- **Review:** have one engineer who worked on Kestrel check the numbers and the snippet, and one outside reader check it without insider vocabulary. Brief them on what to check. Don't forward the draft cold.

## Questions I need answered

1. What does "12x" compare, and how many runs back it?
2. What is the current name of the renamed method, and which Kestrel version should the post pin?
3. Do the build scripts live in a repo you can link publicly?
4. Where did the engineer see no gain? That becomes the limitations section.

Send the draft file and I'll run the scan script and give you line-referenced edits. Tell me which fixes you approve, and I'll rewrite only those passages.