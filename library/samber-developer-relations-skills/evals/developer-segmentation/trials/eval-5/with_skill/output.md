# Decision: JVM/Java — anti-segment ruling, Kettlewell

Applying `developer-segmentation` (Steps 3–5) to close this out. Not a new map — Node/Python-first is your existing cut; this rules on where Java sits under it.

## Sizing (Step 3)

> ~1.9% of signups, ~2.3% of active workspaces — Java/JVM — first-party telemetry; as of 2026-09-19; confidence: **measured**.

Measured beats estimated beats inferred. This is the strongest evidence class the method has — no external source needed to make the call.

One honest caveat, stated so it can't be used against you later: first-party data is survivorship-shaped. You never counted the JVM developers who bounced off a Node/Python-first CI runner before signing up, so this number can't tell you "JVM demand is small" — only "JVM demand inside a product that doesn't ask JVM developers to come is small." That's a real limitation of the instrument, not a reason to reverse the call. It just means the size number isn't your best argument by itself — the decision-unit and effort arguments below are what actually carries it.

## Decision unit (Step 4)

"The JVM enterprise segment" is a company-adoption claim, not a plugin request. Under company adoption, a developer evaluates but an architect/platform lead approves and a budget owner signs. What that role actually asks for: compliance answers, migration path, support SLA, named production references, licence clarity — not a Maven plugin and a quickstart.

That's the tell. A Maven plugin + Java quickstart is *individual-adoption* tooling (champion-level ergonomics). Ship it, and the same advocate is back next quarter asking for the compliance pack and the migration guide, because the plugin alone never gets a real enterprise deal through review. You'd be funding the down payment on an artefact list, not the ask on the table. Naming this now — in writing — is what stops the argument from reopening piece by piece.

## Score (Step 5), weighted for a developer-adoption driver

| Criterion | Score | Why |
|---|---|---|
| Size | 1 | 1.9–2.3%, measured |
| Reachability | 2 | Real venues exist (Java CI/build ecosystem forums, Maven Central), but you have no presence there today |
| Fit | 1 | No quoted pain in Java developers' own words on record — the ask is framed as "the JVM enterprise segment," which is exactly the invented-label pattern the method flags as a stereotype with no members behind it |
| Value | 1 | No named deal, no dollar figure, no lost-deal citing this as the blocker |
| Effort | 3 (high) | Maven plugin + quickstart is the visible ask; JVM *enterprise* adoption additionally needs a compliance pack, migration path, named references — none funded |
| Competitive position | 1 | You'd be entering an ecosystem where Jenkins, Gradle/Maven-native tooling and incumbent JVM CI already own the default |
| Compounding | 1 | Winning a JVM enterprise account doesn't make your Node/Python segment cheaper to win — different ecosystem gravity entirely |

Value-per-effort is low on every axis that isn't effort, and effort is the highest score in the table. That's a segment that loses every round it's scored in — which is exactly the pattern the method warns gets promoted anyway by momentum and advocacy, not by evidence.

## Evidence floor

5–10 independent data points is the bar for a funded segment (lost deals citing Java specifically, support tickets, interviews, sales notes). Ask the advocate directly, once, on the record: how many are there? If the honest answer is "a handful of anecdotes and a strong opinion," this is a **hypothesis segment**, not a segment — it doesn't get funded, it gets a cheap test.

## Ruling

**Anti-segment: JVM/Java, this horizon.** Reason: effort — the real artefact list (compliance, migration, support, references) that "enterprise" implies is unfunded and un-scoped, on a segment that's 1.9–2.3% measured with no quoted pain and no named revenue trigger behind it. Not "1.9% is small" alone — that's not a defensible reason by itself and you'll get pushed back into the same argument if that's all you lead with. The defensible reason is: *the artefact this claim actually requires costs a quarter of engineering, and nothing on record justifies funding it.*

## What would reopen it (say this part out loud — it's what actually ends the recurring argument)

Cheap test, days not quarters, per the method: if the advocate can produce **one named lost or stalled deal** where Maven/JVM support was the stated blocker — not "would help," a deal that actually died on it — that's a real data point and the call gets revisited. Absent that, set a review trigger instead of an open-ended fight:

- Java's share of new signups crosses ~5% for two consecutive quarters, or
- a named enterprise deal stalls specifically on JVM/Maven support, or
- the funded driver changes (e.g., a JVM-heavy acquisition, a pivot to sales-enablement-funded devrel)

Anything short of one of those three is the same debate wearing a new month. Put this section in writing wherever the argument keeps happening — the anti-segment only stops re-litigation if it's recorded, not just decided in your head.