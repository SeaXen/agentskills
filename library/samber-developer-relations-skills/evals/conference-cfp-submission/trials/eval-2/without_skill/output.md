One quick flag before the deliverable: the CFP explicitly anonymizes authors in round one, and this abstract puts Marbleline in the title and the opening line — that's a deliberate call to trade blind-review neutrality for credibility, not a mistake, but worth being aware you're making it. Case-study talks often do lean on the company name this way (it's central to the story, not just a plug), so it's a reasonable trade, not a rules violation.

Title (68/80 characters):

**How Marbleline Rebuilt Its Retry Layer After 1,900 Duplicate Charges**

Abstract (1,103/1,200 characters):

At Marbleline, we believe idempotency is a product feature, not an implementation detail. We're the payments infrastructure behind roughly a third of Nordic card processing, and our retry layer failed quietly for weeks before it surfaced as duplicate charges on 1,900 customers.

This talk walks through the incident: a race between client-side retries and a stateful idempotency-key cache that let duplicate charges slip past two independent safety nets, why monitoring never caught the pattern, and the rebuild that followed. We cover the concrete decisions: moving idempotency keys from an in-memory cache to a durable, request-scoped ledger; redesigning retry and backoff semantics around at-least-once delivery instead of assuming exactly-once; and the contract tests and chaos experiments we now run against every payment code path before it ships.

You'll leave with a checklist for auditing your own retry logic, a mental model for reasoning about idempotency across distributed services, and an honest account of what our first incident fix got wrong: the patch that looked complete and wasn't.