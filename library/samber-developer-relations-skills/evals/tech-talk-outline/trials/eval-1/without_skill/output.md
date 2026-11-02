# "Postgres Wire Protocol Without the Driver" — Talk Outline
**ScaleConf Lisbon · Platform track · 25 min + 5 min Q&A · ~7 weeks to rehearse**

## Thesis (one breath)

Every language reimplements the Postgres wire protocol badly, inside an ORM driver nobody profiles. You cut it out, p99 went from 340ms to 61ms, and the talk gives the audience a decision framework plus a way to measure it on their own stack — not a plea to copy you.

**Note:** the outline below is stack-agnostic. Swap in your actual language/runtime specifics (pgx internals, asyncpg, whatever the ORM was) wherever you see `[stack]`.

## Timing budget (25:00 hard stop)

| Block | Time | Runs |
|---|---|---|
| Cold open | 0:00–1:30 | 1:30 |
| The ORM tax | 1:30–4:30 | 3:00 |
| Flame graph, before | 4:30–8:00 | 3:30 |
| Wire protocol, fast | 8:00–9:30 | 1:30 |
| The migration | 9:30–15:00 | 5:30 |
| Results: flame graph after + numbers | 15:00–19:00 | 4:00 |
| Decision framework | 19:00–22:30 | 3:30 |
| Measure it yourself | 22:30–24:00 | 1:30 |
| Close + OSS pointer | 24:00–25:00 | 1:00 |
| Q&A | 25:00–30:00 | 5:00 |

25 minutes is short for this material. Budget above already assumes you cut, not that you'll magically fit everything.

## Section-by-section

### 1. Cold open (1:30)

Lead with the number, not the premise. Audience needs a "how?" itch before you explain anything.

> "Fourteen months ago, one endpoint at Klaxis had a p99 of 340 milliseconds. Today it's 61. I didn't add a cache. I didn't add hardware. I deleted our ORM's driver."

- Slide: just the two numbers, huge type. Nothing else.
- Do not explain the punchline yet — that's the rest of the talk.

### 2. The ORM tax (3:00)

- State the claim: every ORM driver adds a translation layer between your query and the wire protocol, and that layer is rarely free.
- Name the concrete costs generically before your specific case: reflection/marshaling, unnecessary round trips, prepared-statement re-planning, allocation churn on result decoding.
- One line acknowledging why drivers exist (portability, safety, ergonomics) — you're not telling people ORMs are bad, you're telling them the cost is invisible until measured.
- Slide: a simple request path diagram — app → ORM → driver → wire → Postgres — with the driver box highlighted as "the part nobody profiles."

### 3. Flame graph, before (3:30)

This is your strongest visual asset — spend real time on it.

- Show the actual before flame graph. Don't summarize it first; let people look, then narrate.
- Walk exactly one path down the stack: point at the wide frame, name it, say what it's actually doing (e.g., reflection-based scanning, type conversion, buffer copies).
- Land on the specific finding that triggered the investigation — what made you say "wait, that's not the query, that's us."
- Slide: full-width flame graph, laser-pointer-style annotation (arrows/circles added in the deck, not live pointing — travel + platform-track AV is unpredictable).

### 4. Wire protocol, fast (1:30)

Platform-track audience at a scale-focused conference — assume they know Postgres and ORMs. Do not teach the protocol; orient them in 90 seconds flat.

- Simple query protocol vs. extended query protocol (parse/bind/execute), in one sentence each.
- Text vs. binary format — this is usually where the real win hides; say so explicitly, you'll cash it in during results.
- One slide, one diagram, move on. If you find yourself explaining SCRAM auth handshakes here, you're teaching a workshop, not giving a 25-minute talk — cut it.

### 5. The migration (5:30)

This is the load-bearing section and the riskiest to run long. Keep it a story, not a tutorial.

- What you ripped out: name the driver/ORM layer specifically.
- What you built instead: connection handling, the extended-query path, prepared-statement caching, binary decoding — pick 2-3 to go deep on, not all of them.
- Show 3-5 curated lines from the migration diff, not the diff. Before/after snippet, framed as "this is what changed at the call site" — the point is the shape of the change, not a code review.
- One "it wasn't free" moment: a real gotcha you hit (type mapping edge case, connection pooler interaction, a feature you had to reimplement or explicitly drop). Credibility comes from the scar, not the win.
- Slide sequence: architecture before → architecture after → one diff snippet → one gotcha callout.

### 6. Results: flame graph after + numbers (4:00)

- Show the after flame graph next to (or toggled against) the before one. Let the shape difference do the talking.
- Name where the time actually went: which frames shrank, which disappeared entirely.
- State the numbers again, now earned: 340ms → 61ms p99, plus whatever secondary metrics you have (allocs/op, CPU, p50/p95 if they tell a consistent story — don't dump every metric you own).
- One sentence on what did NOT improve, if anything didn't — this is what makes the talk trustworthy instead of a highlight reel.

### 7. Decision framework (3:30)

This is the section your abstract promised — don't let it get squeezed by an overrun migration section.

- Frame explicitly: "here's how to decide if this is worth it for your service, not just whether it was worth it for mine."
- Give 3-4 concrete signals that make raw protocol access worth considering: driver/ORM overhead is a measured (not assumed) fraction of your p99; query shape is narrow/stable enough to hand-maintain; you have the team bandwidth to own a protocol implementation; the win is on a hot path that actually matters to the business.
- Give the counter-signals just as clearly: wide, ad-hoc query surface; small team; driver overhead isn't actually where your time goes (say this one loud — most services should NOT do this, and saying so is what makes the framework credible).
- Slide: a simple checklist/decision tree, not prose paragraphs — this is the slide people photograph.

### 8. Measure it yourself (1:30)

- Show the benchmark harness, briefly — what it measures, how it isolates driver overhead from query/network/DB time.
- One sentence on methodology discipline: same query, same data, same hardware, driver swapped — the comparison is only honest if that's true.
- This is the "how to measure it" half of your abstract's promise — make sure it's not the part that gets cut when you're over time.

### 9. Close + OSS pointer (1:00)

- One memorable closing line, tied back to the open. Example shape: "We didn't set out to write a Postgres client. We set out to stop guessing where our latency went — the client was just what was left over."
- One slide: repo link, one-line description, explicit low-pressure invite ("if you're curious, it's there — I'm not asking you to adopt it, I'm asking you to measure your own driver first").
- Keep the pitch to this one slide. A platform-track technical audience tunes out fast if the last five minutes turn into a product pitch.

### 10. Q&A prep (5:00 slot — prep more than you need)

Likely questions from a staff/principal-engineer audience — draft a 1-2 sentence answer for each before rehearsing:

- Why not just switch to an existing low-level driver (pgx-equivalent for `[stack]`) instead of hand-rolling?
- What did you lose — COPY, LISTEN/NOTIFY, SSL/GSSAPI negotiation, full type coverage, statement caching semantics?
- How does this interact with connection poolers (pgbouncer/pgcat) in transaction mode?
- How did you validate protocol correctness — fuzzing, conformance tests against real Postgres, auth methods (SCRAM)?
- What's the ongoing maintenance cost of owning a protocol implementation vs. a maintained driver?
- Did you consider a narrower fix (binary format only, pipelining only) before the full rewrite?
- What does the OSS client support today vs. what's still driver-only?

## Cut list (use if a run-through goes over)

Cut in this order — each preserves the abstract's promise, none touch the flame graphs or the decision framework:

1. The second migration deep-dive item (keep one, drop the other).
2. The wire-protocol background slide — compress to one verbal sentence, no slide.
3. One secondary metric in the results section.
4. Trim the gotcha story to one sentence instead of a mini-narrative.

Never cut: the decision framework, the "how to measure it" section, or the counter-signals half of the framework — that's what separates this from a highlight reel.

## Rehearsal plan (today: 2026-09-18 → talk: ~2026-11-06)

| Week | Dates | Focus |
|---|---|---|
| 1 | Sep 18–24 | Lock this outline. Pull the before/after flame graphs and benchmark harness output into rough slides. No polish. |
| 2 | Sep 25–Oct 1 | Write the full speaker script for the narrative sections (open, ORM tax, migration story). Cut the diff down to 3-5 snippets. |
| 3 | Oct 2–8 | Deck v1 complete. First full solo run-through, timed and recorded. Expect to run long — that's normal. |
| 4 | Oct 9–15 | Cut to fit, target 22 minutes to leave buffer. Drill the decision-framework and measurement sections until fluent without notes. |
| 5 | Oct 16–22 | 2-3 more full run-throughs, recorded video this time. Watch for filler words and pacing. Draft the Q&A answer bank above into full answers. |
| 6 | Oct 23–29 | Dry run in front of 1-2 colleagues — ideally one deep on Postgres internals, one who isn't. Incorporate feedback. |
| 7 | Oct 30–Nov 5 | Final polish runs only (3-4x). Tech check: laptop + adapter + clicker, offline deck copy, backup PDF export, backup slide-free verbal version of the open/close in case AV fails. Travel to Lisbon, rest, don't cram the night before. |

## Logistics checklist for the day

- Offline copy of the deck on the laptop and a USB backup; PDF export as a second fallback.
- Confirm the venue's aspect ratio and connector type ahead of time — don't discover it on stage.
- Time-check landmarks memorized: should be entering the migration section by minute 9-10, entering results by minute 15 — if you're not, you're already cutting live.
- Bring the benchmark harness and flame graphs as static images in the deck, not live tooling — never demo live in a 25-minute slot with a hard Q&A cutoff behind it.