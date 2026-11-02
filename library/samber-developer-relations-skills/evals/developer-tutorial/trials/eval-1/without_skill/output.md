# Deploy Quillrail to Production — Tutorial Outline

## Format note

This isn't a linear step-1-through-N tutorial. Three independent choices (cloud, provisioning method, database) mean most readers only care about one path through the content. Structure it as a **decision-tree tutorial**: a short shared spine (overview, prerequisites, architecture) that funnels into path-specific tabbed sections, reconverging for the tuning close. Use tabs (AWS/GCP/Azure, Terraform/Console, Postgres/MongoDB) rather than duplicating full prose per combination — 3×2×2 = 12 combinations would bloat the page and rot fast when one cloud's console changes.

Estimated time: 45–60 min for one path (cloud + provisioning method + one DB), not the full page.

---

## 1. Title & Meta

- **Title:** Deploy Quillrail to Production
- **Time:** 45–60 min (per path)
- **Level:** Intermediate — assumes quickstart completed
- **You'll need:** a cloud account (AWS, GCP, or Azure), admin/owner-level IAM in that account, and connection details for your existing Postgres or MongoDB instance

## 2. Overview

- One paragraph: what "production" adds over the quickstart (persistent infra, real data source, sized indexes, no more local/sandbox API key)
- Upfront **decision matrix** (table) so readers self-select before reading further:

  | Choice | Options | Depends on |
  |---|---|---|
  | Cloud | AWS / GCP / Azure | where your other infra lives |
  | Provisioning | Terraform / Web console | whether you use IaC today |
  | Database | Postgres / MongoDB | what you already run |

- Callout: "Pick one row per column, then jump directly to that section — you don't need to read the other tabs."

## 3. Prerequisites Check

Skip anything already covered by the quickstart (API key, SDK install, local test call). Cover only what's new for production:

| Requirement | Check command / where to get it |
|---|---|
| Cloud account with billing enabled | — |
| IAM permissions to create compute + networking resources | cloud-specific role list |
| Terraform ≥ 1.5 (Terraform path only) | `terraform -version` |
| Console access with project/subscription owner role (Console path only) | — |
| Postgres ≥ 13 or MongoDB ≥ 6 connection string, reachable from the cloud you're picking | `psql "$CONN_STRING" -c 'select 1;'` or `mongosh "$CONN_STRING" --eval 'db.runCommand({ping:1})'` |
| Production Quillrail API key (distinct from quickstart's sandbox key) | Quillrail dashboard → API Keys → Production |

## 4. Architecture Overview

- One diagram: Quillrail service ↔ your VPC/network ↔ your Postgres/MongoDB as system of record ↔ client apps
- Short explainer of what Quillrail stores itself (vector index) vs. what stays in the source DB (source-of-truth records), so readers understand *why* a DB connection is required at all, not just *how* to configure it

## 5. Deploy Quillrail to Your Cloud

Sub-tabs: **AWS | GCP | Azure**. Each tab covers the same four beats so readers can pattern-match across clouds if they ever switch:

1. **Identity setup** — service account / IAM role Quillrail's deploy needs, least-privilege permission list
2. **Networking** — VPC/subnet choice, inbound rule for Quillrail's port, whether a public endpoint or private link is expected
3. **Provisioning** — inner tabs **Terraform | Web console**:
   - *Terraform:* link to the official Quillrail module, minimal `main.tf` (provider block, module call, required variables), `terraform init && terraform apply`, expected plan output
   - *Console:* numbered click-through (Create → select region → select instance size → confirm), with a screenshot placeholder at each state-changing step
4. **Checkpoint** — `curl https://<your-instance>/healthz` returns `200`; note what a non-200 means and point to Troubleshooting

Repeat this shape identically for GCP and Azure — same four beats, cloud-specific commands/screens.

## 6. Wire Up Your Database

Sub-tabs: **Postgres | MongoDB**. Each covers:

1. **Credentials & secrets** — where Quillrail expects the connection string (env var vs. secrets manager reference), least-privilege DB user/role to create for Quillrail (read-only vs. read-write, depending on whether Quillrail only indexes or also writes back)
2. **Schema / collection requirements** — what shape Quillrail expects (required columns/fields for the vectorized content + ID), how to point Quillrail at an existing table/collection vs. a new one
3. **Sync mode** — one-time backfill vs. continuous sync, and the config flag/setting that controls it
4. **Checkpoint** — trigger a small backfill, then run one test query against Quillrail and confirm it returns records that trace back to real rows/documents in the source DB

## 7. Tune Index Size for Your Workload

Closing section, cloud- and DB-agnostic — this is where the two paths reconverge.

- **Low-volume workload** (dev teams, internal tools, <1M vectors): smallest supported index tier, single node, cost-optimized — show the config value and expected monthly cost order of magnitude
- **High-volume workload** (customer-facing, >10M vectors or high QPS): sharding/replica guidance, memory sizing formula (vectors × dimensions × bytes-per-dim, with a worked example), when to move off the shared tier
- **How to tell which one you are** — a short heuristic (expected vector count + peak QPS), not a rigid threshold, since "high volume" is relative to plan tier
- **Resizing later** — confirm this isn't a one-way door; link to the resize/migration doc
- **Checkpoint** — run a benchmark query at your expected peak QPS, compare p50/p99 latency against Quillrail's published SLA numbers for your chosen tier

## 8. Complete Reference Config

- Full `main.tf` per cloud (all three, collapsed/tabbed) for readers who skimmed the step-by-step and just want the end state to copy
- Full console configuration checklist per cloud, same purpose for the non-Terraform path

## 9. Troubleshooting

Cover at minimum:

- Health check returns non-200 after provisioning (per cloud: most common cause is the networking rule from step 5.2)
- Quillrail can't reach Postgres/MongoDB (firewall/security group missing the DB's inbound rule, or DB requires SSL Quillrail isn't configured for)
- Backfill stuck/slow (usually undersized index tier for the data volume — point back to section 7)
- Terraform apply fails on IAM permission errors (missing role from section 5.1)
- Query latency far above SLA post-launch (index tier mismatch — link back to tuning section, not a new fix)

## 10. What You Built

- Recap: production Quillrail instance, running on your chosen cloud, synced to your existing database, sized for your actual traffic
- Note explicitly that this replaces the quickstart's sandbox setup — flag where to retire/rotate the sandbox key

## 11. Next Steps

- Monitoring/observability setup for the production instance (if Quillrail has a separate doc for this)
- Security hardening (private networking, key rotation policy)
- Scaling runbook for when workload crosses from low- to high-volume mid-life
- Support channel / community link