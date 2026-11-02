## Video-program numbers for the budget deck — each with its source

*(Compiled from the `technical-video-script` skill's `references/published-findings.md`, which traces every figure to its original source. Numbers below are split into **sourced research** — citable as an industry standard — and **production baselines** — defensible engineering decisions, not something to defend as "the industry says." Mixing the two is the fastest way to lose a citation fight with a skeptical VP, so they're kept separate.)*

---

### 1. How long should videos be?

**Sourced, hard data:**

- **Median engagement time tops out at 6 minutes, regardless of total video length.** Viewers "often make it less than halfway through videos longer than 9 minutes."
  *Source: Guo, P.J., Kim, J., & Rubin, R. (2014). "How Video Production Affects Student Engagement: An Empirical Study of MOOC Videos." ACM Learning@Scale 2014. n = 6,902,358 viewing sessions, 4 edX courses, Fall 2012 — the largest published study of instructional-video engagement to date.*

- **Shorter wins outright:** the 0–3 minute bucket had the highest engagement and least variance — 75% of sessions ran past three-quarters of the video. Downstream action (viewer goes on to attempt a follow-up exercise) falls monotonically with length: **56% → 48% → 43% → 41% → 31%** across the study's five length buckets.
  *Same source (Guo et al. 2014).*

- **Cross-check, different corpus:** videos under 1 minute average a **52% engagement rate**; viewers watch over half of educational/tutorial videos in the 1–5 minute range; a further drop appears past 30 minutes.
  *Source: Wistia, "2026 State of Video" report, 13M+ hosted videos. This is a business-video corpus, not a teaching one — cite it only as a same-direction cross-check, not primary evidence.*

**What this means for a length policy:** segment any video into **chunks under 6 minutes**, whatever the total runtime — that's Guo et al.'s own headline recommendation, tested against a real course pair (the segmented course beat the spliced-lecture course 55% vs. 41% on follow-on attempts).

**Caveat to state alongside the number:** this is a retrospective log study (watch-time proxy, not a controlled experiment), across 4 math/science MOOCs, with self-selected early-adopter learners. Watch time ≠ learning. State this if anyone pushes back on the number's generality — it protects the number, it doesn't weaken it.

**Myth to pre-empt:** the widely-circulated "100% / 50% / 20% engagement by length" table is a *secondary, simplified rendering* of Guo et al.'s boxplot, not a number the paper itself states. If someone on your team already has that chart in a deck, replace it with the two figures above — they're the actual statements from the paper.

---

### 2. What font size for code on screen?

**Hard numbers:** terminal text **24pt or larger**, editor text **20pt or larger**, checked against a phone-sized playback, not the authoring monitor.

**Important for the citation slide: these are NOT an industry standard.** They are this skill's own baseline, chosen to survive small-screen playback. The one published production guide that addresses this — egghead's instructor guide (`howtoegghead.com`) — only says **"large fonts"**, with no point size. There is no peer-reviewed or platform-published number for code legibility on video. If your VP asks "who says 24pt," the honest answer is "no external source does — we set that floor internally, for phone legibility." State it that way; don't attribute it to a study that didn't measure it.

**What the actual research says about code-on-screen formats (this part IS sourced, and it's a stronger argument than the font size):** code screencasts sit in the **weaker engagement bucket** of Guo et al.'s format comparison. Continuous tablet-drawing tutorials (Khan Academy style) held **1.5–2x the normalized engagement** of "PowerPoint slide and code screencast tutorials" — **40% vs. 31%** on follow-on problem attempts. Their recommendation when code must be on screen: annotate on top of it (zoom, highlight, draw), don't just display it.
*Source: Guo et al. 2014, same study.*

This is a better line for the slide than the font size: **"code-on-screen video underperforms drawing/annotation formats by 1.5–2x in this study — our program budgets for zoom/highlight/annotation work, not just filming a screen."**

---

### 3. How many seconds does the intro get?

**30 seconds** is the hard number — but it's a *platform measurement definition*, not a stylistic guideline: the dominant video platform's audience-retention report defines "intro retention" as the share of viewers still watching **after the first 30 seconds**. That's the boundary your own KPI dashboard will report against, so it's the correct number to put on a slide about intro design.
*Source: platform audience-retention reporting documentation. Platform-defined thresholds get revised — re-verify before the deck ships if you can access current docs.*

**Ceremony budget inside that window: ~5 seconds.** Branding, intro animation, "hey everyone, welcome back" reads as filler beyond about 5 seconds.
*Source: Nielsen Norman Group, video usability research — a measured perception threshold, not a hard cutoff. Round it to "~5 seconds" on a slide, not "exactly 5."*

**What has to happen inside the 30 seconds, per the research-backed opening structure:** name the problem in the viewer's words, show the result already working (not promised), state prerequisites, state the runtime. All four, before second 30.

---

### 4. Industry standards on engagement (general)

| Metric | Number | Source |
|---|---|---|
| Median engagement ceiling | 6 min, regardless of total length | Guo et al. 2014 (n=6.9M sessions) |
| Half-watched threshold | Viewers often <50% through past 9 min | Guo et al. 2014 |
| Downstream action by length bucket | 56%→48%→43%→41%→31% | Guo et al. 2014 |
| Format penalty for code screencasts | 1.5–2x engagement gap vs. drawing tutorials | Guo et al. 2014 |
| Talking-head effect | Interspersed instructor face > slides alone; studio production values showed no measurable benefit | Guo et al. 2014 |
| Speaking rate | Corpus 48–254 wpm (mean 156, sd 31); engagement rose with rate, up to 2x, within a length band | Guo et al. 2014 |
| Sub-1-minute engagement | 52% average engagement rate | Wistia 2026 State of Video (13M+ videos) |
| Intro retention definition | % watching after first 30 seconds | Platform retention reporting |

**One caution worth putting in speaker notes, not on the slide itself:** the speaking-rate finding is explicitly *not* a lever, per the study's own authors: *"Speaking rate is merely a surface feature that correlates with enthusiasm… our recommendation is not to force instructors to speak faster."* If someone tries to turn "faster = more engagement" into a mandate for presenters, that's a misread of the paper — it's correlation with enthusiasm, not a causal dial.

---

### Citation block (ready to paste as footnotes)

1. Guo, P.J., Kim, J., & Rubin, R. (2014). *How Video Production Affects Student Engagement: An Empirical Study of MOOC Videos.* Proceedings of the First ACM Conference on Learning @ Scale (L@S '14). n = 6,902,358 sessions, 4 edX courses, Fall 2012.
2. Wistia. *2026 State of Video Report.* 13M+ hosted videos analyzed.
3. Nielsen Norman Group. Video usability research on duration perception and introduction length.
4. egghead.io instructor guide, `howtoegghead.com` — published production standard for technical screencasts.
5. [Platform] audience retention reporting documentation — defines "intro" as % retained past 30 seconds (verify current version before publishing).
6. Internal baseline (not externally sourced): code legibility floors — terminal ≥24pt, editor ≥20pt, verified at phone-sized playback.