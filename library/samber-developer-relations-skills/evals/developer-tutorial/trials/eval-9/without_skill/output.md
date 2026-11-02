## Tutorials

Ardenmoor tutorials follow the seven numbered standards below. Each cites the research or practice it rests on. Raise disagreements against the source, not the number.

### 1. Checkpoint every 3–5 steps

Insert a runnable checkpoint — a command the reader executes and a concrete result to compare against — after no more than five steps, and no fewer than three.

**Source:** Bunce, D. M., Flens, E. A., & Neiles, K. Y. (2010). "How Long Can Students Pay Attention in Class? A Study of Student Attention Decline Using Clickers." *Journal of Chemical Education*, 87(12), 1438–1443.

**Rationale:** The study clicker-tracked self-reported attention lapses during live lectures and found lapses recurring at short, regular intervals once the initial engagement window passed. A checkpoint resets that clock: it gives the reader a concrete win before attention drifts, not after.

### 2. Tutorial runs 15–60 minutes

Scope every tutorial to a single sitting — no shorter than 15 minutes, no longer than 60.

**Source:** Procida, D. *Diátaxis* (diataxis.fr), "Tutorials." A tutorial is experienced start to finish in one session and must leave the reader with a genuine result, not a fragment.

**Rationale:** 15 minutes is the floor for "genuine result" — shorter than that is a snippet, not a tutorial. 60 minutes is the ceiling before the session fatigue documented in Standard 1's source outpaces what a single sitting can sustain. The exact bounds are Ardenmoor's own, chosen inside that range — this is the one part of the standard to flag if the range itself needs revisiting, since the source sets the shape, not the two numbers.

### 3. Maximum 7 primary steps

A tutorial's top-level step list holds at most seven entries.

**Source:** Miller, G. A. (1956). "The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information." *Psychological Review*, 63(2), 81–97.

**Rationale:** Seven is the classic upper bound on how many discrete items a reader tracks as a flat list without external aid — exactly the situation of a top-level step outline held in mind while executing it.

### 4. Maximum 4 substeps per step

Any step that needs breaking down holds at most four substeps.

**Source:** Cowan, N. (2001). "The Magical Number 4 in Short-Term Memory: A Reconsideration of Mental Storage Capacity." *Behavioral and Brain Sciences*, 24(1), 87–114.

**Rationale:** Substeps are read while the parent step's own context is still held in memory — a nested load Miller's flat 7±2 doesn't model. Cowan's revision, about 4 chunks, is the accepted bound once holding capacity is already partly spent. That's why substeps get the stricter number while the top-level list keeps the more permissive one.

### 5. Minimum 55% completion rate

A published tutorial must sustain a 55% funnel-completion rate (readers who reach the final checkpoint ÷ readers who start step 1). Two consecutive review cycles below that, and the tutorial goes back to drafting.

**Source:** Jordan, K. (2015). "Massive Open Online Course Completion Rates Revisited: Assessment, Length and Attrition." *The International Review of Research in Open and Distributed Learning*, 16(3).

**Rationale:** Jordan's dataset puts unassisted, self-serve online course completion at a median around 13%. That's the floor for content with no checkpoints, no scope limit, and no copy-paste code. Ardenmoor tutorials have all three, so 55% sits well above the unassisted baseline. This is the standard where the source sets the floor we're beating, not the number itself — the number is Ardenmoor's policy call, made against that floor.

### 6. Fade worked code in three stages

Introduce a new technique as complete, runnable code. Reinforce it as a diff against the previous step. Test it by stating the requirement alone and letting the reader produce the code.

**Source:** Atkinson, R. K., Renkl, A., & Merrill, M. M. (2003). "Transitioning From Studying Examples to Solving Problems: Effects of Self-Explanation Prompts and Fading Worked-Out Steps." *Journal of Educational Psychology*, 95(4), 774–783.

**Rationale:** This is the direct source for staged fading of worked examples — full example, partially faded example, problem only. Ardenmoor's three stages (full code → diff → requirement) map onto that progression one-for-one.

### 7. Companion branches run CI on a weekly schedule, not only on push

Every tutorial's companion code branch gets its own CI job, triggered on a weekly cron in addition to any push-triggered run.

**Source:** Gentle, A. (2017). *Docs Like Code*. Lulu.com. The "docs as code" practice of holding documentation to the same CI rigor as production code, including catching drift the docs repo itself didn't cause.

**Rationale:** A tutorial can go stale without a single commit to its own branch — an upstream dependency release breaks a pinned command, a CLI renames a flag. A push-triggered job never fires in that case; a scheduled one does. Weekly is the standard interval CI schedulers and dependency-update bots (GitHub Actions `schedule:`, Dependabot, Renovate) offer for exactly this class of check — frequent enough to catch drift before many readers hit it, infrequent enough not to burn CI budget on a branch nobody touched.

---

Drop this under the existing style guide's table of contents as its own top-level section. Cross-link Standard 6 from wherever the guide already covers code samples, since both govern the same code blocks from different angles.