<!-- Absorbed from the sibling skill 'prisma-expert' (D:\Repo\.agents\skills\prisma-expert\SKILL.md).
     Kept verbatim so this review skill stays self-contained.
     The sibling skill itself was NOT deleted. -->
---
name: prisma-expert
description: Prisma ORM architecture, schema design, and query optimization. Use when designing Prisma data models, handling zero-downtime migrations, optimizing relation queries, configuring connection pooling, and integrating Prisma with serverless edge runtimes.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0
---

# Prisma Expert

> **Data Modeling, Safe Migrations, Connection Pooling & High-Performance Querying**

---

## ðŸ—ï¸ Core Principles

| Principle | Rule |
|-----------|------|
| **Explicit Relations & Foreign Keys** | Always model relations explicitly with `@relation`, `onDelete`, and explicit index tags on foreign key columns. |
| **Safe Migrations** | Use `prisma migrate dev` locally. Use `prisma migrate deploy` in CI/CD. Never use `db push` in production. |
| **Avoid N+1 & Over-fetching** | Use `select` to retrieve only required fields. Avoid uncontrolled deep `include` trees. |
| **Connection Pooling** | In serverless/edge environments (e.g., Vercel, Cloudflare, Lambda), always use a connection pooler (PgBouncer, Prisma Accelerate, Neon Pooler). |
| **Singleton Client** | Maintain a single `PrismaClient` instance globally across hot-reloads to prevent connection exhaustion. |

---

## ðŸ“‹ Global Prisma Client Pattern (Next.js / Node.js)

```typescript
import { PrismaClient } from '@prisma/client';

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined;
};

export const prisma =
  globalForPrisma.prisma ??
  new PrismaClient({
    log: process.env.NODE_ENV === 'development' ? ['query', 'error', 'warn'] : ['error'],
  });

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma;
```

---

## ðŸ“‹ Schema Design Standards

- Always add `@id @default(cuid())` or `@default(uuid())` for scalable IDs.
- Index foreign key lookup columns: `@@index([userId])`.
- Define explicit compound unique constraints where needed: `@@unique([tenantId, email])`.
- Use enum types for finite state machines rather than raw strings.

---

## âŒ Anti-Patterns

- âŒ Calling `new PrismaClient()` inside request handlers or middleware.
- âŒ Running `prisma db push` in production pipelines (risks silent data loss).
- âŒ Using `findMany()` without pagination limits (`take`, `skip` / cursor).
- âŒ Performing sequential queries in loops instead of `prisma.$transaction()` or batch `findMany({ where: { id: { in: ids } } })`.

