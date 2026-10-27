---
name: terraform-architect
description: Terraform Infrastructure as Code (IaC) architecture, state management, module design, and security linting. Use when authoring Terraform configurations, managing remote state backends, writing reusable modules, configuring providers, or preventing state drift.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0
---

# Terraform Architect

> **Infrastructure as Code, Remote State Management & Modular Cloud Provisioning**

---

## 🏗️ Core Principles

| Principle | Rule |
|-----------|------|
| **Remote State Locking** | Always store `.tfstate` in an encrypted remote backend with distributed state locking (e.g., S3 + DynamoDB table). |
| **Strict Module Boundaries** | Separate reusable modules (`modules/`) from root environment configurations (`environments/prod/`). |
| **Predictable Execution** | Always run `terraform plan -out=tfplan` before `terraform apply tfplan`. Never auto-apply in production without a plan file. |
| **No Hardcoded Secrets** | Inject secrets via secret managers (AWS Secrets Manager, HashiCorp Vault) or environment variables; never commit plaintext values. |
| **Blast Radius Isolation** | Split large state files by domain (networking, database, compute) rather than keeping entire infra in a single monolith state. |

---

## 📋 Standard Remote State Backend Configuration

```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = "company-tfstate-prod"
    key            = "services/api/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-locks"
  }
}
```

---

## 📋 Production Module Checklist

- [ ] Variable definitions include explicit `type`, `description`, and `validation` blocks where applicable.
- [ ] Outputs have meaningful descriptions and mark sensitive outputs (`sensitive = true`).
- [ ] Resources tagged with environment, owner, and cost-center tags.
- [ ] Run `terraform fmt -check` and `tflint` in CI before merge.

---

## ❌ Anti-Patterns

- ❌ Committing `.tfstate` or `.tfvars` containing secrets to version control.
- ❌ Running `terraform apply` without an audited `tfplan`.
- ❌ Monolithic state files spanning multiple unrelated microservices.
