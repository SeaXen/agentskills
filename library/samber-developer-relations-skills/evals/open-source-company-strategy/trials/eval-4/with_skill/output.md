Using the `open-source-company-strategy` skill (plus its five reference files: strategic-motives, boundary-tests, company-type-and-authority, operating-model, published-findings) to produce the verdict. The interview normally runs one question at a time, but since you asked for the complete answer directly, I've filled interview gaps with stated assumptions (flagged inline) rather than pausing — flag if any assumption is wrong and the affected rows should be re-run.

**Assumptions made in place of the interview:** no external trigger (no customer/regulator demanding this, no hyperscaler already circling) — this is internally raised by your head of software; nothing is open today; buyers are enterprise warehouse operators with procurement/legal review, not developers; no fixed deadline; this is being asked as a one-time asset decision, not yet a standing policy.

---

# Open source strategy — Nyx Robotics perception stack

## The one-line answer to "is the perception stack open or closed?"

Neither — that's the wrong question. The perception stack is five assets, not one, and they don't share a verdict. Two open, one closed outright, two not yet. Treating it as a single yes/no is exactly the failure mode this process exists to catch: the differentiating layer (grasp-planning model) and the plumbing around it (sensor abstraction, calibration) have opposite answers, and collapsing them into one verdict either gives away the moat or needlessly keeps commodity infrastructure locked up.

## What we sell

Warehouse picking robots (hardware) plus a per-arm software subscription. The subscription is, in substance, billing for continuous access to and improvement of the perception stack's accuracy — the 0.4% mis-pick rate against a 2% industry rate is the sales argument. Customers aren't buying "a robot arm," they're buying that number. That fact governs every row below.

## Motive — named and stress-tested

**Primary: Talent.** No external party is forcing this, so the strongest surviving internal motive is recruiting and retaining perception/robotics engineers — a market you compete for against better-funded rivals (Covariant, Dexterity, Amazon Robotics, RightHand Robotics, and every self-driving alum). Sensor-abstraction and calibration work is legitimately resume-worthy engineering; a well-run, narrow open repo is bait a build script never is. Evidence test passes only for the enabler layer — it does not extend to the grasp-planning model.

**Secondary: Lower maintenance through upstreaming.** If your calibration toolkit and point-cloud pre-processing sit on top of existing open ecosystems (ROS, PCL, Open3D, Kalibr-style approaches), a private fork of that plumbing is a maintenance tax you repay at every upstream version bump. Contributing fixes upstream, or open-sourcing your own layer on top, converts that into shared maintenance — but only for the generic parts.

**Rejected, and why each fails its own test:**
- *Commoditize your complement* — fails immediately. Name the product whose demand should rise: there isn't one distinct from the perception stack itself. You'd be commoditizing the exact thing you sell, the same mistake Spolsky flags in Sun's Java.
- *Demand pull* — nothing stated; no customer or regulator is conditioning a deal on this. If that changes (a customer conditions a renewal on auditability of the safety-relevant parts), re-run this section — demand pull is a trigger, not itself a verdict.
- *Cost sharing* — no other organization named as a co-funder. Publishing code alone isn't cost sharing.
- *Trust/auditability* — plausible in robotics safety generally, but no deal, audit, or compliance review was named where source access was actually requested. Second-order benefit at best right now.
- *Block a competitor from owning a standard* — nobody is currently trying to own a warehouse-perception standard against you. Worth revisiting only if one of your rivals starts pushing an open competing stack as a de facto standard.

## Open

| Asset | Motive served | G1 irreversible | G2 differentiating | G3 value capture | G4 contributable | G5 owner | Verdict |
|---|---|---|---|---|---|---|---|
| Sensor-abstraction layer | Talent, upstreaming | permanent, fine — it's an interface, not the model | context/enabler — swaps camera/LiDAR vendors, doesn't move the mis-pick number | moat stays in grasp model + calibration + hardware integration + trademark; a HAL alone hands nobody your accuracy | yes — this is exactly the shape of thing robotics engineers already contribute to (ROS-adjacent precedent) | **name required before shipping** — assign one perception engineer, ~10%/wk | Open (interface-open) |
| Calibration toolkit | Talent, upstreaming | permanent, fine | context — extrinsic/intrinsic calibration is table-stakes; open toolkits (Kalibr et al.) already exist industry-wide, so you're not conceding anything unique | competitors already have alternatives; you don't monetize calibration standalone | yes, mature problem space with an established contributor audience | **name required before shipping** — same owner or backup, ~5%/wk | Open (infrastructure-only) |

## Closed

| Asset | Motive served | Gate failed | Verdict |
|---|---|---|---|
| Grasp-planning model | none survives | **G1 (irreversibility), outright veto.** If this can never be closed again — does the decision change? Yes, immediately: this model is the mis-pick-rate advantage the subscription bills for. Opening it lets any competitor, including a well-funded new entrant, fine-tune it onto their own arm and match your headline number for free. G2 and G3 fail identically (purely differentiating; no separate value-capture mechanism exists once the model itself is public — the subscription price *is* the value of this exact asset). | **Closed.** Not "not yet" — there's no stated condition that flips this without a change to the entire business model. |

## Not yet

| Asset | Condition that would flip the verdict |
|---|---|
| Point-cloud pipeline | Currently fails G2 run holistically — as described, it's bundled with the warehouse-specific tuning (occlusion handling, reflective/plastic packaging, lighting extremes) that's part of *why* the mis-pick rate is 0.4%, not generic PCL/Open3D-style preprocessing. Per gate 2's rule, run it twice: split into (a) a generic point-cloud utility layer — format conversion, basic filtering, registration — and (b) the warehouse-tuned segmentation/denoising. (a) is a plausible future Open row; (b) stays with the grasp-planning model's verdict. Flip condition: engineering time to do that split and re-score each half separately. |
| Simulation / regression harness | Fails G4 as currently bundled. The harness *engine* (replay point clouds, score against ground truth) is generic infrastructure and could pass all five gates on its own. But it's inseparable right now from the scenario/test-case library — the specific bin configurations, SKU edge cases, and field-failure cases you've learned to handle. That library is a distilled map of exactly what to fix to reach your accuracy, which is more damaging to hand a competitor than the model itself is easy to copy. Flip condition: fund separating engine from scenario corpus, then re-score the engine alone. |

## Competitive case

Named adversary: a funded warehouse-robotics rival (Covariant, Dexterity, Berkshire Grey, RightHand Robotics — pick whichever is your closest head-to-head) or a hyperscaler entering the category with a bundled perception stack of their own.

If they took everything in the **Open** row above: they get a sensor HAL and a calibration toolkit — both already reproducible from public robotics research and existing open tools. You lose nothing you currently bill for.

If they took the **Closed** row (hypothetically, if you'd opened it as your head of software's original framing implied): they get the exact model responsible for your 5x-better mis-pick rate, integrate it onto their own hardware, and your per-arm subscription no longer has anything unique to sell. This is the scenario that must never happen — it's also the reason the original question ("is the perception stack open?") was dangerous as posed: a yes answer at the wrong granularity is irreversible and directly cancels your Series C thesis.

What you still hold under the recommended line: the grasp-planning model, the warehouse-tuned point-cloud logic, the accumulated scenario library, the physical robot and its integration, the trademark, and the customer relationship the per-arm subscription is billed against.

## Decision rights

- **Business-context call** ("should we open this specific asset") — Head of Software owns the day-to-day scoping (sensor-abstraction, calibration), but anything touching the grasp-planning model or point-cloud tuning escalates to CEO/board sign-off. At Series C, investors are underwriting the perception-stack moat directly; treat that model's boundary as a board-visibility item, not an engineering call, the same way Google escalates anything touching its own "secret sauce" past the launch creator's manager.
- **Compliance review** (is this okay to release), run in parallel, never as the decider — general/IP counsel checks: patent filings in flight on grasp-planning or calibration methods (publishing before filing can jeopardize claims), trade-secret status, and whether any released code or config accidentally embeds customer site data or proprietary sensor tuning constants (a release checklist should scan for this before the sensor-abstraction and calibration repos go out).
- Default posture on the two Open rows: approve. Default posture on anything touching grasp-planning: no, escalate.

## Commitments (publish these, not a generic "we love open source" line)

1. The grasp-planning model and the warehouse-tuned perception logic behind our mis-pick rate will not be open-sourced without a board-level strategy change — named explicitly so no individual engineer casually publishes a notebook, a checkpoint, or a fine-tuned config that reconstructs it.
2. Once published, the sensor-abstraction layer and calibration toolkit will not be pulled back closed, and no artificial limits will be added to punish external adopters.
3. Any future change to this boundary — in either direction — is announced before it lands, with the reasoning stated.

## Operating model

- Owner: one perception/platform engineer, ~15% time blended across both open repos, named before either ships (currently unnamed — this is the one gate-5 gap standing between "ready to open" and "not yet" on the two Open rows).
- Release checklist before either repo goes out: license file, notices, secrets/config scan (specifically: no customer warehouse data, no proprietary calibration constants), dependency license audit, security contact, trademark check.
- Legal: general counsel at release time, IP counsel for the patent-timing question above.
- Estimated annual cost: roughly $30–60k fully loaded (maintainer time + periodic legal review) — order-of-magnitude, not a quote; scale down further if only the calibration toolkit ships first and the sensor HAL follows later.
- Upstream-first: if either component already leans on ROS/PCL/Open3D-style ecosystems, default to contributing fixes upstream before maintaining a parallel private version — this is where the "lower maintenance" half of the motive actually gets paid back.

## Measurement and re-evaluation trigger

Per-asset objective, declared now rather than retrofitted:
- Sensor-abstraction layer / calibration toolkit: external forks or contributions within 12 months, and candidates citing the repos in hiring conversations. Not stars, not downloads.
- Grasp-planning model: no signal needed — it's closed. Re-open the question only if a competitor ships an open equivalent that neutralizes the moat, or if you shift from trade-secret to patent protection as the value-capture mechanism.
- Point-cloud pipeline / simulation harness: re-evaluate once the recommended split work is funded; success on the generic half = at least one external contribution within 12 months, or the maintenance argument didn't hold and it should have stayed closed.

Trigger an early re-read (don't wait for the next planning cycle) if: a competitor announces an open perception stack, a hyperscaler enters warehouse picking, a fork of either open repo appears, the named maintainer leaves, or a customer starts conditioning a deal on source access to any part of the stack.

## Brief self-check against the skill's pass threshold

✅ every candidate asset appears exactly once (Open/Closed/Not yet) · ✅ one primary motive named with its evidence test · ✅ value-capture answers are mechanisms, not "the license," and the adversarial scenario names a specific competitor class · ✅ decision rights split business call from compliance review · ✅ commitments stated · ⚠️ named owner and annual cost are placeholders pending your sign-off on who and how many hours — fill this in before either repo actually ships, or the two Open verdicts aren't ready yet.