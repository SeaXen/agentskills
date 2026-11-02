## Second opinion: customer-Python sandboxing architecture

**Bottom line:** The gVisor direction is technically sound in isolation, but the plan is scoped wrong for an 8-person team, understates the real cost, and jumps to "build a secure multi-tenant code execution platform" before ruling out cheaper options. I'd pump the brakes before committing a quarter of your total eng capacity.

### 1. The estimate is the biggest red flag

A quarter covers *building* a sandbox. It doesn't cover *owning* one. Once customer Python runs in your infra, you've taken on a permanent security surface that needs:

- Ongoing gVisor CVE tracking and patching (gVisor has had guest-escape vulnerabilities before — it reduces syscall attack surface, it doesn't eliminate it).
- Dependency supply-chain risk if customers can `pip install` — a malicious or compromised package now runs inside your infra with proximity to other tenants' data.
- Audit logging of what customer code touched and produced — not optional for a bank or healthcare customer, and probably not in the quarter estimate.
- Incident response: a documented kill-switch to disable all customer-code execution instantly, and a plan for what you tell Corveth Bank if you ever have to pull it.
- Support burden: customers *will* write buggy Python and file tickets against your platform for what is actually their bug.

None of that is a one-time cost. Compare against how long comparable platforms (Lambda-style multi-tenant execution, Modal, E2B, Daytona) took to get trustworthy — years, with dedicated teams, and they still treat isolation as a live, funded workstream, not a shipped feature. A quarter, for a team of 8 who also run the core product, likely means the compliance/observability/incident-response pieces get cut to hit the deadline — and those are exactly the pieces that matter for these two customers.

### 2. The threat model doesn't match the customer profile

You're building the riskiest kind of feature (arbitrary code execution, multi-tenant) for the two customers with the least tolerance for a mistake — a bank and a healthcare group. A cross-tenant data leak or resource-exhaustion incident here isn't "bad," it's potentially a regulatory event and a reference-customer-turned-lawsuit. That argues for *more* scrutiny than a standard feature, not a standard quarter-sized project slot.

Also: CPU quotas alone don't isolate a tenant. You need memory limits, disk I/O limits, wall-clock timeouts, process/fork limits, and — most importantly — **network egress control**. Nothing in the description mentions network isolation, and that's the dimension most likely to turn "sandbox escape" into "data exfiltration."

### 3. Cheaper alternatives to rule out first

- **Don't own the isolation boundary — rent it.** For 2 customers, paying a specialized sandboxed-execution vendor (Modal, E2B, or even wrapping cloud-native isolation like Fargate/Cloud Run with strict per-tenant IAM and VPC boundaries) is far cheaper than an in-house gVisor platform, and you inherit a security team you don't have to hire.
- **Shrink the language, not just the sandbox.** "Customer wants to write validation logic in Python" doesn't necessarily mean "arbitrary Python with full syscall access." A restricted execution domain — RestrictedPython, or a small DSL that only exposes data-quality primitives (row/column checks, joins, aggregations) — removes most of the attack surface gVisor exists to contain. If the real ask is "let me write a formula, not call the rule builder UI," you may not need a general-purpose sandbox at all.
- **Push execution outward instead of pulling code inward.** A bank and a healthcare org may actually prefer their validation logic never leaves their environment. An agent model — customer runs a small connector in their own VPC, you orchestrate and ingest results — eliminates the multi-tenant execution problem entirely and lines up with compliance postures these customers likely already have (data residency, no third-party code execution).

### 4. Validate demand before the build

Two accounts out of 120 want this. Before allocating what's probably 15-25% of a quarter's total engineering capacity to it, get concrete: what specific validations do Corveth Bank and the healthcare group actually want to write? If it's a handful of patterns (cross-field consistency, outlier detection, custom regex, cross-table joins), extending the rule builder with a formula/expression mode likely covers it at a fraction of the risk and cost — and stays useful to all 120 accounts, not 2.

If it turns out to be genuinely open-ended logic that only a general-purpose language supports, that's a real signal to keep building toward sandboxed execution — but get that signal from customer conversations, not from the staff engineer's first design pass.

### 5. If you proceed anyway

- Treat this as a security-critical build, not a features build: get an external pen test or security review before either customer's code runs against production data, given the compliance stakes.
- Add network egress allowlisting and memory/disk/wall-clock limits to the design — CPU quota alone is not tenant isolation.
- Decide the package/dependency story explicitly (fixed vetted set vs. arbitrary `pip install`) — this is a materially different risk profile and should be a conscious choice, not a default.
- Build the audit trail and kill-switch as part of the initial quarter, not a fast-follow — they're the two things a bank/healthcare security review will ask for first.
- Re-estimate with patching/monitoring/support as an ongoing tax, not a sunk cost, so the "quarter" number reflects what this actually costs the team over the next year.

**Recommendation:** Don't greenlike the quarter yet. Spend a week getting concrete requirements from both customers and pricing out a rented-isolation or restricted-DSL alternative. If arbitrary Python genuinely turns out to be required, resize the estimate to include the ongoing security/compliance ownership cost, and get an outside security review of the design before committing engineering time — for these two customers specifically, "second opinion" should include someone whose job is breaking sandboxes, not just an internal review.