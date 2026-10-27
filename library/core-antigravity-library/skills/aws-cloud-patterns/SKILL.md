---
name: aws-cloud-patterns
description: AWS Cloud Architecture and serverless design patterns. Use when architecting AWS solutions, writing Lambda functions, configuring S3 buckets, designing DynamoDB single-table schemas, setting up API Gateway, or enforcing IAM least-privilege policies.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0
category: backend-api
---

# AWS Cloud Patterns

> **Serverless Architecture, Least-Privilege IAM, S3 & DynamoDB Best Practices**

---

## 🏗️ Core Principles

| Principle | Rule |
|-----------|------|
| **IAM Least-Privilege** | Grant only the exact actions (`s3:GetObject`) on specific resource ARNs (`arn:aws:s3:::bucket/*`). Never use `Action: "*"` or `Resource: "*"`. |
| **Serverless Cold-Start Minimization** | Bundle Lambda functions with esbuild/rollup. Keep dependencies minimal and initialize DB clients outside the handler. |
| **S3 Security Baseline** | Enable Block Public Access, server-side encryption (SSE-KMS or SSE-S3), and versioning by default. |
| **Idempotent Lambda Handlers** | Design event handlers (SQS, SNS, EventBridge) to be idempotent to handle at-least-once delivery guarantees safely. |
| **Dead-Letter Queues (DLQs)** | Every asynchronous Lambda function must have a configured DLQ (SQS) to capture failed event payloads for inspection. |

---

## 📋 Production Lambda Handler Pattern (TypeScript)

```typescript
import { Context, APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';

// Initialize expensive resources OUTSIDE the handler (reused across warm invocations)
const dbConnection = initializeDatabase();

export async function handler(
  event: APIGatewayProxyEvent,
  context: Context
): Promise<APIGatewayProxyResult> {
  context.callbackWaitsForEmptyEventLoop = false;

  try {
    const body = event.body ? JSON.parse(event.body) : {};
    const result = await processOrder(body, dbConnection);

    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-store',
      },
      body: JSON.stringify({ success: true, data: result }),
    };
  } catch (err: any) {
    console.error('Handler invocation failed:', { error: err.message, requestId: context.awsRequestId });
    return {
      statusCode: err.statusCode || 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ error: err.message || 'Internal Server Error' }),
    };
  }
}
```

---

## ❌ Anti-Patterns

- ❌ Granting `AdministratorAccess` or wildcard `*` permissions to Lambda execution roles.
- ❌ Creating public S3 buckets without explicit CloudFront OAC (Origin Access Control).
- ❌ Connecting hundreds of serverless Lambda instances directly to relational databases without RDS Proxy.
