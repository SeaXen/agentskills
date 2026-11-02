Badges last, not first. Skill names this exact mistake: "Leading with the cheapest fix. The badge row is the fastest thing on the list and nearly the least valuable." Value ordering puts badge row dead last of six fixes. Cut them in step 6, not step 1.

I don't have repo access — can't read halyard-labs/streamsmith or run `readme-audit.sh` against it. Scorecard below built from what you gave me plus assumption: **audience = developer evaluators** (no enterprise/procurement signal mentioned — say so if wrong, changes Step 8).

## Scorecard

```
README audit — halyard-labs/streamsmith  (audience: developer evaluator, ASSUMED)
Band A: A1 unknown (need repo) · A2 FAIL (Node version undocumented) · A3 NEEDS REPO · A4 FAIL (no status) · A5 unknown
Band B: B1 1/2 (vague "simple and fast") · B4 0/2 (install at bottom, wrong order) · B5 0/2 (11 badges)
Verdict: does not pass — A2, A4 blocking on facts you already gave me; A1/A3/A5 need repo read
```

## Fix order, one afternoon (~3h)

Effort-cheapest ≠ value-highest ≠ do-first. Skill's efficiency order, re-ranked for your Friday deadline:

1. **Status line** (A4) — 5 min. Write it now:
   > streamsmith is actively maintained. Issues and PRs get triaged within [your real number] days.

2. **Install block** (A2) — 15 min, you fill the version:
   ```
   Requires Node [X] or later.

   npm install -g streamsmith

   Verify:
   streamsmith --version
   ```
   Get the real minimum from `package.json` `engines.node` or your CI matrix — don't guess it.

3. **Claim check** (A3) — 30–45 min, **you run this, I can't**: grep every flag/command the README shows against your actual arg parser. Any flag documented but not registered = cut it or fix the parser. Any "handles N msg/s" style number needs a benchmark file behind it or it comes out.

4. **Differentiation** (B1) — 30 min. Replace "simple and fast" — it's an unfalsifiable claim, means nothing. Three angles, pick and fill with a real fact, don't ship a made-up capability:
   - Mechanical: "streamsmith replays a Kafka topic from any offset — including a wall-clock timestamp — into a new topic or consumer group, without writing a rebalance-aware consumer by hand."
   - Problem removed: "Replaces the `kafka-console-consumer | kafka-console-producer` pipe or one-off KStreams job people hand-roll to replay a slice of a topic."
   - What it retires: "Stop keeping a scratch reprocessing script around — replay is one CLI invocation."
   Only ship the one you can verify against the actual flags.

5. **Reorder** (B4) — 45–60 min. CLI-tool skeleton, not top-to-bottom rewrite — move existing content, don't reinvent it:
   1. Name + one-liner
   2. Terminal transcript — one real command, real output, plain code block (skip animated/recorded demo — not worth a week for Friday)
   3. Why over the incumbent (step 4's text)
   4. Install (step 2's block)
   5. Common invocations, 3–4 examples
   6. Config (link the rest)
   7. Status/versioning (step 1's line)
   8. Licence, contributing pointer

6. **Badges** (B5) — 10 min, last. Keep 4: npm version, licence, supported Node versions, maintenance/last-release. Cut the other 7 — coverage, contributor count, chat, "made with," build status all read as noise to a first-time visitor per the npm-badge study (Trockman et al., 294,941 packages): badge adoption doesn't raise popularity, and past a few badges it correlates with *less*.

## Skip today

No enterprise trust signals (Step 8) unless Friday's room has procurement people — tell me if it does. No animated terminal demo — costs a week, you have an afternoon.

Next: confirm the real Node minimum and paste your current "Why streamsmith" + install section here, I'll draft the exact replacement text against your real flags instead of placeholders.