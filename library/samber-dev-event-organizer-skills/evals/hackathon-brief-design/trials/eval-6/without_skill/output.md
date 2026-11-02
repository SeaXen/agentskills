# Hack prompts for "smarter stores": how specific, plus a draft

## Answer first

Be specific about the contract and loose about the solution. Don't write per-prompt acceptance tests that decide the winner.

Your co-organizer is right that judging needs to be fair, but acceptance tests only deliver that when the problem has one convergent answer. A "smarter stores" hack is meant to be open-ended, and over 30 hours, 60 engineers will build things you can't predict. A hidden test suite either rejects good, unexpected solutions or rewards whoever best guessed the test author's intent.

Use three layers instead:

1. **Shared starter kit (build once).** It holds synthetic store data, a simulator or replay tool, and a scoring script. It is not one repo per prompt.
2. **Thin automated floor per track.** This is pass/fail: does it run, read the data, and emit the agreed output format? It's cheap to write and objective, and it's worth about 15% of the score.
3. **Measured outcome plus human judging for the rest.** If a track has a measurable outcome, score it on a held-out dataset. Everything else gets a published rubric and judges, ideally including someone who works in a store.

## The specificity dial

| Specify (fixed) | Leave open |
|---|---|
| The problem and who it's for | Architecture, language, stack |
| Input data and output format | Model choice, rules vs ML vs LLM |
| Hard constraints (runtime, offline, no PII) | UI, or whether there's one |
| How it's scored, published before kickoff | What to cut for 30 hours |

**Test for each prompt:** could two teams build completely different solutions that both clear the floor? If yes, it's specific enough. If the test only passes one architecture, it's too tight. If the prompt can't say what "working" means, it's too loose.

## Why not per-prompt acceptance tests as the judge

- **Organizer cost.** N prompts means N repos, N test suites, and N validations that the tests aren't broken or gameable. Nobody dogfoods them before kickoff, and a flaky test during the hack hurts fairness more than no test.
- **Overfitting.** Visible tests get optimized for. Hidden tests feel unfair. Use a public dev set and a held-out set instead.
- **Wasted hours.** At 30 hours, every hour spent fighting someone else's harness is an hour not spent on the idea.
- **The theme gets lost.** "Smarter" is a judgment about usefulness in a store. A test suite can't see that.

## Rough shape for 60 engineers

- About 12 teams of 5, and 3 to 4 tracks. Several teams can take the same track and compete head to head, which is what makes the metric fair.
- A scoring service where a team can submit every couple of hours, capped at about 10 submissions, so the leaderboard can't be brute-forced.
- A final demo for every team, 5 minutes.

## Scoring template (100 points)

| Points | Criterion | Who decides |
|---|---|---|
| 15 | Floor: runs end to end on the starter data, output format valid | Script |
| 25 | Held-out metric | Script |
| 30 | Usefulness to store staff | Judges, with a store-ops person |
| 20 | Demo and craft | Judges |
| 10 | Realistic path to production | Judges |

Tracks with no measurable outcome move the 25 metric points to the judged criteria.

---

## Draft prompt: Track A, "Shelf Gap"

**Problem.** Shelves look full in the system but are empty on the floor (phantom inventory), or are empty and nobody restocks them in time. Store staff walk the aisles by hand to find these gaps, and some are never found. Build something that tells staff which products to check first, before shoppers find the gap.

**Users.** A store associate on shift with a handheld device, and the store manager planning the next restock round.

**What you get (starter kit).**
- `data/dev/`: 4 weeks of synthetic data for 3 stores: POS sales, stock-system quantities, delivery receipts, and shelf-walk results (ground truth for a subset).
- `data/schema.md`: field definitions.
- `tools/replay`: replays events in time order, so you can run as if live.
- `tools/score`: the same scorer used for judging, runnable locally on the dev set.
- `make run`, `make test` and `make score` targets.

**You must (the floor, 15 points).**
1. `make run` reads an event stream from `data/` and writes `out/alerts.jsonl`. Each line has `store_id`, `sku`, `ts`, `confidence` (0 to 1), `reason` (short text).
2. It finishes the 4-week replay in under 10 minutes on a laptop, with no network access.
3. It is deterministic given the same input, or documents its seed.
4. It never uses data timestamped after the alert's `ts`.

**You decide.** The approach (rules, statistics, ML, an LLM, a mix), what the associate sees, and how alerts are ranked and grouped. Any language and stack.

**Held-out metric (25 points).** We replay a fourth store and a fifth week that you never see. We score precision and recall of your top 20 alerts per store per shift against real gaps found on the shelf, with credit only for alerts raised at least 2 hours before the gap was found.

**Judged (60 points).** Would a tired associate act on this alert? Is it clear why the item was flagged? What happens at a store with messy data? How would it ship to 200 stores?

**Out of scope.** Hardware such as shelf cameras or sensors, and anything touching real customer data. Everything is synthetic.

**Demo.** 5 minutes. Show an alert reaching a person and what they do next.

**Rules of the road.**
- Coding agents are allowed.
- 10 scored submissions, one every 2 hours at most.
- The scorer and rubric are frozen at kickoff.

### Floor test (sketch, `tests/test_floor.py`)

```python
import json, subprocess, time
from pathlib import Path

REQUIRED = {"store_id", "sku", "ts", "confidence", "reason"}
MAX_RUNTIME_S = 600  # 10 min cap so a replay of 4 weeks stays laptop-friendly

def test_run_produces_valid_alerts():
    start = time.time()
    subprocess.run(["make", "run"], check=True, timeout=MAX_RUNTIME_S)
    assert time.time() - start < MAX_RUNTIME_S
    lines = Path("out/alerts.jsonl").read_text().splitlines()
    assert lines, "no alerts emitted"
    for line in lines:
        alert = json.loads(line)
        assert REQUIRED <= alert.keys()
        assert 0.0 <= alert["confidence"] <= 1.0

def test_no_lookahead():
    # Replay tool feeds events up to alert ts only; this checks logged data access.
    ...

def test_deterministic():
    ...  # run twice, compare outputs
```

---

## Decisions that would change this

1. **Do teams pick a track or get assigned one?** Assignment keeps head-to-head metrics fair. Choosing is more fun but makes the metric tracks uneven.
2. **Do you have real store data, or only synthetic?** Synthetic is safer legally but easier to game. Even a small anonymized sample would improve the held-out set a lot.
3. **Is there a store-ops person who can judge?** If not, the 30 usefulness points are the weakest part of this design.
4. **Who builds the kit?** I estimate 3 to 5 person-days for the shared kit and scorer plus one track. Each extra track costs roughly 1 to 2 days, mostly data generation and validation.

If you want, I can draft Tracks B and C. Two ideas that follow the same pattern are queue and staffing prediction, and a store-associate assistant (judged, no metric).