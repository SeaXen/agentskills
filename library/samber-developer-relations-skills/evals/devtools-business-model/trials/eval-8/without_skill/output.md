## Braidmark pricing: adding a per-call charge

**Diagnosis is right, mechanism is wrong.** Seats stopped tracking value the moment usage went machine-driven. Three flat quarters of seats while calls tripled isn't stagnation — it's the value metric decoupling from actual consumption. That part of finance's read is correct: uncaptured value is sitting there. But "flat per-call charge, bolted on top, same accounts, today" will cause real damage before it captures any of it.

**Three problems with the proposal as stated:**

- **Raw API calls are the wrong meter.** Coding agents retry, poll, and re-issue calls in ways a human opening a migration never did. Metering the call itself charges for noise, not for delivered value — and it's the easiest metric in the world for customers (or their agents) to route around by batching, which just trains bad behavior and generates support tickets.
- **"On top, same accounts, day one" reads as a stealth price increase.** These are existing customers with no new tier, no opt-in, no notice. The accounts hit hardest are exactly the ones who integrated deepest (CI + agents) — punishing your best-adopted customers first is backwards.
- **CI usage and agent usage aren't the same thing.** CI-triggered migrations are predictable, budgeted, recurring — a legitimate usage-pricing candidate. Agent-triggered calls likely include failed attempts, dry runs, and exploratory retries. Charging both at full price treats waste as value.

**What to do instead:**

1. **Meter the outcome, not the transport.** Charge per successfully applied migration (or per connected repo/database under management), not per API call. Harder to game, easier for a customer to predict, and it actually correlates with what they're getting.
2. **Bundle before you meter.** Give every seat an included migration allowance, then charge overage beyond it. Low-usage seat customers see zero change — only the accounts actually driving the 3x see a new line item. This is the difference between "you found new value" and "you found a way to bill everyone more."
3. **Exclude failed/retry calls from the meter**, at least initially. Bill on success, not attempts — otherwise you're charging agent customers for your own product's retry behavior.
4. **Phase the rollout.** New customers get the new model first — clean read on acceptance, no relationship at risk. For existing high-usage accounts, give advance notice, explain the why (their own CI/agent footprint, not an arbitrary hike), and offer a temporary credit or grace window before the meter goes live. Never flip it for the whole base on one date.
5. **Reframe internally before reframing externally.** Tell finance: this isn't "add a usage fee," it's "fix a value metric that broke." The pitch to customers should be the same — "seats for people, usage for the automation you've wired in" — not a surprise charge that shows up on next month's invoice.

**Net:** agree with finance that seats alone are leaving money on the table. Don't agree that raw-call metering stacked onto current accounts is how you collect it — that version trades a real pricing win for a churn risk and a support-volume problem, for the accounts you can least afford to lose.