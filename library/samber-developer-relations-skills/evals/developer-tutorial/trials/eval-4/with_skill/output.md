**Objective (this is the whole plan — lock this first):** *Receive a webhook, verify its signature, and reject a forged one.* Matches skill's own "strong" objective pattern. Testable: at end, learner does it again unaided on a variation.

**Scope call:** Tutorial confirmed, not how-to. Single path, learning-oriented, audience already past quickstart. No branch needed.

## Hard constraints from your scoping call

| Constraint | What it forces |
|---|---|
| Live Friday | No slack for a second cold-run cycle. One shot at verification. |
| "One-off launch asset," not docs-set foundation | Deletes companion repo + CI-run checkpoints from plan |
| No owner after launch | Deletes polish rung (tests, config, prod shape) from plan |
| 6 hours writing time | Every rung above skeleton+core costs real hours you don't have |

Two separate answers from your leadership (one-off, no owner) both independently rule out the same things. That's not me trimming for style — it's the skill's own decision table.

## Eng lead's 5 asks vs. what the constraints allow

| Ask | Verdict | Why | Swap in instead |
|---|---|---|---|
| Docker Compose | Cut | New environment on top of whatever the quickstart already has running. Skill's own rule: one environment, pinned versions, no second setup tool stealing attention from the concept. | Reuse the app they already have running from the quickstart. Add one route. |
| GitHub Actions workflow | Cut | This is CI-run-checkpoint infrastructure — explicitly deleted by "one-off, no companion repo." Nothing to run it against once the page ships. | The one cold run before ship (below) is the check. |
| pytest + coverage | Cut | Polish rung. No owner means no one keeps a test suite green after Friday. It rots, unowned, becomes technical debt on a page nobody's watching. | The checkpoint itself: send a fixture, assert exact output by hand. That's the "test" a learner runs. |
| Structured logging config | Cut | Polish rung, same reasoning. | One `print()`/log line: `"signature verified"` / `"signature rejected: forged"`. |
| Pipe in real payloads from a sandbox that doesn't exist yet | Cut | Real-data rung is only cheap when the sandbox already exists. Here it's the most expensive rung possible — you'd be blocked on infra that can't exist by Friday. | Two hand-written fixture payloads, inlined in the page: one validly signed, one tampered. Same learning outcome (verify + reject), zero infra dependency. |

**All five map to rungs your own constraints already killed.** Send eng lead the table above — it's a ready answer, not a fight.

## Ladder stop

Default stop is core concept + robustness. This objective bakes robustness in for free — "reject a forged one" *is* the deliberate-failure path, not an add-on. So the ladder is just: skeleton (route responds) → core concept (verify + reject). Real data and polish: cut per above.

## Artifact

One new route added to the app the learner already has running from the quickstart. Not a new project. Verifies + rejects two inline fixture payloads. That's the smallest thing that can't be built without the concept.

**Assumption to confirm with eng lead:** pytest mention suggests Python. Plan below uses Python/Flask as the illustrative stack, reusing whatever the quickstart already set up. If the quickstart's a different language, swap the syntax — the shape (skeleton → verify → reject, two fixtures, one route) doesn't change.

## Outline (fill this, don't draft a full companion repo)

**Before you begin**
| Requirement | Version | Check |
|---|---|---|
| Python | whatever quickstart pinned | `python --version` |
| Brightwake SDK | latest | `pip show brightwake` |
| Webhook signing secret | from quickstart | already in your `.env` |

Assumed knowledge: HTTP request/response basics (link), completed the Brightwake quickstart (link).

**Step 1 — Add a route that receives the webhook** *(skeleton, full code, runs as pasted)*
```python
# app.py — add below your existing routes
@app.route("/webhooks/brightwake", methods=["POST"])
def receive_webhook():
    return "", 200
```
Expected output: `[UNVERIFIED — run and paste real curl+response here before ship]`

**Step 2 — Verify the signature** *(core concept, full code — first time this pattern appears)*
```python
from brightwake import verify_signature  # [UNVERIFIED — confirm real import path]

@app.route("/webhooks/brightwake", methods=["POST"])
def receive_webhook():
    signature = request.headers.get("Brightwake-Signature")  # [UNVERIFIED — confirm real header name]
    if not verify_signature(request.data, signature, WEBHOOK_SECRET):
        return "invalid signature", 401
    return "", 200
```
**Checkpoint 1 — valid payload accepted.** Send the fixture:
```bash
curl -s -X POST localhost:5000/webhooks/brightwake \
  -H "Brightwake-Signature: <signature for fixture below>" \
  -d '{"event":"payment.succeeded","id":"evt_123"}'
```
Expected output: `[UNVERIFIED — real run needed]`
Recovery: no companion repo/branch to reset to (cut per constraints) — recovery is "re-paste the route from step 2."

**Step 3 — Reject a forged payload** *(late-stage: requirement + expected output only — learner reuses step 2's code unaided)*
Send the same fixture with one byte of the signature changed. Should return `401` and the exact string from step 2.
```bash
curl -s -o /dev/null -w "%{http_code}\n" -X POST localhost:5000/webhooks/brightwake \
  -H "Brightwake-Signature: <tampered>" \
  -d '{"event":"payment.succeeded","id":"evt_123"}'
```
Expected output: `401`

**What you built:** a route that verifies a real Brightwake signature and rejects a forged one. You can now: receive a webhook, verify it, reject a forgery.

**Troubleshooting** — candidate entry, confirm real error string during cold run: `[UNVERIFIED]` "signature mismatch with correct secret" → cause: framework parsed the body to JSON before you could read raw bytes; HMAC needs the raw bytes. Fix: read `request.data`, not `request.json`.

**Where to go next:** link to SDK reference for `verify_signature()` only. Skip how-to/explanation links unless those pages already exist — don't build new ones for this.

## 6-hour budget

| Task | Time |
|---|---|
| Confirm environment assumption + cuts with eng lead | 15 min |
| Write + run steps 1–3 for real, fill every `[UNVERIFIED]` block | 2 hr |
| Before-you-begin, what-you-built, troubleshooting entry | 45 min |
| Humanizer pass on prose (not code) | 20 min |
| One cold run: grab any backend engineer, 20–30 min, narrate-aloud, note every hesitation | 45 min |
| Fix what the cold run breaks | 1 hr |
| Buffer | 55 min |
| **Total** | **~5.9 hr** |

Only holds if the 5 cuts above stick. Keep even one (Compose, GHA, pytest, logging, sandbox) and this budget breaks before you write a word.

## Pass threshold for Friday

Criteria 1–4 (real output, checkpoints pass, zero surprise prerequisites, time in-band): covered by the budget above.
Criterion 5 (unaided transfer test) and 6 (trace every hesitation): need that one cold-run engineer. Don't skip this — without it you've shipped a long quickstart with a tutorial's title, which is the exact failure mode this skill exists to catch.

## KPIs

Skip ongoing instrumentation. Nobody owns the page to read a drop-off dashboard. Do the one cold run, report the transfer-test result (pass/fail) to leadership once as launch proof, then stop measuring.

## Next action

Send eng lead the 5-asks table above. Get a yes on the cuts before you write step 1 — every hour spent on Compose/CI/pytest/logging/sandbox now is an hour you don't have Friday.