---
name: nestjs-expert
description: Enterprise NestJS backend architecture, dependency injection, modular systems, guards, interceptors, pipes, microservices, and testing. Use when building scalable NestJS services, structuring modules, configuring auth guards, or integrating Swagger OpenAPI.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0
category: testing-qa
---

# NestJS Expert

> **Enterprise Backend Architecture, Modular Systems & Clean Dependency Injection**

---

## 🏗️ Core Principles

| Principle | Rule |
|-----------|------|
| **Strict Modularity** | Feature-driven modules (`UsersModule`, `AuthModule`) encapsulating controllers, services, and repositories. Export only public providers. |
| **Dependency Injection** | Program to interfaces/abstractions. Inject services via constructor parameter decorators. |
| **Data Validation Pipeline** | Apply `ValidationPipe` globally with `whitelist: true`, `forbidNonWhitelisted: true`, and `transform: true` using `class-validator`. |
| **Cross-Cutting Concerns** | Use Guards for auth/permissions, Interceptors for response mapping/logging, and Exception Filters for standardized error envelopes. |
| **Config Validation** | Validate `@nestjs/config` environment schemas at boot time using Joi or Zod. |

---

## 📋 Standard Architecture Pipeline

```text
Request
  └── Global Middlewares (CORS, Helmet, RateLimiting)
       └── Guards (JwtAuthGuard, RolesGuard)
            └── Interceptors (Pre-Controller: Timing, Logging)
                 └── Pipes (ValidationPipe, ParseUUIDPipe)
                      └── Controller Action
                           └── Domain Service / Repository
                      └── Exception Filters (Catch & Format)
            └── Interceptors (Post-Controller: Response Transformation)
  └── Response
```

---

## 📋 Production Module Example

```typescript
import { Module } from '@nestjs/common';
import { UsersController } from './users.controller';
import { UsersService } from './users.service';
import { PrismaModule } from '../prisma/prisma.module';

@Module({
  imports: [PrismaModule],
  controllers: [UsersController],
  providers: [UsersService],
  exports: [UsersService],
})
export class UsersModule {}
```

---

## ❌ Anti-Patterns

- ❌ Instantiating services directly with `new UsersService()` instead of constructor injection.
- ❌ Circular module dependencies (avoiding `forwardRef()` unless strictly unavoidable).
- ❌ Putting business/database logic directly inside Controller methods.
- ❌ Skipping DTO validation, accepting raw untyped `req.body`.
