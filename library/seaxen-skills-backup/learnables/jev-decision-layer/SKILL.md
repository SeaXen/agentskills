---
name: jev-decision-layer
description: Use when a decision should be a typed call, not an LLM.
---

# JEV as a decision layer (TypeSafe System One)

## What JEV actually is

JEV is **TypeSafe AI's System One model** — not an LLM, not a router, not a framework. Announced 2026-09-14 (early access 2026-09-15), public model `jev-1.13.0`, endpoint `POST /v1/systemone`, aliases `jev-latest` / `jev-preview`. Named after William Stanley Jevons; "System One" after Kahneman's System 1.

**Contract: unstructured state in, typed probabilistic decision out.** You send `state` (text/JSON/array) plus a dictionary of named `questions`. It returns typed answers. It never generates text, cannot produce type errors, and has no sequential token sampling — all questions in one request are evaluated **in parallel** against the same state.

Three question primitives:
- **Noul** — yes/no proposition → probability it's true.
- **Choice** — pick one declared option → full per-option probabilities + `confidence`.
- **Score** — place on an ordered rubric (list of levels) → score, level distribution, `confidence`.

Specs: 64k tokens per request, but only **32k for `state` + the longest single question**. Text-only input (no image/audio/video — pre-process to text/structured fields). $0.042/M input tokens, **output free**. Rate limits 250k tok/s, 1200 req/min → 429; SDKs retry with backoff and honor `retry-after`. No fine-tuning; shape answers via `state` + `instructions`/`criteria`. English primary; other languages work but need your own eval.

`confidence` = derived from the returned distribution shape (`(n_options × peak_prob − 1) / n_options` for Choice/Score; `|p − 0.5| × 2` for Noul). **It is a routing signal, not proof of correctness.** Thresholds must be calibrated on your own data.

## Division of labor (the rule that matters)

| Component | Owns |
|---|---|
| Deterministic code | arithmetic, permissions, limits, dates, state transitions, all side effects, hard policy, retry caps, idempotency, final authorization |
| JEV | bounded choices / scores / yes-no over supplied state, **atomic** questions only |
| LLM | prose, synthesis, drafting, dialogue, open-ended reasoning, explanations |

Never delegate to JEV: user-facing text, exact calculation, open-ended planning, final authorization, the sole order authority in a trading path. Decompose broad asks ("is this trade safe?") into atomic questions and recombine in code.

**Never treat the "200x faster / 400x cheaper" numbers as benchmark results** — those are TypeSafe's own vendor claims from laptop runs. Latency in practice is ~0.4-1.9s per request. One public critique ("Jev Can't Be Calibrated") argues the calibration claim cannot hold; there is also a `jevchat` project that deliberately misuses JEV as a generator to find the boundary. Treat the output schema as bounded but the judgment as still probabilistic.

## SDK shape (verified)

```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient   # or AsyncTypeSafeClient
with TypeSafeClient() as client:
    r = client.system_one(
        state={"document": "I was charged twice. Please fix this ASAP."},
        questions={
            "billing": Noul(instructions="Is this ticket about billing?"),
            "tone": Choice(instructions="What is the customer's tone?",
                          criteria={"calm": None, "frustrated": None, "angry": None}),
            "urgency": Score(instructions="How urgent is this ticket?",
                             criteria=["can wait", "this week", "today"]),
        },
    )
r.nouls["billing"].noul      # .choices["tone"].choice    .scores["urgency"].score
```
TypeScript: `npm i @typesafe-ai/sdk`, `import { TypeSafeClient, choice, noul, score } from '@typesafe-ai/sdk'`, `new TypeSafeClient({ defaultModel: 'jev-1.13.0' })`, response at `response.answers[...]` with `.choice` / `.noul` / `.confidence`. Key in `TYPESAFE_API_KEY`.

LangChain: `pip install langchain-typesafe`, `TypeSafeClassifier().invoke(state=..., questions={...})`. Experimental middleware gives you model routing (`ModelRouterMiddleware` + `ModelChoice`) and a guardrail (`AutoModeMiddleware(tools=["bash"])`) that blocks risky tool calls before execution.

## Pin the version

`jev-latest` moves under you. The response echoes the versioned `model` that answered — **log it**. If your thresholds are tuned, pin `jev-1.13.0` and upgrade on your schedule. Start in shadow mode (decide + log, change nothing), calibrate, then enforce.

## The 20 "JEV x X" pairings — evidence audit

Checked against `yibie/awesome-jev` (1.8k stars, 15 category files, ~470 entries) and vendor docs on 2026-09-28. **Most pairings in that list are aspirational architecture, not shipped integrations.** Do not write JEV code for these as if a reference implementation exists.

**Tier 1 — real public implementations exist:**
- **Hermes Agent** — `kerpopule/hermes-jev-skills` (878 stars, MIT, 11 plain `SKILL.md` skills: model routing, search ranking, memory passage selection, web injection screening, turn selection, skill selection, triage, mail sorting, computer use, browser use; `install.py`, `jev` CLI, `jev dashboard`, `/jev routing shadow|on`). Plus `anpicasso/hermes-jev-approvals` (20 stars) replacing Hermes's `auxiliary.approval` reviewer with 6 parallel typed questions and a **deterministic rule ladder** on top. Also `wojciechwiesner/jit-context` (Hermes JIT Context OS, claims 31.3% fewer turns). Install: `hermes plugins install anpicasso/hermes-jev-approvals/plugin` + `hermes auth add typesafe-jev` + `hermes config set approvals.mode smart`.
- **LangGraph** — `GiesN/typesafe-jev-workflow`: async LangGraph graph with a typed `Choice` (`invoice`|`general`) routing inbound email.
- **MCP SDK** — several: `agent-chaperone` (MCP proxy + hooks screening tool call *and* tool result, 45 test files), `typesafe-mcp` (exposes `certainty` + `decision: act|review|abstain`), `jev-mobile` (per-step JEV loop alongside Mobile MCP), `BrowserClaw` (JEV micro-loop over pruned DOM).
- **LlamaIndex** — two: `jerryjliu/docjev` (classify documents against NL category rules / find sub-document boundaries) and `WiktorB2004/llama-index-jev` (JEV `Score`s each retrieved passage, `Choice`/`Noul` picks the query engine; reports nfcorpus nDCG@5 0.340 to 0.396 at ~$0.0003/query — unverified vendor-style claim).
- **Semgrep** — `uehaj/jev-semgrep`: semantic grep where JEV scores every line against a meaning, meanings AND-combined, 13-file test suite. Note this is JEV *replacing* pattern matching — the inverse of "judge findings then let code enforce".
- **Cloudflare** — `matthewp/flue-jev-demo` routes via Cloudflare AI Gateway (gateway, not Workers AI binding). `thruwire/foreman` sits above Codex workers, JEV judging completion/sufficiency/human-needed.

**Tier 2 — architecturally sound, zero public JEV integration found:**
Temporal, E2B, Meilisearch, Qdrant, Docling, Graphiti, Langfuse, Promptfoo, Sentry, Playwright, GitHub MCP, PostHog, Resend, Stripe, Cloudflare Workers AI.

The pattern for these is identical and unremarkable: *retrieval systems supply `state`; JEV returns a bounded decision; code enforces.* Retrieval/observability/testing stacks do not need a JEV adapter — they need to pass their payloads into a `system_one` call and branch on the typed answer. Build it yourself, budget 0.4-2s added latency per decision, and note that retrieval quality now bounds decision quality.

**Also worth knowing:** `Notra` routes brand-visibility classifiers off an LLM onto JEV `Boolean` at a 0.5 threshold targeting 300ms p50 (a good "off the LLM onto JEV" precedent); `jev-router` / `pi-jev-router` / `Codex Jev Router` are per-request model routers; flag-gating (`NOTRA_JEV_CLASSIFIERS`) is the standard rollout pattern.

## Gotchas

- Cardinality caps at 255; above that JEV runs a 2-stage score-then-choose and slows down. Accuracy also shifts as `state` grows ("jaggedness") — pin state size, not just the model.
- `instructions` and `criteria` are the *entire* tuning surface. Write criteria as human-readable descriptions, not enum labels.
- Malformed or missing answers should **raise**, so the caller fails safe to escalate — never fail open to the model's raw guess.
- Scope confidence to authority: a high confidence only authorizes what that scope already allows.
- awesome-jev warns explicitly against same-day bulk submissions sharing one scaffold and thin commit history — volume is not quality, and listing is not endorsement.
