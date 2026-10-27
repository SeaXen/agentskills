---
name: typescript-expert
description: Modern TypeScript 5+ type system architecture, strict mode standards, type-level programming, generics, and performance optimization. Use when authoring complex types, eliminating type assertions, configuring strict tsconfigs, or debugging compile-time errors.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0
---

# TypeScript Expert

> **Advanced Type Systems, Zero-Any Policy & Type-Safe Architecture**

---

## 🏗️ Core Principles

| Principle | Rule |
|-----------|------|
| **Zero `any` Policy** | Never use `any`. Use `unknown` for unchecked runtime values and validate using narrowing or type guards (Zod, ArkType). |
| **Strict Compiler Flags** | `strict: true`, `noUncheckedIndexedAccess: true`, `exactOptionalPropertyTypes: true`. |
| **Discriminated Unions** | Model domain states as tagged unions (`{ status: 'success'; data: T } | { status: 'error'; error: Error }`). |
| **Type Inference Over Redundancy** | Let TypeScript infer primitive variables and return types where obvious; explicitly type public API boundaries. |
| **Immutability by Default** | Use `readonly` arrays, `as const`, and `Readonly<T>` to guard against unintended object mutation. |

---

## 📋 Common Advanced Patterns

### 1. Discriminated Union with Exhaustive Check
```typescript
type AppState =
  | { state: 'idle' }
  | { state: 'loading' }
  | { state: 'success'; data: string[] }
  | { state: 'error'; error: string };

function render(s: AppState) {
  switch (s.state) {
    case 'idle': return 'Ready';
    case 'loading': return 'Fetching...';
    case 'success': return `Items: ${s.data.length}`;
    case 'error': return `Failed: ${s.error}`;
    default: {
      const _exhaustiveCheck: never = s;
      return _exhaustiveCheck;
    }
  }
}
```

### 2. Branded Types for Safe Primitives
```typescript
declare const __brand: unique symbol;
type Brand<B> = { [__brand]: B };
export type Branded<T, B> = T & Brand<B>;

export type UserId = Branded<string, 'UserId'>;
export type OrderId = Branded<string, 'OrderId'>;

// Prevents accidentally passing OrderId to a function expecting UserId
```

---

## ❌ Anti-Patterns

- ❌ Type assertions via `as unknown as TargetType` to bypass the type checker.
- ❌ Non-null assertions (`!`) without runtime guard checks.
- ❌ Mutating arguments marked as readonly.
- ❌ Using `Function` or `{}` as generic object types instead of `Record<string, unknown>`.
