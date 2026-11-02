**Verdict: Closed.**

The perception stack is the product, not an accessory to it. It's the direct cause of the 0.4% vs 2% mis-pick gap — the one number that wins deals against every competitor. Open-sourcing it gives that number away for free.

**Why this isn't a normal open-source call:**

- Your buyers are warehouse operators and procurement teams, not developers self-serving off GitHub. Open source drives adoption when devs choose the tool themselves. That funnel doesn't exist here — it doesn't lower CAC or fill a pipeline.
- Revenue is a per-arm software subscription. The perception stack is very likely the metered asset. Open-sourcing the thing you bill for undercuts the subscription directly — a competitor or a customer's internal team forks it, and the recurring line disappears.
- 0.4% mis-pick isn't just code — it's code plus fleet calibration data plus a trained grasp-planning model. Publishing the pipeline architecture hands faster-moving competitors the blueprint to close that data/training gap sooner, even if you held back weights.

**Component-level nuance, since "the perception stack" isn't one artifact:**

| Component | Verdict | Why |
|---|---|---|
| Sensor-abstraction layer | Closed (soft call) | Only plausible open candidate — it's glue/interface code, low differentiation. Opening it could earn goodwill from sensor vendors and ease integrations. Not worth it unless you have a specific ecosystem play in mind; default closed until you do. |
| Point-cloud pipeline | Closed | Core differentiator. |
| Calibration toolkit | Closed | Encodes fleet-specific tuning knowledge competitors don't have. |
| Grasp-planning model | Closed | The actual IP behind the mis-pick number. Never open this. |
| Simulation harness | Closed | Internal regression tool. No external audience, no reason to publish. |

**One thing to flag to your head of software:** don't confuse "closed" with "no external engagement." You can still publish benchmarks, write technical blog posts about the *results*, even open a narrow SDK for third-party sensor integration later — without shipping the pipeline, the calibration data, or the model. That gets you credibility without giving away the moat.