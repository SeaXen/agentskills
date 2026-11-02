## Bottom line

Scrap the live-build-from-empty-file plan. Three independent reasons kill it, before we even get to structure:

- **Rehearsal ceiling.** The skill's own rule: *"a low rehearsal ceiling deletes progressive construction and unscripted live typing outright rather than offering them."* You have ~2 hours total. Progressive construction (build-from-nothing) is the single most expensive arc to rehearse, and unscripted live typing is the single riskiest demo tier. Stacking both on 2 hours of prep isn't a plan, it's a coin flip on stage.
- **Ratio problem.** 12 minutes of typing inside a 20-minute slot is 60% of the talk. That leaves ~8 minutes for hook, promise, the actual lesson, and the arrow — and it puts the demo at the end, which the skill flags directly: *"Never end on the demo... an overrun cannot eat the conclusion."*
- **⚠️ Compliance risk, not just talk-craft.** "My laptop, their wifi" against a real staging cluster, live, possibly recorded, means: conference wifi drops (routine, not exotic), and any `kubectl get` against staging puts real internal hostnames/namespaces/config on a public — maybe recorded — screen. That's a harder line than a bad demo; it's internal detail leaving the building.

You already own better material than a from-scratch build: the actual dead ends you hit *while building this for real*, in the last however-many weeks. That's an Incident or Problem→dead-ends arc, and it's cheaper to prep than a live build because it's recall, not construction.

**One open question, answered both ways below so this is usable either way:** did building this admission controller cause a real near-miss or outage (e.g., a bad `failurePolicy: Fail` freezing scheduling cluster-wide)? If yes → Incident arc (cheapest, most credible). If no → Problem→dead-ends→insight arc using the same material, framed as "here's what nearly went wrong" instead of "here's what did." Everything below is written for the incident version; swap the hook and pillar 1 framing to hypothetical if it's the second case.

---

**Arrow**
> "`failurePolicy` is the difference between a webhook that misbehaves and a cluster that stops scheduling anything."

**Arc**
Incident (or Problem→dead-ends→insight if there was no real outage). Rejected: progressive construction (no rehearsal budget for a live build), contrarian (no time to build attack-proof evidence), sparkline (this is a 20-minute technical slot, not a keynote). Efficiency/effort ranking for your timeline: incident and migration are recall — you select and order, you don't invent and verify. That's what fits 2 hours.

**Pillars**
1. **A webhook sits in the write path, synchronously, before anything reaches etcd — it isn't a filter bolted on the side.** Evidence: [fill in your real dead end — most likely candidate given the shape of this bug class: a webhook that was slow/unreachable/cert-mismatched with `failurePolicy: Fail`, and every `apply` in the cluster hung or errored until the webhook was pulled]. Use the real number: how many minutes, how many namespaces affected.
2. **Four knobs make it safe: `failurePolicy`, `timeoutSeconds`, `namespaceSelector`, and a canary rollout before `Fail`.** Evidence: the actual config diff you run in staging today — screenshot it, don't retype it live.

**Realization**
Minute ~6, end of pillar 1: "we used to think a webhook just checks things; we now know it's in the critical path of every write to the cluster." Hold the request-flow diagram silently for a beat here — this is the one slide that must never get cut.

**Time budget** (20 min, assuming Q&A is scheduled separately — confirm with organizers; if Q&A is inside the 20, cut 2 min from pillar 2)

```
0:00-0:01  hook — the near-miss, one sentence, one number, no setup
0:01-0:02  promise + scope — what you'll leave able to tell apart; "not for you if you don't run your own webhooks yet"
0:02-0:08  pillar 1 — webhook in the write path + the dead end → realization at ~0:06
0:08-0:13  pillar 2 — the four knobs + the config diff
0:13-0:17  demo — pre-recorded screencast, seeded local cluster (kind/minikube), NOT staging, NOT live
0:17-0:19  arrow restated + link slide
0:19-0:20  hard stop / buffer
```

**Demo, specifically: record it tonight, don't perform it Thursday.** Ranked by proof-per-hour of prep, a narrated screencast against a seeded local cluster beats a scripted live demo beats unscripted live typing — and it's also the only tier that needs zero venue wifi and shows zero staging internals. Holman's line applies directly here: *"Live demos are like Global Thermonuclear War: the only way to win is to not do a live demo in front of hundreds of strangers in the first place."* State what to watch before it plays ("watch which pod gets rejected, not the terminal scroll") — an unnarrated demo reads as filler even recorded.

**Slide skeleton** (count is an outcome, not a target — this is ~13, that's fine for 20 minutes)

| # | Slide must accomplish | Notes |
|---|---|---|
| 1 | Title + handle | |
| 2 | The near-miss, one sentence, no explanation | **Never cut** |
| 3 | Blast radius in one number | e.g. "N minutes, every apply blocked, cluster-wide" |
| 4 | The promise: safe vs dangerous policy, tell them apart afterward | |
| 5 | Scope, out loud: not for you if you don't run webhooks yet | Section marker |
| 6 | Section marker: "A webhook is in the write path" | |
| 7 | Request-flow diagram, webhook step marked; hold it, say nothing for a beat | **Never cut** — this is the realization |
| 8 | "It's a gate, not a filter" | Pillar 1 landed |
| 9 | Section marker: "Four knobs make it safe" | |
| 10 | `failurePolicy` / `timeoutSeconds` / `namespaceSelector` / canary — one line each | |
| 11 | The config diff that ships today | Highlight changed lines only |
| 12 | DEMO — say what to watch first | Checkpoint: past 0:13, skip to slide 14 |
| 13 | Arrow restated, verbatim from slide 4's promise | **Never cut** |
| 14 | Repo + docs + handle | Repeats a link from earlier; stays up through Q&A |

**Cut checkpoints**
- Past 0:08 at slide 9 → drop to 2 of the 4 knobs (`failurePolicy` + canary only), point at the diff slide for the rest.
- Past 0:13 at slide 12 → skip the demo entirely, show a static before/after results slide instead (prepare this as insurance now, while recording the screencast), go straight to the arrow.
- Never cut: slide 2 (hook), slide 7 (realization), slide 13 (arrow).

**Rehearsal plan** — built for ~2 hours, not the skill's full accordion ladder

*Tonight (Monday), budget ~90 min:*
- 15 min: lock the arrow, both pillars, and your real incident numbers into this outline.
- 35 min: **build the seeded local demo** (kind/minikube, fake namespace names, no staging) and **record 2-3 takes**, keep the cleanest. This is the highest-leverage 35 minutes you have.
- 20 min: build the slide skeleton above, reusing any diagram you already have from the actual build.
- 15-20 min: say the talk out loud once at 3 minutes, then once at 1 minute. Skip the full 3→2→1→0.5 ladder — no time for it. What survives the 1-minute pass is your real arrow and pillar order; what falls off is your cut list, in cut order (don't guess this yourself, let the compression tell you).

*Whatever pockets remain Tue/Wed:*
- One full 20-minute run with a phone timer, out loud, ideally to one colleague or over a call. If only one rehearsal slot exists in your whole week, spend it here, not on more slides.
- Thursday morning: don't touch slides. Re-check the cut checkpoints once. Play the recorded demo once on the actual laptop to confirm it runs **fully offline** — audio, resolution, no dependency on venue wifi at all.

**Honest gate check:** the skill's full bar is two consecutive in-budget timed runs. Two hours won't get you there — say so to yourself now rather than discovering it Thursday morning. The realistic bar for this budget: one full timed run, a demo that's pre-recorded and offline-tested, the three never-cut slides locked, and the arrow said back correctly by one other person before you're on stage.