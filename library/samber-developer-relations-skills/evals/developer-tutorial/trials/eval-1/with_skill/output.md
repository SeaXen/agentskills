Using the `developer-tutorial` skill (Greenfield mode) to produce this outline, per `references/tutorial-outline-template.md`.

## Scope call, out loud

What marketing described — AWS/GCP/Azure, Terraform/console, Postgres/MongoDB, plus a high-volume/low-volume closing section — is a **how-to guide** shape, not a tutorial. Diátaxis calls this exact conflation the most common one in software docs: a tutorial is a single guaranteed path; a how-to forks on the reader's real situation. Five forks on one page would force the learner to resolve decisions before they understand the product, which is the tutorial's #1 failure mode (`Tutorial branches on OS, framework or package manager`).

Resolution, not a rejection of the request:

- **One tutorial**, single path, teaches the transferable skill (wire Quillrail to durable external storage, confirm it survives a restart).
- **Two how-to guides** carry the coverage marketing actually asked for — that content is correctly a how-to guide's job, not a defect to fix in the tutorial:
  1. *Deploy Quillrail to production* — the AWS/GCP/Azure × Terraform/console × Postgres/MongoDB matrix.
  2. *Size your Quillrail index for your workload* — low-volume vs. high-volume tuning.
- The tutorial links both, and previews the second as an optional stretch exercise. Nothing marketing asked for gets dropped; it gets typed correctly so each piece stays maintainable.

## Interview (inferred from your brief — confirm before I write the full page)

| # | Answer | Confidence |
|---|---|---|
| 1. Capability | Deploy a Quillrail index server to AWS with Terraform, wire it to an external Postgres store, prove it survives a restart | Inferred from "deploy to production" + "already ran quickstart" |
| 2. Artefact | One running Quillrail instance, provisioned by Terraform, backed by a real (non-default) Postgres DB | Smallest thing that forces the durable-storage concept |
| 3. Level | Used the product once (ran the quickstart) | Stated |
| 4. Assumed known | Quillrail vocabulary (index, embed, query), basic `terraform plan/apply`, has an AWS account | Stated + inferred |
| 5. Environment | AWS, Terraform ≥1.7, Postgres 13+ — pinned | Chosen (see below) |
| 6. Length | 25–35 min estimate, **not yet measured** | Baseline guess, needs a real cold run before publish |
| 7. Companion repo | **None confirmed to exist.** Required before this can ship — see Blockers | Open question |
| 8. Mode | Greenfield | Stated |
| 9. Test learner | Need a backend engineer who has only run the quickstart, on a clean AWS account | Open question — who? |
| 10. Hard date | Launch date, unspecified | Open question |
| 11. One-off vs. compounding | Treating as **compounding** (every future customer deploying to prod will hit this page) — confirm | Assumed |
| 12. Owner | **No named owner given.** Without one, the polish rung is deleted outright (already is, below) | Open question |

Why AWS / Terraform / Postgres as the canonical path, not GCP/console/Mongo: Terraform matches "backend engineer" more than the console does, it's CI-testable (matches the compounding-asset stop-rung decision), and Postgres is the more common default OLTP store to pair with an idiomatic RDS Terraform resource. GCP, Azure, console, and MongoDB become the how-to guide's forks — they differ from this path only in one or two resource blocks each, so nothing here is wasted when someone writes that page.

## Concept ladder

| Layer | In scope for this tutorial? | Why |
|---|---|---|
| Skeleton | Yes — Step 1 | Terraform apply, instance responds |
| Core concept | Yes — Step 2 | Wired to external Postgres, not the default ephemeral state |
| Real data | Folded into core concept | The external DB *is* the learner's real input — no separate rung needed |
| Robustness | Yes — Step 3 | One deliberate failure path: restart, confirm the index isn't gone |
| Polish | **Cut** | No named owner (open item #12); TLS/IAM/backups/multi-AZ belong in a "harden for production" how-to guide once someone owns this page |

Default stop rung (core concept + robustness) applies unchanged — nothing here promotes a rung, since the real-data case already rides along for free.

## The outline

```markdown
# Deploy a Quillrail index to production on AWS with Terraform

Provision a Quillrail index server on AWS with Terraform, connect it to an
external Postgres metadata store, and confirm it keeps its index across a
restart.

|                       |                                                          |
| --------------------- | -------------------------------------------------------- |
| **Time**              | ~30 minutes (estimate — measure on a real cold run)       |
| **Level**              | Ran the Quillrail quickstart, new to production deployment |
| **You'll need**       | Terraform ≥1.7, AWS CLI configured, an AWS account         |
| **Assumed knowledge** | Quillrail basics (quickstart), `terraform plan`/`apply`    |

## What you'll build

A Quillrail instance running in your own AWS account, provisioned by
Terraform, storing its metadata in a real Postgres database instead of the
quickstart's default in-memory state.

By the end of this tutorial, you'll be able to:

- Provision a Quillrail instance from a Terraform module
- Point Quillrail at an external Postgres store for its metadata
- Confirm a deployment is durable, not just running

## Background

The quickstart runs Quillrail against its built-in, ephemeral metadata
store — fine for a first query, not for production, where a restart or a
redeploy must not lose your index. This tutorial adds the one piece that
makes the difference: an external database Quillrail can trust across
restarts.

## Before you begin

| Requirement | Version | Check |
| --- | --- | --- |
| Terraform | ≥1.7 | `terraform version` |
| AWS CLI, configured | — | `aws sts get-caller-identity` |
| Quillrail API key (from the quickstart) | — | `quillrail whoami` |

Assumed knowledge:

- Quillrail's core vocabulary (index, embed, query) — [quickstart]
- Reading a `terraform plan` diff — [Terraform's own getting-started]

The starter module below owns VPC and networking, so no separate AWS
networking prerequisite is required.

## Step 1: Provision a Quillrail instance

Clone the starter module and apply it as-is — this stands up Quillrail with
its default, ephemeral metadata store, so you have something responding
before you touch persistence.

​```hcl
# main.tf
module "quillrail" {
  source  = "quillrail/quillrail-instance/aws"
  version = "~> 1.0"

  instance_size = "dev"   # smallest size, stays inside the free tier
  region        = "us-east-1"
}

output "endpoint" {
  value = module.quillrail.endpoint
}
​```

​```bash
terraform init
terraform apply
​```

Expected output *(illustrative — replace with a real run before publishing)*:

​```
Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:
endpoint = "https://i-0abc123.quillrail.aws.example.com"
​```

​```bash
curl -s "$(terraform output -raw endpoint)/healthz"
​```

No response? See [Troubleshooting](#error-no-valid-credential-sources-found).

## Step 2: Point Quillrail at your Postgres store

In `main.tf`, add a `postgres_url` variable above the `module "quillrail"`
block you wrote in step 1:

​```hcl
# main.tf — add above module "quillrail"
variable "postgres_url" {
  type      = string
  sensitive = true
}
​```

Then pass it into the module you already have:

​```hcl
module "quillrail" {
  # ...unchanged...
  postgres_url = var.postgres_url
}
​```

​```bash
terraform apply -var="postgres_url=postgresql://user:pass@your-db:5432/quillrail"
​```

Expected output *(illustrative)*:

​```
Apply complete! Resources: 1 changed, 0 added, 0 destroyed.
​```

Connection refused? See [Troubleshooting](#connection-refused).

## Checkpoint: Quillrail is running against durable storage

​```bash
quillrail index create tutorial-demo --dim 384
quillrail query tutorial-demo --vector "[...]"
​```

Expected output *(illustrative — replace with a real run)*:

​```
{ "matches": [...] }
​```

You now have a Quillrail instance backed by real, external storage.

Empty result? The `postgres_url` in step 2 didn't apply — rerun `terraform
apply` and check `terraform show` for the variable.

Want to resume here tomorrow? `git checkout step-2` in the companion repo.
*(Companion repo not built yet — see Blockers below.)*

## Step 3: Confirm the index survives a restart

Replace the running instance and rerun the same query you used at the
checkpoint above — you should get the same result back, not an empty index:

​```bash
terraform apply -replace="module.quillrail.aws_instance.this"
quillrail query tutorial-demo --vector "[...]"
​```

Same result as the checkpoint? Your deployment is durable. A different or
empty result means the instance restarted with fresh state — recheck that
`postgres_url` is set the same way it was in step 2.

## What you built

You can now:

- Provision a Quillrail instance with Terraform, not just the CLI
- Wire it to storage that outlives the instance
- Tell a durable deployment from an ephemeral one, by testing it

Complete config: `step-3` branch of the companion repo *(pending — see
Blockers)*.

**Try it yourself (optional):** your instance above is sized for this demo
index. Before you point Terraform at your own data, guess how
`instance_size` should change for a workload under 100k vectors versus one
over 10M. Then check your reasoning: [Size your Quillrail index for your
workload].

## Troubleshooting

### Error: no valid credential sources found

**Cause:** the AWS CLI has no configured credentials.
**Fix:** run `aws configure`, then retry `terraform apply`.

### connection refused

**Cause:** the Postgres instance's security group doesn't allow traffic
from Quillrail's instance.
**Fix:** add an ingress rule for the Quillrail security group on port 5432.

## Where to go next

- [Deploy Quillrail to production] — GCP, Azure, console-based
  provisioning, and MongoDB, for when your setup differs from this path
- [Terraform module reference] — every variable the `quillrail-instance`
  module accepts
- [Why Quillrail needs external metadata storage] — the architecture
  behind step 2
```

## Blockers to publish (raise with the docs lead / eng owner)

1. **No companion repo exists yet.** Every resume point and "what you built" diff above depends on one, tagged `step-1`/`step-2`/`step-3`, tested in CI against the published Terraform module on a schedule. Without it, checkpoints are unverifiable claims, not resume points.
2. **Every "Expected output" block above is illustrative, not real.** Run list before this can ship: `terraform apply` (step 1), `curl .../healthz` (step 1), `terraform apply -var=...` (step 2), `quillrail index create` + `quillrail query` (checkpoint), `terraform apply -replace=...` + requery (step 3).
3. **Free-tier check unconfirmed.** Confirm `instance_size = "dev"` and a throwaway Postgres stay inside Quillrail's free/trial tier — a billing prompt landing before the final checkpoint breaks the self-serve audience-context rule.
4. **No named page owner.** Given, the polish rung (TLS, IAM least-privilege, backups) stays cut and lives in a separate how-to guide instead of rotting unowned inside this one.
5. **Test learner not identified.** Needs a backend engineer who's only run the quickstart, running this cold on a clean AWS account, before it ships — that run also produces the real output blocks for #2 and the first transfer-test data point.

## Instrumentation (once live)

- Fire a `checkpoint_reached` event at the one checkpoint and at "what you built" — gives per-checkpoint drop-off and completion rate/median time for free off the same events.
- Record transfer-test pass rate from the pre-publish cold run (did the learner complete Step 3 unaided?) and from each later audit.
- Defer support-question tagging and in-product behaviour share (did they deploy for real within a week) until the page has an owner and an identity link between docs and product — wiring that now, with no owner, is the standing job nobody will maintain.