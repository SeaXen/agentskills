Straight talk: the plan as stated has two single points of failure stacked on top of each other — conference wifi *and* a remote staging cluster, live, with no fallback — for a talk where the payoff (rejecting/mutating a real Pod) only happens in the last two minutes. Fix the structure, not just the nerves.

## The core risk to kill first

"My laptop, their wifi" against a remote staging cluster is the single biggest threat to this talk succeeding — bigger than your typing speed. Conference wifi in a packed room is a coin flip; a staging cluster reachable only over that wifi (auth, DNS, firewall rules, VPN) is a second coin flip stacked on the first.

**Swap the live target to a local cluster.** Run `kind` or `k3d` on your laptop, pre-load your image with `kind load docker-image`, and demo against that — zero network dependency for the part that has to work live. Keep the "and yes, this runs against our real staging cluster too" as a single pre-recorded clip or screenshot near the end, not a live dependency.

## Don't build from a truly empty file

"Empty file to working" is a great narrative, not a great risk profile — most of an admission controller's LOC (TLS cert plumbing, webhook registration YAML, RBAC, Deployment manifest) is boilerplate the audience doesn't learn anything from watching you type, and it's exactly the fiddly stuff most likely to eat your clock live.

- Pre-bake: project scaffold, TLS secret/cert already generated, `ValidatingWebhookConfiguration` YAML already written, image already built and pushed.
- Live-type only the part that teaches something: the actual `Validate()` handler logic (~40–60 lines) that inspects the AdmissionReview and decides allow/deny.
- Narrate the pre-baked plumbing ("this is the webhook registration, CA bundle injected, I'm not going to make you watch me generate a cert") instead of typing it. Nobody in the audience has ever complained a live demo skipped boilerplate.

## The safety net: checkpoint commits

This is the highest-leverage trick for any live-coding talk. Tonight, actually write the whole thing end to end, and commit after every logical chunk (server skeleton → handler stub → real logic → cluster wiring). On stage, if you fumble a step, don't debug live — say "let me jump to the working version of this" and `git checkout` the next checkpoint. Audiences respect that completely; silent live debugging is what actually kills talks.

Also: **record a full successful run tonight** (asciinema for the terminal, or plain screen capture) as an absolute fallback. If the cluster/demo dies on stage, play the recording and narrate over it rather than fighting it in front of 200 people.

## Minute-by-minute (20 min)

| Time | Block |
|---|---|
| 0:00–0:30 | Cold open: show the problem (a Pod with no resource limits gets deployed and shouldn't) |
| 0:30–2:00 | 60-second mental model, one slide: API server → webhook → allow/deny/mutate |
| 2:00–2:30 | Show the pre-scaffolded project, explain what's pre-baked and why |
| 2:30–5:30 | Live: HTTP server + `/validate` handler, no-op passthrough, curl it locally with a canned payload |
| 5:30–8:30 | Live: real logic — reject Pods missing `resources.limits`, prove it locally with a good/bad JSON payload (zero network, zero cluster risk — this is your real "aha" moment) |
| 8:30–11:30 | `kubectl apply -f webhook/` against the **local kind cluster** — one command, narrate the pre-built pieces |
| 11:30–13:00 | Payoff: `kubectl apply` a bad Pod (rejected, your message on screen), then a good one (accepted) |
| 13:00–15:30 | Recap + gotchas: `failurePolicy`, `namespaceSelector` (don't brick kube-system), timeouts |
| 15:30–18:00 | Production considerations slide — safe, non-live, compresses if you're running late |
| 18:00–19:30 | Wrap, repo link/QR |
| 19:30–20:00 | Buffer |

If a stage runs long, cut from the back (production-considerations slide first, gotchas second) — never cut your buffer, and never let the live-code block bleed into the payoff block's time.

## What to actually do with your 2 hours

1. **(40 min)** Write the whole thing end to end tonight, confirm it genuinely works once, commit at each checkpoint as described above.
2. **(15 min)** Stand up `kind`/`k3d` locally, pre-load the image, confirm the webhook fires with zero network.
3. **(15 min)** Record the full successful run (asciinema/screen capture), save it locally, confirm it plays with wifi off.
4. **(20 min)** Rehearse the live-typing block twice, out loud, with a timer — first pass rough, second pass for time. This catches overrun risk faster than anything else.
5. **(10 min)** Build 3 slides max: problem, architecture, gotchas/closing. The code is the star, not the deck.
6. **(10 min)** Pack, bump terminal font to 24–28pt with a high-contrast theme, note to arrive early Thursday and test the room's projector/wifi before doors open.

That's ~110 minutes — tight, but it converts a demo with two live single-points-of-failure into one where the only thing that has to work live is logic on your own laptop, with a checkpoint escape hatch and a recorded fallback behind it.